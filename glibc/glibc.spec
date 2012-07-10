Summary:	GNU libc
Name:		glibc
Version:	2.16.0
Release:	2
Epoch:		6
License:	LGPL v2.1+
Group:		Libraries
# branch release/2.15/master
#Source0:	%{name}-%{version}.tar.xz
Source0:	http://ftp.gnu.org/pub/gnu/glibc/%{name}-%{version}.tar.xz
# Source0-md5:	80b181b02ab249524ec92822c0174cf7
Source6:	%{name}-localedb-gen
Source7:	%{name}-LD-path.c
#
Patch0:		%{name}-posix-sh.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=552960
Patch1:		%{name}-pthread_wait_cond.patch
URL:		http://www.gnu.org/software/libc/
BuildRequires:	binutils
BuildRequires:	uClibc-static
BuildRequires:	gawk
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	linux-libc-headers
BuildRequires:	perl-base
BuildRequires:	rpm-build
BuildRequires:	rpm-perlprov
BuildRequires:	sed
BuildRequires:	texinfo
Requires(post):	ldconfig = %{epoch}:%{version}-%{release}
Requires:	%{name}-misc = %{epoch}:%{version}-%{release}
Provides:	glibc(nptl)
Provides:	glibc(tls)
Provides:	rtld(GNU_HASH)
Suggests:	localedb-src
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# avoid -s here (ld.so must not be stripped to allow any program debugging)
%define		filterout_ld		(-Wl,)?-[sS] (-Wl,)?--strip.*

# avoid -D_FORTIFY_SOURCE=X
%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]+

# switch off debug
%define		specflags	-DNDEBUG

# ld.so needs not to be stripped to work
# gdb needs unstripped libpthread for some threading support
# ...but we can strip at least debuginfo from them
%define		_autostripdebug		.*/ld-[0-9.]*so\\|.*/libpthread-[0-9.]*so\\|.*libthread_db-[0-9.]*so

# we don't want perl dependency in glibc-devel
%define		_noautoreqfiles		%{_bindir}/mtrace
# hack: don't depend on rpmlib(PartialHardlinkSets) for easier upgrade from Ra
# (hardlinks here are unlikely to be "partial"... and rpm 4.0.2 from Ra was
# patched not to crash on partial hardlinks too)
%define		_hack_dontneed_PartialHardlinkSets	1
%define		_noautochrpath		.*\\(ldconfig\\|sln\\)
# private symbols
%define		_noautoprov		.*\(GLIBC_PRIVATE\)
%define		_noautoreq		.*\(GLIBC_PRIVATE\)

%description
Contains the standard libraries that are used by multiple programs on
the system. In order to save disk space and memory, as well as to ease
upgrades, common system code is kept in one place and shared between
programs. This package contains the most important sets of shared
libraries, the standard C library and the standard math library.
Without these, a Linux system will not function. It also contains
national language (locale) support.

%package misc
Summary:	Utilities and data used by glibc
Group:		Applications/System
AutoReq:	false
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description misc
Utilities and data used by glibc.

%package devel
Summary:	Additional libraries required to compile
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel-utils = %{epoch}:%{version}-%{release}
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel(%{_target_cpu}) = %{epoch}:%{version}-%{release}
Obsoletes:	libiconv-devel

%description devel
To develop programs which use the standard C libraries (which nearly
all programs do), the system needs to have these standard header files
and object files available for creating the executables.

%package -n ldconfig
Summary:	Create shared library cache and maintains symlinks
Group:		Applications/System
# This is needed because previous package (glibc) had autoreq false and had
# provided this manually. Probably poldek bug that have to have it here.
Provides:	/sbin/ldconfig

%description -n ldconfig
ldconfig scans a running system and sets up the symbolic links that
are used to load shared libraries properly. It also creates
/etc/ld.so.cache which speeds the loading programs which use shared
libraries.

%package headers
Summary:	Header files for development using standard C libraries
Group:		Development/Building
Provides:	%{name}-headers(%{_target_cpu}) = %{epoch}:%{version}-%{release}
Requires:	linux-libc-headers

%description headers
The glibc-headers package contains the header files necessary for
developing programs which use the standard C libraries (which are used
by nearly all programs). If you are developing programs which will use
the standard C libraries, your system needs to have these standard
header files available in order to create the executables.

