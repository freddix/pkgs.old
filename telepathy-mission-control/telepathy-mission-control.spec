Summary:	A Telepathy account manager
Name:		telepathy-mission-control
Version:	5.12.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-mission-control/%{name}-%{version}.tar.gz
# Source0-md5:	f39dcfef785a37dc21efa9af06be2e61
URL:		http://mission-control.sourceforge.net/
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	telepathy-glib-devel
BuildRequires:	telepathy-glib-devel
BuildRequires:	upower-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/telepathy

%description
An account manager for Telepathy.

%package libs
Summary:	mission control library
Group:		Libraries

%description libs
mission control library.

%package devel
Summary:	Header files for mission control library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for mission control library.

%package apidocs
Summary:	mission control API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
mission control API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{telepathy/{clients,managers},mission-control/profiles} \
	$RPM_BUILD_ROOT%{_libdir}/mission-control-plugins.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README

%dir %{_datadir}/mission-control
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/clients
%dir %{_datadir}/telepathy/managers
%dir %{_libdir}/mission-control-plugins.0
%dir %{_libexecdir}

%attr(755,root,root) %{_bindir}/mc-tool
%attr(755,root,root) %{_bindir}/mc-wait-for-name

%attr(755,root,root) %{_libexecdir}/mission-control-5
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.MissionControl5.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.AccountManager.service
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_datadir}/mission-control/profiles

%{_mandir}/man1/mc-tool.1*
%{_mandir}/man1/mc-wait-for-name.1*
%{_mandir}/man8/mission-control-5.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libmission-control-plugins.so.?
%attr(755,root,root) %{_libdir}/libmission-control-plugins.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmission-control-plugins.so
%{_libdir}/libmission-control-plugins.la
%{_includedir}/mission-control-5.5
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/mission-control-plugins

