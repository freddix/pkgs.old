Summary:	Port of WebKit embeddable web component to GTK+
Name:		gtk3-webkit
Version:	1.8.1
Release:	2
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/releases/webkit-%{version}.tar.xz
# Source0-md5:	f2f01b1fdc7262a2eede81ebed0970b2
URL:		http://www.webkitgtk.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	enchant-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	geoclue-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gperf
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libsoup-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webkit is a port of the WebKit embeddable web component to GTK+.

%package devel
Summary:	Development files for webkit
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for webkit.

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
	--enable-geolocation	\
	--enable-introspection	\
	--enable-spellcheck	\
	--with-gtk=3.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang webkit-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f webkit-3.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-*.so.?
%attr(755,root,root) %ghost %{_libdir}/libwebkitgtk-*.so.?
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebkitgtk-*.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%dir %{_datadir}/webkitgtk-3.0
%{_datadir}/webkitgtk-3.0/images
%{_datadir}/webkitgtk-3.0/resources
%{_datadir}/webkitgtk-3.0/webinspector

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsc-3
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/webkitgtk-3.0
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir

