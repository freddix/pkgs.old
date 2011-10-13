Summary:	clxclient library
Name:		clxclient
Version:	3.6.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	bd47f80a855d3203fcf10365e79d85e4
Patch0:		%{name}-make.patch
BuildRequires:	clthreads-devel
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrapper library around the X Window System API.

%package devel
Summary:	Header files for clxclient library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for clxclient library.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX=%{__cxx}			\
	LIBDIR=%{_libdir}		\
	OPTFLAGS="%{rpmcflags}"		\
	OPTLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR=%{_libdir}		\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %ghost %{_libdir}/libclxclient.so.?
%attr(755,root,root) %{_libdir}/libclxclient.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclxclient.so
%{_includedir}/clxclient.h

