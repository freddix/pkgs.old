# $Id: TLPOBJ.pm 12320 2009-03-05 23:36:22Z karl $
# TeXLive::TLPOBJ.pm - module for using tlpobj files
# Copyright 2007, 2008, 2009 Norbert Preining
# This file is licensed under the GNU General Public License version 2
# or any later version.

package TeXLive::TLPOBJ;

use TeXLive::TLConfig qw($DefaultCategory $CategoriesRegexp $MetaCategoriesRegexp $InfraLocation);
use TeXLive::TLUtils;
use TeXLive::TLTREE;

our $_tmp;
my $_containerdir;

sub new {
  my $class = shift;
  my %params = @_;
  my $self = {
    name        => $params{'name'},
    category    => defined($params{'category'}) ? $params{'category'} : $DefaultCategory,
    shortdesc   => $params{'shortdesc'},
    longdesc    => $params{'longdesc'},
    catalogue   => $params{'catalogue'},
    runfiles    => defined($params{'runfiles'}) ? $params{'runfiles'} : [],
    runsize   => $params{'runsize'},
    srcfiles    => defined($params{'srcfiles'}) ? $params{'srcfiles'} : [],
    srcsize   => $params{'srcsize'},
    docfiles    => defined($params{'docfiles'}) ? $params{'docfiles'} : [],
    docsize   => $params{'docsize'},
    executes    => defined($params{'executes'}) ? $params{'executes'} : [],
    # note that binfiles is a HASH with keys of $arch!
    binfiles    => defined($params{'binfiles'}) ? $params{'binfiles'} : {},
    binsize     => defined($params{'binsize'}) ? $params{'binsize'} : {},
    depends     => defined($params{'depends'}) ? $params{'depends'} : [],
    revision    => $params{'revision'},
    cataloguedata   => defined($params{'cataloguedata'}) ? $params{'cataloguedata'} : {},
  };
  $_containerdir = $params{'containerdir'} if defined($params{'containerdir'});
  bless $self, $class;
  return $self;
}



sub copy {
  my $self = shift;
  my $bla = {};
  %$bla = %$self;
  bless $bla, "TeXLive::TLPOBJ";
  return $bla;
}



sub from_file {
  my $self = shift;
  if (@_ != 1) {
    die("TLPOBJ:from_file: Need a filename for initialization");
  }
  open(TMP,"<$_[0]") || die("Cannot open tlpobj file: $_[0]");
  $self->from_fh(\*TMP);
}

sub from_fh {
  my ($self,$fh,$multi) = @_;
  my $started = 0;
  my $lastcmd = "";
  my $arch;
  my $size;

  #while (my $line = $fh->getline) {
  while (my $line = <$fh>) {
    chomp($line);
    # we call tllog only when something will be logged, to speed things up.
    # this is the inner loop bounding the time to read tlpdb.
    dddebug("reading line: >>>$line<<<\n") if ($::opt_verbosity >= 3);
    $line =~ /^\s*#/ && next;          # skip comment lines
    if ($line =~ /^\s*$/o) {
      if (!$started) { next; }
      if (defined($multi)) {
        # we may read from a tldb file
        return 1;
      } else {
        # we are reading one tldb file, nothing else allowed
        die("No empty line allowed within tlpobj files!");
      }
    }
    if ($line =~ /^ /o) {
      if ( ($lastcmd eq "runfiles") ||
           ($lastcmd eq "binfiles") ||
           ($lastcmd eq "docfiles") ||
           ($lastcmd eq "srcfiles") ||
           ($lastcmd eq "executes") ||
           ($lastcmd eq "depend") ) {
        $line =~ s/^ /${lastcmd}continued /;
      } else {
        die("Continuation of $lastcmd not allowed, please fix tlpobj: line = $line!\n");
      }
    }
    if ($line =~ /^name\s*([-.\w]+)/o) {
      $name = "$1";
      $lastcmd = "name";
      $self->name("$name");
      $started && die("Cannot have two name directives: $line!");
      $started = 1;
    } else {
      $started || die("First directive needs to be 'name', not $line");
      if ($line =~ /^(src|run)filescontinued\s+(.*)\s*/o) {
        push @{$self->{$1."files"}}, "$2";
        next;
      } elsif ($line =~ /^docfilescontinued\s+(.*)\s*/o) {
        # docfiles can have tags, but the quotewords function is so
        # time intense that we try to call it only when necessary
        my ($f, $rest) = split(' ', "$1", 2);
        my @words;
        if (defined $rest) {
          @words = &TeXLive::TLUtils::quotewords('\s+', 0, "$rest");
        }
        push @{$self->{'docfiles'}}, $f;
        while (@words) {
          $_ = shift @words;
          if (/^details=(.*)$/) {
            $self->{'docfiledata'}{$f}{'details'} = "$1";
          } elsif (/^language=(.*)$/) {
            $self->{'docfiledata'}{$f}{'language'} = "$1";
          } else {
            die "Unknown docfile tag: $line";
          }
        }
        next;
      } elsif ($line =~ /^binfilescontinued\s+(.*)\s*/o) {
        push @{$self->{'binfiles'}{$arch}}, "$1";
        next;
      } elsif ($line =~ /^binfiles\s+/o) {
        my @words = split ' ',$line;
        # first entry is "binfiles", shift it away
        shift @words;
        while (@words) {
          $_ = shift @words;
          if (/^arch=(.*)$/) {
            $arch=$1;
          } elsif (/^size=(.*)$/) {
            $size=$1;
          } else {
            die "Unknown tag: $line";
          }
        }
        if (defined($size)) {
          $self->{'binsize'}{$arch} = $size;
        }
        $lastcmd = "binfiles";
        next;
      } elsif ($line =~ /^longdesc\s+(.*)\s*/o) {
        if (defined($self->{'longdesc'})) {
          $self->{'longdesc'} .= " $1";
        } else {
          $self->{'longdesc'} = "$1";
        }
        $lastcmd = "longdesc";
        next;
      } elsif ($line =~ /^category\s+$CategoriesRegexp/o) {
        $self->{'category'} = "$1";
        $lastcmd = "category";
        next;
      } elsif ($line =~ /^revision\s+(.*)\s*/o) {
        $self->{'revision'} = "$1";
        $lastcmd = "revision";
        next;
      } elsif ($line =~ /^containersize\s+([0-9]+)\s*/o) {
        $self->containersize("$1");
        $lastcmd = "containersize";
        next;
      } elsif ($line =~ /^srccontainersize\s+([0-9]+)\s*/o) {
        $self->srccontainersize("$1");
        $lastcmd = "srccontainersize";
        next;
      } elsif ($line =~ /^doccontainersize\s+([0-9]+)\s*/o) {
        $self->doccontainersize("$1");
        $lastcmd = "doccontainersize";
        next;
      } elsif ($line =~ /^containermd5\s+([a-f0-9]+)\s*/o) {
        $self->containermd5("$1");
        $lastcmd = "containermd5";
        next;
      } elsif ($line =~ /^srccontainermd5\s+([a-f0-9]+)\s*/o) {
        $self->srccontainermd5("$1");
        $lastcmd = "srccontainermd5";
        next;
      } elsif ($line =~ /^doccontainermd5\s+([a-f0-9]+)\s*/o) {
        $self->doccontainermd5("$1");
        $lastcmd = "doccontainermd5";
        next;
      } elsif ($line =~ /^catalogue\s+(.*)\s*/o) {
        $self->catalogue("$1");
        $lastcmd = "catalogue";
        next;
      } elsif ($line =~ /^(doc|src|run)files\s+/o) {
        my $type = $1;
        my @words = split ' ',$line;
        # first entry is "XXXfiles", shift it away
        $lastcmd = shift @words;
        while (@words) {
          $_ = shift @words;
          if (/^size=(.*)$/) {
            $size=$1;
          } else {
            die "Unknown tag: $line";
          }
        }
        if (defined($size)) {
          $self->{"${type}size"} = $size;
        }
        next;
      } elsif ($line =~ /^execute(continued)?\s*(.*)\s*/o) {
        push @{$self->{'executes'}}, "$2" unless "$2" eq "";
        $lastcmd = "execute";
        next;
      } elsif ($line =~ /^depend(continued)?\s*(.*)\s*/o) {
        push @{$self->{'depends'}}, "$2" unless "$2" eq "";
        $lastcmd = "depend";
        next;
      } elsif ($line =~ /^catalogue-([^\s]+)\s+(.*)\s*/o) {
        $self->{'cataloguedata'}{$1} = "$2";
      } elsif ($line =~ /^catalogue-([^\s]+)\s*/o) {
        1; # ignore e.g. catalogue-ctan without parameter
      } elsif ($line =~ /^shortdesc\s+(.*)\s*/o) {
        $self->{'shortdesc'} .= "$1";
        $lastcmd = "shortdesc";
        next;
      } else {
        die("Unknown directive ...$line... , please fix it!");
      }
    }
  }
  return $started;
}

