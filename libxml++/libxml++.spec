Summary:	C++ interface for working with XML files
Name:		libxml++
Version:	2.34.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.34/%{name}-%{version}.tar.xz
# Source0-md5:	2ec0bf8f0d8d510a3b28c173a8a4b21c
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mm-common
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%package devel
Summary:	Header files for libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxml++.

%package apidocs
Summary:	libxml++ API documentation
Group:		Documentation

%description apidocs
libxml++ API documentation.

%prep
%setup -q

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT	\
	libdocdir=%{_gtkdocdir}/%{name}-%{apiver}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libxml++-2.6
%{_includedir}/*
%{_pkgconfigdir}/*

%files apidocs
%defattr(644,root,root,755)
%doc %{_gtkdocdir}/%{name}-%{apiver}

