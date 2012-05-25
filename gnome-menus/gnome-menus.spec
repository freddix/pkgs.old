Summary:	Implementation of the draft Desktop Menu Specification
Name:		gnome-menus
Version:	3.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-menus/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	fad2a6b9d0dd67f85520161552b51825
Source1:	terminals.menu
Patch0:		%{name}-nokde.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-devel
Obsoletes:	xdg-menus
Provides:	xdg-menus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

%package editor
Summary:	Simple menu editor
Group:		X11/Applications
Requires:	python-pygobject3
Requires:	xdg-menus

%description editor
Simple menu editor.

%package libs
Summary:	gnome-menu library
Group:		Libraries

%description libs
gnome-menu library.

%package devel
Summary:	Header files of gnome-menus library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Headers for gnome-menus library.

%prep
%setup -q
%patch0 -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,dv,en@shaw,gn,ha,ig,io,kg,ps}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/GMenuSimpleEditor/*.py

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/desktop-directories/*
%{_sysconfdir}/xdg/menus/*

%files editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmenu-simple-editor
%{_datadir}/%{name}
%{_desktopdir}/gmenu-simple-editor.desktop
%dir %{py_sitedir}/GMenuSimpleEditor
%{py_sitedir}/GMenuSimpleEditor/*.py[co]

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnome-menu-3.so.?
%attr(755,root,root) %{_libdir}/libgnome-menu-3.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/gnome-menus-3.0
%{_datadir}/gir-1.0/GMenu-3.0.gir

