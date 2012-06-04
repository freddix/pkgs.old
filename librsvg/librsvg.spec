Summary:	SVG Rendering Library
Name:		librsvg
Version:	2.36.1
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/librsvg/2.36/%{name}-%{version}.tar.xz
# Source0-md5:	89d483f30a7c77245b7ee02faaea5a5a
Patch0:		%{name}-parse-path-crash.patch
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	libcroco-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	popt-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to render SVG files using cairo.

%package devel
Summary:	Include files for developing with librsvg
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%package apidocs
Summary:	librsvg API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
librsvg API documentation.

%package -n rsvg
Summary:	Converting tool
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n rsvg
Turns SVG files into raster images.

%package -n gtk+-rsvg
Summary:	Gtk+ rsvg pixbuffer loader
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires(post,postun):	gdk-pixbuf

%description -n gtk+-rsvg
Gtk+ rsvg pixbuffer loader.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-gtk-theme		\
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/loaders/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n gtk+-rsvg
umask 022
%{_bindir}/gdk-pixbuf-query-loaders --update-cache || :

%postun -n gtk+-rsvg
umask 022
%{_bindir}/gdk-pixbuf-query-loaders --update-cache || :

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%{_pkgconfigdir}/*.pc
%{_includedir}/librsvg-2.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files -n rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1*

%files -n gtk+-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.*.*/loaders/libpixbufloader-svg.so

