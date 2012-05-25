Summary:	UPnP library
Name:		gupnp
Version:	0.18.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp/0.18/%{name}-%{version}.tar.xz
# Source0-md5:	9ce2bc56abf0275be9b1d0ecdf67e7bf
URL:		http://gupnp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gssdp-devel
BuildRequires:	gtk-doc
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary:	Header files for gupnp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for the Linux SDK for UPnP Devices
(gupnp).

%package apidocs
Summary:	gupnp API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gupnp API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules			\
	--disable-static			\
	--with-context-manager=linux		\
	--with-html-dir=%{_gtkdocdir}
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
%attr(755,root,root) %ghost %{_libdir}/libgupnp-1.0.so.?
%attr(755,root,root) %{_libdir}/libgupnp-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gupnp-binding-tool
%attr(755,root,root) %{_libdir}/libgupnp-1.0.so
%{_datadir}/gir-1.0/GUPnP-1.0.gir
%{_includedir}/gupnp-1.0
%{_pkgconfigdir}/gupnp-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp

