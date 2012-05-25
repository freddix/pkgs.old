# $Id: TLMedia.pm 11549 2008-12-07 16:52:59Z karl $
# TeXLive::TLMedia.pm - module for accessing TeX Live Media
# Copyright 2008 Norbert Preining
#
# This file is licensed under the GNU General Public License version 2
# or any later version.

package TeXLive::TLMedia;

use TeXLive::TLConfig;
use TeXLive::TLPostActions;
use TeXLive::TLUtils qw(copy win32 dirname mkdirhier basename download_file
                        merge_into debug ddebug info tlwarn);
use TeXLive::TLPDB;

sub new
{
  my ($class, $location) = @_;
  my $media;
  my $self = { };
  # of no argument is given we assume NET and default URL
  if (!defined($location)) {
    return;
  }
  # no default by itself ...
  # $location = "$TeXLiveURL" unless (defined($location));
  # do media autodetection
  if ($location =~ m,http://|ftp://,) {
    $media = 'NET';
  } else {
    if ($location =~ m,file://*(.*)$,) {
      $location = "/$1";
    }
    if (-d "$location/texmf/web2c") {
      $media = 'DVD';
    } elsif (-d "$location/$Archive") {
      $media = 'CD';
    } else {
      # we cannot find the right type, return undefined, that should
      # make people notice
      return;
    }
  }
  debug("Loading $location/$InfraLocation/$DatabaseName ...\n");
  my $tlpdb = TeXLive::TLPDB->new(root => "$location");
  return(undef) unless defined($tlpdb);
  my (@all_c, @std_c, @lang_c, @lang_doc_c);
  my (@schemes);
  my %revs;
  foreach my $pkg ($tlpdb->list_packages) {
    my $tlpobj = $tlpdb->{'tlps'}{$pkg};
    $revs{$tlpobj->name} = $tlpobj->revision;
    if ($tlpobj->category eq "Collection") {
      push @all_c, $pkg;
      if ($pkg =~ /collection-lang/) {
        push @lang_c, $pkg;
      } elsif ($pkg =~ /documentation/) {
        if ($pkg =~ /documentation-base/) {
          push @std_c, $pkg;
        } else {
          push @lang_doc_c, $pkg;
        }
      } else {
        push @std_c, $pkg;
      }
    } elsif ($tlpobj->category eq "Scheme") {
      push @schemes, $pkg;
    }
  }
  my (@systems);
  @systems = $tlpdb->available_architectures;
  $self->{'media'} = $media;
  $self->{'location'} = $location;
  $self->{'tlpdb'} = $tlpdb;
  $self->{'release'} = $tlpdb->config_release;
  @{ $self->{'all_collections'} } = @all_c;
  @{ $self->{'std_collections'} } = @std_c;
  @{ $self->{'lang_collections'} } = @lang_c;
  @{ $self->{'lang_doc_collections'} } = @lang_doc_c;
  @{ $self->{'schemes'} } = @schemes;
  @{ $self->{'systems'} } = @systems;
  %{ $self->{'pkgrevs'} } = %revs;
  bless $self, $class;
  return $self;
}

