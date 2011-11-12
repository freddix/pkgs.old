Summary:	Set of GIMP scripts
Name:		gimp-scripts
Version:	34
Release:	1
License:	GPL/other
Group:		Applications
Source0:	http://www.gimphelp.org/DL/gimp_scripts_26.tar.bz2
# Source0-md5:	bede21dc4d1e68ed9282f38a320fbc97
BuildRequires:	gimp-devel
BuildArch:	noarch
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		presetsdir	%(gimptool --gimpdatadir)/gimpressionist/Presets
%define		scriptsdir	%(gimptool --gimpdatadir)/scripts

%description
A set of verious and useful GIMP scripts.

%prep
%setup -qn gimp_scripts_26

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{presetsdir},%{scriptsdir}}

install *.scm $RPM_BUILD_ROOT%{scriptsdir}
install Presets/*.txt $RPM_BUILD_ROOT%{presetsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{scriptsdir}/*.scm
%{presetsdir}/*.txt

