%define		shiki_ver	4.6
#
Summary:	GNOME Colors icon theme
Name:		gnome-theme-colors
Version:	5.5.1
Release:	6
License:	GPL v2
Group:		X11/Amusements
Source0:	http://gnome-colors.googlecode.com/files/gnome-colors-%{version}.tar.gz
# Source0-md5:	8ec81b556bac351817bd56a1701dbbfb
Source1:	http://gnome-colors.googlecode.com/files/gnome-colors-extras-%{version}.tar.gz
# Source1-md5:	02132ab0483c54a45ac49df22f90c163
Source2:	http://gnome-colors.googlecode.com/files/shiki-colors-murrine-%{shiki_ver}.tar.gz
# Source2-md5:	27dba036c2274784190b4d1bbb68120c
Source3:	http://www.deviantart.com/download/149966599/Shiki_Colors_for_Openbox_by_jmcknight.gz
# Source3-md5:	9bfdc470810ef2b72e107d7edae86661
Patch0:		%{name}-gradients.patch
URL:		http://code.google.com/p/gnome-colors/
BuildRequires:  gtk+
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
%define		_noautostrip	.*%{_iconsdir}/.*
%define		_noautochrpath	.*%{_iconsdir}/.*

%description
This is a set of icon themes based on GNOME, with some
inspiration/icons from Tango, Elementary, Discovery, Tango
Generator and others.

%package brave
Summary:	Brave icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description brave
Brave icon theme, a part of GNOME Colors icon theme.

%package carbonite
Summary:	Carbonite icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description carbonite
Carbonite icon theme, a part of GNOME Colors icon theme.

%package dust
Summary:	Dust icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description dust
Dust icon theme, a part of GNOME Colors icon theme.

%package human
Summary:	Human icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description human
Human icon theme, a part of GNOME Colors icon theme.

%package illustrious
Summary:	Illustrious  icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description illustrious
Illustrious  icon theme, a part of GNOME Colors icon theme.

%package noble
Summary:	Noble icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description noble
Noble icon theme, a part of GNOME Colors icon theme.

%package tribute
Summary:	Tribute icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description tribute
Tribute icon theme, a part of GNOME Colors icon theme.

%package wine
Summary:	Wine icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%description wine
Wine icon theme, a part of GNOME Colors icon theme.

%package wise
Summary:	Wise icon theme
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-icon-theme

%package -n metacity-theme-shiki-colors
Summary:	Shiki Colors for Metacity
Group:		Themes

%description -n metacity-theme-shiki-colors
Shiki Colors for Metacity.

%package -n xfwm4-theme-shiki-colors
Summary:	Shiki Colors for XFWM4
Group:		Themes

%description -n xfwm4-theme-shiki-colors
Shiki Colors for Metacity.

%description wise
Wise icon theme, a part of GNOME Colors icon theme.

%package -n gtk-theme-murrine-brave
Summary:	Brave theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-brave
Murrine Brave GTK+ theme.

%package -n gtk-theme-murrine-dust
Summary:	Dust theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-dust
Murrine Dust GTK+ theme.

%package -n gtk-theme-murrine-human
Summary:	Human theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-human
Murrine Human GTK+ theme.

%package -n gtk-theme-murrine-illustrious
Summary:	Illustrious theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-illustrious
Murrine Illustrious GTK+ theme.

%package -n gtk-theme-murrine-noble
Summary:	Noble theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-noble
Murrine Noble GTK+ theme.

%package -n gtk-theme-murrine-wine
Summary:	Wine theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-wine
Murrine Wine GTK+ theme.

%package -n gtk-theme-murrine-wise
Summary:	Wise theme for Murrine
Group:		Themes
Requires:	gtk-theme-engine-murrine

%description -n gtk-theme-murrine-wise
Murrine Wise GTK+ theme.

%package -n openbox-theme-colors
Summary:	Openbox themes
Group:		Themes
Requires:	openbox

%description -n openbox-theme-colors
"Colors" themes for openbox.

%prep
%setup -qc -a1 -a2 -a3
%patch0 -p1

sed -i 's|bg_pixmap|# bg_pixmap|' Shiki-*/gtk-2.0/panel.rc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome-{brave,carbonite,dust,human,illustrious,noble,tribute,wine,wise} \
	$RPM_BUILD_ROOT%{_datadir}/themes/Shiki-{Brave,Dust,Human,Illustrious,Noble,Wine,Wise} \

for theme in brave carbonite colors-common dust illustrious human noble tribute wine wise
do
	cp -ar gnome-${theme} $RPM_BUILD_ROOT%{_iconsdir}
	gtk-update-icon-cache -f $RPM_BUILD_ROOT%{_iconsdir}/gnome-${theme}
done

for theme in Brave Colors-* Dust Human Illustrious Noble Wine Wise
do
	cp -ar Shiki-${theme} $RPM_BUILD_ROOT%{_datadir}/themes
done

rm -f $RPM_BUILD_ROOT%{_datadir}/themes/*/index.theme
find $RPM_BUILD_ROOT%{_datadir}/themes -name "*~" -exec rm {} \;

mv $RPM_BUILD_ROOT%{_datadir}/themes/{Shiki-Colors-Easy-Metacity,Shiki-Colors-Easy}
mv $RPM_BUILD_ROOT%{_datadir}/themes/{Shiki-Colors-Metacity,Shiki-Colors}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_iconsdir}/gnome-colors-common
%dir %{_datadir}/themes/Shiki-Brave
%dir %{_datadir}/themes/Shiki-Colors
%dir %{_datadir}/themes/Shiki-Colors-Easy
%dir %{_datadir}/themes/Shiki-Dust
%dir %{_datadir}/themes/Shiki-Human
%dir %{_datadir}/themes/Shiki-Illustrious
%dir %{_datadir}/themes/Shiki-Noble
%dir %{_datadir}/themes/Shiki-Wine
%dir %{_datadir}/themes/Shiki-Wise

%files brave
%defattr(644,root,root,755)
%{_iconsdir}/gnome-brave

%files carbonite
%defattr(644,root,root,755)
%{_iconsdir}/gnome-carbonite

%files dust
%defattr(644,root,root,755)
%{_iconsdir}/gnome-dust

%files human
%defattr(644,root,root,755)
%{_iconsdir}/gnome-human

%files illustrious
%defattr(644,root,root,755)
%{_iconsdir}/gnome-illustrious

%files noble
%defattr(644,root,root,755)
%{_iconsdir}/gnome-noble

%files tribute
%defattr(644,root,root,755)
%{_iconsdir}/gnome-tribute

%files wine
%defattr(644,root,root,755)
%{_iconsdir}/gnome-wine

%files wise
%defattr(644,root,root,755)
%{_iconsdir}/gnome-wise

%files -n metacity-theme-shiki-colors
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Colors-Easy/metacity-1
%{_datadir}/themes/Shiki-Colors-Striped-Metacity
%{_datadir}/themes/Shiki-Colors/metacity-1
%{_datadir}/themes/Shiki-Dust/metacity-1

%files -n xfwm4-theme-shiki-colors
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Colors-Easy/xfwm4
%{_datadir}/themes/Shiki-Colors/xfwm4
%{_datadir}/themes/Shiki-Dust/xfwm4

%files -n gtk-theme-murrine-brave
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Brave/gtk-2.0

%files -n gtk-theme-murrine-dust
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Dust/gtk-2.0

%files -n gtk-theme-murrine-human
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Human/gtk-2.0

%files -n gtk-theme-murrine-illustrious
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Illustrious/gtk-2.0

%files -n gtk-theme-murrine-noble
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Noble/gtk-2.0

%files -n gtk-theme-murrine-wine
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Wine/gtk-2.0

%files -n gtk-theme-murrine-wise
%defattr(644,root,root,755)
%{_datadir}/themes/Shiki-Wise/gtk-2.0

%files -n openbox-theme-colors
%defattr(644,root,root,755)
%{_datadir}/themes/*/openbox-3

