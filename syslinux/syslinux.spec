Summary:	Simple bootloader
Name:		syslinux
Version:	4.04
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	a3936208767eb7ced65320abe2e33a10
URL:		http://syslinux.zytor.com/
BuildRequires:	nasm
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
Requires:	mtools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
SYSLINUX is a boot loader for the Linux operating system which
operates off MS-DOS floppies. It is intended to simplify first-time
installation of Linux, rescue disks, and other uses for boot floppies.
A SYSLINUX floppy can be manipulated using standard MS-DOS (or any
other OS that can access an MS-DOS filesystem) tools once it has been
created, and requires only a ~ 7K DOS program or ~ 13K Linux program
to create it in the first place. It also includes PXELINUX, a program
to boot off a network server using a boot PROM compatible with the
Intel PXE (Pre-Execution Environment) specification.

%package devel
Summary:	Header files for syslinux libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description devel
This package includes the header files needed for compilation of
applications that are making use of the syslinux internals. Install
this package only if you plan to develop or will need to compile
customized syslinux clients.

%prep
%setup -q

sed -i 's/-march=i386//' sample/Makefile
sed -i 's/FPNG_NO_WRITE_SUPPORTED/DPNG_NO_WRITE_SUPPORTED/' com32/lib/MCONFIG

%build
rm -f ldlinux.{bin,bss,lst,sys}
%{__make} -j1 installer \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_includedir}}
install core/ldlinux.sys $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} -j1 install-all \
	INSTALLROOT=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir}

rm -fr $RPM_BUILD_ROOT/{boot,tftpboot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README* doc/*.txt
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/diag
%{_datadir}/%{name}/dosutil

%{_datadir}/%{name}/*.0
%{_datadir}/%{name}/*.bin
%{_datadir}/%{name}/*.c32
%{_datadir}/%{name}/*.com
%{_datadir}/%{name}/*.exe
%{_datadir}/%{name}/*.sys
%{_datadir}/%{name}/memdisk

%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_datadir}/%{name}/com32

