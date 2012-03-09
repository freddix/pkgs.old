%define		sover	4.5
#
Summary:	RPM Package Manager
Name:		rpm
Version:	4.5
Release:	21
License:	LGPL
Group:		Base
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6b4cda21de59dc250d2e33e4187fd166
Source1:	%{name}.groups
Source2:	%{name}.platform
Source3:	%{name}-install-tree
Source4:	%{name}-find-spec-bcond
Source5:	%{name}-hrmib-cache
Source6:	%{name}-groups-po.awk
Source7:	%{name}-compress-doc
Source8:	%{name}-gstreamer-deps.sh
Source9:	%{name}-find-debuginfo.sh
Source10:	%{name}-php-provides
Source11:	%{name}-php-requires
Source12:	%{name}.sysinfo
Source13:	%{name}-perl-provides
Source14:	%{name}-user_group.sh
Source15:	%{name}.sysconfig
Source16:	%{name}-macros.java
Source17:	%{name}-java-requires
# http://svn.pld-linux.org/banner.sh/
Source18:	banner.sh
Source19:	%{name}-macros.gstreamer
#
# configure / build
Patch1:		%{name}-po.patch
Patch2:		%{name}-freddix.patch
Patch3:		%{name}-system_libs.patch
Patch4:		%{name}-system_libs-more.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-makefile-no_myLDADD_deps.patch
Patch7:		%{name}-missing-prototypes.patch
Patch8:		%{name}-no-neon.patch
Patch9:		%{name}-no-sqlite.patch
Patch10:	%{name}-nopie.patch
Patch11:	%{name}-cleanlibdirs.patch
Patch12:	%{name}-as_needed-fix.patch
Patch13:	%{name}-configure-add-cxx.patch
Patch14:	%{name}-db3-configure.patch
Patch15:	%{name}-db-configure.patch
Patch16:	%{name}-gstreamer.patch
Patch17:	%{name}-pkgconfig.patch
#
# build process
Patch20:	%{name}-macros.patch
Patch21:	%{name}-rpmrc.patch
Patch22:	%{name}-arch.patch
Patch23:	%{name}-rpmpopt.patch
Patch24:	%{name}-libtool-deps.patch
Patch25:	%{name}-macros-freddix.patch
Patch26:	%{name}-pkgconfigdeps.patch
Patch27:	%{name}-compress-doc.patch
Patch28:	%{name}-ldconfig-always.patch
Patch29:	%{name}-provides-dont-obsolete.patch
Patch30:	%{name}-arch-x86_64.patch
Patch31:	%{name}-debuginfo.patch
Patch32:	%{name}-old-fileconflicts-behaviour.patch
Patch33:	%{name}-popt-coreutils.patch
Patch34:	%{name}-popt-aliases.patch
Patch35:	%{name}-cleanbody.patch
Patch36:	%{name}-installbeforeerase.patch
# p0
Patch37:	%{name}-dirdeps-macro.patch
Patch38:	%{name}-nosmpflags.patch
Patch39:	%{name}-disable-hkp.patch
#
# perl / python / mono / etc
Patch50:	%{name}-perl-makefile.patch
Patch51:	%{name}-perl-macros.patch
Patch52:	%{name}-perl_req-use_base.patch
Patch53:	%{name}-perl_req-skip_multiline.patch
Patch54:	%{name}-perl_req-heredocs_pod.patch
Patch55:	%{name}-mono.patch
Patch56:	%{name}-pythondeps-speedup.patch
#
# fixes
Patch60:	%{name}-gettext-in-header.patch
Patch61:	%{name}-noexpand.patch
Patch62:	%{name}-scripts-closefds.patch
Patch63:	%{name}-unglobal.patch
Patch64:	%{name}-notsc.patch
Patch65:	%{name}-hack-norpmlibdep.patch
Patch66:	%{name}-chroot-hack.patch
Patch67:	%{name}-postun-nofail.patch
Patch68:	%{name}-namespace-probe.patch
Patch69:	%{name}-noversiondir.patch
# p0
Patch70:	%{name}-rpmte-segv.patch
Patch71:	%{name}-hirmib-ts.patch
Patch72:	%{name}-poptexecpath.patch
Patch73:	%{name}-gendiff.patch
Patch74:	%{name}-set-failed-on-reopen.patch
Patch75:	%{name}-shescape-memfault.patch
Patch76:	%{name}-gid-uucp.patch
#
Patch77:	%{name}-am.patch
#
# lzma / xz
Patch80:	%{name}-lzma-mem.patch
Patch81:	%{name}-lzma-size_t.patch
Patch82:	%{name}-lzma-tukaani.patch
Patch83:	%{name}-repackage-wo-lzma.patch
Patch84:	%{name}-lzma-compress-level.patch
#
# backports
# -R
Patch90:	%{name}-rpm5-patchset-8074.patch
Patch91:	%{name}-rpm5-patchset-8637.patch
Patch92:	%{name}-rpm5-patchset-8413.patch
# p0
Patch93:	%{name}-rpm5-patchset-10061.patch
Patch94:	%{name}-debugedit-backport.patch
#
# extra features
Patch100:	%{name}-pld-autodep.patch
Patch101:	%{name}-epoch0.patch
#
URL:		http://rpm5.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	beecrypt-devel
BuildRequires:	bzip2-devel
BuildRequires:	db-devel
BuildRequires:	elfutils-devel
BuildRequires:	gettext-devel
BuildRequires:	libmagic-devel
# needed only for AM_PROG_CXX used for CXX substitution in rpm.macros
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	neon-devel
BuildRequires:	ossp-uuid-devel
BuildRequires:	patch
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	tar
BuildRequires:	zlib-devel
%if 0
BuildRequires:	doxygen
BuildRequires:	ghostscript
BuildRequires:	graphviz
BuildRequires:	tetex-pdftex
%endif
#
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-lib = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_binary_payload		w9.gzdio
%define		_noPayloadPrefix	1

