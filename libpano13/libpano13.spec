Summary:	Panorama Tools library
Name:		libpano13
Version:	2.9.18
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/panotools/%{name}-%{version}.tar.gz
# Source0-md5:	9c3a4fce8b6f1d79e395896ce5d8776e
URL:		http://panotools.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Panorama Tools library.

%package devel
Summary:	Header files for Panorama Tools library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Panorama Tools library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-java
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
%doc AUTHORS ChangeLog NEWS README README.linux doc/*.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libpano13.so.?
%attr(755,root,root) %{_libdir}/libpano13.so.*.*.*
%{_mandir}/man1/panoinfo.1.*
%{_mandir}/man1/PTAInterpolate.1.*
%{_mandir}/man1/PTblender.1.*
%{_mandir}/man1/PTcrop.1.*
%{_mandir}/man1/PTinfo.1.*
%{_mandir}/man1/PTmasker.1.*
%{_mandir}/man1/PTmender.1.*
%{_mandir}/man1/PToptimizer.1.*
%{_mandir}/man1/PTroller.1.*
%{_mandir}/man1/PTtiff2psd.1.*
%{_mandir}/man1/PTtiffdump.1.*
%{_mandir}/man1/PTuncrop.1.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpano13.so
%{_includedir}/pano13
%{_pkgconfigdir}/*.pc

