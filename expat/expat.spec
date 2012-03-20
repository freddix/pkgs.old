Summary:	XML 1.0 parser
Name:		expat
Version:	2.0.1
Release:	14
Epoch:		1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://heanet.dl.sourceforge.net/expat/%{name}-%{version}.tar.gz
# Source0-md5:	ee8b492592568805593f81f8cdf2a04c
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-am18.patch
Patch2:		%{name}-soname.patch
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%package devel
Summary:	Expat header files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Expat header files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}
install conftools/expat.m4 $RPM_BUILD_ROOT%{_aclocaldir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libexpat.so.*.*.* libexpat.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%attr(755,root,root) %{_bindir}/xmlwf
%attr(755,root,root) %ghost %{_libdir}/libexpat.so.?
%attr(755,root,root) %{_libdir}/libexpat.so.*.*.*
%{_mandir}/man1/xmlwf.1*

%files devel
%defattr(644,root,root,755)
%doc doc/{reference.html,style.css}
%attr(755,root,root) %{_libdir}/libexpat.so
%{_libdir}/libexpat.la
%{_includedir}/expat*.h
%{_aclocaldir}/expat.m4

