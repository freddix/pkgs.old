%bcond_with	bootstrap
#
Summary:	GNU Compiler Collection: the C compiler and shared files
Name:		gcc
Version:	4.4.6
Release:	1
Epoch:		6
License:	GPL v3+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ab525d429ee4425050a554bc9247d6c4
Source1:	%{name}-optimize-la.pl
Patch0:		%{name}-nolocalefiles.patch
Patch1:		%{name}-nodebug.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils
BuildRequires:	bison
BuildRequires:	chrpath
BuildRequires:	fileutils
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	binutils
Requires:	cpp = %{epoch}:%{version}-%{release}
Requires:	libgcc = %{epoch}:%{version}-%{release}
Obsoletes:	gcc4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}
%define		filterout	-fwrapv -fno-strict-aliasing -fsigned-char
# FIXME: unresolved symbols
%define		skip_post_check_so	libmudflap.so.0.0.0 libmudflapth.so.0.0.0

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%package -n cpp
Summary:	C Preprocessor
Group:		Development/Languages

%description -n cpp
Cpp is the GNU C-Compatible Compiler Preprocessor.
Cpp is a macro processor which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define macros, abbreviations for longer
constructs.

%package -n libgcc
Summary:	Shared gcc library
License:	GPL v2+ with unlimited link permission
Group:		Libraries
Obsoletes:	libgcc4

%description -n libgcc
Shared gcc library.

%package -n libgomp
Summary:	GNU OpenMP library
License:	LGPL v2.1+ with unlimited link permission
Group:		Libraries

%description -n libgomp
GNU OpenMP library.

%package -n libgomp-devel
Summary:	Development files for GNU OpenMP library
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp = %{epoch}:%{version}-%{release}

%description -n libgomp-devel
Development files for GNU OpenMP library.

%package -n libgomp-static
Summary:	Static GNU OpenMP library
License:	LGPL v2.1+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgomp-devel = %{epoch}:%{version}-%{release}

%description -n libgomp-static
Static GNU OpenMP library.

%package -n libmudflap
Summary:	GCC mudflap shared support library
License:	GPL v2+ with unlimited link permission
Group:		Libraries

%description -n libmudflap
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations.

%package -n libmudflap-devel
Summary:	Development files for GCC mudflap library
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap = %{epoch}:%{version}-%{release}

%description -n libmudflap-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%package -n libmudflap-multilib-devel
Summary:	Development files for GCC mudflap library
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-multilib-devel
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains development
files.

%package -n libmudflap-static
Summary:	Static GCC mudflap library
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libmudflap-devel = %{epoch}:%{version}-%{release}

%description -n libmudflap-static
The libmudflap libraries are used by GCC for instrumenting pointer and
array dereferencing operations. This package contains static
libraries.

%package c++
Summary:	C++ support for gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	gcc4-c++

%description c++
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%package -n libstdc++
Summary:	GNU C++ library
License:	GPL v2+ with free software exception
Group:		Libraries
# >= instead of = to allow keeping older libstdc++ (with different soname)
Requires:	libgcc >= %{epoch}:%{version}-%{release}
Obsoletes:	libstdc++4

%description -n libstdc++
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%package -n libstdc++-devel
Summary:	Header files and documentation for C++ development
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	glibc-devel
Requires:	libstdc++ = %{epoch}:%{version}-%{release}
Obsoletes:	libstdc++4-devel

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%package -n libstdc++-static
Summary:	Static C++ standard library
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libstdc++4-static

%description -n libstdc++-static
Static C++ standard library.

%package fortran
Summary:	Fortran 95 support for gcc
Group:		Development/Languages/Fortran
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Provides:	gcc-g77 = %{epoch}:%{version}-%{release}
Obsoletes:	gcc-g77

%description fortran
This package adds support for compiling Fortran 95 programs with the
GNU compiler.

%package -n libgfortran
Summary:	Fortran 95 Libraries
License:	GPL v2+ with unlimited link permission
Group:		Libraries
Obsoletes:	libg2c

%description -n libgfortran
Fortran 95 Libraries.

%package -n libgfortran-static
Summary:	Static Fortran 95 Libraries
License:	GPL v2+ with unlimited link permission
Group:		Development/Libraries
Requires:	libgfortran = %{epoch}:%{version}-%{release}
Obsoletes:	libg2c-static

%description -n libgfortran-static
Static Fortran 95 Libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv ChangeLog ChangeLog.general

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

%build
cp -f /usr/share/automake/config.sub .
rm -rf builddir && install -d builddir && cd builddir

