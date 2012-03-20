%define		foover	%(echo %{version} | tr . _)

Summary:	Network Security Services
Name:		nss
Version:	3.13.3
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_%{foover}_RTM/src/%{name}-%{version}.tar.gz
# Source0-md5:	006cb82fa900e9e664b4b14a9b7810ca
Source1:	%{name}-mozilla-nss.pc
Source2:	%{name}-config.in
Source3:	http://www.cacert.org/certs/root.der
# Source3-md5:	a61b375e390d9c3654eebd2031461f6b
Patch0:		%{name}-makefile.patch
URL:		http://www.mozilla.org/projects/security/pki/nss/
BuildRequires:	nspr-devel >= 1:4.9
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautostrip    .*%{_libdir}/libfreebl3.so\\|.*%{_libdir}/libsoftokn3.so
%define         _noautochrpath  .*%{_libdir}/libfreebl3.so\\|.*%{_libdir}/libsoftokn3.so

%description
NSS supports cross-platform development of security-enabled server
applications. Applications built with NSS can support PKCS #5,
PKCS #7, PKCS #11, PKCS #12, S/MIME, TLS, SSL v2 and v3, X.509 v3
certificates, and other security standards.

%package tools
Summary:	NSS command line tools and utilities
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tools
The NSS Toolkit command line tool.

%package devel
Summary:	NSS - header files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development part of NSS library.

%package static
Summary:	NSS - static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static NSS Toolkit libraries.

%prep
%setup -q
%patch0 -p1

sed -i -e '/export ADDON_PATH$/a\    echo STRIP \; %{__strip} --strip-unneeded -R.comment -R.note ${5}' mozilla/security/nss/cmd/shlibsign/sign.sh

%build
cd mozilla/security/nss

# http://wiki.cacert.org/wiki/NSSLib
addbuiltin -n "CAcert Inc." -t "CT,C,C" < %{SOURCE3} >> lib/ckfw/builtins/certdata.txt
%{__make} -C lib/ckfw/builtins generate

%{__make} -j1 build_coreconf		\
	BUILD_OPT=1			\
	FREEBL_NO_DEPEND=1		\
	MOZILLA_CLIENT=1		\
	NO_MDUPDATE=1			\
	NSDISTMODE=copy			\
	NS_USE_GCC=1			\
	OPTIMIZER="%{rpmcflags}"	\
	USE_PTHREADS=1

%{__make} -j1 build_dbm			\
	BUILD_OPT=1			\
	FREEBL_NO_DEPEND=1		\
	MOZILLA_CLIENT=1		\
	NO_MDUPDATE=1			\
	NSDISTMODE=copy			\
	NS_USE_GCC=1			\
	OPTIMIZER="%{rpmcflags}"	\
	PLATFORM="freddix"		\
	USE_PTHREADS=1

%{__make} -j1 all			\
	BUILD_OPT=1			\
	FREEBL_NO_DEPEND=1		\
	LOWHASH_EXPORTS=nsslowhash.h	\
	MOZILLA_CLIENT=1		\
	NO_MDUPDATE=1			\
	NSDISTMODE=copy			\
	NS_USE_GCC=1			\
	OPTIMIZER="%{rpmcflags}"	\
	PLATFORM="freddix"		\
	USE_PTHREADS=1			\
	USE_SYSTEM_ZLIB=1		\
	ZLIB_LIBS="-lz"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/nss,/%{_lib},%{_libdir},%{_pkgconfigdir}}

