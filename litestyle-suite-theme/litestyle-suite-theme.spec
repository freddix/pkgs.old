Summary:	Litestyle suite
Name:		litestyle-suite-theme
Version:	0.2a
Release:	6
License:	GPL
Group:		Themes
Source0:	http://www.deviantart.com/download/148308075/Litestyle_suite_by_weakhead.zip
# Source0-md5:	47ba5a2d859c48aa8cbc9cbcc2b1bc91
URL:		http://weakhead.deviantart.com/gallery/#/d2gar8r
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
This is a set of icon themes based on GNOME, with some
inspiration/icons from Tango, Elementary, Discovery, Tango
Generator and others.

%package -n gtk-theme-litestyle
Summary:	GTK+ Litestyle themes
Group:		Themes
Requires:	gtk-engines
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-litestyle
Litestyle GTK+ themes.

%package -n openbox-theme-litestyle
Summary:	Openbox Litestyle themes
Group:		Themes
Requires:	openbox

%description -n openbox-theme-litestyle
Litestyle themes for openbox.

%package -n bmpanel2-theme-litestyle
Summary:	Bmpanel2 Litestyle themes
Group:		Themes
Requires:	bmpanel2

%description -n bmpanel2-theme-litestyle
Litestyle themes for bmpanel2.

%package -n metacity-theme-litestyle
Summary:	Metacity Litestyle theme
Group:		Themes
Requires:	metacity

%description -n metacity-theme-litestyle
Litestyle theme for Metacity.

%package -n xfwm4-theme-litestyle
Summary:	XFWM4 Litestyle theme
Group:		Themes
Requires:	xfwm4

%description -n xfwm4-theme-litestyle
Litestyle themes for XFWM4.

%prep
%setup -qc

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/themes,%{_datadir}/bmpanel2/themes}

cd "Litestyle suite"
cd "GTK and Openbox/Shiki range"
cp -aR * $RPM_BUILD_ROOT%{_datadir}/themes
cd ../"Watered-down range"
cp -aR * $RPM_BUILD_ROOT%{_datadir}/themes
cd ../../"XFWM4 and Metacity"
cp -aR * $RPM_BUILD_ROOT%{_datadir}/themes
cd ../"BMPanel2"
cd "Shiki range"
cp -aR * $RPM_BUILD_ROOT%{_datadir}/bmpanel2/themes
cd ../"Watered-down range"
cp -aR * $RPM_BUILD_ROOT%{_datadir}/bmpanel2/themes

sed -i -e "s|bottom|top|" `find $RPM_BUILD_ROOT%{_datadir}/bmpanel2/themes -name theme -print0 | xargs --null`

find $RPM_BUILD_ROOT%{_datadir}/themes -name "*~" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Litestyle
%dir %{_datadir}/themes/Litestyle-Brave
%dir %{_datadir}/themes/Litestyle-Brave_Dark
%dir %{_datadir}/themes/Litestyle-Caffeine
%dir %{_datadir}/themes/Litestyle-Caffeine_Dark
%dir %{_datadir}/themes/Litestyle-Dust
%dir %{_datadir}/themes/Litestyle-Dust_Dark
%dir %{_datadir}/themes/Litestyle-Gerbera
%dir %{_datadir}/themes/Litestyle-Gerbera_Dark
%dir %{_datadir}/themes/Litestyle-Grass
%dir %{_datadir}/themes/Litestyle-Grass_Dark
%dir %{_datadir}/themes/Litestyle-Human
%dir %{_datadir}/themes/Litestyle-Human_Dark
%dir %{_datadir}/themes/Litestyle-Illustrious
%dir %{_datadir}/themes/Litestyle-Illustrious_Dark
%dir %{_datadir}/themes/Litestyle-Mint
%dir %{_datadir}/themes/Litestyle-Mint_Dark
%dir %{_datadir}/themes/Litestyle-Noble
%dir %{_datadir}/themes/Litestyle-Noble_Dark
%dir %{_datadir}/themes/Litestyle-Orchid
%dir %{_datadir}/themes/Litestyle-Orchid_Dark
%dir %{_datadir}/themes/Litestyle-Sky
%dir %{_datadir}/themes/Litestyle-Sky_Dark
%dir %{_datadir}/themes/Litestyle-Wine
%dir %{_datadir}/themes/Litestyle-Wine_Dark
%dir %{_datadir}/themes/Litestyle-Wise
%dir %{_datadir}/themes/Litestyle-Wise_Dark

