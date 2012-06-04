Summary:	Library for rich GUIs
Name:		clutter
Version:	1.10.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://source.clutter-project.org/sources/clutter/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	23c96fc828de7f3c77ddce69c894dd88
URL:		http://www.clutter-project.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-gobject-devel
BuildRequires:	cogl-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	json-glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXfixes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter is an open source software library for creating fast, visually
rich graphical user interfaces. The most obvious example of potential
usage is in media center type applications. We hope however it can be
used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but
with an API which hides the underlying GL complexity from the
developer. The Clutter API is intended to be easy to use, efficient
and flexible.

%package devel
Summary:	Header files for clutter library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for clutter library.

%package apidocs
Summary:	clutter API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--enable-introspection=yes	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/az_IR

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libclutter-1.0.so.?
%attr(755,root,root) %{_libdir}/libclutter-1.0.so.*.*.*
# compat link
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-1.0.so
%attr(755,root,root) %{_libdir}/libclutter-glx-1.0.so
%{_includedir}/clutter-1.0
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cally
%{_gtkdocdir}/clutter

