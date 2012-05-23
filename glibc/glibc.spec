Summary:	GNU libc
Name:		glibc
Version:	2.12.2
Release:	4
Epoch:		6
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnu.org/pub/gnu/glibc/%{name}-%{version}.tar.xz
# Source0-md5:	e0043f4f8e1aa61acc62fdf0f4d6133d
Source6:	%{name}-localedb-gen
Source7:	%{name}-LD-path.c
#
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-crypt-blowfish.patch
Patch3:		%{name}-paths.patch
Patch4:		%{name}-no_opt_override.patch
Patch5:		%{name}-missing-nls.patch
Patch6:		%{name}-info.patch
Patch7:		%{name}-no_debuggable_objects.patch
Patch8:		%{name}-new-charsets.patch
Patch9:		%{name}-thread_start.patch
#
Patch20:	%{name}-tzfile-noassert.patch
Patch21:	%{name}-morelocales.patch
Patch22:	%{name}-locale_fixes.patch
Patch23:	%{name}-ZA_collate.patch
Patch24:	%{name}-with-stroke.patch
Patch25:	%{name}-cv_gnu89_inline.patch
Patch26:	%{name}-posix-sh.patch
Patch27:	%{name}-static-shared-getpagesize.patch
Patch28:	%{name}-ignore-origin-of-privileged-program.patch
Patch29:	%{name}-bug12343.patch
URL:		http://www.gnu.org/software/libc/
BuildRequires:	autoconf
BuildRequires:	automake
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
Requires:	basesystem
Provides:	glibc(nptl)
Provides:	glibc(tls)
Provides:	rtld(GNU_HASH)
Suggests:	localedb-src
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# avoid -s here (ld.so must not be stripped to allow any program debugging)
%define		filterout_ld		(-Wl,)?-[sS] (-Wl,)?--strip.*
# avoid -D_FORTIFY_SOURCE=X
%define		filterout_cpp		-D_FORTIFY_SOURCE=[0-9]+

# optimize it a lot, switch off debug
%define		specflags	-DNDEBUG

# ld.so needs not to be stripped to work
# gdb needs unstripped libpthread for some threading support
# ...but we can strip at least debuginfo from them
%define		_autostripdebug		.*/libpthread-[0-9.]*so\\|.*/ld-[0-9.]*so

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

chmod +x scripts/cpp

# i786 (aka pentium4) hack
ln -s i686 nptl/sysdeps/i386/i786
ln -s i686 nptl/sysdeps/unix/sysv/linux/i386/i786

%build
cp -f /usr/share/automake/config.sub scripts
%{__aclocal}
%{__autoconf}

rm -rf builddir
install -d builddir
cd builddir

AWK="gawk" \
../%configure \
	--disable-profile			\
	--enable-add-ons=nptl,libidn		\
	--enable-bind-now			\
	--enable-hidden-plt			\
	--enable-kernel="2.6.32"		\
	--enable-stackguard-randomization	\
	--with-__thread				\
	--with-headers=%{_includedir}		\
	--with-tls				\
	--without-cvs				\
	--without-gd 				\
	--without-selinux

%{__make} \
	AWK="gawk" \
	sLIBdir=%{_libdir}

cd ..

%if 0
cd builddir
env LANGUAGE=C LC_ALL=C \
%{__make} tests 2>&1 | awk '
BEGIN { file = "" }
{
	if (($0 ~ /\*\*\* \[.*\.out\] Error/) && ($0 !~ /annexc/) && (file == "")) {
		file=$0;
		gsub(/.*\[/, NIL, file);
		gsub(/\].*/, NIL, file);
	}
	print $0;
}
END { if (file != "") { print "ERROR OUTPUT FROM " file; system("cat " file); exit(1); } }'
cd ..
done
%endif

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

%if 0
env LANGUAGE=C LC_ALL=C \
%{__make} localedata/install-locales \
	install_root=$RPM_BUILD_ROOT
%endif

PICFILES="libc_pic.a libc.map
	math/libm_pic.a libm.map
	resolv/libresolv_pic.a"

install -p $PICFILES	$RPM_BUILD_ROOT%{_libdir}
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

