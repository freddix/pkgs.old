%define		xfce_version	4.10.0

Summary:	Various GTK+ widgets for Xfce
Name:		libxfce4ui
Version:	4.10.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://archive.xfce.org/src/xfce/libxfce4ui/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	6df1ce474a3d4885aee31cda9dbc9192
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various GTK+ widgets for Xfce.

%package apidocs
Summary:	libxfce4ui API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4ui API documentation.

%package devel
Summary:	Development files for libxfce4ui library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the libxfce4ui library.

%package -n libxfce4kbd
Summary:	libxfce4kbd library
Group:		Libraries
Requires:	libxfce4ui = %{version}-%{release}

%description -n libxfce4kbd
libxfce4kbd library.

%package -n libxfce4kbd-devel
Summary:	Development files for libxfce4kbd library
Group:		Development/Libraries
Requires:	libxfce4kbd = %{version}-%{release}
Requires:	libxfce4ui-devel = %{version}-%{release}

%description -n libxfce4kbd-devel
Development files for the libxfce4kbd library.

%package -n xfce4-about
Summary:	XFCE About
Group:		X11/Applications
Requires:	libxfce4ui = %{version}-%{release}
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme

%description -n xfce4-about
XFCE About application.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-gladeui		\
	--disable-silent-rules		\
	--disable-static		\
	--enable-startup-notification	\
	--with-html-dir=%{_gtkdocdir}	\
	--with-vendor-info="Freddix"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{tl_PH,ur_PK}
rm -f $RPM_BUILD_ROOT%{_libdir}/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n libxfce4kbd -p /sbin/ldconfig
%postun	-n libxfce4kbd -p /sbin/ldconfig

%post -n xfce4-about
%update_icon_cache hicolor

%postun -n xfce4-about
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libxfce4ui-1.so.?
%attr(755,root,root) %{_libdir}/libxfce4ui-1.so.*.*.*

%files -n libxfce4kbd
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%attr(755,root,root) %ghost %{_libdir}/libxfce4kbd-private-2.so.?
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-2.so.*.*.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4ui-1.so
%{_includedir}/xfce4/libxfce4ui-1
%{_pkgconfigdir}/libxfce4ui-1.pc

%files -n libxfce4kbd-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-2.so
%{_includedir}/xfce4/libxfce4kbd-private-2
%{_pkgconfigdir}/libxfce4kbd-private-2.pc

%files -n xfce4-about
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfce4-about
%{_desktopdir}/xfce4-about.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-logo.png

