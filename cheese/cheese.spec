Summary:	Photobooth-inspired GNOME application
Name:		cheese
Version:	2.32.0
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	e3b822e46b2558d0bbdfa4809d5d3c24
BuildRequires:	GConf-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	librsvg-devel
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRequires:	xorg-libXtst-devel
Requires(post,preun):	GConf
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gtk+-rsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures
and videos from a webcam. It also includes fancy graphical effects
based on the gstreamer-backend.

%package libs
Summary:	Cheese library
Group:		Libraries

%description libs
Cheese library.

%package devel
Summary:	Header files for cheese library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for cheese library.

%package apidocs
Summary:	cheese API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
cheese API documentation.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install	\
	--disable-scrollkeeper		\
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor/256x256
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall %{name}.schemas

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/cheese
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/cheese/*.sh
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_desktopdir}/cheese.desktop
%{_iconsdir}/hicolor/*/apps/cheese.*
%{_sysconfdir}/gconf/schemas/cheese.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcheese-gtk.so.??
%attr(755,root,root) %{_libdir}/libcheese-gtk.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcheese-gtk.so
%{_libdir}/libcheese-gtk.la
%{_includedir}/cheese
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cheese

