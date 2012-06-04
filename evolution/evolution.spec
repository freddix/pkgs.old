%define		basever	3.4

Summary:	The GNOME Email/Calendar/Addressbook Suite
Name:		evolution
Version:	%{basever}.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	e161138610416bfff07e6e0a1d9e4781
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-bug655753.patch
Patch2:		%{name}-bug655753_2.patch
URL:		http://www.ximian.com/products/ximian_evolution/
BuildRequires:	GConf-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.20.10
BuildRequires:	gstreamer-devel
BuildRequires:	gtk-doc
BuildRequires:	gtkhtml-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mx-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	openldap-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	which
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	rarian
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will be tightly
integrated with one another and act as a seamless personal
information-management tool.

%package libs
Summary:	Evolution libraries
Group:		Development/Libraries

%description libs
This package contains Evolution libraries.

%package devel
Summary:	Header files for evolution
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications
using Evolution's libraries.

%package apidocs
Summary:	EShell API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Eshell API documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-pst-import				\
	--disable-schemas-install			\
	--disable-schemas-compile			\
	--disable-scrollkeeper				\
	--disable-silent-rules				\
	--disable-static				\
	--enable-canberra				\
	--enable-nm=no					\
	--enable-nss=yes				\
	--enable-smime=yes				\
	--enable-weather				\
	--with-html-dir=%{_gtkdocdir}			\
	--with-kde-applnk-path=no 			\
	--with-nspr-includes="%{_includedir}/nspr" 	\
	--with-nspr-libs="%{_libdir}"			\
	--with-nss-includes="%{_includedir}/nss"	\
	--with-nss-libs="%{_libdir}"			\
	--with-openldap					\
	--with-sub-version=" Freddix"			\
	--without-static-ldap

