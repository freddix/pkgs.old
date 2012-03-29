Summary:	Nautilus is a file manager for the GNOME desktop environment
Name:		nautilus
Version:	2.32.2.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	f75f387d1b439079967581d876009426
Source1:	%{name}-mount-archive.desktop
URL:		http://nautilus.eazel.com/
Patch0:		%{name}-freddix.patch
Patch1:		%{name}-deprecated.patch
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	exempi-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libexif-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
Requires(post,preun):	GConf
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	gtk+-rsvg
Requires:	gvfs
Requires:	xdg-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%package libs
Summary:	Nautilus libraries
Group:		X11/Libraries

%description libs
Nautilus libraries.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%package apidocs
Summary:	libnautilus-extension API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnautilus-extension API documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--disable-update-mimedb	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,crh,ha,ig,io,ps}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%gconf_schema_install apps_nautilus_preferences.schemas
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_nautilus_preferences.schemas

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS
%attr(755,root,root) %{_bindir}/nautilus
%attr(755,root,root) %{_bindir}/nautilus-autorun-software
%attr(755,root,root) %{_bindir}/nautilus-connect-server
%attr(755,root,root) %{_bindir}/nautilus-file-management-properties
%attr(755,root,root) %{_libexecdir}/nautilus-convert-metadata

%dir %{_libdir}/nautilus/extensions-2.0

%{_datadir}/mime/packages/*.xml
%{_datadir}/nautilus

%{_desktopdir}/*
%{_pixmapsdir}/nautilus
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/apps_nautilus_preferences.schemas

%{_mandir}/man1/nautilus*.1*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/nautilus
%attr(755,root,root) %ghost %{_libdir}/libnautilus-extension.so.?
%attr(755,root,root) %{_libdir}/libnautilus-extension.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so
%{_libdir}/libnautilus-extension.la
%{_includedir}/%{name}
%{_pkgconfigdir}/libnautilus-extension.pc
%{_datadir}/gir-1.0/Nautilus-2.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnautilus-extension

