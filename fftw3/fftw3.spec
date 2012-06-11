Summary:	Fast Fourier Transform library
Name:		fftw3
Version:	3.3.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.fftw.org/pub/fftw/fftw-%{version}.tar.gz
# Source0-md5:	6977ee770ed68c85698c7168ffa6e178
URL:		http://www.fftw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-fortran
BuildRequires:	libtool
BuildRequires:	texinfo
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-O3 -fomit-frame-pointer -malign-double -ffast-math

%description
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the double precision FFTW
uniprocessor and threads libraries.

%package devel
Summary:	Development files for fftw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}

%description devel
This package contains the files you need to develop programs using the
FFTW (fast fourier transform library).

%package single
Summary:	Fast Fourier Transform library - single precision
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description single
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the single precision FFTW
uniprocessor and threads libraries.

%package single-devel
Summary:	Development files for single precision fftw
Group:		Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-single = %{version}-%{release}

%description single-devel
This package contains the files you need to develop programs using the
single precision FFTW (fast fourier transform library).

%package long
Summary:	Fast Fourier Transform library - long double precision
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description long
FFTW is a collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions. It includes complex,
real, and parallel transforms, and can handle arbitrary array sizes
efficiently. This RPM package includes the long double precision FFTW
uniprocessor and threads libraries.

%package long-devel
Summary:	Development files for long double precision fftw
Group:		Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-long = %{version}-%{release}

%description long-devel
This package contains the files you need to develop programs using the
long double precision FFTW (fast fourier transform library).

%package common
Summary:	Files common for all versions of fftw libraries
Group:		Libraries

%description common
Files common for all versions of fftw libraries (basic documentation,
fftw-wisdom-to-conf utility).

%package common-devel
Summary:	Development files common for all versions of fftw libraries
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description common-devel
Development files common for all versions of fftw libraries (header
files, development documentation).

%prep
%setup -qn fftw-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

install -d build-double
cd build-double
../%configure \
	--disable-debug		\
	--disable-static	\
	--enable-openmp		\
	--enable-shared		\
	--enable-sse2		\
	--enable-threads
%{__make}
cd ..

install -d build-single
cd build-single
../%configure \
	--disable-debug		\
	--disable-static	\
	--enable-float		\
	--enable-openmp		\
	--enable-shared		\
	--enable-sse		\
	--enable-threads
%{__make}
cd ..


install -d build-long-double
cd build-long-double
../%configure \
	--disable-debug		\
	--disable-static	\
	--enable-long-double	\
	--enable-openmp		\
	--enable-shared		\
	--enable-threads
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C build-double \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C build-single \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C build-long-double \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	single	-p /sbin/ldconfig
%postun	single	-p /sbin/ldconfig

%post	long	-p /sbin/ldconfig
%postun	long	-p /sbin/ldconfig

%post	common-devel -p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	common-devel -p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftw-wisdom
%attr(755,root,root) %ghost %{_libdir}/libfftw3.so.?
%attr(755,root,root) %ghost %{_libdir}/libfftw3_omp.so.3
%attr(755,root,root) %ghost %{_libdir}/libfftw3_threads.so.?
%attr(755,root,root) %{_libdir}/libfftw3.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3_omp.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3_threads.so.*.*.*
%{_mandir}/man1/fftw-wisdom.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3.so
%attr(755,root,root) %{_libdir}/libfftw3_omp.so
%attr(755,root,root) %{_libdir}/libfftw3_threads.so
%{_pkgconfigdir}/fftw3.pc

%files single
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwf-wisdom
%attr(755,root,root) %ghost %{_libdir}/libfftw3f.so.?
%attr(755,root,root) %ghost %{_libdir}/libfftw3f_omp.so.?
%attr(755,root,root) %ghost %{_libdir}/libfftw3f_threads.so.?
%attr(755,root,root) %{_libdir}/libfftw3f.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3f_omp.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so.*.*.*
%{_mandir}/man1/fftwf-wisdom.1*

%files single-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3f.so
%attr(755,root,root) %{_libdir}/libfftw3f_omp.so
%attr(755,root,root) %{_libdir}/libfftw3f_threads.so
%{_pkgconfigdir}/fftw3f.pc

%files long
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fftwl-wisdom
%attr(755,root,root) %ghost %{_libdir}/libfftw3l.so.?
%attr(755,root,root) %ghost %{_libdir}/libfftw3l_omp.so.?
%attr(755,root,root) %ghost %{_libdir}/libfftw3l_threads.so.?
%attr(755,root,root) %{_libdir}/libfftw3l.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3l_omp.so.*.*.*
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so.*.*.*
%{_mandir}/man1/fftwl-wisdom.1*

%files long-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfftw3l.so
%attr(755,root,root) %{_libdir}/libfftw3l_omp.so
%attr(755,root,root) %{_libdir}/libfftw3l_threads.so
%{_includedir}/fftw3l.f03
%{_pkgconfigdir}/fftw3l.pc

%files common
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/fftw-wisdom-to-conf
%{_mandir}/man1/fftw-wisdom-to-conf.1*

%files common-devel
%defattr(644,root,root,755)
%doc doc/html doc/FAQ/fftw-faq.html
%{_includedir}/fftw3.*
%{_infodir}/fftw3.info*

