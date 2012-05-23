Summary:	Photobooth-inspired GNOME application
Name:		cheese
Version:	3.4.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	390d4997a4b52ac6da904306f1e699d1
BuildRequires:	clutter-gst-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-video-effects
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	itstool
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	librsvg-devel
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRequires:	xorg-libXtst-devel
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
Requires:	gnome-video-effects
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
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
	--disable-schemas-compile	\
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

%find_lang %{name} --with-gnome

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_desktopdir}/cheese.desktop
%{_iconsdir}/hicolor/*/*/*.*
%{_mandir}/man1/cheese.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcheese-gtk.so.??
%attr(755,root,root) %ghost %{_libdir}/libcheese.so.?
%attr(755,root,root) %{_libdir}/libcheese-gtk.so.*.*.*
%attr(755,root,root) %{_libdir}/libcheese.so.*.*.*
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/cheese
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/Cheese-3.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cheese

