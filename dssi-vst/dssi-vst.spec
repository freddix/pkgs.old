Summary:	DSSI adapter to run Windows VST plugins
Name:		dssi-vst
Version:	0.9.2
Release:	3
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	http://code.breakfastquay.com/attachments/download/10/%{name}-%{version}.tar.bz2
# Source0-md5:	5c569200571de76dac18be4eb6fbd9c8
URL:		http://breakfastquay.com/dssi-vst/
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	vst-plugins-sdk
BuildRequires:	wine-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dssi-vst is an adapter that allows users of Linux audio software
to take VST and VSTi audio effects and instrument plugins compiled
for Windows, and load them into native LADSPA or DSSI plugin hosts.
Plugins run at full speed for most audio processing, although their
user interfaces are slower because of the Windows emulation.

%prep
%setup -q

sed -i -e 's| -g3||g' Makefile

%build
%{__make} \
	CXXFLAGS="-I %{_includedir}/vst -Wall -fPIC %{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/{dssi/dssi-vst,ladspa}}

ln -sf dssi-vst-server.exe dssi-vst-server
ln -sf dssi-vst-scanner.exe dssi-vst-scanner

install dssi-vst-server.exe.so dssi-vst-scanner.exe.so dssi-vst_gui	\
	dssi-vst-server.exe dssi-vst-server dssi-vst-scanner.exe	\
	dssi-vst-scanner $RPM_BUILD_ROOT%{_libdir}/dssi/dssi-vst
install dssi-vst.so \
	$RPM_BUILD_ROOT%{_libdir}/dssi
install dssi-vst.so \
	$RPM_BUILD_ROOT%{_libdir}/ladspa
install vsthost \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vsthost
%dir %{_libdir}/dssi
%dir %{_libdir}/dssi/dssi-vst
%attr(755,root,root) %{_libdir}/dssi/dssi-vst.so
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst-scanner
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst-scanner.exe
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst-scanner.exe.so
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst-server
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst-server.exe
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst-server.exe.so
%attr(755,root,root) %{_libdir}/dssi/dssi-vst/dssi-vst_gui
%attr(755,root,root) %{_libdir}/ladspa/dssi-vst.so
