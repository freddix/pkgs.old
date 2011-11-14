Summary:	XCB support libraries
Name:		xcb-util
Version:	0.3.8
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	8ce019c4bbf20dce246b98f177cfccff
URL:		http://xcb.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package devel
Summary:	Header files for XCB util libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB util libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
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
%doc README
%attr(755,root,root) %ghost %{_libdir}/libxcb-*.so.?
%attr(755,root,root) %{_libdir}/libxcb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-*.so
%{_libdir}/libxcb-*.la
%{_includedir}/xcb/xcb_*.h
%{_pkgconfigdir}/xcb-*.pc

