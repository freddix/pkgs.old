Summary:	OpenSSH free Secure Shell (SSH) implementation
Name:		openssh
Version:	5.9p1
Release:	1
Epoch:		2
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{name}-%{version}.tar.gz
# Source0-md5:	afe17eee7e98d3b8550cc349834a85d0
Source1:	%{name}d.pamd
Source2:	sshd@.service
Source3:	sshd.socket
Source4:	ssh-gen-keys.service
Patch0:		%{name}-config.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-pam_misc.patch
Patch3:		%{name}-sigpipe.patch
# http://chrootssh.sourceforge.net/download/osshChroot-3.7.1p2.diff
Patch4:		%{name}-chroot.patch
Patch5:		%{name}-include.patch
URL:		http://www.openssh.com/
BuildRequires:	perl-base
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
Requires:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/ssh
%define		_libexecdir	%{_libdir}/%{name}
%define		_privsepdir	/usr/share/empty

%description
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to seperate libraries (OpenSSL).

This package includes the core files necessary for both the OpenSSH
client and server. To make this package useful, you should also
install openssh-clients, openssh-server, or both.

%package clients
Summary:	OpenSSH Secure Shell protocol clients
Group:		Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	ssh-clients

%description clients
This package includes the clients necessary to make encrypted
connections to SSH servers.

%package server
Summary:	OpenSSH Secure Shell protocol server (sshd)
Group:		Networking/Daemons
Requires(post,preun,postun):	/bin/systemctl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	/bin/login
Requires:	pam
Requires:	util-linux
Provides:	ssh-server

%description server
This package contains the secure shell daemon. The sshd is the server
part of the secure shell protocol and allows ssh clients to connect to
your host.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cp /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
CPPFLAGS="-DCHROOT"
%configure \
	PERL=%{__perl}				\
	--disable-strip				\
	--with-4in6				\
	--with-ipaddr-display			\
	--with-mantype=man			\
	--with-md5-passwords			\
	--with-pam				\
	--with-pid-dir=%{_localstatedir}/run	\
	--with-privsep-path=%{_privsepdir}	\
	--with-privsep-user=nobody		\
	--with-ssl-engine			\
	--with-tcp-wrappers			\
	--with-xauth=/usr/bin/xauth

echo '#define LOGIN_PROGRAM "/bin/login"' >> config.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{pam.d,security,env.d},/%{_lib}/systemd/system} \
	$RPM_BUILD_ROOT%{_libexecdir}/ssh

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/sshd
install %{SOURCE2} $RPM_BUILD_ROOT/%{_lib}/systemd/system
install %{SOURCE3} $RPM_BUILD_ROOT/%{_lib}/systemd/system
install %{SOURCE4} $RPM_BUILD_ROOT/%{_lib}/systemd/system

install contrib/ssh-copy-id	$RPM_BUILD_ROOT%{_bindir}
install contrib/ssh-copy-id.1	$RPM_BUILD_ROOT%{_mandir}/man1

rm -f	$RPM_BUILD_ROOT%{_mandir}/man1/slogin.1
echo ".so ssh.1" > $RPM_BUILD_ROOT%{_mandir}/man1/slogin.1

%clean
rm -rf $RPM_BUILD_ROOT

%post clients
%env_update

%postun clients
%env_update

%post server
if ! grep -qs ssh /etc/security/passwd.conf ; then
	umask 022
	echo "ssh" >> /etc/security/passwd.conf
fi
if [ "$1" = "1" ]; then
    /bin/systemctl enable sshd.socket >/dev/null 2>&1 || :
    /bin/systemctl enable ssh-gen-keys.service >/dev/null 2>&1 || :
fi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%preun server
if [ "$1" = "0" ]; then
    /bin/systemctl disable sshd.socket >/dev/null 2>&1 || :
    /bin/systemctl disable ssh-gen-keys.service >/dev/null 2>&1 || :
    /bin/systemctl stop sshd.socket >/dev/null 2>&1 || :
fi

%postun server
if [ "$1" = "1" ]; then
    /bin/systemctl try-restart sshd.socket >/dev/null 2>&1 || :
fi

%files
%defattr(644,root,root,755)
%doc TODO README OVERVIEW CREDITS Change*

%dir %{_libexecdir}
%dir %{_sysconfdir}

%attr(755,root,root) %{_bindir}/ssh-key*
%{_mandir}/man1/ssh-key*.1*

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scp
%attr(755,root,root) %{_bindir}/sftp
%attr(755,root,root) %{_bindir}/slogin
%attr(755,root,root) %{_bindir}/ssh
%attr(755,root,root) %{_bindir}/ssh-add
%attr(755,root,root) %{_bindir}/ssh-agent
%attr(755,root,root) %{_bindir}/ssh-copy-id

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ssh_config

%{_mandir}/man1/scp.1*
%{_mandir}/man1/sftp.1*
%{_mandir}/man1/slogin.1*
%{_mandir}/man1/ssh-add.1*
%{_mandir}/man1/ssh-agent.1*
%{_mandir}/man1/ssh-copy-id.1*
%{_mandir}/man1/ssh.1*
%{_mandir}/man5/ssh_config.5*

%files server
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sshd_config
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/sshd
/%{_lib}/systemd/system/ssh-gen-keys.service
/%{_lib}/systemd/system/sshd.socket
/%{_lib}/systemd/system/sshd@.service
%attr(640,root,root) %{_sysconfdir}/moduli
%attr(755,root,root) %{_libexecdir}/sftp-server
%attr(755,root,root) %{_libexecdir}/ssh-keysign
%attr(755,root,root) %{_libexecdir}/ssh-pkcs11-helper
%attr(755,root,root) %{_sbindir}/sshd

%{_mandir}/man5/moduli.5*
%{_mandir}/man5/sshd_config.5*
%{_mandir}/man8/sftp-server.8*
%{_mandir}/man8/ssh-keysign.8*
%{_mandir}/man8/ssh-pkcs11-helper.8.gz
%{_mandir}/man8/sshd.8*

