%define		xfce_version	4.10.0

Summary:	Xfce file manager
Name:		Thunar
Version:	1.4.0
Release:	1
License:	GPL v2 / LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/thunar/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	737ad2c36ed36b10fef82e860b9e990a
URL:		http://thunar.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	exo-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	udev-glib-devel
BuildRequires:	xfce4-panel-devel >= %{xfce_version}
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	exo
Requires:	shared-mime-info
Requires:	xfconf
Suggests:	gvfs
Suggests:	tumbler
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thunar is a modern file manager, aiming to be easy-to-use and fast.

%package libs
Summary:	Thunar libraries
Group:		Libraries

%description libs
Thunar libraries.

%package devel
Summary:	Header files for Thunar libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Thunar libraries.

%package apidocs
Summary:	Thunar API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Thunar API documentation.

%package -n xfce4-plugin-tpa
Summary:	Trash Panel Applet
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	xfce4-panel

%description -n xfce4-plugin-tpa
Thunar-TPA is an extension for the XFCE Panel, which enables users
to add a trash can to their panel.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules		\
	--enable-dbus			\
	--enable-exif			\
	--enable-pcre			\
	--enable-startup-notification	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/thunarx-2/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{nn_NO,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO docs/README.*
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/xdg/Thunar
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/Thunar/*.xml
%dir %{_libdir}/Thunar
%attr(755,root,root) %{_libdir}/Thunar/ThunarBulkRename
%attr(755,root,root) %{_libdir}/Thunar/thunar-sendto-email
%dir %{_libdir}/thunarx-2
%attr(755,root,root) %{_libdir}/thunarx-2/*.so

%{_datadir}/Thunar
%{_datadir}/dbus-1/services/*.service
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_iconsdir}/hicolor/*/*/*/*.png
%{_pixmapsdir}/Thunar
%{_mandir}/man1/Thunar*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libthunar*.so.?
%attr(755,root,root) %{_libdir}/libthunar*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libthunar*.so
%{_includedir}/thunar*
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/thunar*

%files -n xfce4-plugin-tpa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libthunar-tpa.so
%{_datadir}/xfce4/panel-plugins/*.desktop

