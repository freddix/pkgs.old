Summary:	X Fixes extension library
Name:		xorg-libXfixes
Version:	5.0
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2
# Source0-md5:	678071bd7f9f7467e2fc712d81022318
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Fixes extension library.

%package devel
Summary:	Header files for libXfixes library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Fixes extension library.

This package contains the header files needed to develop programs that
use libXfixes.

%prep
%setup -qn libXfixes-%{version}

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
%attr(755,root,root) %ghost %{_libdir}/libXfixes.so.?
%attr(755,root,root) %{_libdir}/libXfixes.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfixes.so
%{_libdir}/libXfixes.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xfixes.pc
%{_mandir}/man3/*.3x*

