Summary:	Plugins for Audacious media player
Name:		audacious-plugins
Version:	3.2.3
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# Source0-md5:	9645637fb108f4d5cc47e72d194c5574
URL:		http://audacious-media-player.org/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	audacious-devel >= %{version}
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	gtkglext-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libglade-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmtp-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	mpg123-libs-devel
BuildRequires:	neon-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	taglib-devel
BuildRequires:	wavpack-devel
Requires:	audacious
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Audacious media player.

%prep
%setup -qn %{name}-%{version}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	--disable-adplug	\
	--disable-modplug	\
	--disable-oss		\
	--disable-sid		\
	--enable-amidiplug	\
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/audacious/paranormal/Presets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/audacious/Skins
%dir %{_libdir}/audacious/Input/amidi-plug
%attr(755,root,root) %{_libdir}/audacious/Container/asx.so
%attr(755,root,root) %{_libdir}/audacious/Container/audpl.so
%attr(755,root,root) %{_libdir}/audacious/Container/m3u.so
%attr(755,root,root) %{_libdir}/audacious/Container/pls.so
%attr(755,root,root) %{_libdir}/audacious/Container/xspf.so

%attr(755,root,root) %{_libdir}/audacious/Effect/compressor.so
%attr(755,root,root) %{_libdir}/audacious/Effect/crossfade.so
%attr(755,root,root) %{_libdir}/audacious/Effect/crystalizer.so
%attr(755,root,root) %{_libdir}/audacious/Effect/echo.so
%attr(755,root,root) %{_libdir}/audacious/Effect/ladspa.so
%attr(755,root,root) %{_libdir}/audacious/Effect/mixer.so
%attr(755,root,root) %{_libdir}/audacious/Effect/resample.so
%attr(755,root,root) %{_libdir}/audacious/Effect/sndstretch.so
%attr(755,root,root) %{_libdir}/audacious/Effect/stereo.so
%attr(755,root,root) %{_libdir}/audacious/Effect/voice_removal.so

%attr(755,root,root) %{_libdir}/audacious/General/alarm.so
%attr(755,root,root) %{_libdir}/audacious/General/albumart.so
%attr(755,root,root) %{_libdir}/audacious/General/aosd.so
%attr(755,root,root) %{_libdir}/audacious/General/cd-menu-items.so
%attr(755,root,root) %{_libdir}/audacious/General/gnomeshortcuts.so
%attr(755,root,root) %{_libdir}/audacious/General/gtkui.so
%attr(755,root,root) %{_libdir}/audacious/General/hotkey.so
%attr(755,root,root) %{_libdir}/audacious/General/lyricwiki.so
%attr(755,root,root) %{_libdir}/audacious/General/mpris2.so
%attr(755,root,root) %{_libdir}/audacious/General/mtp_up.so
%attr(755,root,root) %{_libdir}/audacious/General/notify.so
%attr(755,root,root) %{_libdir}/audacious/General/scrobbler.so
%attr(755,root,root) %{_libdir}/audacious/General/search-tool.so
%attr(755,root,root) %{_libdir}/audacious/General/skins.so
%attr(755,root,root) %{_libdir}/audacious/General/song_change.so
%attr(755,root,root) %{_libdir}/audacious/General/statusicon.so

%attr(755,root,root) %{_libdir}/audacious/Input/aac.so
%attr(755,root,root) %{_libdir}/audacious/Input/amidi-plug.so
%attr(755,root,root) %{_libdir}/audacious/Input/amidi-plug/ap-alsa.so
%attr(755,root,root) %{_libdir}/audacious/Input/amidi-plug/ap-fluidsynth.so
%attr(755,root,root) %{_libdir}/audacious/Input/cdaudio-ng.so
%attr(755,root,root) %{_libdir}/audacious/Input/console.so
%attr(755,root,root) %{_libdir}/audacious/Input/ffaudio.so
%attr(755,root,root) %{_libdir}/audacious/Input/flacng.so
%attr(755,root,root) %{_libdir}/audacious/Input/madplug.so
%attr(755,root,root) %{_libdir}/audacious/Input/metronom.so
%attr(755,root,root) %{_libdir}/audacious/Input/psf2.so
%attr(755,root,root) %{_libdir}/audacious/Input/sndfile.so
%attr(755,root,root) %{_libdir}/audacious/Input/tonegen.so
%attr(755,root,root) %{_libdir}/audacious/Input/vorbis.so
%attr(755,root,root) %{_libdir}/audacious/Input/vtx.so
%attr(755,root,root) %{_libdir}/audacious/Input/wavpack.so
%attr(755,root,root) %{_libdir}/audacious/Input/xsf.so

%attr(755,root,root) %{_libdir}/audacious/Output/alsa.so
%attr(755,root,root) %{_libdir}/audacious/Output/filewriter.so
%attr(755,root,root) %{_libdir}/audacious/Output/jackout.so
%attr(755,root,root) %{_libdir}/audacious/Output/null.so
%attr(755,root,root) %{_libdir}/audacious/Output/pulse_audio.so
%attr(755,root,root) %{_libdir}/audacious/Output/sdlout.so

%attr(755,root,root) %{_libdir}/audacious/Transport/mms.so
%attr(755,root,root) %{_libdir}/audacious/Transport/neon.so
%attr(755,root,root) %{_libdir}/audacious/Transport/unix-io.so

%attr(755,root,root) %{_libdir}/audacious/Visualization/blur_scope.so
%attr(755,root,root) %{_libdir}/audacious/Visualization/cairo-spectrum.so

%{_datadir}/audacious/paranormal
%{_datadir}/audacious/ui

