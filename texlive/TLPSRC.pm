# $Id: TLPSRC.pm 11628 2008-12-16 01:08:20Z karl $
# TeXLive::TLPSRC.pm - module for using tlpsrc files
# Copyright 2007, 2008 Norbert Preining
#
# This file is licensed under the GNU General Public License version 2
# or any later version.

package TeXLive::TLPSRC;

use FileHandle;
use TeXLive::TLConfig qw($CategoriesRegexp);
use TeXLive::TLUtils;
use TeXLive::TLPOBJ;
use TeXLive::TLTREE;

my $_tmp;
my %autopatterns;  # computed once internally

sub new
{
  my $class = shift;
  my %params = @_;
  my $self = {
    name        => $params{'name'},
    category    => defined($params{'category'}) ? $params{'category'} : $DefaultCategory,
    shortdesc   => $params{'shortdesc'},
    longdesc    => $params{'longdesc'},
    catalogue   => $params{'catalogue'},
    runpatterns => $params{'runpatterns'},
    srcpatterns => $params{'srcpatterns'},
    docpatterns => $params{'docpatterns'},
    binpatterns => $params{'binpatterns'},
    executes    => defined($params{'executes'}) ? $params{'executes'} : [],
    depends     => defined($params{'depends'}) ? $params{'depends'} : [],
  };
  bless $self, $class;
  return $self;
}


sub from_file
{
  my $self = shift;
  die "need exactly one filename for initialization" if @_ != 1;
  my $srcfile = $_[0];
  
  if (! -r "$srcfile") {
    # if the argument is not readable as is, try looking for it in the
    # hierarchy where we are.  The %INC hash records where packages were
    # found, so we use that to locate ourselves.
    (my $trydir = $INC{"TeXLive/TLPSRC.pm"}) =~ s,/[^/]*$,,;
    chomp ($trydir = `cd $trydir/../tlpsrc && pwd`);  # make absolute
    my $tryfile = "$trydir/$srcfile.tlpsrc";
    #warn "$trydir\n$tryfile\n";
    $srcfile = $tryfile if -r $tryfile;
  }
  
  open(TMP, "<$srcfile") || die("failed to open tlpsrc '$srcfile': $!");
  my @lines = <TMP>;
  close(TMP);

  my $name = "";
  # default category = Package
  my $category = "Package";
  my $shortdesc = "";
  my $longdesc= "";
  my $catalogue = "";
  my (@executes, @depends);
  my (@runpatterns, @docpatterns, @binpatterns, @srcpatterns);
  my $started = 0;
  my $finished = 0;
  my $savedline = "";

  foreach my $line (@lines) {
    # we allow continuation lines in tlpsrc files, i.e., lines with a \ at
    # the end
    if ($line =~ /^(.*)\\$/) {
      $savedline .= $1;
      next;
    }
    if ($savedline ne "") {
      # we are in a continuation line
      $line = "$savedline$line";
      $savedline = "";
    }

    $line =~ /^\s*#/ && next;          # skip comment lines
    next if $line =~ /^\s*$/;          # skip blank lines
    # (blank lines are significant in tlpobj, but not tlpsrc)

    if ($line =~ /^ /) {
      die "$srcfile: non-continuation indentation not allowed: `$line'";
    }
    # names of source packages can either be
    # - normal names: ^[-\w]+$
    # - win32 specific packages: ^[-\w]+\.win32$
    # - normal texlive specific packages: ^texlive.*\..*$
    # - configuration texlive specific packages: ^00texlive.*\..*$
    if ($line =~ /^name\s*([-\w]+(\.win32)?|00texlive.*|texlive\..*)$/) {
      $name = $1;
      $started && die "$srcfile: second name directive not allowed: $name";
      $started = 1;
    } else {
      $started || die "$srcfile: first directive must be `name', not $line";
      if ($line =~ /^shortdesc\s*(.*)\s*$/) {
        $shortdesc = $1;
        next;
      } elsif ($line =~ /^category\s+$CategoriesRegexp$/) {
        $category = $1;
        next;
      } elsif ($line =~ /^longdesc\s+(.*)\s*$/) {
        $longdesc .= "$1 ";
        next;
      } elsif ($line =~ /^catalogue\s+(.*)\s*$/) {
        $catalogue = $1;
        next;
      } elsif ($line =~ /^runpattern\s+(.*)\s*$/) {
        push @runpatterns, $1 if ($1 ne "");
        next;
      } elsif ($line =~ /^srcpattern\s+(.*)\s*$/) {
        push @srcpatterns, $1 if ($1 ne "");
        next;
      } elsif ($line =~ /^docpattern\s+(.*)\s*$/) {
        push @docpatterns, $1 if ($1 ne "");
        next;
      } elsif ($line =~ /^binpattern\s+(.*)\s*$/) {
        push @binpatterns, $1 if ($1 ne "");
        next;
      } elsif ($line =~ /^execute\s+(.*)\s*$/) {
        push @executes, $1 if ($1 ne "");
        next;
      } elsif ($line =~ /^depend\s+(.*)\s*$/) {
        push @depends, $1 if ($1 ne "");
        next;
      } else {
        tlwarn("$srcfile:$.: unknown tlpsrc directive, please fix: $line\n");
      }
    }
  }
  $self->_srcfile($srcfile);
  $self->name($name);
  $self->category($category);
  $self->catalogue($catalogue) if $catalogue;
  $self->shortdesc($shortdesc) if $shortdesc;
  $self->longdesc($longdesc) if $longdesc;
  $self->srcpatterns(@srcpatterns) if @srcpatterns;
  $self->runpatterns(@runpatterns) if @runpatterns;
  $self->binpatterns(@binpatterns) if @binpatterns;
  $self->docpatterns(@docpatterns) if @docpatterns;
  $self->executes(@executes) if @executes;
  $self->depends(@depends) if @depends;
}


