Summary:	GNOME panel
Name:		gnome-panel
Version:	3.4.2.1
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-panel/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	1a7c12b22b7e5f61ce7ab90608b2c2c8
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dconf-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgweather-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
BuildRequires:	python-libxml2
BuildRequires:	telepathy-glib-devel
Requires(post,preun):	GConf
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	rarian
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgweather-data
Requires:	polkit
Requires:	xdg-icon-theme
Requires:	xdg-menus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
The gnome-panel packages provides the GNOME panel, menus and some
basic applets for the panel.

%package libs
Summary:	GNOME panel library
Group:		X11/Libraries

%description libs
GNOME panel library.

%package devel
Summary:	GNOME panel includes, and more
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Panel header files for creating GNOME panels.

%package apidocs
Summary:	panel-applet API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
panel-applet API documentation.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-schemas-install	\
	--disable-scrollkeeper		\
	--disable-silent-rules		\
	--disable-static		\
	--enable-eds			\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,en@shaw,ha,ig,la,ps}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install clock.schemas
%update_gsettings_cache
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall clock.schemas

%postun
%update_gsettings_cache
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%dir %{_libexecdir}
%attr(755,root,root) %{_bindir}/gnome-desktop-item-edit
%attr(755,root,root) %{_bindir}/gnome-panel
%attr(755,root,root) %{_libexecdir}/clock-applet
%attr(755,root,root) %{_libexecdir}/fish-applet
%attr(755,root,root) %{_libexecdir}/gnome-panel-add
%attr(755,root,root) %{_libexecdir}/notification-area-applet
%attr(755,root,root) %{_libexecdir}/wnck-applet

%{_datadir}/dbus-1/services/org.gnome.panel.applet.ClockAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.FishAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.NotificationAreaAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.WnckletFactory.service

%{_sysconfdir}/gconf/schemas/clock.schemas
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.applet.fish.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.applet.window-list.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.applet.workspace-switcher.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.launcher.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.menu-button.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.object.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-panel.toplevel.gschema.xml

%{_datadir}/gnome-panel
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpanel-applet-4.so
%{_includedir}/gnome-panel-4.0
%{_pkgconfigdir}/libpanelapplet-4.0.pc
%{_datadir}/gir-1.0/PanelApplet-4.0.gir

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpanel-applet-4.so.?
%attr(755,root,root) %{_libdir}/libpanel-applet-4.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/panel-applet-4.0

