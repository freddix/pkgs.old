Summary:	Digital Audio Workstatiton
Name:		ardour
Version:	2.8.12
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	7c031892f53aeacf08a750fc320c79c5
BuildRequires:	aubio-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	gtkmm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libgnomecanvasmm-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	raptor-devel
BuildRequires:	rubberband-devel
BuildRequires:	scons
BuildRequires:	slv2-devel
BuildRequires:	vamp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digital Audio Workstation.

%prep
%setup -q

sed -i -e 's|soundtouch-1.0|soundtouch-1.4|g' SConstruct

%build
%{__scons} \
	ARCH="%{rpmcflags}"	\
	PREFIX=%{_prefix}	\
	SYSLIBS=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__scons} \
	DESTDIR=$RPM_BUILD_ROOT	\
	install

cat > $RPM_BUILD_ROOT%{_desktopdir}/ardour.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=ardour2
Icon=ardour2
Terminal=false
Name=Ardour
Comment=Digital Audio Workstation
Categories=GTK;Audio;AudioVideo;Sequencer;
EOF

install icons/icon/ardour_icon_tango_48px_blue.png $RPM_BUILD_ROOT%{_pixmapsdir}/ardour2.png

mv $RPM_BUILD_ROOT%{_datadir}/locale/{pt,pt_BR}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}

%find_lang gtk2_ardour
%find_lang libardour2
%find_lang libgtkmm2ext

cat {gtk2_ardour,libardour2,libgtkmm2ext}.lang > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/ardour2
%dir %{_libdir}/ardour2/engines
%dir %{_libdir}/ardour2/surfaces
%dir %{_libdir}/ardour2/vamp
%attr(755,root,root) %{_bindir}/ardour2
%attr(755,root,root) %{_libdir}/ardour2/ardour-%{version}
%attr(755,root,root) %{_libdir}/ardour2/engines/libclearlooks.so
%attr(755,root,root) %{_libdir}/ardour2/libardour.so
%attr(755,root,root) %{_libdir}/ardour2/libardour_cp.so
%attr(755,root,root) %{_libdir}/ardour2/libgtkmm2ext.so
%attr(755,root,root) %{_libdir}/ardour2/libmidi++.so
%attr(755,root,root) %{_libdir}/ardour2/libpbd.so
%attr(755,root,root) %{_libdir}/ardour2/librubberband.so
%attr(755,root,root) %{_libdir}/ardour2/libsoundtouch.so
%attr(755,root,root) %{_libdir}/ardour2/libvamphostsdk.so
%attr(755,root,root) %{_libdir}/ardour2/libvampsdk.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_genericmidi.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_mackie.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_powermate.so
%attr(755,root,root) %{_libdir}/ardour2/surfaces/libardour_tranzport.so
%attr(755,root,root) %{_libdir}/ardour2/vamp/libardourvampplugins.so

%{_datadir}/ardour2
%{_sysconfdir}/ardour2

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

