Summary:	A tool for converting text files to various formats
Name:		asciidoc
Version:	8.6.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/asciidoc/%{name}-%{version}.tar.gz
# Source0-md5:	9247724283501ec1cfb27d5eae9e5eaf
URL:		http://www.methods.co.nz/asciidoc/index.html
Requires:	python
Requires:	python-modules
Requires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AsciiDoc is a text document format for writing short documents,
articles, books and UNIX man pages. AsciiDoc files can be translated
to HTML (with or without stylesheets), DocBook and LinuxDoc markup
using the asciidoc(1) command. AsciiDoc is highly configurable: both
the AsciiDoc source file syntax and the backend output markups (which
can be almost any type of SGML/XML markup) can be customized and
extended by the user.

%prep
%setup -q

sed -i -e '1s|^#!/usr/bin/env python|#!/usr/bin/python|' *.py

%build
%configure \
	--sysconfdir="%{_datadir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README
%attr(755,root,root) %{_bindir}/a2x
%attr(755,root,root) %{_bindir}/asciidoc
%attr(755,root,root) %{_bindir}/a2x.py
%attr(755,root,root) %{_bindir}/asciidoc.py
%{_datadir}/%{name}
%{_mandir}/man1/*

