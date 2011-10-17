Summary:	GObject introspection library
Name:		gobject-introspection
Version:	0.10.8
Release:	1
License:	LGPL v2+ (giscanner) and GPL v2+ (tools)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gobject-introspection/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	b5da58a5327d13b4d1e08b8e42b2456d
Patch0:		%{name}-libtool.patch
URL:		http://live.gnome.org/GObjectIntrospection
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	glib-gio-devel
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/girepository-1.0
%define		optcppflags	%{nil}

%description
GObject introspection library.

%package data
Summary:	GObject introspection data
Group:		Development/Libraries
Obsoletes:	gir-repository
Provides:	gir-repository = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description data
This package contains introspection data.

%package devel
Summary:	Header files for gobject-introspection library
Group:		Development/Libraries
Requires:	%{name}-data = %{version}-%{release}

%description devel
Header files for gobject-introspection library.

%package apidocs
Summary:	GI API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GI API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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

rm -f $RPM_BUILD_ROOT%{_libdir}/gobject-introspection/giscanner/*.{la,py}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	data -p /sbin/ldconfig
%postun	data -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/girepository-1.0
%attr(755,root,root) %ghost %{_libdir}/libgirepository-1.0.so.?
%attr(755,root,root) %{_libdir}/libgirepository-1.0.so.*.*.*

%files data
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)

%dir %{_datadir}/gir-1.0
%dir %{_datadir}/gobject-introspection-1.0
%dir %{_libdir}/gobject-introspection
%dir %{_libdir}/gobject-introspection/giscanner

%attr(755,root,root) %{_bindir}/g-ir-annotation-tool
%attr(755,root,root) %{_bindir}/g-ir-compiler
%attr(755,root,root) %{_bindir}/g-ir-generate
%attr(755,root,root) %{_bindir}/g-ir-scanner
%attr(755,root,root) %{_libdir}/lib*.so

%{_datadir}/gir-1.0/*.gir
%{_datadir}/gobject-introspection-1.0/*.c
%{_datadir}/gobject-introspection-1.0/Makefile.introspection
%{_datadir}/gobject-introspection-1.0/tests
%{_includedir}/gobject-introspection-1.0

%{_datadir}/aclocal/introspection.m4
%{_libdir}/libgirepository-*.la
%{_pkgconfigdir}/*.pc

%{_libdir}/gobject-introspection/giscanner/*.py[co]
%attr(755,root,root) %{_libdir}/gobject-introspection/giscanner/*.so

%{_mandir}/man1/g-ir-compiler.1*
%{_mandir}/man1/g-ir-generate.1*
%{_mandir}/man1/g-ir-scanner.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gi

