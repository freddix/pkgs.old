%define		cvs_vers	20110819

Summary:	Basic Networking Tools
Name:		net-tools
Version:	1.60.%{cvs_vers}
Release:	1
License:	GPL
Group:		Networking/Admin
#Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp.archlinux.org/other/net-tools/net-tools-1.60.%{cvs_vers}cvs.tar.bz2
# Source0-md5:	de2ed1f1791b7932e3d2d73fad67e839
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-ipvs.patch
Patch3:		%{name}-et.patch
Patch4:		%{name}-no_multiline.patch
Patch5:		%{name}-x25_address_is_struct.patch
Patch6:		%{name}-make_config_h.patch
Patch7:		%{name}-mii.patch
Patch8:		%{name}-gcc34.patch
Patch9:		%{name}-nameif.patch
Patch10:	%{name}-inet6-lookup.patch
Patch11:	%{name}-ipx.patch
Patch12:	%{name}-manydevs.patch
Patch13:	%{name}-get_name.patch
Patch14:	%{name}-arp_overflow.patch
Patch15:	%{name}-virtualname.patch
Patch16:	%{name}-cycle.patch
Patch17:	%{name}-interface.patch
Patch18:	%{name}-ifaceopt.patch
Patch19:	%{name}-netstat-overflow.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
This is a collection of the basic tools necessary for setting up
networking on a Linux machine. It includes ifconfig, route, netstat,
rarp, and some other minor tools.

%prep
%setup -qn %{name}-%{version}cvs
#%patch0 -p1
%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1
%patch6 -p1
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1
#%patch10 -p1
#%patch11 -p1
#%patch12 -p1
#%patch13 -p1
%patch14 -p1
#%patch15 -p1
#%patch16 -p1
#%patch17 -p1
#%patch18 -p1
%patch19 -p1

%build
echo "yes" | %{__make}
%{__make} update \
	CC="%{__cc}" \
	COPTS="%{rpmcflags} -Wall" \
	I18N=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="install" \
	mandir=%{_mandir} \
	I18N=1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT/usr/share/man/README.net-tools-non-english-man-pages

# standardize localized man dirs
mv -f $RPM_BUILD_ROOT%{_mandir}/{de_DE/man1/*,de/man1}
rmdir $RPM_BUILD_ROOT%{_mandir}/de_DE/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/{de_DE/*,de}
mv -f $RPM_BUILD_ROOT%{_mandir}/{fr_FR,fr}
# we can do it safely as no pt/pt_PT man pages appeared here yet
mv $RPM_BUILD_ROOT%{_mandir}/{pt_BR,pt}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/mactab <<EOF
# Each line here contains an interface name and a Ethernet MAC address. Like:
#lan 00:13:d3:05:15:d2
EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mactab
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/arp
%attr(755,root,root) %{_sbindir}/ifconfig
%attr(755,root,root) %{_sbindir}/mii-tool
%attr(755,root,root) %{_sbindir}/rarp
%attr(755,root,root) %{_sbindir}/route
%attr(755,root,root) %{_sbindir}/nameif

%lang(de) %{_mandir}/de/man[15]/*
%lang(de) %{_mandir}/de/man8/[!ps]*
%lang(es) %{_mandir}/es/man[15]/*
%lang(es) %{_mandir}/es/man8/[!ps]*
%lang(fi) %{_mandir}/fi/man[15]/*
# No fi man8
%lang(fr) %{_mandir}/fr/man[15]/*
%lang(fr) %{_mandir}/fr/man8/[!ps]*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(hu) %{_mandir}/hu/man8/[!ps]*
%lang(id) %{_mandir}/id/man[15]/*
%lang(id) %{_mandir}/id/man8/[!ps]*
%lang(it) %{_mandir}/it/man[15]/*
%lang(it) %{_mandir}/it/man8/[!ps]*
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(ja) %{_mandir}/ja/man8/[!ps]*
# No nl man[15]
%lang(nl) %{_mandir}/nl/man8/[!ps]*
%lang(pt) %{_mandir}/pt/man[15]/*
%lang(pt) %{_mandir}/pt/man8/[!ps]*
%lang(pl) %{_mandir}/pl/man[15]/*
%lang(pl) %{_mandir}/pl/man8/[!ps]*

%{_mandir}/man[15]/*
%{_mandir}/man8/[!ps]*

%attr(755,root,root) %{_sbindir}/slattach
%lang(de) %{_mandir}/de/man8/slattach.8*
%lang(fr) %{_mandir}/fr/man8/slattach.8*
%lang(ja) %{_mandir}/ja/man8/slattach.8*
%lang(pl) %{_mandir}/pl/man8/slattach.8*
%{_mandir}/man8/slattach.8*

%attr(755,root,root) %{_sbindir}/plipconfig
%lang(de) %{_mandir}/de/man8/plipconfig.8*
%lang(fr) %{_mandir}/fr/man8/plipconfig.8*
%lang(ja) %{_mandir}/ja/man8/plipconfig.8*
%{_mandir}/man8/plipconfig.8*

