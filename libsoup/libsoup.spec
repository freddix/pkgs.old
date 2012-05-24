Summary:	SOAP (Simple Object Access Protocol) implementation in C
Name:		libsoup
Version:	2.38.1
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libsoup/2.38/%{name}-%{version}.tar.xz
# Source0-md5:	d13fb4968acea24c26b83268a308f580
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gnutls-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libproxy-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	2.4

%description
It provides an queued asynchronous callback-based mechanism for
sending and servicing SOAP requests, and a WSDL (Web Service
Definition Language) to C compiler which generates client stubs and
server skeletons for easily calling and implementing SOAP methods.

%package devel
Summary:	Include files etc to develop SOAP applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files, etc you can use to develop SOAP applications.

%package gnome
Summary:	GNOME bindings to libsoup
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME bindings to libsoup.

%package gnome-devel
Summary:	Include files etc to develop SOAP applications
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
Header files, etc you can use to develop SOAP applications.

%package apidocs
Summary:	libsoup API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libsoup API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--disable-tls-check		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gnome -p /sbin/ldconfig
%postun gnome -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libsoup-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libsoup-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/Soup-2.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-%{apiver}.so
%{_libdir}/libsoup-%{apiver}.la
%{_includedir}/libsoup-%{apiver}
%{_pkgconfigdir}/libsoup-%{apiver}.pc
%{_datadir}/gir-1.0/Soup-2.4.gir

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsoup-gnome-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libsoup-gnome-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/SoupGNOME-2.4.typelib

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-gnome-%{apiver}.so
%{_libdir}/libsoup-gnome-%{apiver}.la
%{_includedir}/libsoup-gnome-%{apiver}
%{_pkgconfigdir}/libsoup-gnome-%{apiver}.pc
%{_datadir}/gir-1.0/SoupGNOME-2.4.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsoup-*

