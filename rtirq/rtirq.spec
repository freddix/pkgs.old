Summary:	Realtime IRQ thread system tunning
Name:		rtirq
Version:	20120505
Release:	1
License:	GPL v2
Group:		System/Applications
Source0:	http://www.rncbc.org/jack/%{name}-%{version}.tar.gz
# Source0-md5:	1228311c17fe91921689a2bf10b21ce5
BuildArch:	noarch
Requires:	schedtool
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup scripts for tunning the realtime scheduling policy
and priority of relevant IRQ service threads, featured for
a realtime-preempt enabled kernel configuration.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D rtirq.conf $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install -D rtirq.sh $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(754,root,root) %{_sbindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

