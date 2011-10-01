Summary:	GNOME dialogs for polkit
Name:		polkit-gnome
Version:	0.102
Release:	1
License:	LGPL v2+ (polkit-gnome library), GPL v2+ (D-Bus service)
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	f6b485ffd7bd605af815fd2747180481
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	polkit-devel >= 0.102
Requires(post,preun):	GConf
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/polkit

%description
polkit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%package libs
Summary:	polkit add-on library for GNOME
Group:		X11/Libraries

%description libs
polkit add-on library for GNOME.

%package devel
Summary:	Header files for polkit-gnome library
Group:		X11/Development/Libraries
Requires:	%{name}-gir = %{version}-%{release}

%description devel
Header files for polkit-gnome library.

%package apidocs
Summary:	polkit-gnome library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
polkit-gnome library API documentation.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gobject-introspection-data
Requires:	polkit-gir

%description gir
GObject introspection data for %{name}.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-examples	\
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f polkit-gnome-1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/polkit-gnome-authentication-agent-1

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-gtk-1.so.?
%attr(755,root,root) %{_libdir}/libpolkit-gtk-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-gtk-1.so
%{_libdir}/libpolkit-gtk-1.la
%{_includedir}/polkit-gtk-1
%{_pkgconfigdir}/polkit-gtk-1.pc
%{_datadir}/gir-1.0/PolkitGtk-1.0.gir

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/polkit-gtk-1
%endif

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

