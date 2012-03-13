Summary:	Collection of basic system utilities for Linux
Name:		util-linux
Version:	2.21
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/util-linux/v2.21/%{name}-%{version}.tar.xz
# Source0-md5:	208aa058f4117759d2939d1be7d662fc
Source2:	%{name}-login.pamd
URL:		http://userweb.kernel.org/~kzak/util-linux-ng/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	sed
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	pam
Provides:	fdisk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
util-linux contains a large variety of low-level system utilities
necessary for a functional Linux system. This includes, among other
things, configuration tools such as fdisk and system programs such as
logger.

%package -n blockdev
Summary:	Support for blockdev
Group:		Applications/System
Requires:	coreutils

%description -n blockdev
The utility blockdev allows one to call block device ioctls from the
command line. This package also includes initscript to set blockdev
parameters at system startup.

%package -n losetup
Summary:	Programs for setting up and configuring loopback devices
Group:		Applications/System

%description -n losetup
Linux supports a special block device called the loopback device,
which maps a normal file onto a virtual block device. This package
contains programs for setting up and removing the mapping between
files and loopback devices.

Block loopback devices should not be confused with the networking
loopback device, which is configured with the normal ifconfig command.

%package -n mount
Summary:	Programs for mounting and unmounting filesystems
Group:		Applications/System

%description -n mount
mount is used for adding new filesystems, both local and networked, to
your current directory structure. The filesystems must already exist
for this to work. It can also be used to change the access types the
kernel uses for already-mounted filesystems.

This package is critical for the functionality of your system.

%package -n chkdupexe
Summary:	chkdupexe - find duplicate executables
Group:		Applications/System
Provides:	util-linux-chkdupexe = %{version}-%{release}

%description -n chkdupexe
chkdupexe will scan the union of $PATH and a hardcoded list of common
locations for binaries. It will report dangling symlinks and
duplicately-named binaries.

%package -n tunelp
Summary:	Configures kernel parallel port driver
Group:		Applications/System

%description -n tunelp
tunelp aids in configuring the kernel parallel port driver.

%package -n login
Summary:	login is used when signing onto a system
Group:		Applications/System
Requires:	pam

%description -n login
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however).

%package -n agetty
Summary:	Alternative Linux getty
Group:		Applications/System
Requires:	login

%description -n agetty
agetty is simple Linux getty with serial support.

%package -n fsck
Summary:	Check and repair a Linux file system
Group:		Applications/System

%description -n fsck
Check and repair a Linux file system.

%package -n libblkid
Summary:	Library to handle device identification and token extraction
License:	LGPL v2.1+
Group:		Libraries
Requires:	libuuid = %{version}-%{release}


%description -n libblkid
Library to handle device identification and token extraction.

%package -n libblkid-devel
Summary:	blkid library - development files
Group:		Development/Libraries
Requires:	libblkid = %{version}-%{release}

%description -n libblkid-devel
blkid library - development files.

%package -n libblkid-static
Summary:	blkid static library
Group:		Development/Libraries
Requires:	libblkid-devel = %{version}-%{release}

%package -n libmount
Summary:	Library to handle mounting-related tasks
License:	LGPL
Group:		Libraries
Requires:	libblkid = %{version}-%{release}

%description -n libmount
Library to handle mounting-related tasks.

%package -n libmount-devel
Summary:	Header files for mount library
License:	LGPL
Group:		Development/Libraries
Requires:	libblkid-devel = %{version}-%{release}
Requires:	libmount = %{version}-%{release}

%description -n libmount-devel
Header files for mount library.

%package -n libmount-static
Summary:	Static version of mount library
License:	LGPL
Group:		Development/Libraries
Requires:	libmount-devel = %{version}-%{release}

%description -n libmount-static
Static version of mount library.


%description -n libblkid-static
blkid static library.

%package -n libuuid
Summary:	Library for accessing and manipulating UUID
Group:		Libraries

%description -n libuuid
Library for accessing and manipulating UUID.

%package -n libuuid-devel
Summary:	Header files for library for accessing and manipulating UUID
Group:		Development/Libraries
Requires:	libuuid = %{version}-%{release}