sub writeout
{
  my $self = shift;
  my $fd = (@_ ? $_[0] : STDOUT);
  format_name $fd "multilineformat";
  print $fd "name ", $self->name, "\n";
  print $fd "category ", $self->category, "\n";
  defined($self->{'catalogue'}) && print $fd "catalogue $self->{'catalogue'}\n";
  defined($self->{'shortdesc'}) && print $fd "shortdesc $self->{'shortdesc'}\n";
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
  if (defined($self->{'srcpatterns'}) && (@{$self->{'srcpatterns'}})) {
    foreach (sort @{$self->{'srcpatterns'}}) {
      print $fd "srcpattern $_\n";
    }
  }
  if (defined($self->{'runpatterns'}) && (@{$self->{'runpatterns'}})) {
    foreach (sort @{$self->{'runpatterns'}}) {
      print $fd "runpattern $_\n";
    }
  }
  if (defined($self->{'docpatterns'}) && (@{$self->{'docpatterns'}})) {
    foreach (sort @{$self->{'docpatterns'}}) {
      print $fd "docpattern $_\n";
    }
  }
  if (defined($self->{'binpatterns'}) && (@{$self->{'binpatterns'}})) {
    foreach (sort @{$self->{'binpatterns'}}) {
      print $fd "binpattern $_\n";
    }
  }
}