CC="%{__cc}"			\
CFLAGS="%{rpmcflags}"		\
CXXFLAGS="%{rpmcxxflags}"	\
TEXCONFIG=false			\
../configure			\
	--%{?with_bootstrap:en}%{!?with_bootstrap:dis}able-bootstrap	\
	--infodir=%{_infodir}						\
	--libdir=%{_libdir}						\
	--libexecdir=%{_libdir}						\
	--mandir=%{_mandir}						\
	--prefix=%{_prefix}						\
	--with-gxx-include-dir=%{_includedir}/c++/%{version}		\
	--with-local-prefix=%{_prefix}/local				\
	--with-slibdir=%{_slibdir}					\
	--x-libraries=%{_libdir}					\
	--disable-cld							\
	--disable-libstdcxx-pch						\
	--disable-multilib						\
	--disable-werror						\
	--enable-__cxa_atexit						\
	--enable-c99							\
	--enable-cmath							\
	--enable-languages="c,c++,fortran"				\
	--enable-libstdcxx-allocator=new				\
	--enable-linux-futex						\
	--enable-long-long						\
	--enable-nls							\
	--enable-shared							\
	--enable-threads=posix						\
	--with-demangler-in-ld						\
	--with-gnu-as							\
	--with-gnu-ld							\
	--with-pkgversion="Freddix"					\
	--with-system-zlib						\
	--without-x							\
	%{_target_platform}
cd ..

%{__make} -C builddir							\
	BOOT_CFLAGS="%{rpmcflags}"					\
	GCJFLAGS="%{rpmcflags}"						\
	GNATLIBCFLAGS="%{rpmcflags}"					\
	LDFLAGS_FOR_TARGET="%{rpmldflags}"				\
	STAGE1_CFLAGS="%{rpmcflags} -O0 -g0"				\
	infodir=%{_infodir}						\
	mandir=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

%{__make} -j1 -C builddir install	\
	DESTDIR=$RPM_BUILD_ROOT		\
	infodir=%{_infodir}		\
	mandir=%{_mandir}

install builddir/gcc/specs $RPM_BUILD_ROOT%{_libdir}/gcc/%{_target_platform}/%{version}

ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp
ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

libssp=$(cd $RPM_BUILD_ROOT%{_libdir}; echo libssp.so.*.*.*)
mv $RPM_BUILD_ROOT{%{_libdir}/$libssp,%{_slibdir}}
libssp=$(cd $RPM_BUILD_ROOT%{_libdir}; echo libssp.so.*)
mv $RPM_BUILD_ROOT{%{_libdir}/$libssp,%{_slibdir}}
ln -sf %{_slibdir}/$libssp $RPM_BUILD_ROOT%{_libdir}/libssp.so

ln -sf gfortran $RPM_BUILD_ROOT%{_bindir}/g95
echo ".so gfortran.1" > $RPM_BUILD_ROOT%{_mandir}/man1/g95.1

# avoid -L poisoning in *.la - there should be only -L%{_libdir}/gcc/*/%{version}
# normalize libdir, to avoid propagation of unnecessary RPATHs by libtool
for f in libgomp.la libmudflap.la libmudflapth.la libssp.la libssp_nonshared.la \
	libstdc++.la libsupc++.la libgfortran.la ;
do
	%{__perl} %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/$f %{_libdir} > $RPM_BUILD_ROOT%{_libdir}/$f.fixed
	mv $RPM_BUILD_ROOT%{_libdir}/$f{.fixed,}
done

gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*)
cp $gccdir/install-tools/include/*.h $gccdir/include
cp $gccdir/include-fixed/syslimits.h $gccdir/include
rm -rf $gccdir/install-tools
rm -rf $gccdir/include-fixed

%find_lang gcc
%find_lang cpplib

%find_lang libstdc\+\+
install libstdc++-v3/include/precompiled/* $RPM_BUILD_ROOT%{_includedir}

# cvs snap doesn't contain (release does) below files,
# so let's create dummy entries to satisfy %%files.
[ ! -f NEWS ] && touch NEWS
[ ! -f libgfortran/AUTHORS ] && touch libgfortran/AUTHORS
[ ! -f libgfortran/README ] && touch libgfortran/README

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n cpp -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n cpp -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post fortran -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun fortran -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-p /sbin/ldconfig -n libgcc
%postun	-p /sbin/ldconfig -n libgcc
%post	-p /sbin/ldconfig -n libgomp
%postun	-p /sbin/ldconfig -n libgomp
%post	-p /sbin/ldconfig -n libmudflap
%postun	-p /sbin/ldconfig -n libmudflap
%post	-p /sbin/ldconfig -n libstdc++
%postun	-p /sbin/ldconfig -n libstdc++
%post	-p /sbin/ldconfig -n libgfortran
%postun	-p /sbin/ldconfig -n libgfortran

%files -f gcc.lang
%defattr(644,root,root,755)
%doc ChangeLog.general MAINTAINERS NEWS
%doc gcc/{ChangeLog,ONEWS,README.Portability}
%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/cc
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gccbug
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2
%attr(755,root,root) %ghost %{_slibdir}/libssp.so.?
%attr(755,root,root) %{_libdir}/libssp.so
%attr(755,root,root) %{_slibdir}/lib*.so

%dir %{_libdir}/gcc/*/*/include
%dir %{_libdir}/gcc/*/*/include/ssp

