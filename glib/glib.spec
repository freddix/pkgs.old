Summary:	Cross-platform software utility library
Name:		glib
Version:	2.30.0
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://download.gnome.org/sources/glib/2.30/%{name}-%{version}.tar.xz
# Source0-md5:	68ac9516233044f27e76577d4f4e6de9
Patch0:		%{name}-makefile.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pcre-devel >= 8.11
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	zlib-devel
Requires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%package devel
Summary:	Glib development files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%package static
Summary:	Glib static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Glib static library.

%package apidocs
Summary:	Glib API documetation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Glib API documetation.

%package gdbus
Summary:	Introspect and call remote objects
Group:		Applications
Requires:	%{name}-gio = %{epoch}:%{version}-%{release}

%description gdbus
gdbus offers a simple commandline utility for introspecting
and calling methods on remote objects.

%package gio
Summary:	Glib GIO library
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gio
Glib GIO library.


%package gio-gsettings
Summary:	GSettings configuration tool
Group:		Applications
Requires:	%{name}-gdbus = %{epoch}:%{version}-%{release}

%description gio-gsettings
gsettings offers a simple commandline interface to GSettings. It lets
you get, set or monitor an individual key for changes.

%package gio-devel
Summary:	Glib GIO development files
Group:		Development/Libraries
Requires:	%{name}-gio = %{epoch}:%{version}-%{release}

%description gio-devel
Glib GIO development files.

%package gio-static
Summary:	Glib GIO static library
Group:		Development/Libraries
Requires:	%{name}-gio-devel = %{epoch}:%{version}-%{release}

%description gio-static
Glib GIO static library.

%package gio-apidocs
Summary:	Glib GIO API documetation
Group:		Documentation
Requires:	gtk-doc-common

%description gio-apidocs
Glib GIO API documetation.

%prep
%setup -q
%patch0 -p1

sed -i -e 's|])dnl|])|g' acglib.m4

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4macros -I glib/libcharset
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-fam			\
	--disable-silent-rules		\
	--enable-man			\
	--enable-static			\
	--with-html-dir=%{_gtkdocdir}	\
	--with-pcre=system
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install			\
	DESTDIR=$RPM_BUILD_ROOT		\
	m4datadir=%{_aclocaldir}	\
	pkgconfigdir=%{_pkgconfigdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,be@latin,en@shaw}
%{?with_fam:rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la}

%find_lang glib20 --with-gnome

> $RPM_BUILD_ROOT%{_libdir}/gio/modules/giomodule.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gio
/sbin/ldconfig
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules ||:

%postun	gio -p /sbin/ldconfig

%files -f glib20.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%attr(755,root,root) %ghost %{_libdir}/libglib-2.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libgmodule-2.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libgobject-2.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libgthread-2.0.so.?
%attr(755,root,root) %{_libdir}/libglib-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgmodule-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgobject-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgthread-2.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gdbus-codegen
%attr(755,root,root) %{_bindir}/glib-genmarshal
%attr(755,root,root) %{_bindir}/glib-gettextize
%attr(755,root,root) %{_bindir}/glib-mkenums
%attr(755,root,root) %{_bindir}/gobject-query
%attr(755,root,root) %{_bindir}/gtester
%attr(755,root,root) %{_bindir}/gtester-report

%attr(755,root,root) %{_libdir}/libglib-2.0.so
%attr(755,root,root) %{_libdir}/libgmodule-2.0.so
%attr(755,root,root) %{_libdir}/libgobject-2.0.so
%attr(755,root,root) %{_libdir}/libgthread-2.0.so
%{_libdir}/libglib-2.0.la
%{_libdir}/libgmodule-2.0.la
%{_libdir}/libgobject-2.0.la
%{_libdir}/libgthread-2.0.la

%dir %{_libdir}/gdbus-2.0
%dir %{_libdir}/gdbus-2.0/codegen
%{_libdir}/gdbus-2.0/codegen/*.py[co]
%{_mandir}/man1/gdbus-codegen.1*

%{_libdir}/glib-2.0
%dir %{_datadir}/glib-2.0/gettext
%attr(755,root,root) %{_datadir}/glib-2.0/gettext/mkinstalldirs
%{_datadir}/glib-2.0/gdb
%{_datadir}/glib-2.0/gettext/po
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_pkgconfigdir}/glib-2.0.pc
%{_pkgconfigdir}/gmodule-2.0.pc
%{_pkgconfigdir}/gmodule-export-2.0.pc
%{_pkgconfigdir}/gmodule-no-export-2.0.pc
%{_pkgconfigdir}/gobject-2.0.pc
%{_pkgconfigdir}/gthread-2.0.pc

%{_includedir}/*
%{_aclocaldir}/*

%{_mandir}/man1/gio-querymodules.1*
%{_mandir}/man1/glib-genmarshal.1*
%{_mandir}/man1/glib-gettextize.1*
%{_mandir}/man1/glib-mkenums.1*
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libglib-2.0.a
%{_libdir}/libgmodule-2.0.a
%{_libdir}/libgobject-2.0.a
%{_libdir}/libgthread-2.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/glib
%{_gtkdocdir}/gobject
%{_gtkdocdir}/gdbus-object-manager-example

%files gdbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdbus
%{_mandir}/man1/gdbus.1*

%files gio
%defattr(644,root,root,755)
%dir %{_libdir}/gio
%dir %{_libdir}/gio/modules
%ghost %{_libdir}/gio/modules/giomodule.cache
%attr(755,root,root) %{_bindir}/gio-querymodules
%attr(755,root,root) %ghost %{_libdir}/libgio-2.0.so.0
%attr(755,root,root) %{_libdir}/libgio-2.0.so.*.*.*

%files gio-gsettings
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glib-compile-schemas
%attr(755,root,root) %{_bindir}/gsettings
%{_mandir}/man1/glib-compile-schemas.1*
%{_mandir}/man1/gsettings.1*

%files gio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgio-2.0.so
%{_libdir}/libgio-2.0.la
%{_pkgconfigdir}/gio-2.0.pc
%{_pkgconfigdir}/gio-unix-2.0.pc

%files gio-static
%defattr(644,root,root,755)
%{_libdir}/libgio-2.0.a

%files gio-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gio