# don't require very fresh rpm.macros to build
%define		__gettextize gettextize --copy --force --no-changelog; [ -f po/Makevars ] || cp -f po/Makevars{.template,}
%define		find_lang sh ./scripts/find-lang.sh $RPM_BUILD_ROOT
%define		ix86	i386 i486 i586 i686 athlon pentium3 pentium4
%define		ppc	ppc ppc7400 ppc7450
%define		x8664	amd64 ia32e x86_64

# stabilize new build environment
%define		__newcc %{?force_cc}%{!?force_cc:%{_target_cpu}-freddix-linux-gcc}
%define		__newcxx %{?force_cxx}%{!?force_cxx:%{_target_cpu}-freddix-linux-g++}
%define		__newcpp %{?force_cpp}%{!?force_cpp:%{_target_cpu}-freddix-linux-gcc -E}

%define		_rpmlibdir /usr/lib/rpm

%description
RPM is a powerful package manager, which can be used to build,
install, query, verify, update, and uninstall individual software
packages. A package consists of an archive of files, and package
information, including name, version, and description.

%package base
Summary:	RPM base package - scripts used by rpm packages themselves
Group:		Base
Requires:	filesystem

%description base
The RPM base package contains scripts used by rpm packages themselves.
These include:
- scripts for adding/removing groups and users needed for rpm
  packages,
- banner.sh to display %%banner messages from rpm scriptlets.

%package lib
Summary:	RPMs library
Group:		Libraries
Requires:	beecrypt >= %{beecrypt_ver}
Suggests:	xz
Obsoletes:	rpm-libs

%description lib
RPMs library.

%package devel
Summary:	Header files for rpm libraries
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description devel
The RPM packaging system includes C libraries that make it easy to
manipulate RPM packages and databases. They are intended to ease the
creation of graphical package managers and other tools that need
intimate knowledge of RPM packages. This package contains header files
for these libraries.

%package utils
Summary:	Additional utilities for managing RPM packages and database
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description utils
Additional utilities for managing RPM packages and database.

