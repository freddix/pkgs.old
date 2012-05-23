%define		gitver	%{nil}

Summary:	Cairo - multi-platform 2D graphics library
Name:		cairo
Version:	1.12.2
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
%if "%{gitver}" != "%{nil}"
Release:	0.%{gitver}.1
Source:		http://cgit.freedesktop.org/cairo/snapshot/cairo-%{gitver}.tar.bz2
%else
Release:	1
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	87649eb75789739d517c743e94879e51
%endif
Patch0:		%{name}-link.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
%if "%{gitver}" != "%{nil}"
BuildRequires:	gtk-doc
%endif
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pixman-devel
BuildRequires:	pkg-config
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

Cairo exports a stateful rendering API similar in spirit to the path
construction, text, and painting operators of PostScript, (with the
significant addition of translucence in the imaging model). When
complete, the API is intended to support the complete imaging model of
PDF 1.4.

Cairo relies on the Xc library for backend rendering. Xc provides an
abstract interface for rendering to multiple target types. As of this
writing, Xc allows Cairo to target X drawables as well as generic
image buffers. Future backends such as PostScript, PDF, and perhaps
OpenGL are currently being planned.

%package devel
Summary:	Development files for Cairo library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpng-devel

%description devel
Development files for Cairo library.

%package gobject
Summary:	GObject functions library for Cairo graphics library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gobject
GObject functions library for Cairo graphics library.

%package gobject-devel
Summary:	Header files for Cairo GObject library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}

%description gobject-devel
Header files for Cairo GObject library.

%package trace
Summary:	Cairo tracing utility
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description trace
Cairo tracing utility.

%package apidocs
Summary:	Cairo API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Cairo API documentation.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn %{name}-%{gitver}
%else
%setup -q
%endif

sed -i -e 's/-no-undefined/-avoid-version -module -no-undefined/g' \
	util/cairo-trace/Makefile.am	\
	util/cairo-fdr/Makefile.am	\
	util/cairo-sphinx/Makefile.am

%patch0 -p1

%build
%if "%{gitver}" != "%{nil}"
> boilerplate/Makefile.am.features
> src/Makefile.am.features
touch ChangeLog
%{__gtkdocize}
%endif
%{__libtoolize} --automake
%{__aclocal} -I build
%{__autoheader}
%{__automake} --gnu -Wall
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-ps=yes		\
	--enable-tee=yes	\
	--enable-xcb=yes	\
	--enable-xlib=yes	\
	--enable-xml=yes	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/cairo/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_libdir}/cairo
%attr(755,root,root) %ghost %{_libdir}/libcairo-script-interpreter.so.?
%attr(755,root,root) %ghost %{_libdir}/libcairo.so.?
%attr(755,root,root) %{_libdir}/libcairo-script-interpreter.so.*.*.*
%attr(755,root,root) %{_libdir}/libcairo.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo.so
%attr(755,root,root) %{_libdir}/libcairo-script-interpreter.so
%exclude %{_includedir}/cairo/cairo-gobject.h
%{_includedir}/cairo
%exclude %{_pkgconfigdir}/cairo-gobject.pc
%{_pkgconfigdir}/*.pc

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcairo-gobject.so.?
%attr(755,root,root) %{_libdir}/libcairo-gobject.so.*.*.*

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo-gobject.so
%{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo-gobject.pc

%files trace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cairo-trace
%attr(755,root,root) %{_bindir}/cairo-sphinx
%attr(755,root,root) %{_libdir}/cairo/cairo-fdr.so
%attr(755,root,root) %{_libdir}/cairo/cairo-sphinx.so
%attr(755,root,root) %{_libdir}/cairo/libcairo-trace.so

%if "%{gitver}" == "%{nil}"
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cairo
%endif

