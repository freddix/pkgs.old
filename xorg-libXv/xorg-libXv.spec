Summary:	X Video extension library
Name:		xorg-libXv
Version:	1.0.7
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.bz2
# Source0-md5:	5e1ac203ccd3ce3e89755ed1fbe75b0b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Video extension library.

%package devel
Summary:	Header files for libXv library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Video extension library.

This package contains the header files needed to develop programs that
use libXv.

%prep
%setup -qn libXv-%{version}

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
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXv.so.?
%attr(755,root,root) %{_libdir}/libXv.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXv.so
%{_libdir}/libXv.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xv.pc
%{_mandir}/man3/*.3x*

