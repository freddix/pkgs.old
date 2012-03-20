Summary:	Swiss Army knife of sound processing programs
Name:		sox
Version:	14.3.2
Release:	2
License:	GPL v2+ (sox), LGPL v2+ (libsox)
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/sox/%{name}-%{version}.tar.gz
# Source0-md5:	e9d35cf3b0f8878596e0b7c49f9e8302
Patch0:		%{name}-dyn.patch
Patch1:		%{name}-ffmpeg.patch
URL:		http://sox.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	ladspa-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libao-devel
BuildRequires:	libgomp-devel
BuildRequires:	libgsm-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmagic-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	opencore-amr-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	wavpack-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SoX is a cross-platform (Windows, Linux, MacOS X, etc.) command line
utility that can convert various formats of computer audio files in to
other formats. It can also apply various effects to these sound files,
and, as an added bonus, SoX can play and record audio files on most
platforms.

%package libs
Summary:	SoX sound library
Group:		Development/Libraries

%description libs
SoX sound library.

%package devel
Summary:	Header files for the SoX sound file format converter library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the header files needed for compiling
applications which will use the SoX sound file format converter.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--with-distro='Freddix'	\
	--with-dyn-default	\
	--with-lpc10=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{play,rec}.1
echo '.so sox.1' > $RPM_BUILD_ROOT%{_mandir}/man1/play.1
echo '.so sox.1' > $RPM_BUILD_ROOT%{_mandir}/man1/rec.1

%{__rm} $RPM_BUILD_ROOT%{_libdir}/sox/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not GPL/LGPL texts
%doc AUTHORS COPYING ChangeLog README src/monkey.*
%attr(755,root,root) %{_bindir}/play
%attr(755,root,root) %{_bindir}/rec
%attr(755,root,root) %{_bindir}/sox
%attr(755,root,root) %{_bindir}/soxi
%dir %{_libdir}/sox
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_alsa.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_ao.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_flac.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_gsm.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_pulseaudio.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_sndfile.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_caf.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_fap.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_mat4.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_mat5.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_oss.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_paf.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_pvf.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_sd2.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_w64.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_xi.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_vorbis.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_wavpack.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_amr_nb.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_amr_wb.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_ffmpeg.so
%attr(755,root,root) %{_libdir}/sox/libsox_fmt_mp3.so
%{_mandir}/man1/play.1*
%{_mandir}/man1/rec.1*
%{_mandir}/man1/sox.1*
%{_mandir}/man1/soxi.1*
%{_mandir}/man7/soxeffect.7*
%{_mandir}/man7/soxformat.7*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsox.so.?
%attr(755,root,root) %{_libdir}/libsox.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsox.so
%{_libdir}/libsox.la
%{_includedir}/sox.h
%{_includedir}/soxstdint.h
%{_pkgconfigdir}/sox.pc
%{_mandir}/man3/libsox.3*

