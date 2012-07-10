Summary:	GNU libtool, a shared library generation tool
Name:		libtool
Version:	2.4.2
Release:	2
Epoch:		2
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.xz
# Source0-md5:	2ec8997e0c07249eb4cbd072417d70fe
Patch0:		%{name}-relink.patch
Patch1:		%{name}-libdirs.patch
Patch2:		%{name}-linking-order.patch
URL:		http://www.gnu.org/software/libtool/
BuildRequires:	/usr/bin/which
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xz
BuildRequires:	texinfo
%requires_eq	gcc
Requires:	coreutils
Requires:	grep
Requires:	mktemp
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in generic fashion.

%package -n libltdl
Summary:	System independent dlopen wrapper for GNU libtool
Group:		Libraries
Obsoletes:	libtool-libs

%description -n libltdl
System independent dlopen wrapper for GNU libtool.

%package -n libltdl-devel
Summary:	Development components for libltdl
Group:		Development/Libraries
Requires:	libltdl = %{epoch}:%{version}-%{release}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool - development part.
Install this package if you want to develop for libltdl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I libltdl/m4
%{__autoconf}
%{__automake}

cd libltdl
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
cd ..

# Change in configure itself, so it will affect packaged %{_bindir}/libtool
# script, not local libtools generated during packages building:
# libtool packaged as /bin/sh script for general use should work with any
# POSIX sh, not just the ones having extensions (like "+=" operator) that
# shell used to build libtool package had.
%{__sed} -i 's/lt_shell_append=yes/lt_shell_append=no/' configure

%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post   -n libltdl -p /sbin/ldconfig
%postun -n libltdl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO ChangeLog
%attr(755,root,root) %{_bindir}/libtool
%attr(755,root,root) %{_bindir}/libtoolize
%dir %{_datadir}/libtool
%dir %{_datadir}/libtool/config
%attr(755,root,root) %{_datadir}/libtool/config/compile
%attr(755,root,root) %{_datadir}/libtool/config/config.guess
%attr(755,root,root) %{_datadir}/libtool/config/config.sub
%attr(755,root,root) %{_datadir}/libtool/config/depcomp
%attr(755,root,root) %{_datadir}/libtool/config/install-sh
%attr(755,root,root) %{_datadir}/libtool/config/ltmain.sh
%attr(755,root,root) %{_datadir}/libtool/config/missing
# libltdl copy for libtoolize --ltdl
%dir %{_datadir}/libtool/libltdl
%{_datadir}/libtool/libltdl/[!c]*
%{_datadir}/libtool/libltdl/config-h.in
%attr(755,root,root) %{_datadir}/libtool/libltdl/configure
%{_datadir}/libtool/libltdl/configure.ac
%{_mandir}/man1/libtool.1*
%{_mandir}/man1/libtoolize.1*
%{_infodir}/libtool.info*
%{_aclocaldir}/libtool.m4
%{_aclocaldir}/ltoptions.m4
%{_aclocaldir}/ltsugar.m4
%{_aclocaldir}/ltversion.m4
%{_aclocaldir}/lt~obsolete.m4

%files -n libltdl
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libltdl.so.?
%attr(755,root,root) %{_libdir}/libltdl.so.*.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libltdl.so
%{_libdir}/libltdl.la
%{_includedir}/libltdl
%{_includedir}/ltdl.h
%{_aclocaldir}/argz.m4
%{_aclocaldir}/ltdl.m4


