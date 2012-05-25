%define		module	6000
#
Summary:	Microcode image for Intel 6000 Series Wi-Fi Adapters 
Name:		firmware-iwlwifi-%{module}
Version:	9.221.4.1
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-%{module}-ucode-%{version}.tgz
# Source0-md5:	c132a4c1946a9dbc0c36b41696e5c793
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode image for Intel %{module} Series Wi-Fi Adapters.

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

