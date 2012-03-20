Summary:	A library for decoding RAW images
Name:		libopenraw
Version:	0.0.9
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	3611d8aea870d25314665ef53093288e
URL:		http://libopenraw.freedesktop.org/
BuildRequires:	boost-devel
BuildRequires:	boost-unit_test_framework-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libopenraw is an ongoing project to provide a free software
implementation for camera RAW files decoding. One of the main reason
is that dcraw is not suited for easy integration into applications,
and there is a need for an easy to use API to build free software
digital image processing application.

%package devel
Summary:	Header files for libopenraw library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf-devel

%description devel
Header files for libopenraw library.

%package -n gtk+-openraw
Summary:	Gtk+ RAW pixbuffer loader
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n gtk+-openraw
Gtk+ RAW pixbuffer loader.

%prep
%setup -q
sed -i -e 's|LDFLAGS|LIBS|g' m4/*

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
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
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/*.so.?
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files -n gtk+-openraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libopenraw_pixbuf.so

