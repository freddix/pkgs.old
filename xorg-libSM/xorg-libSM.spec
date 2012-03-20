Summary:	Session Management library
Name:		xorg-libSM
Version:	1.2.1
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.bz2
# Source0-md5:	766de9d1e1ecf8bf74cebe2111d8e2bd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libICE-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Session Management library.

%package devel
Summary:	Header files for libSM library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Session Management library.

This package contains the header files needed to develop programs that
use libSM.

%prep
%setup -qn libSM-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-specs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libSM.so.?
%attr(755,root,root) %{_libdir}/libSM.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSM.so
%{_libdir}/libSM.la
%dir %{_includedir}/X11/SM
%{_includedir}/X11/SM/*.h
%{_pkgconfigdir}/sm.pc

