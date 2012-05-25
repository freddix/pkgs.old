Summary:	Dictionaries for use with hunspell
Name:		hunspell-dictionaries
Version:	1.0
Release:	14
License:	GPL v2
Group:		Applications/Text
Source0:	http://pl.openoffice.org/pliki/pl_PL.zip
# Source0-md5:	55395f6ec92a8edd70924e2700e32fbf
Source1:	http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/de_DE_frami.zip
# Source1-md5:	ebaa2489e42d6a75f51aaa8c06a54784
Source2:	http://en-gb.pyxidium.co.uk/dictionary/en_GB.zip
# Source2-md5:	218909136738f4564b81ecd145ade6ee
Requires:	hunspell
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -qc -a1 -a2

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/myspell

mv de_DE_frami.aff de_DE.aff
mv de_DE_frami.dic de_DE.dic

install *.aff $RPM_BUILD_ROOT%{_datadir}/myspell
install *.dic $RPM_BUILD_ROOT%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README_de_DE_frami.txt README_en_GB.txt README_pl_PL.txt
%{_datadir}/myspell/*

