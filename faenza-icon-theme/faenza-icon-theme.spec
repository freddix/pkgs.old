Summary:	Icon theme for GNOME
Name:		faenza-icon-theme
Version:	1.1
Release:	1
License:	GPL v3
Group:		X11/Applications
URL:		http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:	https://faenza-icon-theme.googlecode.com/files/%{name}_%{version}.tar.gz
# Source0-md5:	a7385a92226a3b3ab3949952149fe3a3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and Gnome menu items. Four themes
are included to fit with light or dark themes/panels.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons

cp -a Faenza* $RPM_BUILD_ROOT%{_datadir}/icons

for f in Faenza*; do
    gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%{_iconsdir}/Faenza*

