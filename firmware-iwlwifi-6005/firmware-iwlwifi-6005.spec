%define		module	6005
%define		fware	6000g2a
#
Summary:	Microcode image for for Intel WiFi adapter
Name:		firmware-iwlwifi-%{module}
Version:	17.168.5.3
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{fware}-ucode-%{version}.tgz
# Source0-md5:	fe99ef72d4c016c9b04506fa474c1acd
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for for Intel Centrino Advanced-N 6205 adapter.

%prep
%setup -qn iwlwifi-6000g2a-ucode-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
install * $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.iwlwifi-%{fware}-ucode
/lib/firmware/LICENSE.iwlwifi-%{fware}-ucode
/lib/firmware/*.ucode

