Summary:	D-Bus service for applications to request thumbnails
Name:		tumbler
Version:	0.1.25
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/tumbler/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	d4edc15c172714c7a3eaf3c719b8faf6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	ffmpegthumbnailer-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gstreamer-devel
BuildRequires:	intltool
BuildRequires:	libgsf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	poppler-glib-devel
BuildRequires:	xfce4-dev-tools >= 4.7.3
Obsoletes:	xdg-thumbnail-manager
Provides:	xdg-thumbnail-manager
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/tumbler-1

%description

%package libs
Summary:	Tumbler library
Group:		Libraries

%description libs
Tumbler library.

%package devel
Summary:	Header files for Tumbler library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Tumbler library.

%package apidocs
Summary:	Tumbler API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Tumbler API documentation.

%prep
%setup -q

%build
mkdir m4
%{__gtkdocize}
%{__intltoolize}
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

rm -f $RPM_BUILD_ROOT%{_libdir}/tumbler-1/plugins/{cache/,}*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libexecdir}
%dir %{_libdir}/tumbler-1/plugins
%dir %{_libdir}/tumbler-1/plugins/cache
%attr(755,root,root) %{_libexecdir}/tumblerd
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/*.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/cache/*.so
%{_datadir}/dbus-1/services/org.xfce.Tumbler.Cache1.service
%{_datadir}/dbus-1/services/org.xfce.Tumbler.Manager1.service
%{_datadir}/dbus-1/services/org.xfce.Tumbler.Thumbnailer1.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtumbler-1.so.?
%attr(755,root,root) %{_libdir}/libtumbler-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtumbler-1.so
%{_includedir}/tumbler-1
%{_pkgconfigdir}/tumbler-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/tumbler

