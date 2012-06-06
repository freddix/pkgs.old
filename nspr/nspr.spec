Summary:	Netscape Portable Runtime (NSPR)
Name:		nspr
Version:	4.9.1
Release:	1
Epoch:		1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	d36d7b65a38f5b43ebd50ad3ad227120
Patch0:		%{name}-acfix.patch
URL:		http://www.mozilla.org/projects/nspr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries that implement cross-platform runtime services from
Netscape.

%package devel
Summary:	NSPR library header files for development
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for the NSPR library from Netscape.

%prep
%setup -q
%patch0 -p1

# Win32-specific, requires autoconf2.13
%{__rm} mozilla/nsprpub/build/autoconf/acwinpaths.m4 \
	mozilla/nsprpub/aclocal.m4

%build
cd mozilla/nsprpub

cp -f /usr/share/automake/config.sub build/autoconf
%{__autoconf}
%configure \
	--disable-debug					\
	--enable-ipv6					\
	--enable-optimize="%{rpmcflags}"		\
	--includedir=%{_includedir}/nspr		\
	--with-mozilla					\
	--with-pthreads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} -C mozilla/nsprpub install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s nspr.pc \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nspr.pc

rm $RPM_BUILD_ROOT%{_bindir}/{compile-et.pl,prerr.properties}
rm $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nspr-config
%{_includedir}/nspr
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

