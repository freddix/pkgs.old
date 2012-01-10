Summary:	Common Unix Printing System
Name:		cups
Version:	1.4.8
Release:	3
Epoch:		1
License:	GPL/LGPL
Group:		Applications/Printing
Source0:	http://ftp.easysw.com/pub/cups/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	0ec52d3f3c69bc2ab5ed70c594edbce6
Source1:	%{name}.service
Source2:	%{name}.pamd
Source3:	%{name}.logrotate
Source4:	%{name}.mailto.conf
Source5:	%{name}-modprobe.conf
Source6:	%{name}-tmpfiles.conf
Patch0:		%{name}-config.patch
Patch2:		%{name}-options.patch
Patch3:		%{name}-man_pages_linking.patch
Patch4:		%{name}-nostrip.patch
Patch5:		%{name}-certs_FHS.patch
Patch6:		%{name}-peercred.patch
# svn diff http://svn.easysw.com/public/cups/tags/release-1.4.1/ http://svn.easysw.com/public/cups/branches/branch-1.4/ > cups-branch.diff
URL:		http://www.cups.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gnutls-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pam-devel
BuildRequires:	pkg-config
Requires(post,preun):	/bin/systemctl
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
CUPS provides a portable printing layer for UNIX-based operating
systems. It has been developed by Easy Software Products to promote a
standard printing solution for all UNIX vendors and users. CUPS
provides the System V and Berkeley command-line interfaces. CUPS uses
the Internet Printing Protocol ("IPP") as the basis for managing print
jobs and queues. The Line Printer Daemon ("LPD") Server Message Block
("SMB"), and AppSocket (a.k.a. JetDirect) protocols are also supported
with reduced functionality. CUPS adds network printer browsing and
PostScript Printer Description ("PPD") based printing options to
support real-world printing under UNIX.

%package lib
Summary:	Common Unix Printing System Libraries
Group:		Libraries
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}

%description lib
Common Unix Printing System Libraries.

%package clients
Summary:	Common Unix Printing System Clients
Group:		Applications/Printing
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description clients
Common Unix Printing System Clients.

%package image-lib
Summary:	Common Unix Printing System Libraries - images manipulation
Group:		Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description image-lib
Common Unix Printing System Libraries - images manupalation.

%package devel
Summary:	Common Unix Printing System development files
Group:		Development/Libraries
Requires:	%{name}-image-lib = %{epoch}:%{version}-%{release}
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Requires:	gnutls-devel

%description devel
Common Unix Printing System development files.
CUPS.

%package backend-usb
Summary:	USB backend for CUPS
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-usb
This package allow CUPS printing on USB printers.

%package backend-serial
Summary:	Serial port backend for CUPS
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-serial
This package allow CUPS printing on printers connected by serial
ports.

%package backend-parallel
Summary:	Parallel port backend for CUPS
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-parallel
This package allow CUPS printing on printers connected by parallel
ports.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

sed -i -e 's|.SILENT:.*||g' Makedefs.in

%build
%{__aclocal} -I config-scripts
%{__autoconf}
%configure \
	--disable-cdsassl				\
	--disable-ldap					\
	--enable-dbus					\
	--enable-gnutls					\
	--enable-pam					\
	--enable-shared					\
	--enable-ssl					\
	--libdir=%{_ulibdir}				\
	--with-cups-group=lp				\
	--with-cups-user=lp				\
	--with-dbusdir=/etc/dbus-1			\
	--with-docdir=%{_ulibdir}/%{name}/cgi-bin	\
	--with-printcap=/etc/printcap			\
	--with-system-groups=sys			\
	--without-java					\
	--without-perl					\
	--without-php					\
	--without-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,logrotate.d,modprobe.d,security,tmpfiles.d} \
	$RPM_BUILD_ROOT/%{_lib}/systemd/system \
	$RPM_BUILD_ROOT/var/run/cups \
	$RPM_BUILD_ROOT/var/log/{,archive/}cups

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT	\
	CUPS_USER=$(id -u)		\
	CUPS_GROUP=$(id -g)