# the hard work, generate the TLPOBJ data.
#
sub make_tlpobj
{
  my ($self,$tltree,$autopattern_root) = @_;
  my %allpatterns = &find_default_patterns($autopattern_root);
  my $category_patterns = $allpatterns{$self->category};

  my $tlp = TeXLive::TLPOBJ->new;
  $tlp->name($self->name);
  $tlp->category($self->category);
  $tlp->shortdesc($self->{'shortdesc'}) if (defined($self->{'shortdesc'}));
  $tlp->longdesc($self->{'longdesc'}) if (defined($self->{'longdesc'}));
  $tlp->catalogue($self->{'catalogue'}) if (defined($self->{'catalogue'}));
  $tlp->executes(@{$self->{'executes'}}) if (defined($self->{'executes'}));
  $tlp->depends(@{$self->{'depends'}}) if (defined($self->{'depends'}));
  $tlp->revision(0);
  my $filemax;
  my $usedefault;
  my @allpospats;
  my @allnegpats;
  my $pkgname = $self->name;
  my @autoaddpat;

  # src/run/doc patterns
  #
  # WARNING WARNING WARNING
  # the "bin" must be last since we drop through for further dealing
  # with specialities of the bin patterns!!!!
  for my $pattype (qw/src run doc bin/) {
    @allpospats = ();
    @allnegpats = ();
    @autoaddpat = ();
    $usedefault = 1;
    foreach my $p (@{$self->{${pattype} . 'patterns'}}) {
      if ($p =~ m/^a\s+(.*)\s*$/) {
        # format 
        #   a toplevel1 toplevel2 toplevel3 ...
        # which add autopatterns as if we are doing single packages
        # toplevel1 toplevel2 toplevel3
        push @autoaddpat, split(' ', $1);
      } elsif ($p =~ m/^\+!(.*)$/) {
        push @allnegpats, $1;
      } elsif ($p =~ m/^\+(.*)$/) {
        push @allpospats, $1;
      } elsif ($p =~ m/^!(.*)$/) {
        push @allnegpats, $1;
        $usedefault = 0;
      } else {
        push @allpospats, $p;
        $usedefault = 0;
      }
    }

    if ($usedefault) {
      push @autoaddpat, $pkgname;
    }
    if (defined($category_patterns)) {
      for my $a (@autoaddpat) {
        my $type_patterns = $category_patterns->{$pattype};
        for my $p (@{$type_patterns}) {
          # replace the string %NAME% with the actual package name
          # we have to make a copy of $p otherwise we change it in the
          # hash once and for all
          (my $pp = $p) =~ s/%NAME%/$a/g;
          # sort through the patterns, and make sure that * are added to 
          # tag the default patterns
          if ($pp =~ m/^!(.*)$/) {
            push @allnegpats, "*$1";
          } else {
            push @allpospats, "*$pp";
          }
        }
      }
    }
    # at this point we do NOT do the actual pattern matching for 
    # bin patterns, since we have some specialities to do
    last if ($pattype eq "bin");
    
    # for all other patterns we create the list and add the files
    foreach my $p (@allpospats) {
      ddebug("pos pattern $p\n");
      $self->_do_normal_pattern($p,$tlp,$tltree,$pattype);
    }
    foreach my $p (@allnegpats) {
      ddebug("neg pattern $p\n");
      $self->_do_normal_pattern($p,$tlp,$tltree,$pattype,1);
    }
  }
  #
  # binpatterns
  #
  # mind that @allpospats and @allnegpats have already been set up
  # in the above loop. We only have to deal with the specialities of
  # the bin patterns
  foreach my $p (@allpospats) {
    my @todoarchs = $tltree->architectures;
    my $finalp = $p;
    if ($p =~ m%^(\w+)/(!?[-_a-z0-9,]+)\s+(.*)$%) {
      my $pt = $1;
      my $aa = $2;
      my $pr = $3;
      if ($aa =~ m/^!(.*)$/) {
        # negative specification
        my %negarchs;
        foreach (split(/,/,$1)) {
          $negarchs{$_} = 1;
        }
        my @foo = ();
        foreach (@todoarchs) {
          push @foo, $_ unless defined($negarchs{$_});
        }
        @todoarchs = @foo;
      } else {
        @todoarchs = split(/,/,$aa);
      }
      # set $p to the pattern without arch specification
      $finalp = "$pt $pr";
    }
    # one final trick
    # if the original pattern string matches bin/win32/ then we *only*
    # work on the win32 arch
    if ($finalp =~ m! bin/win32/!) {
      @todoarchs = qw/win32/;
    }
    # now @todoarchs contains only those archs for which we want
    # to match the pattern
    foreach my $arch (@todoarchs) {
      # get only those files matching the pattern
      my @archfiles = $tltree->get_matching_files('bin',$finalp, $arch);
      if (!@archfiles) {
        if (($arch ne "win32") || defined($::tlpsrc_pattern_warn_win)) {
          tlwarn("$self->{name} ($arch): no hit on binpattern $finalp\n");
        }
      }
      $tlp->add_binfiles($arch,@archfiles);
    }
  }
  foreach my $p (@allnegpats) {
    my @todoarchs = $tltree->architectures;
    my $finalp = $p;
    if ($p =~ m%^(\w+)/(!?[-_a-z0-9,]+)\s+(.*)$%) {
      my $pt = $1;
      my $aa = $2;
      my $pr = $3;
      if ($aa =~ m/^!(.*)$/) {
        # negative specification
        my %negarchs;
        foreach (split(/,/,$1)) {
          $negarchs{$_} = 1;
        }
        my @foo = ();
        foreach (@todoarchs) {
          push @foo, $_ unless defined($negarchs{$_});
        }
        @todoarchs = @foo;
      } else {
        @todoarchs = split(/,/,$aa);
      }
      # set $p to the pattern without arch specification
      $finalp = "$pt $pr";
    }
    # now @todoarchs contains only those archs for which we want
    # to match the pattern
    foreach my $arch (@todoarchs) {
      # get only those files matching the pattern
      my @archfiles = $tltree->get_matching_files('bin',$finalp, $arch);
      if (!@archfiles) {
        if (($arch ne "win32") || defined($::tlpsrc_pattern_warn_win)) {
          tlwarn("$self->{name} ($arch): no hit on negative binpattern $finalp\n")
            unless defined($::tlpsrc_pattern_no_warn_negative);
        }
      }
      $tlp->remove_binfiles($arch,@archfiles);
    }
  }
  # add the revision number of the .tlpsrc file to the compute list:
  $tlp->recompute_revision($tltree, 
          $tltree->file_svn_lastrevision("tlpkg/tlpsrc/$self->{name}.tlpsrc"));
  $tlp->recompute_sizes($tltree);
  return $tlp;
}

