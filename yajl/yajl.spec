Summary:	Yet Another JSON Library
Name:		yajl
Version:	1.0.11
Release:	1
License:	BSD
Group:		Libraries
# http://github.com/lloyd/yajl/tarball/2.0.1
Source:		lloyd-yajl-2.0.1-0-gf4b2b1a.tar.gz
URL:		http://lloyd.github.com/yajl/
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAJL (Yet Another JSON Library) is a JSON parsing library written in
C.

%package devel
Summary:	Header files for YAJL library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for YAJL library.

%prep
%setup -qn lloyd-yajl-f4b2b1a

%build
install -d build
cd build

%cmake ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/json_reformat
%attr(755,root,root) %{_bindir}/json_verify
%attr(755,root,root) %ghost %{_libdir}/libyajl.so.2
%attr(755,root,root) %{_libdir}/libyajl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyajl.so
%{_includedir}/yajl

