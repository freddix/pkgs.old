Summary:	Zita convolver library
Name:		zita-convolver
Version:	3.0.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	55d7b186c0fe15877cb33e2288533255
BuildRequires:	fftw3-single-devel
BuildRequires:	libstdc++-devel
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zita convolver library.

%package devel
Summary:	Header files for zita-convolver library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for
zita-convolver library.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C libs \
	CXX="%{__cxx}"		\
	OPTFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C libs install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libzita-convolver.so.?
%attr(755,root,root) %{_libdir}/libzita-convolver.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzita-convolver.so
%{_includedir}/*.h

