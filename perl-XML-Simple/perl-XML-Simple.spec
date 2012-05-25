%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Simple
#
Summary:	XML::Simple - easy API to read/write XML (esp config files)
Name:		perl-XML-Simple
Version:	2.18
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	593aa8001e5c301cdcdb4bb3b63abc33
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
Requires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML::Simple module provides a simple API layer on top of an
underlying XML parsing module (either XML::Parser or one of the SAX2
parser modules).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/Simple.pm

