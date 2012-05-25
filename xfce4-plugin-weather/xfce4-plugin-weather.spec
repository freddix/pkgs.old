%define		org_name	xfce4-weather-plugin

Summary:	Weather plugin for XFCE panel
Name:		xfce4-plugin-weather
Version:	0.7.4
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/0.7/%{org_name}-%{version}.tar.bz2
# Source0-md5:	03c972d13eba5cd226432ff66e3ff282
Patch0:		%{name}-xfce4ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/weather
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel
Requires(post,postun):	gdk-pixbuf
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Weather plugin for XFCE panel.

%prep
%setup -qn %{org_name}-%{version}
%patch0 -p1

%build
%{__intltoolize}
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

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/%{org_name}
%{_datadir}/xfce4/panel-plugins/weather.desktop
%{_datadir}/xfce4/weather
%{_iconsdir}/hicolor/*/*/xfce4-weather.png

