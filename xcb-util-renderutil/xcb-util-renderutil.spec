Summary:	XCB util-renderutil module
Name:		xcb-util-renderutil
Version:	0.3.8
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	b346ff598ee093c141f836fbc0f8f721
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	m4
BuildRequires:	pkg-config
BuildRequires:	xorg-proto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCB util-renderutil module provides the following library:
- renderutil: Convenience functions for the Render extension.

%package devel
Summary:	Header files for XCB util-renderutil library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB util-renderutil library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static	\
	--disable-silent-rules
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
%attr(755,root,root) %ghost %{_libdir}/libxcb-render-util.so.?
%attr(755,root,root) %{_libdir}/libxcb-render-util.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-render-util.so
%{_libdir}/libxcb-render-util.la
%{_includedir}/xcb/*.h
%{_pkgconfigdir}/*.pc