%description -n libuuid-devel
Library for accessing and manipulating UUID - development files.

%package -n libuuid-static
Summary:	uuid static library
Group:		Development/Libraries
Requires:	libuuid-devel = %{version}-%{release}

%description -n libuuid-static
uuid static library.

%prep
%setup -q

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses -DHAVE_LSEEK64_PROTOTYPE -DHAVE_LLSEEK_PROTOTYPE"
export CPPFLAGS
%configure \
	--bindir=/bin			\
	--sbindir=/sbin			\
	--disable-silent-rules		\
	--disable-use-tty-group 	\
	--disable-wall			\
	--enable-kill			\
	--enable-libmount-mount		\
	--enable-line			\
	--enable-login-utils		\
	--enable-partx			\
	--enable-write			\
	--with-pam			\
	--without-selinux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,sysconfig,security} \
	$RPM_BUILD_ROOT{/%{_lib},/var/lock}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -i -e 's,/usr/spool/mail,/var/mail,g' $RPM_BUILD_ROOT%{_mandir}/man1/login.1

mv $RPM_BUILD_ROOT%{_sbindir}/{addpart,delpart,partx} $RPM_BUILD_ROOT/sbin

install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/login

:> $RPM_BUILD_ROOT%{_sysconfdir}/blkid.tab

for lib in blkid mount uuid; do
	mv $RPM_BUILD_ROOT%{_libdir}/lib${lib}.so.* $RPM_BUILD_ROOT/%{_lib}
	ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/lib${lib}.so.*.*.*) \
		 $RPM_BUILD_ROOT%{_libdir}/lib${lib}.so
done

ln -sf hwclock $RPM_BUILD_ROOT/sbin/clock
echo '.so hwclock.8' > $RPM_BUILD_ROOT%{_mandir}/man8/clock.8

# cleanup, remove files not included in package
rm $RPM_BUILD_ROOT%{_bindir}/{chfn,chsh,newgrp} \
	$RPM_BUILD_ROOT%{_sbindir}/{vigr,vipw} \
	$RPM_BUILD_ROOT%{_mandir}/man1/{chfn,chsh,newgrp}.1 \
	$RPM_BUILD_ROOT%{_mandir}/man8/{vigr,vipw}.8

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n libblkid -p /sbin/ldconfig
%postun	-n libblkid -p /sbin/ldconfig

%post	-n libmount -p /sbin/ldconfig
%postun -n libmount -p /sbin/ldconfig

%post	-n libuuid -p /sbin/ldconfig
%postun	-n libuuid -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(2755,root,tty) %{_bindir}/write
%attr(755,root,root) %{_bindir}/cal
%attr(755,root,root) %{_bindir}/chrt
%attr(755,root,root) %{_bindir}/col
%attr(755,root,root) %{_bindir}/colcrt
%attr(755,root,root) %{_bindir}/colrm
%attr(755,root,root) %{_bindir}/column
%attr(755,root,root) %{_bindir}/cytune
%attr(755,root,root) %{_bindir}/fallocate
%attr(755,root,root) %{_bindir}/flock
%attr(755,root,root) %{_bindir}/getopt
%attr(755,root,root) %{_bindir}/hexdump
%attr(755,root,root) %{_bindir}/i386
%attr(755,root,root) %{_bindir}/ionice
%attr(755,root,root) %{_bindir}/ipcmk
%attr(755,root,root) %{_bindir}/ipcrm
%attr(755,root,root) %{_bindir}/ipcs
%attr(755,root,root) %{_bindir}/isosize
%attr(755,root,root) %{_bindir}/line
%attr(755,root,root) %{_bindir}/linux*
%attr(755,root,root) %{_bindir}/logger
%attr(755,root,root) %{_bindir}/look
%attr(755,root,root) %{_bindir}/lscpu
%attr(755,root,root) %{_bindir}/mcookie
%attr(755,root,root) %{_bindir}/namei
%attr(755,root,root) %{_bindir}/pg
%attr(755,root,root) %{_bindir}/prlimit
%attr(755,root,root) %{_bindir}/rename
%attr(755,root,root) %{_bindir}/renice
%attr(755,root,root) %{_bindir}/rev
%attr(755,root,root) %{_bindir}/script
%attr(755,root,root) %{_bindir}/scriptreplay
%attr(755,root,root) %{_bindir}/setarch
%attr(755,root,root) %{_bindir}/setsid
%attr(755,root,root) %{_bindir}/setterm
%attr(755,root,root) %{_bindir}/tailf
%attr(755,root,root) %{_bindir}/taskset
%attr(755,root,root) %{_bindir}/ul
%attr(755,root,root) %{_bindir}/unshare
%attr(755,root,root) %{_bindir}/whereis