%package utils-perl
Summary:	Additional utilities for managing RPM packages and database
Group:		Applications/File
Requires:	%{name}-utils = %{version}-%{release}

%description utils-perl
Additional utilities for managing RPM packages and database.

%package utils-static
Summary:	Static rpm utilities
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description utils-static
Static rpm utilities for repairing system in case something with
shared libraries used by rpm become broken. Currently it contains rpmi
binary, which can be used to install/upgrade/remove packages without
using shared libraries (well, in fact with exception of NSS modules).

%package build
Summary:	Scripts for building binary RPM packages
Group:		Applications/File
Requires(pretrans):	findutils
Requires:	%{name}-build-macros
Requires:	%{name}-utils = %{version}-%{release}
Requires:	/bin/id
Requires:	awk
Requires:	bzip2
Requires:	chrpath
Requires:	cpio
Requires:	diffutils
Requires:	elfutils
Requires:	file
Requires:	fileutils
Requires:	findutils
Requires:	gcc
Requires:	glibc-devel
Requires:	grep
Requires:	gzip
Requires:	make
Requires:	patch
Requires:	sed
Requires:	sh-utils
Requires:	tar
Requires:	textutils
Requires:	xz
Provides:	rpmbuild(monoautodeps)
Provides:	rpmbuild(noauto) = 3

%description build
Scripts for building binary RPM packages.

%package gstreamerprov
Summary:	Additional utilities for checking Gstreamer provides in RPM packages
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer

%description gstreamerprov
Additional utilities for checking Gstreamer provides in RPM packages.

%package javaprov
Summary:	Additional utilities for checking Java provides/requires in RPM packages
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	file
Requires:	findutils
Requires:	mktemp
Requires:	unzip

%description javaprov
Additional utilities for checking Java provides/requires in RPM
packages.

%package perlprov
Summary:	Additional utilities for checking Perl provides/requires in RPM packages
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	perl-devel
Requires:	perl-modules

%description perlprov
Additional utilities for checking Perl provides/requires in RPM
packages.

%package pythonprov
Summary:	Python macros, which simplifies creation of RPM packages with Python software
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	python
Requires:	python-modules

%description pythonprov
Python macros, which simplifies creation of RPM packages with Python
software.

%package php-pearprov
Summary:	Additional utilities for checking PHP PEAR provides/requires in RPM packages
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	sed >= 4.0

%description php-pearprov
Additional utilities for checking PHP PEAR provides/requires in RPM
packages.

%package -n python-rpm
Summary:	Python interface to RPM library
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python

%description -n python-rpm
The rpm-python package contains a module which permits applications
written in the Python programming language to use the interface
supplied by RPM (RPM Package Manager) libraries.

This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.

%package apidocs
Summary:	RPM API documentation and guides
Group:		Documentation

%description apidocs
Documentation for RPM API and guides in HTML format generated from rpm
sources by doxygen.

%prep
%setup -q
# configure / build patches
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
# build time patches
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p0
%patch38 -p1
%patch39 -p1
# perl, python, php, mono, etc. patches
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
# fixes
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p0
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
# lzma / xz
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
# backports
%patch90 -p1 -R
%patch91 -p1
%patch92 -p1
%patch93 -p0
%patch94 -p1

# extra features
%patch100 -p1
%patch101 -p1

sed -e 's/^/@freddix@/' %{SOURCE2} >>platform.in
echo '%%define	__perl_provides	%%{__perl} /usr/lib/rpm/perl.prov' > macros.perl
echo '%%define	__perl_requires	%%{__perl} /usr/lib/rpm/perl.req' >> macros.perl
echo '# obsoleted file' > macros.python
echo '%%define	__php_provides	/usr/lib/rpm/php.prov' > macros.php
echo '%%define	__php_requires	/usr/lib/rpm/php.req' >> macros.php
echo '%%define	__mono_provides	/usr/lib/rpm/mono-find-provides' > macros.mono
echo '%%define	__mono_requires	/usr/lib/rpm/mono-find-requires' >> macros.mono
install %{SOURCE10} scripts/php.prov
install %{SOURCE11} scripts/php.req
install %{SOURCE13} scripts/perl.prov

