Summary:	Flash plugin for Netscape-compatible WWW browsers
Name:		adobe-flash
Version:	11.1.102.55
Release:	1
License:	Free to use, non-distributable
Group:		X11/Applications/Multimedia
Source0:	http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/install_flash_player_11_linux.i386.tar.gz
# Source0-md5:	e9753df741e415c6d0707a2bf65f5940
URL:		http://www.adobe.com/products/flashplayer/
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/adobe
%define		_enable_debug_packages	0

%description
Adobe(R) Flash(R) Player is the high-performance, lightweight, highly
expressive client runtime that delivers powerful and consistent user
experiences across major operating systems, browsers, mobile phones,
and devices. Installed on over 700 million Internet-connected desktops
and mobile devices, Flash Player enables organizations and individuals
to build and deliver great digital experiences to their end users.

%prep
%setup -qTcb 0

%build
s=$(echo 'LNX %{version}' | tr . ,)
v=$(strings libflashplayer.so | grep '^LNX ')
if [ "$v" != "$s" ]; then
    : wrong version
    exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/browser-plugins,%{_iconsdir}}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/mms.cfg
# http://www.adobe.com/cfusion/knowledgebase/index.cfm?id=16701594
AutoUpdateDisable=1
AutoUpdateInterval=0
EOF

install *.so $RPM_BUILD_ROOT%{_libdir}/browser-plugins
install -D usr/bin/flash-player-properties $RPM_BUILD_ROOT%{_bindir}/flash-player-properties
install -D usr/share/applications/flash-player-properties.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/flash-player-properties.desktop
cp -a usr/share/icons/* $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mms.cfg
%attr(755,root,root) %{_bindir}/flash-player-properties
%attr(755,root,root) %{_libdir}/browser-plugins/*.so
%{_desktopdir}/flash-player-properties.desktop
%{_iconsdir}/hicolor/*/apps/*.png