%attr(755,root,root) %{_sbindir}/fdformat
%attr(755,root,root) %{_sbindir}/ldattach
%attr(755,root,root) %{_sbindir}/readprofile
%attr(755,root,root) %{_sbindir}/rtcwake

%attr(755,root,root) /bin/dmesg
%attr(755,root,root) /bin/kill
%attr(755,root,root) /bin/lsblk
%attr(755,root,root) /bin/more

%attr(755,root,root) /sbin/addpart
%attr(755,root,root) /sbin/blkid
%attr(755,root,root) /sbin/cfdisk
%attr(755,root,root) /sbin/chcpu
%attr(755,root,root) /sbin/clock
%attr(755,root,root) /sbin/ctrlaltdel
%attr(755,root,root) /sbin/delpart
%attr(755,root,root) /sbin/fdisk
%attr(755,root,root) /sbin/findfs
%attr(755,root,root) /sbin/fsck.cramfs
%attr(755,root,root) /sbin/fsck.minix
%attr(755,root,root) /sbin/fsfreeze
%attr(755,root,root) /sbin/fstrim
%attr(755,root,root) /sbin/hwclock*
%attr(755,root,root) /sbin/mkfs
%attr(755,root,root) /sbin/mkfs.bfs
%attr(755,root,root) /sbin/mkfs.cramfs
%attr(755,root,root) /sbin/mkfs.minix
%attr(755,root,root) /sbin/mkswap
%attr(755,root,root) /sbin/partx
%attr(755,root,root) /sbin/raw
%attr(755,root,root) /sbin/sfdisk
%attr(755,root,root) /sbin/swaplabel
%attr(755,root,root) /sbin/switch_root
%attr(755,root,root) /sbin/wipefs

%ghost %{_sysconfdir}/blkid.tab

%{_mandir}/man1/cal.1*
%{_mandir}/man1/chrt.1*
%{_mandir}/man1/col.1*
%{_mandir}/man1/colcrt.1*
%{_mandir}/man1/colrm.1*
%{_mandir}/man1/column.1*
%{_mandir}/man1/dmesg.1*
%{_mandir}/man1/fallocate.1*
%{_mandir}/man1/flock.1*
%{_mandir}/man1/getopt.1*
%{_mandir}/man1/hexdump.1*
%{_mandir}/man1/ionice.1*
%{_mandir}/man1/ipcmk.1*
%{_mandir}/man1/ipcrm.1*
%{_mandir}/man1/ipcs.1*
%{_mandir}/man1/kill.1*
%{_mandir}/man1/line.1*
%{_mandir}/man1/logger.1*
%{_mandir}/man1/look.1*
%{_mandir}/man1/lscpu.1*
%{_mandir}/man1/mcookie.1*
%{_mandir}/man1/more.1*
%{_mandir}/man1/namei.1*
%{_mandir}/man1/pg.1*
%{_mandir}/man1/prlimit.1*
%{_mandir}/man1/rename.1*
%{_mandir}/man1/renice.1*
%{_mandir}/man1/rev.1*
%{_mandir}/man1/script.1*
%{_mandir}/man1/scriptreplay.1*
%{_mandir}/man1/setsid.1*
%{_mandir}/man1/setterm.1*
%{_mandir}/man1/tailf.1*
%{_mandir}/man1/taskset.1*
%{_mandir}/man1/ul.1*
%{_mandir}/man1/unshare.1*
%{_mandir}/man1/whereis.1*
%{_mandir}/man1/write.1*

%{_mandir}/man3/libblkid.3*

