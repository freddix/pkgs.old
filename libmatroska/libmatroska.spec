Summary:	Extensible Binary Meta Language access library
Name:		libmatroska
Version:	1.3.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.matroska.org/downloads/libmatroska/%{name}-%{version}.tar.bz2
# Source0-md5:	f4a8c411f09d39c754eb726efd616043
Patch0:		%{name}-makefile.patch
URL:		http://www.matroska.org/
BuildRequires:	libebml-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska is an extensible open standard Audio/Video container format,
aiming to become the standard of Multimedia Container Formats one day.
It is based on EBML (Extensible Binary Meta Language), a kind of
binary version of XML. This way the significant advantages in terms of
future format extensibility are gained without breaking file support
in old parsers.

%package devel
Summary:	Header files for matroska library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for matroska library.

%prep
%setup -q
%undos make/linux/Makefile
%patch0 -p1

%build
%{__make} -C make/linux				\
	prefix=%{_prefix}			\
	libdir=%{_libdir}			\
	CXX="%{__cxx}"				\
	LD="%{__cxx}"				\
	DEBUGFLAGS="%{rpmcflags} %{?debug:-DDEBUG}" \
	LDFLAGS="%{rpmldflags}"			\
	LIBEBML_INCLUDE_DIR="%{_includedir}/ebml"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C make/linux install 		\
	prefix=$RPM_BUILD_ROOT%{_prefix}	\
	libdir=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libmatroska.so.?
%attr(755,root,root) %{_libdir}/libmatroska.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatroska.so
%{_libdir}/libmatroska.la
%{_includedir}/matroska

