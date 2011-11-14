Summary:	XCB util-image module
Name:		xcb-util-image
Version:	0.3.8
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	245a96041f373b05764148e52d2e0211
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	m4
BuildRequires:	pkg-config
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-proto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCB util-image module provides the following library:
- image: Port of Xlib's XImage and XShmImage functions.

%package devel
Summary:	Header files for XCB util-image library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB util-image library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libxcb-image.so.?
%attr(755,root,root) %{_libdir}/libxcb-image.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-image.so
%{_libdir}/libxcb-image.la
%{_includedir}/xcb/*.h
%{_pkgconfigdir}/*.pc

