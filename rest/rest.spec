Summary:	A library for access to RESTful web services
Name:		rest
Version:	0.7.12
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rest/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	dc14e0d89d38af5d8d544ce8f124d186
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	0.7

%description
A library for access to RESTful web services This library was designed
to make it easier to access web services that claim to be "RESTful". A
RESTful service should have urls that represent remote objects, which
methods can then be called on. The majority of services don't actually
adhere to this strict definition. Instead, their RESTful end point
usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of
API that this library is attempting to support.

%package devel
Summary:	Header files for rest library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for rest library.

%package apidocs
Summary:	rest API documentation
Group:		Documentation

%description apidocs
API documentation for rest library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc	\
	--disable-silent-rules	\
	--disable-static	\
	--with-ca-certificates=/etc/certs/ca-certificates.crt	\
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/librest-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/librest-extras-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/librest-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/librest-extras-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librest-%{apiver}.so
%attr(755,root,root) %{_libdir}/librest-extras-%{apiver}.so
%{_libdir}/*.la
%{_datadir}/gir-1.0/*.gir
%{_includedir}/rest-%{apiver}
%{_pkgconfigdir}/rest-%{apiver}.pc
%{_pkgconfigdir}/rest-extras-%{apiver}.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/rest-%{apiver}