sub recompute_revision {
  my ($self,$tltree, $revtlpsrc) = @_;
  my @files = $self->all_files;
  my $filemax = 0;
  foreach my $f (@files) {
    $filemax = $tltree->file_svn_lastrevision($f);
    $self->revision(($filemax > $self->revision) ? $filemax : $self->revision);
  }
  if (defined($revtlpsrc)) {
    if ($self->revision < $revtlpsrc) {
      $self->revision($revtlpsrc);
    }
  }
}

sub recompute_sizes {
  my ($self,$tltree) = @_;
  $self->{'docsize'} = $self->_recompute_size("doc",$tltree);
  $self->{'srcsize'} = $self->_recompute_size("src",$tltree);
  $self->{'runsize'} = $self->_recompute_size("run",$tltree);
  foreach $a ($tltree->architectures) {
    $self->{'binsize'}{$a} = $self->_recompute_size("bin",$tltree,$a);
  }
}


sub _recompute_size {
  my ($self,$type,$tltree,$arch) = @_;
  my $nrivblocks = 0;
  if ($type eq "bin") {
    my %binfiles = %{$self->{'binfiles'}};
    if (defined($binfiles{$arch})) {
      foreach $f (@{$binfiles{$arch}}) {
        my $s = $tltree->size_of($f);
        $nrivblocks += int($s/$TeXLive::TLConfig::BlockSize);
        $nrivblocks++ if (($s%$TeXLive::TLConfig::BlockSize) > 0);
      }
    }
  } else {
    if (defined($self->{"${type}files"}) && (@{$self->{"${type}files"}})) {
      foreach $f (@{$self->{"${type}files"}}) {
        my $s = $tltree->size_of($f);
        if (defined($s)) {
          $nrivblocks += int($s/$TeXLive::TLConfig::BlockSize);
          $nrivblocks++ if (($s%$TeXLive::TLConfig::BlockSize) > 0);
        } else {
          printf STDERR "size for $f not defined, strange ...\n";
        }
      }
    }
  }
  return $nrivblocks;
}