%{_libdir}/gcc/*/*/crt*.o
%{_libdir}/gcc/*/*/include/ammintrin.h
%{_libdir}/gcc/*/*/include/avxintrin.h
%{_libdir}/gcc/*/*/include/bmmintrin.h
%{_libdir}/gcc/*/*/include/cpuid.h
%{_libdir}/gcc/*/*/include/cross-stdarg.h
%{_libdir}/gcc/*/*/include/emmintrin.h
%{_libdir}/gcc/*/*/include/float.h
%{_libdir}/gcc/*/*/include/immintrin.h
%{_libdir}/gcc/*/*/include/iso646.h
%{_libdir}/gcc/*/*/include/limits.h
%{_libdir}/gcc/*/*/include/mm3dnow.h
%{_libdir}/gcc/*/*/include/mm_malloc.h
%{_libdir}/gcc/*/*/include/mmintrin-common.h
%{_libdir}/gcc/*/*/include/mmintrin.h
%{_libdir}/gcc/*/*/include/nmmintrin.h
%{_libdir}/gcc/*/*/include/omp.h
%{_libdir}/gcc/*/*/include/pmmintrin.h
%{_libdir}/gcc/*/*/include/smmintrin.h
%{_libdir}/gcc/*/*/include/ssp/*.h
%{_libdir}/gcc/*/*/include/stdarg.h
%{_libdir}/gcc/*/*/include/stdbool.h
%{_libdir}/gcc/*/*/include/stddef.h
%{_libdir}/gcc/*/*/include/stdfix.h
%{_libdir}/gcc/*/*/include/syslimits.h
%{_libdir}/gcc/*/*/include/tmmintrin.h
%{_libdir}/gcc/*/*/include/unwind.h
%{_libdir}/gcc/*/*/include/varargs.h
%{_libdir}/gcc/*/*/include/wmmintrin.h
%{_libdir}/gcc/*/*/include/x86intrin.h
%{_libdir}/gcc/*/*/include/xmmintrin.h
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/specs
%{_libdir}/libssp.a
%{_libdir}/libssp.la
%{_libdir}/libssp_nonshared.a
%{_libdir}/libssp_nonshared.la

%{_infodir}/gcc*
%{_mandir}/man1/cc.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*

%files -n cpp -f cpplib.lang
%defattr(644,root,root,755)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/*
%dir %{_libdir}/gcc/*/*
%attr(755,root,root) %{_bindir}/cpp
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) /lib/cpp
%{_mandir}/man1/cpp.1*
%{_infodir}/cpp*

%files -n libgcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/lib*.so.*

%files -n libgomp
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgomp.so.?
%attr(755,root,root) %{_libdir}/libgomp.so.*.*.*

%files -n libgomp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgomp.so
%{_libdir}/libgomp.la
%{_libdir}/libgomp.spec
%{_libdir}/gcc/*/*/finclude
%{_infodir}/libgomp*

%files -n libgomp-static
%defattr(644,root,root,755)
%{_libdir}/libgomp.a

%files -n libmudflap
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libmudflap*.so.?
%attr(755,root,root) %{_libdir}/libmudflap*.so.*.*.*

%files -n libmudflap-devel
%defattr(644,root,root,755)
%{_libdir}/gcc/*/*/include/mf-runtime.h
%{_libdir}/libmudflap*.la
%attr(755,root,root) %{_libdir}/libmudflap*.so

%files -n libmudflap-static
%defattr(644,root,root,755)
%{_libdir}/libmudflap*.a

%files c++
%defattr(644,root,root,755)
%doc gcc/cp/{ChangeLog,NEWS}
%attr(755,root,root) %{_bindir}/g++
%attr(755,root,root) %{_bindir}/*-g++
%attr(755,root,root) %{_bindir}/c++
%attr(755,root,root) %{_bindir}/*-c++
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1plus
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%{_mandir}/man1/g++.1*

%files -n libstdc++ -f libstdc++.lang
%defattr(644,root,root,755)
%doc libstdc++-v3/{ChangeLog,README}
%attr(755,root,root) %ghost %{_libdir}/libstdc++.so.?
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/doc/html
%dir %{_includedir}/c++
%{_includedir}/c++/%{version}
%{_includedir}/extc++.h
%{_includedir}/stdc++.h
%{_includedir}/stdtr1c++.h
%{_libdir}/libstdc++.la
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a

%files fortran
%defattr(644,root,root,755)
%doc gcc/fortran/ChangeLog
%attr(755,root,root) %{_bindir}/g95
%attr(755,root,root) %{_bindir}/gfortran
%attr(755,root,root) %{_bindir}/*-gfortran
%{_infodir}/gfortran*
%attr(755,root,root) %{_libdir}/gcc/*/*/f951
%{_libdir}/gcc/*/*/libgfortranbegin.a
%{_libdir}/gcc/*/*/libgfortranbegin.la
%{_libdir}/libgfortran.la
%attr(755,root,root) %{_libdir}/libgfortran.so
%{_mandir}/man1/g95.1*
%{_mandir}/man1/gfortran.1*

%files -n libgfortran
%defattr(644,root,root,755)
%doc libgfortran/{AUTHORS,README,ChangeLog}
%attr(755,root,root) %ghost %{_libdir}/libgfortran.so.?
%attr(755,root,root) %{_libdir}/libgfortran.so.*.*.*

%files -n libgfortran-static
%defattr(644,root,root,755)
%{_libdir}/libgfortran.a

