Summary:	Post-processing scanned and photocopied book pages
Name:		unpaper
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.berlios.de/unpaper/%{name}-%{version}.tar.gz
# Source0-md5:	be41eaf8556e7df39ab53939c99c4f7b
URL:		http://unpaper.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously
created photocopies. The main purpose is to make scanned book pages
better readable on screen after conversion to PDF.
Additionally, unpaper might be useful to enhance the quality
of scanned pages before performing optical character recognition (OCR).

%prep
%setup -q

%build
%{__cc} %{rpmcflags} -o unpaper %{rpmldflags} src/unpaper.c -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unpaper $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README doc
%attr(755,root,root) %{_bindir}/unpaper

