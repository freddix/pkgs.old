%define		gstname		gst-plugins-ugly
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.36

Summary:	Ugly GStreamer Streaming-media framework plugins
Name:		gstreamer-plugins-ugly
Version:	0.10.19
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{gstname}-%{version}.tar.bz2
# Source0-md5:	1d81c593e22a6cdf0f2b4f57eae93df2
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	orc-devel >= 0.4.5
BuildRequires:	pkg-config
#
BuildRequires:	a52dec-libs-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	opencore-amr-devel
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

%package apidocs
Summary:	gstreamer-plugins-ugly API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gstreamer-plugins-ugly API documentation.

%prep
%setup -q -n %{gstname}-%{version}

%build
%{__autopoint}
patch -p0 < common/gettext.patch
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang gst-plugins-ugly-0.10

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gst-plugins-ugly-0.10.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgsta52dec.so
%attr(755,root,root) %{gstlibdir}/libgstamrnb.so
%attr(755,root,root) %{gstlibdir}/libgstamrwbdec.so
%attr(755,root,root) %{gstlibdir}/libgstasf.so
%attr(755,root,root) %{gstlibdir}/libgstcdio.so
%attr(755,root,root) %{gstlibdir}/libgstdvdlpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvdread.so
%attr(755,root,root) %{gstlibdir}/libgstdvdsub.so
%attr(755,root,root) %{gstlibdir}/libgstiec958.so
%attr(755,root,root) %{gstlibdir}/libgstlame.so
%attr(755,root,root) %{gstlibdir}/libgstmad.so
%attr(755,root,root) %{gstlibdir}/libgstmpeg2dec.so
%attr(755,root,root) %{gstlibdir}/libgstmpegaudioparse.so
%attr(755,root,root) %{gstlibdir}/libgstmpegstream.so
%attr(755,root,root) %{gstlibdir}/libgstrmdemux.so
%attr(755,root,root) %{gstlibdir}/libgstx264.so

%{_datadir}/gstreamer-0.10/presets/GstAmrnbEnc.prs
%{_datadir}/gstreamer-0.10/presets/GstX264Enc.prs

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-ugly-plugins-*
%endif

