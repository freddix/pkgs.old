%define		basever		3.4
%define		apiver		1.2
%define		apiver3		3.0

Summary:	Evolution data server
Name:		evolution-data-server
Version:	3.4.1
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution-data-server/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	c1362b0176e9eb8ec810813692dcf3fc
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	intltool
BuildRequires:	libgdata-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libgweather-devel
BuildRequires:	libical-devel
BuildRequires:	libsoup-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	openldap-devel
BuildRequires:	pkg-config
BuildRequires:	vala
Requires(post,postun):	rarian
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
The Evolution data server for the calendar and addressbook.

%package libs
Summary:	Evolution Data Server library
Group:		Libraries

%description libs
This package contains Evolution Data Server library.

%package devel
Summary:	Evolution data server development files
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications
using Evolution's data server libraries.

%package apidocs
Summary:	e-d-s API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
e-d-s API documentation.

%prep
%setup -q
# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules				\
	--disable-static				\
	--enable-vala-bindings				\
	--with-html-dir=%{_gtkdocdir}			\
	--with-krb5=no					\
	--with-libdb=%{_libdir}				\
	--with-openldap=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT		\
	HTML_DIR=%{_gtkdocdir}		\
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libexecdir}/*/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README
%dir %{_libexecdir}
%dir %{_libexecdir}/addressbook-backends
%dir %{_libexecdir}/calendar-backends
%dir %{_libexecdir}/camel-providers
%attr(755,root,root) %{_libexecdir}/camel-index-control-%{apiver}
%attr(755,root,root) %{_libexecdir}/camel-lock-helper-%{apiver}
%attr(755,root,root) %{_libexecdir}/evolution-addressbook-factory
%attr(755,root,root) %{_libexecdir}/evolution-calendar-factory
%attr(755,root,root) %{_libexecdir}/camel-providers/*.so
%attr(755,root,root) %{_libexecdir}/addressbook-backends/*.so
%attr(755,root,root) %{_libexecdir}/calendar-backends/*.so
%{_libdir}/%{name}/camel-providers/*.urls

%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service

%dir %{_datadir}/%{name}-%{basever}
%{_pixmapsdir}/%{name}

%{_datadir}/GConf/gsettings/libedataserver.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcamel-%{apiver}.so.??
%attr(755,root,root) %ghost %{_libdir}/libebackend-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/libebook-%{apiver}.so.??
%attr(755,root,root) %ghost %{_libdir}/libecal-%{apiver}.so.??
%attr(755,root,root) %ghost %{_libdir}/libedata-book-%{apiver}.so.??
%attr(755,root,root) %ghost %{_libdir}/libedata-cal-%{apiver}.so.??
%attr(755,root,root) %ghost %{_libdir}/libedataserver-%{apiver}.so.??
%attr(755,root,root) %ghost %{_libdir}/libedataserverui-%{apiver3}.so.?
%attr(755,root,root) %{_libdir}/libcamel-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libebackend-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libebook-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libecal-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libedata-book-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libedata-cal-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libedataserver-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libedataserverui-%{apiver3}.so.*.*.*
%{_libdir}/girepository-1.0/EBook-1.2.typelib
%{_libdir}/girepository-1.0/ECalendar-1.2.typelib
%{_libdir}/girepository-1.0/EDataServer-1.2.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcamel-%{apiver}.so
%attr(755,root,root) %{_libdir}/libebackend-%{apiver}.so
%attr(755,root,root) %{_libdir}/libebook-%{apiver}.so
%attr(755,root,root) %{_libdir}/libecal-%{apiver}.so
%attr(755,root,root) %{_libdir}/libedata-book-%{apiver}.so
%attr(755,root,root) %{_libdir}/libedata-cal-%{apiver}.so
%attr(755,root,root) %{_libdir}/libedataserver-%{apiver}.so
%attr(755,root,root) %{_libdir}/libedataserverui-%{apiver3}.so
%{_includedir}/evolution-data-server-%{basever}
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/EBook-1.2.gir
%{_datadir}/gir-1.0/ECalendar-1.2.gir
%{_datadir}/gir-1.0/EDataServer-1.2.gir
%{_datadir}/vala/vapi/libebook-1.2.deps
%{_datadir}/vala/vapi/libebook-1.2.vapi
%{_datadir}/vala/vapi/libecalendar-1.2.deps
%{_datadir}/vala/vapi/libecalendar-1.2.vapi
%{_datadir}/vala/vapi/libedataserver-1.2.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/camel
%{_gtkdocdir}/libebackend
%{_gtkdocdir}/libebook
%{_gtkdocdir}/libecal
%{_gtkdocdir}/libedata-book
%{_gtkdocdir}/libedata-cal
%{_gtkdocdir}/libedataserver
%{_gtkdocdir}/libedataserverui

