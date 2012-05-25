%bcond_with	bootstrap

%include	/usr/lib/rpm/macros.perl

Summary:	Library for automatic proxy configuration management
Name:		libproxy
Version:	0.4.7
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://libproxy.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	509e03a488a61cd62bfbaf3ab6a2a7a5
URL:		http://code.google.com/p/libproxy/
%if !%{with bootstrap}
BuildRequires:	NetworkManager-devel
%endif
BuildRequires:	cmake
BuildRequires:	perl-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modulesdir	%{_libdir}/%{name}/%{version}/modules

%description
Library for automatic proxy configuration management.

%package devel
Summary:	Header files for libproxy library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libproxy library.

%package -n perl-Net-Libproxy
Summary:	libproxy Perl bindings
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Net-Libproxy
libproxy Perl bindings.

%package -n python-libproxy
Summary:	libproxy Python bindings
Group:		Libraries/Python
# uses libproxy shared library
Requires:	%{name} = %{version}-%{release}

%description -n python-libproxy
libproxy Python bindings.

%package networkmanager
Summary:	NetworkManager plugin for libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description networkmanager
NetworkManager configuration plugin for libproxy.

%package gnome3
Summary:	GNOME 3 plugin for libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome3
GNOME configuration plugin for libproxy.

%prep
%setup -q

%build
install -d build
cd build
# webkit off by default, unwanted X11 deps for non-X11 lib
%cmake .. \
	-DLIBEXEC_INSTALL_DIR=%{_libdir}/libproxy	\
	-DLIB_INSTALL_DIR=%{_libdir}			\
	-DPERL_VENDORINSTALL=ON				\
	-DWITH_DOTNET=OFF				\
	-DWITH_MOZJS=OFF				\
	-DWITH_VALA=ON					\
	-DWITH_WEBKIT=OFF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/proxy
%attr(755,root,root) %ghost %{_libdir}/libproxy.so.?
%attr(755,root,root) %{_libdir}/libproxy.so.*.*.*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_libdir}/%{name}/%{version}/modules

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproxy.so
%{_includedir}/*.h
%{_pkgconfigdir}/libproxy-1.0.pc
%{_datadir}/cmake/Modules/Findlibproxy.cmake
%{_datadir}/vala/vapi/libproxy-1.0.vapi

%files -n perl-Net-Libproxy
%defattr(644,root,root,755)
%{perl_vendorarch}/Net/Libproxy.pm
%dir %{perl_vendorarch}/auto/Net/Libproxy
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Libproxy/Libproxy.so

%files -n python-libproxy
%defattr(644,root,root,755)
%{py_sitescriptdir}/libproxy.py[co]

%if !%{with bootstrap}
%files networkmanager
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/network_networkmanager.so

%files gnome3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/config_gnome3.so
%attr(755,root,root) %{_libdir}/%{name}/pxgsettings

%if 0
%files mozjs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/pacrunner_mozjs.so
%endif
%endif