Install glibc-headers if you are going to develop programs which will
use the standard C libraries.

%package devel-utils
Summary:	Utilities needed for development using standard C libraries
Group:		Development/Libraries
Provides:	%{name}-devel-utils(%{_target_cpu}) = %{epoch}:%{version}-%{release}

%description devel-utils
The glibc-devel-utils package contains utilities necessary for
developing programs which use the standard C libraries (which are used
by nearly all programs). If you are developing programs which will use
the standard C libraries, your system needs to have these utilities
available.

Install glibc-devel-utils if you are going to develop programs which
will use the standard C libraries.

%package devel-doc
Summary:	Documentation needed for development using standard C libraries
Group:		Documentation
Provides:	%{name}-devel-doc(%{_target_cpu}) = %{epoch}:%{version}-%{release}

%description devel-doc
The glibc-devel-doc package contains info and manual pages necessary
for developing programs which use the standard C libraries (which are
used by nearly all programs).

Install glibc-devel-doc if you are going to develop programs which
will use the standard C libraries.

%package -n localedb-src
Summary:	locale database source code
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gzip
Requires:	sed

%description -n localedb-src
This add-on package contains the data needed to build the locale data
files to use the internationalization features of the GNU libc.

%package localedb-all
Summary:	locale database for all locales supported by glibc
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	iconv = %{epoch}:%{version}-%{release}

%description localedb-all
This package contains locale database for all locales supported by
glibc. In glibc 2.3.x it's one large file (about 39MB) - if you want
something smaller with support for chosen locales only, consider
installing localedb-src and regenerating database using localedb-gen
script (when database is generated, localedb-src can be uninstalled).

%package -n iconv
Summary:	Convert encoding of given files from one encoding to another
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n iconv
Convert encoding of given files from one encoding to another. You need
this package if you want to convert some document from one encoding to
another or if you have installed some programs which use Generic
Character Set Conversion Interface.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-static(%{_target_cpu}) = %{epoch}:%{version}-%{release}
Obsoletes:	libiconv-static

%description static
GNU libc static libraries.

%package -n nss_compat
Summary:	Old style NYS NSS glibc module
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_compat
Old style NYS NSS glibc module.

%package -n nss_dns
Summary:	BIND NSS glibc module
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_dns
BIND NSS glibc module.

%package -n nss_files
Summary:	Traditional files databases NSS glibc module
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_files
Traditional files databases NSS glibc module.

%package -n nss_hesiod
Summary:	hesiod NSS glibc module
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_hesiod
glibc NSS (Name Service Switch) module for databases access.

%package -n nss_nis
Summary:	NIS(YP) NSS glibc module
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_nis
glibc NSS (Name Service Switch) module for NIS(YP) databases access.

%package -n nss_nisplus
Summary:	NIS+ NSS module
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_nisplus
glibc NSS (Name Service Switch) module for NIS+ databases access.

%package pic
Summary:	glibc PIC archive
Group:		Development/Libraries/Libc
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description pic
GNU C Library PIC archive contains an archive library (ar file)
composed of individual shared objects. This is used for creating a
library which is a smaller subset of the standard libc shared library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

chmod +x scripts/cpp

%build
rm -rf builddir
install -d builddir
cd builddir

AWK="gawk" \
../%configure \
	--disable-profile		\
	--enable-add-ons=nptl,libidn	\
	--enable-bind-now		\
	--enable-kernel="2.6.32"	\
	--enable-obsolete-rpc		\
	--with-headers=%{_includedir}	\
	--without-cvs			\
	--without-selinux
%{__make} \
	AWK="gawk" \
	sLIBdir=%{_libdir}

cd ..

CC="%{__cc}"
%{_target_cpu}-uclibc-gcc %{SOURCE7} %{rpmcflags} -Os -static -o glibc-postinst

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{default,logrotate.d,rc.d/init.d,sysconfig},%{_mandir}/man{3,8},/var/log,/var/cache/ldconfig}

cd builddir
env LANGUAGE=C LC_ALL=C \
%{__make} install \
	install_root=$RPM_BUILD_ROOT \
	infodir=%{_infodir} \
	mandir=%{_mandir}

