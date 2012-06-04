%define		gstname		gst-ffmpeg
%define		gst_major_ver	0.10

Summary:	GStreamer Streaming-media framework plug-in using FFmpeg
Name:		gstreamer-ffmpeg
Version:	0.10.12
Release:	4
License:	GPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-ffmpeg/%{gstname}-%{version}.tar.bz2
# Source0-md5:	8507f33c56e6155a3d450dfe6de835a9
URL:		http://gstreamer.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	gstreamer-plugins-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

This plugin contains the FFmpeg codecs, containing codecs for most
popular multimedia formats.

%prep
%setup -qn %{gstname}-%{version}

sed -i -e 's|sleep 15||' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static 	\
	--with-system-ffmpeg
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstffmpeg.so
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstffmpegscale.so
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstpostproc.so

