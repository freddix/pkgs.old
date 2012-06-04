Summary:	Framework providing Desktop activity awareness
Name:		zeitgeist
Version:	0.9.0.1
Release:	1
License:	LGPL v2
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.9/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	08f2eb384824e8458f18e10db7654965
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-rdflib
BuildRequires:	raptor-rapper
BuildRequires:	xapian-core-devel
Requires:	python-dbus
Requires:	python-modules
Requires:	python-modules-sqlite
Requires:	python-pygobject
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Zeitgeist is a service which logs the users's activities and events
(files opened, websites visites, conversations hold with other people,
etc.) and makes relevant information available to other applications.
It is able to establish relationships between items based on
similarity and usage patterns.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
#-f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/zeitgeist-fts
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.fts.service
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%{_datadir}/zeitgeist
%{_mandir}/man1/zeitgeist-daemon.1*
%{py_sitescriptdir}/zeitgeist

