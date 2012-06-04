%define		libjpeg_ver	8c

Summary:	A MMX/SSE2 accelerated library for manipulating JPEG image files
Name:		libjpeg-turbo
Version:	1.2.0
Release:	1
License:	wxWidgets
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libjpeg-turbo/%{name}-%{version}.tar.gz
# Source0-md5:	5329fa80953938cb4f097afae55059e2
URL:		http://libjpeg-turbo.virtualgl.org/
Patch0:		%{name}-turbojpeg.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	nasm
Provides:	libjpeg = %{libjpeg_ver}
Obsoletes:	libjpeg >= %{libjpeg_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libjpeg-turbo is a version of libjpeg which uses MMX, SSE, and SSE2
SIMD instructions to accelerate baseline JPEG
compression/decompression by about 2-4x on x86 and x86-64 platforms.
It is based on libjpeg/SIMD but has numerous enhancements.

%package devel
Summary:	Headers for developing programs using libjpeg-turbo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libjpeg-devel = %{libjpeg_ver}
Obsoletes:	libjpeg-devel >= %{libjpeg_ver}

%description devel
The libjpeg-turbo-devel package includes the header files necessary
for developing programs which will manipulate JPEG files using the
libjpeg-turbo library.

%package progs
Summary:	Simple clients for manipulating JPEG images
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libjpeg-progs = %{libjpeg_ver}
Obsoletes:	libjpeg-progs >= %{libjpeg_ver}

%description progs
Simple clients for manipulating JPEG images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared	\
	--with-jpeg8
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log
%attr(755,root,root) %ghost %{_libdir}/libjpeg.so.8
%attr(755,root,root) %ghost %{_libdir}/libturbojpeg.so.?
%attr(755,root,root) %{_libdir}/libjpeg.so.*.*.*
%attr(755,root,root) %{_libdir}/libturbojpeg.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg.so
%attr(755,root,root) %{_libdir}/libturbojpeg.so
%{_libdir}/libjpeg.la
%{_libdir}/libturbojpeg.la
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_includedir}/turbojpeg.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cjpeg
%attr(755,root,root) %{_bindir}/djpeg
%attr(755,root,root) %{_bindir}/jpegtran
%attr(755,root,root) %{_bindir}/rdjpgcom
%attr(755,root,root) %{_bindir}/tjbench
%attr(755,root,root) %{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

