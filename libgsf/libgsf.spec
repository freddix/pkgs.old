Summary:	GNOME Structured File library
Name:		libgsf
Version:	1.14.23
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgsf/1.14/%{name}-%{version}.tar.xz
# Source0-md5:	3e71b5af1999e62495c6750e51dbbe02
Patch0:		%{name}-no_gconf_macros.patch
URL:		http://www.gnumeric.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	gobject-introspection-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for reading and writing structured files (e.g. MS OLE and
Zip).

%package utils
Summary:	libgsf utilities
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description utils
GSF utilities.

%package devel
Summary:	Support files necessary to compile applications with libgsf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	zlib-devel

%description devel
Headers, and support files necessary to compile applications using
libgsf.

%package apidocs
Summary:	libgsf API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgsf API documentation.

%package thumbnailer
Summary:	Simple document thumbnailer
Group:		Applications

%description thumbnailer
Simple document thumbnailer.

%prep
%setup -q

%build
rm -f acinclude.m4
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gsf/*.la
rm -rf $RPM_BUILD_ROOT%{_includedir}/%{name}-1/gsf-win32

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %ghost %{_libdir}/libgsf-?.so.???
%attr(755,root,root) %{_libdir}/libgsf-?.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf
%attr(755,root,root) %{_bindir}/gsf-vba-dump
%{_mandir}/man1/gsf.1*
%{_mandir}/man1/gsf-vba-dump.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-?.so
%{_datadir}/gir-1.0/*.gir
%{_includedir}/libgsf-1
%{_pkgconfigdir}/libgsf-?.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files thumbnailer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf-office-thumbnailer
%{_datadir}/thumbnailers/gsf-office.thumbnailer
%{_mandir}/man1/gsf-office-thumbnailer.1*