install %{SOURCE1} $RPM_BUILD_ROOT/%{_lib}/systemd/system/cups.service
install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/cups/mailto.conf
install %{SOURCE5} $RPM_BUILD_ROOT/etc/modprobe.d/cups.conf
install %{SOURCE6} $RPM_BUILD_ROOT/etc/tmpfiles.d/cups.conf

touch $RPM_BUILD_ROOT/var/log/cups/{access_log,error_log,page_log}
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{classes,printers,client}.conf

# windows drivers can be put there.
install -d $RPM_BUILD_ROOT%{_datadir}/cups/drivers

# dirs for gimp-print-cups-4.2.7-1
install -d $RPM_BUILD_ROOT%{_datadir}/cups/model/{C,da,en_GB,fr,nb,pl,sv}

touch $RPM_BUILD_ROOT/var/cache/cups/help.index
touch $RPM_BUILD_ROOT/var/cache/cups/{job,remote}.cache
touch $RPM_BUILD_ROOT/var/cache/cups/ppds.dat
install -d $RPM_BUILD_ROOT%{_sysconfdir}/cups/ssl

# links to enable/disable (compatibility!)
ln -s accept $RPM_BUILD_ROOT%{_sbindir}/enable
ln -s accept $RPM_BUILD_ROOT%{_sbindir}/disable

# fix/update locale names
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{nb,zh_CN}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no/cups_no.po,nb/cups_nb.po}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh/cups_zh.po,zh_CN/cups_zh_CN.po}

