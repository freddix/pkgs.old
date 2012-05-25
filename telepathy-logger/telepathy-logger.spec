Summary:	Logging service for Telepathy
Name:		telepathy-logger
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Applications
Source0:	http://telepathy.freedesktop.org/releases/telepathy-logger/%{name}-%{version}.tar.bz2
# Source0-md5:	0b891b860c7f3a01926f5cc22fd26120
Patch0:		%{name}-configure.patch
URL:		http://telepathy.freedesktop.org/wiki/Logger
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRequires:	telepathy-glib-devel
BuildRequires:	xorg-libICE-devel
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/telepathy

%description
This package provides logging service for Telepathy.

%package apidocs
Summary:	telepathy-logger library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%package libs
Summary:	telepathy-logger shared library
Group:		Libraries

%description libs
telepathy-logger shared library.

%package devel
Summary:	Header files for telepathy-logger library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for telepathy-logger library.

%description apidocs
telepathy-logger library API documentation.

%prep
%setup -q
%patch -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libexecdir}/telepathy-logger
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Logger.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Telepathy.Logger.gschema.xml
%{_datadir}/telepathy/clients/Logger.client

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-logger

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-logger.so.?
%attr(755,root,root) %{_libdir}/libtelepathy-logger.so.*.*.*
%{_libdir}/girepository-1.0/TelepathyLogger-0.2.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-logger.so
%{_datadir}/gir-1.0/TelepathyLogger-0.2.gir
%{_includedir}/telepathy-logger-0.2
%{_pkgconfigdir}/telepathy-logger-0.2.pc

