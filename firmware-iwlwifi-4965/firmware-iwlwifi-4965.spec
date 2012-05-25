%define		module	4965
#
Summary:	Microcode image for Intel Wireless WiFi Link 4965AGN Adapter
Name:		firmware-iwlwifi-%{module}
Version:	228.61.2.24
Release:	3
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{module}-ucode-%{version}.tgz
# Source0-md5:	2531028773cfc22aca5539c734f2a241
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for Intel Wireless WiFi Link 4965AGN Adapter.

%prep
%setup -qn iwlwifi-%{module}-ucode-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
install * $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.iwlwifi-%{module}-ucode
/lib/firmware/LICENSE.iwlwifi-%{module}-ucode
/lib/firmware/*.ucode

