Summary:	A userspace implementation of devfs
Name:		udev
Version:	175
Release:	1
Epoch:		1
License:	GPL
Group:		Base
#Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/hotplug/%{name}-%{version}.tar.bz2
Source0:	http://people.freedesktop.org/~kay/udev/%{name}-%{version}.tar.bz2
# Source0-md5:	2fc9c1efcbde98e3d73ffee7a77aea47
Source1:	%{name}-65-permissions.rules
URL:		http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
BuildRequires:	device-mapper-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libusb-compat-devel
BuildRequires:	usbutils
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	coreutils
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Device manager for the Linux 2.6 kernel series.

%package libs
Summary:	Udev library
Group:		Libraries
Provides:	dev

%description libs
Udev library.

%package devel
Summary:	Header files for libvolume_id library
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
this is the package containing the header files for udev library.

%package glib
Summary:	gudev library
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description glib
gudev library.

%package glib-devel
Summary:	Header files for libvolume_id library
Group:		Development/Libraries
Requires:	%{name}-gir = %{epoch}:%{version}-%{release}
Requires:	%{name}-glib = %{epoch}:%{version}-%{release}

%description glib-devel
This is the package containing the header files for gudev library.

%package apidocs
Summary:	udev API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
udev API documentation.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	gobject-introspection-data

%description gir
GObject introspection data for udev.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules			\
	--disable-static			\
	--enable-logging			\
	--enable-shared				\
	--libexecdir=/lib/udev			\
	--with-html-dir=%{_gtkdocdir}		\
	--with-pci-ids-path=/etc/pci.ids	\
	--with-rootlibdir=/%{_lib}		\
	--with-systemdsystemunitdir=/lib/systemd/system	\
	--with-usb-ids-path=/etc/usb.ids	\
	--without-selinux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/%{_lib}/udev/rules.d/65-permissions.rules

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%doc extras/keymap/README.keymap.txt

# dirs
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%dir /%{_lib}/udev
%dir /%{_lib}/udev/keymaps
%dir /%{_lib}/udev/rules.d

%attr(755,root,root) %{_sbindir}/udevadm
%attr(755,root,root) /%{_lib}/udev/udevd

%attr(755,root,root) /%{_lib}/udev/accelerometer
%attr(755,root,root) /%{_lib}/udev/collect
%attr(755,root,root) /%{_lib}/udev/findkeyboards
%attr(755,root,root) /%{_lib}/udev/firmware
%attr(755,root,root) /%{_lib}/udev/keyboard-force-release.sh
%attr(755,root,root) /%{_lib}/udev/keymap
%attr(755,root,root) /%{_lib}/udev/mtd_probe
%attr(755,root,root) /%{_lib}/udev/pci-db
%attr(755,root,root) /%{_lib}/udev/usb-db

%attr(755,root,root) /%{_lib}/udev/ata_id
%attr(755,root,root) /%{_lib}/udev/cdrom_id
%attr(755,root,root) /%{_lib}/udev/scsi_id
%attr(755,root,root) /%{_lib}/udev/v4l_id

# rules
/%{_lib}/udev/rules.d/42-qemu-usb.rules
/%{_lib}/udev/rules.d/50-firmware.rules
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

# systemd
/%{_lib}/systemd/system/basic.target.wants/udev-trigger.service
/%{_lib}/systemd/system/basic.target.wants/udev.service
/%{_lib}/systemd/system/sockets.target.wants/udev-control.socket
/%{_lib}/systemd/system/sockets.target.wants/udev-kernel.socket
/%{_lib}/systemd/system/udev-control.socket
/%{_lib}/systemd/system/udev-kernel.socket
/%{_lib}/systemd/system/udev-settle.service
/%{_lib}/systemd/system/udev-trigger.service
/%{_lib}/systemd/system/udev.service

%{_mandir}/man7/*
%{_mandir}/man8/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libudev.so.?
%attr(755,root,root) /%{_lib}/libudev.so.*.*.*

%dev(c,1,3) %attr(666,root,root) /dev/null
%dev(c,1,5) %attr(666,root,root) /dev/zero
%dev(c,1,8) %attr(666,root,root) /dev/random
%dev(c,4,0) %attr(660,root,root) /dev/tty0
%dev(c,5,0) %attr(660,root,tty) /dev/tty
%dev(c,5,1) %attr(660,root,console) /dev/console

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libudev.so
%{_libdir}/libudev.la
%{_includedir}/libudev.h
%{_pkgconfigdir}/libudev.pc
%{_datadir}/gir-1.0/GUdev-1.0.gir

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libgudev-1.0.so.?
%attr(755,root,root) /%{_lib}/libgudev-1.0.so.*.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgudev-1.0.so
%{_libdir}/libgudev-1.0.la
%{_includedir}/gudev-1.0
%{_pkgconfigdir}/gudev-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gudev
%{_gtkdocdir}/libudev

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

