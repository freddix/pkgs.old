%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Parser
#
Summary:	HTML::Parser - parsing and extracting information from HTML documents
Name:		perl-HTML-Parser
Version:	3.69
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d22cc6468ce670a56034be907e4e7c54
URL:		http://search.cpan.org/dist/HTML-Parser/
BuildRequires:	perl-HTML-Tagset
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# HTTP::Headers (perl-libwww) is not always required
%define		_noautoreq	'perl(HTTP::Headers)'

%description
Perl module HTML::Parser that allows to parse and extract information
from HTML documents.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	DEFINE="-DMARKED_SECTION -DUNICODE_ENTITIES" \
	< /dev/null

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%dir %{perl_vendorarch}/HTML
%{perl_vendorarch}/HTML/*.pm
%dir %{perl_vendorarch}/auto/HTML
%dir %{perl_vendorarch}/auto/HTML/Parser
%{perl_vendorarch}/auto/HTML/Parser/Parser.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Parser/Parser.so
%{_mandir}/man3/*

