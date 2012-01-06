%define		rname	binutils

Summary:	GNU Binary Utility Development Utilities
Name:		cross_X86_64_binutils
Version:	2.22
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
# Source0-md5:	ee0f10756c84979622b992a4a61ea3f5
Patch0:		%{rname}-libtool-relink.patch
Patch1:		%{rname}-discarded.patch
Patch2:		%{rname}-libtool-m.patch
Patch3:		%{rname}-use-hashtype-both-by-default.patch
Patch4:		%{rname}-tooldir.patch
URL:		http://sources.redhat.com/binutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target	x86_64-freddix-linux
%define		arch	%{_prefix}/%{target}

%define		debug_package	%{nil}

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

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

rm config/override.m4

%build
for dir in gas bfd; do
	cd $dir || exit 1
	%{__aclocal} -I .. -I ../config -I ../bfd
	%{__automake} Makefile
	%{__automake} doc/Makefile
	%{__autoconf}
cd ..
done

cp -f /usr/share/automake/config.* .

CFLAGS="%{rpmcflags}"			\
LDFLAGS="%{rpmldflags}"			\
CONFIG_SHELL="/bin/bash"		\
./configure				\
	--build=%{_target_platform}	\
	--disable-debug			\
	--disable-nls			\
	--disable-shared		\
	--disable-werror		\
	--enable-64-bit-bfd		\
	--host=%{_target_platform}	\
	--infodir=%{_infodir}		\
	--libdir=%{_libdir}		\
	--mandir=%{_mandir}		\
	--prefix=%{_prefix}		\
	--target=%{target}		\
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
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{target}-*
%attr(755,root,root) %{arch}/bin/*
%dir %{arch}
%dir %{arch}/bin
%dir %{arch}/lib
%{arch}/lib/ldscripts
%{_mandir}/man1/%{target}-*.1*

