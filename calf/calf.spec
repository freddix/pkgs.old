# main package broken:
# calfjackhost: Symbol `_ZTVN12calf_plugins16plugin_ctl_ifaceE' has different size in shared object, consider re-linking
# calfjackhost: Symbol `_ZTIN12calf_plugins16plugin_ctl_ifaceE' has different size in shared object, consider re-linking
# calfjackhost: symbol lookup error: calfjackhost: undefined symbol: _ZN12calf_plugins15plugin_registry8instanceEv

# lv2 plugins broken
# jalv.gtk: lv2gui.cpp:294: void* gui_instantiate(const _LV2UI_Descriptor*, const char*, const char*, void (*)(void*, uint32_t, uint32_t, uint32_t, const void*), void*, void**, const LV2_Feature* const*): Assertion `xml' failed.
# zsh: abort      jalv.gtk http://calf.sourceforge.net/plugins/Compressor

Summary:	Calf audio plugin pack
Name:		calf
# git f63124a88bff1c6444639e6969854e5ed162f24d
Version:	0.0.19
Release:	0.00000000000000000001
License:	GPL v2/LGPL
Group:		Applications/Sound
#Source0:	http://downloads.sourceforge.net/project/calf/calf/0.0.18.6/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	11a1086a85a99fc97c1ef275d94841ab
Patch0:		%{name}-desktop.patch
URL:		http://calf.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	fftw-devel
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	jack-audio-connection-kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standalone JACK wrapper for Calf plugins.

%package -n lv2-plugins-calf
Summary:	Calf audio plugin pack for LV2
Group:		Applications/Sound

%description -n lv2-plugins-calf
Calf audio plugin pack for LV2.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/calf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/manuals
%attr(755,root,root) %{_bindir}/calfjackhost
%dir %{_libdir}/calf
%attr(755,root,root) %{_libdir}/calf/calf.so
%{_datadir}/calf
%{_iconsdir}/hicolor/*/apps/calf*.png
%{_iconsdir}/hicolor/*/apps/calf*.svg
%{_desktopdir}/calf.desktop
%{_mandir}/man1/calfjackhost.1*
%{_mandir}/man7/calf.7*

%files -n lv2-plugins-calf
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/calf.lv2
%attr(755,root,root) %{_libdir}/lv2/calf.lv2/calf.so
%attr(755,root,root) %{_libdir}/lv2/calf.lv2/calflv2gui.so
%{_libdir}/lv2/calf.lv2/Compressor.ttl
%{_libdir}/lv2/calf.lv2/Filter.ttl
%{_libdir}/lv2/calf.lv2/Filterclavier.ttl
%{_libdir}/lv2/calf.lv2/Flanger.ttl
%{_libdir}/lv2/calf.lv2/Monosynth.ttl
%{_libdir}/lv2/calf.lv2/MultiChorus.ttl
%{_libdir}/lv2/calf.lv2/Organ.ttl
%{_libdir}/lv2/calf.lv2/Phaser.ttl
%{_libdir}/lv2/calf.lv2/Reverb.ttl
%{_libdir}/lv2/calf.lv2/RotarySpeaker.ttl
%{_libdir}/lv2/calf.lv2/VintageDelay.ttl
%{_libdir}/lv2/calf.lv2/manifest.ttl
%{_libdir}/lv2/calf.lv2/Analyzer.ttl
%{_libdir}/lv2/calf.lv2/BassEnhancer.ttl
%{_libdir}/lv2/calf.lv2/Deesser.ttl
%{_libdir}/lv2/calf.lv2/Equalizer12Band.ttl
%{_libdir}/lv2/calf.lv2/Equalizer5Band.ttl
%{_libdir}/lv2/calf.lv2/Equalizer8Band.ttl
%{_libdir}/lv2/calf.lv2/Exciter.ttl
%{_libdir}/lv2/calf.lv2/Gate.ttl
%{_libdir}/lv2/calf.lv2/Limiter.ttl
%{_libdir}/lv2/calf.lv2/MonoInput.ttl
%{_libdir}/lv2/calf.lv2/Multibandcompressor.ttl
%{_libdir}/lv2/calf.lv2/Multibandgate.ttl
%{_libdir}/lv2/calf.lv2/Multibandlimiter.ttl
%{_libdir}/lv2/calf.lv2/Pulsator.ttl
%{_libdir}/lv2/calf.lv2/Saturator.ttl
%{_libdir}/lv2/calf.lv2/Sidechaincompressor.ttl
%{_libdir}/lv2/calf.lv2/Sidechaingate.ttl
%{_libdir}/lv2/calf.lv2/StereoTools.ttl