mv -f po/{sr,sr@Latn}.po
rm -rf sqlite zlib popt
rm -rf db3 db rpmdb/db.h

# generate Group translations to *.po
awk -f %{SOURCE6} %{SOURCE1}

# update macros paths
for f in doc{,/ja,/pl}/rpm.8 doc{,/ja,/pl}/rpmbuild.8 ; do
	sed -e 's@lib/rpm/redhat@lib/rpm/freddix@g' $f > ${f}.tmp
	mv -f ${f}.tmp $f
done

%build
rm -rf file
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

# rpm checks for CPU type at runtime, but it looks better
sed -i \
	-e 's|@host@|%{_target_cpu}-%{_target_vendor}-%{_target_os}|' \
	-e 's|@host_cpu@|%{_target_cpu}|' \
	-e 's|@host_os@|%{_target_os}|' \
	macros.in

# pass CC and CXX too in case of building with some older configure macro
# disable perl-RPM2 build, we have it in separate spec
CPPFLAGS="%{rpmcppflags} -I/usr/include/oosp-uuid"
%configure \
	CC="%{__newcc}" \
	CXX="%{__newcxx}" \
	CPP="%{__newcpp}" \
	WITH_PERL_VERSION=no \
	--enable-adding-packages-names-in-autogenerated-dependancies \
	--enable-shared \
	--enable-static \
	--without-apidocs \
	--with-python=%{py_ver} \
	--without-selinux \
	--without-db

%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CPP="%{__cpp}" \
	libdb_la=%{_libdir}/libdb.la \
	pylibdir=%{py_libdir} \
	myLDFLAGS="%{rpmldflags}" \
	staticLDFLAGS=%{?with_static:-all-static}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},/etc/{sysconfig,tmpwatch},%{_sysconfdir}/rpm,/var/lib/banner,/var/cache/hrmib}

install -d $RPM_BUILD_ROOT/etc/pki/rpm-gpg

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	staticLDFLAGS=%{?with_static:-all-static} \
	pylibdir=%{py_libdir}

cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/platform
# first platform file entry can't contain regexps
%{_target_cpu}-%{_target_vendor}-linux
x86_64-%{_target_vendor}-linux

x86_64-[^-]*-[Ll]inux(-gnu)?
i686-[^-]*-[Ll]inux(-gnu)?
i586-[^-]*-[Ll]inux(-gnu)?
i486-[^-]*-[Ll]inux(-gnu)?
i386-[^-]*-[Ll]inux(-gnu)?
noarch-[^-]*-.*
EOF

rm $RPM_BUILD_ROOT%{_rpmlibdir}/vpkg-provides*
rm $RPM_BUILD_ROOT%{_rpmlibdir}/find-{prov,req}.pl
rm $RPM_BUILD_ROOT%{_rpmlibdir}/find-{provides,requires}.perl
rm $RPM_BUILD_ROOT%{_rpmlibdir}/find-lang.sh

# not installed since 4.4.8 (-tools-perl subpackage)
install scripts/rpmdiff scripts/rpmdiff.cgi $RPM_BUILD_ROOT%{_rpmlibdir}

install macros.perl	$RPM_BUILD_ROOT%{_rpmlibdir}/macros.perl
install macros.python	$RPM_BUILD_ROOT%{_rpmlibdir}/macros.python
install macros.php	$RPM_BUILD_ROOT%{_rpmlibdir}/macros.php
install macros.mono	$RPM_BUILD_ROOT%{_rpmlibdir}/macros.mono
install %{SOURCE16}	$RPM_BUILD_ROOT%{_rpmlibdir}/macros.java
install %{SOURCE19}	$RPM_BUILD_ROOT%{_rpmlibdir}/macros.gstreamer

