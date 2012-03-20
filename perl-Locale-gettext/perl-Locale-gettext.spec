%define		pdir	Locale
%define		pnam	gettext

%include	/usr/lib/rpm/macros.perl

Summary:	Locale::gettext Perl module - message handling functions
Name:		perl-Locale-gettext
Version:	1.05
Release:	15
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	f3d3f474a1458f37174c410dfef61a46
URL:		http://search.cpan.org/dist/gettext/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::gettext is a Perl 5 module quickly written to gain access to
the C library functions for internatialization.  They work just like
the C versions.

%prep
%setup -qn %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Locale/*
%dir %{perl_vendorarch}/auto/Locale/gettext
%{perl_vendorarch}/auto/Locale/gettext/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/gettext/*.so
%{_mandir}/man3/*

