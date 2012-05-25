Summary:	A library for using 3D graphics hardware to draw pretty pictures
Name:		cogl
Version:	1.10.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://source.clutter-project.org/sources/cogl/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	1e47d7b2942d365e21b32f6e884c401a
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkg-config
Suggests:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cogl is a small open source library for using 3D graphics hardware to
draw pretty pictures. The API departs from the flat state machine
style of OpenGL and is designed to make it easy to write orthogonal
components that can render without stepping on each others toes.

%package devel
Summary:	Header files for cogl library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for building and developing applications with cogl.

%package apidocs
Summary:	cogl API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
cogl API documentation.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-cairo		\
	--enable-cogl-pango	\
	--enable-gdk-pixbuf	\
	--enable-glx		\
	--enable-introspection	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libcogl-pango.so.?
%attr(755,root,root) %ghost %{_libdir}/libcogl.so.?
%attr(755,root,root) %{_libdir}/libcogl-pango.so.*.*.*
%attr(755,root,root) %{_libdir}/libcogl.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcogl*.so
%{_includedir}/cogl
%{_pkgconfigdir}/cogl*.pc
%{_datadir}/gir-1.0/*.gir

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cogl
%{_gtkdocdir}/cogl-2.0-experimental
%endif

