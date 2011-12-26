%define		gitver	%{nil}
%define		rel	3

Summary:	C library optimized for size
Name:		uClibc
Version:	0.9.32
Epoch:		1
%if "%{gitver}" != "%{nil}"
Release:	0.%{gitver}.%{rel}
Source0:	http://git.uclibc.org/uClibc/snapshot/%{name}-%{gitver}.tar.bz2
# Source0-md5:	51660b93b8f1edb486049981fecfd148
%else
Release:	%{rel}
Source0:	http://uclibc.org/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	51660b93b8f1edb486049981fecfd148
%endif
License:	LGPL v2.1
Group:		Libraries
Patch0:		%{name}-targetcpu.patch
Patch1:		%{name}-toolchain-wrapper.patch
Patch2:		%{name}-epoll-fix.patch
URL:		http://uclibc.org/
BuildRequires:	cpp
BuildRequires:	linux-libc-headers
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		uclibc_root	/usr/%{_target_cpu}-linux-uclibc

%description
Small libc for building embedded applications.

%package devel
Summary:	Development files for uClibc
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	binutils
Requires:	linux-libc-headers
%requires_eq	gcc

%description devel
Small libc for building embedded applications.

%package static
Summary:	Static uClibc libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	libc-static

%description static
Static uClibc libraries.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn %{name}-%{gitver}
%else
%setup -q
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's|-Wl,-z,combreloc||' Rules.mak

# ARCH is already determined by uname -m
%ifarch %{ix86}
defconfig=extra/Configs/defconfigs/i386
echo 'CONFIG_686=y' >> $defconfig
%endif
%ifarch %{x8664}
defconfig=extra/Configs/defconfigs/x86_64
%endif

cat <<'EOF' >> $defconfig
UCLIBC_HAS_IPV6=y
DO_C99_MATH=y
UCLIBC_HAS_RPC=y
# UCLIBC_HAS_FULL_RPC is not set
# UCLIBC_HAS_REENTRANT_RPC is not set
UCLIBC_HAS_SYS_SIGLIST=y
LDSO_GNU_HASH_SUPPORT=y
SHARED_LIB_LOADER_PREFIX="$(RUNTIME_PREFIX)/lib"
UCLIBC_HAS_PRINTF_M_SPEC=y
UCLIBC_SUSV3_LEGACY=y
UCLIBC_SUSV3_LEGACY_MACROS=y
# DOSTRIP is not set
# UCLIBC_LINUX_MODULE_24 is not set
# UCLIBC_BSD_SPECIFIC is not set
UCLIBC_EXTRA_CFLAGS="%{rpmcflags} -Os"
%if %{with debug}
DODEBUG=y
SUPPORT_LD_DEBUG=y
SUPPORT_LD_DEBUG_EARLY=y
%endif
EOF

%build

# NOTE: 'defconfig' and 'all' must be run in separate make process because of macros
%{__make} defconfig \
	CC="%{__cc}"					\
	GCC_BIN=%{_target_cpu}-freddix-linux-gcc	\
	HOSTCC=%{_target_cpu}-freddix-linux-gcc		\
	HOSTCFLAGS="%{rpmcflags} %{rpmldflags}"		\
	TARGET_CPU="%{_target_cpu}"			\

# The Makefile includes .config and later tries to assign same variable,
# eventually it gets lost and sets wrong value for TARGET_ARCH and bad value
# for UCLIBC_LDSO in extra/gcc-uClibc.
# So we pass it as make arg to be sure it's proper!
target_arch=$(grep -s '^TARGET_ARCH' .config | sed -e 's/^TARGET_ARCH=//' -e 's/"//g')

%{__make} \
	CC="%{__cc}"					\
	GCC_BIN=%{_host_cpu}-%{_vendor}-%{_os}-gcc	\
	HOSTCC="%{__cc}"				\
	HOSTCFLAGS="%{rpmcflags} %{rpmldflags}"		\
	TARGET_ARCH=$target_arch			\
	TARGET_CPU="%{_target_cpu}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -j1 install \
	CC="%{__cc}"				\
	DESTDIR=$RPM_BUILD_ROOT			\
	HOSTCFLAGS="%{rpmcflags} %{rpmldflags}"	\
	HOSTCC="%{__cc}"			\
	TARGET_CPU="%{_target_cpu}"		\
	VERBOSE=0

