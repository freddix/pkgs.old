%define		basever	3.4

Summary:	WebKit-based GNOME web browser
Name:		epiphany
Version:	%{basever}.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany/%{basever}/%{name}-%{version}.tar.xz
# Source0-md5:	dc0bf1dc42eb1dc3f0e80d50174315df
Patch0:		1.patch
Patch1:		2.patch
Patch2:		3.patch
Patch3:		4.patch
Patch4:		5.patch
Patch5:		6.patch
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-glib-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	enchant-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk3-webkit-devel
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	rarian
Requires:	dbus
Requires:	gsettings-desktop-schemas
Requires:	iso-codes
Requires:	xdg-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME web browser based on WebKit.

# doesn't require base
%package devel
Summary:	Epiphany header files
Group:		X11/Applications/Networking

%description devel
Epiphany header files for plugin development.

%package apidocs
Summary:	Epiphany API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Epiphany API documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

echo 'NoDisplay=true' >> data/bme.desktop.in.in

%build
%{__gnome_doc_prepare}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-compile	\
	--disable-seed			\
	--disable-silent-rules		\
	--enable-introspection		\
	--enable-zeroconf		\
	--with-distributor-name=Freddix	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/%{basever}/extensions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,tk,ps}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post
%update_gsettings_cache

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{basever}
%dir %{_libdir}/%{name}/%{basever}/extensions

%attr(755,root,root) %{_bindir}/ephy-profile-migrator
%attr(755,root,root) %{_bindir}/epiphany

%{_datadir}/%{name}

%{_datadir}/GConf/gsettings/epiphany.convert
%{_datadir}/dbus-1/services/org.gnome.Epiphany.service
%{_datadir}/glib-2.0/schemas/org.gnome.Epiphany.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.epiphany.gschema.xml

%{_desktopdir}/epiphany.desktop
%{_mandir}/man1/epiphany.1*

%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%{_aclocaldir}/*.m4
%{_includedir}/epiphany
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/Epiphany-*.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/epiphany

