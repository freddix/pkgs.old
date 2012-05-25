%define		module	1000
#
Summary:	Microcode image for Intel Wireless WiFi Link 1000BGN Adapter
Name:		firmware-iwlwifi-%{module}
Version:	128.50.3.1
Release:	3
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{module}-ucode-%{version}.tgz
# Source0-md5:	cfad8d5a7651dde665c5c23e8209c35d
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for Intel Wireless WiFi Link 1000BGN Adapter.

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

