Summary:	OpenGL extension to GTK
Name:		gtkglext
Version:	1.2.0
Release:	13
License:	LGPL
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
# Source0-md5:	ed7ba24ce06a8630c07f2d0ee5f04ab4
Patch0:		%{name}-gtk+.patch
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GtkGLExt provides the GDK objects to support OpenGL rendering in GTK,
and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.

%package devel
Summary:	Development files for GtkGLExt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel

%description devel
Development files for GtkGLExt.

%package apidocs
Summary:	gtkglext API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gtkglext API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-gtk-doc	\
	--with-gdktarget=x11	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* README TODO
%attr(755,root,root) %ghost %{_libdir}/libg[dt]kglext-x11-*.so.?
%attr(755,root,root) %{_libdir}/libg[dt]kglext-x11-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg[dt]kglext-x11-*.so
%{_libdir}/libg[dt]kglext-x11-*.la
%{_libdir}/%{name}-*
%{_includedir}/%{name}-*
%{_pkgconfigdir}/g[dt]kglext-*.pc
%{_aclocaldir}/gtkglext-*.m4

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtkglext

