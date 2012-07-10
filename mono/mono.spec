%bcond_with	bootstrap

Summary:	Common Language Infrastructure implementation
Name:		mono
Version:	2.10.9
Release:	1
License:	GPL/LGPL/MIT
Group:		Development/Languages
Source0:	http://download.mono-project.com/sources/mono/%{name}-%{version}.tar.bz2
# Source0-md5:	bbbff9d3d0c36b904437ada36a27eb9e
Patch0:		%{name}-sonames.patch
Patch1:		%{name}-pc.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libtool
# requires gcms.exe and rpm provides
%{!?with_bootstrap:BuildRequires:	mono-csharp}
BuildRequires:	pkg-config
BuildRequires:	rpmbuild(monoautodeps)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rpmlibdir		/usr/lib/rpm
%define         skip_post_check_so      '.+(libmonosgen|libmono-profiler).+\.so.+'

%if ! %{with bootstrap}
%define	__mono_provides	%{_rpmlibdir}/mono-find-provides
%define	__mono_requires	%{_rpmlibdir}/mono-find-requires
%endif

%define gac_dll(dll) %{_gacdir}/%{1}	\
	%{_monodir}/?.?/%{1}.dll	\
	%{nil}

%define mono_bin(bin) %{_bindir}/%{1}	\
	%{_monodir}/?.?/%{1}.exe	\
	%{nil}

%description
The Common Language Infrastructure platform. Microsoft has created a
new development platform. The highlights of this new development
platform are:
- A runtime environment that provides garbage collection, threading
  and a virtual machine specification (The Virtual Execution System,
  VES),
- A comprehensive class library,
- A new language, C#. Very similar to Java, C# allows programmers to
  use all the features available on the Mono runtime,
- A language specification that compilers can follow if they want to
  generate classes and code that can interoperate with other programming
  languages (The Common Language Specification: CLS).

%package devel
Summary:	Development resources for mono
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development resources for mono.

%package debug
Summary:	Mono libraries debugging resources
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description debug
Mono libraries debugging resources.

%package csharp
Summary:	C# compiler for mono
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}

%description csharp
C# compiler for mono.

%package ilasm
Summary:	ILasm compiler for mono
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
Provides:	ilasm

%description ilasm
ILasm compiler for mono.

%package jscript
Summary:	jscript compiler for mono
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}

%description jscript
jscript compiler for mono.

%package compat-links
Summary:	Mono compatibility links
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}

%description compat-links
This package contains links to binaries with names used in Mono and
dotGNU.

%package -n monodoc
Summary:	Documentation for Mono class libraries and tools
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description -n monodoc
This package contains the documentation for the Mono class libraries,
tools to produce and edit the documentation, and a documentation
browser.

%package web
Summary:	ASP.NET, Remoting, and Web Services for Mono
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description web
ASP.NET, Remoting, and Web Services for Mono.

%package winforms
Summary:	Windows Forms implementation for Mono
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	libgdiplus

%description winforms
Windows Forms implementation for Mono.

%package db-sqlite
Summary:        sqlite database connectivity for Mono
Group:          Development/Languages
Requires:       mono = %{version}-%{release}
Requires:       sqlite3

%description db-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package db-oracle
Summary:        Oracle database connectivity for Mono
Group:          Development/Languages
Requires:       mono = %{version}-%{release}

%description db-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%package db-postgresql
Summary:        Postgresql database connectivity for Mono
Group:          Development/Languages
Requires:       mono = %{version}-%{release}

%description db-postgresql
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%package db-ibm-db2
Summary:        IBM DB2 database connectivity for Mono
Group:          Development/Languages
Requires:       mono = %{version}-%{release}

%description db-ibm-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Remove prebuilt binaries
rm -rf mcs/class/lib/monolite/*

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoheader}
%{__automake}
%{__autoconf}
cd libgc
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
cd ../eglib
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
cd ..

CPPFLAGS="-DUSE_LIBC_PRIVATE_SYMBOLS -DUSE_COMPILER_TLS"
%configure \
	--enable-fast-install		\
	--with-libgdiplus=installed
%{__make} -j1 V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_rpmlibdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this way we can run rpmbuild -bi several times, and directories
# have more meaningful name.
rm -rf short-circuit-doc
mkdir -p short-circuit-doc/notes
cp -a docs/* short-circuit-doc/notes
rm -f short-circuit-doc/*/Makefile*

mv -f $RPM_BUILD_ROOT%{_bindir}/mono-find* $RPM_BUILD_ROOT%{_rpmlibdir}

# unused
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/*.html
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/README*
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/barrett_diagram
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/gc.man
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.a
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/mono/2.0/gmcs.exe.so
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/mono/2.0/mcs.exe.so
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/mono/2.0/mscorlib.dll.so
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/mono/4.0/dmcs.exe.so
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/mono/4.0/mscorlib.dll.so
%{__rm} -fr $RPM_BUILD_ROOT%{_monodir}/gac/Mono.Security.Win32
%{__rm} -rf $RPM_BUILD_ROOT%{_bindir}/mono-configuration-crypto
%{__rm} -rf $RPM_BUILD_ROOT%{_monodir}/2.0/Mono.Security.Win32.dll
%{__rm} -rf $RPM_BUILD_ROOT%{_monodir}/4.0/Mono.Security.Win32
%{__rm} -rf $RPM_BUILD_ROOT%{_monodir}/4.0/Mono.Security.Win32.dll
%{__rm} -rf $RPM_BUILD_ROOT%{_monodir}/xbuild/Microsoft

%find_lang mcs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README short-circuit-doc/*

# core dirs
%dir %{_gacdir}

%dir %{_monodir}
%dir %{_monodir}/2.0
%dir %{_monodir}/3.5
%dir %{_monodir}/4.0
%dir %{_monodir}/4.0/MSBuild
%dir %{_monodir}/compat-2.0
%dir %{_monodir}/mono-configuration-crypto
%dir %{_monodir}/mono-configuration-crypto/4.0

%dir %{_sysconfdir}/mono
%dir %{_sysconfdir}/mono/2.0
%dir %{_sysconfdir}/mono/2.0/Browsers
%dir %{_sysconfdir}/mono/4.0
%dir %{_sysconfdir}/mono/mconfig

# configuration
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/2.0/Browsers/Compat.browser
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/2.0/machine.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/2.0/settings.map
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/4.0/machine.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/4.0/settings.map
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/4.0/web.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/config

# libraries
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libMonoPosixHelper.so
%attr(755,root,root) %{_libdir}/libMonoSupportW.so
%attr(755,root,root) %{_libdir}/libikvm-native.so

# binaries / wrappers
%attr(755,root,root) %mono_bin certmgr
%attr(755,root,root) %mono_bin chktrust
%attr(755,root,root) %mono_bin gacutil
%attr(755,root,root) %mono_bin mozroots
%attr(755,root,root) %mono_bin secutil
%attr(755,root,root) %mono_bin setreg
%attr(755,root,root) %mono_bin signcode
%attr(755,root,root) %mono_bin sn
%attr(755,root,root) %{_bindir}/gacutil2
%attr(755,root,root) %{_bindir}/mono
%attr(755,root,root) %{_bindir}/mprof-report

# data
%attr(755,root,root) %mono_bin sqlmetal
%attr(755,root,root) %mono_bin sqlsharp
%gac_dll Mono.Data.Tds
%gac_dll WebMatrix.Data
%gac_dll Novell.Directory.Ldap
%gac_dll System.Data
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Linq
%gac_dll System.Data.Services
%gac_dll System.Data.Services.Client
%gac_dll System.DirectoryServices
%gac_dll System.EnterpriseServices
%gac_dll System.Transactions
%{_mandir}/man1/sqlsharp.1*

# extras
%attr(755,root,root) %mono_bin mono-service
%attr(755,root,root) %{_bindir}/mono-service2
%attr(755,root,root) %{_monodir}/2.0/RabbitMQ.Client.Apigen.exe
%attr(755,root,root) %{_monodir}/4.0/RabbitMQ.Client.Apigen.exe
%{_gacdir}/mono-service
%gac_dll Mono.Messaging
%gac_dll Mono.Messaging.RabbitMQ
%gac_dll RabbitMQ.Client
%gac_dll System.Configuration.Install
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceModel
%gac_dll System.ServiceProcess
%{_mandir}/man1/mono-service.1*

# nunit testing framework
%attr(755,root,root) %mono_bin nunit-console
%attr(755,root,root) %{_bindir}/nunit-console2
%gac_dll nunit-console-runner
%gac_dll nunit.core
%gac_dll nunit.core.extensions
%gac_dll nunit.core.interfaces
%gac_dll nunit.framework
%gac_dll nunit.framework.extensions
%gac_dll nunit.mocks
%gac_dll nunit.util
%{_monodir}/2.0/nunit-console.exe.config

# gac
%gac_dll Commons.Xml.Relaxng
%gac_dll CustomMarshalers
%gac_dll I18N
%gac_dll I18N.CJK
%gac_dll I18N.MidEast
%gac_dll I18N.Other
%gac_dll I18N.Rare
%gac_dll I18N.West
%gac_dll ICSharpCode.SharpZipLib
%gac_dll Microsoft.VisualC
%gac_dll Mono.C5
%gac_dll Mono.Cairo
%gac_dll Mono.CodeContracts
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.Debugger.Soft
%gac_dll Mono.Management
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll Mono.Simd
%gac_dll Mono.Tasklets
%gac_dll OpenSystem.C
%gac_dll System
%gac_dll System.ComponentModel.Composition
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.Configuration
%gac_dll System.Core
%gac_dll System.Drawing
%gac_dll System.Dynamic
%gac_dll System.IdentityModel
%gac_dll System.IdentityModel.Selectors
%gac_dll System.Net
%gac_dll System.Numerics
%gac_dll System.Runtime.Caching
%gac_dll System.Runtime.DurableInstancing
%gac_dll System.Runtime.Remoting
%gac_dll System.Runtime.Serialization
%gac_dll System.Security
%gac_dll System.ServiceModel.Discovery
%gac_dll System.ServiceModel.Routing
%gac_dll System.Web.ApplicationServices
%gac_dll System.Windows.Forms.DataVisualization
%gac_dll System.Xaml
%gac_dll System.Xml
%gac_dll WindowsBase
%gac_dll cscompmgd
%{_gacdir}/System.Xml.Linq

# other dlls
%{_monodir}/*.*/mscorlib.dll
%{_gacdir}/Mono.Cecil
%{_monodir}/compat-*/ICSharpCode.SharpZipLib.dll
%{_monodir}/compat-2.0/System.Web.Extensions.Design.dll
%{_monodir}/compat-2.0/System.Web.Extensions.dll
%{_monodir}/compat-2.0/System.Web.Mvc.dll

# manuals
%{_mandir}/man1/cert*.1*
%{_mandir}/man1/chktrust.1*
%{_mandir}/man1/gacutil.1*
%{_mandir}/man1/mono-shlib-cop.1*
%{_mandir}/man1/mono-xmltool.1*
%{_mandir}/man1/mono.1*
%{_mandir}/man1/monop.1*
%{_mandir}/man1/mozroots.1*
%{_mandir}/man1/secutil.1*
%{_mandir}/man1/signcode.1*
%{_mandir}/man1/sn.1*

# 2.0
%{_monodir}/2.0/System.Xml.Linq.dll

# 3.5
%{_monodir}/3.5/MSBuild
%{_monodir}/3.5/Microsoft.Build.Engine.dll
%{_monodir}/3.5/Microsoft.Build.Framework.dll
%{_monodir}/3.5/Microsoft.Build.xsd
%{_monodir}/3.5/Microsoft.CSharp.targets
%{_monodir}/3.5/Microsoft.Common.ta*
%{_monodir}/3.5/Microsoft.VisualBasic.targets

# 4.0
%{_monodir}/4.0/System.Xml.Linq.dll
%{_monodir}/4.0/Accessibility.dll*
%{_monodir}/4.0/MSBuild/Microsoft*
%{_monodir}/4.0/Microsoft.Common.targets
%{_monodir}/4.0/Microsoft.Common.tasks
%{_monodir}/4.0/Microsoft.VisualBasic.targets
%{_monodir}/4.0/PEAPI.dll
%{_monodir}/4.0/mono-shlib-cop.exe.config

%{_monodir}/4.0/sqlmetal.exe.config
%{_monodir}/4.0/xbuild.rsp

