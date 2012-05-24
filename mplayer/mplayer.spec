%define		pre	rc5
%define		sname	MPlayer
%define		subver	rc5
%define		svnver	20120320
#
Summary:	Movie player
Name:		mplayer
Version:	1.0
Release:	5.%{subver}.%{svnver}.2
Epoch:		3
License:	GPL
Group:		Applications/Multimedia
#Source0:	ftp://ftp2.mplayerhq.hu/MPlayer/releases/%{sname}-%{version}%{pre}.tar.bz2
Source0:	%{name}-%{version}%{pre}-%{svnver}.tar.xz
# Source0-md5:	965ec593e1bca2036d2a97217c600661
Source1:	%{name}.desktop
Patch0:		%{name}-link.patch
URL:		http://www.mplayerhq.hu/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	dirac-devel
BuildRequires:	docbook-style-xsl
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libbluray-devel
BuildRequires:	libdca-devel
BuildRequires:	libdv-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libx264-devel
BuildRequires:	libxslt-progs
BuildRequires:	ncurses-devel
BuildRequires:	openal-soft-devel
BuildRequires:	opencore-amr-devel
BuildRequires:	openjpeg-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	schroedinger-devel
BuildRequires:	speex-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXv-devel
BuildRequires:	xorg-libXvMC-devel
BuildRequires:	xorg-libXxf86dga-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	xvidcore-devel
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires(post,postun):	desktop-file-utils
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

# internal ffmpeg:
# the asm code in cabac.h cannot be compiled with current gcc without
# -fomit-frame-pointer
%define		specflags	-fomit-frame-pointer

%description
MPlayer is a movie player.

%package common
Summary:	Configuration files and documentation for MPlayer
Group:		Applications/Multimedia

%description common
Configuration files, man page and HTML documentation for MPlayer.

%package -n mencoder
Summary:	MEncoder - a movie encoder for Linux
Group:		Applications/Multimedia
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description -n mencoder
MEncoder is a movie encoder for Linux and is a part of the MPlayer
package.

%prep
%setup -qn mplayer
%patch0 -p1

echo %{svnver} > VERSION

install -d ffmpeg

cp -f etc/codecs.conf etc/codecs.win32.conf

%build
CC="%{__cc}"
CFLAGS="%{rpmcflags}"
LDFLAGS="%{rpmldflags}"
export CC CFLAGS LDFLAGS

./configure \
	--confdir=%{_sysconfdir}/mplayer	\
	%if 0
	--disable-ffmpeg_a			\
	%endif
	--codecsdir=%{_libdir}/codecs		\
	--disable-aa				\
	--disable-arts				\
	--disable-caca				\
	--disable-dga1				\
	--disable-dga2				\
	--disable-directfb			\
	--disable-dxr3				\
	--disable-enca				\
	--disable-esd				\
	--disable-ggi				\
	--disable-gui				\
	--disable-libcdio			\
	--disable-lirc				\
	--disable-live				\
	--disable-mga				\
	--disable-ossaudio			\
	--disable-select			\
	--disable-smb				\
	--disable-svga				\
	--disable-tdfxfb			\
	--disable-xmga				\
	--enable-alsa				\
	--enable-bluray				\
	--enable-cdparanoia			\
	--enable-dvdnav				\
	--enable-dynamic-plugins		\
	--enable-fbdev				\
	--enable-gl				\
	--enable-pulse				\
	--enable-runtime-cpudetection		\
	--enable-sdl				\
	--enable-vm				\
	--enable-x11				\
	--enable-xv				\
	--enable-xvmc				\
	--language=en,de,pl			\
	--prefix=%{_prefix}			\
	--with-xvmclib=XvMCW			\
        --disable-nas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/mplayer}	\
	$RPM_BUILD_ROOT%{_datadir}/mplayer			\
	$RPM_BUILD_ROOT%{_desktopdir}				\
	$RPM_BUILD_ROOT%{_mandir}/man1				\
	$RPM_BUILD_ROOT%{_mandir}/{de,pl}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install mencoder $RPM_BUILD_ROOT%{_bindir}/mencoder
install mplayer $RPM_BUILD_ROOT%{_bindir}/mplayer

install DOCS/man/de/*.1 $RPM_BUILD_ROOT%{_mandir}/de/man1
install DOCS/man/en/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install DOCS/man/pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

cat etc/example.conf > etc/mplayer.conf

cat etc/example.conf > etc/mplayer.conf
cat << 'EOF' >> etc/mplayer.conf

[default]
fontconfig = yes
subcp = cp1250
font = "Droid Sans"

EOF

install etc/{codecs,mplayer,menu,input}.conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/mplayer

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mplayer*
%{_desktopdir}/*.desktop

%files -n mencoder
%defattr(644,root,root,755)
%doc DOCS/tech/encoding-guide.txt DOCS/tech/encoding-tips.txt
%doc DOCS/tech/swscaler_filters.txt DOCS/tech/swscaler_methods.txt
%doc DOCS/tech/colorspaces.txt
%attr(755,root,root) %{_bindir}/mencoder*

%files common
%defattr(644,root,root,755)
%doc etc/codecs.win32.conf
%doc AUTHORS Changelog README

%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.conf
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(pl) %{_mandir}/pl/man1/*

