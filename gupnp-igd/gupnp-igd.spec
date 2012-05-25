Summary:	Library to handle UPnP IGD port mapping
Name:		gupnp-igd
Version:	0.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-igd/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	7097d474dc6247fa4ef96e4a2621f9cd
URL:		http://www.gupnp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	gobject-introspection-devel
BuildRequires:	gupnp-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to handle UPnP Internet Gateway Device port mappings.

%package devel
Summary:	Header files for gupnp-igd library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gupnp-igd library.

%package apidocs
Summary:	gupnp-igd library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gupnp-igd library API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-python	\
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libgupnp-igd-1.0.so.?
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so.*.*.*
%{_libdir}/girepository-1.0/GUPnPIgd-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-igd-1.0.so
%{_includedir}/gupnp-igd-1.0
%{_pkgconfigdir}/gupnp-igd-1.0.pc
%{_datadir}/gir-1.0/GUPnPIgd-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-igd

