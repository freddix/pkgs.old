Summary:	Library for parsing EXIF files from digital cameras
Name:		libexif
Version:	0.6.20
Release:	2
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	19844ce6b5d075af16f0d45de1e8a6a3
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package devel
Summary:	Header files for libexif
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libexif.

%package apidocs
Summary:	libexif API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for libexif library.

%prep
%setup -q

rm -f po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4m
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

rm -rf $RPM_BUILD_ROOT%{_docdir}/libexif

%find_lang %{name}-12

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-12.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %ghost %{_libdir}/lib*.so.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%doc doc/doxygen-output/libexif*

