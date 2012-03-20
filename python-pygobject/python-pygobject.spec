%define		module	pygobject
#
Summary:	Python bindings for GObject library
Name:		python-%{module}
Version:	2.28.6
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/pygobject/2.28/%{module}-%{version}.tar.bz2
# Source0-md5:	a43d783228dd32899e6908352b8308f3
Source1:	%{name}-as-ac-expand.m4
Source2:	%{name}-jhflags.m4
Source3:	%{name}-python.m4
Patch0:		%{name}-css.patch
Patch1:		%{name}-compat.patch
Patch2:		%{name}-codegen.patch
Patch3:		%{name}-link.patch
URL:		http://www.pygtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-gio-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	python-devel
BuildRequires:	python-pycairo-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
# requires GLib-2.0.typelib, GModule-2.0.typelib
# GObject-2.0.typelib, Gio-2.0.typelib
Requires:	gobject-introspection-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GObject library.

%package devel
Summary:	Python bindings for GObject library
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains files required to build wrappers for GObject
addon libraries so that they interoperate with Python bindings.

%package apidocs
Summary:	pygobject API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygobject API documentation.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d m4

# missing in tarball somtetimes...
#install %{SOURCE1} m4/as-ac-expand.m4
#install %{SOURCE2} m4/jhflags.m4
#install %{SOURCE3} m4/python.m4

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	TARGET_DIR=%{_gtkdocdir}/pygobject

install -D docs/style.css $RPM_BUILD_ROOT%{_datadir}/pygobject/css/style.css

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/{*.la,*/*.la}

%py_comp $RPM_BUILD_ROOT%{_datadir}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}

%py_postclean
rm -f $RPM_BUILD_ROOT%{_datadir}/%{module}/2.0/codegen/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%dir %{_datadir}/%{module}
%dir %{_datadir}/%{module}/2.0
%dir %{_datadir}/%{module}/2.0/codegen
%dir %{_datadir}/%{module}/css
%dir %{_datadir}/%{module}/xsl

%{py_sitedir}/*.py[co]
%{py_sitedir}/pygtk.pth

%dir %{py_sitedir}/gi
%dir %{py_sitedir}/gi/overrides
%dir %{py_sitedir}/gi/repository
%attr(755,root,root) %{py_sitedir}/gi/_gi.so
%attr(755,root,root) %{py_sitedir}/gi/_gi_cairo.so
%{py_sitedir}/gi/*.py[co]
%{py_sitedir}/gi/overrides/*.py[co]
%{py_sitedir}/gi/repository/*.py[co]

%dir %{py_sitedir}/glib
%attr(755,root,root) %{py_sitedir}/glib/*.so
%{py_sitedir}/glib/*.py[co]

%dir %{py_sitedir}/gobject
%attr(755,root,root) %{py_sitedir}/gobject/*.so
%{py_sitedir}/gobject/*.py[co]

%dir %{py_sitedir}/gtk-2.0
%dir %{py_sitedir}/gtk-2.0/gio
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gio/*.so
%{py_sitedir}/gtk-2.0/gio/*.py[co]
%{py_sitedir}/gtk-2.0/*.py[co]

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pygobject-codegen-2.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/pygtk-2.0
%{_pkgconfigdir}/*.pc
%{_datadir}/%{module}/css/*.css
%{_datadir}/%{module}/xsl/*.py*
%{_datadir}/%{module}/xsl/*.xsl
%{_datadir}/%{module}/2.0/defs
%{_datadir}/%{module}/2.0/codegen/*.py[co]

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{module}