%{_mandir}/man8/addpart.8*
%{_mandir}/man8/blkid.8*
%{_mandir}/man8/cfdisk.8*
%{_mandir}/man8/chcpu.8*
%{_mandir}/man8/clock.8*
%{_mandir}/man8/ctrlaltdel.8*
%{_mandir}/man8/cytune.8*
%{_mandir}/man8/delpart.8*
%{_mandir}/man8/fdformat.8*
%{_mandir}/man8/fdisk.8*
%{_mandir}/man8/findfs.8*
%{_mandir}/man8/fsck.minix.8*
%{_mandir}/man8/fsfreeze.8*
%{_mandir}/man8/fstrim.8*
%{_mandir}/man8/hwclock.8*
%{_mandir}/man8/i386*
%{_mandir}/man8/isosize.8*
%{_mandir}/man8/ldattach.8*
%{_mandir}/man8/linux*
%{_mandir}/man8/lsblk.8*
%{_mandir}/man8/mkfs.8*
%{_mandir}/man8/mkfs.bfs.8*
%{_mandir}/man8/mkfs.minix.8*
%{_mandir}/man8/mkswap.8*
%{_mandir}/man8/partx.8*
%{_mandir}/man8/raw.8.gz
%{_mandir}/man8/readprofile.8*
%{_mandir}/man8/rtcwake.8*
%{_mandir}/man8/setarch.8*
%{_mandir}/man8/sfdisk.8*
%{_mandir}/man8/swaplabel.8*
%{_mandir}/man8/switch_root.8*
%{_mandir}/man8/wipefs.8*

%files -n libblkid
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libblkid.so.?
%attr(755,root,root) /%{_lib}/libblkid.so.*.*.*

%files -n libblkid-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libblkid.so
%{_includedir}/blkid
%{_pkgconfigdir}/blkid.pc

%files -n libblkid-static
%defattr(644,root,root,755)
%{_libdir}/libblkid.a

%files -n libmount
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libmount.so.?
%attr(755,root,root) /%{_lib}/libmount.so.*.*

%files -n libmount-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmount.so
%{_includedir}/libmount
%{_pkgconfigdir}/mount.pc

%files -n libmount-static
%defattr(644,root,root,755)
%{_libdir}/libmount.a

%files -n libuuid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uuidgen
%attr(755,root,root) %ghost /%{_lib}/libuuid.so.?
%attr(755,root,root) /%{_lib}/libuuid.so.*.*.*
%{_mandir}/man1/uuidgen.1*

%files -n libuuid-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuuid.so
%{_includedir}/uuid
%{_pkgconfigdir}/uuid.pc
%{_mandir}/man3/*uuid*

%files -n libuuid-static
%defattr(644,root,root,755)
%{_libdir}/libuuid.a

%files -n agetty
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/agetty
%{_mandir}/man8/agetty.8*

%files -n blockdev
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/blockdev
%{_mandir}/man8/blockdev.8*

%files -n chkdupexe
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chkdupexe
%{_mandir}/man1/chkdupexe.1*

%files -n fsck
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/fsck
%{_mandir}/man8/fsck.8*

%files -n login
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/login
%attr(755,root,root) /bin/login
%{_mandir}/man1/login.1*

%files -n losetup
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/losetup
%{_mandir}/man8/losetup.8*

%files -n mount
%defattr(644,root,root,755)
%attr(4755,root,root) /bin/mount
%attr(4755,root,root) /bin/umount
%attr(755,root,root) /bin/findmnt
%attr(755,root,root) /bin/mountpoint
%attr(755,root,root) /sbin/pivot_root
%attr(755,root,root) /sbin/swapoff
%attr(755,root,root) /sbin/swapon
%{_mandir}/man1/mountpoint.1*
%{_mandir}/man5/fstab.5*
%{_mandir}/man8/findmnt.8*
%{_mandir}/man8/mount.8*
%{_mandir}/man8/pivot_root.8*
%{_mandir}/man8/swapoff.8*
%{_mandir}/man8/swapon.8*
%{_mandir}/man8/umount.8*

%files -n tunelp
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tunelp
%{_mandir}/man8/tunelp.8*

