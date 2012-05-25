# $Id: TLConfig.pm 12278 2009-03-01 22:19:39Z karl $
# TeXLive::TLConfig.pm - module exporting configuration stuff
# Copyright 2007, 2008, 2009 Norbert Preining
# This file is licensed under the GNU General Public License version 2
# or any later version.

package TeXLive::TLConfig;

BEGIN {
  use Exporter ();
  use vars qw( @ISA @EXPORT_OK @EXPORT );
  @ISA = qw(Exporter);
  @EXPORT_OK = qw(
    @MetaCategories
    @NormalCategories
    @Categories
    $MetaCategoriesRegexp
    $CategoriesRegexp
    $DefaultCategory
    $DefaultContainerExtension
    $InfraLocation
    $DatabaseName
    $BlockSize
    $Archive
    $TeXLiveServerURL
    $TeXLiveServerPath
    $TeXLiveURL
    $WinSpecialUpdatePackagesRegexp
    @CriticalPackagesList
    @AllowedConfigOptions
  );
  @EXPORT = @EXPORT_OK;
}

# Meta Categories do not ship files, but call only for other packages
our @MetaCategories = qw/Collection Scheme/;
our $MetaCategoriesRegexp = '(Collection|Scheme)';
# Normal Categories contain actial files and do not depend on other things.
our @NormalCategories = qw/Package TLCore Documentation/;

# list of all Categories
our @Categories = (@MetaCategories, @NormalCategories);

our $CategoriesRegexp = '(Collection|Scheme|Package|TLCore|Documentation)';

our $DefaultCategory = "Package";

# location of various infra files (texlive.tlpdb, .tlpobj etc)
# relative to a root (e.g., the Master/, or the installation path)
our $InfraLocation = "tlpkg";
our $DatabaseName = "texlive.tlpdb";

our $BlockSize = 4096;

# the way we package things on the web
our $DefaultContainerExtension = "tar.lzma";

our $Archive = "archive";
our $TeXLiveServerURL = "http://mirror.ctan.org";
our $TeXLiveServerPath = "systems/texlive/tlnet/2008";
our $TeXLiveURL = "$TeXLiveServerURL/$TeXLiveServerPath";

our $WinSpecialUpdatePackagesRegexp = 
  '^(texlive\.infra|bin-tlperl\.win32$|bin-texlive)';


our @CriticalPackagesList = qw/texlive.infra bin-texlive/;
push(@CriticalPackagesList, "bin-tlperl.win32") if ($^O=~/^MSWin(32|64)$/i);
  

our @AllowedConfigOptions = qw/
  available_architectures
  opt_create_symlinks
  opt_create_formats
  opt_paper
  opt_sys_bin
  opt_sys_info
  opt_sys_man
  opt_install_docfiles
  opt_install_srcfiles
  platform
  location
  backupdir
  autobackup
  /;

1;


=head1 NAME

C<TeXLive::TLConfig> -- TeX Live Configurations

=head1 SYNOPSIS

  use TeXLive::TLConfig;

=head1 DESCRIPTION

The L<TeXLive::TLConfig> module contains definitions of variables 
configuring all of TeX Live.

=over 4

=head1 EXPORTED VARIABLES

All of the following variables are pulled into the callers namespace,
i.e., are declared with C<EXPORT> (and C<EXPORT_OK>).

=item C<@TeXLive::TLConfig::MetaCategories>

The list of meta categories, i.e., those categories whose packages only
depend on other packages, but don't ship any files. Currently 
C<Collection> and <Scheme>.

=item C<@TeXLive::TLConfig::NormalCategories>

The list of normal categories, i.e., those categories whose packages do
ship files. Currently C<TLCore>, C<Documentation>, C<Package>.

=item C<@TeXLive::TLConfig::Categories>

The list of all categories, i.e., the union of the above.

=item C<$TeXLive::TLConfig::CategoriesRegexp>

A regexp matching any category.

=item C<$TeXLive::TLConfig::DefaultCategory>

The default category used when creating new packages.

=item C<$TeXLive::TLConfig::InfraLocation>

The subdirectory with various infrastructure files (C<texlive.tlpdb>,
tlpobj files, ...) relative to the root of the installation; currently
C<tlpkg>.

=item C<$TeXLive::TLConfig::BlockSize>

The assumed block size, currently 4k.

=item C<$TeXLive::TLConfig::Archive>
=item C<$TeXLive::TLConfig::TeXLiveURL>

These values specify where to find packages.

=item C<$TeXLive::TLConfig::TeXLiveServerURL>
=item C<$TeXLive::TLConfig::TeXLiveServerPath>

C<TeXLiveURL> is concatencated from these values, with a string between.
The defaults are respectively, C<http://mirror.ctan.org> and
C<systems/texlive/tlnet/>I<rel>, where I<rel> specifies the TeX Live
release version, such as C<tldev> or C<2008>.

=item C<$TeXLive::TLConfig::WinSpecialUpdatePackagesRegexp>

A regexp matching all those packages which cannot be normally updated 
because they contain files which are open during the update process.

=item C<@TeXLive::TLConfig::CriticalPackagesList>

A list of all those packages which we do not update regularly
since they are too central, currently bin-texlive and texlive.infra.

=item C<@TeXLive::TLConfig::AllowedConfigOptions>

A list of a config options that can be set in 00texlive-installation.config.

=back

=head1 SEE ALSO

The modules L<TeXLive::TLUtils>, L<TeXLive::TLPSRC>,
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
