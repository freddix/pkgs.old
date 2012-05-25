Summary:	A social network data aggregator
Name:		libsocialweb
Version:	0.25.20
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsocialweb/0.25/%{name}-%{version}.tar.xz
# Source0-md5:	10332cd8674c39402e0834064e2b5437
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	rest-devel
BuildRequires:	vala-vapigen
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
libsocialweb is a social data server which fetches data from the
"social web", such as your friend's blog posts and photos, upcoming
events, recently played tracks, and pending eBay auctions. It also
provides a service to update your status on web services which support
it, such as MySpace and Twitter.

%package libs
Summary:	Socialweb libraries
Group:		Libraries

%description libs
Socialweb library.

%package devel
Summary:	Header files for socialweb library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for socialweb library.

%package apidocs
Summary:	socialweb library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for socialweb library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-all-services	\
	--enable-vala-bindings	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsocialweb/services/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_libdir}/libsocialweb
%dir %{_libdir}/libsocialweb/services
%attr(755,root,root) %{_libexecdir}/libsocialweb-core
%attr(755,root,root) %{_libdir}/libsocialweb/services/libfacebook.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libflickr.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/liblastfm.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libmyspace.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libphotobucket.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libplurk.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libsina.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libsmugmug.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libtwitter.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libvimeo.so
%attr(755,root,root) %{_libdir}/libsocialweb/services/libyoutube.so
%{_datadir}/dbus-1/services/libsocialweb.service
%{_datadir}/libsocialweb

%files libs
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib
%attr(755,root,root) %ghost %{_libdir}/libsocialweb-client.so.?
%attr(755,root,root) %ghost %{_libdir}/libsocialweb-keyfob.so.?
%attr(755,root,root) %ghost %{_libdir}/libsocialweb-keystore.so.?
%attr(755,root,root) %ghost %{_libdir}/libsocialweb.so.?
%attr(755,root,root) %{_libdir}/libsocialweb-client.so.*.*.*
%attr(755,root,root) %{_libdir}/libsocialweb-keyfob.so.*.*.*
%attr(755,root,root) %{_libdir}/libsocialweb-keystore.so.*.*.*
%attr(755,root,root) %{_libdir}/libsocialweb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsocialweb-client.so
%attr(755,root,root) %{_libdir}/libsocialweb-keyfob.so
%attr(755,root,root) %{_libdir}/libsocialweb-keystore.so
%attr(755,root,root) %{_libdir}/libsocialweb.so
%{_datadir}/gir-1.0/SocialWebClient-0.25.gir
%{_datadir}/vala/vapi/libsocialweb-client.deps
%{_datadir}/vala/vapi/libsocialweb-client.vapi
%{_includedir}/libsocialweb
%{_pkgconfigdir}/libsocialweb-client.pc
%{_pkgconfigdir}/libsocialweb-keyfob.pc
%{_pkgconfigdir}/libsocialweb-keystore.pc
%{_pkgconfigdir}/libsocialweb-module.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsocialweb-client
%{_gtkdocdir}/libsocialweb-dbus
%{_gtkdocdir}/libsocialweb

