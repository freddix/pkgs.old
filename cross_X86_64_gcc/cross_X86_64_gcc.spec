%bcond_without	bootstrap
#
Summary:	Cross GNU Compiler Collection for the x86_64 architecture
Name:		cross_X86_64_gcc
Version:	4.4.6
Release:	2
License:	GPL v3+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	ab525d429ee4425050a554bc9247d6c4
Source1:	gcc-optimize-la.pl
Patch1:		gcc-nodebug.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cross_X86_64_binutils
%if !%{with bootstrap}
BuildRequires:	cross_X86_64_gcc
%endif
BuildRequires:	bison
BuildRequires:	chrpath
BuildRequires:	fileutils
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel
BuildRequires:	gmp-devel
BuildRequires:	libmpc-devel
BuildRequires:	mpfr-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	cross_X86_64_binutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}

%define         target          x86_64-freddix-linux
%define         arch            %{_prefix}/%{target}
%define         gccarch         %{_libdir}/gcc/%{target}
%define         gcclib          %{gccarch}/%{version}

%define         _noautostrip    .*/lib.*\\.a

%define		debug_package	%{nil}

%description
Cross GNU Compiler Collection for the x86_64 architecture.

%prep
%setup -qn gcc-%{version}
%patch1 -p1

%build
cp -f %{_datadir}/automake/config.* .
rm -rf obj-%{target}
install -d obj-%{target}
cd obj-%{target}

TEXCONFIG=false				\
../configure				\
	--bindir=%{_bindir}		\
	--infodir=%{_infodir} 		\
	--libdir=%{_libdir}		\
	--libexecdir=%{_libexecdir}	\
	--mandir=%{_mandir}		\
	--prefix=%{_prefix}		\
	--target=%{target}		\
	--disable-nls			\
%if %{with bootstrap}
	--disable-decimal-float         \
	--disable-multilib              \
	--disable-nls                   \
	--disable-shared                \
	--enable-languages=c            \
	--enable-threads=single         \
%else
	--disable-cld			\
	--disable-libstdcxx-pch		\
	--disable-multilib		\
	--enable-__cxa_atexit		\
	--enable-c99			\
	--enable-languages=c,c++	\
	--enable-libstdcxx-allocator=new	\
	--enable-linux-futex		\
	--enable-long-long		\
	--enable-shared			\
	--with-demangler-in-ld		\
	--without-system-libunwind
%endif
	--without-headers
cd ..

%{__make} -C obj-%{target} all-gcc all-target-libgcc \
	CFLAGS_FOR_TARGET="-O2"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

%{__make} -C obj-%{target} -j1 install-gcc install-target-libgcc \
	DESTDIR=$RPM_BUILD_ROOT

install obj-%{target}/gcc/specs $RPM_BUILD_ROOT%{gcclib}
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

gccdir=$RPM_BUILD_ROOT%{gcclib}
mv $gccdir/include-fixed/{limits,syslimits}.h $gccdir/include
rm -r $gccdir/include-fixed
rm -r $gccdir/install-tools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{gccarch}
%dir %{gcclib}
%dir %{gcclib}/include
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcc*
%attr(755,root,root) %{_bindir}/%{target}-gcov
%attr(755,root,root) %{gcclib}/*.a
%attr(755,root,root) %{gcclib}/*.o
%attr(755,root,root) %{gcclib}/cc1
%attr(755,root,root) %{gcclib}/collect2
%if !%{with bootstrap}
%attr(755,root,root) %{_bindir}/%{target}-c++
%attr(755,root,root) %{_bindir}/%{target}-g++
%attr(755,root,root) %{gcclib}/cc1plus
%endif
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*
%{gcclib}/include/*.h
%{gcclib}/specs*

