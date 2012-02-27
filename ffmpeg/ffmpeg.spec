Summary:	Realtime audio/video encoder and streaming server
Name:		ffmpeg
Version:	0.7.11
Release:	1
License:	GPL with LGPL parts
Group:		Applications/Multimedia
Source0:	http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	fb3de74e8a92152698aba429435ab73c
URL:		http://ffmpeg.org/
BuildRequires:	SDL-devel
BuildRequires:	dirac-devel
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	flac-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libvpx-devel
BuildRequires:	libx264-devel
BuildRequires:	nasm
BuildRequires:	openjpeg-devel
BuildRequires:	perl-tools-pod
BuildRequires:	schroedinger-devel
BuildRequires:	speex-devel
BuildRequires:	texinfo
BuildRequires:	xvidcore-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
ffmpeg is a hyper fast realtime audio/video encoder and streaming
server. It can grab from a standard Video4Linux video source and
convert it into several file formats based on DCT/motion compensation
encoding. Sound is compressed in MPEG audio layer 2 or using an AC3
compatible stream.

%package libs
Summary:	ffmpeg libraries
Group:		Libraries

%description libs
This package contains ffmpeg shared libraries.

%package devel
Summary:	ffmpeg header files
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
ffmpeg header files.

%prep
%setup -q

sed -i -e 's|gsm/gsm.h|gsm.h|' configure libavcodec/libgsm.c

%build
# - it's not autoconf configure
./configure \
	--arch=%{_target_base_arch}	\
	--libdir=%{_libdir}		\
	--mandir=%{_mandir}		\
	--prefix=%{_prefix}		\
	--shlibdir=%{_libdir}		\
	--cc="%{__cc}"			\
	--extra-cflags="%{rpmcflags}"	\
	--extra-ldflags="%{rpmldflags}"	\
	--disable-debug			\
	--disable-ffplay		\
	--disable-ffserver		\
	--disable-static		\
	--disable-stripping		\
	--enable-gpl			\
	--enable-nonfree		\
	--enable-version3		\
	--enable-libdc1394		\
	--enable-libdirac		\
	--enable-libfaac		\
	--enable-libgsm			\
	--enable-libmp3lame		\
	--enable-libopencore-amrnb	\
	--enable-libopencore-amrwb	\
	--enable-libopenjpeg		\
	--enable-libschroedinger	\
	--enable-libspeex		\
	--enable-libtheora		\
	--enable-libvorbis		\
	--enable-libvpx			\
	--enable-libx264		\
	--enable-libxvid		\
	--enable-avfilter		\
	--enable-postproc		\
	--enable-pthreads		\
	--enable-runtime-cpudetect	\
	--enable-shared			\
	--enable-x11grab
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/RELEASE_NOTES doc/TODO
# BR tetex doc/*.html
%attr(755,root,root) %{_bindir}/ffmpeg
%attr(755,root,root) %{_bindir}/ffprobe

# BR tetex
#%{_mandir}/man1/ffmpeg.1*
#%{_mandir}/man1/ffprobe.1

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.??
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.??
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.?
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.??
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.??
%attr(755,root,root) %ghost %{_libdir}/libpostproc.so.??
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.?
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ffpreset

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavdevice.so
%attr(755,root,root) %{_libdir}/libavfilter.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%attr(755,root,root) %{_libdir}/libswscale.so
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libswscale
%{_pkgconfigdir}/*.pc

