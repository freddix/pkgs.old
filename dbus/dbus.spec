Summary:	D-BUS message bus
Name:		dbus
Version:	1.6.0
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://dbus.freedesktop.org/releases/dbus/%{name}-%{version}.tar.gz
# Source0-md5:	16dcae2dd0c76e398381601ac9acdec4
Source1:	%{name}-xinitrc.sh
Source2:	%{name}-tmpfiles.conf
Patch0:		%{name}-nolibs.patch
URL:		http://www.freedesktop.org/Software/dbus
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	sed >= 4.0
BuildRequires:	systemd-devel
BuildRequires:	xmlto
BuildRequires:	xorg-libX11-devel
Requires(post):	/bin/systemctl
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	/bin/systemctl
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(messagebus)
Provides:	user(messagebus)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}-1.0

%description
D-BUS is a system for sending messages between applications. It is
used both for the systemwide message bus service, and as a
per-user-login-session messaging facility.

%package xinit
Summary:	D-BUS xinit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-app-xinit

%description xinit
D-BUS xinit.

%package libs
Summary:	D-BUS libraries
Group:		Libraries

%description libs
D-BUS libraries.

%package devel
Summary:	Header files for D-BUS
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for D-BUS.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-asserts					\
	--disable-silent-rules					\
	--disable-static					\
	--disable-tests						\
	--enable-systemd					\
	--with-console-auth-dir=%{_localstatedir}/run/console/	\
	--with-system-pid-file=%{_localstatedir}/run/messagebus.pid	\
	--with-systemdsystemunitdir=/lib/systemd/system		\
	--with-xml=expat
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dbus-1/{interfaces,services} \
	$RPM_BUILD_ROOT/etc/{X11/xinit/xinitrc.d,profile.d,tmpfiles.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/00-start-message-bus.sh
install %{SOURCE2} $RPM_BUILD_ROOT/etc/tmpfiles.d/dbus.conf

rm -rf $RPM_BUILD_ROOT%{_docdir}/dbus/api

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 122 messagebus
%useradd -u 122 -d /usr/share/empty -s /bin/false -c "System message bus" -g messagebus messagebus

%post
export NORESTART="yes"
%systemd_post messagebus.service

%preun
%systemd_preun messagebus.service

%postun
if [ "$1" = "0" ]; then
	%userremove messagebus
	%groupremove messagebus
fi
%systemd_reload

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/session.d
%dir %{_sysconfdir}/dbus-1/system.d
%dir /var/lib/dbus

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/*.conf
/etc/tmpfiles.d/dbus.conf

%attr(4750,root,messagebus) %{_libexecdir}/dbus-daemon-launch-helper
%attr(755,root,root) %{_bindir}/dbus-cleanup-sockets
%attr(755,root,root) %{_bindir}/dbus-daemon
%attr(755,root,root) %{_bindir}/dbus-monitor
%attr(755,root,root) %{_bindir}/dbus-send
%attr(755,root,root) %{_bindir}/dbus-uuidgen

%dir /%{_lib}/systemd/system/dbus.target.wants
/%{_lib}/systemd/system/dbus.service
/%{_lib}/systemd/system/dbus.socket
/%{_lib}/systemd/system/dbus.target.wants/dbus.socket
/%{_lib}/systemd/system/multi-user.target.wants/dbus.service
/%{_lib}/systemd/system/sockets.target.wants/dbus.socket

%{_mandir}/man1/dbus-cleanup-sockets.1*
%{_mandir}/man1/dbus-daemon.1*
%{_mandir}/man1/dbus-launch.1*
%{_mandir}/man1/dbus-monitor.1*
%{_mandir}/man1/dbus-send.1*
%{_mandir}/man1/dbus-uuidgen.1*

%files xinit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbus-launch
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/00-start-message-bus.sh

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/TODO
%attr(755,root,root) %ghost %{_libdir}/libdbus-1.so.?
%attr(755,root,root) %{_libdir}/libdbus-1.so.*.*.*

%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/interfaces
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/dbus-1/system-services
%dir %{_libdir}/dbus-1.0

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,txt}
%attr(755,root,root) %{_libdir}/libdbus-1.so
%{_includedir}/dbus*
%{_libdir}/dbus-*/include
%{_pkgconfigdir}/dbus-1.pc

