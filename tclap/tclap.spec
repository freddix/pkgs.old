Summary:	Templatized C++ Command Line Parser Library
Name:		tclap
Version:	1.2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tclap/%{name}-%{version}.tar.gz
# Source0-md5:	eb0521d029bf3b1cc0dcaa7e42abf82a
URL:		http://zthread.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TCLAP is a small, flexible library that provides a simple interface
for defining and accessing command line arguments. It was intially
inspired by the user friendly CLAP libary. The difference is that this
library is templatized, so the argument class is type independent.
Type independence avoids identical-except-for-type objects, such as
IntArg, FloatArg, and StringArg. While the library is not strictly
compliant with the GNU or POSIX standards, it is close.

This package contains header files for TCLAP library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/tclap
%{_pkgconfigdir}/*.pc

