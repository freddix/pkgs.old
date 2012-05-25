Summary:	Library for compression and decompression
Name:		zlib
Version:	1.2.6
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.zlib.net/%{name}-%{version}.tar.gz
# Source0-md5:	618e944d7c7cd6521551e30b32322f4a
URL:		http://www.zlib.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

%package devel
Summary:	Header files and libraries for zlib development
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these zlib.

%package static
Summary:	Static zlib libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static zlib libraries.

%prep
%setup -q
cp contrib/asm686/match.S .

%build
CFLAGS="-D_REENTRANT -fPIC %{rpmcflags} -DASMV" \
CC="%{__cc}"			\
./configure			\
	--prefix=%{_prefix}	\
	--libdir=%{_libdir}	\
	--sharedlibdir=%{_libdir}

%{__make} \
	OBJA=match.o	\
	PIC_OBJA=match.lo

%check
%{__make} -j1 test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_includedir},%{_libdir},%{_mandir}/man3}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install libz.a $RPM_BUILD_ROOT%{_libdir}
install zutil.h $RPM_BUILD_ROOT%{_includedir}

mv -f $RPM_BUILD_ROOT%{_libdir}/libz.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib} && echo libz.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libz.so

grep -A 24 '^  Copyright' zlib.h > LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ LICENSE README doc/algorithm.txt
%attr(755,root,root) %ghost /%{_lib}/libz.so.?
%attr(755,root,root) /%{_lib}/libz.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libz.so
%{_includedir}/*.h
%{_pkgconfigdir}/zlib.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

