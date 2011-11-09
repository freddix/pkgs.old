Summary:	Virtual lighttable and darkroom for photographers
Name:		darktable
Version:	0.9.3
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/darktable/%{name}-%{version}.tar.gz
# Source0-md5:	49253a3a2990a4bf8e0b0a19295f19bd
BuildRequires:	GConf-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exiv2-devel
#BuildRequires:	gegl-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	lcms2-devel
BuildRequires:	lensfun-devel >= 0.2.3
BuildRequires:	libglade-devel
BuildRequires:	libgomp-devel
BuildRequires:	libtool
BuildRequires:	sqlite3-devel
Requires(post,preun):	GConf
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gdk-pixbuf
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

sed -i 's/^[ \t]*//' data/%{name}.desktop

%build
install -d build
cd build
%cmake .. \
	-DDONT_INSTALL_GCONF_SCHEMAS=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/darktable/{plugins,plugins/*,plugins/*/*,views}/*.la

%find_lang %{name}

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/darktable.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install darktable.schemas
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall darktable.schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{AUTHORS,ChangeLog,NEWS,README,TODO}
%dir %{_libdir}/darktable
%dir %{_libdir}/darktable/plugins
%dir %{_libdir}/darktable/plugins/imageio
%dir %{_libdir}/darktable/plugins/imageio/format
%dir %{_libdir}/darktable/plugins/imageio/storage
%dir %{_libdir}/darktable/plugins/lighttable
%dir %{_libdir}/darktable/views
%attr(755,root,root) %{_bindir}/darktable
%attr(755,root,root) %{_bindir}/darktable-cltest
%attr(755,root,root) %{_bindir}/darktable-faster
%attr(755,root,root) %{_bindir}/darktable-viewer
%attr(755,root,root) %{_libdir}/darktable/libdarktable.so
%attr(755,root,root) %{_libdir}/darktable/plugins/*.so
%attr(755,root,root) %{_libdir}/darktable/plugins/imageio/format/*.so
%attr(755,root,root) %{_libdir}/darktable/plugins/imageio/storage/*.so
%attr(755,root,root) %{_libdir}/darktable/plugins/lighttable/*.so
%attr(755,root,root) %{_libdir}/darktable/views/*.so
%{_datadir}/%{name}
%{_desktopdir}/darktable.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_sysconfdir}/gconf/schemas/darktable.schemas
%{_mandir}/man1/darktable.1*

