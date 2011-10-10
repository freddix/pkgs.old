Summary:	Toolchain to create panoramic images
Name:		hugin
Version:	2011.2.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.bz2
# Source0-md5:	3f5cc3c02a5763f268d674a0bc91cb95
Patch0:		%{name}-cppflags.patch
Patch1:		%{name}-desktop.patch
URL:		http://hugin.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	ZThread-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	exiv2-devel
BuildRequires:	freeglut-devel
BuildRequires:	gettext-devel
BuildRequires:	glew-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpano13-devel >= 2.9.18
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	sed
BuildRequires:	tclap
BuildRequires:	wxGTK-unicode-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
Requires:	autopano-sift-C
Requires:	enblend-enfuse
Requires:	perl-Image-ExifTool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With hugin you can assemble a mosaic of photographs into a complete
immensive panorama, stitch any series of overlapping pictures and much
more.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

mv -f src/translations/{ca_ES,ca}.po
mv -f src/translations/{cs_CZ,cs}.po

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_EXE_LINKER_FLAGS="%{rpmldflags}"	\
	-DCMAKE_MODULE_LINKER_FLAGS="%{rpmldflags}"	\
	-DCMAKE_SHARED_LINKER_FLAGS="%{rpmldflags}"	\
	-DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# cmake is so great there is no way to pass proper path
mv $RPM_BUILD_ROOT%{_iconsdir}/{gnome,hicolor}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENCE_VIGRA README TODO
%attr(755,root,root) %{_bindir}/PTBatcher
%attr(755,root,root) %{_bindir}/PTBatcherGUI
%attr(755,root,root) %{_bindir}/align_image_stack
%attr(755,root,root) %{_bindir}/autooptimiser
%attr(755,root,root) %{_bindir}/autopano-noop.sh
%attr(755,root,root) %{_bindir}/calibrate_lens_gui
%attr(755,root,root) %{_bindir}/celeste_standalone
%attr(755,root,root) %{_bindir}/cpclean
%attr(755,root,root) %{_bindir}/deghosting_mask
%attr(755,root,root) %{_bindir}/fulla
%attr(755,root,root) %{_bindir}/hugin
%attr(755,root,root) %{_bindir}/hugin_hdrmerge
%attr(755,root,root) %{_bindir}/hugin_stitch_project
%attr(755,root,root) %{_bindir}/checkpto
%attr(755,root,root) %{_bindir}/cpfind
%attr(755,root,root) %{_bindir}/icpfind
%attr(755,root,root) %{_bindir}/matchpoint
%attr(755,root,root) %{_bindir}/nona
%attr(755,root,root) %{_bindir}/nona_gui
%attr(755,root,root) %{_bindir}/pano_modify
%attr(755,root,root) %{_bindir}/pano_trafo
%attr(755,root,root) %{_bindir}/pto2mk
%attr(755,root,root) %{_bindir}/pto_merge
%attr(755,root,root) %{_bindir}/tca_correct
%attr(755,root,root) %{_bindir}/vig_optimize

%dir %{_libdir}/hugin
%attr(755,root,root) %{_libdir}/hugin/libceleste.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libflann_cpp.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhuginbase.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhuginbasewx.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhuginlines.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libhuginvigraimpex.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libicpfindlib.so.*.*
%attr(755,root,root) %{_libdir}/hugin/liblocalfeatures.so.*.*
%attr(755,root,root) %{_libdir}/hugin/libmakefilelib.so.*.*

%{_datadir}/%{name}
%{_datadir}/mime/packages/hugin.xml

%{_desktopdir}/calibrate_lens_gui.desktop
%{_desktopdir}/hugin.desktop
%{_iconsdir}/hicolor/*/mimetypes/gnome-mime-application-x-ptoptimizer-script.png
%{_pixmapsdir}/hugin.png

%{_mandir}/man1/*.1*

