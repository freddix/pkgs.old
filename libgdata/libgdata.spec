Summary:	GData access library
Name:		libgdata
Version:	0.12.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	ccf0bd3da08a9e86acf704ef71fb73d6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	glib-gio-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgnome-keyring-devel
BuildRequires:	liboauth-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol - most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package devel
Summary:	Support files necessary to compile applications with libgdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers, and support files necessary to compile applications using
libgdata.

%package apidocs
Summary:	libgdata API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgdata API documentation.

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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gdata

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gdata.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %ghost %{_libdir}/libgdata.so.??
%attr(755,root,root) %{_libdir}/libgdata.so.*.*.*
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdata.so
%{_libdir}/libgdata.la
%{_includedir}/libgdata
%{_pkgconfigdir}/libgdata.pc
%{_datadir}/gir-1.0/GData-0.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdata

