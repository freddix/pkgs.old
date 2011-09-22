Summary:	Nettle - a cryptographic library
Name:		nettle
Version:	2.4
Release:	1
License:	GPL v2+ (parts on LGPL v2.1+)
Group:		Libraries
Source0:	ftp://ftp.lysator.liu.se/pub/security/lsh/%{name}-%{version}.tar.gz
# Source0-md5:	450be8c4886d46c09f49f568ad6fa013
URL:		http://www.lysator.liu.se/~nisse/lsh/
BuildRequires:	ghostscript
BuildRequires:	gmp-devel
BuildRequires:	m4
BuildRequires:	tetex-dvips
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space. Nettle does only one thing, the low-level
crypto stuff, providing simple but general interface to it. In
particular, Nettle doesn't do algorithm selection. It doesn't do
memory allocation. It doesn't do any I/O. All these is up to
application.

%package devel
Summary:	Header files for nettle library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nettle library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/nettle-hash
%attr(755,root,root) %{_bindir}/nettle-lfib-stream
%attr(755,root,root) %{_bindir}/pkcs1-conv
%attr(755,root,root) %{_bindir}/sexp-conv

%attr(755,root,root) %ghost %{_libdir}/libhogweed.so.?
%attr(755,root,root) %ghost %{_libdir}/libnettle.so.?
%attr(755,root,root) %{_libdir}/libhogweed.so.*.*
%attr(755,root,root) %{_libdir}/libnettle.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhogweed.so
%attr(755,root,root) %{_libdir}/libnettle.so
%{_includedir}/nettle
%{_infodir}/nettle.info*
%{_pkgconfigdir}/*.pc

