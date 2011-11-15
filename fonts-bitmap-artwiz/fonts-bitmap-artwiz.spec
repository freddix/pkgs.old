Summary:	Alec Zapka's Artwiz bitmap fonts
Name:		fonts-bitmap-artwiz
Version:	1.3
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	http://downloads.sourceforge.net/sourceforge/artwizaleczapka/artwiz-aleczapka-en-%{version}.tar.bz2
# Source0-md5:	6c6c704f2f08f9d6308d366423dfa90e
Source1:	http://downloads.sourceforge.net/sourceforge/artwizaleczapka/artwiz-aleczapka-de-%{version}.tar.bz2
# Source1-md5:	c5a9d0ad3d1b99809c77d84139949993
Source2:	http://downloads.sourceforge.net/sourceforge/artwizaleczapka/artwiz-aleczapka-se-%{version}.tar.bz2
# Source2-md5:	dfc861c4f54e73eea3fd82d60be26dbc
URL:		http://artwizaleczapka.sourceforge.net/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_miscfontsdir	%{_fontsdir}/misc

%description
This package contains artwiz bitmap fonts (PCF) updated and expanded
by Alec Zapka.

%prep
%setup -qc -a1 -a2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_miscfontsdir}
install */*.pcf $RPM_BUILD_ROOT%{_miscfontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc artwiz-aleczapka-en-1.3/{README,AUTHORS,ChangeLog}
%doc artwiz-aleczapka-de-1.3/README.DE
%doc artwiz-aleczapka-se-1.3/README.SE
%{_miscfontsdir}/*

