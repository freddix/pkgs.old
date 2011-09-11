Summary:	Rotates, compresses, removes and mails system log files
Name:		logrotate
Version:	3.8.1
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/l/o/logrotate/%{name}-%{version}.tar.gz
# Source0-md5:	bd2e20d8dc644291b08f9215397d28a5
BuildRequires:	popt-devel
Requires:	coreutils
Requires:	crondaemon
Requires:	gzip
Requires:	setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files. Logrotate
allows for the automatic rotation compression, removal and mailing of
log files. Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size. Normally,
logrotate runs as a daily cron job.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{cron.daily,logrotate.d} \
	$RPM_BUILD_ROOT{%{_mandir},%{_localstatedir},/var/log/archive}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_sbindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install examples/logrotate.cron $RPM_BUILD_ROOT/etc/cron.daily/logrotate
install examples/logrotate-default $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.conf
> $RPM_BUILD_ROOT%{_localstatedir}/logrotate.status
> $RPM_BUILD_ROOT/var/log/archiv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_sbindir}/logrotate
%attr(750,root,root) /etc/cron.daily/logrotate
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/logrotate.conf
%attr(640,root,root) %ghost %{_localstatedir}/logrotate.status
%attr(750,root,logs) %dir /var/log/archive
%ghost /var/log/archiv
%{_mandir}/man5/logrotate.conf.5*
%{_mandir}/man8/logrotate.8*