PICFILES="libc_pic.a libc.map
	math/libm_pic.a libm.map
	resolv/libresolv_pic.a"

install -p $PICFILES $RPM_BUILD_ROOT%{_libdir}
install -p elf/soinit.os $RPM_BUILD_ROOT%{_libdir}/soinit.o
install -p elf/sofini.os $RPM_BUILD_ROOT%{_libdir}/sofini.o

# Include %{_libdir}/gconv/gconv-modules.cache
./iconv/iconvconfig --nostdlib --prefix=$RPM_BUILD_ROOT \
	%{_libdir}/gconv -o $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules.cache
cd ..

install glibc-postinst $RPM_BUILD_ROOT/sbin

mv -f $RPM_BUILD_ROOT/%{_lib}/libpcprofile.so $RPM_BUILD_ROOT%{_libdir}

# moved to tzdata package
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/localtime
rm -rf $RPM_BUILD_ROOT%{_datadir}/zoneinfo

ln -sf libbsd-compat.a $RPM_BUILD_ROOT%{_libdir}/libbsd.a

# make symlinks across top-level directories absolute
for l in BrokenLocale anl cidn crypt dl m nsl resolv rt thread_db util; do
	test -L $RPM_BUILD_ROOT%{_libdir}/lib${l}.so || exit 1
	rm -f $RPM_BUILD_ROOT%{_libdir}/lib${l}.so
	ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/lib${l}.so.*) $RPM_BUILD_ROOT%{_libdir}/lib${l}.so
done

# linking nss modules directly is not supported
rm -f $RPM_BUILD_ROOT%{_libdir}/libnss_*.so

sed -e 's#\([ \t]\)db\([ \t]\)#\1#g' nss/nsswitch.conf > $RPM_BUILD_ROOT%{_sysconfdir}/nsswitch.conf
install posix/gai.conf		$RPM_BUILD_ROOT%{_sysconfdir}
cp -a nis/nss $RPM_BUILD_ROOT/etc/default/nss

: > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.cache
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
echo 'include ld.so.conf.d/*.conf' > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf
: > $RPM_BUILD_ROOT/var/cache/ldconfig/aux-cache

# doesn't fit with out tzdata concept and configure.in is stupid assuming bash
# is first posix compatible shell making this script depend on bash.
rm -f $RPM_BUILD_ROOT%{_bindir}/tzselect
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/tzselect.8*
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man8/tzselect.8*

rm -rf documentation
install -d documentation

for f in ANNOUNCE ChangeLog DESIGN-{barrier,condvar,rwlock,sem}.txt TODO{,-kernel,-testing}; do
	cp -af nptl/$f documentation/$f.nptl
done
cp -af crypt/README.ufc-crypt ChangeLog* documentation

