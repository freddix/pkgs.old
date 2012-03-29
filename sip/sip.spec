Summary:	Python bindings generator for C++ class libraries
Name:		sip
Version:	4.12.4
Release:	1
Epoch:		2
License:	redistributable (see LICENSE)
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/sip4/%{name}-%{version}.tar.gz
# Source0-md5:	6cbd56abb7d35aad833789c98ae61652
URL:		http://www.riverbankcomputing.co.uk/sip/index.php
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
Generates Python bindings for C++ class libraries from a set of class
specification files.

%package -n python-sip
Summary:	Python module needed by generated bindings
Group:		Libraries/Python
%pyrequires_eq	python-libs

%description -n python-sip
Generates Python bindings for C++ class libraries from a set of class
specification files. This package includes runtime library needed by
all generated bindings.

%package -n python-sip-devel
Summary:	Development files needed to build bindings
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-devel
%pyrequires_eq	python-libs

%description -n python-sip-devel
Development files needed to build bindings for C++ classes.

%prep
%setup -q

%build
# configure.py notes:
# - macros overrides must be last
# - cannot pass CXXFLAGS+="%{rpmcflags}" or so - builtin -O2 overrides rpmcflags
python configure.py 			\
	-b %{_bindir}			\
	-e %{py_incdir}			\
	-v %{_sipfilesdir}		\
	-d %{py_sitedir}		\
	CC="%{__cc}"			\
	CXX="%{__cxx}"			\
	CFLAGS="%{rpmcflags}"		\
	CXXFLAGS="%{rpmcxxflags}"	\
	LINK="%{__cxx}"			\
	LINK_SHLIB="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sipfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS doc/*
%attr(755,root,root) %{_bindir}/*

%files -n python-sip
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/sip.so

%files -n python-sip-devel
%defattr(644,root,root,755)
%{py_sitedir}/sip*.py
%{py_incdir}/*.h
%dir %{_sipfilesdir}

