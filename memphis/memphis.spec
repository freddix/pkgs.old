Summary:	Map renderer for OpenStreetMap data
Name:		memphis
Version:	0.2.3
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	http://wenner.ch/files/public/mirror/memphis/%{name}-%{version}.tar.gz
# Source0-md5:	dbed61f37d07801c1f660c0b5a5d81bc
URL:		http://trac.openstreetmap.ch/trac/memphis/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memphis is a map-rendering library for OpenStreetMap data.

%package devel
Summary:	Header files for libmemphis library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmemphis library.

%package apidocs
Summary:	libmemphis library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmemphis library API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libmemphis-0.2.so.?
%attr(755,root,root) %{_libdir}/libmemphis-0.2.so.*.*.*
%{_libdir}/girepository-1.0/Memphis-0.2.typelib
%{_datadir}/memphis

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmemphis-0.2.so
%{_includedir}/libmemphis-0.2
%{_pkgconfigdir}/memphis-0.2.pc
%{_datadir}/gir-1.0/Memphis-0.2.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmemphis

