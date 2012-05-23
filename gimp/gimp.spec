%define		mver	2.0

Summary:	The GNU Image Manipulation Program
Name:		gimp
Version:	2.8.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	28997d14055f15db063eb92e1c8a7ebb
URL:		http://www.gimp.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gegl-devel
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	gtk-webkit-devel
BuildRequires:	intltool
BuildRequires:	lcms-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	poppler-glib-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	udev-glib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires(post,postun):  gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gegl
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GIMP is an image manipulation program suitable for photo
retouching, image composition and image authoring. Many people find it
extremely useful in creating logos and other graphics for web pages.
The GIMP has many of the tools and filters you would expect to find in
similar commercial offerings, and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including
channel operations and layers, effects, sub-pixel imaging and
anti-aliasing, and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of
the included scripts rely on fonts that we cannot distribute. The GIMP
FTP site has a package of fonts that you can install by yourself,
which includes all the fonts needed to run the included scripts.

%package libs
Summary:	GIMP libraries
Group:		Libraries

%description libs
This package contains GIMP libraries.

%package devel
Summary:	GIMP plugin and extension development kit
License:	LGPL
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files for writing GIMP plugins and extensions.

%package apidocs
Summary:	GIMP libraries API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GIMP libraries API documentation.

%package svg
Summary:	SVG plugin for Gimp
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description svg
SVG plugin for Gimp.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--enable-default-binary		\
	--enable-mmx			\
	--enable-mp			\
	--enable-sse			\
	--with-html-dir=%{_gtkdocdir}	\
	--with-libcurl			\
	--with-shm=posix		\
	--without-aa			\
	--without-gvfs 			\
	--without-wmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Link gimptool to gimptool-2.0
ln -s gimptool-%{mver} $RPM_BUILD_ROOT%{_bindir}/gimptool
echo '.so gimptool-%{mver}' > $RPM_BUILD_ROOT%{_mandir}/man1/gimptool.1

rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/modules/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/python/*.{la,py}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ca@valencia

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%doc docs/Wilber*

%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-2.8
%attr(755,root,root) %{_bindir}/gimp-console
%attr(755,root,root) %{_bindir}/gimp-console-2.8
%attr(755,root,root) %{_libdir}/gimp/%{mver}/modules/*.so
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/*
%attr(755,root,root) %{_libdir}/gimp/%{mver}/python/*.so

%config %verify(not md5 mtime) %{_sysconfdir}/%{name}/%{mver}/gimprc*
%config %{_sysconfdir}/%{name}/%{mver}/controllerrc
%config %{_sysconfdir}/%{name}/%{mver}/gtkrc*
%config %{_sysconfdir}/%{name}/%{mver}/menurc
%config %{_sysconfdir}/%{name}/%{mver}/sessionrc
%config %{_sysconfdir}/%{name}/%{mver}/unitrc
%config(noreplace) %{_sysconfdir}/%{name}/%{mver}/templaterc

%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{mver}
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{mver}
%dir %{_libdir}/gimp/%{mver}/modules
%dir %{_libdir}/gimp/%{mver}/plug-ins
%dir %{_libdir}/gimp/%{mver}/python
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{mver}

%{_datadir}/gimp/%{mver}/brushes
%{_datadir}/gimp/%{mver}/dynamics
%{_datadir}/gimp/%{mver}/fractalexplorer
%{_datadir}/gimp/%{mver}/gfig
%{_datadir}/gimp/%{mver}/gflare
%{_datadir}/gimp/%{mver}/gimpressionist
%{_datadir}/gimp/%{mver}/gradients
%{_datadir}/gimp/%{mver}/images
%{_datadir}/gimp/%{mver}/menus
%{_datadir}/gimp/%{mver}/palettes
%{_datadir}/gimp/%{mver}/patterns
%{_datadir}/gimp/%{mver}/scripts
%{_datadir}/gimp/%{mver}/tags
%{_datadir}/gimp/%{mver}/themes
%{_datadir}/gimp/%{mver}/tips
%{_datadir}/gimp/%{mver}/tool-presets
%{_datadir}/gimp/%{mver}/ui

%{_desktopdir}/gimp.desktop
%{_iconsdir}/hicolor/*/apps/gimp.*

%{_libdir}/gimp/%{mver}/environ
%{_libdir}/gimp/%{mver}/interpreters
%{_libdir}/gimp/%{mver}/python/*.png
%{_libdir}/gimp/%{mver}/python/*.py[co]

%{_mandir}/man1/gimp-2.8.1*
%{_mandir}/man1/gimp-console-*
%{_mandir}/man1/gimp-console.1*
%{_mandir}/man1/gimp.1*
%{_mandir}/man5/gimprc-2.8.5*
%{_mandir}/man5/gimprc.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gimptool-%{mver}
%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%{_includedir}/gimp-2.0
%{_aclocaldir}/gimp-2.0.m4

%{_mandir}/man1/gimptool-%{mver}*
%{_mandir}/man1/gimptool.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgimp*

