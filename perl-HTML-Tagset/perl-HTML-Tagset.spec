%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Tagset
#
Summary:	This module contains data tables useful in dealing with HTML
Name:		perl-HTML-Tagset
Version:	3.20
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d2bfa18fe1904df7f683e96611e87437
URL:		http://search.cpan.org/dist/HTML-Tagset/
BuildRequires:	rpm-perlprov
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Tagset - This module contains data tables useful in dealing with
HTML. It provides no functions or methods.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/HTML/Tagset.pm
%{_mandir}/man3/*