install %{SOURCE1} doc/manual/groups
install %{SOURCE3} $RPM_BUILD_ROOT%{_rpmlibdir}/install-build-tree
install %{SOURCE4} $RPM_BUILD_ROOT%{_rpmlibdir}/find-spec-bcond
install %{SOURCE7} $RPM_BUILD_ROOT%{_rpmlibdir}/compress-doc
install %{SOURCE8} $RPM_BUILD_ROOT%{_rpmlibdir}/gstreamerdeps.sh
install %{SOURCE9} $RPM_BUILD_ROOT%{_rpmlibdir}/find-debuginfo.sh

install %{SOURCE14} $RPM_BUILD_ROOT%{_rpmlibdir}/user_group.sh
install %{SOURCE17} $RPM_BUILD_ROOT%{_rpmlibdir}/java-find-requires
install scripts/php.{prov,req}	$RPM_BUILD_ROOT%{_rpmlibdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_rpmlibdir}/hrmib-cache
install %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/rpm

install %{SOURCE18} $RPM_BUILD_ROOT%{_bindir}/banner.sh

install -d $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo
touch $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo/Conflictname
touch $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo/Dirnames
install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo/Filelinktos
touch $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo/Obsoletename
touch $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo/Providename
touch $RPM_BUILD_ROOT%{_sysconfdir}/rpm/sysinfo/Requirename

cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros <<EOF
# customized rpm macros - global for host
#
%%distribution Freddix
#
# remove or replace with file_contexts path if you want to use custom
# SELinux file contexts policy instead of one stored in packages payload
%%_install_file_context_path	%%{nil}
%%_verify_file_context_path	%%{nil}

# If non-zero, all erasures will be automagically repackaged.
%_repackage_all_erasures	0

# If non-zero, create debuginfo packages
#%%_enable_debug_packages	0

# Boolean (i.e. 1 == "yes", 0 == "no") that controls whether files
# marked as %doc should be installed.
#%%_excludedocs   1

# For static /dev not to update perms if upgraded and tmpfs mounted
#%%_netsharedpath /dev/shm
EOF

cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.lang <<EOF
# Customized rpm macros - global for host
#	A colon separated list of desired locales to be installed;
#	"all" means install all locale specific files.
#
%%_install_langs pl_PL:de_DE:en_US
EOF

cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/noautoprovfiles <<EOF
# global list of files (regexps) which don't generate Provides
EOF
cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/noautoprov <<EOF
# global list of script capabilities (regexps) not to be used in Provides
EOF
cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/noautoreqfiles <<EOF
# global list of files (regexps) which don't generate Requires
^%{_examplesdir}/
^%{_docdir}/
EOF
cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/noautoreq <<EOF
# global list of script capabilities (regexps) not to be used in Requires
EOF
cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/noautoreqdep <<EOF
# global list of capabilities (SONAME, perl(module), php(module) regexps)
# which don't generate dependencies on package NAMES
# -- OpenGL implementation
^libGL.so.1
^libGLU.so.1
^libOSMesa.so
EOF
cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/noautocompressdoc <<EOF
# global list of file masks not to be compressed in DOCDIR
EOF

# for rpm -e|-U --repackage
install -d $RPM_BUILD_ROOT/var/{spool/repackage,lock/rpm}
touch $RPM_BUILD_ROOT/var/lock/rpm/transaction

# move rpm to /bin
install -d $RPM_BUILD_ROOT/bin
mv $RPM_BUILD_ROOT%{_bindir}/rpm $RPM_BUILD_ROOT/bin
# move essential libs to /lib (libs that /bin/rpm links to)
for a in librpm-%{sover}.so librpmdb-%{sover}.so librpmio-%{sover}.so ; do
	mv -f $RPM_BUILD_ROOT%{_libdir}/$a $RPM_BUILD_ROOT/%{_lib}
	ln -s /%{_lib}/$a $RPM_BUILD_ROOT%{_libdir}/$a
done

