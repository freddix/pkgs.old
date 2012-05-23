Summary:	An image viewer and browser for GNOME
Name:		gthumb
Version:	3.0.0
Release:	1
License:	GPL v2
Vendor:		GNOME
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/gthumb/3.0/%{name}-%{version}.tar.xz
# Source0-md5:	70cc20019cd7fc033b000a1d780d834d
URL:		http://live.gnome.org/gthumb
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	brasero-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libexif-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	xorg-libXtst-devel
BuildRequires:	xorg-libXxf86vm-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	rarian
Requires:	gtk+3
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
	--disable-schemas-compile	\
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
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/extensions
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/extensions/*.so
%{_libdir}/%{name}/extensions/*.extension
%{_datadir}/gthumb
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.change-date.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.comments.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.contact-sheet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.convert-format.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.crop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.facebook.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.file-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.gstreamer-tools.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.image-print.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.image-viewer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.photo-importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.picasaweb.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.pixbuf-savers.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.rename-series.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.resize-images.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.resize.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.rotate.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.slideshow.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.webalbums.gschema.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg

