Summary:	pthread library helper
Name:		libpthread-stubs
Version:	0.3
Release:	2
License:	MIT
Group:		Development/Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	e8fa31b42e13f87e8f5a7a2b731db7ee
URL:		http://xcb.freedesktop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
This library provides weak aliases for pthread functions not provided
in libc or otherwise available by default. Libraries like libxcb rely
on pthread stubs to use pthreads optionally, becoming thread-safe when
linked to libpthread, while avoiding any performance hit when running
single-threaded. libpthread-stubs supports this behavior even on
platforms which do not supply all the necessary pthread stubs. On
platforms which already supply all the necessary pthread stubs, this
package ships only the pkg-config file pthread-stubs.pc, to allow
libraries to unconditionally express a dependency on pthread-stubs and
still obtain correct behavior.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install		\
	DESTDIR=$RPM_BUILD_ROOT	\
	pkgconfigdir=%{_datadir}/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/pkgconfig/*.pc