%files -n gtk-theme-litestyle
%defattr(644,root,root,755)
%{_datadir}/themes/Litestyle-Mint_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Mint/gtk-2.0
%{_datadir}/themes/Litestyle-Gerbera/gtk-2.0
%{_datadir}/themes/Litestyle-Gerbera_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Brave/gtk-2.0
%{_datadir}/themes/Litestyle-Caffeine/gtk-2.0
%{_datadir}/themes/Litestyle-Sky/gtk-2.0
%{_datadir}/themes/Litestyle-Grass_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Brave_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Orchid/gtk-2.0
%{_datadir}/themes/Litestyle-Caffeine_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Human_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Dust_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Wine_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Noble_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Orchid_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Dust/gtk-2.0
%{_datadir}/themes/Litestyle-Illustrious/gtk-2.0
%{_datadir}/themes/Litestyle-Sky_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Grass/gtk-2.0
%{_datadir}/themes/Litestyle-Human/gtk-2.0
%{_datadir}/themes/Litestyle-Noble/gtk-2.0
%{_datadir}/themes/Litestyle-Wine/gtk-2.0
%{_datadir}/themes/Litestyle-Illustrious_Dark/gtk-2.0
%{_datadir}/themes/Litestyle-Wise/gtk-2.0
%{_datadir}/themes/Litestyle-Wise_Dark/gtk-2.0

%files -n openbox-theme-litestyle
%defattr(644,root,root,755)
%{_datadir}/themes/Litestyle-Mint_Dark/openbox-3
%{_datadir}/themes/Litestyle-Mint/openbox-3
%{_datadir}/themes/Litestyle-Wise_Dark/openbox-3
%{_datadir}/themes/Litestyle-Gerbera/openbox-3
%{_datadir}/themes/Litestyle-Gerbera_Dark/openbox-3
%{_datadir}/themes/Litestyle-Brave/openbox-3
%{_datadir}/themes/Litestyle-Caffeine/openbox-3
%{_datadir}/themes/Litestyle-Sky/openbox-3
%{_datadir}/themes/Litestyle-Grass_Dark/openbox-3
%{_datadir}/themes/Litestyle-Brave_Dark/openbox-3
%{_datadir}/themes/Litestyle-Orchid/openbox-3
%{_datadir}/themes/Litestyle-Caffeine_Dark/openbox-3
%{_datadir}/themes/Litestyle-Human_Dark/openbox-3
%{_datadir}/themes/Litestyle-Dust_Dark/openbox-3
%{_datadir}/themes/Litestyle-Wine_Dark/openbox-3
%{_datadir}/themes/Litestyle-Noble_Dark/openbox-3
%{_datadir}/themes/Litestyle-Orchid_Dark/openbox-3
%{_datadir}/themes/Litestyle-Dust/openbox-3
%{_datadir}/themes/Litestyle-Illustrious/openbox-3
%{_datadir}/themes/Litestyle-Sky_Dark/openbox-3
%{_datadir}/themes/Litestyle-Grass/openbox-3
%{_datadir}/themes/Litestyle-Human/openbox-3
%{_datadir}/themes/Litestyle-Noble/openbox-3
%{_datadir}/themes/Litestyle-Wine/openbox-3
%{_datadir}/themes/Litestyle-Illustrious_Dark/openbox-3
%{_datadir}/themes/Litestyle-Wise/openbox-3

%files -n bmpanel2-theme-litestyle
%defattr(644,root,root,755)
%{_datadir}/bmpanel2/themes/Litestyle-Brave
%{_datadir}/bmpanel2/themes/Litestyle-Caffeine
%{_datadir}/bmpanel2/themes/Litestyle-Dust
%{_datadir}/bmpanel2/themes/Litestyle-Gerbera
%{_datadir}/bmpanel2/themes/Litestyle-Grass
%{_datadir}/bmpanel2/themes/Litestyle-Human
%{_datadir}/bmpanel2/themes/Litestyle-Illustrious
%{_datadir}/bmpanel2/themes/Litestyle-Mint
%{_datadir}/bmpanel2/themes/Litestyle-Noble
%{_datadir}/bmpanel2/themes/Litestyle-Orchid
%{_datadir}/bmpanel2/themes/Litestyle-Sky
%{_datadir}/bmpanel2/themes/Litestyle-Wine
%{_datadir}/bmpanel2/themes/Litestyle-Wise

%files -n metacity-theme-litestyle
%defattr(644,root,root,755)
%{_datadir}/themes/Litestyle/metacity-1

%files -n xfwm4-theme-litestyle
%defattr(644,root,root,755)
%{_datadir}/themes/Litestyle/xfwm4

