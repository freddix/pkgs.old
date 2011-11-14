Summary:	xkbui library
Name:		xorg-libxkbui
Version:	1.0.2
Release:	11
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxkbui-%{version}.tar.bz2
# Source0-md5:	1143e456f7429e18e88f2eadb2f2b6b1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-libXt-devel
BuildRequires:	xorg-libxkbfile-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbui library.

%package devel
Summary:	Header files for libxkbui library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
xkbui library.

This package contains the header files needed to develop programs that
use libxkbui.

%prep
%setup -qn libxkbui-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
%attr(755,root,root) %ghost %{_libdir}/libxkbui.so.?
%attr(755,root,root) %{_libdir}/libxkbui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbui.so
%{_libdir}/libxkbui.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xkbui.pc

