Summary:	Xau - Authorization Protocol for X
Name:		xorg-libXau
Version:	1.0.7
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.bz2
# Source0-md5:	2d241521df40d27034413436d1a1465c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xau - Authorization Protocol for X.

%package devel
Summary:	Header files for libXau library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xau - Authorization Protocol for X.

This package contains the header files needed to develop programs that
use libXau.

%prep
%setup -qn libXau-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libXau.so.?
%attr(755,root,root) %{_libdir}/libXau.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXau.so
%{_libdir}/libXau.la
%{_includedir}/X11/Xauth.h
%{_pkgconfigdir}/xau.pc
%{_mandir}/man3/*.3x*

