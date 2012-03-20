Summary:	Xxf86vm library
Name:		xorg-libXxf86vm
Version:	1.1.2
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.bz2
# Source0-md5:	ffd93bcedd8b2b5aeabf184e7b91f326
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xxf86vm library.

%package devel
Summary:	Header files for libXxf86vm library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xxf86vm library.

This package contains the header files needed to develop programs that
use libXxf86vm.

%prep
%setup -qn libXxf86vm-%{version}

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
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXxf86vm.so.?
%attr(755,root,root) %{_libdir}/libXxf86vm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86vm.so
%{_libdir}/libXxf86vm.la
%{_includedir}/X11/extensions/xf86vmode.h
%{_pkgconfigdir}/xxf86vm.pc
%{_mandir}/man3/*.3x*

