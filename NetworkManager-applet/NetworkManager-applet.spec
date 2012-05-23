%define		orgname	network-manager-applet

Summary:	NetworkManager applet for GNOME
Name:		NetworkManager-applet
Version:	0.9.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/network-manager-applet/0.9/%{orgname}-%{version}.tar.xz
# Source0-md5:	a8de4ace4a40e432838e434f0bf71e7a
BuildRequires:	NetworkManager-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gnome-bluetooth-devel
BuildRequires:	gtk+-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
Requires(post,preun):	GConf
Requires(post,postun):	hicolor-icon-theme
Requires:       %{name}-libs = %{version}-%{release}
Requires:	NetworkManager
Requires:	xdg-desktop-notification-daemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/NetworkManager

%description
Network Manager applet for GNOME.

%package libs
Summary:        GTK+ dialogs library for NetworkManager
Group:          Development/Libraries

%description libs
GTK+ dialogs library for NetworkManager.

%package devel
Summary:        Development files for nm-gtk library
Group:          X11/Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Development files for nm-gtk library.

%package -n gnome-bluetooth-plugin-network-manager
Summary:	GNOME Bluetooth plugin
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-bluetooth

%description -n gnome-bluetooth-plugin-network-manager
GNOME Bluetooth plugin.

%prep
%setup -qn %{orgname}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install nm-applet.schemas

%preun
%gconf_schema_uninstall nm-applet.schemas

%postun
%update_icon_cache hicolor

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/nm-applet
%attr(755,root,root) %{_bindir}/nm-connection-editor
%{_datadir}/nm-applet
%{_desktopdir}/nm-applet.desktop
%{_desktopdir}/nm-connection-editor.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_sysconfdir}/gconf/schemas/nm-applet.schemas
%{_sysconfdir}/xdg/autostart/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libnm-gtk.so.?
%attr(755,root,root) %{_libdir}/libnm-gtk.so.*.*.*
%{_datadir}/libnm-gtk

%files devel
%defattr(644,root,root,755)
%{_includedir}/libnm-gtk
%{_libdir}/libnm-gtk.so
%{_pkgconfigdir}/libnm-gtk.pc

%files -n gnome-bluetooth-plugin-network-manager
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-bluetooth/plugins/libnma.so

