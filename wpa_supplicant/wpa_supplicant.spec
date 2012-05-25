%bcond_without	gui

Summary:	Linux WPA/WPA2/RSN/IEEE 802.1X supplicant
Name:		wpa_supplicant
Version:	0.7.3
Release:	2
License:	GPL v2
Group:		Networking
Source0:	http://hostap.epitest.fi/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f516f191384a9a546e3f5145c08addda
Source1:	%{name}.config
Source2:	%{name}-tmpfiles.conf
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-nl.patch
Patch2:		%{name}-dbus.patch
Patch3:		%{name}-bss-changed-prop-notify.patch
URL:		http://hostap.epitest.fi/wpa_supplicant/
BuildRequires:	dbus-devel
BuildRequires:	libnl-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
%if %{with gui}
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wpa_supplicant is a WPA Supplicant with support for WPA and WPA2 (IEEE
802.11i / RSN). Supplicant is the IEEE 802.1X/WPA component that is
used in the client stations. It implements key negotiation with a WPA
Authenticator and it controls the roaming and IEEE 802.11
authentication/association of the wlan driver.

wpa_supplicant is designed to be a "daemon" program that runs in the
background and acts as the backend component controlling the wireless
connection. Support for separate frontend programs is included and an
example text-based frontend, wpa_cli, is included with wpa_supplicant.

Supported WPA/IEEE 802.11i features:
- WPA-PSK ("WPA-Personal")
- WPA with EAP (e.g., with RADIUS authentication server)
  ("WPA-Enterprise") (currently, EAP-TLS and EAP-PEAP/MSCHAPv2 are
  supported with an integrated IEEE 802.1X Supplicant; other EAP types
  may be used with an external program, Xsupplicant)
- key management for CCMP, TKIP, WEP104, WEP40
- RSN/WPA2 (IEEE 802.11i)

%package gui
Summary:	Linux WPA/WPA2/RSN/IEEE 802.1X supplicant GUI
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description gui
Linux WPA/WPA2/RSN/IEEE 802.1X supplicant GUI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

install %{SOURCE1} wpa_supplicant/.config

%build
CFLAGS="%{rpmcppflags} %{rpmcflags} `pkg-config --cflags libnl-3.0`"
export CFLAGS
%{__make} -C wpa_supplicant		\
	CC="%{__cc}"			\
	LDFLAGS="%{rpmldflags}"		\
	V=1

%if %{with gui}
cd wpa_supplicant/wpa_gui-qt4
qmake-qt4 -unix -o Makefile wpa_gui.pro
%{__make} \
	BINDIR="%{_bindir}"		\
	LIBDIR="%{_libdir}"		\
	CC="%{__cc}"			\
	LDFLAGS="%{rpmldflags}"		\
	OPTCFLAGS="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man{5,8},%{_bindir},/var/run/%{name}} \
	   $RPM_BUILD_ROOT{%{_sysconfdir}/dbus-1/system.d,%{_datadir}/dbus-1/system-services} \
	   $RPM_BUILD_ROOT/usr/lib/tmpfiles.d

%{__make} -C wpa_supplicant install \
	BINDIR="%{_sbindir}"		\
	LIBDIR="%{_libdir}"		\
	DESTDIR=$RPM_BUILD_ROOT

install wpa_supplicant/doc/docbook/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install wpa_supplicant/doc/docbook/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

install wpa_supplicant/dbus/dbus-wpa_supplicant.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d/wpa_supplicant.conf
install wpa_supplicant/dbus/*.service $RPM_BUILD_ROOT%{_datadir}/dbus-1/system-services

install -D wpa_supplicant/wpa_supplicant.conf $RPM_BUILD_ROOT%{_sysconfdir}/wpa_supplicant.conf

%if %{with gui}
install wpa_supplicant/wpa_gui-qt4/wpa_gui $RPM_BUILD_ROOT%{_bindir}
%endif

install %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wpa_supplicant/ChangeLog wpa_supplicant/README wpa_supplicant/eap_testing.txt wpa_supplicant/todo.txt
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/wpa_supplicant.conf
%{_datadir}/dbus-1/system-services/*.service
/usr/lib/tmpfiles.d/%{name}.conf
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

%if %{with gui}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wpa_gui
%endif

