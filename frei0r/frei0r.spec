Summary:	Minimalistic plugin API for video effects
Name:		frei0r
Version:	1.3
Release:	2
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.dyne.org/frei0r/releases/%{name}-plugins-%{version}.tar.gz
# Source0-md5:	a2eb63feeeb0c5cf439ccca276cbf70c
BuildRequires:	OpenCV-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gavl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimalistic plugin API for video effects.

%package devel
Summary:	Header files for frei0r library
Group:		Development/Libraries

%description devel
This is the package containing the header files for frei0r library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT	\
	htmldocsdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/frei0r-1
%attr(755,root,root) %{_libdir}/frei0r-1/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_pkgconfigdir}/*pc