# rebuild *.c and *.h from *.idl
find -name \*.idl -exec touch {} \;

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,48x48}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/*/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/gconf

%find_lang %{name} --all-name --with-omf --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor
%update_desktop_database_post
%update_gsettings_cache

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f evolution.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* README

%dir %{_datadir}/evolution
%dir %{_datadir}/evolution/%{basever}
%dir %{_datadir}/evolution/%{basever}/default
%dir %{_datadir}/evolution/%{basever}/default/C
%dir %{_datadir}/evolution/%{basever}/etspec
%dir %{_datadir}/evolution/%{basever}/views

%attr(755,root,root) %{_bindir}/evolution

%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-addressbook.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-bogofilter.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-calendar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-composer-autosave.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-mail.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-mailto-handler.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-mdn.so
#%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-network-manager.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-offline-alert.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-online-accounts.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-plugin-lib.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-plugin-manager.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-spamassassin.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/modules/libevolution-module-startup-wizard.so

%attr(755,root,root) %{_libdir}/evolution/%{basever}/csv2vcard
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-addressbook-export
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-alarm-notify
%attr(755,root,root) %{_libdir}/evolution/%{basever}/evolution-backup
%attr(755,root,root) %{_libdir}/evolution/%{basever}/killev

%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-addressbook-file.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-audio-inline.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-backup-restore.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-calendar-file.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-calendar-http.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-calendar-weather.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-dbx-import.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-default-source.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-email-custom-header.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-evolution-attachment-reminder.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-evolution-bbdb.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-evolution-caldav.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-evolution-google.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-evolution-webdav.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-face.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-imap-features.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-itip-formatter.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-mail-notification.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-mail-to-task.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-mailing-list-actions.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-mark-all-read.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-prefer-plain.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-publish-calendar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-save-calendar.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-templates.so
%attr(755,root,root) %{_libdir}/evolution/%{basever}/plugins/liborg-gnome-vcard-inline.so

%{_libdir}/evolution/%{basever}/plugins/*.eplug

%{_datadir}/evolution/%{basever}/*.xml
%{_datadir}/evolution/%{basever}/address_formats.dat
%{_datadir}/evolution/%{basever}/countrytransl.map
%{_datadir}/evolution/%{basever}/default/C/mail
%{_datadir}/evolution/%{basever}/ecps
%{_datadir}/evolution/%{basever}/errors
%{_datadir}/evolution/%{basever}/etspec/*addressbook*
%{_datadir}/evolution/%{basever}/etspec/*cal-list*
%{_datadir}/evolution/%{basever}/etspec/*calendar*
%{_datadir}/evolution/%{basever}/etspec/*meeting*
%{_datadir}/evolution/%{basever}/etspec/*memo*
%{_datadir}/evolution/%{basever}/etspec/*message-list*
%{_datadir}/evolution/%{basever}/help
%{_datadir}/evolution/%{basever}/icons
%{_datadir}/evolution/%{basever}/images
%{_datadir}/evolution/%{basever}/mail-autoconfig
%{_datadir}/evolution/%{basever}/sounds
%{_datadir}/evolution/%{basever}/theme
%{_datadir}/evolution/%{basever}/ui
%{_datadir}/evolution/%{basever}/views/addressbook
%{_datadir}/evolution/%{basever}/views/calendar
%{_datadir}/evolution/%{basever}/views/mail
%{_datadir}/evolution/%{basever}/views/memos
%{_datadir}/evolution/%{basever}/views/tasks

%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.*
%{_sysconfdir}/xdg/autostart/evolution-alarm-notify.desktop

%{_datadir}/GConf/gsettings/evolution.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.itip.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.mail-notification.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml

%lang(ca) %dir %{_datadir}/evolution/%{basever}/default/ca
%lang(ca) %{_datadir}/evolution/%{basever}/default/ca/mail
%lang(cs) %dir %{_datadir}/evolution/%{basever}/default/cs
%lang(cs) %{_datadir}/evolution/%{basever}/default/cs/mail
%lang(de) %dir %{_datadir}/evolution/%{basever}/default/de
%lang(de) %{_datadir}/evolution/%{basever}/default/de/mail
%lang(es) %dir %{_datadir}/evolution/%{basever}/default/es
%lang(es) %{_datadir}/evolution/%{basever}/default/es/mail
%lang(fi) %dir %{_datadir}/evolution/%{basever}/default/fi
%lang(fi) %{_datadir}/evolution/%{basever}/default/fi/mail
%lang(fr) %dir %{_datadir}/evolution/%{basever}/default/fr
%lang(fr) %{_datadir}/evolution/%{basever}/default/fr/mail
%lang(hu) %dir %{_datadir}/evolution/%{basever}/default/hu
%lang(hu) %{_datadir}/evolution/%{basever}/default/hu/mail
%lang(id) %dir %{_datadir}/evolution/%{basever}/default/id
%lang(id) %{_datadir}/evolution/%{basever}/default/id/mail
%lang(it) %dir %{_datadir}/evolution/%{basever}/default/it
%lang(it) %{_datadir}/evolution/%{basever}/default/it/mail
%lang(ja) %dir %{_datadir}/evolution/%{basever}/default/ja
%lang(ja) %{_datadir}/evolution/%{basever}/default/ja/mail
%lang(ko) %dir %{_datadir}/evolution/%{basever}/default/ko
%lang(ko) %{_datadir}/evolution/%{basever}/default/ko/mail
%lang(lt) %dir %{_datadir}/evolution/%{basever}/default/lt
%lang(lt) %{_datadir}/evolution/%{basever}/default/lt/mail
%lang(mk) %dir %{_datadir}/evolution/%{basever}/default/mk
%lang(mk) %{_datadir}/evolution/%{basever}/default/mk/mail
%lang(nl) %dir %{_datadir}/evolution/%{basever}/default/nl
%lang(nl) %{_datadir}/evolution/%{basever}/default/nl/mail
%lang(pl) %dir %{_datadir}/evolution/%{basever}/default/pl
%lang(pl) %{_datadir}/evolution/%{basever}/default/pl/mail
%lang(pt) %dir %{_datadir}/evolution/%{basever}/default/pt
%lang(pt) %{_datadir}/evolution/%{basever}/default/pt/mail
%lang(ro) %dir %{_datadir}/evolution/%{basever}/default/ro
%lang(ro) %{_datadir}/evolution/%{basever}/default/ro/mail
%lang(sr) %dir %{_datadir}/evolution/%{basever}/default/sr
%lang(sr) %{_datadir}/evolution/%{basever}/default/sr/mail
%lang(sr@latin) %dir %{_datadir}/evolution/%{basever}/default/sr@latin
%lang(sr@latin) %{_datadir}/evolution/%{basever}/default/sr@latin/mail
%lang(sv) %dir %{_datadir}/evolution/%{basever}/default/sv
%lang(sv) %{_datadir}/evolution/%{basever}/default/sv/mail
%lang(zh_CN) %dir %{_datadir}/evolution/%{basever}/default/zh_CN
%lang(zh_CN) %{_datadir}/evolution/%{basever}/default/zh_CN/mail

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/evolution
%dir %{_libdir}/evolution/%{basever}
%dir %{_libdir}/evolution/%{basever}/modules
%dir %{_libdir}/evolution/%{basever}/plugins
%attr(755,root,root) %{_libdir}/evolution/%{basever}/lib*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/%{basever}/lib*.so
%{_libdir}/evolution/%{basever}/*.la
%{_includedir}/%{name}-%{basever}
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/eshell

