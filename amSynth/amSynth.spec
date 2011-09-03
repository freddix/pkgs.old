%define		pre	beta2

Summary:	Software synthesizer
Name:		amSynth
Version:	1.3
Release:	0.%{pre}.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://amsynth.googlecode.com/files/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	8b5df8c2f82a3abc6e0addbaf6cffc58
BuildRequires:	alsa-lib-devel
BuildRequires:	gtkmm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
amSynth is a software synth that provides a classic subtractive
synthesizer topology, with
- Dual oscillators with classic waveforms - sine / saw / square
  / noise
- 24 dB/oct low-pass resonant filter
- Independent ADSR envelopes for filter & amplitude
- LFO which can module the oscillators, filter, and amplitude
- Distortion effect
- Reverb

Currently it runs as a stand-alone application on Linux, supporting
OSS, ALSA and JACK for Audio / MIDI I/O.

%prep
%setup -qn %{name}-%{version}-%{pre}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/amsynth.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/amsynth.desktop
%{_pixmapsdir}/amsynth.png

