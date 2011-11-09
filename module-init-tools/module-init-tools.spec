Summary:	Linux userspace module loading utilities
Name:		module-init-tools
Version:	3.16
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://kernel.org/pub/linux/utils/kernel/module-init-tools/%{name}-%{version}.tar.gz
# Source0-md5:	743d2511a639814fa428b82b9f659e4f
Source1:	%{name}-blacklist
Source2:	%{name}-usb
Patch0:		%{name}-insmod-zlib.patch
Patch1:		%{name}-modprobe_d.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-static
BuildRequires:	zlib-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/sbin
%define		_sbindir	/sbin

%description
The module-init-tools are used by modern 2.6 series Linux systems to
provideuserspace-side assistance in loading kernel modules and their
dependencies. Originally written to replace the older "modutils",
the utilities include the "modprobe" (load modules and their
dependencies), "insmod" (load just a single module), "modinfo"
(retrieve module information), and other related module management
commands. These are intended to be relatively lightweight in their
design, since 2.6 series kernels do much of the work internally.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/modprobe.d,%{_mandir}/man{5,8}}

%{__make} install install-am \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	INSTALL=install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/modprobe.d/blacklist.conf
install %{SOURCE2} $RPM_BUILD_ROOT/etc/modprobe.d/usb.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{_sysconfdir}/modprobe.d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/modprobe.d/blacklist.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/modprobe.d/usb.conf
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*

