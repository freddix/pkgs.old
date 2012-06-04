Summary:	Utilities to manage the passwd and shadow user information
Name:		pwdutils
Version:	3.2.19
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
Source0:	http://www.linux-nis.org/download/pwdutils/%{name}-%{version}.tar.bz2
# Source0-md5:	25a77a0ab376eacf24ad5eab7af4cdce
Source1:	%{name}.useradd
Source2:	%{name}.login.defs
Source10:	%{name}-chage.pamd
Source11:	%{name}-chfn.pamd
Source12:	%{name}-chsh.pamd
Source13:	%{name}-passwd.pamd
Source14:	%{name}-useradd.pamd
Source15:	%{name}-userdb.pamd
Patch0:		%{name}-f-option.patch
Patch1:		%{name}-no_bash.patch
Patch2:		%{name}-silent_crontab.patch
URL:		http://www.thkukuk.de/pam/pwdutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	libnscd-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
Requires:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for pam module in /%{_lib}/security
%define		_libdir		/%{_lib}

%description
pwdutils is a collection of utilities to manage the passwd and shadow
user information. The difference to the shadow suite is that these
utilities can also modify the information stored in NIS, NIS+, or
LDAP. PAM is used for user authentication and changing the pasword. It
contains passwd, chage, chfn, chsh, and a daemon for changing the
password on a remote machine over a secure SSL connection. The daemon
also uses PAM so that it can change passwords independent of where
they are stored.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-ldap		\
	--disable-pam_rpasswd	\
	--disable-rpath		\
	--disable-selinux	\
	--disable-static	\
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pwdutils,security,skel/tmp}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sbindir}/*.local $RPM_BUILD_ROOT%{_sysconfdir}/pwdutils
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/default/useradd
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/login.defs

install %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/chage
install %{SOURCE11} $RPM_BUILD_ROOT/etc/pam.d/chfn
install %{SOURCE12} $RPM_BUILD_ROOT/etc/pam.d/chsh
install %{SOURCE13} $RPM_BUILD_ROOT/etc/pam.d/passwd
install %{SOURCE14} $RPM_BUILD_ROOT/etc/pam.d/useradd
install %{SOURCE15} $RPM_BUILD_ROOT/etc/pam.d/shadow

rm -f $RPM_BUILD_ROOT%{_libdir}/pwdutils/*.la
rm -f $RPM_BUILD_ROOT/etc/init.d/rpasswdd

:> $RPM_BUILD_ROOT%{_sysconfdir}/shadow
:> $RPM_BUILD_ROOT/etc/security/chfn.allow
:> $RPM_BUILD_ROOT/etc/security/chsh.allow

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shadow ]; then
	%{_sbindir}/pwconv
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO

%attr(4755,root,root) %{_bindir}/chfn
%attr(4755,root,root) %{_bindir}/chsh
%attr(4755,root,root) %{_bindir}/expiry
%attr(4755,root,root) %{_bindir}/gpasswd
%attr(4755,root,root) %{_bindir}/passwd

%attr(755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/newgrp
%attr(4755,root,root) %{_bindir}/sg

%attr(755,root,root) %{_sbindir}/chpasswd
%attr(755,root,root) %{_sbindir}/groupadd
%attr(755,root,root) %{_sbindir}/groupdel
%attr(755,root,root) %{_sbindir}/groupmod
%attr(755,root,root) %{_sbindir}/grpck
%attr(755,root,root) %{_sbindir}/grpconv
%attr(755,root,root) %{_sbindir}/grpunconv
%attr(755,root,root) %{_sbindir}/pwck
%attr(755,root,root) %{_sbindir}/pwconv
%attr(755,root,root) %{_sbindir}/pwunconv
%attr(755,root,root) %{_sbindir}/useradd
%attr(755,root,root) %{_sbindir}/userdel
%attr(755,root,root) %{_sbindir}/usermod
%attr(755,root,root) %{_sbindir}/vigr
%attr(755,root,root) %{_sbindir}/vipw

%attr(755,root,root) %{_libdir}/pwdutils/liblog_syslog.so*

%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/shadow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/logging
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chage
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chfn
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/chsh
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/passwd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/shadow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/useradd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/chfn.allow
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/chsh.allow
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.local

%attr(750,root,root) %dir %{_sysconfdir}/%{name}
%attr(750,root,root) %dir %{_sysconfdir}/default

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/login.defs

%dir %{_libdir}/pwdutils
%dir /etc/skel
%dir /etc/skel/tmp

%{_mandir}/man?/*

