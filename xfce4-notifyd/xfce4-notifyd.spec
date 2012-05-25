Summary:	Xfce Notification Daemon
Name:		xfce4-notifyd
Version:	0.2.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-notifyd/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	8687fb7a0f270231ada265e363b6ffcc
URL:		http://goodies.xfce.org/projects/applications/xfce4-notifyd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Obsoletes:	xdg-desktop-notification-daemon
Provides:	xdg-desktop-notification-daemon
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce implementation of the Desktop Notifications Specification.

%prep
%setup -q
sed -i 's|pt_PT|pt|' configure.ac
mv po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/xfce4-notifyd-config
%dir %{_libdir}/xfce4/notifyd
%attr(755,root,root) %{_libdir}/xfce4/notifyd/xfce4-notifyd
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_desktopdir}/xfce4-notifyd-config.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-notifyd.png
%{_mandir}/man1/xfce4-notifyd-config.1*

%{_datadir}/themes/Default/xfce-notify-4.0
%{_datadir}/themes/Smoke
%{_datadir}/themes/ZOMG-PONIES!/


