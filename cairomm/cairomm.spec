Summary:	C++ wrapper for cairo
Name:		cairomm
Version:	1.10.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	9c63fb1c04c8ecd3c5e6473075b8c39f
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mm-common
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	1.0

%description
C++ wrapper for cairo.

%package devel
Summary:	Development files for cairomm library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for cairomm library.

%package apidocs
Summary:	Cairomm API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Cairomm API documentation.

%prep
%setup -q

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I build
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdocdir=%{_gtkdocdir}/%{name}-%{apiver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libcairomm-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libcairomm-%{apiver}.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairomm-%{apiver}.so
%{_includedir}/cairomm-%{apiver}
%{_libdir}/cairomm-%{apiver}
%{_pkgconfigdir}/cairomm-*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-%{apiver}

