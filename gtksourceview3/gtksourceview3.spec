Summary:	Text widget that extends the standard GTK+ 3.x
Name:		gtksourceview3
Version:	3.4.1
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/3.4/gtksourceview-%{version}.tar.xz
# Source0-md5:	637a8a5b909cfd7e77ca0e414a225e24
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceView is a text widget that extends the standard GTK+ 3.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

%package devel
Summary:	Header files for GtkSourceView
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GtkSourceView.

%package apidocs
Summary:	GtkSourceView API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GtkSourceView API documentation.

%prep
%setup -qn gtksourceview-%{version}

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
	--disable-silent-rules	\
	--enable-providers	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gtksourceview-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtksourceview-3.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgtksourceview-3.0.so.?
%attr(755,root,root) %{_libdir}/libgtksourceview-3.0.so.*.*.*
%{_datadir}/gtksourceview-3.0
%{_libdir}/girepository-1.0/GtkSource-3.0.typelib

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtksourceview-3.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-3.0.so
%{_includedir}/gtksourceview-3.0
%{_pkgconfigdir}/gtksourceview-3.0.pc
%{_datadir}/gir-1.0/GtkSource-3.0.gir

