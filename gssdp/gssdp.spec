Summary:	Simple Service Discovery Protocol library
Name:		gssdp
Version:	0.12.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	e7ac04abe7349a89d13d0ab4ee7d2e1b
URL:		http://gupnp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSSDP implements resource discovery and announcement over SSDP.

%package libs
Summary:	gssdp library
Group:		Libraries

%description libs
gssdp library.

%package devel
Summary:	Header files for gssdp
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files for gssdp.

%package apidocs
Summary:	gssdp API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gssdp API documentation.

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
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gssdp-device-sniffer
%dir %{_datadir}/gssdp
%{_datadir}/gssdp/gssdp-device-sniffer.ui

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgssdp-1.0.so.?
%attr(755,root,root) %{_libdir}/libgssdp-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssdp-1.0.so
%{_datadir}/gir-1.0/GSSDP-1.0.gir
%{_libdir}/libgssdp-1.0.la
%{_includedir}/gssdp-1.0
%{_pkgconfigdir}/gssdp-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gssdp

