Summary:	Default themes for GNOME environment
Name:		gnome-themes-standard
Version:	3.4.1
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	8395760f650776c5753f5c995d962472
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf
BuildRequires:	gettext-devel
BuildRequires:	gtk+-update-icon-cache
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	gnome-icon-theme >= 3.4.0
Requires:	gtk+3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME 3 environment.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

CD=`pwd`
cd $RPM_BUILD_ROOT%{_iconsdir}
for dir in *
    do
	gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
	done
cd $CD

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.so
%{_datadir}/themes/Adwaita
%{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrastInverse
%{_datadir}/themes/LowContrast
%{_datadir}/gnome-background-properties/adwaita.xml
%{_iconsdir}/Adwaita
%{_iconsdir}/HighContrast
%{_iconsdir}/HighContrastInverse
%{_iconsdir}/LowContrast

