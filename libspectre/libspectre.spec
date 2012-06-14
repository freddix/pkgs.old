Summary:	A library for rendering PostScript documents
Name:		libspectre
Version:	0.2.6
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	5c6db35f2097c3a04c48c7f435d4b507
URL:		http://libspectre.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ghostscript-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small library for rendering PostScript documents. It provides a
convenient easy to use API for handling and rendering PostScript
documents.

%package devel
Summary:	Header files for libspectre library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghostscript-devel

%description devel
Header files for libspectre library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-test
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libspectre.so.?
%attr(755,root,root) %{_libdir}/libspectre.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspectre.so
%{_includedir}/libspectre
%{_pkgconfigdir}/libspectre.pc

