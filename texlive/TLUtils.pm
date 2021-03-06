# $Id: TLUtils.pm 12110 2009-02-07 01:41:31Z karl $
# The inevitable utilities for TeX Live.
#
# Copyright 2007, 2008, 2009 Norbert Preining, Reinhard Kotucha
# This file is licensed under the GNU General Public License version 2
# or any later version.

package TeXLive::TLUtils;

=pod

=head1 NAME

C<TeXLive::TLUtils> -- utilities used in the TeX Live infrastructure

=head1 SYNOPSIS

  use TeXLive::TLUtils;

=head2 Platform Detection

  TeXLive::TLUtils::platform();
  TeXLive::TLUtils::platform_desc($platform);
  TeXLive::TLUtils::win32();
  TeXLive::TLUtils::unix();

=head2 System Tools

  TeXLive::TLUtils::getenv($string);
  TeXLive::TLUtils::which($string);
  TeXLive::TLUtils::get_system_tmpdir();
  TeXLive::TLUtils::tl_tmpdir();
  TeXLive::TLUtils::xchdir($dir);
  TeXLive::TLUtils::xsystem(@args);

=head2 File Utilities

  TeXLive::TLUtils::dirname($path);
  TeXLive::TLUtils::basename($path);
  TeXLive::TLUtils::dirname_and_basename($path);
  TeXLive::TLUtils::dir_writable($path);
  TeXLive::TLUtils::mkdirhier($path);
  TeXLive::TLUtils::rmtree($root, $verbose, $safe);
  TeXLive::TLUtils::copy($file, $target_dir);
  TeXLive::TLUtils::touch(@files);
  TeXLive::TLUtils::download_file($path, $destination [, $progs ]);
  TeXLive::TLUtils::setup_programs($bindir, $platform);

=head2 Installer Functions

  TeXLive::TLUtils::make_var_skeleton($path);
  TeXLive::TLUtils::make_local_skeleton($path);
  TeXLive::TLUtils::create_fmtutil($tlpdb,$dest,$localconf);
  TeXLive::TLUtils::create_updmap($tlpdb,$dest,$localconf);
  TeXLive::TLUtils::create_language_dat($tlpdb,$dest,$localconf);
  TeXLive::TLUtils::create_language_def($tlpdb,$dest,$localconf);
  TeXLive::TLUtils::install_packages($from_tlpdb,$media,$to_tlpdb,$what,$opt_src, $opt_doc)>);
  TeXLive::TLUtils::install_package($what, $filelistref, $target, $platform);

=head2 Miscellaneous

  TeXLive::TLUtils::sort_uniq(@list);
  TeXLive::TLUtils::push_uniq(\@list, @items);
  TeXLive::TLUtils::member($item, @list);
  TeXLive::TLUtils::merge_into(\%to, \%from);
  TeXLive::TLUtils::texdir_check($texdir);
  TeXLive::TLUtils::conv_to_w32_path($path);
  TeXLive::TLUtils::give_ctan_mirror($path);
  TeXLive::TLUtils::tlmd5($path);

=head1 DESCRIPTION

=cut

BEGIN {
  use Exporter ();
  use vars qw( @ISA @EXPORT_OK @EXPORT);
  @ISA = qw(Exporter);
  @EXPORT_OK = qw(
    &platform
    &platform_desc
    &unix
    &getenv
    &which
    &get_system_tmpdir
    &dirname
    &basename
    &dirname_and_basename
    &dir_writable
    &mkdirhier
    &rmtree
    &copy
    &touch
    &collapse_dirs
    &install_package
    &install_packages
    &make_var_skeleton
    &make_local_skeleton
    &create_fmtutil
    &create_updmap
    &create_language_dat
    &create_language_def
    &sort_uniq
    &push_uniq
    &texdir_check
    &member
    &quotewords
    &conv_to_w32_path
    &untar
    &merge_into
    &welcome
    &welcome_paths
    &give_ctan_mirror
    &tlmd5
    &xsystem
  );
  @EXPORT = qw(setup_programs download_file process_logging_options
               tlwarn info log debug ddebug dddebug debug_hash
               win32 xchdir xsystem);
}

use Cwd;
use Digest::MD5;
use Getopt::Long;
use File::Temp;

use TeXLive::TLConfig;
$::opt_verbosity = 0;  # see process_logging_options


=head2 Platform Detection

=over 4

=item C<platform>

If C<$^O=~/MSWin(32|64)$/i> is true we know that we're on
Windows and we set the global variable C<$::_platform_> to C<win32>.
Otherwise we call C<config.guess>.  The output of C<config.guess>
is filtered as described below.

CPU type is determined by a regexp.  And it's necessary to
C<s/i.86/i386/>.

For OS we need a list because we probably have something like
C<linux-gnu> but we need C<linux>.  This list might/should contain OSs
which are not currently supported.  The list currently supports all
platforms supported by TeX Live 2007 plus Cygwin.

If a particular platform is not found in this list we use the regexp
C</.*-(.*$)/> as a last resort and hope it provides something useful.

The result is stored in a global variable C<$::_platform_>.  If you call
C<platform> repeatedly, only the first call of C<platform> will access
the HD/CD/DVD.

=cut

sub platform {
  unless (defined $::_platform_) {
    if ($^O=~/^MSWin(32|64)$/i) {
      $::_platform_="win32";
    } else {
      my $config_guess = "$::installerdir/tlpkg/installer/config.guess";
      my @OSs = qw(aix cygwin darwin freebsd hpux irix linux netbsd
                   openbsd solaris);

      # We cannot rely on #! in config.guess but have to call /bin/sh
      # explicitly because sometimes the 'noexec' flag is set in
      # /etc/fstab for ISO9660 file systems.
      chomp (my $guessed_platform = `/bin/sh $config_guess`);
      
      # For example, if the disc or reader has hardware problems.
      die "$0: could not run $config_guess, cannot proceed, sorry"
        if ! $guessed_platform;
      
      $guessed_platform =~ s/^x86_64-(.*)-freebsd/amd64-$1-freebsd/;
      my $CPU; # CPU type as reported by config.guess.
      my $OS;  # O/S type as reported by config.guess.
      ($CPU = $guessed_platform) =~ s/(.*?)-.*/$1/;
      $CPU =~ s/^alpha(.*)/alpha/;   # alphaev56 or whatever
      $CPU =~ s/powerpc64/powerpc/;  # we don't distinguish on ppc64
      for my $os (@OSs) {
        $OS = $os if $guessed_platform =~ /$os/;
      }
      if ($OS eq "darwin") {
        $CPU = "universal"; # TL provides universal binaries
      } elsif ($CPU =~ /^i.86$/) {
        $CPU =~ s/i.86/i386/;
      }
      unless (defined $OS) {
        ($OS = $guessed_platform) =~ s/.*-(.*)/$1/;
      }
      $::_platform_ = "$CPU-$OS";
    }
  }
  return $::_platform_;
}


=item C<platform_desc($platform)>

Return a string which describes a particular platform identifier, e.g.,
given C<i386-linux> we return C<Intel x86 with GNU/Linux>.

=cut

sub platform_desc {
  my ($platform) = @_;

  my %platform_name=(
    'alpha-linux'    => 'DEC Alpha with GNU/Linux',
    'alphaev5-osf'   => 'DEC Alphaev5 OSF',
    'amd64-freebsd'  => 'x86_64 with FreeBSD',
    'hppa-hpux'      => 'HP-UX',
    'i386-cygwin'    => 'Intel x86 with Cygwin',
    'i386-darwin'    => 'Intel x86 with MacOSX/Darwin',
    'i386-freebsd'   => 'Intel x86 with FreeBSD',
    'i386-openbsd'   => 'Intel x86 with OpenBSD',
    'i386-netbsd'    => 'Intel x86 with NetBSD',
    'i386-linux'     => 'Intel x86 with GNU/Linux',
    'i386-solaris'   => 'Intel x86 with Sun Solaris',
    'mips-irix'      => 'SGI IRIX',
    'powerpc-aix'    => 'PowerPC with AIX',
    'powerpc-darwin' => 'PowerPC with MacOSX/Darwin',
    'powerpc-linux'  => 'PowerPC with GNU/Linux',
    'sparc-linux'    => 'Sparc with GNU/Linux',
    'sparc-solaris'  => 'Sparc with Solaris',
    'universal-darwin' => 'universal binaries for MacOSX/Darwin',
    'win32'          => 'Windows',
    'x86_64-linux'   => 'x86_64 with GNU/Linux'
      );

  # the inconsistency between amd64-freebsd and x86_64-linux is
  # unfortunate (it's the same hardware), but the os people say those
  # are the conventional names on the respective os's, so ...

  if (exists $platform_name{$platform}) {
    return "$platform_name{$platform}";
  } else {
    my ($CPU,$OS) = split ('-', $platform);
    return "$CPU with " . ucfirst "$OS";
  }
}


