Summary:	Library for handling different jpeg files
Name:		libjpeg
Version:	8d
Release:	1
License:	distributable
Group:		Libraries
Source0:	http://www.ijg.org/files/jpegsrc.v%{version}.tar.gz
# Source0-md5:	52654eb3b2e60c35731ea8fc87f1bd29
URL:		http://www.ijg.org/
Patch0:		%{name}-maxmem-sysconf.patch
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images.

%package devel
Summary:	Headers for developing programs using libjpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}
Conflicts:	libjpeg6-devel

%description devel
The libjpeg-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpeg library.

If you are going to develop programs which will manipulate JPEG
images, you should install libjpeg-devel. You'll also need to have the
libjpeg package installed.

%package static
Summary:	Static jpeg library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Conflicts:	libjpeg6-static

%description static
Static jpeg library.

%package progs
Summary:	Simple clients for manipulating jpeg images
Group:		Development/Libraries
Requires:	%{name} = %{version}
Conflicts:	libjpeg6-progs

%description progs
Simple clients for manipulating jpeg images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%prep
%setup  -qn jpeg-%{version}
%patch0 -p1

%build
#cp -f %{_datadir}/libtool/config/config.sub .
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--enable-shared		\
	--enable-static
%{__make}

%check
LD_PRELOAD=$PWD/.libs/%{name}.so \
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install jversion.h $RPM_BUILD_ROOT%{_includedir}

# remove HAVE_STD{DEF,LIB}_H
# (not necessary but may generate warnings confusing autoconf)
sed -i -e 's#.*HAVE_STD..._H.*##g' $RPM_BUILD_ROOT%{_includedir}/jconfig.h

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README change.log
%attr(755,root,root) %ghost %{_libdir}/libjpeg.so.8
%attr(755,root,root) %{_libdir}/libjpeg.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg.so
%{_libdir}/libjpeg.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjpeg.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

