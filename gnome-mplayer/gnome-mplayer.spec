%define		gecko_ver	1.0.3

Summary:	Simple GUI for MPlayer
Name:		gnome-mplayer
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://gnome-mplayer.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	72a1c7d640a67eb2d60f2671108919c2
Source1:	http://gecko-mediaplayer.googlecode.com/files/gecko-mediaplayer-%{gecko_ver}.tar.gz
# Source1-md5:	4996b243ed720dc30f5dcc9bc253bf68
Source2:	%{name}.desktop
URL:		http://code.google.com/p/gnome-mplayer/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libmusicbrainz3-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	nautilus-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xulrunner-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%{_libdir}/browser-plugins

%description
GNOME MPlayer is a simple GUI for MPlayer. It is based heavily
on the mplayerplug-in source code and can basically be seen as
a standalone version of that.

%package -n browser-plugin-gnome-mplayer
Summary:	GNOME MPlayer web browser plugin
Group:		X11/Applications
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{version}-%{release}

%description -n browser-plugin-gnome-mplayer
GNOME MPlayer xulrunner plugin.

%package -n nautilus-extension-gnome-mplayer
Summary:	GNOME MPlayer nautilus extension
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus

%description -n nautilus-extension-gnome-mplayer
GNOME MPlayer nautilus extension.

%prep
%setup -q -a1
sed -i 's|install-data-hook: install-schemas|install-data-hook:|' Makefile.am

cd gecko-mediaplayer-%{gecko_ver}
sed -i 's|install-data-hook: install-schemas|install-data-hook:|' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--with-gpm-new-method
%{__make}

cd gecko-mediaplayer-%{gecko_ver}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-silent-rules
%{__make} \
	GECKO_IDLDIR="%{_includedir}/xulrunner/idl/stable"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C gecko-mediaplayer-%{gecko_ver} install	\
	DESTDIR=$RPM_BUILD_ROOT			\
	install_libexecdir="%{plugindir}"	\
	xptdir="%{plugindir}"

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

rm -rf $RPM_BUILD_ROOT%{_docdir}/{%{name},gecko-mediaplayer}

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la
rm -f $RPM_BUILD_ROOT%{libdir}/browser-plugins/*.la

%find_lang %{name}
%find_lang gecko-mediaplayer

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_gsettings_cache

%post -n browser-plugin-gnome-mplayer
%update_gsettings_cache

%preun -n browser-plugin-gnome-mplayer
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gnome-mplayer
%{_datadir}/glib-2.0/schemas/apps.gnome-mplayer.preferences.enums.xml
%{_datadir}/glib-2.0/schemas/apps.gnome-mplayer.preferences.gschema.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/gnome-mplayer.*
%{_mandir}/man1/gnome-mplayer.1*

%files -n browser-plugin-gnome-mplayer -f gecko-mediaplayer.lang
%attr(755,root,root) %{plugindir}/gecko-mediaplayer-dvx.so
%attr(755,root,root) %{plugindir}/gecko-mediaplayer-qt.so
%attr(755,root,root) %{plugindir}/gecko-mediaplayer-rm.so
%attr(755,root,root) %{plugindir}/gecko-mediaplayer-wmp.so
%attr(755,root,root) %{plugindir}/gecko-mediaplayer.so
%{_datadir}/glib-2.0/schemas/apps.gecko-mediaplayer.preferences.gschema.xml

%files -n nautilus-extension-gnome-mplayer
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/*.so

