Summary:	Scalable vector graphics editor
Name:		inkscape
Version:	0.48.2
Release:	2
License:	GPL v2, LGPL v2.1
Group:		X11/Applications/Graphics
Source0:	http://download.sourceforge.net/inkscape/%{name}-%{version}.tar.bz2
# Source0-md5:	f60b98013bd1121b2cc301f3485076ba
URL:		http://www.inkscape.org/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	gc-devel
BuildRequires:	gettext-devel
BuildRequires:	gsl-devel
BuildRequires:	gtkmm-devel
BuildRequires:	intltool
BuildRequires:	lcms-devel
BuildRequires:	libpng-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	poppler-glib-devel
BuildRequires:	popt-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-libXft-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	python-lxml
Requires:	xdg-icon-theme
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inkscape is a program for viewing, making, and editing two-dimensional
vector drawings.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--enable-lcms		\
	--enable-poppler-cairo	\
	--without-gnome-vfs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en_US@piglatin,sr@latin,te_IN}
rm -f $RPM_BUILD_ROOT%{_datadir}/inkscape/*/README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TRANSLATORS

%dir %{_datadir}/inkscape
%dir %{_datadir}/inkscape/extensions
%dir %{_datadir}/inkscape/extensions/Barcode
%dir %{_datadir}/inkscape/extensions/xaml2svg
%dir %{_datadir}/inkscape/filters
%dir %{_datadir}/inkscape/screens
%dir %{_datadir}/inkscape/templates
%dir %{_datadir}/inkscape/tutorials

%attr(755,root,root) %{_bindir}/*

%attr(755,root,root) %{_datadir}/inkscape/extensions/*.js
%attr(755,root,root) %{_datadir}/inkscape/extensions/*.pl
%attr(755,root,root) %{_datadir}/inkscape/extensions/*.pm
%attr(755,root,root) %{_datadir}/inkscape/extensions/*.py
%attr(755,root,root) %{_datadir}/inkscape/extensions/*.sh
%attr(755,root,root) %{_datadir}/inkscape/extensions/Barcode/*.py

%{_datadir}/inkscape/clipart
%{_datadir}/inkscape/examples
%{_datadir}/inkscape/extensions/*.inx
%{_datadir}/inkscape/extensions/*.svg
%{_datadir}/inkscape/extensions/*.xml
%{_datadir}/inkscape/extensions/*.xsl
%{_datadir}/inkscape/extensions/*.xslt
%{_datadir}/inkscape/extensions/Poly3DObjects
%{_datadir}/inkscape/extensions/alphabet_soup
%{_datadir}/inkscape/extensions/xaml2svg/*.xsl
%{_datadir}/inkscape/filters/*.svg
%{_datadir}/inkscape/icons
%{_datadir}/inkscape/keys
%{_datadir}/inkscape/markers
%{_datadir}/inkscape/palettes
%{_datadir}/inkscape/patterns
%{_datadir}/inkscape/ui

%{_datadir}/inkscape/screens/about.svg

%{_datadir}/inkscape/templates/default.svg
%lang(ca) %{_datadir}/inkscape/templates/*.ca.svg
%lang(cs) %{_datadir}/inkscape/templates/*.cs.svg
%lang(de) %{_datadir}/inkscape/templates/*.de.svg
%lang(eo) %{_datadir}/inkscape/templates/*.eo.svg
%lang(es) %{_datadir}/inkscape/templates/*.es.svg
%lang(fi) %{_datadir}/inkscape/templates/*.fi.svg
%lang(fr) %{_datadir}/inkscape/templates/*.fr.svg
%lang(hu) %{_datadir}/inkscape/templates/*.hu.svg
%lang(it) %{_datadir}/inkscape/templates/*.it.svg
%lang(ja) %{_datadir}/inkscape/templates/*.ja.svg
%lang(lt) %{_datadir}/inkscape/templates/*.lt.svg
%lang(nl) %{_datadir}/inkscape/templates/*.nl.svg
%lang(pl) %{_datadir}/inkscape/templates/*.pl.svg
%lang(pt_BR) %{_datadir}/inkscape/templates/*.pt_BR.svg
%lang(sk) %{_datadir}/inkscape/templates/*.sk.svg

%{_datadir}/inkscape/templates/A4.svg
%{_datadir}/inkscape/templates/A4_landscape.svg
%{_datadir}/inkscape/templates/CD_cover_300dpi.svg
%{_datadir}/inkscape/templates/DVD_cover_regular_300dpi.svg
%{_datadir}/inkscape/templates/DVD_cover_slim_300dpi.svg
%{_datadir}/inkscape/templates/DVD_cover_superslim_300dpi.svg
%{_datadir}/inkscape/templates/DVD_cover_ultraslim_300dpi.svg
%{_datadir}/inkscape/templates/LaTeX_Beamer.svg
%{_datadir}/inkscape/templates/Letter.svg
%{_datadir}/inkscape/templates/Letter_landscape.svg
%{_datadir}/inkscape/templates/black_opaque.svg
%{_datadir}/inkscape/templates/business_card_85x54mm.svg
%{_datadir}/inkscape/templates/business_card_90x50mm.svg
%{_datadir}/inkscape/templates/desktop_1024x768.svg
%{_datadir}/inkscape/templates/desktop_1600x1200.svg
%{_datadir}/inkscape/templates/desktop_640x480.svg
%{_datadir}/inkscape/templates/desktop_800x600.svg
%{_datadir}/inkscape/templates/fontforge_glyph.svg
%{_datadir}/inkscape/templates/icon_16x16.svg
%{_datadir}/inkscape/templates/icon_32x32.svg
%{_datadir}/inkscape/templates/icon_48x48.svg
%{_datadir}/inkscape/templates/icon_64x64.svg
%{_datadir}/inkscape/templates/no_borders.svg
%{_datadir}/inkscape/templates/no_layers.svg
%{_datadir}/inkscape/templates/video_HDTV_1920x1080.svg
%{_datadir}/inkscape/templates/video_NTSC_720x486.svg
%{_datadir}/inkscape/templates/video_PAL_720x576.svg
%{_datadir}/inkscape/templates/web_banner_468x60.svg
%{_datadir}/inkscape/templates/web_banner_728x90.svg
%{_datadir}/inkscape/templates/white_opaque.svg

%{_datadir}/inkscape/tutorials/tutorial-advanced.svg
%{_datadir}/inkscape/tutorials/tutorial-basic.svg
%{_datadir}/inkscape/tutorials/tutorial-calligraphy.svg
%{_datadir}/inkscape/tutorials/tutorial-elements.svg
%{_datadir}/inkscape/tutorials/tutorial-interpolate.svg
%{_datadir}/inkscape/tutorials/tutorial-shapes.svg
%{_datadir}/inkscape/tutorials/tutorial-tips.svg
%{_datadir}/inkscape/tutorials/tutorial-tracing.svg

%lang(bg) %{_datadir}/inkscape/tutorials/*.bg.svg
%lang(ca) %{_datadir}/inkscape/tutorials/*.ca.svg
%lang(cs) %{_datadir}/inkscape/tutorials/*.cs.svg
%lang(da) %{_datadir}/inkscape/tutorials/*.da.svg
%lang(de) %{_datadir}/inkscape/tutorials/*.de.svg
%lang(es) %{_datadir}/inkscape/tutorials/*.es.svg
%lang(fr) %{_datadir}/inkscape/tutorials/*.fr.svg
%lang(hu) %{_datadir}/inkscape/tutorials/*.hu.svg
%lang(it) %{_datadir}/inkscape/tutorials/*.it.svg
%lang(ja) %{_datadir}/inkscape/tutorials/*.ja.svg
%lang(nn) %{_datadir}/inkscape/tutorials/*.nn.svg
%lang(pl) %{_datadir}/inkscape/tutorials/*.pl.svg
%lang(pt_BR) %{_datadir}/inkscape/tutorials/*.pt_BR.svg
%lang(ru) %{_datadir}/inkscape/tutorials/*.ru.svg
%lang(sk) %{_datadir}/inkscape/tutorials/*.sk.svg
%lang(sl) %{_datadir}/inkscape/tutorials/*.sl.svg
%lang(tr) %{_datadir}/inkscape/tutorials/*.tr.svg
%lang(vi) %{_datadir}/inkscape/tutorials/*.vi.svg
%lang(zh_CN) %{_datadir}/inkscape/tutorials/*.zh_CN.svg

%{_datadir}/inkscape/tutorials/potrace.png
%lang(ca) %{_datadir}/inkscape/tutorials/potrace-ca.png
%lang(de) %{_datadir}/inkscape/tutorials/potrace-de.png
%lang(es) %{_datadir}/inkscape/tutorials/potrace-es.png
%lang(fr) %{_datadir}/inkscape/tutorials/potrace-fr.png
%lang(hu) %{_datadir}/inkscape/tutorials/potrace-hu.png
%lang(pl) %{_datadir}/inkscape/tutorials/potrace-pl.png
%lang(ru) %{_datadir}/inkscape/tutorials/potrace-ru.png

%{_datadir}/inkscape/tutorials/edge3d.svg
%{_datadir}/inkscape/tutorials/gpl-2.svg
%{_datadir}/inkscape/tutorials/making_markers.svg
%{_datadir}/inkscape/tutorials/oldguitar.jpg
%{_datadir}/inkscape/tutorials/tux.png

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/inkscape.png

%{_mandir}/man1/*

%lang(ca) %doc README.ca.txt
%lang(de) %doc README.de.txt
%lang(es) %doc README.es.txt
%lang(fr) %doc README.fr.txt
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %doc README.it.txt

