Summary:	Hewlett-Packard Linux Imaging and Printing Project
Name:		hplip
Version:	3.12.2
Release:	1
License:	BSD, GPL v2 and MIT
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/hplip/%{name}-%{version}.tar.gz
# Source0-md5:	6572ec99c1818cc92d97b793bff08633
Patch0:		%{name}-desktop.patch
URL:		http://hplipopensource.com/hplip-web/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libusb-devel
BuildRequires:	libusb-devel
BuildRequires:	openssl-devel
BuildRequires:	polkit-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-PyQt4
Requires:	python-PyQt4-QtDBus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cups_ppd_dir	%{_cups_dir}/model
%define 	_cups_dir	%(cups-config --datadir)
%define         _ulib_dir	%{_prefix}/lib

%description
The Hewlett-Packard Linux Imaging and Printing project (HPLIP)
provides a unified single and multi-function connectivity solution for
Linux. The goal of this project is to provide "radically simple"
printing, faxing, scanning, photo-card access, and device management
to the consumer and small business desktop Linux users.

%package libs
Summary:	HPLIP Libraries
Group:		Libraries

%description libs
HPLIP Libraries.

%package ppd
Summary:	PPD database for Hewlett Packard printers
Group:		Applications/System
Requires:	cups

%description ppd
PPD database for Hewlett Packard printers.

%package -n cups-backend-hp
Summary:	HP backend for CUPS
Group:		Applications/Printing
Requires:	%{name} = %{version}-%{release}
Requires:	cups
Requires:	foomatic-filters
Requires:	ghostscript-pstoraster

%description -n cups-backend-hp
This package allow CUPS printing on HP printers.

%prep
%setup -q
%patch0 -p1

sed -i 's,^#!/usr/bin/env python$,#!/usr/bin/python,' *.py
sed -i 's,chgrp.*,,g' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-fax-build			\
	--disable-qt3				\
	--disable-scan-build			\
	--enable-cups-ppd-install=yes		\
	--enable-network-build			\
	--enable-policykit			\
	--enable-qt4				\
	--enable-udev-acl-rules			\
	--with-hpppddir=%{_cups_ppd_dir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT		\
	drvdir=%{_cups_dir}/drivers	\
	rulesdir=/lib/udev/rules.d

rm -f $RPM_BUILD_ROOT%{_cups_ppd_dir}/*.ppd
rm -f $RPM_BUILD_ROOT%{_datadir}/hplip/hplip-install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/sane/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la
rm -rf $RPM_BUILD_ROOT/etc/sane.d

ln -sf %{_bindir}/foomatic-rip $RPM_BUILD_ROOT%{_ulib_dir}/cups/filter/foomatic-rip-hplip

mv -f $RPM_BUILD_ROOT/lib/udev/rules.d/{40-hplip.rules,70-hplip.rules}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/hp-align
%attr(755,root,root) %{_bindir}/hp-check
%attr(755,root,root) %{_bindir}/hp-clean
%attr(755,root,root) %{_bindir}/hp-colorcal
%attr(755,root,root) %{_bindir}/hp-devicesettings
%attr(755,root,root) %{_bindir}/hp-fab
%attr(755,root,root) %{_bindir}/hp-faxsetup
%attr(755,root,root) %{_bindir}/hp-firmware
%attr(755,root,root) %{_bindir}/hp-info
%attr(755,root,root) %{_bindir}/hp-levels
%attr(755,root,root) %{_bindir}/hp-linefeedcal
%attr(755,root,root) %{_bindir}/hp-makecopies
%attr(755,root,root) %{_bindir}/hp-makeuri
%attr(755,root,root) %{_bindir}/hp-mkuri
%attr(755,root,root) %{_bindir}/hp-pkservice
%attr(755,root,root) %{_bindir}/hp-plugin
%attr(755,root,root) %{_bindir}/hp-pqdiag
%attr(755,root,root) %{_bindir}/hp-print
%attr(755,root,root) %{_bindir}/hp-printsettings
%attr(755,root,root) %{_bindir}/hp-probe
%attr(755,root,root) %{_bindir}/hp-query
%attr(755,root,root) %{_bindir}/hp-scan
%attr(755,root,root) %{_bindir}/hp-sendfax
%attr(755,root,root) %{_bindir}/hp-setup
%attr(755,root,root) %{_bindir}/hp-systray
%attr(755,root,root) %{_bindir}/hp-testpage
%attr(755,root,root) %{_bindir}/hp-timedate
%attr(755,root,root) %{_bindir}/hp-toolbox
%attr(755,root,root) %{_bindir}/hp-unload
%attr(755,root,root) %{_bindir}/hp-wificonfig

%attr(755,root,root) %{py_sitedir}/cupsext.so
%attr(755,root,root) %{py_sitedir}/hpmudext.so
%attr(755,root,root) %{py_sitedir}/pcardext.so

%attr(755,root,root) %{_ulib_dir}/cups/filter/hplipjs

%dir %{_sysconfdir}/hp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hp/*

%{_datadir}/dbus-1/system-services/com.hp.hplip.service
%{_datadir}/polkit-1/actions/com.hp.hplip.policy
%{_sysconfdir}/dbus-1/system.d/com.hp.hplip.conf

%dir %{_datadir}/hplip
%dir %{_datadir}/hplip/base
%dir %{_datadir}/hplip/copier
%dir %{_datadir}/hplip/installer
%dir %{_datadir}/hplip/pcard
%dir %{_datadir}/hplip/prnt
%dir %{_datadir}/hplip/ui4

%dir /var/lib/hp
%ghost /var/lib/hp/hplip.state

%attr(755,root,root) %{_datadir}/hplip/*.py
%attr(755,root,root) %{_datadir}/hplip/base/*.py
%attr(755,root,root) %{_datadir}/hplip/copier/*.py
%attr(755,root,root) %{_datadir}/hplip/installer/*.py
%attr(755,root,root) %{_datadir}/hplip/pcard/*.py
%attr(755,root,root) %{_datadir}/hplip/prnt/*.py
%attr(755,root,root) %{_datadir}/hplip/ui4/*.py

%{_datadir}/hplip/installer/*.dat
%{_datadir}/hplip/data
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libhpip.so.?
%attr(755,root,root) %ghost %{_libdir}/libhpmud.so.?
%attr(755,root,root) %{_libdir}/libhpip.so.*.*.*
%attr(755,root,root) %{_libdir}/libhpmud.so.*.*.*

%files ppd
%defattr(644,root,root,755)
%{_cups_ppd_dir}/*.ppd.gz

%files -n cups-backend-hp
%defattr(644,root,root,755)
%{_datadir}/cups/drivers/hpcups.drv
%attr(755,root,root) %{_ulib_dir}/cups/backend/hp
%attr(755,root,root) %{_ulib_dir}/cups/filter/foomatic-rip-hplip
%attr(755,root,root) %{_ulib_dir}/cups/filter/hpcac
%attr(755,root,root) %{_ulib_dir}/cups/filter/hpcups
%attr(755,root,root) %{_ulib_dir}/cups/filter/hplipjs
%attr(755,root,root) %{_ulib_dir}/cups/filter/pstotiff
/lib/udev/rules.d/70-hplip.rules