%{_monodir}/mono-configuration-crypto/4.0/Mono.Configuration.Crypto.dll*
%{_monodir}/mono-configuration-crypto/4.0/mono-config*


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_rpmlibdir}/mono-find*
%{_libdir}/lib*.la
%{_datadir}/%{name}-2.0
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/*.pc

%attr(755,root,root) %mono_bin al
%attr(755,root,root) %mono_bin caspol
%attr(755,root,root) %mono_bin ccrewrite
%attr(755,root,root) %mono_bin cert2spc
%attr(755,root,root) %mono_bin dtd2rng
%attr(755,root,root) %mono_bin dtd2xsd
%attr(755,root,root) %mono_bin genxs
%attr(755,root,root) %mono_bin installvst
%attr(755,root,root) %mono_bin macpack
%attr(755,root,root) %mono_bin makecert
%attr(755,root,root) %mono_bin mkbundle
%attr(755,root,root) %mono_bin mono-api-info
%attr(755,root,root) %mono_bin mono-shlib-cop
%attr(755,root,root) %mono_bin mono-xmltool
%attr(755,root,root) %mono_bin monolinker
%attr(755,root,root) %mono_bin monop
%attr(755,root,root) %mono_bin permview
%attr(755,root,root) %mono_bin sgen
%attr(755,root,root) %mono_bin xbuild
%attr(755,root,root) %{_bindir}/al2
%attr(755,root,root) %{_bindir}/mono-gdb.py
%attr(755,root,root) %{_bindir}/mono-heapviz
%attr(755,root,root) %{_bindir}/mono-sgen
%attr(755,root,root) %{_bindir}/mono-sgen-gdb.py
%attr(755,root,root) %{_bindir}/mono-test-install
%attr(755,root,root) %{_bindir}/monodis
%attr(755,root,root) %{_bindir}/monograph
%attr(755,root,root) %{_bindir}/monop2
%attr(755,root,root) %{_bindir}/pedump
%attr(755,root,root) %{_bindir}/peverify
%attr(755,root,root) %{_bindir}/prj2make
%attr(755,root,root) %{_monodir}/[24].0/culevel.exe
%attr(755,root,root) %{_monodir}/4.0/ictool.exe
%attr(755,root,root) %{_monodir}/4.0/installutil.exe
%{_libdir}/mono-source-libs

%gac_dll Microsoft.Build
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%gac_dll Microsoft.Build.Tasks
%gac_dll Microsoft.Build.Tasks.v3.5
%gac_dll Microsoft.Build.Tasks.v4.0
%gac_dll Microsoft.Build.Utilities
%gac_dll Microsoft.Build.Utilities.v3.5
%gac_dll Microsoft.Build.Utilities.v4.0
%{_monodir}/3.5/xbuild.rsp
%{_monodir}/4.0/Microsoft.Build.xsd
%{_monodir}/xbuild-frameworks
%gac_dll PEAPI

%{_gacdir}/Mono.Cecil.Mdb
%{_monodir}/2.0/MSBuild
%{_monodir}/2.0/Microsoft.*.targets
%{_monodir}/2.0/Microsoft.Build.xsd
%{_monodir}/2.0/Microsoft.Common.tasks
%{_monodir}/2.0/xbuild.rsp

# manuals
%{_mandir}/man1/al.1*
%{_mandir}/man1/ccrewrite.1.*
%{_mandir}/man1/cilc.1*
%{_mandir}/man1/dtd2xsd.1*
%{_mandir}/man1/genxs.1*
%{_mandir}/man1/macpack.1*
%{_mandir}/man1/makecert.1*
%{_mandir}/man1/mkbundle.1*
%{_mandir}/man1/mono-api-info.1.*
%{_mandir}/man1/mono-configuration-crypto.1.*
%{_mandir}/man1/monodis.1*
%{_mandir}/man1/monolinker.1*
%{_mandir}/man1/mprof-report.1*
%{_mandir}/man1/permview.1*
%{_mandir}/man1/prj2make.1*
%{_mandir}/man1/setreg.1*
%{_mandir}/man1/sgen.1*
%{_mandir}/man1/xbuild.1*
%{_mandir}/man5/mono-config.5*

%files compat-links
%defattr(644,root,root,755)
%mono_bin resgen
%attr(755,root,root) %{_bindir}/resgen2
%{_mandir}/man1/resgen.1*

%files csharp -f mcs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %mono_bin csharp
%attr(755,root,root) %mono_bin dmcs
%attr(755,root,root) %mono_bin gmcs
%attr(755,root,root) %mono_bin lc
%attr(755,root,root) %mono_bin mono-cil-strip
%attr(755,root,root) %mono_bin pdb2mdb
%attr(755,root,root) %mono_bin svcutil
%attr(755,root,root) %{_bindir}/csharp2
%attr(755,root,root) %{_bindir}/mcs
%{_monodir}/2.0/gmcs.exe.config
%{_monodir}/2.0/mcs.exe
%{_monodir}/4.0/Microsoft.CSharp.targets
%{_monodir}/4.0/dmcs.exe.config
%gac_dll Mono.CSharp
%gac_dll Microsoft.CSharp
%{_mandir}/man1/csharp.1*
%{_mandir}/man1/lc.1*
%{_mandir}/man1/mcs.1*
%{_mandir}/man1/mono-cil-strip.1*
%{_mandir}/man1/pdb2mdb.1*

%files ilasm
%defattr(644,root,root,755)
%attr(755,root,root) %mono_bin ilasm
%{_mandir}/man1/ilasm.1*

%files -n monodoc
%defattr(644,root,root,755)
%attr(755,root,root) %mono_bin mdoc
%attr(755,root,root) %mono_bin mod
%attr(755,root,root) %{_bindir}/mdassembler
%attr(755,root,root) %{_bindir}/mdoc-assemble
%attr(755,root,root) %{_bindir}/mdoc-export-html
%attr(755,root,root) %{_bindir}/mdoc-export-msxdoc
%attr(755,root,root) %{_bindir}/mdoc-update
%attr(755,root,root) %{_bindir}/mdoc-validate
%attr(755,root,root) %{_bindir}/mdvalidater
%attr(755,root,root) %{_bindir}/monodocer
%attr(755,root,root) %{_bindir}/monodocs2html
%attr(755,root,root) %{_bindir}/monodocs2slashdoc

%{_gacdir}/monodoc
%{_libdir}/monodoc
%{_monodir}/monodoc

# manuals
%{_mandir}/man1/md*.1*
%{_mandir}/man1/monodoc*.1*
%{_mandir}/man5/mdoc*.5*

%files web
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/2.0/web.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/browscap.ini
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mono/mconfig
%attr(755,root,root) %mono_bin disco
%attr(755,root,root) %mono_bin httpcfg
%attr(755,root,root) %mono_bin mconfig
%attr(755,root,root) %mono_bin soapsuds
%attr(755,root,root) %mono_bin wsdl
%attr(755,root,root) %mono_bin xsd
%attr(755,root,root) %{_bindir}/wsdl2
%attr(755,root,root) %{_monodir}/4.0/browsercaps-updater.exe
%gac_dll Microsoft.Web.Infrastructure
%gac_dll Mono.Http
%gac_dll Mono.Web
%gac_dll Mono.WebBrowser
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.ServiceModel.Web
%gac_dll System.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.DynamicData
%gac_dll System.Web.Extensions
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Mvc
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%{_mandir}/man1/disco.1*
%{_mandir}/man1/httpcfg.1*
%{_mandir}/man1/mconfig.1*
%{_mandir}/man1/soapsuds.1*
%{_mandir}/man1/wsdl.1*
%{_mandir}/man1/xsd.1*

%files winforms
%defattr(644,root,root,755)
%gac_dll Accessibility
%gac_dll System.Design
%gac_dll System.Drawing.Design
%gac_dll System.Windows.Forms

# database access
%files db-ibm-db2
%defattr(644,root,root,755)
%gac_dll IBM.Data.DB2

%files db-sqlite
%defattr(644,root,root,755)
%gac_dll Mono.Data.Sqlite

%files db-oracle
%defattr(644,root,root,755)
%gac_dll System.Data.OracleClient

%files db-postgresql
%defattr(644,root,root,755)
%gac_dll Npgsql

%files debug
%defattr(644,root,root,755)
%{_monodir}/*/*.mdb
%{_monodir}/gac/*/*/*.mdb

