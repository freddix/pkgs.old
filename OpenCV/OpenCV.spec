Summary:	A library of programming functions mainly aimed at real time computer vision
Name:		OpenCV
Version:	2.3.1
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencvlibrary/%{name}-%{version}a.tar.bz2
# Source0-md5:	82e4b6bfa349777233eea09b075e931e
URL:		http://opencv.willowgarage.com
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	jasper-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python
BuildRequires:	zlib-devel
%pyrequires_eq	python-libs
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCV (Open Source Computer Vision) is a library of programming
functions mainly aimed at real time computer vision.

%package libs
Summary:	Opencv library
Group:		Libraries

%description libs
Opencv library.

%package devel
Summary:	Header files and develpment documentation for opencv
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files and opencv documentation.

%package -n python-opencv
Summary:	OpenCV Python bindings
Group:		Development/Languages/Python
%pyrequires_eq  python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description -n python-opencv
OpenCV Python bindings.

%prep
%setup -q

rm -rf 3rdparty/{ilmimf,libjasper,libjpeg,libpng,libtiff,zlib}

find -perm 755 -name "*.cpp" -exec chmod -x  {} ';'
find -perm 755 -name "*.c" -exec chmod -x  {} ';'

%undos samples/c/adaptiveskindetector.cpp

sed -i -e 's/USE_O3 ON/USE_O3 OFF/'		\
    -i -e 's/ENABLE_SSE ON/ENABLE_SSE OFF/'	\
    -i -e 's/ENABLE_SSE2 ON/ENABLE_SSE2 OFF/'	\
    CMakeLists.txt

%build
mkdir build
cd build
%cmake .. \
	-DBUILD_SWIG_PYTHON_SUPPORT=1	\
	-DBUILD_TESTS=0			\
	-DENABLE_OPENMP=1		\
	-DUSE_FAST_MATH=0		\
	-DUSE_O3=0			\
	-DUSE_OMIT_FRAME_POINTER=0	\
	-DWITH_LAPACK=1			\
	-DWITH_V4L=0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/opencv/samples

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/OpenCV
%{_datadir}/OpenCV/haarcascades
%{_datadir}/OpenCV/lbpcascades
%{_datadir}/OpenCV/*.cmake

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?.?
%attr(755,root,root) %{_libdir}/lib*so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/opencv
%{_includedir}/opencv2
%{_pkgconfigdir}/*.pc

%files -n python-opencv
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/cv2.so