sub writeout {
  my $self = shift;
  my $fd = (@_ ? $_[0] : STDOUT);
  print $fd "name ", $self->name, "\n";
  print $fd "category ", $self->category, "\n";
  defined($self->{'revision'}) && print $fd "revision $self->{'revision'}\n";
  defined($self->{'catalogue'}) && print $fd "catalogue $self->{'catalogue'}\n";
  defined($self->{'shortdesc'}) && print $fd "shortdesc $self->{'shortdesc'}\n";
  defined($self->{'license'}) && print $fd "license $self->{'license'}\n";
  # ugly hack to get rid of use FileHandle; see man perlform
  #format_name $fd "multilineformat";
  select((select($fd),$~ = "multilineformat")[0]);
  if (defined($self->{'longdesc'})) {
    $_tmp = "$self->{'longdesc'}";
    write $fd;
  }
  if (defined($self->{'depends'})) {
    foreach (@{$self->{'depends'}}) {
      print $fd "depend $_\n";
    }
  }
  if (defined($self->{'executes'})) {
    foreach (@{$self->{'executes'}}) {
      print $fd "execute $_\n";
    }
  }
  if (defined($self->{'containersize'})) {
    print $fd "containersize $self->{'containersize'}\n";
  }
  if (defined($self->{'containermd5'})) {
    print $fd "containermd5 $self->{'containermd5'}\n";
  }
  if (defined($self->{'doccontainersize'})) {
    print $fd "doccontainersize $self->{'doccontainersize'}\n";
  }
  if (defined($self->{'doccontainermd5'})) {
    print $fd "doccontainermd5 $self->{'doccontainermd5'}\n";
  }
  if (defined($self->{'docfiles'}) && (@{$self->{'docfiles'}})) {
    print $fd "docfiles size=$self->{'docsize'}\n";
    foreach my $f (sort @{$self->{'docfiles'}}) {
      print $fd " $f";
      if (defined($self->{'docfiledata'}{$f}{'details'})) {
        print $fd ' details="', $self->{'docfiledata'}{$f}{'details'}, '"';
      }
      if (defined($self->{'docfiledata'}{$f}{'language'})) {
        print $fd ' language="', $self->{'docfiledata'}{$f}{'language'}, '"';
      }
      print $fd "\n";
    }
  }
  if (defined($self->{'srccontainersize'})) {
    print $fd "srccontainersize $self->{'srccontainersize'}\n";
  }
  if (defined($self->{'srccontainermd5'})) {
    print $fd "srccontainermd5 $self->{'srccontainermd5'}\n";
  }
  if (defined($self->{'srcfiles'}) && (@{$self->{'srcfiles'}})) {
    print $fd "srcfiles size=$self->{'srcsize'}\n";
    foreach (sort @{$self->{'srcfiles'}}) {
      print $fd " $_\n";
    }
  }
  if (defined($self->{'runfiles'}) && (@{$self->{'runfiles'}})) {
    print $fd "runfiles size=$self->{'runsize'}\n";
    foreach (sort @{$self->{'runfiles'}}) {
      print $fd " $_\n";
    }
  }
  foreach my $arch (sort keys %{$self->{'binfiles'}}) {
    if (@{$self->{'binfiles'}{$arch}}) {
      print $fd "binfiles arch=$arch size=", $self->{'binsize'}{$arch}, "\n";
      foreach (sort @{$self->{'binfiles'}{$arch}}) {
        print $fd " $_\n";
      }
    }
  }
  # writeout all the catalogue keys
  foreach my $k (sort keys %{$self->cataloguedata}) {
    print $fd "catalogue-$k ", $self->cataloguedata->{$k}, "\n";
  }
}

sub writeout_simple {
  my $self = shift;
  my $fd = (@_ ? $_[0] : STDOUT);
  print $fd "name ", $self->name, "\n";
  print $fd "category ", $self->category, "\n";
  if (defined($self->{'depends'})) {
    foreach (@{$self->{'depends'}}) {
      print $fd "depend $_\n";
    }
  }
  if (defined($self->{'executes'})) {
    foreach (@{$self->{'executes'}}) {
      print $fd "execute $_\n";
    }
  }
  if (defined($self->{'docfiles'}) && (@{$self->{'docfiles'}})) {
    print $fd "docfiles\n";
    foreach (sort @{$self->{'docfiles'}}) {
      print $fd " $_\n";
    }
  }
  if (defined($self->{'srcfiles'}) && (@{$self->{'srcfiles'}})) {
    print $fd "srcfiles\n";
    foreach (sort @{$self->{'srcfiles'}}) {
      print $fd " $_\n";
    }
  }
  if (defined($self->{'runfiles'}) && (@{$self->{'runfiles'}})) {
    print $fd "runfiles\n";
    foreach (sort @{$self->{'runfiles'}}) {
      print $fd " $_\n";
    }
  }
  foreach my $arch (sort keys %{$self->{'binfiles'}}) {
    if (@{$self->{'binfiles'}{$arch}}) {
      print $fd "binfiles arch=$arch\n";
      foreach (sort @{$self->{'binfiles'}{$arch}}) {
        print $fd " $_\n";
      }
    }
  }
}


