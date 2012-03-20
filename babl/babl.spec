Summary:	Library for pixel-format agnosticism
Name:		babl
Version:	0.1.6
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/babl/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	dc960981a5ec5330fc1c177be9f59068
URL:		http://www.gegl.org/babl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	rsvg
BuildRequires:	w3m
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Babl is a dynamic, any to any, pixel format conversion library. It
provides conversions between the myriad of buffer types images can be
stored in. Babl doesn't only help with existing pixel formats, but
also facilitates creation of new and uncommon ones.

%package devel
Summary:	Header files for babl library
Group:		Development/Libraries
Requires:	%{name}-gir = %{version}-%{release}

%description devel
Development files for babl library.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gobject-introspection-data

%description gir
GObject introspection data for %{name}.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/babl-*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%dir %{_libdir}/babl-*
%attr(755,root,root) %ghost %{_libdir}/libbabl-*.so.?
%attr(755,root,root) %{_libdir}/libbabl-*.so.*.*.*
%attr(755,root,root) %{_libdir}/babl-*/*.so

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/Babl-0.1.gir
%{_includedir}/babl-*
%{_libdir}/libbabl-*.so
%{_pkgconfigdir}/babl.pc

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

