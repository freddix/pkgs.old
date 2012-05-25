%define		module	5000
#
Summary:	Microcode image for Intel Wireless WiFi 5100AGN, 5300AGN, and 5350AGN
Name:		firmware-iwlwifi-%{module}
Version:	8.24.2.12
Release:	3
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{module}-ucode-%{version}.tgz
# Source0-md5:	45f74d052d52f6f473dc7a8d412f2274
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for Intel Wireless WiFi 5100AGN, 5300AGN, and 5350AGN.

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

