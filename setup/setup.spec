%define		iana_etc_ver	2.30
%undefine	with_ccache
#
Summary:	Simple setup files
Name:		setup
Version:	2.6.2
Release:	20
License:	Public Domain, partially BSD-like
Group:		Base
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ebd20f3ea4d766cfe16d2abf253224ac
Source1:	http://sethwklein.net/projects/iana-etc/downloads/iana-etc-%{iana_etc_ver}.tar.bz2
# Source1-md5:	3ba3afb1d1b261383d247f46cb135ee8
Patch0:		%{name}-iana-etc.patch
# This is source of non-iana changes in services file
Patch1:		%{name}-freddix.patch
Patch2:		%{name}-services.patch
Patch3:		%{name}-more-group.patch
BuildRequires:	uClibc-static
BuildRequires:	gawk
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		specflags	-Os

%description
This package contains a number of very important configuration and
setup files, including the passwd, group, profile files, etc.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch3 -p1

mv iana-etc{-%{iana_etc_ver},}

%build
%{__make} -C iana-etc
%{__patch} iana-etc/services %{PATCH2}
%{__sed} -i -e 's,[ \t]\+$,,' iana-etc/services

%{__make} \
	OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags} -static" \
	CC="%{_target_cpu}-uclibc-gcc"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a iana-etc/protocols $RPM_BUILD_ROOT%{_sysconfdir}/protocols

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -p /sbin/postshell -- %{name} < %{version}-%{release}
%{_sbindir}/joinpasswd
%{_sbindir}/delpasswd -g ttyS cdwrite


%post -p /sbin/postshell
-/sbin/env-update -u

%postun -p /sbin/postshell
-/sbin/env-update -u

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/delpasswd
%attr(755,root,root) %{_sbindir}/joinpasswd
%attr(755,root,root) %{_sbindir}/postshell
%attr(755,root,root) %{_sbindir}/update-fstab
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) /etc/profile.d/*.sh
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(755,root,root) /etc/profile.d/*.csh
%dir /etc/profile.d
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/env.d/*
%dir %{_sysconfdir}/env.d
%dir %{_sysconfdir}/shrc.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fstab
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/group
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/host.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/passwd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/profile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/protocols
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/secure*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/services
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/filesystems
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/motd
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/resolv.conf
%ghost %{_sysconfdir}/shells

