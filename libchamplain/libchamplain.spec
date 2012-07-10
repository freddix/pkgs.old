%define		api	0.12

Summary:	C library providing a ClutterActor to display maps
Name:		libchamplain
Version:	0.12.2
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://download.gnome.org/sources/libchamplain/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	f0b0961e32afa39fe2051fe6e436f1c2
URL:		http://projects.gnome.org/libchamplain/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	memphis-devel
BuildRequires:	pkg-config
BuildRequires:	vala
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C library providing a ClutterActor to display maps.

%package devel
Summary:	Header files for libchamplain library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libchamplain library.

%package gtk
Summary:	GTK+ bindings to libchamplain
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+ bindings to libchamplain.

%package gtk-devel
Summary:	Header files for libchamplain-gtk library
Group:		Development/Libraries
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description gtk-devel
This is the package containing the header files for
libchamplain-gtk library.

%package apidocs
Summary:	libchamplain API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libchamplain API documentation.

%package gtk-apidocs
Summary:	libchamplain-gtk API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description gtk-apidocs
libchamplain-gtk API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--enable-vala			\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libchamplain-%{api}.so.?
%attr(755,root,root) %{_libdir}/libchamplain-%{api}.so.*.*.*
%{_libdir}/girepository-1.0/Champlain-%{api}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchamplain-%{api}.so
%{_includedir}/libchamplain-%{api}
%{_libdir}/libchamplain-%{api}.la
%{_pkgconfigdir}/champlain-%{api}.pc
%{_pkgconfigdir}/champlain-memphis-%{api}.pc
%{_datadir}/gir-1.0/Champlain-%{api}.gir
%{_datadir}/vala/vapi/champlain-%{api}.vapi

%files gtk
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libchamplain-gtk-%{api}.so.?
%attr(755,root,root) %{_libdir}/libchamplain-gtk-%{api}.so.*.*.*
%{_libdir}/girepository-1.0/GtkChamplain-%{api}.typelib

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchamplain-gtk-%{api}.so
%{_includedir}/libchamplain-gtk-%{api}
%{_libdir}/libchamplain-gtk-%{api}.la
%{_pkgconfigdir}/champlain-gtk-%{api}.pc
%{_datadir}/gir-1.0/GtkChamplain-%{api}.gir
%{_datadir}/vala/vapi/champlain-gtk-%{api}.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libchamplain

%files gtk-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libchamplain-gtk