ln -sf libbsd-compat.a		$RPM_BUILD_ROOT%{_libdir}/libbsd.a

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
#   tlh - Klingon (bzflag)
# and variants:
#   sr@ije (use LANGUAGE=sr_ME@ije/sr_RS@ije) (gnome)
#
# To be added when they become supported by glibc:
#   az_IR (gtk+2)
#   bal (newt,pessulus)
#   bem (alacarte)
#   ckb [or ku_IQ/ku_IR] (vlc,miro)
#   co  (vlc)
#   gn  (gn_BR in gnome, maybe gn_PY)
#   bal (newt)
#   haw (iso-codes)
#   ilo (kudzu)
#   io  (gtk+2, gnome, alacarte)
#   jv  (gmpc)
#   kok (iso-codes)
#   lb  (geany,miro)
#   man (ccsm; incorrectly named md)
#   mus (bluez-gnome)
#   sco (gnomad2, picard)
#   swg (sim)
#   syr (iso-codes)
#   tet (vlc)
#
# bn is used for bn_BD or bn_IN? Assume bn_IN as nothing for bn_BD appeared
# till now.
#
# Omitted here - already existing (with libc.mo):
#   be ca cs da de el en_GB es fi fr gl hr hu it ja ko nb nl pl pt_BR ru rw sk
#   sv tr zh_CN zh_TW
#
for i in aa aa@saaho af am an ang ar ar_TN as ast az be@alternative be@latin \
	bg bn bn_IN bo br bs byn ca@valencia crh csb cy de_AT de_CH dv dz en \
	en@boldquot en@quot en@shaw en_AU en_CA en_NZ en_US eo es_AR es_CL es_CO es_CR \
	es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_SV es_UY \
	es_VE et eu fa fil fo fr_BE fr_CA fr_CH fur fy ga gd gez gu gv ha he \
	hi hne hsb hy ia id ig ik is it_CH iu jv ka kk kl km kn ks ku kw ky la \
	lg li lo lt lv mai mg mi mk ml mn mr ms mt my nds ne nl_BE nn nr nso \
	oc om or pa pap ps pt ps rm ro sa sc se si sid sl so sq sr sr@Latn \
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
for i in af be bg ca cs da de el en eo es et eu fi fr ga gl hu id it ja ko lg lt \
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
rm -f $RPM_BUILD_ROOT%{_mandir}/README.*
rm -f $RPM_BUILD_ROOT%{_mandir}/diff.*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# we don't support kernel without ptys support
rm -f $RPM_BUILD_ROOT%{_libdir}/pt_chown
# rpcbind
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man8/rpcinfo.8
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/rpcinfo.8
rm -f $RPM_BUILD_ROOT%{_sbindir}/rpcinfo

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
%doc README NEWS FAQ BUGS
%attr(755,root,root) /sbin/glibc-postinst
# TODO: package ldconfig symlinks as %ghost
%attr(755,root,root) /%{_lib}/ld-%{version}.so
# wildly arch-dependent ld.so SONAME symlink
%attr(755,root,root) /%{_lib}/ld-linux.so.2
%attr(755,root,root) /%{_lib}/libBrokenLocale-%{version}.so
%attr(755,root,root) /%{_lib}/libBrokenLocale.so.1
%attr(755,root,root) /%{_lib}/libSegFault.so
%attr(755,root,root) /%{_lib}/libanl-%{version}.so
%attr(755,root,root) /%{_lib}/libanl.so.1
%attr(755,root,root) /%{_lib}/libc-%{version}.so
%attr(755,root,root) /%{_lib}/libc.so.6
%attr(755,root,root) /%{_lib}/libcidn-%{version}.so
%attr(755,root,root) /%{_lib}/libcidn.so.1
%attr(755,root,root) /%{_lib}/libcrypt-%{version}.so
%attr(755,root,root) /%{_lib}/libcrypt.so.1
%attr(755,root,root) /%{_lib}/libdl-%{version}.so
%attr(755,root,root) /%{_lib}/libdl.so.2
%attr(755,root,root) /%{_lib}/libm-%{version}.so
%attr(755,root,root) /%{_lib}/libm.so.6
%attr(755,root,root) /%{_lib}/libnsl-%{version}.so
%attr(755,root,root) /%{_lib}/libnsl.so.1
%attr(755,root,root) /%{_lib}/libpthread-%{version}.so
%attr(755,root,root) /%{_lib}/libpthread.so.0
%attr(755,root,root) /%{_lib}/libresolv-%{version}.so
%attr(755,root,root) /%{_lib}/libresolv.so.2
%attr(755,root,root) /%{_lib}/librt-%{version}.so
%attr(755,root,root) /%{_lib}/librt.so.1
%attr(755,root,root) /%{_lib}/libthread_db-1.0.so
%attr(755,root,root) /%{_lib}/libthread_db.so.1
%attr(755,root,root) /%{_lib}/libutil-%{version}.so
%attr(755,root,root) /%{_lib}/libutil.so.1

%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_dns-%{version}.so
%attr(755,root,root) /%{_lib}/libnss_dns.so.2

%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_files-%{version}.so
%attr(755,root,root) /%{_lib}/libnss_files.so.2

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

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nsswitch.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gai.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/nss

%config %{_sysconfdir}/rpc

%attr(755,root,root) /sbin/sln
%attr(755,root,root) %{_bindir}/catchsegv
%attr(755,root,root) %{_bindir}/getconf
%attr(755,root,root) %{_bindir}/getent
%attr(755,root,root) %{_bindir}/iconv
%attr(755,root,root) %{_bindir}/ldd
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
%doc documentation/* NOTES PROJECTS
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

%files pic
%defattr(644,root,root,755)
%{_libdir}/lib*_pic.a
%{_libdir}/lib*.map
%{_libdir}/soinit.o
%{_libdir}/sofini.o

