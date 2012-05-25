Summary:	GNOME Display Manager
Name:		gdm
Version:	3.4.1
Release:	8
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdm/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	fda0470340f9c0bc2f8daccb280af520
Source1:	%{name}-password.pamd
Source2:	%{name}-welcome.pamd
Source10:	%{name}.service
Source11:	%{name}-tmpfiles.conf
Patch0:		%{name}-polkit.patch
Patch1:		%{name}-defaults.patch
Patch2:		%{name}-paths.patch
URL:		http://www.gnome.org/projects/gdm/
BuildRequires:	accountsservice-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	check
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libtool
BuildRequires:	libxklavier-devel
BuildRequires:	nss-devel
BuildRequires:	pam-devel
BuildRequires:	pango-devel
BuildRequires:	perl-modules
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
BuildRequires:  systemd-devel
BuildRequires:	upower-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXau-devel
BuildRequires:	xorg-libXdmcp-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(posttrans):	dconf
Requires:	%{name}-libs = %{version}-%{release}
Requires:	accountsservice
Requires:	dbus-xinit
Requires:	gnome-session
Requires:	gnome-settings-daemon
Requires:	gnome-shell
Requires:	hicolor-icon-theme
Requires:	pam
Requires:	which
Requires:	xorg-app-sessreg
Requires:	xorg-xserver-server
Provides:	group(xdm)
Provides:	user(xdm)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%package libs
Summary:	GDM libraries
Group:		Libraries

%description libs
GDM libraries.

%package devel
Summary:	Header files for GDM
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications
using GDM's libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
touch data/gdm.schemas.in.in
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile		\
	--disable-scrollkeeper			\
	--disable-silent-rules			\
	--disable-static			\
	--enable-authentication-scheme=pam	\
	--enable-split-authentication		\
	--with-at-spi-registryd-directory=/usr/lib/at-spi2	\
	--with-console-kit=no			\
	--with-group=xdm			\
	--with-pam-prefix=/etc			\
	--with-systemd				\
	--with-tcp-wrappers=no			\
	--with-user=xdm				\
	--with-xinerama=yes			\
	--without-selinux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/pam.d \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/log/gdm} \
	$RPM_BUILD_ROOT{%{_datadir}/xsessions,%{systemdunitdir}} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=%{_sysconfdir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm-password
install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/gdm-welcome
install %{SOURCE10} $RPM_BUILD_ROOT%{systemdunitdir}/gdm.service
install %{SOURCE11} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/gdm.conf

%find_lang %{name} --with-gnome --with-omf --all-name

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdm/simple-greeter/extensions/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%posttrans
umask 022
/usr/bin/dconf update

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "GNOME Display Manager" -g xdm xdm

%post
%systemd_reload
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%systemd_reload
%update_icon_cache hicolor
%update_gsettings_cache
if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm-password
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm-welcome

%attr(1755,root,xdm) %dir /var/cache/gdm
%attr(1770,root,xdm) %dir /var/gdm
%attr(1770,root,xdm) %dir /var/lib/gdm
%attr(711,root,xdm) %dir /var/run/gdm
%attr(750,xdm,xdm) %dir /var/log/gdm
%attr(750,xdm,xdm) /home/services/xdm
%attr(755,xdm,xdm) %dir /var/lib/gdm/.config/dconf
%attr(755,xdm,xdm) %dir /var/run/gdm/greeter
%attr(755,xdm,xdm) /var/lib/gdm/.local
%dir %{_libdir}/gdm/simple-greeter
%dir %{_libdir}/gdm/simple-greeter/extensions
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%dir %{_sysconfdir}/gdm/PostLogin
%dir /var/lib/gdm/.config

%attr(755,root,root) %config %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession

%attr(755,root,root) %{_bindir}/gdm-screenshot
%attr(755,root,root) %{_bindir}/gdmflexiserver
#%attr(755,root,root) %{_libdir}/gdm/simple-greeter/extensions/libfingerprint.so
%attr(755,root,root) %{_libdir}/gdm/simple-greeter/extensions/libpassword.so
#%attr(755,root,root) %{_libdir}/gdm/simple-greeter/extensions/libsmartcard.so
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gdm-crash-logger
%attr(755,root,root) %{_libexecdir}/gdm-factory-slave
%attr(755,root,root) %{_libexecdir}/gdm-product-slave
%attr(755,root,root) %{_libexecdir}/gdm-session-worker
%attr(755,root,root) %{_libexecdir}/gdm-simple-greeter
%attr(755,root,root) %{_libexecdir}/gdm-simple-slave
%attr(755,root,root) %{_libexecdir}/gdm-smartcard-worker
# XDMCP
%attr(755,root,root) %{_libexecdir}/gdm-host-chooser
%attr(755,root,root) %{_libexecdir}/gdm-simple-chooser
%attr(755,root,root) %{_libexecdir}/gdm-xdmcp-chooser-slave

%attr(755,root,root) %{_sbindir}/gdm
%attr(755,root,root) %{_sbindir}/gdm-binary
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/*
%{_datadir}/gdm
%{_datadir}/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
%{_datadir}/gnome-session/sessions/gdm-fallback.session
%{_datadir}/gnome-session/sessions/gdm-shell.session
%{_datadir}/polkit-1/actions/gdm.policy
%{_iconsdir}/hicolor/*/apps/*.png
%{_pixmapsdir}/*
%{_sysconfdir}/dconf/db/gdm.d
%{_sysconfdir}/dconf/profile/gdm
%{systemdtmpfilesdir}/%{name}.conf
%{systemdunitdir}/gdm.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgdmgreeter.so.?
%attr(755,root,root) %ghost %{_libdir}/libgdmsimplegreeter.so.?
%attr(755,root,root) %{_libdir}/libgdmgreeter.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdmsimplegreeter.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/gdm
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir

