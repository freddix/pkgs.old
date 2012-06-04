Summary:	Library for serialising LV2 atoms to/from RDF
Name:		libsratom
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/sratom-%{version}.tar.bz2
# Source0-md5:	c03cf2849186818610ffe889be4f5b55
BuildRequires:	libserd-devel >= 0.14.0
BuildRequires:	libsord-devel >= 0.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sratom is a library for serialising LV2 atoms to/from RDF,
particularly the Turtle syntax.

%package devel
Summary:	Header files for sratom library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for sratom library.

%prep
%setup -qn sratom-%{version}

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
%doc README
%attr(755,root,root) %ghost %{_libdir}/libsratom-0.so.?
%attr(755,root,root) %{_libdir}/libsratom-0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsratom-0.so
%{_includedir}/sratom-0
%{_pkgconfigdir}/sratom-0.pc

