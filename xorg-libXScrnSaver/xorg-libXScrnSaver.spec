Summary:	XScrnSaver library
Name:		xorg-libXScrnSaver
Version:	1.2.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2
# Source0-md5:	7a773b16165e39e938650bcc9027c1d5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XScrnSaver library.

%package devel
Summary:	Header files for libXScrnSaver library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
XScrnSaver library.

This package contains the header files needed to develop programs that
use libXScrnSaver.

%prep
%setup -qn libXScrnSaver-%{version}

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
%attr(755,root,root) %ghost %{_libdir}/libXss.so.?
%attr(755,root,root) %{_libdir}/libXss.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXss.so
%{_libdir}/libXss.la
%{_includedir}/X11/extensions/scrnsaver.h
%{_pkgconfigdir}/xscrnsaver.pc
%{_mandir}/man3/*.3x*

