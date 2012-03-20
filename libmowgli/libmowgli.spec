Summary:	Development framework for C (like GLib)
Name:		libmowgli
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.bz2
# Source0-md5:	e5f99410cb7b161f322b6bccd4b05dbe
URL:		http://www.atheme.org/projects/mowgli.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib functions (like list
manipulation), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%package devel
Summary:        Header files for libmowgli
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for libmowgli.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmowgli.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libmowgli.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmowgli.so
%{_includedir}/libmowgli
%{_pkgconfigdir}/libmowgli.pc

