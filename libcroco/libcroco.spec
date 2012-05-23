Summary:	A CSS2 parsing library
Name:		libcroco
Version:	0.6.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libcroco/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	d4d6313dd1c347d8a22addb240300338
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS2 parsing and manipulation library for GNOME.

%package devel
Summary:	Header files for developing with libcroco
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package provides the necessary header files files to allow you
to develop with libcroco.

%package apidocs
Summary:	%{name} API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
%{name} API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
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
%attr(755,root,root) %{_bindir}/csslint-0.6
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/usage.txt
%attr(755,root,root) %{_bindir}/croco-*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libcroco-0.6
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

