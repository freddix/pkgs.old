%define		pname	confuse

Summary:	Library for parsing configuration files
Name:		libconfuse
Version:	2.7
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/confuse/%{pname}-%{version}.tar.gz
# Source0-md5:	45932fdeeccbb9ef4228f1c1a25e9c8f
URL:		http://www.nongnu.org/confuse/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libConfuse is a configuration file parser library written in C. It
supports sections and (lists of) values (strings, integers, floats,
booleans or other sections), as well as some other features (such as
single/double-quoted strings, environment variable expansion,
functions and nested include statements).

%package devel
Summary:	Header files for libConfuse library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for libConfuse library.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -DYY_NO_INPUT"
%configure \
	--disable-static \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man3,%{_pkgconfigdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

%find_lang %{pname}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{pname}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libconfuse.so.0
%attr(755,root,root) %{_libdir}/libconfuse.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html doc/tutorial-html
%attr(755,root,root) %{_libdir}/libconfuse.so
%{_libdir}/libconfuse.la
%{_includedir}/confuse.h
%{_pkgconfigdir}/libconfuse.pc
%{_mandir}/man3/cfg_*.3*
%{_mandir}/man3/confuse.h.3*

