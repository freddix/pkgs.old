Summary:	Remote mail fetch daemon for POP2, POP3, APOP, IMAP
Name:		fetchmail
Version:	6.3.21
Release:	1
License:	GPL
Group:		Applications/Mail
#Source0Download: http://developer.berlios.de/project/showfiles.php?group_id=1824
Source0:	http://download2.berlios.de/fetchmail/%{name}-%{version}.tar.xz
# Source0-md5:	db75ef2058423599386add311bc954ce
URL:		http://fetchmail.berlios.de/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fetchmail is a program that is used to retrieve mail from a remote
mail server. It can use the Post Office Protocol (POP) or IMAP
(Internet Mail Access Protocol) for this, and delivers the mail
through the local SMTP server (normally sendmail).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	procmail=%{_bindir}/procmail	\
	--disable-rpath			\
	--enable-NTLM			\
	--enable-RPA			\
	--enable-SDPS			\
	--enable-fallback=procmail	\
	--enable-nls			\
	--with-ssl=%{_prefix}		\
	--without-kerberos
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/fetchmailconf.1

%find_lang %{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FEATURES README NEWS NOTES README.NTLM *.html FAQ
%attr(755,root,root) %{_bindir}/fetchmail
%{_mandir}/man1/fetchmail.1*

