Summary:	Cron daemon
Name:		cronie
Version:	1.4.8
Release:	3
License:	MIT and BSD and GPL v2
Group:		Daemons
Source0:	https://fedorahosted.org/releases/c/r/cronie/%{name}-%{version}.tar.gz
# Source0-md5:	9b1d2ce6db8d1883e06635f437170657
Source1:	%{name}.service
Source2:	%{name}.logrotate
Source3:	%{name}.crontab
Source4:	%{name}.pam
Source5:	run-parts
Patch0:		%{name}-nosyscrontab.patch
Patch1:		%{name}-sendmail-path.patch
URL:		https://fedorahosted.org/cronie/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
Requires(post):	fileutils
Requires(post,preun,postun):	/bin/systemctl
Requires(postun):	/usr/sbin/groupdel
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires:	psmisc
Provides:	crondaemon
Provides:	group(crontab)
Obsoletes:	crondaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cronie contains the standard UNIX daemon crond that runs specified
programs at scheduled times and related tools. It is based on the
original cron and has security and configuration enhancements like the
ability to use pam and SELinux.

%package anacron
Summary:	Utility for running regular jobs
Group:		Base

%description anacron
Anacron becames part of cronie. Anacron is used only for running
regular jobs. The default settings execute regular jobs by anacron,
however this could be overloaded in settings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SYSCRONTAB=/etc/crontab		\
	SYS_CROND_DIR=/etc/cron.d	\
	--enable-anacron		\
	--sysconfdir=/etc/cron		\
	--with-pam			\
	--without-audit			\
	--without-selinux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/{log,spool/{ana,}cron},%{_mandir}} \
	$RPM_BUILD_ROOT/etc/logrotate.d \
	$RPM_BUILD_ROOT%{_sysconfdir}/{cron,cron.{d,hourly,daily,weekly,monthly},pam.d}	\
	$RPM_BUILD_ROOT/%{_lib}/systemd/system

%{__make} install \
	pamdir=/etc/pam.d \
	DESTDIR=$RPM_BUILD_ROOT

cp -a contrib/0anacron $RPM_BUILD_ROOT/etc/cron.hourly/0anacron
cp -a %{SOURCE1} $RPM_BUILD_ROOT/%{_lib}/systemd/system/crond.service
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/cron
cp -a %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/crontab
cp -a %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/crond
cp -a %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/run-parts
touch $RPM_BUILD_ROOT/var/log/cron

cat > $RPM_BUILD_ROOT%{_sysconfdir}/cron/cron.allow << 'EOF'
# cron.allow	This file describes the names of the users which are
#		allowed to use the local cron daemon
root
EOF

cat > $RPM_BUILD_ROOT%{_sysconfdir}/cron/cron.deny << 'EOF'
# cron.deny	This file describes the names of the users which are
#		NOT allowed to use the local cron daemon
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 117 -r -f crontab

%post
if [ ! -f /var/log/cron ]; then
	install -m 660 -g crontab /dev/null /var/log/cron
fi
if [ "$1" = "1" ] ; then
    # initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    /bin/systemctl enable crond.service >/dev/null 2>&1 || :
fi

%preun
if [ "$1" = "0" ]; then
    /bin/systemctl --no-reload disable crond.service >/dev/null 2>&1 || :
    /bin/systemctl stop crond.service > /dev/null 2>&1 || :
fi

%postun
if [ "$1" = "0" ]; then
	%groupremove crontab
fi
if [ "$1" -ge "1" ]; then
    /bin/systemctl try-restart crond.service >/dev/null 2>&1 || :
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(2755,root,crontab) %{_bindir}/crontab
%attr(755,root,root) %{_bindir}/run-parts
%attr(640,root,crontab) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/cron/cron.allow
%attr(640,root,crontab) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/cron/cron.deny
%attr(640,root,crontab) %config(noreplace,missingok) /etc/cron.d/crontab
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/cron
%attr(750,root,crontab) %dir %{_sysconfdir}/cron*
%attr(755,root,root) %{_sbindir}/crond
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/crond
/%{_lib}/systemd/system/crond.service

%{_mandir}/man8/crond.8*
%{_mandir}/man8/cron.8*
%{_mandir}/man5/crontab.5*
%{_mandir}/man1/crontab.1*

%attr(1730,root,crontab) /var/spool/cron
%attr(660,root,crontab) %ghost /var/log/cron

%files anacron
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/anacron
%attr(755,root,root) %{_sysconfdir}/cron.hourly/0anacron
%attr(1730,root,crontab) /var/spool/anacron
%{_mandir}/man5/anacrontab.5*
%{_mandir}/man8/anacron.8*

