Summary:	GNOME desktop library
Name:		gnome-desktop
Version:	2.32.1
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-desktop/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	5c80d628a240eb9d9ff78913b31f2f67
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	rarian
BuildRequires:	startup-notification-devel
Requires(post,postun):	rarian
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnome-main
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME desktop library.

%package libs
Summary:	gnome-desktop library
Group:		Development/Libraries

%description libs
This package contains gnome-desktop library.

%package devel
Summary:	GNOME desktop includes
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
GNOME desktop header files.

%package apidocs
Summary:	gnome-desktop API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnome-desktop API documentation.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.in

%build
%{__gtkdocize}
%{__intltoolize}
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules			\
	--disable-static			\
	--with-pnp-ids-path=/etc/pci.ids	\
	--with-gnome-distributor="Freddix"	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,en@shaw,ig,ug,yo}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome-about
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-2.so.??
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so
%{_libdir}/libgnome-desktop-2.la
%{_includedir}/gnome-desktop-2.0
%{_pkgconfigdir}/gnome-desktop-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