sub make_container
{
  my ($self,$type,$instroot,$destdir,$containername,$relative) = @_;
  if (($type ne "lzma") && ($type ne "tar")) {
    die "$0: TLPOBJ supports tar and lzma containers, not $type";
  }
  if (!defined($containername)) {
    $containername = $self->name;
  }
  my @files = ();
  my $compresscmd;
  my $tlpobjdir = "$InfraLocation/tlpobj";
  my %binf = %{$self->{'binfiles'}};
  foreach (keys %binf) {
    push @files, @{$binf{$_}};
  }
  push @files, $self->runfiles;
  push @files, $self->docfiles;
  push @files, $self->srcfiles;
  @files = TeXLive::TLUtils::sort_uniq(@files);
  # we do relative packages ONLY if the files do NOT span multiple
  # texmf trees. check this here
  my $tltree;
  if ($relative) {
    foreach (@files) {
      my $tmp;
      ($tmp) = split m@/@;
      if (defined($tltree) && ($tltree ne $tmp)) {
        die ("$0: package $containername spans multiple trees, "
             . "relative generation not allowed");
      } else {
        $tltree = $tmp;
      }
    }
    my @nf;
    map { s@^$tltree/@@ ; push @nf, $_; } @files;
    @files = @nf;
  }
  # load Cwd only if necessary ...
  require Cwd;
  my $cwd = &Cwd::getcwd;
  if ("$destdir" !~ m@^(.:)?/@) {
    # we have an relative containerdir, so we have to make it absolute
    $destdir = "$cwd/$destdir";
  }
  &TeXLive::TLUtils::mkdirhier("$destdir");
  chdir($instroot);
  # in the relative case we have to chdir to the respective tltree
  # and put the tlpobj into the root!
  if ($relative) {
    chdir("./$tltree");
    $tlpobjdir = ".";
  }
  # we add the .tlpobj into the .tlpobj directory
  my $removetlpobjdir = 0;
  if (! -d "$tlpobjdir") {
    &TeXLive::TLUtils::mkdirhier("$tlpobjdir");
    $removetlpobjdir = 1;
  }
  open(TMP,">$tlpobjdir/$self->{'name'}.tlpobj") 
  || die "$0: create($tlpobjdir/$self->{'name'}.tlpobj) failed: $!";
  $self->writeout(\*TMP);
  close(TMP);
  push(@files, "$tlpobjdir/$self->{'name'}.tlpobj");
  $tarname = "$containername.tar";
  if ($type eq "tar") {
    $containername = $tarname;
  } else {
    $containername = "$tarname.lzma";
  }

  # start the fun
  my $tar = $::progs{'tar'};
  my $lzma;
  if (!defined($tar)) {
    tlwarn("$0: programs not set up, trying \"tar\".\n");
    $tar = "tar";
  }
  if ($type eq "lzma") {
    $lzma = $::progs{'lzma'};
    if (!defined($lzma)) {
      tlwarn("$0: programs not set up, trying \"lzma\".\n");
      $lzma = "lzma";
    }
  }
  
  # No owner/group options if we are being called on a user's machine to
  # make a backup.  We only want these when we are making the master
  # containers for tlnet.  Also exclude .svn directories when making the
  # masters.  We determine user vs. master by whether there's a revision
  # suffix in the container name.
  my @attrs = $containername =~ /\.r[0-9]/
              ? () : ("--owner", "0", "--group", "0", "--exclude", ".svn");
  my @cmdline = ($tar, "-cf", "$destdir/$tarname", @attrs);

  # Get list of files and symlinks to back up.  Nothing else should be
  # in the list.
  my @files_to_backup = ();
  for my $f (@files) {
    if (-f $f || -l $f) {
      push(@files_to_backup, $f);
    } elsif (! -e $f) {
      tlwarn("$0: (make_container $containername) $f does not exist\n");
    } else {
      tlwarn("$0: (make_container $containername) $f not file or symlink\n");
    }
  }
  
  my $tartempfile = "";
  if (win32()) {
    # Since we provide our own (GNU) tar on Windows, we know it has -T.
    my $tmpdir = TeXLive::TLUtils::get_system_tmpdir();
    $tartempfile = "$tmpdir/mc$$";
    open(TMP, ">$tartempfile") || die "open(>$tartempfile) failed: $!";
    print TMP map { "$_\n" } @files_to_backup;
    close(TMP) || warn "close(>$tartempfile) failed: $!";
    push(@cmdline, "-T", $tartempfile);
  } else {
    # For Unix, we pass all the files on the command line, because there
    # is no portable (across different platforms and different tars)  way
    # to pass them on stdin.  Unfortunately, this can be too lengthy of
    # a command line -- our biggest package is tex4ht, which needs about
    # 200k.  CentOS 5.2, at least, starts complaining around 140k.
    # 
    # Therefore, if the command is likely to be too long, we call
    # our collapse_dirs routine; in practice, this eliminates
    # essentially all the individual files, leaving just a few
    # directories, which is no problem.  (For example, tex4ht collapses
    # down to five directories and one file.)
    # 
    # Although in principle we could do this in all cases, collapse_dirs
    # isn't the most thoroughly tested function in the world.  It seems
    # safer to only do it in the (few) potentially problematic cases.
    # 
    if (length ("@files_to_backup") > 50000) {
      @files_to_backup = TeXLive::TLUtils::collapse_dirs(@files_to_backup);
      # Yet another complication.  collapse_dirs returns absolute paths.
      # We want to change them back to relative so that the backup tar
      # has the same structure.
      s,^$instroot/,, foreach @files_to_backup;
    }
    push(@cmdline, @files_to_backup);
  }

  # Run tar. Unlink both here in case the container is also plain tar.
  unlink("$destdir/$tarname");
  unlink("$destdir/$containername");
  xsystem(@cmdline);

  # compress it.
  if ($type eq "lzma") {
    if (-r "$destdir/$tarname") {
      system($lzma, "--force", "-z", "$destdir/$tarname");
    } else {
      tlwarn("$0: Couldn't find $destdir/$tarname to run $lzma\n");
      return (0, 0, "");
    }
  }
  
  # compute the size.
  if (! -r "$destdir/$containername") {
    tlwarn ("$0: Couldn't find $destdir/$containername\n");
    return (0, 0, "");
  }
  my $size = (stat "$destdir/$containername") [7];
  my $md5 = TeXLive::TLUtils::tlmd5("$destdir/$containername");
  
  # cleaning up
  unlink("$tlpobjdir/$self->{'name'}.tlpobj");
  unlink($tartempfile) if $tartempfile;
  rmdir($tlpobjdir) if $removetlpobjdir;
  xchdir($cwd);

  debug(" done $containername, size $size, $md5\n");
  return ($size, $md5, "$destdir/$containername");
}



sub is_arch_dependent {
  my $self = shift;
  if (keys %{$self->{'binfiles'}}) {
    return 1;
  } else {
    return 0;
  }
}

# computes the total size of a package
# if no arguments are given this is
#   docsize + runsize + srcsize + max of binsize
sub total_size {
  my ($self,@archs) = @_;
  my $ret = $self->docsize + $self->runsize + $self->srcsize;
  if ($self->is_arch_dependent) {
    my $max = 0;
    my %foo = %{$self->binsize};
    foreach my $k (keys %foo) {
      $max = $foo{$k} if ($foo{$k} > $max);
    }
    $ret += $max;
  }
  return($ret);
}