install mozilla/dist/private/nss/* $RPM_BUILD_ROOT%{_includedir}/nss
install mozilla/dist/public/dbm/*  $RPM_BUILD_ROOT%{_includedir}/nss
install mozilla/dist/public/nss/*  $RPM_BUILD_ROOT%{_includedir}/nss
install mozilla/dist/freddix/bin/*  $RPM_BUILD_ROOT%{_bindir}
install mozilla/dist/freddix/lib/*  $RPM_BUILD_ROOT%{_libdir}

sed -e '
	s#libdir=.*#libdir=%{_libdir}#g
	s#includedir=.*#includedir=%{_includedir}#g
	s#VERSION#%{version}#g
' %{SOURCE1} > $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nss.pc

ln -s mozilla-nss.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/nss.pc

NSS_VMAJOR=$(awk '/#define.*NSS_VMAJOR/ {print $3}' mozilla/security/nss/lib/nss/nss.h)
NSS_VMINOR=$(awk '/#define.*NSS_VMINOR/ {print $3}' mozilla/security/nss/lib/nss/nss.h)
NSS_VPATCH=$(awk '/#define.*NSS_VPATCH/ {print $3}' mozilla/security/nss/lib/nss/nss.h)

sed -e "
	s,@libdir@,%{_libdir},g
	s,@prefix@,%{_prefix},g
	s,@exec_prefix@,%{_prefix},g
	s,@includedir@,%{_includedir}/nss,g
	s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g
	s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g
	s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g
" %{SOURCE2} > $RPM_BUILD_ROOT%{_bindir}/nss-config
chmod +x $RPM_BUILD_ROOT%{_bindir}/nss-config

mv $RPM_BUILD_ROOT%{_libdir}/libfreebl3.so $RPM_BUILD_ROOT/%{_lib}
ln -s /%{_lib}/libfreebl3.so $RPM_BUILD_ROOT%{_libdir}/libfreebl3.so
mv $RPM_BUILD_ROOT%{_libdir}/libfreebl3.chk $RPM_BUILD_ROOT/%{_lib}
ln -s /%{_lib}/libfreebl3.chk $RPM_BUILD_ROOT%{_libdir}/libfreebl3.chk

[ -f "$RPM_BUILD_ROOT%{_includedir}/nss/nsslowhash.h" ] || exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreebl3.so
%attr(755,root,root) %{_libdir}/libnss3.so
%attr(755,root,root) %{_libdir}/libnssckbi.so
%attr(755,root,root) %{_libdir}/libnssdbm3.so
%attr(755,root,root) %{_libdir}/libnssutil3.so
%attr(755,root,root) %{_libdir}/libsmime3.so
%attr(755,root,root) %{_libdir}/libsoftokn3.so
%attr(755,root,root) %{_libdir}/libssl3.so
%{_libdir}/libfreebl3.chk
%{_libdir}/libnssdbm3.chk
%{_libdir}/libsoftokn3.chk

%attr(755,root,root) /%{_lib}/libfreebl3.so
/%{_lib}/libfreebl3.chk


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nss-config
%{_includedir}/nss
%{_libdir}/libcrmf.a
%{_pkgconfigdir}/mozilla-nss.pc
%{_pkgconfigdir}/nss.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcertdb.a
%{_libdir}/libcerthi.a
%{_libdir}/libcryptohi.a
%{_libdir}/libdbm.a
%{_libdir}/libfreebl3.a
%{_libdir}/libjar.a
%{_libdir}/libnss3.a
%{_libdir}/libnssb.a
%{_libdir}/libnssckfw.a
%{_libdir}/libnssdbm3.a
%{_libdir}/libnssdev.a
%{_libdir}/libnsspki3.a
%{_libdir}/libnssutil3.a
%{_libdir}/libpk11wrap3.a
%{_libdir}/libpkcs12.a
%{_libdir}/libpkcs7.a
%{_libdir}/libpkixcertsel.a
%{_libdir}/libpkixchecker.a
%{_libdir}/libpkixcrlsel.a
%{_libdir}/libpkixmodule.a
%{_libdir}/libpkixparams.a
%{_libdir}/libpkixpki.a
%{_libdir}/libpkixresults.a
%{_libdir}/libpkixstore.a
%{_libdir}/libpkixsystem.a
%{_libdir}/libpkixtop.a
%{_libdir}/libpkixutil.a
%{_libdir}/libsectool.a
%{_libdir}/libsmime3.a
%{_libdir}/libsoftokn3.a
%{_libdir}/libssl3.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/nss-config

