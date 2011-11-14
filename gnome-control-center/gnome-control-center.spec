Summary:	GNOME Control Center
Name:		gnome-control-center
Version:	2.32.1
Release:	2
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-control-center/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	b4e8ab5c7556ae07addbfcfb4fa2f761
Patch0:		%{name}-freddix.patch
Patch1:		%{name}-desktop-update.patch
Patch2:		%{name}-bug588729.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-settings-daemon-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libglade-devel
BuildRequires:	libgnomekbd-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	metacity-devel
BuildRequires:	nautilus-devel
BuildRequires:	xorg-libXxf86misc-devel
BuildRequires:	xorg-libxkbfile-devel
Requires(post,preun):	GConf
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gdk-pixbuf
Requires(post,postun):	rarian
Requires(post,postun):	shared-mime-info
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gnome-desktop
Requires:	gnome-main
Requires:	gnome-settings-daemon
Requires:	gstreamer-plugins-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Configuration tool for easily setting up your GNOME environment.

%package libs
Summary:	GNOME Control Center gnome-window-settings library
Group:		Development/Libraries

%description libs
This package contains gnome-window-settings library.

%package devel
Summary:	GNOME Control Center header files
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
GNOME Control-Center header files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__gnome_doc_prepare}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install	\
	--disable-silent-rules		\
	--disable-static		\
	--disable-update-desktop	\
	--disable-update-mimedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir="%{_pkgconfigdir}"

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions*/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la

rm -f $RPM_BUILD_ROOT%{_desktopdir}/gnomecc.desktop

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ha,ig,la}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install control-center.schemas
%gconf_schema_install fontilus.schemas
%gconf_schema_install gnome-control-center.schemas
%scrollkeeper_update_post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall control-center.schemas
%gconf_schema_uninstall fontilus.schemas
%gconf_schema_uninstall gnome-control-center.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/gnome-display-properties-install-systemwide
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so

%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/default-apps
%dir %{_datadir}/gnome-control-center/keybindings
%dir %{_libdir}/window-manager-settings

%{_datadir}/desktop-directories/*.directory
%{_datadir}/gnome-control-center/default-apps/gnome-default-applications.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/gnome-control-center/ui
%{_datadir}/gnome/cursor-fonts
%{_datadir}/mime/packages/*.xml
%{_datadir}/polkit-1/actions/org.gnome.randr.policy

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg

%{_sysconfdir}/gconf/schemas/control-center.schemas
%{_sysconfdir}/gconf/schemas/fontilus.schemas
%{_sysconfdir}/gconf/schemas/gnome-control-center.schemas
%{_sysconfdir}/xdg/menus/gnomecc.menu

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-window-settings-2.0
%{_pkgconfigdir}/*.pc

