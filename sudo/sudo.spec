Summary:	Allows command execution as root for specified users
Name:		sudo
Version:	1.8.5p2
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.sudo.ws/pub/sudo/%{name}-%{version}.tar.gz
# Source0-md5:	dc42ed9f0946d92273762d0ae7314d59
Source1:	%{name}.pamd
Source2:	%{name}.logrotate
Patch0:		%{name}-ac.patch
URL:		http://www.sudo.ws/sudo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pam-devel
Requires:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Sudo (superuser do) allows a permitted user to execute a command as
the superuser (real and effective uid and gid are set to 0 and root's
group as set in the passwd file respectively).

Sudo determines who is an authorized user by consulting the file
/etc/sudoers. By giving sudo the -v flag a user can update the time
stamp without running a command. The password prompt itself will also
time out if the password is not entered with N minutes (again, this is
defined at installation time and defaults to 5 minutes).

%prep
%setup -q

# only local macros
mv -f aclocal.m4 acinclude.m4
# kill libtool.m4 copy
rm -f acsite.m4

%build
%configure \
	NROFFPROG=nroff		\
	--with-all-insults	\
	--with-env-editor	\
	--with-logfac=auth	\
	--without-kerb5		\
	--without-ldap		\
	--with-secure-path="/bin:/sbin:/usr/bin:/usr/sbin"	\
	--without-skey
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{pam.d,logrotate.d},/var/{log,run/sudo}}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT	\
	install_uid=`id -u`	\
	install_gid=`id -g`	\
	sudoers_uid=`id -u`	\
	sudoers_gid=`id -g`

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/sudo
touch $RPM_BUILD_ROOT/var/log/sudo
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/sudo

chmod -R +r $RPM_BUILD_ROOT%{_prefix}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{HISTORY,TROUBLESHOOTING,sample.*} README
%attr(440,root,root) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/sudoers
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/sudo
%attr(4755,root,root) %{_bindir}/sudo*
%attr(755,root,root) %{_sbindir}/visudo
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/*.so
%{_mandir}/man*/*
%attr(600,root,root) %ghost /var/log/sudo
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*

