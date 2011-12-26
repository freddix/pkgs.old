Summary:	Extensible Binary Meta Language access library
Name:		libebml
Version:	1.2.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.bz2
# Source0-md5:	726cc2bd1a525929ff35ff9854c0ebab
Patch0:		%{name}-makefile.patch
URL:		http://www.matroska.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensible Binary Meta Language access library is a library for
reading and writing files with the Extensible Binary Meta Language, a
binary pendant to XML.

%package devel
Summary:	Header files for Extensible Binary Meta Language library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Extensible Binary Meta Language library.

%prep
%setup -q
%undos make/linux/Makefile
%patch0 -p1

%build
%{__make} -C make/linux			\
	prefix=%{_prefix}		\
	libdir=%{_libdir}		\
	CXX="%{__cxx}"			\
	CXXFLAGS="%{rpmcxxflags}"	\
	LD="%{__cxx}"			\
	LDFLAGS="%{rpmldflags}"		\
	DEBUGFLAGS="%{rpmcflags} %{?debug:-DDEBUG}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C make/linux install		\
	DESTDIR=$RPM_BUILD_ROOT		\
	prefix=%{_prefix}		\
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libebml.so.?
%attr(755,root,root) %{_libdir}/libebml.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so
%{_libdir}/libebml.la
%{_includedir}/ebml

