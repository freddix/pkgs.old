Summary:	SVG Rendering Library
Name:		librsvg
Version:	2.34.2
Release:	4
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/librsvg/2.34/%{name}-%{version}.tar.bz2
# Source0-md5:	4a7eda78019cb89d4e7ae7c841480399
Patch0:		%{name}-parse-path-crash.patch
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	libcroco-devel
BuildRequires:	libgsf-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	popt-devel
BuildRequires:	pkg-config
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An library to render SVG (scalable vector graphics), databased upon libart.

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
%{_includedir}/librsvg-2.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files -n rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files -n gtk+-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.*.*/loaders/libpixbufloader-svg.so
%{_pixmapsdir}/*

