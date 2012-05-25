Summary:	Totem Playlist Parser library
Name:		totem-pl-parser
Version:	3.4.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem-pl-parser/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	0b0d5b16dd0849b873e2f9b97f4f978b
URL:		http://www.gnome.org/projects/totem/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	gmime-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to parse and save playlists, as used in music and movie
players.

%package devel
Summary:	Header files for totem-pl-parser library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for totem-pl-parser library.

%package apidocs
Summary:	totem-pl-parser library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
totem-pl-parser library API documentation.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.in

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-gtk-doc	\
	--enable-introspection	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libtotem*.so.??
%attr(755,root,root) %{_libdir}/libtotem*.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-*.so
%{_libdir}/libtotem*.la
%{_includedir}/totem-pl-parser
%{_pkgconfigdir}/totem*.pc
%{_datadir}/gir-1.0/TotemPlParser-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/totem-pl-parser

