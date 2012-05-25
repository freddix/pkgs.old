Summary:	GObject contact aggregation library
Name:		folks
Version:	0.6.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/folks/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	49b739a9359a9b030844a2719cf5bb45
URL:		http://telepathy.freedesktop.org/wiki/Folks
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libgee-devel
BuildRequires:	libsocialweb-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	telepathy-glib-devel
BuildRequires:	tracker-devel
BuildRequires:	vala-vapigen
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution-data-server
Requires:	libsocialweb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Folks is a library that aggregates people from multiple sources
(eg, Telepathy connection managers and eventually evolution data
server, Facebook, etc.) to create metacontacts. It's written in Vala
(in part to evaluate Vala). The initial goal is for GObject/C support,
though the Vala bindings should basically automatic.

%package libs
Summary:	Folks libraries
Group:		Libraries

%description libs
Folks libraries.

%package devel
Summary:	Header files for Folks library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Folks library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules 		\
	--enable-tracker-backend	\
	--enable-eds-backend		\
	--enable-vala
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/folks/*/backends/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/folks-import
%attr(755,root,root) %{_bindir}/folks-inspect

%dir %{_libdir}/folks
%dir %{_libdir}/folks
%dir %{_libdir}/folks/??
%dir %{_libdir}/folks/??/backends
%dir %{_libdir}/folks/??/backends/eds
%dir %{_libdir}/folks/32/backends/key-file
%dir %{_libdir}/folks/32/backends/libsocialweb
%dir %{_libdir}/folks/32/backends/telepathy
%dir %{_libdir}/folks/32/backends/tracker

%attr(755,root,root) %{_libdir}/folks/??/backends/eds/eds.so
%attr(755,root,root) %{_libdir}/folks/??/backends/key-file/key-file.so
%attr(755,root,root) %{_libdir}/folks/??/backends/libsocialweb/libsocialweb.so
%attr(755,root,root) %{_libdir}/folks/??/backends/telepathy/telepathy.so
%attr(755,root,root) %{_libdir}/folks/??/backends/tracker/tracker.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libfolks-eds.so.??
%attr(755,root,root) %ghost %{_libdir}/libfolks-libsocialweb.so.??
%attr(755,root,root) %ghost %{_libdir}/libfolks-telepathy.so.??
%attr(755,root,root) %ghost %{_libdir}/libfolks-tracker.so.??
%attr(755,root,root) %ghost %{_libdir}/libfolks.so.??
%attr(755,root,root) %{_libdir}/libfolks-eds.so.*.*.*
%attr(755,root,root) %{_libdir}/libfolks-libsocialweb.so.*.*.*
%attr(755,root,root) %{_libdir}/libfolks-telepathy.so.*.*.*
%attr(755,root,root) %{_libdir}/libfolks-tracker.so.*.*.*
%attr(755,root,root) %{_libdir}/libfolks.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/folks
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%{_pkgconfigdir}/*.pc

