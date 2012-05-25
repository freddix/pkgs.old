Summary:	GNOME Settings Daemon
Name:		gnome-settings-daemon
Version:	3.4.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	28144a0c69556cf1915a8e43c25a2869
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	colord-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	intltool
BuildRequires:	libgnomekbd-devel
BuildRequires:	libtool
BuildRequires:	libwacom-devel
BuildRequires:	libxklavier-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	systemd-devel
BuildRequires:	xorg-driver-input-wacom-devel
BuildRequires:	xorg-libXxf86misc-devel
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
GNOME Settings Daemon.

%package devel
Summary:	Header file for developing GNOME Settings Daemon clients
Group:		Development/Libraries

%description devel
Header file for developing GNOME Settings Daemon clients.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-systemd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ha,ig,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/gnome-settings-daemon

%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/*.so
%{_libdir}/gnome-settings-daemon-3.0/*-plugin
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/dbus-1/services/org.gnome.SettingsDaemon.service
%{_datadir}/gnome-settings-daemon
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop
%{_iconsdir}/hicolor/*/*/*.*
%{_mandir}/man1/gnome-settings-daemon.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-3.0
%{_pkgconfigdir}/gnome-settings-daemon.pc