# Collect locale files and mark them with %%lang()
echo '%defattr(644,root,root,755)' > glibc.lang
for i in $RPM_BUILD_ROOT%{_datadir}/locale/*; do
	if [ -d $i ]; then
		lang=$(basename $i)
		dir="${i#$RPM_BUILD_ROOT}"
		echo "%lang($lang) $dir" >> glibc.lang
	fi
done

# NOTES:
# Languages not supported by glibc locales, but usable via $LANGUAGE:
#   ang - Old English (gtk+, gnome)
#   ca@valencia (gtk+, gnome; as ca_ES@valencia in FileZilla; locale exists in Debian)
#   en@shaw - English with Shavian alphabet (gnome)
#   la - Latin
#   tlh - Klingon (bzflag)
# and variants:
#   sr@ije (use LANGUAGE=sr_ME@ije/sr_RS@ije) (gnome)
#
# To be added when they become supported by glibc:
#   az_IR (gtk+2)
#   bal (newt,pessulus)
#   bem (alacarte)
#   co  (vlc)
#   fil (stellarium)
#   frp (xfce, lxlauncher)
#   gn  (gn_BR in gnome, maybe gn_PY)
#   haw (iso-codes, stellarium)
#   hrx (stellarium)
#   ilo (kudzu)
#   io  (gtk+2, gnome, alacarte)
#   jv  (gmpc, avant-window-navigator, kdesudo)
#   kok (iso-codes)
#   lb  (geany,miro,deluge)
#   man (ccsm; incorrectly named md)
#   mhr (pidgin)
#   mus (bluez-gnome)
#   pms (deluge)
#   sco (gnomad2, picard, stellarium)
#   swg (sim)
#   syr (iso-codes)
#   tet (vlc)
#
# To be removed (after fixing packages still using it):
#   sr@Latn (use sr@latin instead)
#
# To be clarified:
#   sr@ije or sr@ijekavian? (currently sr@ije is supported)
#   sr@ijelatin or sr@ijekavianlatin? (currently not supported)
#   sr@ijekavian and sr@ijekavianlatin exist in: akonadi-googledata, amarok, k3b, konversation, ktorrent, wesnoth
#
# Short forms (omitted country code, used instead of long form) for ambiguous or unclear cases:
# aa=aa_ER
# ar=common? (AE, BH, DZ, EG, IQ, JO, KW, LB, LY, MA, OM, QA, SA, SD, SY, TN, YE)
# bn=bn_BD
# bo=bo_CN? (or common for CN, IN?)
# ca=ca_ES
# ckb=ckb_IQ
# de=de_DE
# en=common? (en_AU, en_CA, en_GB, en_NZ, en_US are used for particular variants)
# eo=common
# es=es_ES
# eu=eu_ES
# fr=fr_FR
# fy=fy_NL
# gez=gez_ET (?)
# it=it_IT
# li=li_NL
# nds=nds_DE
# nl=nl_NL
# om=om_ET
# pa=pa_IN
# pt=pt_PT
# ru=ru_RU
# so=so_SO
# sr=sr_RS [cyrillic]
# sv=sv_SE
# sw=sw_TZ (or common for KE, TZ, UG?)
# ta=ta_IN
# te=te_IN
# ti=ti_ER (?)
# tr=tr_TR
# ur=ur_PK (?)
# zh: no short code used (use zh_CN, zh_HK, zh_SG[not included yet], zh_TW)
#
# Omitted here - already existing (with libc.mo):
#   be ca cs da de el en_GB es fi fr gl hr hu it ja ko nb nl pl pt_BR ru rw sk
#   sv tr zh_CN zh_TW
#
for i in aa aa@saaho af am an ang ar ar_TN as ast az be@latin be@tarask \
	bg bn bn_IN bo br bs byn ca@valencia ckb crh csb cy de_AT de_CH dv dz en \
	en@boldquot en@quot en@shaw en_AU en_CA en_NZ en_US eo es_AR es_CL es_CO es_CR \
	es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_SV es_UY \
	es_VE et eu fa fil fo fr_BE fr_CA fr_CH fur fy ga gd gez gu gv ha he \
	hi hne hsb hy ia id ig ik is it_CH iu ka kg kk kl km kn ks ku kw ky la \
	lg li lo lt lv mai mg mi mk ml mn mr ms mt my nds ne nl_BE nn nr nso \
	oc om or pa pap ps pt ps rm ro sa sc se si sid sl so sq sr sr@Latn tl \
	sr@ije sr@latin ss st sw ta te tg th ti tig tk tl tlh tn ts tt ug uk \
	ur uz uz@cyrillic ve vi wa wal wo xh yi yo zh_HK zu; do
	if [ ! -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES ]; then
		install -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES
		# use lang() tags with ll_CC@variant (stripping charset and @quot|@boldquot)
		lang=$(echo $i | sed -e 's/@quot\>\|@boldquot\>//')
		echo "%lang($lang) %{_datadir}/locale/$i" >> glibc.lang
	fi
done

# LC_TIME category, used for localized date formats (at least by coreutils)
for i in af be bg ca cs da de el en eo es et eu fi fr ga gl hu id it ja kk ko lg lt \
	ms nb nl pl pt pt_BR ro ru rw sk sl sv tr uk vi zh_CN zh_TW; do
	if [ ! -d $RPM_BUILD_ROOT%{_datadir}/locale/$i ]; then
		echo "%lang($lang) %{_datadir}/locale/$i" >> glibc.lang
	fi
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_TIME
done

# localedb-gen infrastructure
sed -e 's,@localedir@,%{_libdir}/locale,' %{SOURCE6} > $RPM_BUILD_ROOT%{_bindir}/localedb-gen
chmod +x $RPM_BUILD_ROOT%{_bindir}/localedb-gen
install localedata/SUPPORTED $RPM_BUILD_ROOT%{_datadir}/i18n

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# we don't support kernel without ptys support
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pt_chown

%if 0
%check
cd builddir
%{__make} -j1 check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/glibc-postinst /%{_lib}/%{_host_cpu} /%{_lib}/tls
/sbin/ldconfig

%postun	-p /sbin/ldconfig

%post -n iconv -p %{_sbindir}/iconvconfig

%post -n localedb-src
SUPPORTED_LOCALES=
[ -f /etc/sysconfig/i18n ] && . /etc/sysconfig/i18n
[ -f /etc/sysconfig/localedb ] && . /etc/sysconfig/localedb
if [ "$SUPPORTED_LOCALES" ]; then
	localedb-gen || :
fi

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS BUGS
%attr(755,root,root) /sbin/glibc-postinst
# TODO: package ldconfig symlinks as %ghost
%attr(755,root,root) /%{_lib}/ld-*.so
# wildly arch-dependent ld.so SONAME symlink
%attr(755,root,root) /%{_lib}/ld-linux.so.2
%attr(755,root,root) /%{_lib}/libBrokenLocale-*.so
%attr(755,root,root) /%{_lib}/libBrokenLocale.so.1
%attr(755,root,root) /%{_lib}/libSegFault.so
%attr(755,root,root) /%{_lib}/libanl-*.so
%attr(755,root,root) /%{_lib}/libanl.so.1
%attr(755,root,root) /%{_lib}/libc-*.so
%attr(755,root,root) /%{_lib}/libc.so.6
%attr(755,root,root) /%{_lib}/libcidn-*.so
%attr(755,root,root) /%{_lib}/libcidn.so.1
%attr(755,root,root) /%{_lib}/libcrypt-*.so
%attr(755,root,root) /%{_lib}/libcrypt.so.1
%attr(755,root,root) /%{_lib}/libdl-*.so
%attr(755,root,root) /%{_lib}/libdl.so.2
%attr(755,root,root) /%{_lib}/libm-*.so
%attr(755,root,root) /%{_lib}/libm.so.6
%attr(755,root,root) /%{_lib}/libnsl-*.so
%attr(755,root,root) /%{_lib}/libnsl.so.1
%attr(755,root,root) /%{_lib}/libpthread-*.so
%attr(755,root,root) /%{_lib}/libpthread.so.0
%attr(755,root,root) /%{_lib}/libresolv-*.so
%attr(755,root,root) /%{_lib}/libresolv.so.2
%attr(755,root,root) /%{_lib}/librt-*.so
%attr(755,root,root) /%{_lib}/librt.so.1
%attr(755,root,root) /%{_lib}/libthread_db-1.0.so
%attr(755,root,root) /%{_lib}/libthread_db.so.1
%attr(755,root,root) /%{_lib}/libutil-*.so
%attr(755,root,root) /%{_lib}/libutil.so.1

%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_dns-*.so
%attr(755,root,root) /%{_lib}/libnss_dns.so.2

%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_files-*.so
%attr(755,root,root) /%{_lib}/libnss_files.so.2

%attr(755,root,root) %{_bindir}/makedb
%attr(755,root,root) /%{_lib}/libnss_db-*.so
%attr(755,root,root) /%{_lib}/libnss_db.so.2
%{_var}/db/Makefile

%files -n ldconfig
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/ldconfig
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ld.so.conf
%dir %attr(700,root,root) /var/cache/ldconfig
%dir %{_sysconfdir}/ld.so.conf.d
%ghost %attr(600,root,root) /var/cache/ldconfig/aux-cache
%ghost %{_sysconfdir}/ld.so.cache

%files misc -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/catchsegv
%attr(755,root,root) %{_bindir}/ldd
%attr(755,root,root) %{_bindir}/pldd

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nsswitch.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gai.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/nss

%config %{_sysconfdir}/rpc

%attr(755,root,root) /sbin/sln
%attr(755,root,root) %{_bindir}/catchsegv
%attr(755,root,root) %{_bindir}/getconf
%attr(755,root,root) %{_bindir}/getent
%attr(755,root,root) %{_bindir}/iconv
%attr(755,root,root) %{_bindir}/lddlibc4
%attr(755,root,root) %{_bindir}/locale
%attr(755,root,root) %{_bindir}/rpcgen

%attr(755,root,root) %{_sbindir}/zdump
%attr(755,root,root) %{_sbindir}/zic

%dir %{_libexecdir}/getconf
%attr(755,root,root) %{_libexecdir}/getconf/*

%dir %{_datadir}/locale
%{_datadir}/locale/locale.alias

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libBrokenLocale.so
%attr(755,root,root) %{_libdir}/libanl.so
%attr(755,root,root) %{_libdir}/libcrypt.so
%attr(755,root,root) %{_libdir}/libcidn.so
%attr(755,root,root) %{_libdir}/libdl.so
%attr(755,root,root) %{_libdir}/libm.so
%attr(755,root,root) %{_libdir}/libnsl.so
%attr(755,root,root) %{_libdir}/libpcprofile.so
%attr(755,root,root) %{_libdir}/libresolv.so
%attr(755,root,root) %{_libdir}/librt.so
%attr(755,root,root) %{_libdir}/libthread_db.so
%attr(755,root,root) %{_libdir}/libutil.so
%{_libdir}/crt[1in].o
%{_libdir}/[MSg]crt1.o
# ld scripts
%{_libdir}/libc.so
%{_libdir}/libpthread.so
# static-only libs
%{_libdir}/libbsd-compat.a
%{_libdir}/libbsd.a
%{_libdir}/libc_nonshared.a
%{_libdir}/libg.a
%{_libdir}/libieee.a
%{_libdir}/libpthread_nonshared.a
%{_libdir}/librpcsvc.a
%{_includedir}/gnu/stubs-*.h

%files headers
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/arpa
%{_includedir}/bits
%dir %{_includedir}/gnu
%{_includedir}/gnu/lib*.h
%{_includedir}/gnu/stubs.h
%{_includedir}/net
%{_includedir}/netash
%{_includedir}/netatalk
%{_includedir}/netax25
%{_includedir}/neteconet
%{_includedir}/netiucv
%{_includedir}/netinet
%{_includedir}/netipx
%{_includedir}/netpacket
%{_includedir}/netrom
%{_includedir}/netrose
%{_includedir}/nfs
%{_includedir}/protocols
%{_includedir}/rpc
%{_includedir}/rpcsvc
%{_includedir}/scsi
%{_includedir}/sys

%files devel-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gencat
%attr(755,root,root) %{_bindir}/*prof*
%attr(755,root,root) %{_bindir}/*trace

%files devel-doc
%defattr(644,root,root,755)
%doc documentation/* PROJECTS
%{_infodir}/libc.info*

%files -n localedb-src
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/localedef
%attr(755,root,root) %{_bindir}/localedb-gen
%{_datadir}/i18n

%if 0
%files localedb-all
%defattr(644,root,root,755)
%{_libdir}/locale/locale-archive
%endif

%files -n iconv
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/iconvconfig
%dir %{_libdir}/gconv
%{_libdir}/gconv/gconv-modules
%verify(not md5 mtime size) %{_libdir}/gconv/gconv-modules.cache
%attr(755,root,root) %{_libdir}/gconv/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libanl.a
%{_libdir}/libBrokenLocale.a
%{_libdir}/libc.a
%{_libdir}/libcrypt.a
%{_libdir}/libdl.a
%{_libdir}/libm.a
%{_libdir}/libmcheck.a
%{_libdir}/libnsl.a
%{_libdir}/libpthread.a
%{_libdir}/libresolv.a
%{_libdir}/librt.a
%{_libdir}/libutil.a

%files -n nss_compat
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_compat-*.so
%attr(755,root,root) /%{_lib}/libnss_compat.so.2

%files -n nss_hesiod
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_hesiod-*.so
%attr(755,root,root) /%{_lib}/libnss_hesiod.so.2

%files -n nss_nis
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_nis-*.so
%attr(755,root,root) /%{_lib}/libnss_nis.so.2

%files -n nss_nisplus
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_nisplus-*.so
%attr(755,root,root) /%{_lib}/libnss_nisplus.so.2

%files pic
%defattr(644,root,root,755)
%{_libdir}/lib*_pic.a
%{_libdir}/lib*.map
%{_libdir}/soinit.o
%{_libdir}/sofini.o

