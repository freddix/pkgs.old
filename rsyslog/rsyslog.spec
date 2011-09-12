Summary:	Linux system and kernel logger
Name:		rsyslog
Version:	5.8.5
Release:	2
License:	GPL v3+
Group:		Daemons
Source0:	http://www.rsyslog.com/files/download/rsyslog/%{name}-%{version}.tar.gz
# Source0-md5:	a73cb577cb4bc5b9c8f0d217eb054ad2
Source1:	%{name}.logrotate
Source2:	%{name}.conf
URL:		http://www.rsyslog.com/
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
Requires(post):	/bin/systemctl
Requires(post):	fileutils
Requires(postun):	/bin/systemctl
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/lib/rpm/user_group.sh
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires:	logrotate
Requires:	psmisc
Provides:	group(syslog)
Provides:	syslogdaemon
Provides:	user(syslog)
Obsoletes:	syslog-ng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rsyslog is an enhanced multi-threaded syslogd supporting, among
others, MySQL, syslog/tcp, RFC 3195, permitted sender lists, filtering
on any message part, and fine grain output format control. It is quite
compatible to stock sysklogd and can be used as a drop-in replacement.
Its advanced features make it suitable for enterprise-class,
encryption protected syslog relay chains while at the same time being
very easy to setup for the novice user.

%prep
%setup -q

%build
%configure \
	--enable-unlimited-select	\
	--with-systemdsystemunitdir=/%{_lib}/systemd/system
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d,logrotate.d,rsyslog.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{5,8},%{_bindir}} \
	$RPM_BUILD_ROOT/var/log

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/logrotate.d/rsyslog
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/rsyslog.conf

for n in debug kernel maillog messages secure syslog user spooler lpr daemon
do
	> $RPM_BUILD_ROOT/var/log/$n
done

%{__rm} $RPM_BUILD_ROOT%{_libdir}/rsyslog/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -P syslog -g 18 syslog
%useradd -P syslog -u 18 -g syslog -c "Syslog User" syslog
%addusertogroup syslog logs

%post
for n in /var/log/{cron,daemon,debug,kernel,lpr,maillog,messages,secure,spooler,syslog,user}; do
	if [ -f $n ]; then
		chown syslog:syslog $n
		continue
	else
		touch $n
		chmod 000 $n
		chown syslog:syslog $n
		chmod 640 $n
	fi
done

# enable on install
if [ "$1" = "1" ]; then
    /bin/systemctl enable rsyslog.service >/dev/null 2>&1 || :
fi

%preun
if [ "$1" = "0" ]; then
    /bin/systemctl --no-reload disable rsyslog.service >/dev/null 2>&1 || :
    /bin/systemctl stop rsyslog.service >/dev/null 2>&1 || :
fi

%postun
if [ "$1" = "0" ]; then
	%userremove syslog
	%groupremove syslog
fi

# try to restart on upgrade
if [ "$1" = "1" ]; then
    /bin/systemctl try-restart rsyslog.service >/dev/null 2>&1 || :
fi


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%dir %{_libdir}/rsyslog
%dir %{_sysconfdir}/rsyslog.d

%attr(640,root,root) %ghost /var/log/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/rsyslog
%attr(640,root,syslog) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rsyslog.conf
/%{_lib}/systemd/system/%{name}.service

%attr(755,root,root) %{_sbindir}/rsyslogd

%attr(755,root,root) %{_libdir}/rsyslog/imklog.so
%attr(755,root,root) %{_libdir}/rsyslog/immark.so
%attr(755,root,root) %{_libdir}/rsyslog/imtcp.so
%attr(755,root,root) %{_libdir}/rsyslog/imudp.so
%attr(755,root,root) %{_libdir}/rsyslog/imuxsock.so
%attr(755,root,root) %{_libdir}/rsyslog/lmnet.so
%attr(755,root,root) %{_libdir}/rsyslog/lmnetstrms.so
%attr(755,root,root) %{_libdir}/rsyslog/lmnsd_ptcp.so
%attr(755,root,root) %{_libdir}/rsyslog/lmregexp.so
%attr(755,root,root) %{_libdir}/rsyslog/lmstrmsrv.so
%attr(755,root,root) %{_libdir}/rsyslog/lmtcpclt.so
%attr(755,root,root) %{_libdir}/rsyslog/lmtcpsrv.so
%attr(755,root,root) %{_libdir}/rsyslog/lmzlibw.so
%attr(755,root,root) %{_libdir}/rsyslog/omruleset.so
%attr(755,root,root) %{_libdir}/rsyslog/omtesting.so

%{_mandir}/man5/rsyslog.conf.5*
%{_mandir}/man8/rsyslogd.8*