sub _do_normal_pattern {
  my ($self,$p,$tlp,$tltree,$type,$negative) = @_;
  my $is_default_pattern = 0;
  if ($p =~ m/^\*/) {
    $is_default_pattern = 1;
    $p =~ s/^\*//;
  }
  my @matchfiles = $tltree->get_matching_files($type,$p);
  if (!$is_default_pattern && !@matchfiles && ($p !~ m/^f ignore/)) {
    tlwarn("$self->{name}: no hit for pattern $p\n");
  }
  if (defined($negative) && $negative == 1) {
    $tlp->remove_files($type,@matchfiles);
  } else {
    $tlp->add_files($type,@matchfiles);
  }
}


# get the default patterns for all categories from an external file,
# return hash with keys being the categories (Package, Documentation)
# and values being refs to another hash.  The subhash's keys are the
# file types (run bin doc ...) with values being refs to an array of
# patterns for that type.
# 
sub find_default_patterns
{
  my ($tlroot) = @_;
  # %autopatterns is global.
  return %autopatterns if keys %autopatterns;  # only compute once
  
  my $apfile = "$tlroot/tlpkg/tlpsrc/00texlive.autopatterns.tlpsrc";
  die "No autopatterns file found: $apfile" if ! -r $apfile;

  my $tlsrc = new TeXLive::TLPSRC;
  $tlsrc->from_file ($apfile);
  if ($tlsrc->binpatterns) {
    for my $p ($tlsrc->binpatterns) {
      my ($cat, @rest) = split ' ', $p;
      push @{$autopatterns{$cat}{"bin"}}, join(' ', @rest);
    }
  }
  if ($tlsrc->srcpatterns) {
    for my $p ($tlsrc->srcpatterns) {
      my ($cat, @rest) = split ' ', $p;
      push @{$autopatterns{$cat}{"src"}}, join(' ', @rest);
    }
  }
  if ($tlsrc->docpatterns) {
    for my $p ($tlsrc->docpatterns) {
      my ($cat, @rest) = split ' ', $p;
      push @{$autopatterns{$cat}{"doc"}}, join(' ', @rest);
    }
  }
  if ($tlsrc->runpatterns) {
    for my $p ($tlsrc->runpatterns) {
      my ($cat, @rest) = split ' ', $p;
      push @{$autopatterns{$cat}{"run"}}, join(' ', @rest);
    }
  }

  for my $cat (keys %autopatterns) {
    debug ("Category $cat\n");
    for my $d (@{$autopatterns{$cat}{"bin"}}) {
      debug ("Found auto bin pattern $d\n");
    }
    for my $d (@{$autopatterns{$cat}{"src"}}) {
      debug ("Found auto src pattern $d\n");
    }
    for my $d (@{$autopatterns{$cat}{"doc"}}) {
      debug ("Found auto doc pattern $d\n");
    }
    for my $d (@{$autopatterns{$cat}{"run"}}) {
      debug ("Found auto run pattern $d\n");
    }
  }
  
  return %autopatterns;
}


