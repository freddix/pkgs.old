%include	/usr/lib/rpm/macros.perl
#
Summary:	LaTeX automation frontend
Name:		latexmk
Version:	4.26
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.phys.psu.edu/~collins/software/latexmk-jcc/%{name}-426.zip
# Source0-md5:	b0cc244f430330456828a4c11b85026b
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Latexmk completely automates the process of generating a LaTeX
document.  Essentially, it is a highly specialized cousin of the
general make utility.  Given the source files for a document, latexmk
issues the appropriate sequence of commands to generate a .dvi, .ps,
.pdf or hardcopy version of the document, including repeated running
of the programs until cross references etc are resolved.  Latexmk can
also be set to run continuously with a previewer; the latex program,
etc, are rerun whenever one of the source files is modified.

%prep
%setup -qc %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install latexmk.pl -D $RPM_BUILD_ROOT%{_bindir}/latexmk
install latexmk.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/latexmk.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README example_rcfiles/ extra-scripts/
%attr(755,root,root) %{_bindir}/latexmk
%{_mandir}/man1/latexmk.1*

