Summary:	Utility for managing filesystem extended attributes
Name:		attr
Version:	2.4.43
Release:	3
License:	LGPL v2+ (library), GPL v2+ (utilities)
Group:		Applications/System
Source0:	ftp://linux-xfs.sgi.com/projects/xfs/cmd_tars/%{name}_%{version}-1.tar.gz
# Source0-md5:	91583a14bcbd637adaa9b07ea49c5d4b
Patch0:		%{name}-miscfix.patch
Patch1:		%{name}-lt.patch
Patch2:		%{name}-LDFLAGS.patch
URL:		http://oss.sgi.com/projects/xfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_libdir		/%{_lib}
%define		_libexecdir	/usr/%{_lib}

%description
An experimental attr command to manipulate extended attributes under
Linux.

%package devel
Summary:	Header files and libraries to use extended attributes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files to develop software which manipulate extended attributes.

%package static
Summary:	Static libraries for extended attributes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for extended attributes.

%description static -l pl.UTF-8
Biblioteki statyczne do korzystania z rozszerzonych atrybutów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f aclocal.m4

%build
mv install-sh install-custom-sh
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
install %{_datadir}/automake/config.* .
mv install-custom-sh install-sh

%configure \
	DEBUG="-DNDEBUG" \
	OPTIMIZER="%{rpmcflags} -DENABLE_GETTEXT"

%{__make} \
	LLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

DIST_ROOT=$RPM_BUILD_ROOT
DIST_INSTALL=`pwd`/install.manifest
DIST_INSTALL_DEV=`pwd`/install-dev.manifest
DIST_INSTALL_LIB=`pwd`/install-lib.manifest
export DIST_ROOT DIST_INSTALL DIST_INSTALL_DEV DIST_INSTALL_LIB

%{__make} -j1 install \
	DIST_MANIFEST=$DIST_INSTALL
%{__make} -j1 install-dev \
	DIST_MANIFEST=$DIST_INSTALL_DEV
%{__make} -j1 install-lib \
	DIST_MANIFEST=$DIST_INSTALL_LIB

ln -sf %{_libdir}/$(basename $RPM_BUILD_ROOT%{_libdir}/libattr.so.*.*.*) \
	 $RPM_BUILD_ROOT%{_libexecdir}/libattr.so

%{__sed} -i "s|libdir='%{_libdir}'|libdir='%{_libexecdir}'|" \
	$RPM_BUILD_ROOT%{_libexecdir}/libattr.la

rm -rf	$RPM_BUILD_ROOT%{_mandir}/man2

%find_lang %{name}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

# already in /usr
rm -f $RPM_BUILD_ROOT%{_libdir}/libattr.{so,la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/CHANGES
%attr(755,root,root) %{_bindir}/attr
%attr(755,root,root) %{_bindir}/getfattr
%attr(755,root,root) %{_bindir}/setfattr
%attr(755,root,root) %ghost %{_libdir}/libattr.so.?
%attr(755,root,root) %{_libdir}/libattr.so.*.*.*
%{_mandir}/man1/attr.1*
%{_mandir}/man1/getfattr.1*
%{_mandir}/man1/setfattr.1*
%{_mandir}/man5/attr.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/libattr.so
%{_libexecdir}/libattr.la
%{_includedir}/attr
%{_mandir}/man3/attr_*.3*

%files static
%defattr(644,root,root,755)
%{_libexecdir}/libattr.a