# member access functions
#
sub _srcfile {
  my $self = shift;
  if (@_) { $self->{'_srcfile'} = shift }
  return $self->{'_srcfile'};
}
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
sub catalogue {
  my $self = shift;
  if (@_) { $self->{'catalogue'} = shift }
  return $self->{'catalogue'};
}
sub srcpatterns {
  my $self = shift;
  if (@_) { @{ $self->{'srcpatterns'} } = @_ }
  if (defined($self->{'srcpatterns'})) {
    return @{ $self->{'srcpatterns'} };
  } else {
    return;
  }
}
sub docpatterns {
  my $self = shift;
  if (@_) { @{ $self->{'docpatterns'} } = @_ }
  if (defined($self->{'docpatterns'})) {
    return @{ $self->{'docpatterns'} };
  } else {
    return;
  }
}
sub binpatterns {
  my $self = shift;
  if (@_) { @{ $self->{'binpatterns'} } = @_ }
  if (defined($self->{'binpatterns'})) {
    return @{ $self->{'binpatterns'} };
  } else {
    return;
  }
}
sub depends {
  my $self = shift;
  if (@_) { @{ $self->{'depends'} } = @_ }
  return @{ $self->{'depends'} };
}
sub runpatterns {
  my $self = shift;
  if (@_) { @{ $self->{'runpatterns'} } = @_ }
  if (defined($self->{'runpatterns'})) {
    return @{ $self->{'runpatterns'} };
  } else {
    return;
  }
}
sub executes {
  my $self = shift;
  if (@_) { @{ $self->{'executes'} } = @_ }
  return @{ $self->{'executes'} };
}

format multilineformat =
longdesc ^<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<~~
$_tmp
.

1;
__END__


=head1 NAME

C<TeXLive::TLPSRC> -- TeX Live Package Source module

=head1 SYNOPSIS

  use TeXLive::TLPSRC;

  my $tlpsrc = TeXLive::TLPSRC->new(name => "foobar");
  $tlpsrc->from_file("/some/tlpsrc/package.tlpsrc");
  $tlpsrc->from_file("package");
  $tlpsrc->writeout;
  $tlpsrc->writeout(\*FILEHANDLE);

=head1 DESCRIPTION

The C<TeXLive::TLPSRC> module handles TeX Live Package Source
(C<.tlpsrc>) files, which contain all (and only) the information which
cannot be automatically derived from other sources, notably the TeX Live
directory tree and the TeX Catalogue.  In other words, C<.tlpsrc> files
are hand-maintained.

=head1 FILE SPECIFICATION

A C<tlpsrc> file consists of lines of the form:

I<key> I<value>

where I<key> can be C<name>, C<category>, C<shortdesc>, C<longdesc>,
C<catalogue>, C<runpattern>, C<srcpattern>, C<docpattern>, C<binpattern>,
C<execute>, or C<depend>.

Continuation lines are supported via a trailing backslash.  That is, if
the C<.tlpsrc> file contains two physical lines like this:
  
  foo\
  bar