sub update_from_catalogue {
  my ($self, $tlc) = @_;
  my $tlcname = $self->name;
  if (defined($self->catalogue)) {
    $tlcname = $self->catalogue;
  } elsif ($tlcname =~ m/^bin-(.*)$/) {
    my $shortname = $1;
    if (!defined($tlc->entries->{$tlcname})) {
      $tlcname = $1;
    }
  }
  if (defined($tlc->entries->{$tlcname})) {
    my $entry = $tlc->entries->{$tlcname};
    if (defined($entry->entry->{'date'})) {
      my $foo = $entry->entry->{'date'};
      $foo =~ s/^.Date: //;
      $foo =~ s/ \(.*\) \$$//;
      $self->cataloguedata->{'date'} = $foo;
    }
    if (defined($entry->license)) {
      $self->cataloguedata->{'license'} = $entry->license;
    }
    if (defined($entry->version) && ($entry->version ne "")) {
      $self->cataloguedata->{'version'} = $entry->version;
    }
    if (defined($entry->ctan)) {
      $self->cataloguedata->{'ctan'} = $entry->ctan;
    }
    #if (defined($entry->texlive)) {
    # $self->cataloguedata->{'texlive'} = $entry->texlive;
    #}
    #if (defined($entry->miktex)) {
    #  $self->cataloguedata->{'miktex'} = $entry->miktex;
    #}
    if (defined($entry->caption)) {
      $self->{'shortdesc'} = $entry->caption unless $self->{'shortdesc'};
    }
    if (defined($entry->description)) {
      $self->{'longdesc'} = $entry->description unless $self->{'longdesc'};
    }
    #
    # we need to do the following:
    # - take the href entry for a documentation file entry in the TC
    # - remove the 'ctan:' prefix
    # - remove the <ctan path='...'> part
    # - match the rest against all docfiles in an intelligent way
    #
    # Example:
    # juramisc.xml contains:
    # <documentation details='Package documentation' language='de'
    #   href='ctan:/macros/latex/contrib/juramisc/doc/jmgerdoc.pdf'/>
    # <ctan path='/macros/latex/contrib/juramisc'/>
    my @tcdocfiles = keys %{$entry->docs};
    my @tlpdocfiles = $self->docfiles;
    foreach my $tcdocfile (@tcdocfiles) {
      # basename also kills the ctan: prefix!
      my $tcdocfilebasename = $tcdocfile;
      # remove the ctan: prefix
      $tcdocfilebasename =~ s/^ctan://;
      # remove the ctan path if present
      my $tcctanpath = $entry->ctan ? $entry->ctan : "";
      $tcdocfilebasename =~ s/^$tcctanpath//;
      foreach my $tlpdocfile (@tlpdocfiles) {
        if ($tlpdocfile =~ m/$tcdocfilebasename$/) {
          # update the language/detail tags if present!
          if (defined($entry->docs->{$tcdocfile}{'details'})) {
            $self->{'docfiledata'}{$tlpdocfile}{'details'} = $entry->docs->{$tcdocfile}{'details'};
          }
          if (defined($entry->docs->{$tcdocfile}{'language'})) {
            $self->{'docfiledata'}{$tlpdocfile}{'language'} = $entry->docs->{$tcdocfile}{'language'};
          }
        }
      }
    }
  }
}

sub is_meta_package {
  my $self = shift;
  if ($self->category =~ /^$MetaCategoriesRegexp$/) {
    return 1;
  }
  return 0;
}

sub docfiles_package {
  my $self = shift;
  if (not($self->docfiles)) { return ; }
  my $tlp = new TeXLive::TLPOBJ;
  $tlp->name($self->name . ".doc");
  $tlp->shortdesc("doc files of " . $self->name);
  $tlp->revision($self->revision);
  $tlp->category($self->category);
  $tlp->add_docfiles($self->docfiles);
  $tlp->docsize($self->docsize);
  # $self->clear_docfiles();
  # $self->docsize(0);
  return($tlp);
}

sub srcfiles_package {
  my $self = shift;
  if (not($self->srcfiles)) { return ; }
  my $tlp = new TeXLive::TLPOBJ;
  $tlp->name($self->name . ".source");
  $tlp->shortdesc("source files of " . $self->name);
  $tlp->revision($self->revision);
  $tlp->category($self->category);
  $tlp->add_srcfiles($self->srcfiles);
  $tlp->srcsize($self->srcsize);
  # $self->clear_srcfiles();
  # $self->srcsize(0);
  return($tlp);
}

sub split_bin_package {
  my $self = shift;
  my %binf = %{$self->binfiles};
  my @retlist;
  foreach $a (keys(%binf)) {
    my $tlp = new TeXLive::TLPOBJ;
    $tlp->name($self->name . ".$a");
    $tlp->shortdesc("binary files of " . $self->name . " for $a");
    $tlp->revision($self->revision);
    $tlp->category($self->category);
    $tlp->add_binfiles($a,@{$binf{$a}});
    $tlp->binsize( $a => $self->binsize->{$a} );
    push @retlist, $tlp;
  }
  if (keys(%binf)) {
    push @{$self->{'depends'}}, $self->name . ".ARCH";
  }
  $self->clear_binfiles();
  return(@retlist);
}


# Helpers.
#
sub add_files {
  my ($self,$type,@files) = @_;
  die("Cannot use add_files for binfiles, we need that arch!")
    if ($type eq "bin");
  &TeXLive::TLUtils::push_uniq(\@{ $self->{"${type}files"} }, @files);
}

sub remove_files {
  my ($self,$type,@files) = @_;
  die("Cannot use remove_files for binfiles, we need that arch!")
    if ($type eq "bin");
  my @finalfiles;
  foreach my $f (@{$self->{"${type}files"}}) {
    if (not(&TeXLive::TLUtils::member($f,@files))) {
      push @finalfiles,$f;
    }
  }
  $self->{"${type}files"} = [ @finalfiles ];
}

sub contains_file {
  my ($self,$fn) = @_;
  # if the filename already contains a / do not add it at the beginning
  my $ret = "";
  if ($fn =~ m!/!) {
    return(grep(m!$fn$!, $self->all_files));
  } else {
    return(grep(m!/$fn$!,$self->all_files));
  }
}

