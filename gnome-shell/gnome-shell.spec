Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	3.4.1
Release:	2
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	82a7dae5d0aa3de2afe317d882c79ee9
Patch0:		%{name}-freddix.patch
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	folks-devel
BuildRequires:	gcr-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	gnome-bluetooth-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libcanberra-devel
BuildRequires:	libcroco-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mutter-devel >= 3.4.1
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	startup-notification-devel
BuildRequires:	systemd-devel
BuildRequires:	telepathy-glib-devel
BuildRequires:	telepathy-logger-devel
Requires(post,postun):	glib-gio-gsettings
Requires:	accountsservice
Requires:	at-spi2-atk
Requires:	caribou
Requires:	evolution-data-server
Requires:	gjs
Requires:	gnome-menus
Requires:	gnome-settings-daemon
Requires:	gsettings-desktop-schemas
Requires:	mutter
Requires:	nautilus
Requires:	telepathy-logger
Requires:	telepathy-mission-control
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
GNOME Shell is the defining technology of the GNOME 3 desktop user
experience. It provides core interface functions like switching to
windows and launching applications. GNOME Shell takes advantage of the
capabilities of modern graphics hardware and introduces innovative
user interface concepts to provide a delightful and easy to use
experience.

%package apidocs
Summary:	GNOME Shell API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
This package provides GNOME Shell API documentation.

%package -n browser-plugin-%{name}
Summary:	gnome-shell plugin for WWW browsers
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n browser-plugin-%{name}
gnome-shell plugin for WWW browsers.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-ca-certificates=/etc/certs/ca-certificates.crt	\
	--with-html-dir=%{_gtkdocdir}	\
	--with-systemd
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-shell/{extensions,search-providers}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mozillalibdir=%{_libdir}/browser-plugins

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-shell/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%attr(755,root,root) %{_bindir}/gnome-shell-extension-prefs
%attr(755,root,root) %{_bindir}/gnome-shell-extension-tool
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnome-shell-calendar-server
%attr(755,root,root) %{_libexecdir}/gnome-shell-hotplug-sniffer
%attr(755,root,root) %{_libexecdir}/gnome-shell-perf-helper
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell.so
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell-js.so
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/ShellJS-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-shell
%{_desktopdir}/gnome-shell.desktop
%{_desktopdir}/gnome-shell-extension-prefs.desktop
%{_mandir}/man1/gnome-shell.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/shell
%{_gtkdocdir}/st

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/browser-plugins/libgnome-shell-browser-plugin.so

