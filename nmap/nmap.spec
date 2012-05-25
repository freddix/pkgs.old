Summary:	Network exploration tool and security scanner
Name:		nmap
Version:	6.00
Release:	1
License:	GPL with exception
Group:		Networking
Source0:	http://nmap.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	e365cdada811c57e172b24b62746ab7d
URL:		http://www.insecure.org/nmap/index.html
BuildRequires:	libstdc++-devel
BuildRequires:	lua-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
Requires:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nmap ("Network Mapper") is a free and open source (license) utility
for network discovery and security auditing. Many systems and network
administrators also find it useful for tasks such as network inventory
managing service upgrade schedules, and monitoring host or service
uptime. Nmap uses raw IP packets in novel ways to determine what hosts
are available on the network, what services (application name
and version) those hosts are offering, what operating systems (and OS
versions) they are running, what type of packet filters/firewalls are
in use, and dozens of other characteristics. It was designed to
rapidly scan large networks, but works fine against single hosts.

%package gui
Summary:        GUIs for nmap
Group:          X11/Applications/Networking
Requires:       %{name} = %{version}-%{release}
Requires:       bash
Requires:       python-pygtk-gtk
Requires:       python-sqlite

%description gui
This package includes graphical frontends for nmap.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

ln -sf /etc/certs/ca-certificates.crt $RPM_BUILD_ROOT/%{_datadir}/ncat/ca-bundle.crt

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_bindir}/uninstall_zenmap

# fix locale names
mv $RPM_BUILD_ROOT%{_mandir}/{jp,ja}
mv $RPM_BUILD_ROOT%{_mandir}/pt{_PT,}
mv $RPM_BUILD_ROOT%{_mandir}/zh{,_CN}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README docs/*.txt CHANGELOG COPYING
%attr(755,root,root) %{_bindir}/ncat
%attr(755,root,root) %{_bindir}/ndiff
%attr(755,root,root) %{_bindir}/nmap
%attr(755,root,root) %{_bindir}/nping
%{_datadir}/nmap
%{_datadir}/ncat
%{_mandir}/man1/ncat.1*
%{_mandir}/man1/ndiff.1*
%{_mandir}/man1/nmap.1*
%{_mandir}/man1/nping.1*
%lang(de) %{_mandir}/de/man1/nmap.1*
%lang(es) %{_mandir}/es/man1/nmap.1*
%lang(fr) %{_mandir}/fr/man1/nmap.1*
%lang(hr) %{_mandir}/hr/man1/nmap.1*
%lang(hu) %{_mandir}/hu/man1/nmap.1*
%lang(it) %{_mandir}/it/man1/nmap.1*
%lang(ja) %{_mandir}/ja/man1/nmap.1*
%lang(pl) %{_mandir}/pl/man1/nmap.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/nmap.1*
%lang(pt) %{_mandir}/pt/man1/nmap.1*
%lang(ro) %{_mandir}/ro/man1/nmap.1*
%lang(ru) %{_mandir}/ru/man1/nmap.1*
%lang(sk) %{_mandir}/sk/man1/nmap.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/nmap.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmapfe
%attr(755,root,root) %{_bindir}/xnmap
%attr(755,root,root) %{_bindir}/zenmap
%{py_sitescriptdir}/radialnet
%{py_sitescriptdir}/zenmapCore
%{py_sitescriptdir}/zenmapGUI
%dir %{_datadir}/zenmap
%{_datadir}/zenmap/config
%{_datadir}/zenmap/docs
%{_datadir}/zenmap/misc
%dir %{_datadir}/zenmap/locale
%lang(de) %{_datadir}/zenmap/locale/de
%lang(fr) %{_datadir}/zenmap/locale/fr
%lang(hr) %{_datadir}/zenmap/locale/hr
%lang(pt_BR) %{_datadir}/zenmap/locale/pt_BR
%lang(ru) %{_datadir}/zenmap/locale/ru
%{_datadir}/zenmap/pixmaps
%{_datadir}/zenmap/su-to-zenmap.sh
%{_desktopdir}/zenmap-root.desktop
%{_desktopdir}/zenmap.desktop
%{_mandir}/man1/zenmap.1*

