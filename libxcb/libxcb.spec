Summary:	X protocol C-language Binding library
Name:		libxcb
Version:	1.8.1
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	a906566857eb9ba2772a7d40da4f04fe
URL:		http://xcb.freedesktop.org/
BuildRequires:	check-devel
BuildRequires:	doxygen
BuildRequires:	libpthread-stubs
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	xorg-libXau-devel
BuildRequires:	xorg-libXdmcp-devel
BuildRequires:	xorg-proto >= 7.6-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol C-language Binding library.

libxcb provides an interface to the X Window System protocol, slated to
replace the current Xlib interface. It has several advantages over
Xlib, including:
- size: small library and lower memory footprint
- latency hiding: batch several requests and wait for the replies later
- direct protocol access: one-to-one mapping between interface and protocol
- proven thread support: transparently access XCB from multiple threads
- easy extension implementation: interfaces auto-generated from XML-XCB

Xlib can also use XCB as a transport layer, allowing software to make
requests and receive responses with both, which eases porting to XCB.
However, client programs, libraries, and toolkits will gain the most
benefit from a native XCB port.

%package devel
Summary:	Header files for XCB library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
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

rm -rf $RPM_BUILD_ROOT%{_docdir}/libxcb

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %ghost %{_libdir}/libxcb-*.so.?
%attr(755,root,root) %ghost %{_libdir}/libxcb.so.?
%attr(755,root,root) %{_libdir}/libxcb-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libxcb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-*.so
%attr(755,root,root) %{_libdir}/libxcb.so
%{_libdir}/libxcb*.la
%{_includedir}/xcb
%{_pkgconfigdir}/xcb-*.pc
%{_pkgconfigdir}/xcb.pc