# remove arch dependant macros which have no use on noarch
%{__sed} -i -e '
/{__spec_install_post_strip}/d
/{__spec_install_post_chrpath}/d
/{__spec_install_post_compress_modules}/d
' $RPM_BUILD_ROOT%{_rpmlibdir}/noarch-linux/macros

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/rpm/*.{la,a,py}

# (currently) not used or supported
%{__rm} $RPM_BUILD_ROOT%{_rpmlibdir}/{http.req,perldeps.pl}
# wrong location, not used anyway
%{__rm} $RPM_BUILD_ROOT%{_rpmlibdir}/rpm.{daily,log,xinetd}

# unpackaged in 4.4.9, reasons unknown
%{__rm} $RPM_BUILD_ROOT%{_rpmlibdir}/symclash.{sh,py}
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/RPM.pm
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/RPM/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/RPM/RPM.bs
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/RPM/RPM.so
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/RPM.3pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{,ja,pl}/man8/rpm{cache,graph}.8

%find_lang %{name}

rm -rf manual
cp -a doc/manual manual
rm -f manual/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun lib -- %{name}-lib < %{version}
echo >&2 "rpm-lib upgrade: Removing /var/lib/rpm/__db* from older rpmdb version"
rm -f /var/lib/rpm/__db*
if [ -d /vservers ]; then
	echo >&2 "rpm-lib upgrade: Removing vservers apps/pkgmgmt/base/rpm/state/__* from older rpmdb version"
	rm -f /etc/vservers/*/apps/pkgmgmt/base/rpm/state/__*
fi
echo >&2 "You should rebuild your rpmdb: rpm --rebuilddb to avoid random rpmdb errors"

