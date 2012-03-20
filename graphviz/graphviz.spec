Summary:	Graph Visualization Tools
Name:		graphviz
Version:	2.26.3
Release:	3
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	6f45946fa622770c45609778c0a982ee
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-no-versioned-plugins.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-ltdl.patch
URL:		http://www.graphviz.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	freetype-devel
BuildRequires:	gawk
BuildRequires:	gd-devel
BuildRequires:	gettext-devel
BuildRequires:	ghostscript-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXaw-devel
BuildRequires:	xorg-libXpm-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ghostscript-fonts-std
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%package libs
Summary:	Graphviz libraries
Group:		Libraries

%description libs
Graphviz libraries.

%package devel
Summary:	Header files for graphviz libraries
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	expat-devel
Requires:	zlib-devel

%description devel
This package contains the header files for graphviz libraries.

%package graphs
Summary:	Demo graphs for graphviz
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description graphs
This package provides some example graphs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-guile		\
	--disable-java		\
	--disable-lua		\
	--disable-ocaml		\
	--disable-ruby		\
	--disable-sharp		\
	--disable-silent-rules	\
	--disable-static	\
	--disable-swig		\
	--disable-tcl		\
	--with-included-ltdl=no	\
	--with-ltdl-include=%{_includedir}	\
	--with-ltdl-lib=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# replace dead (after compression) softlinks by groff redirections
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{circo,fdp,neato,twopi}.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/circo.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/fdp.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/neato.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/twopi.1

# created by %{_bindir}/dot -c
touch $RPM_BUILD_ROOT%{_libdir}/graphviz/config
rm -f $RPM_BUILD_ROOT%{_libdir}/graphviz/*/libgv_*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/graphviz/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/graphiz/doc

rm -rf $RPM_BUILD_ROOT%{_datadir}/graphviz/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x %{_bindir}/dot ] || %{_bindir}/dot -c > /dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_core.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_dot_layout.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gd.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_neato_layout.so

%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gdk_pixbuf.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gs.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gtk.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_pango.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_rsvg.so
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_xlib.so

%dir %{_libdir}/graphviz
%dir %{_libdir}/graphviz/guile
%dir %{_libdir}/graphviz/perl
%dir %{_libdir}/graphviz/python
%ghost %{_libdir}/graphviz/config

# what about the rest of *.la?
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/lefty
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcdt.so.?
%attr(755,root,root) %ghost %{_libdir}/libcgraph.so.?
%attr(755,root,root) %ghost %{_libdir}/libgraph.so.?
%attr(755,root,root) %ghost %{_libdir}/libgvc.so.?
%attr(755,root,root) %ghost %{_libdir}/libpathplan.so.?
%attr(755,root,root) %ghost %{_libdir}/libgvpr.so.?
%attr(755,root,root) %ghost %{_libdir}/libxdot.so.?
%attr(755,root,root) %{_libdir}/libcdt.so.*.*.*
%attr(755,root,root) %{_libdir}/libcgraph.so.*.*.*
%attr(755,root,root) %{_libdir}/libgraph.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvc.so.*.*.*
%attr(755,root,root) %{_libdir}/libpathplan.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvpr.so.*.*.*
%attr(755,root,root) %{_libdir}/libxdot.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdt.so
%attr(755,root,root) %{_libdir}/libcgraph.so
%attr(755,root,root) %{_libdir}/libgraph.so
%attr(755,root,root) %{_libdir}/libgvc.so
%attr(755,root,root) %{_libdir}/libgvpr.so
%attr(755,root,root) %{_libdir}/libpathplan.so
%attr(755,root,root) %{_libdir}/libxdot.so
%{_includedir}/graphviz
%{_pkgconfigdir}/libcdt.pc
%{_pkgconfigdir}/libcgraph.pc
%{_pkgconfigdir}/libgraph.pc
%{_pkgconfigdir}/libgvc.pc
%{_pkgconfigdir}/libgvpr.pc
%{_pkgconfigdir}/libpathplan.pc
%{_pkgconfigdir}/libxdot.pc

%{_mandir}/man3/*
%{_mandir}/man7/graphviz.7*

%files graphs
%defattr(644,root,root,755)
%{_datadir}/graphviz/graphs

