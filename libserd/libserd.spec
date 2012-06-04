Summary:	Lightweight C library for RDF syntax
Name:		libserd
Version:	0.14.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/serd-%{version}.tar.bz2
# Source0-md5:	405b11ee92f3f19ce4a757ba34953886
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight C library for RDF syntax.

%package devel
Summary:	Header files for serd library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for serd library.

%prep
%setup -qn serd-%{version}

sed -i "s|bld.add_post_fun(autowaf.run_ldconfig)||" wscript

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure --nocache --prefix=%{_prefix} --mandir=%{_mandir}
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

# great waf build system
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/serdi
%attr(755,root,root) %ghost %{_libdir}/libserd-0.so.?
%attr(755,root,root) %{_libdir}/libserd-0.so.*.*.*
%{_mandir}/man1/serdi.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libserd-0.so
%{_includedir}/serd-0
%{_pkgconfigdir}/serd-0.pc

