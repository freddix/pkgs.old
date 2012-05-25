%define		intel_mcode_ver	20111110

Summary:	Intel CPU Microcode Utility
Name:		microcode_ctl
Version:	1.17
Release:	13
Epoch:		1
License:	GPL
Group:		Base
Source0:	http://www.urbanmyth.org/microcode/%{name}-%{version}.tar.gz
# Source0-md5:	98a7f06acef8459c8ef2a1b0fb86a99e
Source1:	http://downloadmirror.intel.com/20728/eng/microcode-%{intel_mcode_ver}.tgz
# Source1-md5:	ba288eb9490986513e59c5a035c93a65
Source2:	microcode.rules
Source3:	intel-microcode2ucode.c
Patch0:		%{name}-makefile.patch
URL:		http://www.urbanmyth.org/microcode/
Requires:	udev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The microcode_ctl utility is a companion to the IA32 microcode driver.
The utility has two uses: a) it decodes and sends new microcode to the
kernel driver to be uploaded to Intel IA32 family processors. (Pentium
Pro, PII, Celeron, PIII, Xeon Pentium 4 etc.) b) it signals the kernel
driver to release any buffers it may hold

The microcode update is volatile and needs to be uploaded on each
system boot i.e. it doesn't reflash your cpu permanently, reboot and
it reverts back to the old microcode.

%prep
%setup -q -a1
%patch0 -p1

%build
%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} -Wall \
	microcode_ctl.c -o microcode_ctl

%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} -Wall \
	%{SOURCE3} -o intel-microcode2ucode

./intel-microcode2ucode microcode.dat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/{firmware/intel-ucode,udev/rules.d}
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install	%{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE2} $RPM_BUILD_ROOT/lib/udev/rules.d/89-microcode.rules
cp intel-ucode/* $RPM_BUILD_ROOT/lib/firmware/intel-ucode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(640,root,root) /lib/firmware/intel-ucode
%attr(755,root,root) %{_sbindir}/*
/lib/udev/rules.d/89-microcode.rules
%{_mandir}/man?/*

