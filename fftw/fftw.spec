Summary:	Fast Fourier Transform library
Name:		fftw
Version:	2.1.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.fftw.org/pub/fftw/%{name}-%{version}.tar.gz
# Source0-md5:	8d16a84f3ca02a785ef9eb36249ba433
Patch0:		%{name}-link.patch
URL:		http://www.fftw.org/
BuildRequires:	autoconf
BuildRequires:	automake
# to detect proper F77 name mangling for fortran binding functions
BuildRequires:	gcc-g77
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the single and double precision
FFTW uniprocessor and threads libraries.

%package devel
Summary:	Header files and development documentation for FFTW library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the additional header files and documentation
you need to develop programs using the FFTW (fast Fourier transform
library).

%package single
Summary:	Single-precision Fast Fourier Transform libraries
Group:		Libraries

%description single
Single-precision Fast Fourier Transform libraries.

%package single-devel
Summary:	Header files for single-precision FFTW libraries
Group:		Development/Libraries
Requires:	%{name}-single = %{version}-%{release}

%description single-devel
Header files for single-precision FFTW libraries.

%prep
%setup -q
%patch0 -p1

# don't use pregenerated file
rm -f fftw/config.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

install -d build-single
cd build-single
../%configure \
	--disable-debug		\
	--disable-static	\
	--enable-float		\
	--enable-i386-hacks	\
	--enable-shared		\
	--enable-threads	\
	--enable-type-prefix
%{__make}
cd ..

install -d build-double
cd build-double
../%configure \
	--disable-debug		\
	--disable-static	\
	--enable-i386-hacks	\
	--enable-shared		\
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-single install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C build-double install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	single -p /sbin/ldconfig
%postun	single -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libfftw.so.?
%attr(755,root,root) %ghost %{_libdir}/libfftw_threads.so.?
%attr(755,root,root) %ghost %{_libdir}/librfftw.so.?
%attr(755,root,root) %ghost %{_libdir}/librfftw_threads.so.?
%attr(755,root,root) %{_libdir}/libfftw.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw_threads.so.*.*.*
%attr(755,root,root) %{_libdir}/librfftw.so.*.*.*
%attr(755,root,root) %{_libdir}/librfftw_threads.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw.so
%attr(755,root,root) %{_libdir}/libfftw_threads.so
%attr(755,root,root) %{_libdir}/librfftw.so
%attr(755,root,root) %{_libdir}/librfftw_threads.so
%{_includedir}/fftw*.h
%{_includedir}/rfftw*.h
%{_infodir}/fftw.info*

%files single
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsfftw.so.?
%attr(755,root,root) %ghost %{_libdir}/libsfftw_threads.so.?
%attr(755,root,root) %ghost %{_libdir}/libsrfftw.so.?
%attr(755,root,root) %ghost %{_libdir}/libsrfftw_threads.so.?
%attr(755,root,root) %{_libdir}/libsfftw.so.*.*.*
%attr(755,root,root) %{_libdir}/libsfftw_threads.so.*.*.*
%attr(755,root,root) %{_libdir}/libsrfftw.so.*.*.*
%attr(755,root,root) %{_libdir}/libsrfftw_threads.so.*.*.*

%files single-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsfftw.so
%attr(755,root,root) %{_libdir}/libsfftw_threads.so
%attr(755,root,root) %{_libdir}/libsrfftw.so
%attr(755,root,root) %{_libdir}/libsrfftw_threads.so
%{_includedir}/sfftw*.h
%{_includedir}/srfftw*.h

