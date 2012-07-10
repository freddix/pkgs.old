%define		apiver	0.14

Summary:	Tracker - an indexing subsystem
Name:		tracker
Version:	0.14.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker/0.14/%{name}-%{version}.tar.xz
# Source0-md5:	35cbd8e791bbc809b42f54948c602c43
Patch0:		%{name}-link.patch
URL:		http://projects.gnome.org/tracker/
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	enca-devel
BuildRequires:	evolution-devel
BuildRequires:	exempi-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gtk-doc
BuildRequires:	id3lib-devel
BuildRequires:	intltool
BuildRequires:	libexif-devel
BuildRequires:	libgee-devel
BuildRequires:	libgsf-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	nautilus-devel
BuildRequires:	pkg-config
BuildRequires:	poppler-glib-devel
BuildRequires:	sqlite3-devel
BuildRequires:	totem-pl-parser-devel
#BuildRequires:	unac-devel
BuildRequires:	upower-devel
BuildRequires:	vala
BuildRequires:	zlib-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gzip
Requires:	hicolor-icon-theme
Requires:	odt2txt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/tracker-%{apiver}

%description
Tracker is an indexing sub-system and search aggregator.

%package libs
Summary:	Tracker libraries
Group:		Libraries

%description libs
Tracker libraries.

%package devel
Summary:	Header files for Tracker libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Tracker development files.

%package apidocs
Summary:	Tracker libraries API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Tracker libraries API documentation.

%package -n evolution-plugin-tracker
Summary:	Tracker plugin for Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	evolution

%description -n evolution-plugin-tracker
Tracker plugin for Evolution.

%package -n nautilus-extension-tracker
Summary:	Tracker extension for Nautilus
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus

%description -n nautilus-extension-tracker
Adds Tracker integration to Nautilus.

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
	--disable-hal				\
	--disable-silent-rules			\
	--disable-tracker-search-bar		\
	--disable-unit-tests			\
	--enable-libvorbis			\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/tracker-%{apiver}/*/*.la

sed -i -e 's|XFCE;|XFCE;OPENBOX;|g' $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/*.desktop

%find_lang %{name}

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

%files -f tracker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker-control
%attr(755,root,root) %{_bindir}/tracker-explorer
%attr(755,root,root) %{_bindir}/tracker-import
%attr(755,root,root) %{_bindir}/tracker-info
%attr(755,root,root) %{_bindir}/tracker-needle
%attr(755,root,root) %{_bindir}/tracker-preferences
%attr(755,root,root) %{_bindir}/tracker-search
%attr(755,root,root) %{_bindir}/tracker-sparql
%attr(755,root,root) %{_bindir}/tracker-stats
%attr(755,root,root) %{_bindir}/tracker-tag

%attr(755,root,root) %{_libexecdir}/tracker-extract
%attr(755,root,root) %{_libexecdir}/tracker-miner-flickr
%attr(755,root,root) %{_libexecdir}/tracker-miner-fs
%attr(755,root,root) %{_libexecdir}/tracker-store
%attr(755,root,root) %{_libexecdir}/tracker-writeback

%dir %{_libdir}/tracker-%{apiver}/extract-modules
%dir %{_libdir}/tracker-%{apiver}/writeback-modules
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-abw.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-epub.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-gif.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-gstreamer.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-html.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-icon.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-jpeg.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-mp3.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-msoffice-xml.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-msoffice.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-oasis.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-pdf.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-playlist.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-png.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-ps.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-text.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-tiff.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-vorbis.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/extract-modules/libextract-xmp.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/writeback-modules/libwriteback-taglib.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/writeback-modules/libwriteback-xmp.so

%{_sysconfdir}/xdg/autostart/tracker-miner-fs.desktop
%{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-flickr.desktop

%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Applications.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.EMails.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Flickr.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service

%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.FTS.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Store.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Writeback.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.enums.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.gschema.xml

%{_datadir}/tracker

%{_desktopdir}/tracker-needle.desktop
%{_desktopdir}/tracker-preferences.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%{_mandir}/man1/tracker-control.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-import.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-miner-fs.1*
%{_mandir}/man1/tracker-needle.1*
%{_mandir}/man1/tracker-preferences.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man1/tracker-writeback.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtracker-extract-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/libtracker-miner-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/libtracker-sparql-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libtracker-extract-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libtracker-miner-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{apiver}.so.*.*.*

%dir %{_libexecdir}
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/libtracker-common.so.*
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/libtracker-data.so.*

%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-extract-%{apiver}.so
%attr(755,root,root) %{_libdir}/libtracker-miner-%{apiver}.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/libtracker-common.so
%attr(755,root,root) %{_libdir}/tracker-%{apiver}/libtracker-data.so

%{_datadir}/gir-1.0/Tracker-%{apiver}.gir
%{_datadir}/gir-1.0/TrackerExtract-%{apiver}.gir
%{_datadir}/gir-1.0/TrackerMiner-%{apiver}.gir

%{_includedir}/tracker-%{apiver}

%{_libdir}/libtracker-extract-%{apiver}.la
%{_libdir}/libtracker-miner-%{apiver}.la
%{_libdir}/libtracker-sparql-%{apiver}.la
%{_libdir}/libtracker-sparql-%{apiver}.so
%{_libdir}/tracker-%{apiver}/libtracker-common.la
%{_libdir}/tracker-%{apiver}/libtracker-data.la

%{_pkgconfigdir}/tracker-extract-%{apiver}.pc
%{_pkgconfigdir}/tracker-miner-%{apiver}.pc
%{_pkgconfigdir}/tracker-sparql-%{apiver}.pc

%{_datadir}/vala/vapi/tracker-miner-%{apiver}.deps
%{_datadir}/vala/vapi/tracker-miner-%{apiver}.vapi
%{_datadir}/vala/vapi/tracker-sparql-%{apiver}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{apiver}.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtracker-extract
%{_gtkdocdir}/libtracker-miner
%{_gtkdocdir}/libtracker-sparql

%files -n evolution-plugin-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/3.4/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/3.4/plugins/org-freedesktop-Tracker-evolution-plugin.eplug

%files -n nautilus-extension-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags.so