# returns a scalar (0) on error
# returns a reference to a hash with actions on success
sub install_package {
  my ($self, $pkg, $totlpdb, $nopostinstall, $fallbackmedia) = @_;
  my $fromtlpdb = $self->tlpdb;
  my $ret;
  die("TLMedia not initialized, cannot find tlpdb!") unless (defined($fromtlpdb));
  my $tlpobj = $fromtlpdb->get_package($pkg);
  if (!defined($tlpobj)) {
    if (defined($fallbackmedia)) {
      if ($ret = $fallbackmedia->install_package($pkg,$totlpdb, $nopostinstall)) {
        debug("installed $pkg from fallback\n");
        return $ret;
      } else {
        tlwarn("$0: Cannot find package $pkg (in fallback, either)\n");
        return 0;
      }
    } else {
      tlwarn("$0: Cannot find package $pkg\n");
      return 0;
    }
  } else {
    my $container_src_split = $fromtlpdb->config_src_container;
    my $container_doc_split = $fromtlpdb->config_doc_container;
    # get options about src/doc splitting from $totlpdb
    my $opt_src = $totlpdb->option_install_srcfiles;
    my $opt_doc = $totlpdb->option_install_docfiles;
    my $real_opt_doc = $opt_doc;
    if ($tlpobj->category =~ m/documentation/i) {
      # we do install documenation files for category Documentation
      # even if opt_doc is false
      $real_opt_doc = 1;
    }
    my $container;
    my @installfiles;
    my $location = $self->location;
    foreach ($tlpobj->runfiles) {
      # s!^!$location/!;
      push @installfiles, $_;
    }
    foreach ($tlpobj->allbinfiles) {
      # s!^!$location/!;
      push @installfiles, $_;
    }
    if ($opt_src) {
      foreach ($tlpobj->srcfiles) {
        # s!^!$location/!;
        push @installfiles, $_;
      }
    }
    if ($real_opt_doc) {
      foreach ($tlpobj->docfiles) {
        # s!^!$location/!;
        push @installfiles, $_;
      }
    }
    my $media = $self->media;
    if ($media eq 'DVD') {
      $container = \@installfiles;
    } elsif ($media eq 'CD') {
      if (-r "$location/$Archive/$pkg.zip") {
        $container = "$location/$Archive/$pkg.zip";
      } elsif (-r "$location/$Archive/$pkg.tar.lzma") {
        $container = "$location/$Archive/$pkg.tar.lzma";
      } else {
        tlwarn("Cannot find a package $pkg (.zip or .lzma) in $location/$Archive\n");
        next;
      }
    } elsif (&media eq 'NET') {
      $container = "$location/$Archive/$pkg.$DefaultContainerExtension";
    }
    $self->_install_package($container,\@installfiles,$totlpdb) || return(0);
    # if we are installing from CD or NET we have to fetch the respective
    # source and doc packages $pkg.source and $pkg.doc and install them, too
    if (($media eq 'NET') || ($media eq 'CD')) {
      # we install split containers under the following conditions:
      # - the container were split generated
      # - src/doc files should be installed
      # (- the package is not already a split one (like .i386-linux))
      # the above test has been removed because it would mean that
      #   texlive.infra.doc.tar.lzma
      # will never be installed, and we do already check that there
      # are at all src/doc files, which in split packages of the form 
      # foo.ARCH are not present. And if they are present, than that is fine,
      # too (bin-foobar.win32.doc.tar.lzma)
      # - there are actually src/doc files present
      if ($container_src_split && $opt_src && $tlpobj->srcfiles) {
        my $srccontainer = $container;
        $srccontainer =~ s/(\.tar\.lzma|\.zip)$/.source$1/;
        $self->_install_package($srccontainer,\@installfiles,$totlpdb) || return(0);
      }
      if ($container_doc_split && $real_opt_doc && $tlpobj->docfiles) {
        my $doccontainer = $container;
        $doccontainer =~ s/(\.tar\.lzma|\.zip)$/.doc$1/;
        $self->_install_package($doccontainer,\@installfiles,$totlpdb) || return(0);
      }
    }
    # we don't want to have wrong information in the tlpdb, so remove the
    # src/doc files if they are not installed ...
    if (!$opt_src) {
      $tlpobj->clear_srcfiles;
    }
    if (!$real_opt_doc) {
      $tlpobj->clear_docfiles;
    }
    # we have to write out the tlpobj file since it is contained in the
    # archives (.tar.lzma) but at DVD install time we don't have them
    my $tlpod = $totlpdb->root . "/tlpkg/tlpobj";
    mkdirhier( $tlpod );
    open(TMP,">$tlpod/".$tlpobj->name.".tlpobj") or
      die("Cannot open tlpobj file for ".$tlpobj->name);
    $tlpobj->writeout(\*TMP);
    close(TMP);
    $totlpdb->add_tlpobj($tlpobj);
    $totlpdb->save;
    # compute the return value
    my %ret;
    merge_into(\%ret, $tlpobj->make_return_hash_from_executes("enable"));
    if (!$nopostinstall) {
      # do the postinstallation actions
      if (defined($PostInstall{$pkg})) {
        info("running post install action for $pkg\n");
        &{$PostInstall{$pkg}}($totlpdb->root);
      }
    }
    return \%ret;
  }
}

