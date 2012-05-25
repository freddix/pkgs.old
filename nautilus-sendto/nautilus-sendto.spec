Summary:	Nautilus context menu for sending files
Name:		nautilus-sendto
Version:	3.0.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-sendto/3.0/%{name}-%{version}.tar.xz
# Source0-md5:	cfd7e91cdd27adaed50bf7050229c8bc
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	gupnp-devel
BuildRequires:	intltool
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	nautilus-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires:	file-roller
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugins	evolution nautilus-burn removable-devices upnp

%description
nautilus-sendto provides a Nautilus context menu for sending
files via other desktop applications.

%package devel
Summary:	nautilus-sendto development files
Group:		Development

%description devel
nautilus-sendto development files.

%package apidocs
Summary:	%{name} API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
%{name} API documentation.

%package burn
Summary:	nautilus-sendto burner plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	brasero

%description burn
A nautilus-sendto plugin for sending files to Nautilus CD Burner.

%package evolution
Summary:	nautilus-sendto Evolution plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	evolution

%description evolution
A nautilus-sendto plugin for sending files via Evolution.

%package upnp
Summary:	nautilus-sendto upnp plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description upnp
A nautilus-sendto plugin for sending files via Pidgin.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g'		\
    configure.in

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--with-html-dir=%{_gtkdocdir}	\
	--with-plugins="%{plugins}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{nautilus/extensions-3.0,nautilus-sendto/plugins}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ug}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins

%attr(755,root,root) %{_bindir}/*
%{_libdir}/nautilus-sendto/plugins/libnstremovable_devices.so

%{_datadir}/GConf/gsettings/nautilus-sendto-convert
%{_datadir}/glib-2.0/schemas/org.gnome.Nautilus.Sendto.gschema.xml
%{_datadir}/%{name}

%{_mandir}/man1/%{name}.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/nautilus-sendto
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files burn
%defattr(644,root,root,755)
%{_libdir}/nautilus-sendto/plugins/libnstburn.so

%files evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstevolution.so

%files upnp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstupnp.so

