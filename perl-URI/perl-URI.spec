%define		pdir	URI
%define		pnam	URI

%include	/usr/lib/rpm/macros.perl

Summary:	URI - Uniform Resource Identifiers (absolute and relative)
Name:		perl-URI
Version:	1.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	70f739be8ce28b8baba7c5920ffee4dc
URL:		http://search.cpan.org/dist/URI/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	perl-MIME-Base64
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Business::ISBN)'

%description
This package contains the URI.pm module with friends. The module
implements the URI class. Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

%prep
%setup -q -n %{pnam}-%{version}
mv t/heuristic.t{,.blah}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%check
%{__make} test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/URI
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