#mv -f $RPM_BUILD_ROOT%{uclibc_root}/usr/lib/{libpthread-uclibc,libpthread}.so
#ln -sf libpthread-%{version}.so $RPM_BUILD_ROOT%{uclibc_root}/lib/libpthread.so.0
chmod a+rx $RPM_BUILD_ROOT%{uclibc_root}/lib/*.so

# these links are *needed* (by stuff in bin/)
for f in $RPM_BUILD_ROOT%{uclibc_root}/bin/*; do
	if [ -L $f ]; then
		l=$(readlink $f)
		a=${l##*/}
		d=${l%/*}
		case "$d" in
		%{_bindir})
			ln -sf ${l#%{_bindir}/} $RPM_BUILD_ROOT%{_bindir}/${f##*/}
			rm -f $f
			;;
		$a)
			mv -f $f $RPM_BUILD_ROOT%{_bindir}
			;;
		*)
			exit 1
			;;
		esac
	else
		a=${f#*/%{_target_cpu}-uclibc-}
		ln -sf %{_bindir}/$(basename $f) $RPM_BUILD_ROOT%{uclibc_root}/usr/bin/$a
		mv -f $f $RPM_BUILD_ROOT%{_bindir}
	fi
done

%if 0
for f in $RPM_BUILD_ROOT%{uclibc_root}/usr/bin/*; do
	if [ -L $f ]; then
		l=$(readlink $f)
		case "${l%/*}" in
		%{uclibc_root}/bin)
			a=${l#*/%{_target_cpu}-uclibc-}
			ln -sf %{_bindir}/$a $f
			echo $f
			;;
		%{_bindir})
			:
			;;
		*)
			exit 2
			;;
		esac
	fi
done
%endif

rm -rf $RPM_BUILD_ROOT%{uclibc_root}/usr/include/{linux,asm*}
ln -sf /usr/include/asm $RPM_BUILD_ROOT%{uclibc_root}/usr/include/asm
ln -sf /usr/include/asm-generic $RPM_BUILD_ROOT%{uclibc_root}/usr/include/asm-generic
ln -sf /usr/include/linux $RPM_BUILD_ROOT%{uclibc_root}/usr/include/linux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog* DEDICATION.mjn3 MAINTAINERS README TODO
%dir %{uclibc_root}
%dir %{uclibc_root}/lib
%attr(755,root,root) %{uclibc_root}/lib/*.so*


%files devel
%defattr(644,root,root,755)
%doc docs/*.txt
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-addr2line
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-ar
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-as
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-c++
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-cc
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-cpp
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-g++
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-gcc
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-ld
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-nm
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-objcopy
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-objdump
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-ranlib
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-size
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-strings
%attr(755,root,root) %{_bindir}/%{_target_cpu}-uclibc-strip
%{uclibc_root}/usr/lib/*.o

%dir %{uclibc_root}/usr
%dir %{uclibc_root}/usr/bin
%dir %{uclibc_root}/usr/lib

%attr(755,root,root) %{uclibc_root}/usr/bin/addr2line
%attr(755,root,root) %{uclibc_root}/usr/bin/ar
%attr(755,root,root) %{uclibc_root}/usr/bin/as
%attr(755,root,root) %{uclibc_root}/usr/bin/c++
%attr(755,root,root) %{uclibc_root}/usr/bin/cc
%attr(755,root,root) %{uclibc_root}/usr/bin/cpp
%attr(755,root,root) %{uclibc_root}/usr/bin/g++
%attr(755,root,root) %{uclibc_root}/usr/bin/gcc
%attr(755,root,root) %{uclibc_root}/usr/bin/ld
%attr(755,root,root) %{uclibc_root}/usr/bin/nm
%attr(755,root,root) %{uclibc_root}/usr/bin/objcopy
%attr(755,root,root) %{uclibc_root}/usr/bin/objdump
%attr(755,root,root) %{uclibc_root}/usr/bin/ranlib
%attr(755,root,root) %{uclibc_root}/usr/bin/size
%attr(755,root,root) %{uclibc_root}/usr/bin/strings
%attr(755,root,root) %{uclibc_root}/usr/bin/strip
%attr(755,root,root) %{uclibc_root}/usr/lib/*.so

%{uclibc_root}/usr/lib/uclibc_nonshared.a
%{uclibc_root}/usr/include

%files static
%defattr(644,root,root,755)
%{uclibc_root}/usr/lib/lib*.a

