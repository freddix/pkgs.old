Summary:	LV2 port of MDA plugins
Name:		lv2-plugin-mda
Version:	1.0.0
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://download.drobilla.net/mda-lv2-%{version}.tar.bz2
# Source0-md5:	843ac4eade386034562917e95905e5d8
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDA-LV2 is an LV2 port of the MDA plugins by Paul Kellett.
It contains 36 high-quality plugins for a variety of tasks.

%prep
%setup -qn mda-lv2-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2/mda.lv2
%attr(755,root,root) %{_libdir}/lv2/mda.lv2/*.so
%{_libdir}/lv2/mda.lv2/*.ttl