# check-files cleanup
rm -rf $RPM_BUILD_ROOT%{_mandir}/{,es/,fr/}cat?
rm -rf $RPM_BUILD_ROOT/''etc/{init.d,rc?.d}/*
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/cupsd.conf.default

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
    /bin/systemctl enable cups.service >/dev/null 2>&1 || :
fi

%preun
if [ "$1" = "0" ]; then
    /bin/systemctl stop cups.service >/dev/null 2>&1 || :
    /bin/systemctl disable cups.service >/dev/null 2>&1 || :
fi

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%post	image-lib -p /sbin/ldconfig
%postun	image-lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(4755,lp,root) %{_bindir}/lppasswd
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/classes.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/mailto.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/printers.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/snmp.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/cupsd.conf

/%{_lib}/systemd/system/cups.service

%attr(640,root,root) %config %verify(not md5 mtime size) /etc/pam.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}

%attr(755,root,root) %{_bindir}/cupstestdsc
%attr(755,root,root) %{_bindir}/cupstestppd
%attr(755,root,root) %{_bindir}/ppd*

%attr(755,root,root) %{_sbindir}/cupsctl
%attr(755,root,root) %{_sbindir}/cupsd
%attr(755,root,root) %{_sbindir}/cupsfilter

%dir %attr(700,root,lp) %{_sysconfdir}/%{name}/ssl
%dir %attr(755,root,lp) %{_sysconfdir}/%{name}/ppd
%dir %{_sysconfdir}/%{name}/interfaces
%{_sysconfdir}/tmpfiles.d/cups.conf

/etc/dbus-1/system.d/cups.conf

%dir %{_ulibdir}/cups
%dir %{_ulibdir}/cups/*

%attr(755,root,root) %{_ulibdir}/cups/cgi-bin/*.cgi
%{_ulibdir}/cups/cgi-bin/*.css
%{_ulibdir}/cups/cgi-bin/*.html
%{_ulibdir}/cups/cgi-bin/*.txt
%{_ulibdir}/cups/cgi-bin/help
%{_ulibdir}/cups/cgi-bin/images

%lang(de) %{_ulibdir}/cups/cgi-bin/de
%lang(es) %{_ulibdir}/cups/cgi-bin/es
%lang(eu) %{_ulibdir}/cups/cgi-bin/eu
%lang(id) %{_ulibdir}/cups/cgi-bin/id
%lang(it) %{_ulibdir}/cups/cgi-bin/it
%lang(ja) %{_ulibdir}/cups/cgi-bin/ja
%lang(pl) %{_ulibdir}/cups/cgi-bin/pl
%lang(ru) %{_ulibdir}/cups/cgi-bin/ru

%dir %{_datadir}/cups/templates
%{_datadir}/cups/templates/*.tmpl
%lang(de) %{_datadir}/cups/templates/de
%lang(es) %{_datadir}/cups/templates/es
%lang(eu) %{_datadir}/cups/templates/eu
%lang(id) %{_datadir}/cups/templates/id
%lang(it) %{_datadir}/cups/templates/it
%lang(ja) %{_datadir}/cups/templates/ja
%lang(pl) %{_datadir}/cups/templates/pl
%lang(ru) %{_datadir}/cups/templates/ru

%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/C
%lang(da) %dir %{_datadir}/cups/model/da
%lang(en_GB) %dir %{_datadir}/cups/model/en_GB
%lang(fr) %dir %{_datadir}/cups/model/fr
%lang(nb) %dir %{_datadir}/cups/model/nb
%lang(pl) %dir %{_datadir}/cups/model/pl
%lang(sv) %dir %{_datadir}/cups/model/sv

%exclude %{_ulibdir}/cups/backend/usb
%exclude %{_ulibdir}/cups/backend/serial
%exclude %{_ulibdir}/cups/backend/parallel

%attr(755,root,root) %{_ulibdir}/cups/backend/*
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-deviced
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-driverd
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-polld
%attr(755,root,root) %{_ulibdir}/cups/filter/*
%attr(755,root,root) %{_ulibdir}/cups/monitor/*
%attr(755,root,root) %{_ulibdir}/cups/notifier/*

%{_datadir}/cups/banners
%{_datadir}/cups/charsets
%{_datadir}/cups/data
%{_datadir}/cups/drivers
%{_datadir}/cups/drv
%{_datadir}/cups/examples
%{_datadir}/cups/fonts
%{_datadir}/cups/mime

%{_datadir}/cups/ppdc

%{_mandir}/man1/cupstestppd.1*
%{_mandir}/man1/cupstestdsc.1*
%{_mandir}/man1/lppasswd.1*
%{_mandir}/man1/ppd*.1*
%{_mandir}/man7/backend.7*
%{_mandir}/man7/filter.7*
%{_mandir}/man7/notifier.7*
%{_mandir}/man5/*
%{_mandir}/man8/accept.8*
%{_mandir}/man8/cups-deviced.8*
%{_mandir}/man8/cups-driverd.8*
%{_mandir}/man8/cups-polld.8*
%{_mandir}/man8/cupsaddsmb.8*
%{_mandir}/man8/cupsctl.8*
%{_mandir}/man8/cupsd.8*
%{_mandir}/man8/cupsenable.8*
%{_mandir}/man8/cupsfilter.8*
%{_mandir}/man8/lp*

%dir %attr(775,root,lp) /var/cache/cups
%dir %attr(755,root,lp) /var/lib/cups
%dir %attr(511,lp,sys) /var/lib/cups/certs
%dir %attr(755,root,lp) /var/run/cups
%dir %attr(710,root,lp) /var/spool/cups
%dir %attr(1770,root,lp) /var/spool/cups/tmp

%attr(600,lp,lp) %ghost /var/cache/cups/help.index
%attr(640,root,lp) %ghost /var/cache/cups/job.cache
%attr(600,lp,lp) %ghost /var/cache/cups/ppds.dat
%attr(640,root,lp) %ghost /var/cache/cups/remote.cache
%attr(750,root,logs) %dir /var/log/archive/cups
%attr(750,root,logs) %dir /var/log/cups
%attr(640,root,logs) %ghost /var/log/cups/access_log
%attr(640,root,logs) %ghost /var/log/cups/error_log
%attr(640,root,logs) %ghost /var/log/cups/page_log

%lang(da) %{_datadir}/locale/da/cups_da.po
%lang(de) %{_datadir}/locale/de/cups_de.po
%lang(es) %{_datadir}/locale/es/cups_es.po
%lang(eu) %{_datadir}/locale/eu/cups_eu.po
%lang(fi) %{_datadir}/locale/fi/cups_fi.po
%lang(fr) %{_datadir}/locale/fr/cups_fr.po
%lang(id) %{_datadir}/locale/id/cups_id.po
%lang(it) %{_datadir}/locale/it/cups_it.po
%lang(ja) %{_datadir}/locale/ja/cups_ja.po
%lang(ko) %{_datadir}/locale/ko/cups_ko.po
%lang(nb) %{_datadir}/locale/nb/cups_nb.po
%lang(nl) %{_datadir}/locale/nl/cups_nl.po
%lang(pl) %{_datadir}/locale/pl/cups_pl.po
%lang(pt) %{_datadir}/locale/pt/cups_pt.po
%lang(pt_BR) %{_datadir}/locale/pt_BR/cups_pt_BR.po
%lang(ru) %{_datadir}/locale/ru/cups_ru.po
%lang(sv) %{_datadir}/locale/sv/cups_sv.po
%lang(zh_CN) %{_datadir}/locale/zh_CN/cups_zh_CN.po
%lang(zh_TW) %{_datadir}/locale/zh_TW/cups_zh_TW.po

%files lib
%defattr(644,root,root,755)
%dir %attr(755,root,lp) %{_sysconfdir}/%{name}
%attr(755,root,root) %{_libdir}/libcups.so.*
%attr(755,root,root) %{_libdir}/libcupscgi.so.*
%attr(755,root,root) %{_libdir}/libcupsdriver.so.*
%attr(755,root,root) %{_libdir}/libcupsmime.so.*
%attr(755,root,root) %{_libdir}/libcupsppdc.so.*
%dir %{_datadir}/cups
%{_datadir}/cups/charmaps

%files clients
%defattr(644,root,root,755)
%attr(644,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/client.conf
%attr(755,root,root) %{_bindir}/cancel
%attr(755,root,root) %{_bindir}/lp
%attr(755,root,root) %{_bindir}/lpoptions
%attr(755,root,root) %{_bindir}/lpq
%attr(755,root,root) %{_bindir}/lpr
%attr(755,root,root) %{_bindir}/lprm
%attr(755,root,root) %{_bindir}/lpstat
%attr(755,root,root) %{_sbindir}/accept
%attr(755,root,root) %{_sbindir}/cupsaccept
%attr(755,root,root) %{_sbindir}/cupsaddsmb
%attr(755,root,root) %{_sbindir}/cupsenable
%attr(755,root,root) %{_sbindir}/cupsdisable
%attr(755,root,root) %{_sbindir}/cupsreject
%attr(755,root,root) %{_sbindir}/disable
%attr(755,root,root) %{_sbindir}/enable
%attr(755,root,root) %{_sbindir}/lpadmin
%attr(755,root,root) %{_sbindir}/lpc
%attr(755,root,root) %{_sbindir}/lpinfo
%attr(755,root,root) %{_sbindir}/lpmove
%attr(755,root,root) %{_sbindir}/reject

%{_mandir}/man1/cancel.1*
%{_mandir}/man1/lp.1*
%{_mandir}/man1/lpoptions.1*
%{_mandir}/man1/lpq.1*
%{_mandir}/man1/lpr.1*
%{_mandir}/man1/lprm.1*
%{_mandir}/man1/lpstat.1*
%{_mandir}/man8/cupsaccept.8*
%{_mandir}/man8/cupsdisable.8*
%{_mandir}/man8/cupsreject.8*
%{_mandir}/man8/reject.8*

%files image-lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcupsimage.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cups-config
%attr(755,root,root) %{_libdir}/libcups.so
%attr(755,root,root) %{_libdir}/libcupscgi.so
%attr(755,root,root) %{_libdir}/libcupsdriver.so
%attr(755,root,root) %{_libdir}/libcupsimage.so
%attr(755,root,root) %{_libdir}/libcupsmime.so
%attr(755,root,root) %{_libdir}/libcupsppdc.so
%{_includedir}/cups
%{_mandir}/man1/cups-config*

%files backend-usb
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/usb
/etc/modprobe.d/cups.conf

%files backend-serial
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/serial

%files backend-parallel
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/parallel