they are concatenated into C<foobar>.  The newline is removed; no other
whitespace is added or removed, so typically the continuation line
starts with one or more spaces.

Comment lines begin with a # and continue to the end of the line.

Blank lines are ignored.

The meaning of the I<key>s are:

=over 4

=item C<name>

identifies the package; C<value> must consist only of C<[-_a-zA-Z0-9]>,
i.e., with what Perl considers a C<\w>. 

There are three exceptions to this rule:

=over 8

=item B<name.ARCH>

where B<ARCH> is a supported architecture-os combination.  This has two
uses.  First, packages are split (automatically) into containers for the
different architectures to make possible installations including only
the necessary binaries.  Second, one can add 'one-arch-only' packages,
often used to deal with Windows peculiarities.

=item B<00texlive>I<something>

These packages are used for internal operation and storage containers
for settings.  I<00texlive> packages are never be split into separate
arch-packages, and containers are never generated for these packages.

The full list of currently used packages of this type is:

=over 8

=item B<00texlive.config>

This package contains configuration options for the TeX Live archive.
If container_split_{doc,src}_files occurs in the depend lines the
{doc,src} files are split into separate containers (.tar.lzma) 
during container build time. Note that this has NO effect on the
appearance within the texlive.tlpdb. It is only on container level.
The container_format/XXXXX specifies the format, currently allowed
is only "lzma", which generates .tar.lzma files. zip can be supported.
release/NNNN specifies the release number as used in the installer.

=item B<00texlive-installation.config>

This package serves a double purpose:

1. at installation time the present values are taken as default for
the installer

2. on an installed system it serves as configuration file. Since
we have to remember these settings for additional package
installation, removal, etc.

=item B<00texlive.core>

This package collects some files which are not caught by any of the
other TL packages. Its primary purpose is to make the file coverage
check happy.  The files here are not copied by the installer
and containers are not built; they exist only in the
full DVD image.

=item B<00texlive.installer>

This package defines the files to go into the installer
archives (install-tl-unx.tar.gz, install-tl.zip) built
by the tl-make-installer script.  Most of what's here is also
included in the texlive.infra package -- ordinarily duplicates
are not allowed, but in this case, 00texlive.installer is never
used *except* to build the installer archives, so it's ok.

=back

=item B<texlive>I<some.thing>

(notice the dot in the package name) These packages are central TeX Live
internal packages and are treated as usual packages in (more or less)
all respects, but have that extra dot to be sure they will never clash
with any package that can possibly appear on CTAN.  The only such
package currently is C<texlive.infra>, which contains L<tlmgr> and other
basic infrastructure functionality.

=back

=item C<category>

identifies the category into which this package belongs. This determines
the default patterns applied.  Possible categories are defined in
C<TeXLive::TLConfig>, currently C<Collection>, C<Scheme>, C<TLCore>,
C<Documentation>, C<Package>.  Most packages will fall into the
C<Package> category.

=item C<catalogue>

identifies the name under which this package can be found in the TeX
Catalogue.

=item C<shortdesc>

gives a one line description of the package. Subsequent entries will
overwrite the former ones. In TeX Live only used for collections and
schemes.

=item C<longdesc>

gives a long description of the package. Susequent entries are
concatenated into a long text. In TeX Live only used for collections and
schemes.

=item C<depend>

gives the list of dependencies, which are just other package names.
All the C<depend> lines contribute to the dependencies of the package.
Examples:
  
  depend cm
  depend plain
  depend collection-basicbin

=item C<execute>

gives a free form entry of install time jobs to be executed. Currently
the following possible values are understood by the installers:

=over 4

=item C<execute addMap> I<font>C<.map>

enables the font map file I<font>C<.map> in the C<updmap.cfg> file.

=item C<execute addMixedMap> I<font>C<.map>

enables the font map file I<font>C<.map> for Mixed mode in the
C<updmap.cfg> file.

=item C<execute AddHyphen name=I<texlang> file=I<file> [I<var>...]>

