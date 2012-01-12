Summary:	A framework for defining policy for system-wide components
Name:		polkit
Version:	0.102
Release:	3
License:	MIT
Group:		Libraries
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a3726bdb9728c103e58f62131e26693a
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	expat-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkg-config
BuildRequires:	xmlto
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ConsoleKit
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
PolicyKit is a framework for defining policy for system-wide
components and for desktop pieces to configure it. It is used by HAL.

%package libs
Summary:	PolicyKit libraries
Group:		Libraries

%description libs
PolicyKit libraries.

%package devel
Summary:	Header files for PolicyKit
Group:		Development/Libraries
Requires:	%{name}-gir = %{version}-%{release}

%description devel
Header files for PolicyKit.

%package apidocs
Summary:	PolicyKit API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
PolicyKit API documentation.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gobject-introspection-data

%description gir
GObject introspection data for %{name}.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}	\
	--with-pam-include=system-auth	\
	--with-pam-module-dir=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/polkit-1/extensions/*.la

%find_lang %{name}-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}-1.lang
%defattr(644,root,root,755)
%doc AUTHORS README

# The directory /etc/polkit-1/localauthority must be owned
# by root and have mode 700
%attr(700,root,root) %dir %{_sysconfdir}/polkit-1/localauthority

%dir %{_sysconfdir}/polkit-1
%dir %{_sysconfdir}/polkit-1/localauthority.conf.d
%dir %{_sysconfdir}/polkit-1/localauthority/10-vendor.d
%dir %{_sysconfdir}/polkit-1/localauthority/20-org.d
%dir %{_sysconfdir}/polkit-1/localauthority/30-site.d
%dir %{_sysconfdir}/polkit-1/localauthority/50-local.d
%dir %{_sysconfdir}/polkit-1/localauthority/90-mandatory.d
%dir %{_sysconfdir}/polkit-1/nullbackend.conf.d

# The directory /var/lib/polkit-1 must be owned
# by root and have mode 700
%attr(700,root,root) %dir /var/lib/polkit-1

%dir /var/lib/polkit-1/localauthority
%dir /var/lib/polkit-1/localauthority/10-vendor.d
%dir /var/lib/polkit-1/localauthority/20-org.d
%dir /var/lib/polkit-1/localauthority/30-site.d
%dir /var/lib/polkit-1/localauthority/50-local.d
%dir /var/lib/polkit-1/localauthority/90-mandatory.d

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polkit-1/localauthority.conf.d/50-localauthority.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polkit-1/nullbackend.conf.d/50-nullbackend.conf
/etc/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
/etc/pam.d/polkit-1

# The file /usr/bin/pkexec must be owned by root and
# have mode 4755 (setuid root binary)
%attr(4755,root,root) %{_bindir}/pkexec

# The file /usr/lib/polkit/polkit-agent-helper-1 must be owned
# by root and have mode 4755 (setuid root binary)
%attr(4755,root,root) %{_libexecdir}/polkit-agent-helper-1

%attr(755,root,root) %{_bindir}/pkaction
%attr(755,root,root) %{_bindir}/pkcheck
%attr(755,root,root) %{_libdir}/polkit-1/extensions/libnullbackend.so
%attr(755,root,root) %{_libexecdir}/polkitd

%{_datadir}/dbus-1/system-services/org.freedesktop.PolicyKit1.service
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.policy

%{_mandir}/man1/pkaction.1*
%{_mandir}/man1/pkcheck.1*
%{_mandir}/man1/pkexec.1*
%{_mandir}/man8/pklocalauthority.8*
%{_mandir}/man8/polkit.8*
%{_mandir}/man8/polkitd.8*

%files libs
%defattr(644,root,root,755)
# notes which license applies to which package part, AFL text (and GPL text copy)
%doc COPYING
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%dir %{_libdir}/polkit-1
%dir %{_libdir}/polkit-1/extensions
%dir %{_libexecdir}

%attr(755,root,root) %ghost %{_libdir}/libpolkit-agent-1.so.?
%attr(755,root,root) %ghost %{_libdir}/libpolkit-backend-1.so.?
%attr(755,root,root) %ghost %{_libdir}/libpolkit-gobject-1.so.?
%attr(755,root,root) %{_libdir}/libpolkit-agent-1.so.*.*.*
%attr(755,root,root) %{_libdir}/libpolkit-backend-1.so.*.*.*
%attr(755,root,root) %{_libdir}/libpolkit-gobject-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-agent-1.so
%attr(755,root,root) %{_libdir}/libpolkit-backend-1.so
%attr(755,root,root) %{_libdir}/libpolkit-gobject-1.so
%{_libdir}/libpolkit-agent-1.la
%{_libdir}/libpolkit-backend-1.la
%{_libdir}/libpolkit-gobject-1.la
%{_includedir}/polkit-1
%{_pkgconfigdir}/polkit-agent-1.pc
%{_pkgconfigdir}/polkit-backend-1.pc
%{_pkgconfigdir}/polkit-gobject-1.pc
%{_datadir}/gir-1.0/Polkit-1.0.gir
%{_datadir}/gir-1.0/PolkitAgent-1.0.gir

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

