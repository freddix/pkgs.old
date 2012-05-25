%define		xfce_version	4.10.0
#
Summary:	Power manager for XFCE desktop
Name:		xfce4-power-manager
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	935599b7114b0a4b0e2c9a5d6c72524c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfconf-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	polkit
Requires:	upower
Requires:	xdg-desktop-notification-daemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Power manager for XFCE desktop.

%package -n xfce4-plugin-power-manager
Summary:	Power manager applets for Xfce panel
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	xfce4-panel

%description -n xfce4-plugin-power-manager
Power manager applets for Xfce panel.

%prep
%setup -qn %{name}-%{version}

%build
export CONFIG_SHELL=/bin/bash
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
bash %configure \
	--disable-static	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir="%{_datadir}/xfce4/help/%{name}"

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-power-manager
%attr(755,root,root) %{_bindir}/xfce4-power-information
%attr(755,root,root) %{_bindir}/xfce4-power-manager-settings
%attr(755,root,root) %{_sbindir}/xfpm-power-backlight-helper
%{_datadir}/polkit-1/actions/org.xfce.power.policy
/etc/xdg/autostart/xfce4-power-manager.desktop
%{_desktopdir}/%{name}-settings.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/xfce4-power-manager*.1*

%files -n xfce4-plugin-power-manager
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-brightness-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-brightness-plugin.desktop

