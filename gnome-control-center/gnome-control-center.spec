Summary:	GNOME Control Center
Name:		gnome-control-center
Version:	3.4.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-control-center/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	cebb27d87bdfc8175073eebb6610a498
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel
BuildRequires:	NetworkManager-applet-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cheese-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	gnome-settings-daemon-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libgnomekbd-devel
BuildRequires:	libgtop-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	nautilus-devel
BuildRequires:	tzdata
BuildRequires:	xorg-libXxf86misc-devel
BuildRequires:	xorg-libxkbfile-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	rarian
Requires(post,postun):	shared-mime-info
Requires:	gnome-settings-daemon
Requires:	gstreamer-plugins-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Configuration tool for easily setting up your GNOME environment.

%package devel
Summary:	GNOME Control Center header files
Group:		X11/Development/Libraries

%description devel
GNOME Control-Center header files.

%prep
%setup -q

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
	--disable-silent-rules		\
	--disable-static		\
	--disable-update-mimedb		\
	--enable-systemd		\
	--with-cheese			\
	--with-libsocialweb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ha,ig,la}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-control-center
%attr(755,root,root) %{_bindir}/gnome-sound-applet
%dir %{_libdir}/control-center-1
%dir %{_libdir}/control-center-1/panels
%attr(755,root,root) %{_libdir}/control-center-1/panels/libbackground.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libbluetooth.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libcolor.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdate_time.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdisplay.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libinfo.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libkeyboard.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libmouse-properties.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libnetwork.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libonline-accounts.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libregion.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libsound.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libpower.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libprinters.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libscreen.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libuniversal-access.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libuser-accounts.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libwacom-properties.so
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%{_datadir}/gnome-control-center
%{_datadir}/sounds/gnome
%{_datadir}/desktop-directories/*.directory
%{_iconsdir}/hicolor/*/*/*.*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/faces
%{_sysconfdir}/xdg/autostart/gnome-sound-applet.desktop
%{_sysconfdir}/xdg/menus/gnomecc.menu

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/*.pc

