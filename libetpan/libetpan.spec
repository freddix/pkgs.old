Summary:	Portable mail access library
Name:		libetpan
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libetpan/%{name}-%{version}.tar.gz
# Source0-md5:	5addc766141a0b1d29ee1ca4ba1b6808
URL:		http://sourceforge.net/projects/libetpan/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	libsasl2-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this mail library is to provide a portable, efficient
middleware for different kinds of mail access. It will be used for
low-level mail handling: network protocols (IMAP/NNTP/POP3/SMTP over
TCP/IP and SSL/TCP/IP, already implemented), local storage
(mbox/MH/maildir), message / MIME parser.

%package devel
Summary:	Header files for libEtPan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libEtPan library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %ghost %{_libdir}/libetpan.so.??
%attr(755,root,root) %{_libdir}/libetpan.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/API/*.htm
%attr(755,root,root) %{_bindir}/libetpan-config
%attr(755,root,root) %{_libdir}/libetpan.so
%{_libdir}/libetpan.la
%{_includedir}/libetpan
%{_includedir}/*.h

