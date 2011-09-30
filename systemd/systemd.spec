Summary:	A System and Service Manager
Name:		systemd
Version:	36
Release:	1
License:	GPL v2+
Group:		Base
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.bz2
# Source0-md5:	e1213338efb697abc8215d9a66a7f082
Source10:	%{name}-locale.conf
Source11:	%{name}-loop.conf
Source12:	%{name}-sysctl.conf
Source13:	%{name}-vconsole.conf
Source14:	%{name}-os-release
Source15:	%{name}-timezone
Patch0:		%{name}-freddix.patch
Patch1:		%{name}-machine_id_writable.patch
URL:		http://www.freedesktop.org/wiki/Software/systemd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cryptsetup-devel
BuildRequires:	dbus-devel
BuildRequires:	docbook-style-xsl
BuildRequires:	libcap-devel
#BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	libxslt-progs
BuildRequires:	m4
BuildRequires:	pam-devel
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRequires:	vala
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-units = %{version}-%{release}
Provides:	virtual(init-daemon)
Requires:	agetty
Requires:	dbus
Requires:	kbd
Requires:	python-dbus
Requires:	terminus-font-console
Requires:	udev
Requires:	util-linux >= 2.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package units
Summary:	Configuration files, directories and installation tool for systemd
Group:		Base
Requires(post):	coreutils

%description units
Basic configuration files, directories and installation tool for the
systemd system and service manager.

%package gtk
Summary:	Graphical frontend for systemd
Group:		Base
Requires:	%{name} = %{version}-%{release}
Requires:	polkit

%description gtk
Graphical front-end for systemd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-audit		\
	--disable-gtk		\
	--disable-selinux	\
	--disable-silent-rules	\
	--disable-static	\
	--with-distro=freddix	\
	--with-rootdir=		\
	--with-udevrulesdir=/lib/udev/rules.d
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
	$RPM_BUILD_ROOT/sbin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

