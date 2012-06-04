Summary:	Lightweight C library for storing RDF data in memory
Name:		libsord
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/sord-%{version}.tar.bz2
# Source0-md5:	62be6a2cd6e9bc2933d1297afeacda30
BuildRequires:	glib-devel
BuildRequires:	libserd-devel >= 0.14.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight C library for storing RDF data in memory.

%package devel
Summary:	Header files for sord library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for serd library.

%prep
%setup -qn sord-%{version}

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
%attr(755,root,root) %{_bindir}/sord_validate
%attr(755,root,root) %{_bindir}/sordi
%attr(755,root,root) %ghost %{_libdir}/libsord-0.so.?
%attr(755,root,root) %{_libdir}/libsord-0.so.*.*.*
%{_mandir}/man1/sordi.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsord-0.so
%{_includedir}/sord-0
%{_pkgconfigdir}/sord-0.pc