activates the hyphenation pattern with name I<texlang> and load the file
I<file> for that language.  The additional variables I<var> are:
C<lefthyphenmin>, C<righthyphenmin> (both integers), and C<synonyms> (a
comma-separated list of alias names for that hyphenation).

=item C<execute BuildFormat> I<format>

build the format I<format>, as specified in the C<fmtutil.cnf> file.

=back

=item C<(src|run|doc|bin)pattern> I<pattern>

adds a pattern (next section) to the respective list of patterns.

=back

=head1 PATTERNS

Patterns specify which files are to be included into a C<tlpobj> at
expansion time. Patterns are of the form

  [PREFIX]TYPE[/[!]ARCHSPEC] PAT

where

  PREFIX = + | +! | !
  TYPE = t | f | d | r
  ARCHSPEC = <list of architectures separated by comma>

Simple patterns without PREFIX and ARCHSPEC specifications are explained
first.

=over 4

=item C<f> I<path>

includes all files which match C<path> where B<only> the last component
of C<path> can contain the usual glob characters C<*> and C<?> (but no
others!).

=item C<d> I<path>

includes all the files in and below the directory specified as C<path>.

=item C<t> I<word1 ... wordN wordL>

includes all the files in and below all directories of the form

  word1/word2/.../wordN/.../any/dirs/.../wordL/

i.e., all the first words but the last form the prefix of the path, then
there can be an arbitrary number of subdirectories, followed by C<wordL>
as the final directory.  A real life example from C<omega.tlpsrc>:

  runpattern t texmf-dist fonts omega

matches C<texmf-dist/fonts/**/omega>, where C<**> matches any number of
intervening subdirectories, e.g.:

  texmf-dist/fonts/ofm/public/omega
  texmf-dist/fonts/tfm/public/omega
  texmf-dist/fonts/type1/public/omega

=item C<r> I<regexp>

includes all files matching the regexp C</^regexp$/>

=item C<a> I<name1> [<name2> ...]

includes auto generated patterns for each I<nameN> as if the package 
itself would be named I<nameN>. That is useful if a package (like venturisadf)
contains toplevel directories named after different fonts.

=back

=head2 Special patterns

=over 4

=item PREFIX

If the C<PREFIX> contains the symbol C<!> the meaning of the pattern is
reversed, i.e., files matching this pattern are removed from the list of
included files.

The prefix C<+> means to append to the list of automatically synthesized
patterns, instead of replacing them.

The C<+> and C<!> prefixes can be combined.  This is useful to exclude
directories from the automatic pattern list.  For example,
C<graphics.tlpsrc> contains this line:

  docpattern +!d texmf-dist/doc/latex/tufte-latex/graphics

