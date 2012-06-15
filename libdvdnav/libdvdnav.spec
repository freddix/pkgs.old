Summary:	DVD menu support library
Name:		libdvdnav
Version:	4.2.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	53be8903f9802e101929a3451203bbf6
Patch0:		%{name}-link.patch
URL:		http://dvdnav.mplayerhq.hu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel >= 4.2.0
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD menu support library.

%package devel
Summary:	Development files for libdvdnav
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for libdvdnav.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
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
%doc README ChangeLog
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/dvdnav
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

