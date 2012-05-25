Summary:	A collection of SNMP protocol tools
Name:		net-snmp
Version:	5.7.1
Release:	1
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://downloads.sourceforge.net/net-snmp/%{name}-%{version}.tar.gz
# Source0-md5:	c95d08fd5d93df0c11a2e1bdf0e01e0b
URL:		http://www.net-snmp.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	elfutils-devel
BuildRequires:	libnl-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel
BuildRequires:	pciutils-devel
BuildRequires:	perl-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# linking libraries is ugly in this package
%define		no_install_post_check_so	1

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management (hence the name). The net-snmp project includes
various SNMP tools: an extensible agent, an SNMP library, tools for
requesting or setting information from SNMP agents, tools for
generating and handling SNMP traps, a version of the netstat command
which uses SNMP, and a Tk/Perl mib browser. This package contains the
snmpd daemon, documentation, etc.

%package libs
Summary:	NET SNMP libraries
Group:		Libraries

%description libs
NET SNMP libraries.

%package devel
Summary:	The development environment for the net-snmp project
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	elfutils-devel
Requires:	libnl-devel
Requires:	libwrap-devel
Requires:	openssl-devel

%description devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the net-snmp project's network management
tools.

%package compat-devel
Summary:	The development environment for the UCD-SNMP project
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description compat-devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the UCD-SNMP project's network management
tools.

%package utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}

%description utils
This package contains various utilities for managing your network
using the SNMP protocol.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	ac_cv_path_DPKG_QUERY_PATH= \
	--disable-debugging \
	--disable-agent \
	--disable-applications \
	--disable-manuals \
	--disable-scripts \
	--disable-mibs \
	--enable-as-needed \
	--disable-static \
	--with-cflags="%{rpmcflags} %{rpmcppflags} -I/usr/include/et" \
	--with-ldflags="%{rpmldflags}" \
	--with-default-snmp-version=3 \
	--without-perl-modules \
	--without-python-modules \
	--without-rpm \
	--enable-ipv6

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig,snmp},/var/log,/var/lib/net-snmp,%{_libdir}/snmp/dlmod}

%{__make} -j1 install \
	mibdir=%{_datadir}/mibs \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AGENT.txt CHANGES COPYING ChangeLog EXAMPLE.conf{,.def} FAQ NEWS README{,.agent-mibs,.agentx,.snmpv3,.sql,.thread} TODO local
%if 0
%attr(755,root,root) %{_sbindir}/snmpd
%attr(755,root,root) %{_bindir}/net-snmp-create-v3-user
%dir %{_libdir}/snmp
%dir %{_libdir}/snmp/dlmod
%attr(755,root,root) %{_datadir}/snmp/snmp_perl.pl
%{_mandir}/man1/net-snmp-create-v3-user.1*
%{_mandir}/man5/snmpd.conf.5*
%{_mandir}/man5/snmpd.examples.5*
%{_mandir}/man5/snmpd.internal.5*
%{_mandir}/man5/variables.5*
%{_mandir}/man8/snmpd.8*

%dir %attr(700,root,root) /var/lib/net-snmp
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libnetsnmp.so.??
%attr(755,root,root) %ghost %{_libdir}/libnetsnmpagent.so.??
%attr(755,root,root) %ghost %{_libdir}/libnetsnmphelpers.so.??
%attr(755,root,root) %ghost %{_libdir}/libnetsnmpmibs.so.??
%attr(755,root,root) %{_libdir}/libnetsnmp.so.*.*.*
%attr(755,root,root) %{_libdir}/libnetsnmpagent.so.*.*.*
%attr(755,root,root) %{_libdir}/libnetsnmphelpers.so.*.*.*
%attr(755,root,root) %{_libdir}/libnetsnmpmibs.so.*.*.*
%dir %{_sysconfdir}/snmp
%dir %{_datadir}/snmp

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/net-snmp-config
%attr(755,root,root) %{_libdir}/libnetsnmp.so
%attr(755,root,root) %{_libdir}/libnetsnmpagent.so
%attr(755,root,root) %{_libdir}/libnetsnmphelpers.so
%attr(755,root,root) %{_libdir}/libnetsnmpmibs.so
%{_libdir}/libnetsnmp.la
%{_libdir}/libnetsnmpagent.la
%{_libdir}/libnetsnmphelpers.la
%{_libdir}/libnetsnmpmibs.la
%{_includedir}/net-snmp
%if 0
%{_datadir}/snmp/mib2c*
%{_mandir}/man1/mib2c.1*
%{_mandir}/man1/mib2c-update.1*
%{_mandir}/man1/net-snmp-config.1*
%{_mandir}/man3/[!NS]*
%{_mandir}/man5/mib2c.conf.5*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/agentxtrap
%attr(755,root,root) %{_bindir}/encode_keychange
%attr(755,root,root) %{_bindir}/snmpbulkget
%attr(755,root,root) %{_bindir}/snmpbulkwalk
%attr(755,root,root) %{_bindir}/snmpdelta
%attr(755,root,root) %{_bindir}/snmpdf
%attr(755,root,root) %{_bindir}/snmpget
%attr(755,root,root) %{_bindir}/snmpgetnext
%attr(755,root,root) %{_bindir}/snmpinform
%attr(755,root,root) %{_bindir}/snmpnetstat
%attr(755,root,root) %{_bindir}/snmpset
%attr(755,root,root) %{_bindir}/snmpstatus
%attr(755,root,root) %{_bindir}/snmptable
%attr(755,root,root) %{_bindir}/snmptest
%attr(755,root,root) %{_bindir}/snmptls
%attr(755,root,root) %{_bindir}/snmptranslate
%attr(755,root,root) %{_bindir}/snmptrap
%attr(755,root,root) %{_bindir}/snmpusm
%attr(755,root,root) %{_bindir}/snmpvacm
%attr(755,root,root) %{_bindir}/snmpwalk
%{_mandir}/man1/agentxtrap.1*
%{_mandir}/man1/encode_keychange.1*
%{_mandir}/man1/snmpbulkget.1*
%{_mandir}/man1/snmpbulkwalk.1*
%{_mandir}/man1/snmpcmd.1*
%{_mandir}/man1/snmpdelta.1*
%{_mandir}/man1/snmpdf.1*
%{_mandir}/man1/snmpget.1*
%{_mandir}/man1/snmpgetnext.1*
%{_mandir}/man1/snmpinform.1*
%{_mandir}/man1/snmpnetstat.1*
%{_mandir}/man1/snmpset.1*
%{_mandir}/man1/snmpstatus.1*
%{_mandir}/man1/snmptable.1*
%{_mandir}/man1/snmptest.1*
%{_mandir}/man1/snmptranslate.1*
%{_mandir}/man1/snmptrap.1*
%{_mandir}/man1/snmpusm.1*
%{_mandir}/man1/snmpvacm.1*
%{_mandir}/man1/snmpwalk.1*
%{_mandir}/man5/snmp.conf.5*
%{_mandir}/man5/snmp_config.5*

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/snmp.conf
%endif

