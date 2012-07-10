%include	/usr/lib/rpm/macros.gstreamer

%define		gstname		gst-plugins-bad
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.35

Summary:	Bad GStreamer Streaming-media framework plugins
Name:		gstreamer-plugins-bad
Version:	0.10.23
Release:	3
License:	LPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.xz
# Source0-md5:	e4822fa2cc933768e2998311a1565979
Patch0:		%{name}-divx4linux.patch
Patch1:		%{name}-musicbrainz5.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib-devel
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.5
BuildRequires:	pkg-config
#
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	dirac-devel
BuildRequires:	exempi-devel
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	frei0r-devel
BuildRequires:	jasper-devel
BuildRequires:	libcdaudio-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libdca-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libkate-devel
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libofa-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libx264-devel
BuildRequires:	mjpegtools-devel
BuildRequires:	neon-devel
BuildRequires:	rpm-gstreamerprov
BuildRequires:	soundtouch-devel
BuildRequires:	vo-aacenc-devel
BuildRequires:	xvidcore-devel
Requires(post,preun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%package libs
Summary:	Gstreamer bad plugins - shared libraries
Group:		Libraries

%description libs
Gstreamer base plugins - shared libraries.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer-devel >= %{gst_req_ver}

%description devel
Include files for GStreamer streaming-media framework plugins.

%package apidocs
Summary:	gstreamer-plugins-bad API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gstreamer-plugins-bad API documentation.

%prep
%setup -qn %{gstname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__autopoint}
patch -p0 < common/gettext.patch
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gsm		\
	--disable-ladspa	\
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstadpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmenc.so
%attr(755,root,root) %{gstlibdir}/libgstaiff.so
%attr(755,root,root) %{gstlibdir}/libgstapexsink.so
%attr(755,root,root) %{gstlibdir}/libgstasfmux.so
%attr(755,root,root) %{gstlibdir}/libgstaudiovisualizers.so
%attr(755,root,root) %{gstlibdir}/libgstautoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstbayer.so
%attr(755,root,root) %{gstlibdir}/libgstbz2.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin2.so
%attr(755,root,root) %{gstlibdir}/libgstcdaudio.so
%attr(755,root,root) %{gstlibdir}/libgstcdxaparse.so
%attr(755,root,root) %{gstlibdir}/libgstcelt.so
%attr(755,root,root) %{gstlibdir}/libgstcog.so
%attr(755,root,root) %{gstlibdir}/libgstcoloreffects.so
%attr(755,root,root) %{gstlibdir}/libgstcolorspace.so
%attr(755,root,root) %{gstlibdir}/libgstcurl.so
%attr(755,root,root) %{gstlibdir}/libgstdataurisrc.so
%attr(755,root,root) %{gstlibdir}/libgstdc1394.so
%attr(755,root,root) %{gstlibdir}/libgstdccp.so
%attr(755,root,root) %{gstlibdir}/libgstdebugutilsbad.so
%attr(755,root,root) %{gstlibdir}/libgstdecklink.so
%attr(755,root,root) %{gstlibdir}/libgstdirac.so
%attr(755,root,root) %{gstlibdir}/libgstdtmf.so
%attr(755,root,root) %{gstlibdir}/libgstdtsdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvb.so
%attr(755,root,root) %{gstlibdir}/libgstdvbsuboverlay.so
%attr(755,root,root) %{gstlibdir}/libgstdvdspu.so
%attr(755,root,root) %{gstlibdir}/libgstfaac.so
%attr(755,root,root) %{gstlibdir}/libgstfaad.so
%attr(755,root,root) %{gstlibdir}/libgstfaceoverlay.so
%attr(755,root,root) %{gstlibdir}/libgstfbdevsink.so
%attr(755,root,root) %{gstlibdir}/libgstfestival.so
%attr(755,root,root) %{gstlibdir}/libgstfieldanalysis.so
%attr(755,root,root) %{gstlibdir}/libgstfragmented.so
%attr(755,root,root) %{gstlibdir}/libgstfreeverb.so
%attr(755,root,root) %{gstlibdir}/libgstfreeze.so
%attr(755,root,root) %{gstlibdir}/libgstfrei0r.so
%attr(755,root,root) %{gstlibdir}/libgstgaudieffects.so
%attr(755,root,root) %{gstlibdir}/libgstgeometrictransform.so
%attr(755,root,root) %{gstlibdir}/libgstgsettingselements.so
%attr(755,root,root) %{gstlibdir}/libgsth264parse.so
%attr(755,root,root) %{gstlibdir}/libgsthdvparse.so
%attr(755,root,root) %{gstlibdir}/libgstid3tag.so
%attr(755,root,root) %{gstlibdir}/libgstinter.so
%attr(755,root,root) %{gstlibdir}/libgstinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstivfparse.so
%attr(755,root,root) %{gstlibdir}/libgstjp2k.so
%attr(755,root,root) %{gstlibdir}/libgstjp2kdecimator.so
%attr(755,root,root) %{gstlibdir}/libgstjpegformat.so
%attr(755,root,root) %{gstlibdir}/libgstkate.so
%attr(755,root,root) %{gstlibdir}/libgstlegacyresample.so
%attr(755,root,root) %{gstlibdir}/libgstlinsys.so
%attr(755,root,root) %{gstlibdir}/libgstliveadder.so
%attr(755,root,root) %{gstlibdir}/libgstmms.so
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstmpeg2enc.so
%attr(755,root,root) %{gstlibdir}/libgstmpegdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegvideoparse.so
%attr(755,root,root) %{gstlibdir}/libgstmplex.so
%attr(755,root,root) %{gstlibdir}/libgstmusepack.so
%attr(755,root,root) %{gstlibdir}/libgstmve.so
%attr(755,root,root) %{gstlibdir}/libgstmxf.so
%attr(755,root,root) %{gstlibdir}/libgstneonhttpsrc.so
%attr(755,root,root) %{gstlibdir}/libgstnsf.so
%attr(755,root,root) %{gstlibdir}/libgstnuvdemux.so
%attr(755,root,root) %{gstlibdir}/libgstofa.so
%attr(755,root,root) %{gstlibdir}/libgstopenal.so
%attr(755,root,root) %{gstlibdir}/libgstpatchdetect.so
%attr(755,root,root) %{gstlibdir}/libgstpcapparse.so
%attr(755,root,root) %{gstlibdir}/libgstpnm.so
%attr(755,root,root) %{gstlibdir}/libgstrawparse.so
%attr(755,root,root) %{gstlibdir}/libgstreal.so
%attr(755,root,root) %{gstlibdir}/libgstremovesilence.so
%attr(755,root,root) %{gstlibdir}/libgstrfbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstrsvg.so
%attr(755,root,root) %{gstlibdir}/libgstrtpmux.so
%attr(755,root,root) %{gstlibdir}/libgstrtpvp8.so
%attr(755,root,root) %{gstlibdir}/libgstscaletempoplugin.so
%attr(755,root,root) %{gstlibdir}/libgstschro.so
%attr(755,root,root) %{gstlibdir}/libgstsdi.so
%attr(755,root,root) %{gstlibdir}/libgstsdl.so
%attr(755,root,root) %{gstlibdir}/libgstsdpelem.so
%attr(755,root,root) %{gstlibdir}/libgstsegmentclip.so
%attr(755,root,root) %{gstlibdir}/libgstshm.so
%attr(755,root,root) %{gstlibdir}/libgstsiren.so
%attr(755,root,root) %{gstlibdir}/libgstsmooth.so
%attr(755,root,root) %{gstlibdir}/libgstsndfile.so
%attr(755,root,root) %{gstlibdir}/libgstsoundtouch.so
%attr(755,root,root) %{gstlibdir}/libgstspeed.so
%attr(755,root,root) %{gstlibdir}/libgststereo.so
%attr(755,root,root) %{gstlibdir}/libgstsubenc.so
%attr(755,root,root) %{gstlibdir}/libgsttta.so
%attr(755,root,root) %{gstlibdir}/libgstvcdsrc.so
%attr(755,root,root) %{gstlibdir}/libgstvdpau.so
%attr(755,root,root) %{gstlibdir}/libgstvideofiltersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideomaxrate.so
%attr(755,root,root) %{gstlibdir}/libgstvideomeasure.so
%attr(755,root,root) %{gstlibdir}/libgstvideoparsersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideosignal.so
%attr(755,root,root) %{gstlibdir}/libgstvmnc.so
%attr(755,root,root) %{gstlibdir}/libgstvoaacenc.so
%attr(755,root,root) %{gstlibdir}/libgstvp8.so
%attr(755,root,root) %{gstlibdir}/libgstxvid.so
%attr(755,root,root) %{gstlibdir}/libgsty4mdec.so
%attr(755,root,root) %{gstlibdir}/libresindvd.so

%{_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gstreamer-0.10/gst/basecamerabinsrc
%{_includedir}/gstreamer-0.10/gst/codecparsers
%{_includedir}/gstreamer-0.10/gst/interfaces/photography-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/interfaces/photography.h
%{_includedir}/gstreamer-0.10/gst/signalprocessor
%{_includedir}/gstreamer-0.10/gst/vdpau
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideocodec.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideodecoder.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoencoder.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoutils.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoutils.h
%{_includedir}/gstreamer-0.10/gst/video/gstsurfacebuffer.h
%{_includedir}/gstreamer-0.10/gst/video/gstsurfaceconverter.h
%{_includedir}/gstreamer-0.10/gst/video/videocontext.h
%{_pkgconfigdir}/gstreamer-basevideo-0.10.pc
%{_pkgconfigdir}/gstreamer-codecparsers-0.10.pc
%{_pkgconfigdir}/gstreamer-plugins-bad-0.10.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-bad-libs-*

