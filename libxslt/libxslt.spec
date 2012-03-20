Summary:	XSLT processor
Name:		libxslt
Version:	1.1.26
Release:	3
License:	MIT
Group:		Libraries
Source0:	ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
# Source0-md5:	e61d0364a30146aaa3001296f853b2b9
URL:		http://xmlsoft.org/XSLT/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-libxml2
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for XSLT processing.

%package devel
Summary:	Header files for libxslt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxslt - XSLT processor.

%package progs
Summary:	XSLT processor
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description progs
XSLT processor.

%package -n python-%{name}
Summary:	Python support for libxslt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libxml2
%pyrequires_eq	python-modules

%description -n python-%{name}
Python support for libxslt.

%prep
%setup -q

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

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-python-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{py,la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright FEATURES NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libexslt.so.?
%attr(755,root,root) %ghost %{_libdir}/libxslt.so.?
%attr(755,root,root) %{_libdir}/libexslt.so.*.*.*
%attr(755,root,root) %{_libdir}/libxslt.so.*.*.*
%dir %{_libdir}/libxslt-plugins

%files devel
%defattr(644,root,root,755)
%doc doc/{*.{gif,html},html}
%attr(755,root,root) %{_bindir}/xslt-config
%attr(755,root,root) %{_libdir}/libexslt.so
%attr(755,root,root) %{_libdir}/libxslt.so
%attr(755,root,root) %{_libdir}/xsltConf.sh
%{_includedir}/libexslt
%{_includedir}/libxslt
%{_mandir}/man3/libexslt.3*
%{_mandir}/man3/libxslt.3*
%{_aclocaldir}/libxslt.m4
%{_pkgconfigdir}/libexslt.pc
%{_pkgconfigdir}/libxslt.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsltproc
%{_mandir}/man1/*

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/libxsltmod.so
%{py_sitedir}/libxslt.py[co]

