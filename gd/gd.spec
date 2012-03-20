Summary:	Library for PNG, JPEG creation
Name:		gd
Version:	2.0.35
Release:	16
License:	BSD-like
Group:		Libraries
Source0:	http://www.libgd.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	6c6c3dbb7bf079e0bb5fbbfd3bb8a71c
Patch0:		%{name}-fontpath.patch
URL:		http://www.boutell.com/gd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	xorg-libXpm-devel
BuildRequires:	zlib-devel
Provides:	gd(gif) = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gd is the image manipulating library. It was created to allow graphs,
charts and the like to be generated on the fly for use on the World
wide Web, but is useful for any application in which custom images are
useful. It is not a paint program; it is a library. gd library creates
PNG, JPEG, GIF and WBMP images. PNG is a more compact format, and full
compression is available. JPEG works well with photographic images,
and is still more compatible with the major Web browsers than even PNG
is. WBMP is intended for wireless devices (not regular web browsers).

%package devel
Summary:	Development part of the GD library
Group:		Development/Libraries
Provides:	gd-devel(gif) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig(fontconfig)
Requires:	pkgconfig(freetype2)
Requires:	pkgconfig(libpng)
Requires:	pkgconfig(xpm)


%description devel
This package contains the files needed for development of programs
linked against GD.

%package progs
Summary:	Utility programs that use libgd
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
These are utility programs supplied with gd, the image manipulation
library. The libgd-progs package contains a group of scripts for
manipulating the graphics files in formats which are supported by the
libgd library.

%prep
%setup -q
%patch0 -p1

# hack to avoid inclusion of -s in --ldflags
sed -i -e 's,\@LDFLAGS\@,,g' config/gdlib-config.in

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
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
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING index.html
%attr(755,root,root) %ghost %{_libdir}/libgd.so.?
%attr(755,root,root) %{_libdir}/libgd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdlib-config
%attr(755,root,root) %{_libdir}/libgd.so
%{_libdir}/libgd.la
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/gdlib-config

