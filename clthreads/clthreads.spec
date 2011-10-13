Summary:	clthreads library
Name:		clthreads
Version:	2.4.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	90b650f1f5c9f39f4d77f73aca3c53be
BuildRequires:	libstdc++-devel
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clthreads library.

%package devel
Summary:	Header files for clthreads library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for clthreads library.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	LDFLAGS="%{rpmldflags}"	\
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %ghost %{_libdir}/libclthreads.so.?
%attr(755,root,root) %{_libdir}/libclthreads.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclthreads.so
%{_includedir}/clthreads.h

