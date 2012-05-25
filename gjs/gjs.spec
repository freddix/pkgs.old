Summary:	GObject-introspection based JavaScript bindings
Name:		gjs
Version:	1.32.0
Release:	2
License:	MPL1.1/LGPLv2+/GPLv2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gjs/1.32/%{name}-%{version}.tar.xz
# Source0-md5:	a77fe0edb6f681434d8360c62e471abf
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	js-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GObject-introspection based JavaScript bindings.

%package libs
Summary:	GJS libraries
Group:		Libraries

%description libs
GJS libraries.

%package devel
Summary:	Header files for GJS library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for GJS library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gjs-1.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gjs-1.0/*.so
%{_datadir}/gjs-1.0

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/gjs-1.0
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/girepository-1.0/GjsDBus-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_datadir}/gir-1.0/GjsDBus-1.0.gir
%{_includedir}/gjs-1.0
%{_pkgconfigdir}/*.pc

