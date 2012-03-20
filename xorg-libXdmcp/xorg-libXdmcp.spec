Summary:	X Display Manager Control Protocol library
Name:		xorg-libXdmcp
Version:	1.1.1
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
# Source0-md5:	b94af6cef211cf3ee256f7e81f70fcd9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Display Manager Control Protocol library.

%package devel
Summary:	Header files for libXdmcp library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Display Manager Control Protocol library.

This package contains the header files needed to develop programs that
use libXdmcp.

%prep
%setup -qn libXdmcp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--disable-silent-rules
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
%attr(755,root,root) %ghost %{_libdir}/libXdmcp.so.?
%attr(755,root,root) %{_libdir}/libXdmcp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXdmcp.so
%{_libdir}/libXdmcp.la
%{_includedir}/X11/Xdmcp.h
%{_pkgconfigdir}/xdmcp.pc

