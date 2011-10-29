Summary:	PulseAudio Volume Control
Name:		pavucontrol
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/pavucontrol/%{name}-%{version}.tar.gz
# Source0-md5:	c8bcd9cfe005d884651e0e5510b8dd1b
URL:		http://0pointer.de/lennart/projects/pavucontrol/
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libglademm-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
Requires:	libcanberra-runtime
Requires:	pulseaudio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK+ based volume
control tool ("mixer") for the PulseAudio sound server. In contrast to
classic mixer tools this one allows you to control both the volume of
hardware devices and of each playback stream seperately.

%prep
%setup -q

%build
%configure \
	--disable-gtk3	\
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pavucontrol
%{_datadir}/pavucontrol
%{_desktopdir}/pavucontrol.desktop

