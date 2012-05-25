Summary:	ISO MPEG-4 compliant video codec
Name:		xvidcore
Version:	1.3.2
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://downloads.xvid.org/downloads/xvidcore-%{version}.tar.bz2
# Source0-md5:	34389e980d4f849688f8b1e168f4e2f9
URL:		http://www.xvid.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	yasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO MPEG-4 compliant video codec. You can play OpenDivX and DivX4
videos with it, too.

%package devel
Summary:	Development files of XviD video codec
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xvidcore-devel = %{epoch}:%{version}-%{release}

%description devel
Development files of XviD video codec.

%prep
%setup -qn %{name}

%build
cd build/generic
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} -C build/generic install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libxvidcore.so.*.* libxvidcore.so
/sbin/ldconfig -n .

chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

