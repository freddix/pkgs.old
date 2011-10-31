Summary:	Set of common Unix utilities for embeded systems
Name:		busybox
Version:	1.19.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	c3938e1ac59602387009bbf1dd1af7f6
Source1:	%{name}-initrd.config
Source2:	%{name}-huge.config
Patch0:		%{name}-logconsole.patch
Patch1:		%{name}-printf-gettext.patch
Patch2:		%{name}-kernel_headers.patch
URL:		http://www.busybox.net/
BuildRequires:	perl-tools-pod
BuildRequires:	uClibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_initrd_bindir	/lib/initrd-utils/bin

%description
BusyBox combines tiny versions of many common UNIX utilities into a
single small executable. It provides minimalist replacements for most
of the utilities you usually find in fileutils, shellutils, findutils,
textutils, grep, gzip, tar, etc. BusyBox provides a fairly complete
POSIX environment for any small or embedded system. The utilities in
BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts.

BusyBox has been written with size-optimization and limited resources
in mind. It is also extremely modular so you can easily include or
exclude commands (or features) at compile time. This makes it easy to
customize your embedded systems. To create a working system, just add
a kernel, a shell (such as ash), and an editor (such as elvis-tiny or
ae).

%package initrd
Summary:	Static busybox for initrd
Group:		Applications

%description initrd
Static busybox for initrd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's|#!/bin/sh|#!/bin/bash|' scripts/gen_build_files.sh

%build
install -d built
install %{SOURCE1} .config

# initrd
%{__make} oldconfig
%{__make} \
	CC="%{_target_cpu}-uclibc-gcc"	\
	LDFLAGS="%{rpmldflags} -static"	\
	V=1

mv -f busybox_unstripped built/busybox.initrd
%{__make} distclean

# huge
install %{SOURCE2} .config
%{__make} oldconfig
%{__make} -j1 \
	CC="%{_target_cpu}-uclibc-gcc"	\
	LDFLAGS="%{rpmldflags} -static"	\
	V=1

%{__make} busybox.links docs/busybox.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_initrd_bindir}/bin,%{_bindir},%{_mandir}/man1,%{_libdir}/busybox}

install built/busybox.initrd $RPM_BUILD_ROOT%{_initrd_bindir}/busybox
install busybox_unstripped $RPM_BUILD_ROOT%{_bindir}/busybox
ln -sf %{_bindir}/busybox $RPM_BUILD_ROOT%{_bindir}/vi

install busybox.links $RPM_BUILD_ROOT%{_libdir}/busybox
install docs/busybox.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README .config
%attr(755,root,root) %{_bindir}/vi
%attr(755,root,root) %{_bindir}/busybox
%{_libdir}/busybox
%{_mandir}/man1/*

%files initrd
%defattr(644,root,root,755)
%attr(755,root,root) %{_initrd_bindir}/busybox