#
# _install_package
# actually does the installation work
# returns 1 on success and 0 on error
#
sub _install_package {
  my ($self, $what, $filelistref, $totlpdb) = @_;

  my $media = $self->media;
  my $target = $totlpdb->root;

  my @filelist = @$filelistref;

  # we assume that $::progs has been set up!
  my $wget = $::progs{'wget'};
  my $lzmadec = $::progs{'lzmadec'};
  if (!defined($wget) || !defined($lzmadec)) {
    tlwarn("_install_package: programs not set up properly, strange.\n");
    return(0);
  }

  if (ref $what) {
    # we are getting a ref to a list of files, so install from DVD
    my $location = $self->location;
    foreach my $file (@$what) {
      # @what is taken, not @filelist!
      # is this still needed?
      my $dn=dirname($file);
      mkdirhier("$target/$dn");
      copy "$location/$file", "$target/$dn";
    }
    # we always assume that copy will work
    return(1);
  } elsif ($what =~ m,\.tar(\.lzma)?$,) {
    my $type = defined($1) ? "lzma" : "tar";
      
    # this is the case when we install from CD or the NET, or a backup
    #
    # in all other cases we create temp files .tar.lzma (or use the present
    # one), lzmadec them, and then call tar

    my $fn = basename($what);
    mkdirhier("$target/temp");
    my $tarfile;
    my $remove_tarfile = 1;
    if ($type eq "lzma") {
      my $lzmafile = "$target/temp/$fn";
      $tarfile  = "$target/temp/$fn"; $tarfile =~ s/\.lzma$//;
      my $lzmafile_quote = $lzmafile;
      my $tarfile_quote = $tarfile;
      my $target_quote = $target;
      if (win32()) {
        $lzmafile =~ s!/!\\!g;
        $lzmafile_quote = "\"$lzmafile\"";
        $tarfile =~ s!/!\\!g;
        $tarfile_quote = "\"$tarfile\"";
        $target =~ s!/!\\!g;
        $target_quote = "\"$target\"";
      }
      if ($what =~ m,http://|ftp://,) {
        # we are installing from the NET
        # download the file and put it into temp
        if (!download_file($what, $lzmafile) || (! -r $lzmafile)) {
          tlwarn("Downloading \n");
          tlwarn("   $what\n");
          tlwarn("did not succeed, please retry.\n");
          unlink($tarfile, $lzmafile);
          return(0);
        }
      } else {
        # we are installing from CD
        # copy it to temp
        copy($what, "$target/temp");
      }
      debug("un-lzmaing $lzmafile to $tarfile\n");
      system("$lzmadec < $lzmafile_quote > $tarfile_quote");
      if (! -f $tarfile) {
        tlwarn("_install_package: Unpacking $lzmafile failed, please retry.\n");
        unlink($tarfile, $lzmafile);
        return(0);
      }
      unlink($lzmafile);
    } else {
      $tarfile = "$target/temp/$fn";
      if ($what =~ m,http://|ftp://,) {
        if (!download_file($what, $tarfile) || (! -r $tarfile)) {
          tlwarn("Downloading \n");
          tlwarn("   $what\n");
          tlwarn("failed, please retry.\n");
          unlink($tarfile);
          return(0);
        }
      } else {
        $tarfile = $what;
        $remove_tarfile = 0;
      }
    }
    return TeXLive::TLUtils::untar($tarfile, $target, $remove_tarfile);
  } else {
    tlwarn("_install_package: Don't know how to install $what\n");
    return(0);
  }
}



# member access functions
#
sub media { my $self = shift ; return $self->{'media'}; }
sub location { my $self = shift ; return $self->{'location'}; }
sub tlpdb { my $self = shift ; return $self->{'tlpdb'}; }
sub release { my $self = shift ; return $self->{'release'}; }
sub all_collections { my $self = shift; return @{ $self->{'all_collections'} }; }
sub std_collections { my $self = shift; return @{ $self->{'std_collections'} }; }
sub lang_collections { my $self = shift; return @{ $self->{'lang_collections'} }; }
sub lang_doc_collections { my $self = shift; return @{ $self->{'lang_doc_collections'} }; }
sub schemes { my $self = shift; return @{ $self->{'schemes'} }; }
sub systems { my $self = shift; return @{ $self->{'systems'} }; }

1;
__END__


=head1 NAME

C<TeXLive::TLMedia> -- TeX Live Media module

=head1 SYNOPSIS

  use TeXLive::TLMedia;

  my $tlnet = TeXLive::TLMedia->new('NET');
  my $tlneo = TeXLive::TLMedia->new('NET','http://www.ctan.org/mirror/tl/');
  my $tlcd  = TeXLive::TLMedia->new('CD','/mnt/tl-cd/');
  my $tldvd = TeXLive::TLMedia->new('DVD','/mnt/tl-dvd/');

=head1 DESCRIPTION

missing

=head1 MEMBER ACCESS FUNCTIONS

scalars: media, location, tlpdb, release
lists: all_collections, std_collections, lang_collections, lang_doc_collections,
schemes, systems

=back

=head1 SEE ALSO

The modules L<TeXLive::TLConfig>, L<TeXLive::TLUtils>, L<TeXLive::TLPOBJ>, 
L<TeXLive::TLPDB>, L<TeXLive::TLTREE>.

=head1 AUTHORS AND COPYRIGHT

This script and its documentation were written for the TeX Live
distribution (L<http://tug.org/texlive>) and both are licensed under the
GNU General Public License Version 2 or later.

=cut

### Local Variables:
### perl-indent-level: 2
### tab-width: 2
### indent-tabs-mode: nil
### End:
# vim:set tabstop=2 expandtab: #
