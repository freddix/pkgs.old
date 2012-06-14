Summary:	p2p VoIP application
Name:		skype
Version:	4.0.0.7
Release:	1
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	b57a3a5e178ae40fc96583b7c1851663
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
Requires:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*%{_bindir}/skype

%description
p2p VoIP application.

License requirement: The Software originates from Skype and use the
links and graphics as published and indicated on
<http://www.skype.com/go/redistribution/>.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{avatars,lang,sounds},%{_desktopdir}} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps \
	$RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install avatars/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/avatars
install icons/SkypeBlue_16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/skype.png
install icons/SkypeBlue_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/skype.png
install icons/SkypeBlue_48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/skype.png
install lang/skype_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
install skype.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

%find_lang %{name} --without-mo --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lang
%{_datadir}/%{name}/avatars
%{_datadir}/%{name}/sounds
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_sysconfdir}/dbus-1/system.d/skype.conf