%post	lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%pretrans build
find %{_rpmlibdir} -name '*-linux' -type l | xargs rm -f

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES CREDITS README manual/*

%attr(755,root,root) /bin/rpm

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rpm/macros
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rpm/macros.lang
%dir %{_sysconfdir}/rpm/sysinfo
# these are ok to be replaced
%config %verify(not md5 mtime size) %{_sysconfdir}/rpm/sysinfo/*
%config %verify(not md5 mtime size) %{_sysconfdir}/rpm/platform


%{_mandir}/man8/rpm.8*
%lang(fr) %{_mandir}/fr/man8/rpm.8*
%lang(ja) %{_mandir}/ja/man8/rpm.8*
%lang(ko) %{_mandir}/ko/man8/rpm.8*
%lang(pl) %{_mandir}/pl/man8/rpm.8*
%lang(ru) %{_mandir}/ru/man8/rpm.8*
%lang(sk) %{_mandir}/sk/man8/rpm.8*

%dir /var/lib/rpm
%dir %attr(700,root,root) /var/spool/repackage
%dir /var/lock/rpm
/var/lock/rpm/transaction

# exported package NVRA (stamped with install tid)
# net-snmp hrSWInstalledName queries, bash-completions
%dir /var/cache/hrmib

%{_rpmlibdir}/rpmpopt*
%{_rpmlibdir}/macros

%attr(755,root,root) %{_rpmlibdir}/hrmib-cache

%files base
%defattr(644,root,root,755)
%dir %{_sysconfdir}/rpm
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rpm
%dir %{_rpmlibdir}
%attr(755,root,root) %{_bindir}/banner.sh
%attr(755,root,root) %{_rpmlibdir}/user_group.sh
%dir /var/lib/banner

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/librpm-%{sover}.so
%attr(755,root,root) /%{_lib}/librpmdb-%{sover}.so
%attr(755,root,root) /%{_lib}/librpmio-%{sover}.so
%attr(755,root,root) %{_libdir}/librpmbuild-%{sover}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librpm.so
%attr(755,root,root) %{_libdir}/librpm-%{sover}.so
%attr(755,root,root) %{_libdir}/librpmio.so
%attr(755,root,root) %{_libdir}/librpmio-%{sover}.so
%attr(755,root,root) %{_libdir}/librpmdb.so
%attr(755,root,root) %{_libdir}/librpmdb-%{sover}.so
%attr(755,root,root) %{_libdir}/librpmbuild.so
%{_includedir}/rpm
%{_pkgconfigdir}/*.pc

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rpm2cpio
%attr(755,root,root) %{_bindir}/rpmdigest
%attr(755,root,root) %{_bindir}/rpmmtree
%attr(755,root,root) %{_bindir}/rpmrepo
%attr(755,root,root) %{_rpmlibdir}/debugedit
%attr(755,root,root) %{_rpmlibdir}/find-debuginfo.sh
%attr(755,root,root) %{_rpmlibdir}/rpmdb_loadcvt
%attr(755,root,root) %{_rpmlibdir}/rpmdeps
%attr(755,root,root) %{_rpmlibdir}/tgpg
%{_mandir}/man8/rpm2cpio.8*
%{_mandir}/man8/rpmdeps.8*
%lang(ja) %{_mandir}/ja/man8/rpm2cpio.8*
%lang(ko) %{_mandir}/ko/man8/rpm2cpio.8*
%lang(pl) %{_mandir}/pl/man8/rpm2cpio.8*
%lang(pl) %{_mandir}/pl/man8/rpmdeps.8*
%lang(ru) %{_mandir}/ru/man8/rpm2cpio.8*

%files utils-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_rpmlibdir}/rpmdiff*

%files build
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rpm/noauto*
%attr(755,root,root) %{_rpmlibdir}/brp-*
%attr(755,root,root) %{_rpmlibdir}/check-files
%attr(755,root,root) %{_rpmlibdir}/compress-doc
%attr(755,root,root) %{_rpmlibdir}/cross-build
%attr(755,root,root) %{_rpmlibdir}/executabledeps.sh
%attr(755,root,root) %{_rpmlibdir}/find-spec-bcond
%attr(755,root,root) %{_rpmlibdir}/getpo.sh
%attr(755,root,root) %{_rpmlibdir}/install-build-tree
%attr(755,root,root) %{_rpmlibdir}/libtooldeps.sh
%attr(755,root,root) %{_rpmlibdir}/mimetypedeps.sh
%attr(755,root,root) %{_rpmlibdir}/u_pkg.sh
# needs hacked pkg-config to return anything
%attr(755,root,root) %{_rpmlibdir}/pkgconfigdeps.sh
%{_rpmlibdir}/noarch-*
%ifarch %{ix86}
%{_rpmlibdir}/i?86*
%{_rpmlibdir}/pentium*
%{_rpmlibdir}/athlon*
%endif
%ifarch ia64
%{_rpmlibdir}/ia64*
%endif
%ifarch %{x8664}
%{_rpmlibdir}/amd64*
%{_rpmlibdir}/ia32e*
%{_rpmlibdir}/x86_64*
%endif

# must be here for "Requires: rpm-*prov" to work
%{_rpmlibdir}/macros.gstreamer
%{_rpmlibdir}/macros.java
%{_rpmlibdir}/macros.mono
%{_rpmlibdir}/macros.perl
%{_rpmlibdir}/macros.php

%attr(755,root,root) %{_bindir}/gendiff
%attr(755,root,root) %{_bindir}/rpmbuild

%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpmbuild.8*
%lang(ja) %{_mandir}/ja/man8/rpmbuild.8*
%lang(pl) %{_mandir}/pl/man1/gendiff.1*
%lang(pl) %{_mandir}/pl/man8/rpmbuild.8*

%files gstreamerprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_rpmlibdir}/gstreamerdeps.sh

%files javaprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_rpmlibdir}/java-find-requires
%attr(755,root,root) %{_rpmlibdir}/javadeps.sh

%files perlprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_rpmlibdir}/perl.*

%files pythonprov
%defattr(644,root,root,755)
%{_rpmlibdir}/macros.python
%attr(755,root,root) %{_rpmlibdir}/pythondeps.sh

%files php-pearprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_rpmlibdir}/php*

%files -n python-rpm
%defattr(644,root,root,755)
%dir %{py_sitedir}/rpm
%attr(755,root,root) %{py_sitedir}/rpm/*.so
%{py_sitedir}/rpm/*.py[co]

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc apidocs
%endif

