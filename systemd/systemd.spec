# NOTE:
# for multi-user target tty1 is not enabled by default
#
# mkdir -p ${FS_DIR}/etc/systemd/system/getty.target.wants
# ln -sf /lib/systemd/system/getty@.service \
# 	${FS_DIR}/etc/systemd/system/getty.target.wants/getty@tty1.service
#
Summary:	A System and Service Manager
Name:		systemd
Version:	44
Release:	1
License:	GPL v2+
Group:		Base
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz
# Source0-md5:	11f44ff74c87850064e4351518bcff17
Source10:	%{name}-locale.conf
Source11:	%{name}-loop.conf
Source12:	%{name}-sysctl.conf
Source13:	%{name}-vconsole.conf
Source14:	%{name}-os-release
Source15:	%{name}-timezone
# for rsyslog
Source20:	listen.conf
Patch0:		%{name}-freddix.patch
Patch1:		%{name}-machine_id_writable.patch
URL:		http://www.freedesktop.org/wiki/Software/systemd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cryptsetup-devel
BuildRequires:	dbus-devel
BuildRequires:	docbook-style-xsl
BuildRequires:	kmod-devel
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
Requires:       %{name}-libs = %{version}-%{release}
Requires:	%{name}-units = %{version}-%{release}
Provides:	virtual(init-daemon)
Requires:	agetty
Requires:	dbus
Requires:	kbd
Requires:	kmod
Requires:	python-dbus
Requires:	terminus-font-console
Requires:	udev
Requires:	util-linux
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

%package libs
Summary:        systemd libraries
Group:          Libraries

%description libs
systemd libraries.

%package devel
Summary:        Header files for systemd libraries
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Header files for systemd libraries.

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
	--with-rootlibdir=/%{_lib}	\
	--with-rootprefix=	\
	--with-udevrulesdir=/lib/udev/rules.d
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
	$RPM_BUILD_ROOT%{_sysconfdir}/rsyslog.d	\
	$RPM_BUILD_ROOT/sbin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

rm -f $RPM_BUILD_ROOT%{_npkgconfigdir}/systemd.pc

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/*.target.wants

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

install %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/rsyslog.d

install -d $RPM_BUILD_ROOT/sbin
ln -s ../lib/systemd/systemd $RPM_BUILD_ROOT/sbin/init
ln -s ../lib/systemd/systemd $RPM_BUILD_ROOT/bin/systemd

ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/halt
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/poweroff
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/reboot
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/runlevel
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/shutdown
ln -s ../bin/systemctl $RPM_BUILD_ROOT/sbin/telinit

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/systemd-machine-id-setup > /dev/null 2>&1 || :
/usr/lib/systemd/systemd-random-seed save > /dev/null 2>&1 || :
/bin/systemctl daemon-reexec > /dev/null 2>&1 || :

%post units
if [ "$1" = "1" ] ; then
    /bin/systemctl enable getty@.service \
    systemd-readahead-collect.service \
    systemd-readahead-replay.service  \
    remote-fs.target > /dev/null 2>&1 || :
    ln -sf /lib/systemd/system/multi-user.target \
    	/etc/systemd/system/default.target
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
if [ "$1" -ge "1" ] ; then
	/bin/systemctl daemon-reload > /dev/null 2>&1 || :
	/bin/systemctl try-restart systemd-logind.service >/dev/null 2>&1 || :
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc DISTRO_PORTING README TODO

%attr(755,root,root) /bin/systemd
%attr(755,root,root) /bin/systemd-journalctl
%attr(755,root,root) /bin/systemd-ask-password
%attr(755,root,root) /bin/systemd-loginctl
%attr(755,root,root) /bin/systemd-machine-id-setup
%attr(755,root,root) /bin/systemd-notify
%attr(755,root,root) /bin/systemd-tty-ask-password-agent

%attr(755,root,root) %{_bindir}/systemd-analyze
%attr(755,root,root) %{_bindir}/systemd-cat
%attr(755,root,root) %{_bindir}/systemd-cgls
%attr(755,root,root) %{_bindir}/systemd-cgtop
%attr(755,root,root) %{_bindir}/systemd-nspawn
%attr(755,root,root) %{_bindir}/systemd-stdio-bridge

%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-cryptsetup-generator
%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-getty-generator
%attr(755,root,root) /%{_lib}/systemd/systemd-*
%attr(755,root,root) /%{_lib}/systemd/systemd

%attr(755,root,root) /sbin/halt
%attr(755,root,root) /sbin/init
%attr(755,root,root) /sbin/poweroff
%attr(755,root,root) /sbin/reboot
%attr(755,root,root) /sbin/runlevel
%attr(755,root,root) /sbin/shutdown
%attr(755,root,root) /sbin/telinit

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/systemd-journald.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/systemd-logind.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/user.conf
%{_sysconfdir}/rsyslog.d/listen.conf

%config(noreplace) %verify(not md5 mtime size) /etc/hostname
%config(noreplace) %verify(not md5 mtime size) /etc/locale.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modules-load.d/loop.conf
%config(noreplace) %verify(not md5 mtime size) /etc/os-release
%config(noreplace) %verify(not md5 mtime size) /etc/sysctl.d/sysctl.conf
%config(noreplace) %verify(not md5 mtime size) /etc/timezone
%config(noreplace) %verify(not md5 mtime size) /etc/vconsole.conf

%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info

%dir %{_datadir}/systemd
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/user-generators
%dir %{_sysconfdir}/systemd
%dir /%{_lib}/systemd/system-generators
%dir /%{_lib}/systemd/system-shutdown

%{_datadir}/systemd/kbd-model-map

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
%{_prefix}/lib/sysctl.d/coredump.conf

%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*
%exclude %{_mandir}/man1/systemctl.1*
%exclude %{_mandir}/man5/tmpfiles.d.5*
%exclude %{_mandir}/man8/systemd-tmpfiles.8*

%attr(755,root,root) /%{_lib}/security/pam_systemd.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libsystemd-daemon.so.?
%attr(755,root,root) %ghost /%{_lib}/libsystemd-id128.so.?
%attr(755,root,root) %ghost /%{_lib}/libsystemd-journal.so.?
%attr(755,root,root) %ghost /%{_lib}/libsystemd-login.so.?
%attr(755,root,root) /%{_lib}/libsystemd-daemon.so.*.*.*
%attr(755,root,root) /%{_lib}/libsystemd-id128.so.*.*.*
%attr(755,root,root) /%{_lib}/libsystemd-journal.so.*.*.*
%attr(755,root,root) /%{_lib}/libsystemd-login.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsystemd-*.so
%{_datadir}/dbus-1/interfaces/*.xml
%{_includedir}/systemd
%{_pkgconfigdir}/libsystemd-*.pc
%{_mandir}/man3/*.3*

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

