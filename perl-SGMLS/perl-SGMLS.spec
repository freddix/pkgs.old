%include	/usr/lib/rpm/macros.perl
#
Summary:	SGMLS - postprocessing the output from the SGMLS and NSGMLS parsers
Name:		perl-SGMLS
Version:	1.03ii
Release:	23
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.gz
# Source0-md5:	5bcb197fd42e67d51c739b1414d514a7
BuildRequires:	rpm-perlprov
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains SGMLS.pm, a perl5 class library for parsing
the output from James Clark's SGMLS and NSGMLS parsers.

%prep
# empty

%setup -q -n SGMLSpm
mkdir -p lib/SGMLS
mv Output.pm Refs.pm skel.pl lib/SGMLS
mv SGMLS.pm lib
mv sgmlspl.pl sgmlspl
mv test-SGMLS.pl test.pl

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -wle 'WriteMakefile(NAME=>"SGMLS", EXE_FILES=>["sgmlspl"])' \
	INSTALLDIRS=vendor
%{__make}

%if 0
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README BUGS TODO DOC/*sgml DOC/*pl elisp
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SGMLS.pm
%{perl_vendorlib}/SGMLS
%{_mandir}/man3/*

