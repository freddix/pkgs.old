%define		module	pygtk

Summary:	Python bindings for GTK+ 2.x libraries
Name:		python-%{module}
Version:	2.24.0
Release:	3
Epoch:		2
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/pygtk/2.24/%{module}-%{version}.tar.bz2
# Source0-md5:	a1051d5794fd7696d3c1af6422d17a49
Source1:	%{name}-python.m4
Source2:	%{name}-jhflags.m4
URL:		http://www.pygtk.org/
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	python-numpy-devel
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygobject-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GTK+ 2.x libraries. This package contains
documentation and examples.

%package devel
Summary:	Python bindings for GTK+ 2.x libraries - development files
Group:		Development/Languages/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-glade = %{epoch}:%{version}-%{release}
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	python-devel

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with Python bindings.

%package gtk
Summary:	Python bindings for GTK+ library
Group:		Libraries/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	python-pycairo

%description gtk
Python bindings for GTK+ library.

%package atk
Summary:	Python bindings for ATK library
Group:		Libraries/Python
Requires:	python-pygobject

%description atk
Python bindings for ATK library.

%package pango
Summary:	Python bindings for Pango library
Group:		Libraries/Python
Requires:	python-pycairo
Requires:	python-pygobject

%description pango
Python bindings for Pango library.

%package glade
Summary:	Python bindings for Glade library
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}

%description glade
Python bindings for Glade library.

%package apidocs
Summary:	pygtk API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygtk API documentation.

%prep
%setup -qn %{module}-%{version}

sed -i -e 's|codegen.py|codegen.pyc|' Makefile.am gtk/Makefile.am
sed -i -e 's|createdefs.py|createdefs.pyc|' gtk/Makefile.am

%if 0
mkdir m4
cp %{SOURCE1} m4/python.m4
cp %{SOURCE2} m4/jhflags.m4
%endif

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-thread
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	TARGET_DIR='%{_gtkdocdir}/%{name}'

%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*,*/*}.la
rm -f $RPM_BUILD_ROOT%{_datadir}/pygtk/2.0/codegen/*.py
rm -rf $RPM_BUILD_ROOT%{_libdir}/pygtk/2.0/{demos,pygtk-demo*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THREADS TODO
%dir %{_datadir}/%{module}
%dir %{_datadir}/%{module}/2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{module}/2.0/defs
%{_includedir}/pygtk-2.0
%{_pkgconfigdir}/*.pc

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gtk
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkunixprint.so
%{py_sitedir}/gtk-2.0/gtk/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk*.so

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango*.so

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade*.so

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

