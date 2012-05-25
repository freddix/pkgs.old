Summary:	GNOME media programs
Name:		gnome-media
Version:	2.32.0
Release:	1
License:	GPL v2+/LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-media/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	06fc8c67add34c98bc484e0dbc404d41
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-control-center-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
Requires(post,postun):	rarian
Requires(post,preun):	GConf
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gstreamer-plugins-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME media programs. GNOME is the GNU Network Object Model
Environment. That's a fancy name but really GNOME is a nice GUI
desktop environment. It makes using your computer easy, powerful, and
easy to configure.

%package libs
Summary:	gnome-media library
Group:		Development/Libraries

%description libs
This package contains gnome-media library.

%package cd
Summary:	CD player
Group:		X11/Applications/Multimedia
Requires(post):	GConf
Requires(post):	rarian
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}
Requires:	gstreamer-plugins-base

%description cd
CD player.

%package cddb
Summary:	CD database server
Group:		X11/Applications/Multimedia
Requires(post):	GConf
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description cddb
CD database server.

%package cddb-devel
Summary:	gnome-media-cddb devel file
Group:		X11/Development/Libraries
Requires:	%{name}-cddb = %{epoch}:%{version}-%{release}

%description cddb-devel
gnome-media-cddb devel files.

%package devel
Summary:	gnome-media devel files
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
gnome-media devel files.

%package sound-recorder
Summary:	Sound recorder
Group:		X11/Applications/Multimedia
Requires(post):	GConf
Requires(post):	rarian
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-plugins-base

%description sound-recorder
Sound recorder.

%package volume-control
Summary:	Volume controler
Group:		X11/Applications/Multimedia
# don't require base
Requires:	gstreamer-plugins-base
Requires:	libcanberra-runtime

%description volume-control
Volume control.

%package volume-control-applet
Summary:	Volume control applet
Group:		X11/Applications/Multimedia
# don't require base
Requires:	%{name}-volume-control = %{epoch}:%{version}-%{release}
Requires:	pulseaudio

%description volume-control-applet
Volume control applet.

%package -n gstreamer-properties
Summary:	Gstreamer properties
Group:		X11/Applications/Multimedia
Requires(post):	rarian
Requires:	GConf
Requires:	gstreamer-plugins-base

%description -n gstreamer-properties
Gstreamer properties.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-cddbslave		\
	--disable-gnomecd		\
	--disable-schemas-install	\
	--disable-scrollkeeper		\
	--disable-static		\
	--disable-vumeter
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D gstreamer-properties/gstreamer-properties.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/gstreamer-properties.png

rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/libgnome-media-profiles.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ha,ig,la}

%find_lang %{name}-2.0
%find_lang gnome-audio-profiles --with-gnome --with-omf
%find_lang gnome-sound-recorder --with-gnome --with-omf
%find_lang gstreamer-properties --with-gnome --with-omf
cat gnome-audio-profiles.lang >> %{name}-2.0.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install gnome-audio-profiles.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gnome-audio-profiles.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post sound-recorder
%scrollkeeper_update_post
%gconf_schema_install gnome-sound-recorder.schemas

%preun sound-recorder
%gconf_schema_install gnome-sound-recorder.schemas

%postun sound-recorder
%scrollkeeper_update_postun

%post -n gstreamer-properties
%scrollkeeper_update_post

%postun -n gstreamer-properties
%scrollkeeper_update_postun

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-audio-profiles-properties

%dir %{_datadir}/gnome-media
%dir %{_datadir}/gnome-media/icons
%dir %{_datadir}/gnome-media/sounds
%dir %{_datadir}/sounds/gnome
%dir %{_datadir}/sounds/gnome/default
%dir %{_datadir}/sounds/gnome/default/alerts

%{_datadir}/gnome-media/*.ui
%{_datadir}/gnome-media/icons/hicolor
%{_datadir}/gnome-media/sounds/gnome-sounds-default.xml
%{_datadir}/sounds/gnome/default/alerts/*.ogg

%{_iconsdir}/hicolor/*/*/*
%{_sysconfdir}/gconf/schemas/gnome-audio-profiles.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnome-media-profiles.so.?
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-media-profiles.so
%{_libdir}/libgnome-media-profiles.la
%{_includedir}/gnome-media
%{_pkgconfigdir}/*

%files sound-recorder -f gnome-sound-recorder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/gnome-sound-recorder
%{_desktopdir}/gnome-sound-recorder.desktop
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas

%files volume-control
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-volume-control
%{_desktopdir}/gnome-volume-control.desktop

%files volume-control-applet
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/gnome-volume-control-applet.desktop
%attr(755,root,root) %{_bindir}/gnome-volume-control-applet

%files -n gstreamer-properties -f gstreamer-properties.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gstreamer-properties
%{_datadir}/gstreamer-properties
%{_desktopdir}/gstreamer-properties.desktop
%{_pixmapsdir}/gstreamer-properties.png

