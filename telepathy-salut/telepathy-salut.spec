Summary:	A link-local XMPP connection manager
Name:		telepathy-salut
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-salut/%{name}-%{version}.tar.gz
# Source0-md5:	43639c23de33e8466540de02816d23bf
BuildRequires:	check-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	telepathy-glib-devel
Provides:	telepathy-service
Requires:	avahi
Requires:	nss-mdns
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/telepathy

%description
Gabble is a Jabber connection manager.

%prep
%setup -q

%build
%configure \
	--disable-avahi-tests	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libexecdir}/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libexecdir}/telepathy-salut
%dir %{_libexecdir}/salut-0
%dir %{_libexecdir}/salut-0/lib
%attr(755,root,root) %{_libexecdir}/salut-0/lib/*.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.salut.service
%{_datadir}/telepathy/managers/salut.manager
%{_mandir}/man8/telepathy-salut.8*

