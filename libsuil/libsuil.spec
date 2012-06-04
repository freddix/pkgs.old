Summary:	Lightweight C library for loading and wrapping LV2 plugin UIs
Name:		libsuil
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/suil-%{version}.tar.bz2
# Source0-md5:	062f1166786cf59a28b3b9bfbda6f15c
BuildRequires:	QtGui-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight C library for loading and wrapping LV2 plugin UIs.

%package devel
Summary:	Header files for suil library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for suil library.

%package gui-support
Summary:	GUI support
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gui-support
Suil currently supports Gtk+ and Qt, i.e. with Suil a Gtk program can
embed a Qt plugin UI without depending on Qt, and a Qt program can
embed a Gtk+ plugin UI without depending on Gtk+.

%prep
%setup -qn suil-%{version}

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
%attr(755,root,root) %ghost %{_libdir}/libsuil-0.so.?
%attr(755,root,root) %{_libdir}/libsuil-0.so.*.*.*

%files gui-support
%defattr(644,root,root,755)
%dir %{_libdir}/suil-0
%attr(755,root,root) %{_libdir}/suil-0/libsuil_gtk2_in_qt4.so
%attr(755,root,root) %{_libdir}/suil-0/libsuil_qt4_in_gtk2.so
%attr(755,root,root) %{_libdir}/suil-0/libsuil_x11_in_gtk2.so
%attr(755,root,root) %{_libdir}/suil-0/libsuil_x11_in_qt4.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsuil-0.so
%{_includedir}/suil-0
%{_pkgconfigdir}/suil-0.pc

