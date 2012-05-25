%define		module	3945
#
Summary:	Microcode image for Intel PRO/Wireless 3945ABG/BG Adapter
Name:		firmware-iwlwifi-%{module}
Version:	15.32.2.9
Release:	3
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{module}-ucode-%{version}.tgz
# Source0-md5:	d99a75ab1305d1532a09471b2f9a547a
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for Intel PRO/Wireless 3945ABG/BG Adapter.

%prep
%setup -qn iwlwifi-%{module}-ucode-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
install * $RPM_BUILD_ROOT/lib/firmware

ln -sf iwlwifi-3945-2.ucode $RPM_BUILD_ROOT/lib/firmware/iwlwifi-3945-1.ucode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.iwlwifi-%{module}-ucode
/lib/firmware/LICENSE.iwlwifi-%{module}-ucode
/lib/firmware/iwlwifi-3945-1.ucode
/lib/firmware/iwlwifi-3945-2.ucode

