%define		rname		dbus-python
#
Summary:	Python library for using D-BUS
Name:		python-dbus
Version:	1.0.0
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://dbus.freedesktop.org/releases/dbus-python/%{rname}-%{version}.tar.gz
# Source0-md5:	775a8235736bf760cdd96e2d76546469
URL:		http://www.freedesktop.org/Software/dbus
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	dbus-glib-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-Pyrex
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-BUS add-on library to integrate the standard D-BUS library with
Python.

%package devel
Summary:	C API for _dbus_bindings module
License:	AFL v2.1 or LGPL v2.1
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.93
Requires:	python-devel >= 1:2.5

%description devel
Development files for _dbus_bindings module.

%prep
%setup -qn %{rname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pythondir=%{py_sitedir}	\
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT{%{py_sitedir}/*.la,%{_docdir}/dbus-python}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/dbus
%dir %{py_sitedir}/dbus/mainloop
%attr(755,root,root) %{py_sitedir}/_dbus_bindings.so
%attr(755,root,root) %{py_sitedir}/_dbus_glib_bindings.so
%{py_sitedir}/dbus/*.py[co]
%{py_sitedir}/dbus/mainloop/*.py[co]


%files devel
%defattr(644,root,root,755)
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_pkgconfigdir}/dbus-python.pc

