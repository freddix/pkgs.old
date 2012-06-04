# NOTE:
# for multi-user target tty1 is not enabled by default
#
# mkdir -p ${FS_DIR}/etc/systemd/system/getty.target.wants
# ln -sf /lib/systemd/system/getty@.service \
# 	${FS_DIR}/etc/systemd/system/getty.target.wants/getty@tty1.service
#
Summary:	A System and Service Manager
Name:		systemd
Version:	185
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Base
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz
# Source0-md5:	a7dbbf05986eb0d2c164ec8e570eb78f
Source10:	%{name}-locale.conf
Source11:	%{name}-loop.conf
Source12:	%{name}-sysctl.conf
Source13:	%{name}-vconsole.conf
Source14:	%{name}-os-release
Source15:	%{name}-timezone
Source16:	00-keyboard.conf
# for rescue target, borrowed from sysvinit
# to be removed after upgrade to util-linux-2.22
Source20:	sulogin.c
# udev stuff
Source30:	udev-65-permissions.rules
#
Patch0:		%{name}-freddix.patch
Patch1:		%{name}-machine_id_writable.patch
Patch2:		%{name}-use_kmsg.patch
URL:		http://www.freedesktop.org/wiki/Software/systemd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cryptsetup-devel
BuildRequires:	dbus-devel
BuildRequires:	docbook-style-xsl
BuildRequires:	kmod-devel
BuildRequires:	libcap-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	libxslt-progs
BuildRequires:	m4
BuildRequires:	pam-devel
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRequires:	vala
Requires(post,postun):	/sbin/ldconfig
Requires:       %{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-units = %{epoch}:%{version}-%{release}
Provides:	virtual(init-daemon)
Requires:	agetty
Requires:	dbus
Requires:	kbd
Requires:	kmod
Requires:	python-dbus
Requires:	terminus-font-console
Requires:	udev = %{epoch}:%{version}-%{release}
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	/lib

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
Requires:       %{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files for systemd libraries.

%package units
Summary:	Configuration files, directories and installation tool for systemd
Group:		Base
Requires(post):	coreutils

%description units
Basic configuration files, directories and installation tool for the
systemd system and service manager.

%package -n udev
Summary:	udev is the device manager for the Linux kernel.
Group:		Base
Requires:	udev-libs = %{epoch}:%{version}-%{release}

%description -n udev
udev is the device manager for the Linux kernel.

%package -n udev-libs
Summary:	Udev library
Group:		Libraries

%description -n udev-libs
Udev library.

%package -n udev-devel
Summary:	Header files for libvolume_id library
Group:		Development/Libraries
Requires:	udev-libs = %{epoch}:%{version}-%{release}

%description -n udev-devel
this is the package containing the header files for udev library.

%package -n udev-glib
Summary:	gudev library
Group:		Libraries
Requires:	udev-libs = %{epoch}:%{version}-%{release}

%description -n udev-glib
gudev library.

%package -n udev-glib-devel
Summary:	Header files for libvolume_id library
Group:		Development/Libraries
Requires:	udev-glib = %{epoch}:%{version}-%{release}

%description -n udev-glib-devel
This is the package containing the header files for gudev library.

%package -n udev-apidocs
Summary:	udev API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description -n udev-apidocs
udev API documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# build fix
sed -i -e '26d;' src/login/logind-inhibit.h

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
	--with-rootprefix=""
%{__make}

%{__cc} %{rpmcflags} %{rpmldflags} %{SOURCE20} -lcrypt -o sulogin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{udev/rules.d,X11/xorg.conf.d} \
	$RPM_BUILD_ROOT/sbin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

rm -f $RPM_BUILD_ROOT%{_npkgconfigdir}/systemd.pc
rm -f $RPM_BUILD_ROOT%{_libdir}/{*/,}*.la
rm -f $RPM_BUILD_ROOT/lib/*/*.la

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
install %{SOURCE16} $RPM_BUILD_ROOT/etc/X11/xorg.conf.d

install %{SOURCE30} $RPM_BUILD_ROOT/%{_lib}/udev/rules.d/65-permissions.rules

# required for rescue and emergency targets
install sulogin $RPM_BUILD_ROOT/sbin

ln -s ../lib/systemd/systemd $RPM_BUILD_ROOT/sbin/init
ln -s ../lib/systemd/systemd $RPM_BUILD_ROOT/bin/systemd

# compat with old stuff
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
/lib/systemd/systemd-random-seed save > /dev/null 2>&1 || :
/bin/systemctl daemon-reexec > /dev/null 2>&1 || :
/bin/systemctl start systemd-udev.service > /dev/null 2>&1 || :

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

%post	-n udev-libs -p /sbin/ldconfig
%postun	-n udev-libs -p /sbin/ldconfig

%post	-n udev-glib -p /sbin/ldconfig
%postun	-n udev-glib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc DISTRO_PORTING README TODO

%attr(755,root,root) /bin/journalctl
%attr(755,root,root) /bin/loginctl
%attr(755,root,root) /bin/systemd
%attr(755,root,root) /bin/systemd-ask-password
%attr(755,root,root) /bin/systemd-inhibit
%attr(755,root,root) /bin/systemd-machine-id-setup
%attr(755,root,root) /bin/systemd-notify
%attr(755,root,root) /bin/systemd-tty-ask-password-agent

%attr(755,root,root) %{_bindir}/systemd-analyze
%attr(755,root,root) %{_bindir}/systemd-cat
%attr(755,root,root) %{_bindir}/systemd-cgls
%attr(755,root,root) %{_bindir}/systemd-cgtop
%attr(755,root,root) %{_bindir}/systemd-nspawn
%attr(755,root,root) %{_bindir}/systemd-stdio-bridge
%attr(755,root,root) %{_bindir}/systemd-detect-virt
%attr(755,root,root) %{_bindir}/systemd-delta

%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-cryptsetup-generator
%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-fstab-generator
%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-getty-generator
%attr(755,root,root) /%{_lib}/systemd/system-generators/systemd-system-update-generator
%attr(755,root,root) /%{_lib}/systemd/systemd
%attr(755,root,root) /%{_lib}/systemd/systemd-*

%attr(755,root,root) /sbin/halt
%attr(755,root,root) /sbin/init
%attr(755,root,root) /sbin/poweroff
%attr(755,root,root) /sbin/reboot
%attr(755,root,root) /sbin/runlevel
%attr(755,root,root) /sbin/shutdown
%attr(755,root,root) /sbin/telinit

# rescue.service & emergency.service dependency
%attr(755,root,root) /sbin/sulogin

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/systemd/user.conf

%config(noreplace) %verify(not md5 mtime size) /etc/hostname
%config(noreplace) %verify(not md5 mtime size) /etc/locale.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modules-load.d/loop.conf
%config(noreplace) %verify(not md5 mtime size) /etc/os-release
%config(noreplace) %verify(not md5 mtime size) /etc/sysctl.d/sysctl.conf
%config(noreplace) %verify(not md5 mtime size) /etc/timezone
%config(noreplace) %verify(not md5 mtime size) /etc/vconsole.conf
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xorg.conf.d/00-keyboard.conf

%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info

%dir %{_datadir}/systemd
%dir %{_prefix}/lib/systemd
%dir %{_sysconfdir}/systemd
%dir /%{_lib}/systemd/system-generators
%dir /%{_lib}/systemd/system-shutdown
%dir /%{_lib}/systemd/user-generators

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

# ------------------------------------------

%files -n udev
%defattr(644,root,root,755)

# dirs
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%dir /%{_lib}/udev
%dir /%{_lib}/udev/keymaps
%dir /%{_lib}/udev/rules.d

%attr(755,root,root) %{_bindir}/udevadm
%attr(755,root,root) /%{_lib}/systemd/systemd-udevd

%attr(755,root,root) /%{_lib}/udev/accelerometer
%attr(755,root,root) /%{_lib}/udev/collect
%attr(755,root,root) /%{_lib}/udev/findkeyboards
%attr(755,root,root) /%{_lib}/udev/keyboard-force-release.sh
%attr(755,root,root) /%{_lib}/udev/keymap
%attr(755,root,root) /%{_lib}/udev/mtd_probe

%attr(755,root,root) /%{_lib}/udev/ata_id
%attr(755,root,root) /%{_lib}/udev/cdrom_id
%attr(755,root,root) /%{_lib}/udev/scsi_id
%attr(755,root,root) /%{_lib}/udev/v4l_id

# rules
/%{_lib}/udev/rules.d/42-usb-hid-pm.rules
/%{_lib}/udev/rules.d/50-udev-default.rules
/%{_lib}/udev/rules.d/60-cdrom_id.rules
/%{_lib}/udev/rules.d/60-persistent-alsa.rules
/%{_lib}/udev/rules.d/60-persistent-input.rules
/%{_lib}/udev/rules.d/60-persistent-serial.rules
/%{_lib}/udev/rules.d/60-persistent-storage-tape.rules
/%{_lib}/udev/rules.d/60-persistent-storage.rules
/%{_lib}/udev/rules.d/60-persistent-v4l.rules
/%{_lib}/udev/rules.d/61-accelerometer.rules
/%{_lib}/udev/rules.d/65-permissions.rules
/%{_lib}/udev/rules.d/70-power-switch.rules
/%{_lib}/udev/rules.d/75-net-description.rules
/%{_lib}/udev/rules.d/75-probe_mtd.rules
/%{_lib}/udev/rules.d/75-tty-description.rules
/%{_lib}/udev/rules.d/78-sound-card.rules
/%{_lib}/udev/rules.d/80-drivers.rules
/%{_lib}/udev/rules.d/95-keyboard-force-release.rules
/%{_lib}/udev/rules.d/95-keymap.rules
/%{_lib}/udev/rules.d/95-udev-late.rules

%{_sysconfdir}/udev/udev.conf

/%{_lib}/udev/keymaps/*

# systemd stuff
/%{_lib}/systemd/system/sockets.target.wants/systemd-udev-control.socket
/%{_lib}/systemd/system/sockets.target.wants/systemd-udev-kernel.socket
/%{_lib}/systemd/system/systemd-udev-control.socket
/%{_lib}/systemd/system/systemd-udev-kernel.socket
/%{_lib}/systemd/system/systemd-udev-settle.service
/%{_lib}/systemd/system/systemd-udev-trigger.service
/%{_lib}/systemd/system/systemd-udev.service

%{_mandir}/man7/*
%{_mandir}/man8/*

%files -n udev-libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libudev.so.?
%attr(755,root,root) /%{_lib}/libudev.so.*.*.*

%dev(c,1,3) %attr(666,root,root) /dev/null
%dev(c,1,5) %attr(666,root,root) /dev/zero
%dev(c,1,8) %attr(666,root,root) /dev/random
%dev(c,4,0) %attr(660,root,root) /dev/tty0
%dev(c,5,0) %attr(660,root,tty) /dev/tty
%dev(c,5,1) %attr(660,root,console) /dev/console

%files -n udev-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libudev.so
%{_datadir}/gir-1.0/GUdev-1.0.gir
%{_includedir}/libudev.h
%{_npkgconfigdir}/udev.pc
%{_pkgconfigdir}/libudev.pc

%files -n udev-glib
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libgudev-1.0.so.?
%attr(755,root,root) /%{_lib}/libgudev-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files -n udev-glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgudev-1.0.so
%{_includedir}/gudev-1.0
%{_pkgconfigdir}/gudev-1.0.pc

%if 0
%files -n udev-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gudev
%{_gtkdocdir}/libudev
%endif

