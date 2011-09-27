Summary:	Key management application for SSH RSA/DSA keys
Name:		keychain
Version:	2.7.1
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.funtoo.org/archive/keychain/%{name}-%{version}.tar.bz2
# Source0-md5:	07c622833192189f483cbaec287f9704
URL:		http://www.funtoo.org/en/security/keychain/intro/
Requires:	openssh-clients
Requires:	sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keychain is an extremely handy OpenSSH and commercial SSH2-compatible
RSA/DSA key management application. It acts as a front-end to
ssh-agent, allowing you to easily have one long-running ssh-agent
process per system, rather than per login session. This dramatically
reduces the number of times you need to enter your passphrase from
once per new login session to once every time your local machine is
rebooted.

%prep
%setup -q

%build
%{__make} keychain.1 keychain

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p keychain $RPM_BUILD_ROOT%{_bindir}/keychain
cp -a keychain.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.rst
%attr(755,root,root) %{_bindir}/keychain
%{_mandir}/man1/keychain.1*

