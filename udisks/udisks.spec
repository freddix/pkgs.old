Summary:	Storage devices service
Name:		udisks
Version:	1.0.4
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	86c63b2b5484f2060499a052b5b6256b
Source1:	%{name}-tmpfiles.conf
Patch0:		%{name}-smartware.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	device-mapper-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libatasmart-devel
BuildRequires:	libtool
BuildRequires:	parted-devel
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	sg3_utils-devel
BuildRequires:	sqlite3-devel
BuildRequires:	udev-glib-devel
Requires:	polkit
Requires:	udev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/udisks
%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
udisks is a daemon that provide interfaces to obtain
information and perform operations on storage devices.

%package remote-access
Summary:	Remote access for udisks
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	avahi

%description remote-access
udisks development files.

%package devel
Summary:	udisks development files
Group:		Development
Requires:	dbus-glib-devel

%description devel
udisks development files.

%package apidocs
Summary:	udisks API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
udisks API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/polkit-1/extensions/*.la

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/tmpfiles.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_bindir}/udisks
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/udisks-daemon
%attr(755,root,root) %{_libexecdir}/udisks-helper-ata-smart-collect
%attr(755,root,root) %{_libexecdir}/udisks-helper-ata-smart-selftest
%attr(755,root,root) %{_libexecdir}/udisks-helper-change-filesystem-label
%attr(755,root,root) %{_libexecdir}/udisks-helper-change-luks-password
%attr(755,root,root) %{_libexecdir}/udisks-helper-create-partition
%attr(755,root,root) %{_libexecdir}/udisks-helper-create-partition-table
%attr(755,root,root) %{_libexecdir}/udisks-helper-delete-partition
%attr(755,root,root) %{_libexecdir}/udisks-helper-drive-benchmark
%attr(755,root,root) %{_libexecdir}/udisks-helper-drive-detach
%attr(755,root,root) %{_libexecdir}/udisks-helper-drive-poll
%attr(755,root,root) %{_libexecdir}/udisks-helper-fstab-mounter
%attr(755,root,root) %{_libexecdir}/udisks-helper-linux-md-check
%attr(755,root,root) %{_libexecdir}/udisks-helper-linux-md-remove-component
%attr(755,root,root) %{_libexecdir}/udisks-helper-mdadm-expand
%attr(755,root,root) %{_libexecdir}/udisks-helper-mkfs
%attr(755,root,root) %{_libexecdir}/udisks-helper-modify-partition

%attr(755,root,root) /%{_lib}/udev/udisks-dm-export
%attr(755,root,root) /%{_lib}/udev/udisks-part-id
%attr(755,root,root) /%{_lib}/udev/udisks-probe-ata-smart
%attr(755,root,root) /%{_lib}/udev/udisks-probe-sas-expander
%config(noreplace) %verify(not md5 mtime size) /%{_lib}/udev/rules.d/80-udisks.rules

%attr(755,root,root) /sbin/umount.udisks

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.UDisks.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks.service
%{_sysconfdir}/tmpfiles.d/%{name}.conf

%{_datadir}/polkit-1/actions/org.freedesktop.udisks.policy

%attr(700,root,root) %dir /var/lib/%{name}

%{_mandir}/man1/udisks.1*
%{_mandir}/man7/udisks.7*
%{_mandir}/man8/udisks-daemon.8*

%files remote-access
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/udisks-tcp-bridge
%{_mandir}/man1/udisks-tcp-bridge.1*
/etc/avahi/services/udisks.service

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/udisks.pc
%{_datadir}/dbus-1/interfaces/*.xml

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/udisks
%endif