so that this subdirectory of the C<tufte-latex> package that happens to
be named `graphics' is not mistakenly included in the C<graphics>
package.

=item Auto-generated patterns

If a given pattern section is empty or B<all> the provided patterns have
the prefix C<+> (e.g., C<+f ...>), then the following patterns, listed
by type are I<automatically> added at expansion time. Note that this list
is not definitive, but is taken from the patterns of tlpsrc files
named C<00texlive.autopatterns.>I<Category>C<.tlpsrc>.

=over 4

=item C<runpattern>

for category C<Package>:

  t texmf-dist topdir $name

where C<topdir> is one of: C<bibtex>, C<context>, C<dvips>, C<fonts>,
C<makeindex>, C<metafont>, C<metapost>, C<mft>, C<omega>, C<scripts>,
C<tex>, C<vtex>.

For other categories B<no> patterns are automatically added to the 
list of C<runpattern>s.

=item C<docpattern>

for category C<Package>:

  t texmf-dist doc $name

for category C<Documentation>:

  t texmf-doc doc $name

=item C<srcpattern>

for category C<Package>:

  t texmf-dist source $name

for category C<Documentation>:

  t texmf-doc source $name

=item C<binpattern>

No C<binpattern>s are ever automatically added.

=back

=item Special treatment of binpatterns

The binpatterns have to deal with all the different architectures. To
ease the writing of patterns, we have the following:

=over 4

=item Architecture expansion

In case the string C<${>I<ARCH>} occurs in one C<binpattern> it is
automatically expanded to the respective architecture.

=item C<bat/exe/dll/texlua> for Windows

C<binpattern>s that match Windows, e.g., C<f bin/win32/foobar> or C<f
bin/${ARCH}/foobar>, also match the files C<foobar.bat>, C<foobar.cmd>,
C<foobar.dll>, C<foobar.exe>, and C<foobar.texlua>.

The above two properties allows to capture the binaries for all
architectures in one binpattern

  binpattern f bin/${ARCH}/dvips

and would get C<bin/win32/dvips.exe> into the runfiles for C<arch=win32>.

This C<bat>/C<exe>/etc. expansion I<only> works for patterns of the C<f>
type.

=item ARCHSPEC specification of a pattern

Sometimes files should be included into the list of binfiles of a
package only for some architectures, or for all but some architectures.
This can be done by specifying the list of architectures for which this
pattern should be matched after the pattern specifier using a C</>:

  binpattern f/win32 tlpkg/bin/perl.exe

will include the file C<tlpkg/bin/perl.exe> only in the binfiles for
the architecture C<win32>. Another example:

  binpattern f/arch1,arch2,arch3 path/$ARCH/foo/bar

This will only try to match this pattern for arch1, arch2, and arch3.

Normally, a binpattern is matched against all possible architectures. If
you want to exclude some architectures, instead of listing all the ones
you want to include as above, you can prefix the list of architectures
with a ! and these architectures will not be tested. Example:

  binpattern f/!arch1,arch2 path/$ARCH/foo/bar

will be matched against all architectures I<except> arch1 and arch2.

=back

=back


=head1 MEMBER ACCESS FUNCTIONS

For any of the above I<key>s a function

  $tlpsrc->key

is available, which returns the current value when called without an argument,
and sets the respective value when called with an argument.

Arguments and return values for C<name>, C<category>, C<shortdesc>,
C<longdesc>, C<catalogue> are single scalars. Arguments and return values
for C<depends>, C<executes>, and the various C<patterns> are lists.

In addition, the C<_srcfile> member refers to the filename for this
C<TLPSRC> object, if set (normally by C<from_file>).

=head1 OTHER FUNCTIONS

The following functions can be called for a C<TLPSRC> object:

=over 4

=item C<new>

The constructor C<new> returns a new C<TLPSRC> object. The arguments
to the C<new> constructor can be in the usual hash representation for
the different keys above:

  $tlpsrc = TLPSRC->new (name => "foobar",
                         shortdesc => "The foobar package");

=item C<from_file("filename")>

reads a C<tlpsrc> file from disk.  C<filename> can either be a full path
(if it's readable, it's used), or just a package identifier such as
C<plain>.  In the latter case, the directory searched is the C<tlpsrc>
sibling of the C<TeXLive> package directory where C<TLPSRC.pm> was found.

  $tlpsrc=new TeXLive::TLPSRC;
  $tlpsrc->from_file("/path/to/the/tlpsrc/somepkg.tlpsrc");
  $tlpsrc->from_file("somepkg");

=item C<writeout>

writes the textual representation of a C<TLPSRC> object to stdout, or the
filehandle if given:

  $tlpsrc->writeout;
  $tlpsrc->writeout(\*FILEHANDLE);

=item C<make_tlpobj($tltree)>

creates a C<TLPOBJ> object from a C<TLPSRC> object and a C<TLTREE> object.
This function does the necessary work to expand the manual data and
enrich it which the actual content from C<$tltree> to a C<TLPOBJ> object.

=back

=head1 SEE ALSO

The modules L<TeXLive::TLConfig>, L<TeXLive::TLUtils>, L<TeXLive::TLPOBJ>, 
L<TeXLive::TLPDB>, L<TeXLive::TLTREE>.

The programs L<tlpsrc2tlpdb> and L<tlpsrc2tlpobj>.

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
