%define		_enable_debug_packages	0
%define		__spec_clean_body	%{nil}

Summary:	Common directories
Name:		filesystem
Version:	3.2
Release:	2
License:	GPL
Group:		Base
BuildRequires:	automake
Requires:	FHS
Requires:	setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# directory for "privilege separation" chroot
%define		_privsepdir	/usr/share/empty
# directory for *.idl files (for CORBA implementations)
%define		_idldir		/usr/share/idl

%define		no_install_post_strip	1
%define		_enable_debug_packages	0

%description
This package contains common directories for packages that extend
some programs functionality, but don't require them themselves.

%package debuginfo
Summary:	Common directories for debug information
Group:		Development/Debug
Requires:	%{name} = %{version}-%{release}

%description debuginfo
This package provides common directories for debug information.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT/{initrd,run,sys} \
	$RPM_BUILD_ROOT/etc/{X11/xinit/xinitrc.d,certs,logrotate.d,security,sysconfig/wmstyle,xdg/{autostart,menus}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{cron.d,cron.{hourly,daily,weekly,monthly},cron} \
	$RPM_BUILD_ROOT/home/{users,services} \
	$RPM_BUILD_ROOT/lib/{firmware,security} \
	$RPM_BUILD_ROOT/usr/include/security \
	$RPM_BUILD_ROOT/usr/lib/{cgi-bin,debug,pkgconfig} \
	$RPM_BUILD_ROOT/var/lib/color/icc \
	$RPM_BUILD_ROOT/usr/share/{backgrounds,desktop-directories,gnome/help,color/{icc,targets},man/man{n,l},man/pl/mann,pkgconfig,sounds/sf2,themes/Default,thumbnailers,wallpapers,gnome/wm-properties,xsessions} \
	$RPM_BUILD_ROOT/usr/src/{debug,examples} \
	$RPM_BUILD_ROOT/var/lock/subsys \
	$RPM_BUILD_ROOT/var/log/archive \
	$RPM_BUILD_ROOT{%{_aclocaldir},%{_desktopdir}/docklets,%{_iconsdir},%{_pixmapsdir}/backgrounds,%{_datadir}/gtk-engines} \
	$RPM_BUILD_ROOT%{_fontsdir}/{{100,75}dpi,OTF,Speedo,Type1/{afm,pfm},TTF,cyrillic,local,misc} \
	$RPM_BUILD_ROOT{%{_idldir},%{_privsepdir}} \
	$RPM_BUILD_ROOT%{_libdir}/browser-plugins \
	$RPM_BUILD_ROOT%{_datadir}/gnome-2.0/ui	\
	$RPM_BUILD_ROOT/lib/initrd-utils/{bin,dev,etc,lib,media/{cdrom,fs},proc,sbin,sys,tmp}

install -d \
	$RPM_BUILD_ROOT/usr/lib/debug/%{_lib} \
	$RPM_BUILD_ROOT/usr/lib/debug%{_libdir} \
	$RPM_BUILD_ROOT/usr/lib/debug/{bin,sbin} \
	$RPM_BUILD_ROOT/usr/lib/debug/usr/{bin,sbin} \
	$RPM_BUILD_ROOT/usr/lib/debug/lib/security \
	$RPM_BUILD_ROOT/usr/src/debug

> %{name}.lang
install -d $RPM_BUILD_ROOT/usr/share/help/C

for lang in ar bg ca cs da de el en_GB es eu fi fr gl he hi hr hu id it ja ko lt lv nb nl oc pa pl ps pt_BR ro ru sl sr sr@latin sv te th tr uk vi zh_CN zh_HK zh_TW; do
	install -d $RPM_BUILD_ROOT/usr/share/help/${lang}
	echo "%%lang($lang) %dir /usr/share/help/${lang}" >> %{name}.lang
done

find $RPM_BUILD_ROOT/usr/lib/debug -type d | while read line; do
	echo ${line#$RPM_BUILD_ROOT}
done > $RPM_BUILD_ROOT/usr/src/debug/%{name}-debuginfo.files

# create this for %clean
tar -cf checkfiles.tar -C $RPM_BUILD_ROOT .

%clean
mkdir -p $RPM_BUILD_ROOT
tar -xf checkfiles.tar -C $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT

check_filesystem_dirs() {
	RPMFILE=%{_rpmdir}/%{name}-%{version}-%{release}.%{_target_cpu}.rpm
	RPMFILE2=%{?with_debuginfo:%{_rpmdir}/%{name}-debuginfo-%{version}-%{release}.%{_target_cpu}.rpm}
	TMPFILE=$(mktemp)
	# note: we must exclude from check all existing dirs belonging to FHS
	find | sed -e 's|^\.||g' -e 's|^$||g' | LC_ALL=C sort | grep -v $TMPFILE | grep -E -v '^/(etc|etc/X11|home|lib|lib64|usr|usr/include|usr/lib|usr/lib64|usr/share|usr/share/man|usr/share/man/pl|usr/src|var|var/lib|var/lock|var/log)$' > $TMPFILE

	# find finds also '.', so use option -B for diff
	rpm -qpl $RPMFILE $RPMFILE2 | grep -v '^/$' | LC_ALL=C sort | diff -uB - $TMPFILE || :

	rm -f $TMPFILE
}

check_filesystem_dirs

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir /etc/X11/xinit
%dir /etc/X11/xinit/xinitrc.d
%attr(751,root,root) %dir /etc/certs
%attr(751,root,root) %dir /etc/security
%attr(640,root,crontab) %dir %{_sysconfdir}/cron
%attr(640,root,crontab) %dir /etc/cron.*
%dir /etc/logrotate.d
%dir /etc/sysconfig
%dir /etc/sysconfig/wmstyle
%dir /etc/xdg
%dir /etc/xdg/autostart
%dir /etc/xdg/menus
%dir /home/users
%attr(751,root,adm) %dir /home/services
%dir /initrd
%dir /run
%dir /lib/firmware
%dir /lib/security
%dir /lib/initrd-utils
%dir /lib/initrd-utils/bin
%dir /lib/initrd-utils/dev
%dir /lib/initrd-utils/etc
%dir /lib/initrd-utils/lib
%dir /lib/initrd-utils/media
%dir /lib/initrd-utils/media/cdrom
%dir /lib/initrd-utils/media/fs
%dir /lib/initrd-utils/proc
%dir /lib/initrd-utils/sbin
%dir /lib/initrd-utils/sys
%dir /lib/initrd-utils/tmp
%dir /sys
%dir /usr/include/security
%dir /usr/lib/cgi-bin
%dir /usr/lib/pkgconfig
%dir /usr/share/backgrounds
%dir /usr/share/desktop-directories
%dir /usr/share/gnome
%dir /usr/share/gnome/help
%dir /usr/share/help
%dir /usr/share/help/C
%dir /usr/share/color
%dir /usr/share/color/icc
%dir /usr/share/color/targets
%dir /usr/share/man/man[nl]
%lang(pl) %dir /usr/share/man/pl/mann
%dir /usr/share/pkgconfig
%dir /usr/share/sounds
%dir /usr/share/sounds/sf2
%dir /usr/share/themes
%dir /usr/share/themes/Default
%dir /usr/share/thumbnailers
%dir /usr/share/wallpapers
%dir /usr/share/gnome/wm-properties
%dir /usr/share/xsessions
%dir /usr/src/examples
%dir /var/lib/color
%dir /var/lib/color/icc
%attr(700,root,root) %dir /var/lock/subsys
%attr(751,root,logs) %dir /var/log/archive
%dir %{_aclocaldir}
%dir %{_datadir}/gtk-engines
%dir %{_desktopdir}
%dir %{_desktopdir}/docklets
%dir %{_iconsdir}
%dir %{_idldir}
%dir %{_pixmapsdir}
%dir %{_pixmapsdir}/backgrounds
%dir %{_privsepdir}
%{_libdir}/browser-plugins
%{_fontsdir}

%files debuginfo
%defattr(644,root,root,755)
%dir /usr/lib/debug
%dir /usr/src/debug
/usr/lib/debug/*
/usr/src/debug/filesystem-debuginfo.files


