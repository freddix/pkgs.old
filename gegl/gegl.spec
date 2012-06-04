# V4L:		no
# spiro:	no  (usable SPIRO library not found)
# umfpack:	no  (usable umfpack library not found)

Summary:	Generic image processing library
Name:		gegl
Version:	0.2.0
Release:	4
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.gimp.org/pub/gegl/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	32b00002f1f1e316115c4ed922e1dec8
Patch0:		%{name}-gi.patch
URL:		http://www.gegl.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	babl-devel >= 0.1.10
BuildRequires:	cairo-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gobject-introspection-devel
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
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for gegl library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-docs		\
	--disable-silent-rules	\
	--disable-static	\
	--enable-introspection	\
	--without-vala
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gegl-*/*.la

%find_lang %{name}-0.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}-0.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_libdir}/gegl-*/*.so
%dir %{_libdir}/gegl-*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgegl-*.so.?
%attr(755,root,root) %{_libdir}/libgegl-*.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/*.gir
%{_includedir}/gegl-*
%{_libdir}/libgegl-*.so
%{_pkgconfigdir}/gegl-*.pc

