Summary:	Image processing and analysis library
Name:		leptonica
Version:	1.68
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	http://leptonica.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	5cd7092f9ff2ca7e3f3e73bfcd556403
Patch0:		%{name}-zlib-include.patch
URL:		http://www.leptonica.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An open source C library for efficient image processing and image
analysis operations

%package devel
Summary:	Header files for leptonica library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for leptonica library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc README.html leptonica-license.txt version-notes.html moller52.jpg
%attr(755,root,root) %ghost %{_libdir}/liblept.so.?
%attr(755,root,root) %{_libdir}/liblept.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblept.so
%{_libdir}/liblept.la
%{_includedir}/leptonica

