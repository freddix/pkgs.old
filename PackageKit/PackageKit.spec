Summary:	System daemon that is a D-Bus abstraction layer for package management
Name:		PackageKit
Version:	0.7.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.packagekit.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	8031ed03099cda09e1d0df4f3e95e6d3
Patch0:		%{name}-config.patch
Patch1:		%{name}-no-bash.patch
Patch2:		%{name}-smart-fix.patch
URL:		http://www.packagekit.org/
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libarchive-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	poldek-devel
BuildRequires:	polkit-devel
BuildRequires:	python-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel
BuildRequires:	udev-glib-devel
Requires(post,postun):	shared-mime-info
Requires:	%{name}-backend
Requires:	%{name}-libs = %{version}-%{release}
Requires:	crondaemon
Requires:	polkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

%package libs
Summary:	packagekit-glib library
Group:		Libraries

%description libs
packagekit-glib library.

%package devel
Summary:	Header files for packagekit-glib library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for packagekit-glib library.

%package backend-poldek
Summary:	PackageKit Poldek backend
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	poldek
Provides:	%{name}-backend

%description backend-poldek
A backend for PackageKit to enable Poldek functionality.

%package apidocs
Summary:	PackageKit library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
PackageKit library API documentation.

%package gstreamer-plugin
Summary:	GStreamer codecs installer
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gtk-module = %{version}-%{release}

%description gstreamer-plugin
The PackageKit GStreamer plugin allows any GStreamer application to
install codecs from configured repositories using PackageKit.

%package gtk+3-module
Summary:	GTK+ 3.x module to detect and install missing fonts
Group:		X11/Libraries
Requires(post,postun):	glib-gio-gsettings

%description gtk+3-module
The PackageKit GTK+ 3.x module allows any pango application to install
missing fonts from configured repositories using PackageKit.

%package pm-utils
Summary:	PackageKit script for pm-utils
Group:		Applications/System
Requires:	pm-utils

%description pm-utils
PackageKit script for pm-utils.

%package -n python-packagekit
Summary:	PackageKit Python bindings
Group:		Development/Languages/Python
Requires:	python-dbus
Requires:	python-pygobject

%description -n python-packagekit
PackageKit Python bindings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

# no need to force newer Python
sed -i -e "s/2.7/2.6/" configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-browser-plugin	\
	--disable-command-not-found	\
	--disable-dummy			\
	--disable-qt			\
	--disable-silent-rules		\
	--disable-static		\
	--disable-yum			\
	--enable-poldek			\
	--enable-smart			\
	--with-default-backend=poldek	\
	--with-html-dir=%{_gtkdocdir}	\
	--with-security-framework=polkit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# use pk-gstreamer-install as codec installer
ln -s pk-gstreamer-install $RPM_BUILD_ROOT%{_libdir}/gst-install-plugins-helper

install -d $RPM_BUILD_ROOT%{_libdir}/pm-utils/sleep.d
install -p contrib/pm-utils/95packagekit $RPM_BUILD_ROOT%{_libdir}/pm-utils/sleep.d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/modules/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/packagekit-backend/libpk_backend_test_*.so
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/PackageKit/helpers/test_spawn

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/it_IT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%post gtk+3-module
%update_gsettings_cache

%postun gtk+3-module
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO

%dir %{_datadir}/PackageKit
%dir %{_datadir}/PackageKit/helpers
%dir %{_libdir}/packagekit-backend
%dir %{_libdir}/packagekit-plugins
%dir %{_sysconfdir}/PackageKit
%dir %{_sysconfdir}/PackageKit/events
%dir /var/cache/PackageKit
%dir /var/cache/PackageKit/downloads
%dir /var/lib/PackageKit

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/packagekit-background
%attr(750,root,root) /etc/cron.daily/packagekit-background.cron
%attr(755,root,root) %{_bindir}/packagekit-bugreport.sh
%attr(755,root,root) %{_bindir}/pk-debuginfo-install
%attr(755,root,root) %{_bindir}/pkcon
%attr(755,root,root) %{_bindir}/pkgenpack
%attr(755,root,root) %{_bindir}/pkmon
%attr(755,root,root) %{_datadir}/PackageKit/pk-upgrade-distro.sh
%attr(755,root,root) %{_libdir}/packagekitd
%attr(755,root,root) %{_libdir}/packagekit-plugins/*.so
%attr(755,root,root) %{_sbindir}/pk-device-rebind

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/PackageKit/PackageKit.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/PackageKit/Vendor.conf
%ghost /var/lib/PackageKit/transactions.db

%{_datadir}/dbus-1/system-services/org.freedesktop.PackageKit.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/mime/packages/packagekit-catalog.xml
%{_datadir}/mime/packages/packagekit-package-list.xml
%{_datadir}/mime/packages/packagekit-servicepack.xml
%{_datadir}/polkit-1/actions/org.freedesktop.packagekit.policy
%{_mandir}/man1/pk-debuginfo-install.1*
%{_mandir}/man1/pk-device-rebind.1*
%{_mandir}/man1/pkcon.1*
%{_mandir}/man1/pkgenpack.1*
%{_mandir}/man1/pkmon.1*
%{_sysconfdir}/PackageKit/events/post-transaction.d
%{_sysconfdir}/PackageKit/events/pre-transaction.d
/etc/dbus-1/system.d/org.freedesktop.PackageKit.conf

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpackagekit-glib2.so.??
%attr(755,root,root) %{_libdir}/libpackagekit-glib2.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpackagekit-glib2.so
%{_pkgconfigdir}/packagekit-*.pc
%dir %{_includedir}/PackageKit
%{_includedir}/PackageKit/backend
%{_includedir}/PackageKit/packagekit-glib2
%{_includedir}/PackageKit/plugin
%{_datadir}/gir-1.0/*.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/PackageKit

%files backend-poldek
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/packagekit-backend/libpk_backend_poldek.so

%files gstreamer-plugin
%defattr(644,root,root,755)
%doc contrib/gstreamer-plugin/README
%attr(755,root,root) %{_libdir}/gst-install-plugins-helper
%attr(755,root,root) %{_libdir}/pk-gstreamer-install

%files gtk+3-module
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libpk-gtk-module.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/pk-gtk-module.desktop
%{_datadir}/glib-2.0/schemas/*.xml

%files pm-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pm-utils/sleep.d/95packagekit

%files -n python-packagekit
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/packagekit
%{py_sitescriptdir}/packagekit/*.py[co]

