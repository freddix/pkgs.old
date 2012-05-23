%define		abiver		2.10.0

Summary:	An image loading and scaling library
Name:		gdk-pixbuf
Version:	2.26.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/2.26/%{name}-%{version}.tar.xz
# Source0-md5:	82197921c651a81ae28178aa9adfc0e6
URL:		http://www.gtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	perl-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
Requires:	gtk+-rsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdk-pixbuf is an image loading and scaling library that can be
extended by loadable modules for new image formats.

%package devel
Summary:	Header files for gdk-pixbuf library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gdk-pixbuf library.

%package apidocs
Summary:	gdk-pixbuf API documentation
Group:		Documentation

%description apidocs
API documentation for gdk-pixbuf library.

%prep
%setup -qn gdk-pixbuf-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules		\
	--enable-man			\
	--with-html-dir=%{_gtkdocdir}	\
	--with-included-loaders=png	\
	--with-libjasper		\
	--with-x11
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/%{abiver}/loaders.cache
rm -f $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/%{abiver}/loaders/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/io

%find_lang gdk-pixbuf %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/gdk-pixbuf-query-loaders --update-cache || :

%postun
/sbin/ldconfig
if [ "$1" != "0" ]; then
	umask 022
	%{_bindir}/gdk-pixbuf-query-loaders --update-cache || :
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %ghost %{_libdir}/libgdk_pixbuf*.so.?
%attr(755,root,root) %{_libdir}/libgdk_pixbuf-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/%{abiver}
%dir %{_libdir}/gdk-pixbuf-2.0/%{abiver}/loaders

%attr(755,root,root) %{_bindir}/gdk-pixbuf-query-loaders
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/%{abiver}/loaders/libpixbufloader-*.so
%ghost %{_libdir}/gdk-pixbuf-2.0/%{abiver}/loaders.cache
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdk-pixbuf-csource
%attr(755,root,root) %{_bindir}/gdk-pixbuf-pixdata
%attr(755,root,root) %{_libdir}/libgdk_pixbuf*.so
%{_libdir}/libgdk_pixbuf*.la
%{_datadir}/gir-1.0/GdkPixbuf-2.0.gir
%{_includedir}/gdk-pixbuf-2.0
%{_mandir}/man1/gdk-pixbuf-csource.1*
%{_pkgconfigdir}/gdk-pixbuf-2.0.pc
%{_pkgconfigdir}/gdk-pixbuf-xlib-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdk-pixbuf

