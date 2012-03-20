Summary:	OCR
Name:		cuneiform
Version:	1.1.0
Release:	2
License:	BSD-like
Group:		Applications
Source0:	http://launchpad.net/cuneiform-linux/1.1/1.1/+download/%{name}-linux-%{version}.tar.bz2
# Source0-md5:	09fd160cdfc512f26442a7e91246598d
Patch0:		%{name}-link.patch
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cuneiform is an OCR system originally developed and open
sourced by Cognitive technologies.

%package lang-german
Summary:	German language support for %{name}
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description lang-german
German language support for %{name}.

%package lang-polish
Summary:	Polish language support for %{name}
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description lang-polish
Polish language support for %{name}.

%prep
%setup -qn %{name}-linux-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt issues.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%if 0
# TODO
%files lang-german
%defattr(644,root,root,755)

%files lang-polish
%defattr(644,root,root,755)
%endif