=item C<win32>

Return C<1> if platform is Windows and C<0> otherwise.  The test is
currently based on the value of Perl's C<$^O> variable.

=cut

sub win32
{
  if ($^O=~/^MSWin(32|64)$/i) {
    return 1;
  } else {
    return 0;
  }
  # the following needs config.guess, which is quite bad ...
  # return (&platform eq "win32")? 1:0;
}


=item C<unix>

Return C<1> if platform is UNIX and C<0> otherwise.

=cut

sub unix {
  return (&platform eq "win32")? 0:1;
}


=back

=head2 System Tools

=over 4

=item C<getenv($string)>

Get an environment variable.  It is assumed that the environment
variable contains a path.  On Windows all backslashes are replaced by
forward slashes as required by Perl.  If this behavior is not desired,
use C<$ENV{"$variable"}> instead.  C<0> is returned if the
environment variable is not set.

=cut

sub getenv {
  my $envvar=shift;
  my $var=$ENV{"$envvar"};
  return 0 unless (defined $var);
  if (&win32) {
    $var=~s!\\!/!g;  # change \ -> / (required by Perl)
  }
  return "$var";
}


=item C<which($string)>

C<which> does the same as the UNIX command C<which(1)>, but it is
supposed to work on Windows too.  On Windows we have to try all the
extensions given in the C<PATHEXT> environment variable.  We also try
without appending an extension because if C<$string> comes from an
environment variable, an extension might aleady be present.

=cut

sub which {
  my ($prog) = @_;
  my @PATH;
  my $PATH = getenv('PATH');

  if (&win32) {
    my @PATHEXT = split (';', getenv('PATHEXT'));
    push (@PATHEXT, '');  # in case argument contains an extension
    @PATH = split (';', $PATH);
    for my $dir (@PATH) {
      for my $ext (@PATHEXT) {
        if (-f "$dir/$prog$ext") {
          return "$dir/$prog$ext";
        }
      }
    }

  } else { # not windows
    @PATH = split (':', $PATH);
    for my $dir (@PATH) {
      if (-x "$dir/$prog") {
        return "$dir/$prog";
      }
    }
  }
  return 0;
}

=item C<get_system_tmpdir>

Evaluate the environment variables C<TMPDIR>, C<TMP>, and C<TEMP> in
order to find the system temporary directory.

=cut

sub get_system_tmpdir {
  my $systmp=0;
  $systmp||=getenv 'TMPDIR';
  $systmp||=getenv 'TMP';
  $systmp||=getenv 'TEMP';
  $systmp||='/tmp';
  return "$systmp";
}

=item C<tl_tmpdir>

Create a temporary directory which is cleaned up as soon as the program 
is terminated.

=cut

sub tl_tmpdir {
  return (File::Temp::tempdir(CLEANUP => 1));
}

=item C<xchdir($dir)>

C<chdir($dir)> or die.

=cut

sub xchdir
{
  my ($dir) = @_;
  chdir($dir) || die "$0: chdir($dir) failed: $!";
  ddebug("xchdir($dir) ok\n");
}


=item C<xsystem(@args)>

Run C<system(@args)> and die if unsuccessfully.

=cut

sub xsystem
{
  my (@args) = @_;
  ddebug("running system(@args)\n");
  my $retval = system(@args);
  if ($retval != 0) {
    $retval /= 256 if $retval > 0;
    my $pwd = cwd ();
    die "$0: system(@args) failed in $pwd, status $retval";
  }
}


=back

=head2 File Utilities

=over 4

=item C<dirname($path)>

Return C<$path> with its trailing C</component> removed.

=cut

sub dirname {
  my $path=shift;
  if (win32) {
    $path=~s!\\!/!g;
  }
  if ($path=~m!/!) {  # dirname("foo/bar/baz") -> "foo/bar"
    $path=~m!(.*)/.*!;
    return $1;
  } else {              # dirname("ignore") -> "."
    return ".";
  }
}


=item C<basename($path)>

Return C<$path> with any leading directory components removed.

=cut

sub basename {
  my $path=shift;
  if (win32) {
    $path=~s!\\!/!g;
  }
  if ($path=~m!/!) {  # basename("foo/bar") -> "bar"
    $path=~m!.*/(.*)!;
    return $1;
  } else {            # basename("ignore") -> "ignore"
    return $path;
  }
}


=item C<dirname_and_basename($path)>

Return both C<dirname> and C<basename>.  Example:

  ($dirpart,$filepart) = dirname_and_basename ($path);

=cut

sub dirname_and_basename {
  my $path=shift;
  if (win32) {
    $path=~s!\\!/!g;
  }
  $path=~/(.*)\/(.*)/;
  return ("$1", "$2");
}


=item C<dir_writable($path)>

Tests whether its argument is writable by trying to write to
it. This function is necessary because the built-in C<-w> test just
looks at mode and uid/guid, which on Windows always returns true and
even on Unix is not always good enough for directories mounted from
a fileserver.

=cut

# Theoretically, the test below, which uses numbers as names, might
# lead to a race condition. OTOH, it should work even on a very
# broken Perl.

# The Unix test gives the wrong answer when used under Windows Vista
# with one of the `virtualized' directories such as Program Files:
# lacking administrative permissions, it would write successfully to
# the virtualized Program Files rather than fail to write to the
# real Program Files. Ugh.

sub dir_writable {
  $path=shift;
  return 0 unless -d $path;
  $path =~ s!\\!/!g if win32;
  $path =~ s!/$!!g;
  my $i = 0;
  while (-e $path . "/" . $i) { $i++; }
  my $f = $path."/".$i;
  if (win32) {
    my $fb = $f;
    $fb =~ s!/!\\!g;
    return 0 if
      system('copy /b ' . $ENV{'COMSPEC'} . ' "' . $fb . '" >nul 2>&1');
    unlink $f if -e $f;
    return 1;
  } else {
    return 0 unless open TEST, ">".$f;
    my $written = 0;
    $written = (print TEST "\n");
    close TEST;
    unlink $f;
    return $written;
  }
}


=item C<mkdirhier($path, [$mode])>

The function C<mkdirhier> does the same as the UNIX command C<mkdir -p>.
The optional parameter sets the permission flags.

=cut

sub mkdirhier {
  my ($tree,$mode) = @_;

  return if (-d "$tree");
  my $subdir = "";

  @dirs = split (/\//, $tree);
  for my $dir (@dirs) {
    $subdir .= "$dir/";
    if (! -d $subdir) {
      if (defined $mode) {
        mkdir ($subdir, $mode)
        || die "$0: mkdir($subdir,$mode) failed, goodbye: $!\n";
      } else {
        mkdir ($subdir) || die "$0: mkdir($subdir) failed, goodbye: $!\n";
      }
    }
  }
}


=item C<rmtree($root, $verbose, $safe)>

The C<rmtree> function provides a convenient way to delete a
subtree from the directory structure, much like the Unix command C<rm -r>.
C<rmtree> takes three arguments:

=over 4

=item *

the root of the subtree to delete, or a reference to
a list of roots.  All of the files and directories
below each root, as well as the roots themselves,
will be deleted.

=item *

a boolean value, which if TRUE will cause C<rmtree> to
print a message each time it examines a file, giving the
name of the file, and indicating whether it's using C<rmdir>
or C<unlink> to remove it, or that it's skipping it.
(defaults to FALSE)

=item *

a boolean value, which if TRUE will cause C<rmtree> to
skip any files to which you do not have delete access
(if running under VMS) or write access (if running
under another OS).  This will change in the future when
a criterion for 'delete permission' under OSs other
than VMS is settled.  (defaults to FALSE)

=back

It returns the number of files successfully deleted.  Symlinks are
simply deleted and not followed.

B<NOTE:> There are race conditions internal to the implementation of
C<rmtree> making it unsafe to use on directory trees which may be
altered or moved while C<rmtree> is running, and in particular on any
directory trees with any path components or subdirectories potentially
writable by untrusted users.

Additionally, if the third parameter is not TRUE and C<rmtree> is
interrupted, it may leave files and directories with permissions altered
to allow deletion (and older versions of this module would even set
files and directories to world-read/writable!)

Note also that the occurrence of errors in C<rmtree> can be determined I<only>
by trapping diagnostic messages using C<$SIG{__WARN__}>; it is not apparent
from the return value.

=cut

#taken from File/Path.pm
#
my $Is_VMS = $^O eq 'VMS';
my $Is_MacOS = $^O eq 'MacOS';

# These OSes complain if you want to remove a file that you have no
# write permission to:
my $force_writeable = ($^O eq 'os2' || $^O eq 'dos' || $^O eq 'MSWin32' ||
		       $^O eq 'amigaos' || $^O eq 'MacOS' || $^O eq 'epoc');

sub rmtree {
  my($roots, $verbose, $safe) = @_;
  my(@files);
  my($count) = 0;
  $verbose ||= 0;
  $safe ||= 0;

  if ( defined($roots) && length($roots) ) {
    $roots = [$roots] unless ref $roots;
  } else {
    warn "No root path(s) specified";
    return 0;
  }

  my($root);
  foreach $root (@{$roots}) {
    if ($Is_MacOS) {
      $root = ":$root" if $root !~ /:/;
      $root =~ s#([^:])\z#$1:#;
    } else {
      $root =~ s#/\z##;
    }
    (undef, undef, my $rp) = lstat $root or next;
    $rp &= 07777;	# don't forget setuid, setgid, sticky bits
    if ( -d _ ) {
      # notabene: 0700 is for making readable in the first place,
      # it's also intended to change it to writable in case we have
      # to recurse in which case we are better than rm -rf for
      # subtrees with strange permissions
      chmod($rp | 0700, ($Is_VMS ? VMS::Filespec::fileify($root) : $root))
        or warn "Can't make directory $root read+writeable: $!"
          unless $safe;

      if (opendir my $d, $root) {
        no strict 'refs';
        if (!defined ${"\cTAINT"} or ${"\cTAINT"}) {
          # Blindly untaint dir names
          @files = map { /^(.*)$/s ; $1 } readdir $d;
        } else {
          @files = readdir $d;
        }
        closedir $d;
      } else {
        warn "Can't read $root: $!";
        @files = ();
      }
      # Deleting large numbers of files from VMS Files-11 filesystems
      # is faster if done in reverse ASCIIbetical order
      @files = reverse @files if $Is_VMS;
      ($root = VMS::Filespec::unixify($root)) =~ s#\.dir\z## if $Is_VMS;
      if ($Is_MacOS) {
        @files = map("$root$_", @files);
      } else {
        @files = map("$root/$_", grep $_!~/^\.{1,2}\z/s,@files);
      }
      $count += rmtree(\@files,$verbose,$safe);
      if ($safe &&
            ($Is_VMS ? !&VMS::Filespec::candelete($root) : !-w $root)) {
        print "skipped $root\n" if $verbose;
        next;
      }
      chmod $rp | 0700, $root
        or warn "Can't make directory $root writeable: $!"
          if $force_writeable;
      print "rmdir $root\n" if $verbose;
      if (rmdir $root) {
	      ++$count;
      } else {
        warn "Can't remove directory $root: $!";
        chmod($rp, ($Is_VMS ? VMS::Filespec::fileify($root) : $root))
          or warn("and can't restore permissions to "
            . sprintf("0%o",$rp) . "\n");
      }
    } else {
      if ($safe &&
            ($Is_VMS ? !&VMS::Filespec::candelete($root)
              : !(-l $root || -w $root)))
      {
        print "skipped $root\n" if $verbose;
        next;
      }
      chmod $rp | 0600, $root
        or warn "Can't make file $root writeable: $!"
          if $force_writeable;
      print "unlink $root\n" if $verbose;
      # delete all versions under VMS
      for (;;) {
        unless (unlink $root) {
          warn "Can't unlink file $root: $!";
          if ($force_writeable) {
            chmod $rp, $root
              or warn("and can't restore permissions to "
                . sprintf("0%o",$rp) . "\n");
          }
          last;
        }
        ++$count;
        last unless $Is_VMS && lstat $root;
      }
    }
  }
  $count;
}


=item C<copy($file, $target_dir)>

=item C<copy("-f", $file, $destfile)>

Copy file C<$file> to directory C<$target_dir>, or to the C<$destfile> in
the second case.  No external programs
are involved.  Since we need C<sysopen()>, the Perl module C<Fcntl.pm>
is required.  The time stamps are preserved and symlinks are created
on UNIX systems.  On Windows, C<(-l $file)> will certainly never
return 'C<true>' and symlinks will be copied as regular files.

C<copy> invokes C<mkdirhier> if target directories do not exist.
Files have mode C<0777>-I<umask> if they are executable and
C<0666>-I<umask> otherwise.

Note that C<copy> will work with file:/ prefixes, too.

=cut

sub copy {
  my $infile=shift;
  my $filemode = 0;
  if ($infile eq "-f") {
    # second argument is a file!!!
    $filemode = 1;
    $infile = shift;
  }
  my $destdir=shift;
  my $outfile;
  my @stat;
  my $mode;
  my $buffer;
  my $offset;
  my $filename;
  my $dirmode=0755;
  my $blocksize=2048;

  $infile =~ s!^file://*!/!i;
  $filename=basename "$infile";
  if ($filemode) {
    # we actually got a destination file
    $outfile = $destdir;
    $destdir = dirname($outfile);
  } else {
    $outfile="$destdir/$filename";
  }

  mkdirhier ("$destdir") unless -d "$destdir";

  if (-l "$infile") {
    symlink readlink "$infile", "$destdir/$filename";
  } else {
    open (IN, $infile) || die "open($infile) failed: $!";
    binmode IN;

    $mode=(-x "$infile")? oct("0777"):oct("0666");
    $mode-=umask;

    open (OUT, ">$outfile") || die "open(>$outfile) failed: $!";
    binmode OUT;

    chmod $mode, "$outfile";

    while ($read=sysread IN, $buffer, $blocksize) {
      die "system read error: $!\n" unless defined $read;
      $offset=0;
      while ($read) {
        $written=syswrite OUT, $buffer, $read, $offset;
        die "system write error: $!\n" unless defined $written;
        $read-=$written;
        $offset+=$written;
      }
    }
    close OUT;
    close IN;
    @stat=lstat "$infile";
    utime $stat[8], $stat[9], "$outfile";
  }
}


=item C<touch(@files)>

Update modification and access time of C<@files>.  Non-existent files
are created.

=cut

sub touch {
  my @files=@_;
  
  foreach my $file (@_) {
    if (-e $file) {
	    utime time, time, $file;
    } else {
	    open TMP, ">>$file" && close TMP
          or warn "Can't update timestamps of $file: $!\n";
    }
  }
}





=item C<collapse_dirs(@files)>

Return a (more or less) minimal list of directories and files, given an
original list of files C<@files>.  That is, if every file within a given
directory is included in C<@files>, replace all of those files with the
absolute directory name in the return list.  Any files which have
sibling files not included are retained and made absolute.

We try to walk up the tree so that the highest-level directory
containing only directories or files that are in C<@files> is returned.
(This logic may not be perfect, though.)

This is not just a string function; we check for other directory entries
existing on disk within the directories of C<@files>.  Therefore, if the
entries are relative pathnames, the current directory must be set by the
caller so that file tests work.

As mentioned above, the returned list is absolute paths to directories
and files.

For example, suppose the input list is

  dir1/subdir1/file1
  dir1/subdir2/file2
  dir1/file3

If there are no other entries under C<dir1/>, the result will be
C</absolute/path/to/dir1>.

=cut

sub collapse_dirs
{
  my (@files) = @_;
  my @ret = ();
  my %by_dir;
  
  # construct hash of all directories mentioned, values are lists of the
  # files in that directory.
  for my $f (@files) {
    my $abs_f = Cwd::abs_path ($f);
    die ("oops, no abs_path($f) from " . `pwd`) unless $abs_f;
    (my $d = $abs_f) =~ s,/[^/]*$,,;
    my @a = exists $by_dir{$d} ? @{$by_dir{$d}} : ();
    push (@a, $abs_f);
    $by_dir{$d} = \@a;
  }
  
  # for each of our directories, see if we are given everything in
  # the directory.  if so, return the directory; else return the
  # individual files.
  for my $d (sort keys %by_dir) {
    opendir (DIR, $d) || die "opendir($d) failed: $!";
    my @dirents = readdir (DIR);
    closedir (DIR) || warn "closedir($d) failed: $!";
    
    # initialize test hash with all the files we saw in this dir.
    # (These idioms are due to "Finding Elements in One Array and Not
    # Another" in the Perl Cookbook.)
    my %seen;
    my @rmfiles = @{$by_dir{$d}};
    @seen{@rmfiles} = ();

    # see if everything is the same.
    my $ok_to_collapse = 1;
    for my $dirent (@dirents) {
      next if $dirent =~ /^\.(\.|svn)?$/;  # ignore . .. .svn

      my $item = "$d/$dirent";  # prepend directory for comparison
      if (! exists $seen{$item}) {
        $ok_to_collapse = 0;
        last;  # no need to keep looking after the first.
      }
    }
    
    push (@ret, $ok_to_collapse ? $d : @{$by_dir{$d}});
  }
  
  if (@ret != @files) {
    @ret = &collapse_dirs (@ret);
  }
  return @ret;
}


=item C<install_packages($from_tlpdb, $media, $to_tlpdb, $what, $opt_src, $opt_doc)>

Installs the list of packages found in C<@$what> (a ref to a list) into
the TLPDB given by C<$to_tlpdb>. Information on files are taken from
the TLPDB C<$from_tlpdb>.

C<$opt_src> and C<$opt_doc> specify whether srcfiles and docfiles should be
installed (currently implemented only for installation from DVD).

Returns 1 on success and 0 on error.

=cut

sub install_packages {
  my ($fromtlpdb,$media,$totlpdb,$what,$opt_src,$opt_doc) = @_;
  my $container_src_split = $fromtlpdb->config_src_container;
  my $container_doc_split = $fromtlpdb->config_doc_container;
  my $root = $fromtlpdb->root;
  my @packs = @$what;
  my $totalnr = $#packs + 1;
  my $td = length("$totalnr");
  my $n = 0;
  my %tlpobjs;
  my $totalsize = 0;
  my $donesize = 0;
  my %tlpsizes;
  foreach my $p (@packs) {
    $tlpobjs{$p} = $fromtlpdb->get_package($p);
    if (!defined($tlpobjs{$p})) {
      die "STRANGE: $p not to be found in ", $fromtlpdb->root;
    }
    if ($media ne 'DVD') {
      # we use the container size as the measuring unit since probably
      # downloading will be the limiting factor
      $tlpsizes{$p} = $tlpobjs{$p}->containersize;
      $tlpsizes{$p} += $tlpobjs{$p}->srccontainersize if $opt_src;
      $tlpsizes{$p} += $tlpobjs{$p}->doccontainersize if $opt_doc;
    } else {
      # we have to add the respective sizes, that is checking for 
      # installation of src and doc file
      $tlpsizes{$p} = $tlpobjs{$p}->runsize;
      $tlpsizes{$p} += $tlpobjs{$p}->srcsize if $opt_src;
      $tlpsizes{$p} += $tlpobjs{$p}->docsize if $opt_doc;
      my %foo = %{$tlpobjs{$p}->binsize};
      for my $k (keys %foo) { $tlpsizes{$p} += $foo{$k}; }
      # all the packages sizes are in blocks, so transfer that to bytes
      $tlpsizes{$p} *= $TeXLive::TLConfig::BlockSize;
    }
    $totalsize += $tlpsizes{$p};
  }
  my $starttime = time();
  foreach my $package (@packs) {
    my $tlpobj = $tlpobjs{$package};
    $n++;
    my $remtime = "??:??";
    my $tottime = "??:??";
    if ($donesize > 0) {
      # try to compute the remaining time
      my $curtime = time();
      my $passedtime = $curtime - $starttime;
      my $esttotalsecs = int ( ( $passedtime * $totalsize ) / $donesize );
      my $remsecs = $esttotalsecs - $passedtime;
      my $min = int($remsecs/60);
      my $hour;
      if ($min >= 60) {
        $hour = int($min/60);
        $min %= 60;
      }
      my $sec = $remsecs % 60;
      $remtime = sprintf("%02d:%02d", $min, $sec);
      if ($hour) {
        $remtime = sprintf("%02d:$remtime", $hour);
      }
      my $tmin = int($esttotalsecs/60);
      my $thour;
      if ($tmin >= 60) {
        $thour = int($tmin/60);
        $tmin %= 60;
      }
      my $tsec = $esttotalsecs % 60;
      $tottime = sprintf("%02d:%02d", $tmin, $tsec);
      if ($thour) {
        $tottime = sprintf("%02d:$tottime", $thour);
      }
    }
    my $infostr = sprintf("Installing [%0${td}d/$totalnr, "
                     . "time/total: $remtime/$tottime]: $package [%dk]",
                     $n, int($tlpsizes{$package}/1024) + 1);
    info("$infostr\n");
    foreach my $h (@::install_packages_hook) {
      &$h($n,$totalnr);
    }
    my $real_opt_doc = $opt_doc;
    # if we install a package from the Documentation class we
    # reactivate the do_doc in any case. It should apply ONLY for fonts
    # and macros!
    if ($tlpobj->category =~ m/documentation/i) {
      $real_opt_doc = 1;
    }
    my $container;
    my @installfiles;
    push @installfiles, $tlpobj->runfiles;
    push @installfiles, $tlpobj->allbinfiles;
    push @installfiles, $tlpobj->srcfiles if ($opt_src);
    push @installfiles, $tlpobj->docfiles if ($real_opt_doc);
    if ($media eq 'DVD') {
      $container = [ $root, @installfiles ];
    } elsif ($media eq 'CD') {
      if (-r "$root/$Archive/$package.zip") {
        $container = "$root/$Archive/$package.zip";
      } elsif (-r "$root/$Archive/$package.tar.lzma") {
        $container = "$root/$Archive/$package.tar.lzma";
      } else {
        tlwarn("No package $package (.zip or .lzma) in $root/$Archive\n");
        next;
      }
    } elsif ($media eq 'NET') {
      $container = "$root/$Archive/$package.$DefaultContainerExtension";
    }
    if (!install_package($container, $tlpobj->containersize, 
                         $tlpobj->containermd5, \@installfiles, 
                         $totlpdb->root, $vars{'this_platform'})) {
      # we already warn in install_package that something bad happened,
      # so only return here
      return 0;
    }
    # if we are installing from CD or NET we have to fetch the respective
    # source and doc packages $pkg.source and $pkg.doc and install them, too
    if (($media eq 'NET') || ($media eq 'CD')) {
      # we install split containers under the following conditions:
      # - the container were split generated
      # - src/doc files should be installed
      # (- the package is not already a split one (like .i386-linux))
      # the above test has been removed since that would mean that packages
      # with a dot like texlive.infra will never have the docfiles installed
      # that is already happening ...bummer. But since we already check
      # whether there are src/docfiles present at all that is fine
      # - there are actually src/doc files present
      if ($container_src_split && $opt_src && $tlpobj->srcfiles) {
        my $srccontainer = $container;
        $srccontainer =~ s/(\.tar\.lzma|\.zip)$/.source$1/;
        if (!install_package($srccontainer, $tlpobj->srccontainersize,
                             $tlpobj->srccontainermd5, \@installfiles,
                             $totlpdb->root, $vars{'this_platform'})) {
          return 0;
        }
      }
      if ($container_doc_split && $real_opt_doc && $tlpobj->docfiles) {
        my $doccontainer = $container;
        $doccontainer =~ s/(\.tar\.lzma|\.zip)$/.doc$1/;
        if (!install_package($doccontainer,
                             $tlpobj->doccontainersize,
                             $tlpobj->doccontainermd5, \@installfiles,
                             $totlpdb->root, $vars{'this_platform'})) {
          return 0;
        }
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
    $totlpdb->add_tlpobj($tlpobj);
    # we have to write out the tlpobj file since it is contained in the
    # archives (.tar.lzma) but at DVD install time we don't have them
    my $tlpod = $totlpdb->root . "/tlpkg/tlpobj";
    mkdirhier( $tlpod );
    open(TMP,">$tlpod/".$tlpobj->name.".tlpobj") ||
      die "$0: open tlpobj " . $tlpobj->name . "failed: $!";
    $tlpobj->writeout(\*TMP);
    close(TMP);
    $donesize += $tlpsizes{$package};
  }
  my $totaltime = time() - $starttime;
  my $totmin = int ($totaltime/60);
  my $totsec = $totaltime % 60;
  info(sprintf("Time used for installing the packages: %02d:%02d\n", 
       $totmin, $totsec));
  $totlpdb->save;
  return 1;
}


=item C<install_package($what, $size, $md5, $filelistref, $target, $platform)>

This function installs the files given in @$filelistref from C<$what>
into C<$target>.

C<$size> gives the size in bytes of the container, or -1 if we are
installing from DVD, i.e., from a list of files to be copied.

If C<$what> is a reference to a list of files then these files are
assumed to be readable and are copied to C<$target>, creating dirs on
the way. In this case the list C<@$filelistref> is not taken into
account.

If C<$what> starts with C<http://> or C<ftp://> then C<$what> is
downloaded from the net and piped through C<lzmadec> and C<tar>.

If $what ends with C<.tar.lzma> (but does not start with C<http://> or
C<ftp://>, but possibly with C<file:/>) it is assumed to be a readable
file on the system and is likewise piped through C<lzmadec> and C<tar>.

In both of these cases currently the list C<$@filelistref> currently
is not taken into account (should be fixed!).

Returns 1 on success and 0 on error.

=cut

sub install_package {
  my ($what, $whatsize, $whatmd5, $filelistref, $target, $platform) = @_;

  my @filelist = @$filelistref;

  # we assume that $::progs has been set up!
  my $wget = $::progs{'wget'};
  my $lzmadec = $::progs{'lzmadec'};
  if (!defined($wget) || !defined($lzmadec)) {
    tlwarn("install_package: wget/lzmadec programs not set up properly.\n");
    return 0;
  }
  if (ref $what) {
    # we are getting a ref to a list of files, so install from DVD
    my ($root, @files) = @$what;
    foreach my $file (@files) {
      # @what is taken, not @filelist!
      # is this still needed?
      my $dn=dirname($file);
      mkdirhier("$target/$dn");
      copy "$root/$file", "$target/$dn";
    }
  } elsif ($what =~ m,\.tar.lzma$,) {
    # this is the case when we install from CD or the NET
    #
    # in all other cases we create temp files .tar.lzma (or use the present
    # one), lzmadec them, and then call tar

    my $fn = basename($what);
    mkdirhier("$target/temp");
    my $lzmafile = "$target/temp/$fn";
    my $tarfile  = "$target/temp/$fn"; $tarfile =~ s/\.lzma$//;
    my $lzmafile_quote = $lzmafile;
    my $tarfile_quote = $tarfile;
    if (win32()) {
      $lzmafile =~ s!/!\\!g;
      $tarfile =~ s!/!\\!g;
      $target =~ s!/!\\!g;
    }
    $lzmafile_quote = "\"$lzmafile\"";
    $tarfile_quote = "\"$tarfile\"";
    my $gotfiledone = 0;
    if (-r $lzmafile) {
      # check that the downloaded file is not partial
      if ($whatsize >= 0) {
        # we have the size given, so check that first
        my $size = (stat $lzmafile)[7];
        if ($size == $whatsize) {
          # we want to check also the md5sum if we have it present
          if ($whatmd5) {
            if (tlmd5($lzmafile) eq $whatmd5) {
              $gotfiledone = 1;
            } else {
              tlwarn("Downloaded $what, size equal, but md5sum differs;\n",
                     "downloading again.\n");
            }
          } else {
            # size ok, no md5sum
            tlwarn("Downloaded $what, size equal, but no md5sum available;\n",
                   "continuing, with fingers crossed.");
            $gotfiledone = 1;
          }
        } else {
          tlwarn("Partial download of $what found, removing it.\n");
          unlink($tarfile, $lzmafile);
        }
      } else {
        # ok no size information, hopefully we have md5 sums
        if ($whatmd5) {
          if (tlmd5($lzmafile) eq $whatmd5) {
            $gotfiledone = 1;
          } else {
            tlwarn("Downloaded file, but md5sum differs, removing it.\n");
          }
        } else {
          tlwarn("Container found, but cannot verify size of md5sum;\n",
                 "continuing, with fingers crossed.\n");
          $gotfiledone = 1;
        }
      }
      debug("Reusing already downloaded container $lzmafile\n")
        if ($gotfiledone);
    }
    if (!$gotfiledone) {
      if ($what =~ m,http://|ftp://,) {
        # we are installing from the NET
        # download the file and put it into temp
        if (!download_file($what, $lzmafile) || (! -r $lzmafile)) {
          tlwarn("Downloading $what did not succeed.\n");
          return 0;
        }
      } else {
        # we are installing from CD
        # copy it to temp
        copy($what, "$target/temp");
      }
    }
    debug("un-lzmaing $lzmafile to $tarfile\n");
    system("$lzmadec < $lzmafile_quote > $tarfile_quote");
    if (! -f $tarfile) {
      tlwarn("Unpacking $lzmafile did not succeed.\n");
      return 0;
    }
    if (!TeXLive::TLUtils::untar($tarfile, $target, 1)) {
      tlwarn("Un-tarring $tarfile did not succeed.\n");
      return 0;
    }
  } else {
    tlwarn("Sorry, no idea how to install $what\n");
    return 0;
  }
  return 1;
}


=item C<untar($tarfile,$targetdir, $remove_tarfile)>

Unpacked C<$tarfile> in C<$targetdir> (changing directories to
C<$targetdir> and then back to the original directory).  If
C<$remove_tarfile> is true, unlink C<$tarfile> after unpacking.

Assumes the global C<$::progs{"tar"}> has been set up.

=cut

# return 1 if success, 0 if failure.
sub untar {
  my ($tarfile, $targetdir, $remove_tarfile) = @_;
  my $ret;

  my $tar = $::progs{'tar'};  # assume it's been set up
  
  # don't use the -C option to tar since Solaris tar et al. don't support it.
  # don't use system("cd ... && $tar ...") since that opens us up to
  # quoting issues.
  # so fall back on chdir in Perl.
  # 
  debug("unpacking $tarfile in $targetdir\n");
  my $cwd = cwd();
  chdir($targetdir) || die "chdir($targetdir) failed: $!";

  if (system($tar, "xf", $tarfile) != 0) {
    tlwarn("untarring $tarfile failed, please retry\n");
    $ret = 0;
  } else {
    $ret = 1;
  }
  unlink($tarfile) if $remove_tarfile;

  chdir($cwd) || die "chdir($cwd) failed: $!";
  return $ret;
}



=item C<setup_programs($bindir, $platform)>

Populate the global C<$::progs> hash containing the paths to the
programs C<wget>, C<tar>, C<lzmadec>. The C<$bindir> argument specifies
the path to the location of the C<lzmadec> binaries, the C<$platform>
gives the TeX Live platform name, used as the extension on our
executables.  If a program is not present in the TeX Live tree, we also
check along PATH (without the platform extension.)

Return 0 if failure, nonzero if success.

=cut

sub setup_programs {
  my ($bindir, $platform) = @_;
  my $ok = 1;
  
  $::progs{'wget'} = "wget";
  $::progs{'lzmadec'} = "lzmadec";
  $::progs{'lzma'} = "lzma";
  $::progs{'tar'} = "tar";

  if ($^O =~ /^MSWin(32|64)$/i) {
    $::progs{'wget'}    = conv_to_w32_path("$bindir/wget/wget.exe");
    $::progs{'tar'}     = conv_to_w32_path("$bindir/tar.exe");
    $::progs{'lzmadec'} = conv_to_w32_path("$bindir/lzma/lzmadec.win32.exe");
    $::progs{'lzma'}    = conv_to_w32_path("$bindir/lzma/lzma.exe");
    for my $prog ("lzmadec", "wget") {
      my $opt = $prog eq "lzmadec" ? "--help" : "--version";
      my $ret = system("$::progs{$prog} $opt >nul 2>&1"); # on windows
      if ($ret != 0) {
        warn "TeXLive::TLUtils::setup_programs (w32) failed";  # no nl for perl
        warn "$::progs{$prog} $opt failed (status $ret): $!\n";
        warn "Output is:\n";
        system ("$::progs{$prog} $opt");
        warn "\n";
        $ok = 0;
      }
    }
  } else {
    if (!defined($platform) || ($platform eq "")) {
      # we assume that we run from the DVD, so we can call platform() and
      # thus also the config.guess script
      # but we have to setup $::installerdir because the platform script
      # relies on it
      $::installerdir = "$bindir/../..";
      $platform = platform();
    }
    my $s = 0;
    $s += setup_unix_one('wget', "$bindir/wget/wget.$platform", "--version");
    $s += setup_unix_one('lzmadec',"$bindir/lzma/lzmadec.$platform","--help");
    $s += setup_unix_one('lzma', "$bindir/lzma/lzma.$platform", "notest");
    $ok = ($s == 3);  # failure return unless all are present.
  }

  return $ok;
}


# setup one prog on unix using the following logic:
# - if the shipped one is -x and can be executed, use it
# - if the shipped one is -x but cannot be executed, copy it. set -x
#   . if the copy is -x and executable, use it
#   . if the copy is not executable, GOTO fallback
# - if the shipped one is not -x, copy it, set -x
#   . if the copy is -x and executable, use it
#   . if the copy is not executable, GOTO fallback
# - if nothing shipped, GOTO fallback
#
# fallback:
# if prog is found in PATH and can be executed, use it.
# 
# Return 0 if failure, 1 if success.
#
sub setup_unix_one {
  my ($p, $def, $arg) = @_;
  our $tmp;
  my $test_fallback = 0;
  if (-r $def) {
    my $ready = 0;
    if (-x $def) {
      # checking only for the executable bit is not enough, we have
      # to check for actualy "executability" since a "noexec" mount
      # option may interfere, which is not taken into account by
      # perl's -x test.
      $::progs{$p} = $def;
      if ($arg ne "notest") {
        my $ret = system("$def $arg > /dev/null 2>&1" ); # we are on Unix
        if ($ret == 0) {
          $ready = 1;
          debug("Using shipped $def for $p (tested).\n");
        } else {
          ddebug("Shipped $def has -x but cannot be executed.\n");
        }
      } else {
        # do not test, just return
        $ready = 1;
        debug("Using shipped $def for $p (not tested).\n");
      }
    }
    if (!$ready) {
      # out of some reasons we couldn't execute the shipped program
      # try to copy it to a temp directory and make it executable
      #
      # create tmp dir only when necessary
      $tmp = TeXLive::TLUtils::tl_tmpdir() unless defined($tmp);
      # probably we are running from DVD and want to copy it to 
      # some temporary location
      copy($def, $tmp);
      my $bn = basename($def);
      $::progs{$p} = "$tmp/$bn";
      chmod(0755,$::progs{$p});
      # we do not check the return value of chmod, but check whether
      # the -x bit is now set, the only thing that counts
      if (! -x $::progs{$p}) {
        # hmm, something is going really bad, not even the copy is
        # executable. Fall back to normal path element
        $test_fallback = 1;
        ddebug("Copied $p $::progs{$p} does not have -x bit, strange!\n");
      } else {
        # check again for executability
        if ($arg ne "notest") {
          my $ret = system("$::progs{$p} $arg > /dev/null 2>&1");
          if ($ret == 0) {
            # ok, the copy works
            debug("Using copied $::progs{$p} for $p (tested).\n");
          } else {
            # even the copied prog is not executable, strange
            $test_fallback = 1;
            ddebug("Copied $p $::progs{$p} has x bit but not executable, strange!\n");
          }
        } else {
          debug("Using copied $::progs{$p} for $p (not tested).\n");
        }
      }
    }
  } else {
    # hope that we can find in in the global PATH
    $test_fallback = 1;
  }
  if ($test_fallback) {
    # all our playing around and copying did not succeed, try the 
    # fallback
    $::progs{$p} = $p;
    if ($arg ne "notest") {
      my $ret = system("$p $arg > /dev/null 2>&1");
      if ($ret == 0) {
        debug("Using system $p (tested).\n");
      } else {
        tlwarn("$0: Initialization failed (in setup_unix_one):\n");
        tlwarn("  could not find a usable program for $p.\n");
        return 0;
      }
    } else {
      debug ("Using system $p (not tested).\n");
    }
  }
  return 1;
}

=item C<download_file( $relpath, $destination [, $progs ] )>

Try to download the file given in C<$relpath> from C<$TeXLiveURL>
into C<$destination>, which can be either
a filename of simply C<|>. In the latter case a file handle is returned.

The optional argument C<$progs> is a reference to a hash giving full
paths to the respective programs, at least C<wget>.  If C<$progs> is not
given the C<%::progs> hash is consulted, and if this also does not exist
we try a literal C<wget>.

Downloading honors two environment variables: C<TL_DOWNLOAD_PROGRAM> and
C<TL_DOWNLOAD_ARGS>. The former overrides the above specification
devolving to C<wget>, and the latter overrides the default wget
arguments, which are: C<--tries=8 --timeout=60 -q -O>.

C<TL_DOWNLOAD_ARGS> must be defined so that the file the output goes to
is the first argument after the C<TL_DOWNLOAD_ARGS>.  Thus, typically it
would end in C<-O>.  Use with care.

=cut

sub download_file {
  my ($relpath, $dest, $progs) = @_;
  my $wget;
  if (defined($progs) && defined($progs->{'wget'})) {
    $wget = $progs->{'wget'};
  } elsif (defined($::progs{'wget'})) {
    $wget = $::progs{'wget'};
  } else {
    tlwarn ("download_file: Programs not set up, trying literal wget\n");
    $wget = "wget";
  }
  my $url;
  if ($relpath =~ m;^file://*(.*)$;) {
    my $filetoopen = "/$1";
    # $dest is a file name, we have to get the respective dirname
    if ($dest eq "|") {
      open(RETFH, "<$filetoopen") or
        die("Cannot open $filetoopen for reading");
      # opening to a pipe always succeeds, so we return immediately
      return \*RETFH;
    } else {
      my $par = dirname ($dest);
      if (-r $filetoopen) {
        copy ($filetoopen, $par);
        return 1;
      }
      return 0;
    }
  }
  if ($relpath =~ /^(http|ftp):\/\//) {
    $url = $relpath;
  } else {
    $url = "$TeXLiveURL/$relpath";
  }
  my $ret = _download_file($url, $dest, $wget);
  return($ret);
}

sub _download_file {
  my ($url, $dest, $wgetdefault) = @_;
  if (win32()) {
    $dest =~ s!/!\\!g;
  }

  my $wget = $ENV{"TL_DOWNLOAD_PROGRAM"} || $wgetdefault;
  my $wgetargs = $ENV{"TL_DOWNLOAD_ARGS"}
                 || "--tries=8 --timeout=60 -q -O";

  debug("downloading $url using $wget $wgetargs\n");
  my $ret;
  if ($dest eq "|") {
    open(RETFH, "$wget $wgetargs - $url|")
    || die "open($url) via $wget $wgetargs failed: $!";
    # opening to a pipe always succeeds, so we return immediately
    return \*RETFH;
  } else {
    my @wgetargs = split (" ", $wgetargs);
    $ret = system ($wget, @wgetargs, $dest, $url);
    # we have to reverse the meaning of ret because system has 0=success.
    $ret = ($ret ? 0 : 1);
  }
  # return false/undef in case the download did not succeed.
  return ($ret) unless $ret;
  debug("download of $url succeeded\n");
  if ($dest eq "|") {
    return \*RETFH;
  } else {
    return 1;
  }
}


=back

=head2 Installer Functions

=over 4

=item C<make_var_skeleton($prefix)>

Generate a skeleton of empty directories in the C<TEXMFSYSVAR> tree.

=cut

sub make_var_skeleton {
  my $prefix=shift;

  mkdirhier "$prefix/tex/generic/config";
  mkdirhier "$prefix/fonts/map/dvipdfm/updmap";
  mkdirhier "$prefix/fonts/map/dvips/updmap";
  mkdirhier "$prefix/fonts/map/pdftex/updmap";
  mkdirhier "$prefix/fonts/pk";
  mkdirhier "$prefix/fonts/tfm";
  mkdirhier "$prefix/web2c";
  mkdirhier "$prefix/xdvi";
  mkdirhier "$prefix/tex/context/config";
}


=item C<make_local_skeleton($prefix)>

Generate a skeleton of empty directories in the C<TEXMFLOCAL> tree.

=cut

sub make_local_skeleton {
  my $prefix=shift;

  mkdirhier "$prefix/tex/latex/local";
  mkdirhier "$prefix/tex/plain/local";
  mkdirhier "$prefix/dvips/local";
  mkdirhier "$prefix/bibtex/bib/local";
  mkdirhier "$prefix/bibtex/bst/local";
  mkdirhier "$prefix/fonts/tfm/local";
  mkdirhier "$prefix/fonts/vf/local";
  mkdirhier "$prefix/fonts/source/local";
  mkdirhier "$prefix/fonts/type1/local";
  mkdirhier "$prefix/metapost/local";
  mkdirhier "$prefix/web2c";
}



=item C<create_fmtutil($tlpdb, $dest, $localconf)>

=item C<create_updmap($tlpdb, $dest, $localconf)>

=item C<create_language_dat($tlpdb, $dest, $localconf)>

=item C<create_language_def($tlpdb, $dest, $localconf)>

These four functions create C<fmtutil.cnf>, C<updmap.cfg>, C<language.dat>,
and C<language.def> respectively, in C<$dest> (which by default is below
C<$TEXMFSYSVAR>).  These functions merge the information present in the
TLPDB C<$tlpdb> (formats, maps, hyphenations) with local configuration
additions: C<$localconf>.

Currently the "merging" is done trivially by appending the content of
the local configuration files at the end of the file. This should be
improved (checking for duplicates).

=cut

sub create_fmtutil {
  my ($tlpdb,$dest,$localconf) = @_;
  my @lines = $tlpdb->fmtutil_cnf_lines;
  _create_config_files($tlpdb, "texmf/fmtutil/fmtutil-hdr.cnf", $dest,
                       $localconf, 0, '#', \@lines);
}

sub create_updmap {
  my ($tlpdb,$dest,$localconf) = @_;
  my @lines = $tlpdb->updmap_cfg_lines;
  _create_config_files($tlpdb, "texmf/web2c/updmap-hdr.cfg", $dest,
                       $localconf, 0, '#', \@lines);
}

sub create_language_dat {
  my ($tlpdb,$dest,$localconf) = @_;
  my @lines = $tlpdb->language_dat_lines;
  _create_config_files($tlpdb, "texmf/tex/generic/config/language.us", $dest,
                       $localconf, 0, '%', \@lines);
}

sub create_language_def {
  my ($tlpdb,$dest,$localconf) = @_;
  my @lines = $tlpdb->language_def_lines;
  my @postlines;
  push @postlines, "%%% No changes may be made beyond this point.\n";
  push @postlines, "\n";
  push @postlines, "\\uselanguage {USenglish}             %%% This MUST be the last line of the file.\n";
  _create_config_files ($tlpdb, "texmf/tex/generic/config/language.us.def", $dest, $localconf, 1, '%', \@lines, @postlines);
}

sub _create_config_files {
  my ($tlpdb, $headfile, $dest,$localconf, $keepfirstline, $cc, $tlpdblinesref, @postlines) = @_;
  my $root = $tlpdb->root;
  open(INFILE,"<$root/$headfile") or die("Cannot open $root/$headfile");
  my @lines = <INFILE>;
  push @lines, @$tlpdblinesref;
  close (INFILE);
  if (-r "$localconf") {
    #
    # this should be done more intelligently, but for now only add those
    # lines without any duplication check ...
    open FOO, "<$localconf"
      or die "strange, -r ok but cannot open $localconf: $!";
    my @tmp = <FOO>;
    push @lines, @tmp;
  }
  if (@postlines) {
    push @lines, @postlines;
  }
  if ($#lines >= 0) {
    open(OUTFILE,">$dest")
      or die("Cannot open $dest for writing: $!");

    if (!$keepfirstline) {
      print OUTFILE $cc;
      printf OUTFILE " Generated by %s on %s\n", "$0", scalar localtime;
    }
    print OUTFILE @lines;
    close(OUTFILE) || warn "close(>$dest) failed: $!";
  }
}



=back

=head2 Miscellaneous

Ideas from Fabrice Popineau's C<FileUtils.pm>.

=over 4

=item C<sort_uniq(@list)>

The C<sort_uniq> function sorts the given array and throws away multiple
occurrences of elements. It returns a sorted and unified array.

=cut

sub sort_uniq {
  my (@l) = @_;
  my ($e, $f, @r);
  $f = "";
  @l = sort(@l);
  foreach $e (@l) {
    if ($e ne $f) {
      $f = $e;
      push @r, $e;
    }
  }
  return @r;
}


=item C<push_uniq(\@list, @items)>

The C<push_uniq> function pushes the last elements on the list referenced
by the first argument.

=cut

sub push_uniq {
  # can't we use $l as a reference, and then use my?  later ...
  local (*l, @le) = @_;
  foreach my $e (@le) {
    if (! &member($e, @l)) {
      push @l, $e;
    }
  }
}


=item C<member($item, @list)>

The C<member> function returns true if the the first argument is contained
in the list of the remaining arguments.

=cut

sub member {
  my ($e, @l) = @_;
  my ($f);
  foreach $f (@l) {
    if ($e eq $f) {
      return 1;
    }
  }
  return 0;
}


=item C<merge_into(\%to, \%from)>

Merges the keys of %from into %to.

=cut

sub merge_into {
  my ($to, $from) = @_;
  foreach my $k (keys %$from) {
    if (defined($to->{$k})) {
      push @{$to->{$k}}, @{$from->{$k}};
    } else {
      $to->{$k} = [ @{$from->{$k}} ];
    }
  }
}


=item C<texdir_check($texdir)>

Test whether installation with TEXDIR set to $texdir would succeed due to
writing permissions.

=cut

sub texdir_check {
  my ($texdir) = shift;                       # PATH/texlive/2008
  my $texdirparent = dirname($texdir);        # PATH/texlive
  my $texdirpparent = dirname($texdirparent); # PATH
  if ( (dir_writable($texdirpparent)) ||
       ( (-d $texdirparent) && (dir_writable($texdirparent)) ) ||
       ( (-d $texdir) && (dir_writable($texdir)) ) ) {
    return 1;
  }
  return 0;
}


# no newlines or spaces are added, multiple args are just concatenated.
# 
sub logit {
  my ($out, $level, @rest) = @_;
  _logit($out, $level, @rest) unless $::opt_quiet;
  _logit('file', $level, @rest);
}

sub _logit {
  my ($out, $level, @rest) = @_;
  if ($::opt_verbosity >= $level) {
    # if $out is a ref/glob to STDOUT or STDERR, print it there
    if (ref($out) eq "GLOB") {
      print $out @rest;
    } else {
      # we should log it into the logfile, but that might be not initialized
      # so either print it to the filehandle $::LOGFILE, or push it onto
      # the to be printed log lines @::LOGLINES
      if (defined($::LOGFILE)) {
        print $::LOGFILE @rest;
      } else {
        push @::LOGLINES, join ("", @rest);
      }
    }
  }
}


=item C<info ($str1, $str2, ...)>

Write a normal informational message, the concatenation of the argument
strings.  The message will be written unless C<-q> was specified.  If
the global C<$::machinereadable> is set (the C<--machine-readable>
option to C<tlmgr>), then output is written to stderr, else to stdout.
If the log file (see L<process_logging_options>) is defined, it also
writes there.

It is best to use this sparingly, mainly to give feedback during lengthy
operations and for final results.

=cut

sub info {
  my $str = join("", @_);
  my $fh = ($::machinereadable ? \*STDERR : \*STDOUT);
  logit($fh, 0, $str);
  for my $i (@::info_hook) {
    &{$i}($str);
  }
}


=item C<debug ($str1, $str2, ...)>

Write a debugging message, the concatenation of the argument strings.
The message will be omitted unless C<-v> was specified.  If the log
file (see L<process_logging_options>) is defined, it also writes there.

This first level debugging message reports on the overall flow of
work, but does not include repeated messages about processing of each
package.

=cut

sub debug {
  my $str = "D:" . join("", @_);
  return if ($::opt_verbosity < 1);
  logit(\*STDOUT, 1, $str);
  for my $i (@::debug_hook) {
    &{$i}($str);
  }
}


=item C<ddebug ($str1, $str2, ...)>

Write a deep debugging message, the concatenation of the argument
strings.  The message will be omitted unless C<-v -v> (or higher) was
specified.  If the log file (see L<process_logging_options>) is defined,
it also writes there.

This second level debugging message reports messages about processing
each package, in addition to the first level.

=cut

sub ddebug {
  my $str = "DD:" . join("", @_);
  return if ($::opt_verbosity < 2);
  logit(\*STDOUT, 2, $str);
  for my $i (@::ddebug_hook) {
    &{$i}($str);
  }
}

=item C<dddebug ($str1, $str2, ...)>

Write the deepest debugging message, the concatenation of the argument
strings.  The message will be omitted unless C<-v -v -v> was specified.
If the log file (see L<process_logging_options>) is defined, it also
writes there.

This third level debugging message reports messages about processing
each line of any tlpdb files read, in addition to the first and second
levels.

=cut

sub dddebug {
  my $str = "DDD:" . join("", @_);
  return if ($::opt_verbosity < 3);
  logit(\*STDOUT, 3, $str);
  for my $i (@::dddebug_hook) {
    &{$i}($str);
  }
}


=item C<log ($str1, $str2, ...)>

Write a message to the log file (and nowhere else), the concatenation of
the argument strings.

=cut

sub log {
  my $savequiet = $::opt_quiet;
  $::opt_quiet = 0;
  _logit('file', -100, @_);
  $::opt_quiet = $savequiet;
}


=item C<tlwarn ($str1, $str2, ...)>

Write a warning message, the concatenation of the argument strings.
This always and unconditionally writes the message to standard error; if
the log file (see L<process_logging_options>) is defined, it also writes
there.

=cut

sub tlwarn {
  my $savequiet = $::opt_quiet;
  my $str = join("", @_);
  $::opt_quiet = 0;
  logit (\*STDERR, -100, $str);
  $::opt_quiet = $savequiet;
  for my $i (@::warn_hook) {
    &{$i}($str);
  }
}


=item C<debug_hash ($label, hash))>

Write LABEL followed by HASH elements, all on one line, to stderr.
If HASH is a reference, it is followed.

=cut

sub debug_hash
{
  my ($label) = shift;
  my (%hash) = (ref $_[0] && $_[0] =~ /.*HASH.*/) ? %{$_[0]} : @_;

  my $str = "$label: {";
  my @items = ();
  for my $key (sort keys %hash) {
    my $val = $hash{$key};
    $key =~ s/\n/\\n/g;
    $val =~ s/\n/\\n/g;
    push (@items, "$key:$val");
  }
  $str .= join (",", @items);
  $str .= "}";

  warn "$str\n";
}


=item C<process_logging_options ($texdir)>

This function handles the common logging options for TeX Live scripts.
It should be called before C<GetOptions> for any program-specific option
handling.  For our conventional calling sequence, see (for example) the
L<tlpfiles> script.

These are the options handled here:

=over 4

=item B<-q>

Omit normal informational messages.

=item B<-v>

Include debugging messages.  With one C<-v>, reports overall flow; with
C<-v -v> (or C<-vv>), also reports per-package processing; with C<-v -v
-v> (or C<-vvv>), also reports each line read from any tlpdb files.
Further repeats of C<-v>, as in C<-v -v -v -v>, are accepted but
ignored.  C<-vvvv> is an error.

The idea behind these levels is to be able to specify C<-v> to get an
overall idea of what is going on, but avoid terribly voluminous output
when processing many packages, as we often are.  When debugging a
specific problem with a specific package, C<-vv> can help.  When
debugging problems with parsing tlpdb files, C<-vvv> gives that too.

=item B<-logfile> I<file>

Write all messages (informational, debugging, warnings) to I<file>, in
addition to standard output or standard error.  In TeX Live, only the
installer sets a log file by default; none of the other standard TeX
Live scripts use this feature, but you can specify it explicitly.

=back

See also the L<info>, L<debug>, L<ddebug>, and L<tlwarn> functions,
which actually write the messages.

=cut

sub process_logging_options {
  $::opt_verbosity = 0;
  $::opt_quiet = 0;
  my $opt_logfile;
  my $opt_Verbosity = 0;
  my $opt_VERBOSITY = 0;
  # check all the command line options for occurrences of -q and -v;
  # do not report errors.
  my $oldconfig = Getopt::Long::Configure(qw(pass_through permute));
  GetOptions("logfile=s" => \$opt_logfile,
             "v+"  => \$::opt_verbosity,
             "vv"  => \$opt_Verbosity,
             "vvv" => \$opt_VERBOSITY,
             "q"   => \$::opt_quiet);
  Getopt::Long::Configure($oldconfig);
  
  # verbosity level, forcing -v -v instead of -vv is too annoying.
  $::opt_verbosity = 2 if $opt_Verbosity;
  $::opt_verbosity = 3 if $opt_VERBOSITY;
  
  # open log file if one was requested.
  if ($opt_logfile) {
    open(TLUTILS_LOGFILE, ">$opt_logfile") || die "open(>$opt_logfile) failed: $!\n";
    $::LOGFILE = \*TLUTILS_LOGFILE;
    $::LOGFILENAME = $opt_logfile;
  }
}


=item C<welcome>

Return the welcome message.

=cut

sub welcome {
  my $welcome=<<"EOF";

 See ./index.html for links to documentation.  The TeX Live web site
 (http://tug.org/texlive/) contains any updates and corrections.

 TeX Live is a joint project of the TeX user groups around the world;
 please consider supporting it by joining the group best for you. The
 list of groups is available on the web at http://tug.org/usergroups.html.

 Welcome to TeX Live!

EOF
  return $welcome;
}


=item C<welcome>

The same welcome message as above but with hints about C<PATH>, C<MANPATH>,
and C<INFOPATH>.

=cut

sub welcome_paths {
  my $welcome=<<"EOF";

 See 
   $::vars{'TEXDIR'}/index.html 
 for links to documentation.  The TeX Live web site (http://tug.org/texlive/) 
 contains any updates and corrections.

 TeX Live is a joint project of the TeX user groups around the world;
 please consider supporting it by joining the group best for you. The
 list of groups is available on the web at http://tug.org/usergroups.html.

 Add $::vars{'TEXDIR'}/texmf/doc/man to MANPATH.
 Add $::vars{'TEXDIR'}/texmf/doc/info to INFOPATH.
EOF
  if ($::vars{'from_dvd'} and !win32()) {
    $welcome .= <<"EOF";
 Set TEXMFCNF to $::vars{'TEXMFSYSVAR'}/web2c.
EOF
}
  $welcome .= <<"EOF";
 Most importantly, add $::vars{'TEXDIR'}/bin/$::vars{'this_platform'}
 to your PATH for current and future sessions.

 Welcome to TeX Live!

EOF
  return $welcome;
}

=pod

This function returns a "windowsified" version of its single argument
I<path>, i.e., replaces all forward slashes with backslashes, and adds
an additional C<"> at the beginning and end if I<path> contains any
spaces.  It also makes the path absolute. So if $path does not start
with one (arbitrary) characer followed by C<:>, we add the output of
C<`cd`>.

The result is suitable for running in shell commands, but not file tests
or other manipulations, since in such internal Perl contexts, the quotes
would be considered part of the filename.

=cut

sub conv_to_w32_path {
  my $p = shift;
  $p =~ s!/!\\!g;
  # we need absolute paths, too
  if ($p !~ m!^.:!) {
    my $cwd = `cd`;
    die "sorry, could not find current working directory via cd?!" if ! $cwd;
    chomp($cwd);
    $p = "$cwd\\$p";
  }
  if ($p =~ m/ /) { $p = "\"$p\""; }
  return($p);
}


=item C<give_ctan_mirror()>

Return the specific mirror chosen from the generic CTAN auto-redirecting
default (specified in L<$TLConfig::TexLiveServerURL>) if possible, else
the default url again.

Neither C<TL_DOWNLOAD_PROGRAM> nor <TL_DOWNLOAD_ARGS> is honored (see
L<download_file>), since certain options have to be set to do the job
and the program has to be C<wget> since we parse the output.

=cut

sub give_ctan_mirror
{
  my $wget = $::progs{'wget'};
  if (!defined ($wget)) {
    tlwarn ("give_ctan_mirror: Programs not set up, trying wget\n");
    $wget = "wget";
  }
  
  # we need the verbose output, so no -q.
  # do not reduce retries here, but timeout still seems desirable.
  my $cmd = "$wget $TeXLiveServerURL --timeout=60 -O "
            . (win32() ? "nul" : "/dev/null") . " 2>&1";
  my @out = `$cmd`;
  # analyze the output for the mirror actually selected.
  my $mirror = $TeXLiveURL;
  foreach (@out) {
    if (m/^Location: (\S*)\s*.*$/) {
      (my $mhost = $1) =~ s,/*$,,;  # remove trailing slashes since we add it
      $mirror = "$mhost/$TeXLiveServerPath";
      last;
    }
  }
  # if we cannot find a mirror, return the default again.
  return $mirror;
}

sub tlmd5 {
  my ($file) = @_;
  if (-r $file) {
    open(FILE, $file) || die "open($file) failed: $!";
    binmode(FILE);
    return Digest::MD5->new->addfile(*FILE)->hexdigest;
    close(FILE);
  } else {
    tlwarn("tlmd5, given file not readable: $file\n");
    return "";
  }
}

#############################################
#
# Taken from Text::ParseWords
#
sub quotewords {
  my($delim, $keep, @lines) = @_;
  my($line, @words, @allwords);

  foreach $line (@lines) {
    @words = parse_line($delim, $keep, $line);
    return() unless (@words || !length($line));
    push(@allwords, @words);
  }
  return(@allwords);
}

sub parse_line {
  my($delimiter, $keep, $line) = @_;
  my($word, @pieces);

  no warnings 'uninitialized';	# we will be testing undef strings

  while (length($line)) {
    $line =~ s/^(["'])			# a $quote
              ((?:\\.|(?!\1)[^\\])*)	# and $quoted text
              \1				# followed by the same quote
                |				# --OR--
            ^((?:\\.|[^\\"'])*?)		# an $unquoted text
            (\Z(?!\n)|(?-x:$delimiter)|(?!^)(?=["']))
                  # plus EOL, delimiter, or quote
      //xs or return;		# extended layout
    my($quote, $quoted, $unquoted, $delim) = ($1, $2, $3, $4);
    return() unless( defined($quote) || length($unquoted) || length($delim));

    if ($keep) {
      $quoted = "$quote$quoted$quote";
    } else {
      $unquoted =~ s/\\(.)/$1/sg;
      if (defined $quote) {
        $quoted =~ s/\\(.)/$1/sg if ($quote eq '"');
        $quoted =~ s/\\([\\'])/$1/g if ( $PERL_SINGLE_QUOTE && $quote eq "'");
      }
    }
    $word .= substr($line, 0, 0);	# leave results tainted
    $word .= defined $quote ? $quoted : $unquoted;

    if (length($delim)) {
      push(@pieces, $word);
      push(@pieces, $delim) if ($keep eq 'delimiters');
      undef $word;
    }
    if (!length($line)) {
      push(@pieces, $word);
    }
  }
  return(@pieces);
}



1;
__END__
=back

=head1 SEE ALSO

The modules L<TeXLive::TLPSRC>, L<TeXLive::TLPOBJ>,
L<TeXLive::TLPDB>, L<TeXLive::TLTREE>, and the
document L<Perl-API.txt> and the specification in the TeX Live
repository trunk/Master/tlpkg/doc/.

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
