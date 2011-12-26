Summary:	An image viewer and browser for GNOME
Name:		gthumb
Version:	2.14.1
Release:	1
License:	GPL v2
Vendor:		GNOME
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/gthumb/2.14/%{name}-%{version}.tar.xz
# Source0-md5:	00b68db29b9db05e7ff22d53bbdee822
URL:		http://live.gnome.org/gthumb
BuildRequires:	GConf-devel
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	brasero-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libexif-devel
BuildRequires:	libglade-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	xorg-libXtst-devel
BuildRequires:	xorg-libXxf86vm-devel
Requires(post,preun):	GConf
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	rarian
Suggests:	dcraw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images,
view slideshows, set your desktop background, and more.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__gnome_doc_prepare}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-gnome-3		\
	--disable-schemas-install	\
	--disable-scrollkeeper		\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/*.la
rm -rf $RPM_BUILD_ROOT%{_includedir}

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/hicolor

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gthumb-comments.schemas
%gconf_schema_install gthumb-facebook.schemas
%gconf_schema_install gthumb-file-manager.schemas
%gconf_schema_install gthumb-gstreamer.schemas
%gconf_schema_install gthumb-image-viewer.schemas
%gconf_schema_install gthumb-importer.schemas
%gconf_schema_install gthumb-picasaweb.schemas
%gconf_schema_install gthumb-pixbuf-savers.schemas
%gconf_schema_install gthumb-slideshow.schemas
%gconf_schema_install gthumb.schemas
%gconf_schema_install gthumb_change_date.schemas
%gconf_schema_install gthumb_contact_sheet.schemas
%gconf_schema_install gthumb_convert_format.schemas
%gconf_schema_install gthumb_crop_options.schemas
%gconf_schema_install gthumb_image_print.schemas
%gconf_schema_install gthumb_photo_importer.schemas
%gconf_schema_install gthumb_rename_series.schemas
%gconf_schema_install gthumb_resize_images.schemas
%gconf_schema_install gthumb_resize_options.schemas
%gconf_schema_install gthumb_rotate_options.schemas
%gconf_schema_install gthumb_webalbums.schemas

%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gthumb-comments.schemas
%gconf_schema_uninstall gthumb-facebook.schemas
%gconf_schema_uninstall gthumb-file-manager.schemas
%gconf_schema_uninstall gthumb-gstreamer.schemas
%gconf_schema_uninstall gthumb-image-viewer.schemas
%gconf_schema_uninstall gthumb-importer.schemas
%gconf_schema_uninstall gthumb-picasaweb.schemas
%gconf_schema_uninstall gthumb-pixbuf-savers.schemas
%gconf_schema_uninstall gthumb-slideshow.schemas
%gconf_schema_uninstall gthumb.schemas
%gconf_schema_uninstall gthumb_change_date.schemas
%gconf_schema_uninstall gthumb_contact_sheet.schemas
%gconf_schema_uninstall gthumb_convert_format.schemas
%gconf_schema_uninstall gthumb_crop_options.schemas
%gconf_schema_uninstall gthumb_image_print.schemas
%gconf_schema_uninstall gthumb_photo_importer.schemas
%gconf_schema_uninstall gthumb_rename_series.schemas
%gconf_schema_uninstall gthumb_resize_images.schemas
%gconf_schema_uninstall gthumb_resize_options.schemas
%gconf_schema_uninstall gthumb_rotate_options.schemas
%gconf_schema_uninstall gthumb_webalbums.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/extensions
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/extensions/*.so
%{_libdir}/%{name}/extensions/*.extension
%{_datadir}/gthumb
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_sysconfdir}/gconf/schemas/gthumb-comments.schemas
%{_sysconfdir}/gconf/schemas/gthumb-facebook.schemas
%{_sysconfdir}/gconf/schemas/gthumb-file-manager.schemas
%{_sysconfdir}/gconf/schemas/gthumb-gstreamer.schemas
%{_sysconfdir}/gconf/schemas/gthumb-image-viewer.schemas
%{_sysconfdir}/gconf/schemas/gthumb-importer.schemas
%{_sysconfdir}/gconf/schemas/gthumb-picasaweb.schemas
%{_sysconfdir}/gconf/schemas/gthumb-pixbuf-savers.schemas
%{_sysconfdir}/gconf/schemas/gthumb-slideshow.schemas
%{_sysconfdir}/gconf/schemas/gthumb.schemas
%{_sysconfdir}/gconf/schemas/gthumb_change_date.schemas
%{_sysconfdir}/gconf/schemas/gthumb_contact_sheet.schemas
%{_sysconfdir}/gconf/schemas/gthumb_convert_format.schemas
%{_sysconfdir}/gconf/schemas/gthumb_crop_options.schemas
%{_sysconfdir}/gconf/schemas/gthumb_image_print.schemas
%{_sysconfdir}/gconf/schemas/gthumb_photo_importer.schemas
%{_sysconfdir}/gconf/schemas/gthumb_rename_series.schemas
%{_sysconfdir}/gconf/schemas/gthumb_resize_images.schemas
%{_sysconfdir}/gconf/schemas/gthumb_resize_options.schemas
%{_sysconfdir}/gconf/schemas/gthumb_rotate_options.schemas
%{_sysconfdir}/gconf/schemas/gthumb_webalbums.schemas

