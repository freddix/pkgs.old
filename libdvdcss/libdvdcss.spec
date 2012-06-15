Summary:	Library to decrypt CSS-encoded DVD
Name:		libdvdcss
Version:	1.2.12
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.videolan.org/pub/videolan/libdvdcss/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	2218a193900e3203aa10dc24cdf54275
URL:		http://www.videolan.org/libdvdcss/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdcss is a simple library designed for accessing DVDs like a block
device without having to bother about the decryption.

%package devel
Summary:	libdvdcss library headers
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdcss into applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-doc	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/*.h $RPM_BUILD_ROOT%{_includedir}/dvdcss

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/dvdcss
%{_pkgconfigdir}/*.pc

