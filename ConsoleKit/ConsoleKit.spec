Summary:	ConsoleKit for PolicyKit
Name:		ConsoleKit
Version:	0.4.5
Release:	5
License:	GPL v2+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/ConsoleKit/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	f2657f93761206922d558471a936fbc3
Source1:	%{name}-pam-console-compat.ck
Source2:	%{name}-tmpfiles.conf
Patch0:		%{name}-cleanup_console_tags.patch
Patch1:		%{name}-consolekit_park.patch
URL:		http://www.freedesktop.org/wiki/Software/ConsoleKit
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	xmlto
BuildRequires:	xorg-libX11-devel
Requires(post,postun):	/bin/systemctl
Requires(preun):	/bin/systemctl
Requires:	%{name}-libs = %{version}-%{release}
Requires:	polkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
ConsoleKit is a framework for defining and tracking users, login
sessions, and seats.

%package libs
Summary:	ConsoleKit library
License:	AFL v2.1 or GPL v2
Group:		Libraries

%description libs
ConsoleKit library.

%package devel
Summary:	Header files for ConsoleKit
License:	AFL v2.1 or GPL v2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ConsoleKit.

%package x11
Summary:	ConsoleKit x11 utilities
License:	AFL v2.1 or GPL v2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description x11
ConsoleKit x11 utilities.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules			\
	--enable-docbook-docs			\
	--enable-pam-module			\
	--with-pam-module-dir=/%{_lib}/security	\
	--with-systemdsystemunitdir=/%{_lib}/systemd/system
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.la

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/ConsoleKit/run-session.d
install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/tmpfiles.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post console-kit-daemon.service
if [ -f /var/log/ConsoleKit/history ]; then
    chmod a+r /var/log/ConsoleKit/history
fi

%preun
%systemd_post console-kit-daemon.service

%postun
%systemd_reload

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/dbus/ConsoleKit.html
%attr(755,root,root) %dir /var/log/ConsoleKit

%attr(755,root,root) %{_bindir}/ck-history
%attr(755,root,root) %{_bindir}/ck-launch-session
%attr(755,root,root) %{_bindir}/ck-list-sessions
%attr(755,root,root) %{_libdir}/ConsoleKit/scripts/*
%attr(755,root,root) %{_libexecdir}/ck-collect-session-info
%attr(755,root,root) %{_sbindir}/ck-log-system-restart
%attr(755,root,root) %{_sbindir}/ck-log-system-start
%attr(755,root,root) %{_sbindir}/ck-log-system-stop
%attr(755,root,root) %{_sbindir}/console-kit-daemon

%dir /%{_lib}/systemd/system/halt.target.wants
%dir /%{_lib}/systemd/system/kexec.target.wants
%dir /%{_lib}/systemd/system/poweroff.target.wants
%dir /%{_lib}/systemd/system/reboot.target.wants
/%{_lib}/systemd/system/basic.target.wants/console-kit-log-system-start.service
/%{_lib}/systemd/system/console-kit-daemon.service
/%{_lib}/systemd/system/console-kit-log-system-restart.service
/%{_lib}/systemd/system/console-kit-log-system-start.service
/%{_lib}/systemd/system/console-kit-log-system-stop.service
/%{_lib}/systemd/system/halt.target.wants/console-kit-log-system-stop.service
/%{_lib}/systemd/system/kexec.target.wants/console-kit-log-system-restart.service
/%{_lib}/systemd/system/poweroff.target.wants/console-kit-log-system-stop.service
/%{_lib}/systemd/system/reboot.target.wants/console-kit-log-system-restart.service

%attr(755,root,root) /%{_lib}/security/pam_ck_connector.so

%dir %{_libdir}/ConsoleKit
%dir %{_libdir}/ConsoleKit/run-seat.d
%dir %{_libdir}/ConsoleKit/run-session.d
%dir %{_libdir}/ConsoleKit/scripts

%dir %{_sysconfdir}/ConsoleKit
%dir %{_sysconfdir}/ConsoleKit/run-seat.d
%dir %{_sysconfdir}/ConsoleKit/run-session.d
%dir %{_sysconfdir}/ConsoleKit/seats.d

%attr(755,root,root) %{_libdir}/ConsoleKit/run-session.d/*.ck

%{_datadir}/dbus-1/system-services/org.freedesktop.ConsoleKit.service
%{_datadir}/polkit-1/actions/org.freedesktop.consolekit.policy
%{_mandir}/man8/pam_ck_connector*
%{_sysconfdir}/ConsoleKit/seats.d/00-primary.seat
%{_sysconfdir}/dbus-1/system.d/ConsoleKit.conf
/etc/tmpfiles.d/ConsoleKit.conf

%files libs
%defattr(644,root,root,755)
%dir %{_libexecdir}
%attr(755,root,root) %ghost %{_libdir}/libck-connector.so.?
%attr(755,root,root) %{_libdir}/libck-connector.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libck-connector.so
%dir %{_includedir}/ConsoleKit
%dir %{_includedir}/ConsoleKit/ck-connector
%{_includedir}/ConsoleKit/ck-connector/*.h
%{_pkgconfigdir}/ck-connector.pc
%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.Seat.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.Session.xml

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ck-get-x11-display-device
%attr(755,root,root) %{_libexecdir}/ck-get-x11-server-pid

