Summary:	Platform-independent, multi-threading and synchronization library for C++
Name:		ZThread
Version:	2.3.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/zthread/%{name}-%{version}.tar.gz
# Source0-md5:	f2782d19b8ed6f1ff2ab8824dd4ba48e
Patch0:		%{name}-c++.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-am.patch
URL:		http://zthread.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ZThread package is an advanced object-oriented, cross-platform,
C++ threading and synchronization library that has been designed and
implemented by the author and released under the MIT license. It
provides a high level abstraction of the native threading mechanisms
to offer a great deal of flexibility and control.

%package devel
Summary:	Header files for ZThread library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ZThread library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I share
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libZThread-2.3.so.?
%attr(755,root,root) %{_libdir}/libZThread-2.3.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,js,css}
%attr(755,root,root) %{_bindir}/zthread-config
%attr(755,root,root) %{_libdir}/libZThread.so
%{_libdir}/libZThread.la
%{_includedir}/zthread
%{_aclocaldir}/pthread.m4
%{_aclocaldir}/zthread.m4

