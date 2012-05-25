%define		module	6030
%define		fware	6000g2b

Summary:	Microcode image for for Intel WiFi adapters
Name:		firmware-iwlwifi-%{module}
Version:	18.168.6.1
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{fware}-ucode-%{version}.tgz
# Source0-md5:	98745515bd65e9cb34540da47b5a75d6
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for for Intel Centrino Advanced-N 6230,
Wireless-N 1030, Wireless-N 130 and Advanced-N 6235 adapters

%prep
%setup -qn iwlwifi-%{fware}-ucode-%{version}

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

