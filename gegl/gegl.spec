# V4L:		no
# spiro:	no  (usable SPIRO library not found)
# umfpack:	no  (usable umfpack library not found)

Summary:	Generic image processing library
Name:		gegl
Version:	0.1.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.gimp.org/pub/gegl/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	c8279b86b3d584ee4f503839fc500425
URL:		http://www.gegl.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	babl-devel >= 0.1.4
BuildRequires:	cairo-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	graphviz
BuildRequires:	graphviz-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	pkg-config
BuildRequires:	rsvg
BuildRequires:	w3m
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies. and a simple well defined API.

%package libs
Summary:	gegl library
Group:		Libraries

%description libs
gegl library.

%package devel
Summary:	Header files for gegl library
Group:		Development/Libraries
Requires:	%{name}-gir = %{version}-%{release}

%description devel
Header files for gegl library.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gobject-introspection-data

%description gir
GObject introspection data for %{name}.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-docs		\
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gegl-*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_libdir}/gegl-*/*.so
%dir %{_libdir}/gegl-*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgegl-*.so.?
%attr(755,root,root) %{_libdir}/libgegl-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/Gegl-0.1.gir
%{_includedir}/gegl-*
%{_libdir}/libgegl-*.so
%{_pkgconfigdir}/gegl.pc

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