sub all_files {
  my ($self) = shift;
  my @ret = ();

  push (@ret, $self->docfiles);
  push (@ret, $self->runfiles);
  push (@ret, $self->srcfiles);
  push (@ret, $self->allbinfiles);

  return @ret;
}

sub allbinfiles {
  my $self = shift;
  my @ret;
  my %binfiles = %{$self->binfiles};
  foreach my $arch (keys %binfiles) {
    push (@ret, @{$binfiles{$arch}});
  }

  return @ret;
}

sub make_return_hash_from_executes {
  my $self = shift;
  my $type = shift;
  if (!defined($type) || (($type ne "enable") && ($type ne "disable"))) {
    die "make_return_hash_from_executes: enable or disable, not type $type";
  }
  my %ret;
  my (@maps, @formats, @dats);
  if ($self->runfiles) {
    $ret{'mktexlsr'} = 1;
  }
  if ($self->srcfiles) {
    $ret{'mktexlsr'} = 1;
  }
  if ($self->docfiles) {
    $ret{'mktexlsr'} = 1;
  }
  foreach my $e ($self->executes) {
    if ($e =~ m/^add((Mixed)?Map)\s+([^\s]+)\s*$/) {
      if ($type eq "enable") {
        push @maps, "enable $1=$3";
      } else {
        push @maps, "disable $3";
      }
    } elsif ($e =~ m/^BuildFormat\s+([^\s]+)\s*$/) {
      push @formats, $1;
    } elsif ($e =~ m/^AddHyphen\s+(.*)\s*$/) {
      push @dats, $1;
    } else {
      tlwarn("Unknown execute $e in ", $self->name, "\n");
    }
  }
  $ret{'map'} = [ @maps ] if (@maps);
  $ret{'format'} = [ @formats ] if (@formats);
  $ret{'language'} = [ @dats ] if (@dats);
  return(\%ret);
}


# member access functions
#
sub name {
  my $self = shift;
  if (@_) { $self->{'name'} = shift }
  return $self->{'name'};
}
sub category {
  my $self = shift;
  if (@_) { $self->{'category'} = shift }
  return $self->{'category'};
}
sub shortdesc {
  my $self = shift;
  if (@_) { $self->{'shortdesc'} = shift }
  return $self->{'shortdesc'};
}
sub longdesc {
  my $self = shift;
  if (@_) { $self->{'longdesc'} = shift }
  return $self->{'longdesc'};
}
sub revision {
  my $self = shift;
  if (@_) { $self->{'revision'} = shift }
  return $self->{'revision'};
}
sub catalogue {
  my $self = shift;
  if (@_) { $self->{'catalogue'} = shift }
  return $self->{'catalogue'};
}
sub srcfiles {
  my $self = shift;
  if (@_) { $self->{'srcfiles'} = [ @_ ] }
  return @{ $self->{'srcfiles'} };
}
sub containersize {
  my $self = shift;
  if (@_) { $self->{'containersize'} = shift }
  return ( defined($self->{'containersize'}) ? $self->{'containersize'} : -1 );
}
sub srccontainersize {
  my $self = shift;
  if (@_) { $self->{'srccontainersize'} = shift }
  return ( defined($self->{'srccontainersize'}) ? $self->{'srccontainersize'} : -1 );
}
sub doccontainersize {
  my $self = shift;
  if (@_) { $self->{'doccontainersize'} = shift }
  return ( defined($self->{'doccontainersize'}) ? $self->{'doccontainersize'} : -1 );
}
sub containermd5 {
  my $self = shift;
  if (@_) { $self->{'containermd5'} = shift }
  return ( defined($self->{'containermd5'}) ? $self->{'containermd5'} : "" );
}
sub srccontainermd5 {
  my $self = shift;
  if (@_) { $self->{'srccontainermd5'} = shift }
  return ( defined($self->{'srccontainermd5'}) ? $self->{'srccontainermd5'} : "" );
}
sub doccontainermd5 {
  my $self = shift;
  if (@_) { $self->{'doccontainermd5'} = shift }
  return ( defined($self->{'doccontainermd5'}) ? $self->{'doccontainermd5'} : "" );
}
sub srcsize {
  my $self = shift;
  if (@_) { $self->{'srcsize'} = shift }
  return ( defined($self->{'srcsize'}) ? $self->{'srcsize'} : 0 );
}
sub clear_srcfiles {
  my $self = shift;
  $self->{'srcfiles'} = [ ] ;
}
sub add_srcfiles {
  my ($self,@files) = @_;
  $self->add_files("src",@files);
}
sub remove_srcfiles {
  my ($self,@files) = @_;
  $self->remove_files("src",@files);
}
sub docfiles {
  my $self = shift;
  if (@_) { $self->{'docfiles'} = [ @_ ] }
  return @{ $self->{'docfiles'} };
}
sub clear_docfiles {
  my $self = shift;
  $self->{'docfiles'} = [ ] ;
}
sub docsize {
  my $self = shift;
  if (@_) { $self->{'docsize'} = shift }
  return ( defined($self->{'docsize'}) ? $self->{'docsize'} : 0 );
}
sub add_docfiles {
  my ($self,@files) = @_;
  $self->add_files("doc",@files);
}
sub remove_docfiles {
  my ($self,@files) = @_;
  $self->remove_files("doc",@files);
}
sub docfiledata {
  my $self = shift;
  my %newfiles = @_;
  if (@_) { $self->{'docfiledata'} = \%newfiles }
  return $self->{'docfiledata'};
}
sub binfiles {
  my $self = shift;
  my %newfiles = @_;
  if (@_) { $self->{'binfiles'} = \%newfiles }
  return $self->{'binfiles'};
}
sub clear_binfiles {
  my $self = shift;
  $self->{'binfiles'} = { };
}
sub binsize {
  my $self = shift;
  my %newsizes = @_;
  if (@_) { $self->{'binsize'} = \%newsizes }
  return $self->{'binsize'};
}
sub add_binfiles {
  my ($self,$arch,@files) = @_;
  &TeXLive::TLUtils::push_uniq(\@{ $self->{'binfiles'}{$arch} }, @files);
}
sub remove_binfiles {
  my ($self,$arch,@files) = @_;
  my @finalfiles;
  foreach my $f (@{$self->{'binfiles'}{$arch}}) {
    if (not(&TeXLive::TLUtils::member($f,@files))) {
      push @finalfiles,$f;
    }
  }
  $self->{'binfiles'}{$arch} = [ @finalfiles ];
}
sub runfiles {
  my $self = shift;
  if (@_) { $self->{'runfiles'} = [ @_ ] }
  return @{ $self->{'runfiles'} };
}
sub clear_runfiles {
  my $self = shift;
  $self->{'runfiles'} = [ ] ;
}
sub runsize {
  my $self = shift;
  if (@_) { $self->{'runsize'} = shift }
  return ( defined($self->{'runsize'}) ? $self->{'runsize'} : 0 );
}
sub add_runfiles {
  my ($self,@files) = @_;
  $self->add_files("run",@files);
}
sub remove_runfiles {
  my ($self,@files) = @_;
  $self->remove_files("run",@files);
}
sub depends {
  my $self = shift;
  if (@_) { $self->{'depends'} = [ @_ ] }
  return @{ $self->{'depends'} };
}
sub executes {
  my $self = shift;
  if (@_) { $self->{'executes'} = [ @_ ] }
  return @{ $self->{'executes'} };
}
sub containerdir {
  my @self = shift;
  if (@_) { $_containerdir = $_[0] }
  return $_containerdir;
}
sub cataloguedata {
  my $self = shift;
  my %ct = @_;
  if (@_) { $self->{'cataloguedata'} = \%ct }
  return $self->{'cataloguedata'};
}

