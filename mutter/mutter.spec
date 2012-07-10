Summary:	Window manager
Name:		mutter
Version:	3.4.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.acc.umu.se/pub/GNOME/sources/mutter/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	3ca02d4ca270e8587643af405c10f57d
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gsettings-desktop-schemas
Provides:	window-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Window manager.

%package libs
Summary:	Mutter library
Group:		Libraries

%description libs
Mutter library.

%package devel
Summary:	Header files for Mutter library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Mutter library.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ZENITY=%{_bindir}/zenity	\
	--disable-schemas-compile	\
	--disable-scrollkeeper		\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{la,ca@valencia}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_bindir}/mutter
%attr(755,root,root) %{_bindir}/mutter-message
%attr(755,root,root) %{_bindir}/mutter-theme-viewer
%attr(755,root,root) %{_bindir}/mutter-window-demo
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-windows.xml
%{_desktopdir}/mutter.desktop
%{_mandir}/man1/*.1*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/mutter
%attr(755,root,root) %ghost %{_libdir}/libmutter.so.?
%attr(755,root,root) %{_libdir}/libmutter.so.*.*.*
%{_libdir}/mutter/Meta-*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter.so
%{_includedir}/mutter
%{_pkgconfigdir}/*.pc
%{_libdir}/mutter/Meta-*.gir

