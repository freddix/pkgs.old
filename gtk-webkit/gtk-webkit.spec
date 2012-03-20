Summary:	Port of WebKit embeddable web component to GTK+
Name:		gtk-webkit
Version:	1.6.3
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/webkit-%{version}.tar.xz
# Source0-md5:	c476d9335419df061510d31e21175df1
URL:		http://www.webkitgtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	enchant-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gperf
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libsoup-devel >= 2.36.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-libXft-devel
Requires(post,postun):  glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webkit is a port of the WebKit embeddable web component to GTK+.

%package devel
Summary:	Development files for webkit
Group:		X11/Development/Libraries
Requires:	%{name}-gir = %{version}-%{release}

%description devel
Development files for webkit.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gobject-introspection-data

%description gir
GObject introspection data for WebKit GTK+.

%package demo
Summary:	Demo GTK+/webkit application
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description demo
Simple GTK+/webkit based browser.

%prep
%setup -qn webkit-%{version}

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I Source/autotools
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-geolocation=no	\
	--enable-introspection	\
	--enable-spellcheck	\
	--with-gtk=2.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang webkit-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_gsettings_cache

%postun
/sbin/ldconfig
%update_gsettings_cache

%files -f webkit-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-*.so.?
%attr(755,root,root) %ghost %{_libdir}/libwebkitgtk-*.so.?
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebkitgtk-*.so.*.*.*

%{_datadir}/webkitgtk-*
%{_datadir}/glib-2.0/schemas/org.webkitgtk-1.0.gschema.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsc-1
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/webkit-*
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