format multilineformat =
longdesc ^<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<~~
$_tmp
.

1;
__END__


=head1 NAME

C<TeXLive::TLPOBJ> -- TeX Live Package Object access module

=head1 SYNOPSIS

  use TeXLive::TLPOBJ;

  my $tlpobj=TeXLive::TLPOBJ->new(name => "foobar");

=head1 DESCRIPTION

The L<TeXLive::TLPOBJ> module provide access to TeX Live Package Object
files describing a self-contained package.

=head1 FILE SPECIFICATION

Please see L<TeXLive::TLPSRC> documentation for the specification. The
only differences are that the various C<*pattern> keys are invalid, and
instead there are the respective C<*files> keys described below. Furthermore
some more I<keys> is allowed: C<revision> which specifies the maximum of
all last changed revision of files contained in the package, and anything
starting with C<catalogue-> specifying information coming from the
TeX Catalogue.

All these keys have in common that they are followed by a list of files
I<indented> by one space. They differ only in the first line itself
(described below).

=over 4

=item C<srcfiles>, C<runfiles>, C<binfiles>, C<docfiles>
each of these items contains addition the sum of sizes of the
single files (in number of C<TeXLive::TLConfig::BlockSize> blocks, which
is currently 4k).

  srcfiles size=NNNNNN
  runfiles size=NNNNNN

=item C<docfiles>

The docfiles line itself is similar to the C<srcfiles> and C<runfiles> lines
above:

  docfiles size=NNNNNN

But the lines listing the files are allowed to have additional tags:

  /------- excerpt from achemso.tlpobj
  |...
  |docfiles size=1702468
  | texmf-dist/doc/latex/aeguill/README details="Package Readme"
  | texmf-dist/doc/latex/achemso/achemso.pdf details="Package documentation" language="en"
  |...

Currently only the tags C<details> and C<language> are allowed. These
additional information can be accessed via the C<docfiledata> function
returning a hash with the respective files (including path) as key.

=item C<binfiles>

Since C<binfiles> are different for the different architectures one
C<tlpobj> file can contain C<binfiles> lines for different
architectures. The architecture is specified on the C<binfiles> using
the C<arch=>I<XXX> tag. Thus, C<binfiles> lines look like

  binfiles arch=XXXX size=NNNNN

=back

Here is an excerpt from the representation of the C<bin-dvipsk> package,
with C<|> characters inserted to show the indentation:

  |name bin-dvipsk
  |category TLCore
  |revision 4427
  |docfiles size=959434
  | texmf/doc/dvips/dvips.html
  | ...
  |runfiles size=1702468
  | texmf/dvips/base/color.pro
  | ...
  | texmf/scripts/pkfix/pkfix.pl
  |binfiles arch=i386-solaris size=329700
  | bin/i386-solaris/afm2tfm
  | bin/i386-solaris/dvips
  | bin/i386-solaris/pkfix
  |binfiles arch=win32 size=161280
  | bin/win32/afm2tfm.exe
  | bin/win32/dvips.exe
  | bin/win32/pkfix.exe
  |...

=head1 PACKAGE VARIABLES

