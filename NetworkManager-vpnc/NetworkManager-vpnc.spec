Summary:	NetworkManager VPN integration for vpnc
Name:		NetworkManager-vpnc
Version:	0.8.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/NetworkManager-vpnc/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	3f6bd06c1056dc1275dd303f52a00a15
Patch0:		%{name}-binary_path.patch
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires:	NetworkManager
Requires:	vpnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/NetworkManager

%description
NetworkManager VPN integration for vpnc.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
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

rm -f $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libexecdir}/nm-vpnc-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-vpnc-service
%attr(755,root,root) %{_libexecdir}/nm-vpnc-service-vpnc-helper
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpnc-properties.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf
%{_datadir}/gnome-vpn-properties/vpnc
#%{_desktopdir}/nm-vpnc.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name

