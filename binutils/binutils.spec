Summary:	GNU Binary Utility Development Utilities
Name:		binutils
Version:	2.22
Release:	1
Epoch:		3
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/binutils/%{name}-%{version}.tar.bz2
# Source0-md5:	ee0f10756c84979622b992a4a61ea3f5
Patch0:		%{name}-libtool-relink.patch
Patch1:		%{name}-discarded.patch
Patch2:		%{name}-libtool-m.patch
Patch3:		%{name}-use-hashtype-both-by-default.patch
Patch4:		%{name}-tooldir.patch
URL:		http://sources.redhat.com/binutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binutils is a collection of binary utilities, including:
- ar - create, modify and extract from archives,
- nm - lists symbols from object files,
- objcopy - copy and translate object files,
- objdump - display information from object files,
- ranlib - generate an index for the contents of an archive,
- size - list the section sizes of an object or archive file,
- strings - list printable strings from files,
- strip - discard symbols,
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

%package libs
Summary:	GNU binutils shared libraries (libbfd, libopcodes).
Group:		Libraries

%description libs
GNU binutils shared libraries (libbfd, libopcodes).

%package devel
Summary:	Development files for GNU binutils libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Development files for GNU binutils libraries.

%package static
Summary:	GNU binutils static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNU binutils static libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

#rm config/override.m4

%build
cp -f /usr/share/automake/config.* .

CFLAGS="%{rpmcflags}"; export CFLAGS
CC="%{__cc}"; export CC

./configure %{_target_platform} 				\
	--disable-debug						\
	--disable-werror					\
	--enable-build-warnings=,-Wno-missing-prototypes	\
	--enable-shared						\
	--enable-targets=i686-linux				\
	--infodir=%{_infodir}					\
	--libdir=%{_libdir}					\
	--mandir=%{_mandir}					\
	--prefix=%{_prefix}					\
	--with-tooldir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/standards.info*

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{dlltool,nlmconv,windres}.1

install include/libiberty.h $RPM_BUILD_ROOT%{_includedir}
install libiberty/pic/libiberty.a $RPM_BUILD_ROOT%{_libdir}

# remove evil -L pointing inside builder's home
perl -pi -e 's@-L[^ ]*/pic @@g' $RPM_BUILD_ROOT%{_libdir}/libbfd.la

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang bfd
%find_lang binutils
%find_lang gas
%find_lang gprof
touch ld.lang
%find_lang ld
%find_lang opcodes
cat bfd.lang opcodes.lang > %{name}-libs.lang
cat gas.lang gprof.lang ld.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/[!g]*
%attr(755,root,root) %{_bindir}/g[!a]*
#%{_prefix}/lib/ldscripts

%{_mandir}/man1/*

%{_infodir}/as.info*
%{_infodir}/binutils.info*
%{_infodir}/configure.info*
%{_infodir}/gprof.info*
%{_infodir}/ld.info*

%files libs -f %{name}-libs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfd-*.so
%attr(755,root,root) %{_libdir}/libopcodes-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbfd.so
%attr(755,root,root) %{_libdir}/libopcodes.so
%{_libdir}/libbfd.la
%{_libdir}/libopcodes.la
%{_libdir}/libiberty.a
%{_includedir}/*.h
%{_infodir}/bfd.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbfd.a
%{_libdir}/libopcodes.a

