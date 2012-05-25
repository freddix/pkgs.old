Summary:	Raptor RDF Parser Toolkit
Name:		raptor
Version:	1.4.21
Release:	1
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group:		Libraries
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	992061488af7a9e2d933df6b694bb876
Patch0:		%{name}-curl.patch
URL:		http://librdf.org/raptor/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	openldap-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raptor is the RDF Parser Toolkit for Redland written in C consisting
of two parsers for the RDF/XML and N-Triples syntaxes for RDF. Raptor
is designed to work efficiently when used with Redland but is entirely
separate.

%package devel
Summary:	libraptor library header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libraptor library header files.

%package apidocs
Summary:	Raptor API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Raptor API documentation.

%package rapper
Summary:	Raptor RDF parser test program
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description rapper
Raptor RDF parser test program.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# avoid -s in LDFLAGS, `raptor-config --libs` would print it
# (note: don't pass empty LDFLAGS - it would be overridden)
LDFLAGS="`echo %{rpmldflags} | sed -e 's/\(^\| \)-s\>/ /'`"
# avoid using parsedate from libinn, use curl_getdate instead
%configure \
	ac_cv_header_libinn_h=no	\
	--enable-release		\
	--disable-static		\
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
%doc AUTHORS ChangeLog LICENSE.txt NEWS README
%attr(755,root,root) %ghost %{_libdir}/libraptor.so.?
%attr(755,root,root) %{_libdir}/libraptor.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/raptor-config
%attr(755,root,root) %{_libdir}/libraptor.so
%{_libdir}/libraptor.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/raptor-config.1*
%{_mandir}/man3/*

%files rapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rapper
%{_mandir}/man1/rapper.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