rm -f $RPM_BUILD_ROOT%{_npkgconfigdir}/systemd.pc

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/*.target.wants

# hugepages are controlled from kernel space
rm -f $RPM_BUILD_ROOT/lib/systemd/system/dev-hugepages.mount
rm -f $RPM_BUILD_ROOT/lib/systemd/system/sysinit.target.wants/dev-hugepages.automount
rm -f $RPM_BUILD_ROOT/lib/systemd/system/dev-hugepages.automount

touch $RPM_BUILD_ROOT%{_sysconfdir}/machine-id
touch $RPM_BUILD_ROOT%{_sysconfdir}/machine-info

# main system configuration
echo "freddix" > $RPM_BUILD_ROOT/etc/hostname
install %{SOURCE10} $RPM_BUILD_ROOT/etc/locale.conf
install %{SOURCE11} $RPM_BUILD_ROOT/etc/modules-load.d/loop.conf
install %{SOURCE12} $RPM_BUILD_ROOT/etc/sysctl.d/sysctl.conf
install %{SOURCE13} $RPM_BUILD_ROOT/etc/vconsole.conf
install %{SOURCE14} $RPM_BUILD_ROOT/etc/os-release
install %{SOURCE15} $RPM_BUILD_ROOT/etc/timezone

ln -s ../bin/systemd $RPM_BUILD_ROOT/sbin/init
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/reboot
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/halt
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/poweroff
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/shutdown
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/telinit
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/runlevel

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/bin/systemd-machine-id-setup > /dev/null 2>&1 || :
/bin/systemctl daemon-reexec > /dev/null 2>&1 || :

%post units
if [ "$1" = "1" ] ; then
    # And symlink what we found to the new-style default.target
    ln -sf "$target" %{_sysconfdir}/systemd/system/default.target > /dev/null 2>&1 || :
    /bin/systemctl enable getty@.service \
    systemd-readahead-collect.service \
    systemd-readahead-replay.service  \
    remote-fs.target > /dev/null 2>&1 || :
fi

%preun units
if [ "$1" = "0" ]; then
    /bin/systemctl disable getty@.service \
    systemd-readahead-collect.service \
    systemd-readahead-replay.service  \
    remote-fs.target > /dev/null 2>&1 || :
    rm -f %{_sysconfdir}/systemd/system/default.target > /dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ "$1" -ge "1" ] ; then
	/bin/systemctl daemon-reload > /dev/null 2>&1 || :
fi

%files
%defattr(644,root,root,755)
%doc DISTRO_PORTING README TODO

%attr(755,root,root) /bin/systemd
%attr(755,root,root) /bin/systemd-ask-password
%attr(755,root,root) /bin/systemd-loginctl
%attr(755,root,root) /bin/systemd-machine-id-setup
%attr(755,root,root) /bin/systemd-notify
%attr(755,root,root) /bin/systemd-tty-ask-password-agent

%attr(755,root,root) %{_bindir}/systemd-analyze
%attr(755,root,root) %{_bindir}/systemd-cgls
%attr(755,root,root) %{_bindir}/systemd-nspawn
%attr(755,root,root) %{_bindir}/systemd-stdio-bridge

%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-cryptsetup-generator
%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-getty-generator
%attr(755,root,root) /%{_lib}/systemd/systemd-*

%attr(755,root,root) %ghost %{_libdir}/libsystemd-daemon.so.?
%attr(755,root,root) %ghost %{_libdir}/libsystemd-login.so.?
%attr(755,root,root) %{_libdir}/libsystemd-daemon.so.*.*.*
%attr(755,root,root) %{_libdir}/libsystemd-login.so.*.*.*

%attr(755,root,root) /sbin/halt
%attr(755,root,root) /sbin/init
%attr(755,root,root) /sbin/poweroff
%attr(755,root,root) /sbin/reboot
%attr(755,root,root) /sbin/runlevel
%attr(755,root,root) /sbin/shutdown
%attr(755,root,root) /sbin/telinit

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/systemd-logind.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/user.conf

%config(noreplace) %verify(not md5 mtime size) /etc/hostname
%config(noreplace) %verify(not md5 mtime size) /etc/locale.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modules-load.d/loop.conf
%config(noreplace) %verify(not md5 mtime size) /etc/os-release
%config(noreplace) %verify(not md5 mtime size) /etc/sysctl.d/sysctl.conf
%config(noreplace) %verify(not md5 mtime size) /etc/timezone
%config(noreplace) %verify(not md5 mtime size) /etc/vconsole.conf

%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info

%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/user-generators
%dir %{_sysconfdir}/systemd
%dir /%{_lib}/systemd/system-generators
%dir /%{_lib}/systemd/system-shutdown

%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service

%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy

/etc/dbus-1/system.d/org.freedesktop.hostname1.conf
/etc/dbus-1/system.d/org.freedesktop.locale1.conf
/etc/dbus-1/system.d/org.freedesktop.systemd1.conf
/etc/dbus-1/system.d/org.freedesktop.timedate1.conf
/etc/dbus-1/system.d/org.freedesktop.login1.conf

/etc/xdg/systemd
/%{_lib}/udev/rules.d/70-uaccess.rules
/%{_lib}/udev/rules.d/71-seat.rules
/%{_lib}/udev/rules.d/73-seat-late.rules
/%{_lib}/udev/rules.d/99-systemd.rules
%{_prefix}/lib/systemd/user
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/x11.conf

%{_mandir}/man1/init.1
%{_mandir}/man1/systemadm.1.*
%{_mandir}/man1/systemd-ask-password.1*
%{_mandir}/man1/systemd-cgls.1*
%{_mandir}/man1/systemd-loginctl.1.*
%{_mandir}/man1/systemd-notify.1*
%{_mandir}/man1/systemd-nspawn.1*
%{_mandir}/man1/systemd.1*
%{_mandir}/man3/sd_booted.3*
%{_mandir}/man3/sd_is_fifo.3*
%{_mandir}/man3/sd_is_socket.3
%{_mandir}/man3/sd_is_socket_inet.3
%{_mandir}/man3/sd_is_socket_unix.3
%{_mandir}/man3/sd_listen_fds.3*
%{_mandir}/man3/sd_notify.3*
%{_mandir}/man3/sd_notifyf.3
%{_mandir}/man3/sd_readahead.3*
%{_mandir}/man5/binfmt.d.5*
%{_mandir}/man5/hostname.5*
%{_mandir}/man5/locale.conf.5*
%{_mandir}/man5/machine-id.5*
%{_mandir}/man5/machine-info.5*
%{_mandir}/man5/modules-load.d.5*
%{_mandir}/man5/os-release.5*
%{_mandir}/man5/sysctl.d.5*
%{_mandir}/man5/systemd-logind.conf.5.*
%{_mandir}/man5/systemd.automount.5*
%{_mandir}/man5/systemd.conf.5*
%{_mandir}/man5/systemd.device.5*
%{_mandir}/man5/systemd.exec.5*
%{_mandir}/man5/systemd.mount.5*
%{_mandir}/man5/systemd.path.5*
%{_mandir}/man5/systemd.service.5*
%{_mandir}/man5/systemd.snapshot.5*
%{_mandir}/man5/systemd.socket.5*
%{_mandir}/man5/systemd.swap.5*
%{_mandir}/man5/systemd.target.5*
%{_mandir}/man5/systemd.timer.5*
%{_mandir}/man5/systemd.unit.5*
%{_mandir}/man5/timezone.5*
%{_mandir}/man5/vconsole.conf.5*
%{_mandir}/man7/daemon.7*
%{_mandir}/man7/sd-daemon.7*
%{_mandir}/man7/sd-readahead.7*
%{_mandir}/man7/systemd.special.7*
%{_mandir}/man8/halt.8*
%{_mandir}/man8/poweroff.8
%{_mandir}/man8/reboot.8
%{_mandir}/man8/runlevel.8*
%{_mandir}/man8/shutdown.8*
%{_mandir}/man8/telinit.8*

%attr(755,root,root) /%{_lib}/security/pam_systemd.so
%{_mandir}/man8/pam_systemd.8*

%files units
%defattr(644,root,root,755)
%attr(755,root,root) /bin/systemctl
%attr(755,root,root) /bin/systemd-tmpfiles

%dir %{_prefix}/lib/binfmt.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/tmpfiles.d

%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/tmpfiles.d

%dir /%{_lib}/systemd
/%{_lib}/systemd/system

%{_mandir}/man1/systemctl.1*
%{_mandir}/man5/tmpfiles.d.5*
%{_mandir}/man8/systemd-tmpfiles.8*

%if 0
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/systemadm
%attr(755,root,root) %{_bindir}/systemd-gnome-ask-password-agent
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_mandir}/man1/systemadm.1*
%endif

