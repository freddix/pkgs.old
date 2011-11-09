Summary:	Biblioteka operacji na pikselach
Summary:	Pixel manipulation library
Name:		pixman
Version:	0.24.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.gz
# Source0-md5:	a2d0b120509bdccb10aa7f4bec3730e4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pixman is a pixel manipulation library.

%package devel
Summary:	Development files for pixman
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for pixman library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

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
%doc TODO
%attr(755,root,root) %ghost %{_libdir}/libpixman-1.so.?
%attr(755,root,root) %{_libdir}/libpixman-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpixman-1.so
%{_libdir}/libpixman-1.la
%{_includedir}/pixman-1
%{_pkgconfigdir}/pixman-1.pc

