Summary:	GNOME Bluetooth
Name:		gnome-bluetooth
Version:	3.4.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-bluetooth/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	6e5763f4cfd98753cb191346c156a786
URL:		http://live.gnome.org/GnomeBluetooth
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	nautilus-devel
BuildRequires:	pkg-config
BuildRequires:	sed >= 4.0
Requires(post,postun):	gdk-pixbuf
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	bluez
Requires:	obexd
Obsoletes:	bluez-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Bluetooth is a fork of bluez-gnome focused on integration
with the GNOME desktop environment

%package libs
Summary:	GNOME Bluetooth libraries
License:	LGPL
Group:		Development/Libraries

%description libs
GNOME bluetooth shared libraries.

%package devel
Summary:	Header files for GNOME bluetooth subsystem
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GNOME Bluetooth subsystem.

%package apidocs
Summary:	GNOME Bluetooth API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GNOME Bluetooth API documentation.

%package -n nautilus-sendto-bluetooth
Summary:	nautilus-sendto Bluetooth plugin
License:	LGPL
Group:		X11/Applications
Requires:	nautilus

%description -n nautilus-sendto-bluetooth
nautilus-sendto Bluetooth plugin.

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
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-desktop-update	\
	--disable-icon-update		\
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{en@shaw,mus}
rm -f $RPM_BUILD_ROOT%{_libdir}/*/*/*.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/plugins/libgbtgeoclue.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/status/*
%{_sysconfdir}/xdg/autostart/bluetooth-applet.desktop
%{_datadir}/GConf/gsettings/gnome-bluetooth-nst
%{_datadir}/glib-2.0/schemas/org.gnome.Bluetooth.nst.gschema.xml

%{_mandir}/man1/bluetooth-*.1*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
# no %ghost here!
%attr(755,root,root) %{_libdir}/%{name}/libgnome-bluetooth-applet.so.?
%attr(755,root,root) %ghost %{_libdir}/libgnome-bluetooth.so.??
%attr(755,root,root) %{_libdir}/%{name}/libgnome-bluetooth-applet.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnome-bluetooth.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/gnome-bluetooth/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/gnome-bluetooth-1.0.pc
%{_datadir}/gir-1.0/GnomeBluetooth-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files -n nautilus-sendto-bluetooth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus-sendto/plugins/libnstbluetooth.so

