Summary:	VisualOn AAC encoder library
Name:		vo-aacenc
Version:	0.1.1
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	b5724e89d8b33abe41bc57032e671019
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains an encoder implementation of the Advanced Audio
Coding audio codec. The library is based on a codec implementation by
VisualOn as part of the Stagefright framework from the Google Android
project.

%package devel
Summary:	Header files for VisualOn AAC encoder library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VisualOn AAC encoder library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvo-aacenc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS NOTICE README
%attr(755,root,root) %ghost %{_libdir}/libvo-aacenc.so.?
%attr(755,root,root) %{_libdir}/libvo-aacenc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvo-aacenc.so
%{_includedir}/vo-aacenc
%{_pkgconfigdir}/vo-aacenc.pc

