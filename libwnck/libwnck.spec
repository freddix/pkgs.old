Summary:	General Window Manager interfacing for GNOME utilities
Name:		libwnck
Version:	2.30.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libwnck/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	9bef4b8560acca78cd6f08a95039af9c
Patch0:		%{name}-link.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General Window Manager interfacing for GNOME utilities. This library
is a part of the GNOME platform.

%package devel
Summary:	Header files and documentation for libwnck
Group:		X11/Development/Libraries
Requires:	%{name}-gir = %{version}-%{release}

%description devel
Header, docs and development libraries for libwnck.

%package apidocs
Summary:	libwnck API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libwnck API documentation.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gobject-introspection-data

%description gir
GObject introspection data for wnck library.

%prep
%setup -q
%patch0 -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

# fix gir breakage
sed -i -e 's/--warn-all //' libwnck/Makefile.am

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,en@shaw}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/wnck-urgency-monitor
%attr(755,root,root) %{_bindir}/wnckprop
%attr(755,root,root) %ghost %{_libdir}/libwnck-1.so.??
%attr(755,root,root) %{_libdir}/libwnck-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwnck-1.so
%{_libdir}/libwnck-1.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/libwnck-1.0.pc
%{_datadir}/gir-1.0/Wnck-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

