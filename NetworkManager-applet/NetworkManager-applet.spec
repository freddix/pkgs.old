%define		orgname	network-manager-applet

Summary:	NetworkManager applet for GNOME
Name:		NetworkManager-applet
Version:	0.8.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/network-manager-applet/0.8/%{orgname}-%{version}.tar.xz
# Source0-md5:	ec454c37c2f4653e7da1b44ecb30869d
BuildRequires:	NetworkManager-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gnome-bluetooth-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libiw-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
Requires(post,preun):	GConf
Requires(post,postun):	hicolor-icon-theme
Requires:	NetworkManager
Requires:	gnome-keyring
Requires:	xdg-desktop-notification-daemon
Provides:	network-manager-applet = %{version}-%{release}
Obsoletes:	network-manager-applet < %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/NetworkManager

%description
Network Manager applet for GNOME.

%package -n gnome-bluetooth-nma
Summary:	GNOME Bluetooth plugin
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-bluetooth

%description -n gnome-bluetooth-nma
GNOME Bluetooth plugin.

%prep
%setup -qn %{orgname}-%{version}

sed -i -e 's|-Werror ||g' m4/*.m4

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/nm-applet
%attr(755,root,root) %{_bindir}/nm-connection-editor
%{_datadir}/nm-applet
%{_desktopdir}/nm-connection-editor.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_sysconfdir}/dbus-1/system.d/nm-applet.conf
%{_sysconfdir}/gconf/schemas/nm-applet.schemas
%{_sysconfdir}/xdg/autostart/*.desktop

%files -n gnome-bluetooth-nma
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-bluetooth/plugins/libnma.so

