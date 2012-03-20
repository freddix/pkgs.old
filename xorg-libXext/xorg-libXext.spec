Summary:	X extension library
Name:		xorg-libXext
Version:	1.3.1
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
# Source0-md5:	71251a22bc47068d60a95f50ed2ec3cf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X extension library.

%package devel
Summary:	Header files for libXext library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X extension library.

This package contains the header files needed to develop programs that
use libXext.

%prep
%setup -qn libXext-%{version}

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
%attr(755,root,root) %ghost %{_libdir}/libXext.so.?
%attr(755,root,root) %{_libdir}/libXext.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXext.so
%{_libdir}/libXext.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xext.pc
%{_mandir}/man3/*.3x*

