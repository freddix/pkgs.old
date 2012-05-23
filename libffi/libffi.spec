Summary:	Foreign Function Interface library
Name:		libffi
Version:	3.0.11
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	ftp://sourceware.org/pub/libffi/%{name}-%{version}.tar.gz
# Source0-md5:	f69b9693227d976835b4857b1ba7d0e3
URL:		http://sources.redhat.com/libffi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at
run-time.

Ffi stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
libffi library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above libffi that handles type conversions for values passed
between the two languages.

%package devel
Summary:	libffi development package
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libffi.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog* LICENSE README
%attr(755,root,root) %ghost %{_libdir}/libffi.so.?
%attr(755,root,root) %{_libdir}/libffi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi-%{version}
%{_pkgconfigdir}/libffi.pc
%{_mandir}/man3/ffi*.3*
%{_infodir}/libffi.info*

