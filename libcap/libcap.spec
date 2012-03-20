Summary:	POSIX.1e capability suite
Name:		libcap
Version:	2.21
Release:	2
Epoch:		1
License:	GPL or BSD
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.gz
# Source0-md5:	61966ef40f2dee8731b69db895e4548d
Patch0:		%{name}-make.patch
URL:		http://sites.google.com/site/fullycapable/
BuildRequires:	attr-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
The POSIX.1e capability library for Linux. This package contains the
getcap and setcap binaries and manual pages.

%package devel
Summary:	Header files and development documentation for libcap
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for libcap.

%package -n pam-pam_cap
Summary:	Capability module for PAM
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	pam

%description -n pam-pam_cap
PAM capability module enforces inheritable capability sets.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"			\
	DEBUG=				\
	LDLIBS="-L../libcap -lcap"	\
	OPT_CFLAGS="-Iinclude %{rpmcflags} %{rpmcppflags}" \
	OPT_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	RAISE_SETFCAP=no		\
	FAKEROOT=$RPM_BUILD_ROOT	\
	lib=%{_lib}

install -d $RPM_BUILD_ROOT/%{_lib}/security
install -p pam_cap/pam_cap.so $RPM_BUILD_ROOT/%{_lib}/security
install -d $RPM_BUILD_ROOT/etc/security
cp -a pam_cap/capability.conf $RPM_BUILD_ROOT/etc/security

install -d $RPM_BUILD_ROOT%{_libdir}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libcap.so.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libcap.so
%{__rm} $RPM_BUILD_ROOT/%{_lib}/libcap.so
%{__rm} $RPM_BUILD_ROOT/%{_lib}/libcap.a

chmod a+x $RPM_BUILD_ROOT/%{_lib}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG License README
%attr(755,root,root) /%{_lib}/libcap.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libcap.so.2

%attr(755,root,root) %{_sbindir}/capsh
%attr(755,root,root) %{_sbindir}/getcap
%attr(755,root,root) %{_sbindir}/getpcaps
%attr(755,root,root) %{_sbindir}/setcap
%{_mandir}/man1/capsh.1*
%{_mandir}/man8/getcap.8*
%{_mandir}/man8/setcap.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcap.so
%{_includedir}/sys/capability.h
%{_mandir}/man3/libcap*.3*
%{_mandir}/man3/cap_*
%{_mandir}/man3/capgetp.3*
%{_mandir}/man3/capsetp.3*

%files -n pam-pam_cap
%defattr(644,root,root,755)
%doc pam_cap/License
%attr(755,root,root) /%{_lib}/security/pam_cap.so
%config(noreplace) %verify(not md5 mtime size) /etc/security/capability.conf