TeXLive::TLPOBJ has one package wide variable which is C<containerdir> where
generated container files are saved (if not otherwise specified.

  TeXLive::TLPOBJ->containerdir("path/to/container/dir");

=head1 MEMBER ACCESS FUNCTIONS

For any of the I<keys> a function

  $tlpobj->key

is available, which returns the current value when called without an argument,
and sets the respective value when called with an argument. For the
TeX Catalogue Data the function

  $tlpobj->cataloguedata

returns and takes as argument a hash.

Arguments and return values for C<name>, C<category>, C<shortdesc>,
C<longdesc>, C<catalogue>, C<revision> are single scalars.

Arguments and return values for C<depends>, C<executes> are lists.

Arguments and return values for C<docfiles>, C<runfiles>, C<srcfiles>
are lists.

Arguments and return values for C<binfiles> is a hash with the
architectures as keys.

Arguments and return values for C<docfiledata> is a hash with the
full file names of docfiles as key, and the value is again a hash.

The size values are handled with these functions:

  $tlpobj->docsize
  $tlpobj->runsize
  $tlpobj->srcsize
  $tlpobj->binsize("arch1" => size1, "arch2" => size2, ...)

which set or get the current value of the respective sizes. Note that also
the C<binsize> function returns (and takes as argument) a hash with the
architectures as keys, similar to the C<runfiles> functions (see above).

Futhermore, if the tlpobj is contained ina tlpdb which describes a media
where the files are distributed in packed format (usually as .tar.lzma),
there are 6 more possible keys:

  $tlpobj->containersize
  $tlpobj->doccontainersize
  $tlpobj->srccontainersize
  $tlpobj->containermd5
  $tlpobj->doccontainermd5
  $tlpobj->srccontainermd5

describing the respective sizes and md5sums in bytes and as hex string, resp.
The latter two are only present
if src/doc file container splitting is activated for that install medium.

=head1 OTHER FUNCTIONS

The following functions can be called for an C<TLPOBJ> object:

=over 4

=item C<new>

The constructor C<new> returns a new C<TLPSRC> object. The arguments
to the C<new> constructor can be in the usual hash representation for
the different keys above:

  $tlpobj=TLPOBJ->new(name => "foobar", shortdesc => "The foobar package");

=item C<from_file("filename")>

reads a C<tlpobj> file.

  $tlpobj = new TLPOBJ;
  $tlpobj->from_file("path/to/the/tlpobj/file");

=item C<from_fh($filehandle[, $multi])>

read the textual representation of a TLPOBJ from an already opened
file handle.  If C<$multi> is undefined (ie not given) then multiple
tlpobj in the same file are treated as errors. If C<$multi> is defined
then returns after reading one tlpobj.

Returns C<1> if it found a C<tlpobj>, otherwise C<0>.

=item C<writeout>

writes the textual representation of a C<TLPOBJ> object to C<stdout>,
or the filehandle if given:

  $tlpsrc->writeout;
  $tlpsrc->writeout(\*FILEHANDLE);

=item C<writeout_simple>

debugging function for comparison with C<tpm>/C<tlps>, will go away.

=item C<make_container($type,$instroot[, $destdir[, $containername[, $relative]]])>

creates a container file of the all files in the C<TLPOBJ>
in C<$destdir> (if not defined then C<< TLPOBJ->containerdir >> is used).

The C<$type> variable specifies the type of container to be used.
Currently only C<zip> or C<lzma> are allowed, and are generating
zip files and tar.lzma files, respectively.

The file name of the created container file is C<$containername.extension>,
where extension is either C<.zip> or C<.tar.lzma>, depending on the
setting of C<$type>. If no C<$containername> is specified the package name
is used.

All container files B<also> contain the respective
C<TLPOBJ> file in C<tlpkg/tlpobj/$name.tlpobj>.

The argument C<$instroot> specifies the root of the installation from
which the files should be taken.

If the argument C<$relative> is present and true (perlish true) AND the
packages does not span multiple texmf trees (i.e., all the first path
components of all files are the same) then a relative packages is created,
i.e., the first path component is stripped. In this case the tlpobj file
is placed into the root of the installation.

This is used to distribute packages which can be installed in any arbitrary
texmf tree (of other distributions, too).

Return values are the size, the md5sum, and the full name of the container.

=item C<recompute_sizes($tltree)>

recomputes the sizes based on the information present in C<$tltree>.

=item C<recompute_revision($tltree [, $revtlpsrc ])>

recomputes the revision based on the information present in C<$tltree>.
The optional argument C<$rectlpsrc> can be an additional revision number
which is taken into account. C<$tlpsrc->make_tlpobj> adds the revision
number of the C<tlpsrc> file here so that collections (which do not
contain files) also have revision number.

=item C<update_from_catalogue($texcatalogue)>

adds information from a C<TeXCatalogue> object
(currently license, version, url, and updates docfiles with details and
languages tags if present in the Catalogue).

=item C<split_bin_package>

splits off the binfiles of C<TLPOBJ> into new independent C<TLPOBJ> with
the original name plus ".arch" for every arch for which binfiles are present.
The original package is changed in two respects: the binfiles are removed
(since they are now in the single name.arch packages), and an additional
depend on "name.ARCH" is added. Note that the ARCH is a placeholder.

=item C<srcfiles_package>

=item C<docfiles_package>

splits off the srcfiles or docfiles of C<TLPOBJ> into new independent
C<TLPOBJ> with
the original name plus ".sources". The source/doc files are
B<not> removed from the original package, since these functions are only
used for the creation of split containers.

=item C<is_arch_dependent>

returns C<1> if there are C<binfiles>, otherwise C<0>.

=item C<total_size>

If no argument is given returns the sum of C<srcsize>, C<docsize>,
C<runsize>.

If arguments are given, they are assumed to be architecture names, and
it returns the above plus the sum of sizes of C<binsize> for those
architectures.

=item C<is_meta_package>

Returns true if the package is a meta package as defined in TLConfig
(Currently Collection and Scheme).

=item C<clear_{src,run,doc,bin}files>

Removes all the src/run/doc/binfiles from the C<TLPOBJ>.

=item C<{add,remove}_{src,run,doc}files(@files)>

adds or removes files to the respective list of files.

=item C<{add,remove}_binfiles($arch, @files)>

adds or removes files from the list of C<binfiles> for the given architecture.

=item C<{add,remove}_files($type, $files)>

adds or removes files for the given type (only for C<run>, C<src>, C<doc>).

=item C<contains_file($filename)>

returns the list of files matching $filename which are contained in
the package. If $filename contains a / the matching is only anchored
at the end with $. Otherwise it is prefix with a / and anchored at the end.

=item C<all_files>

returns a list of all files of all types.

=item C<allbinfiles>

returns a list of all binary files.

=back

=head1 SEE ALSO

The modules L<TeXLive::TLConfig>, L<TeXLive::TLUtils>, L<TeXLive::TLPSRC>,
L<TeXLive::TLPDB>, L<TeXLive::TLTREE>, L<TeXLive::TeXCatalogue>.

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
