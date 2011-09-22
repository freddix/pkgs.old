Summary:	Library and proxy module for properly loading and sharing PKCS#11 modules
Name:		p11-kit
Version:	0.6
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://p11-glue.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	c1ff3e52f172fda8bf3b426f7fb63c92
URL:		http://p11-glue.freedesktop.org/p11-kit.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
P11-KIT provides a way to load and enumerate PKCS#11 modules. It also
provides a standard configuration setup for installing PKCS#11 modules
in such a way that they-re discoverable.

%package libs
Summary:	Header files for P11-KIT library
Group:		Libraries

%description libs
P11-KIT library.

%package devel
Summary:	Header files for P11-KIT library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for P11-KIT library.

%package apidocs
Summary:	P11-KIT API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for P11-KIT library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/modules

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README p11-kit/pkcs11.conf.example
%attr(755,root,root) %{_bindir}/p11-kit
%attr(755,root,root) %{_libdir}/p11-kit-proxy.so
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libp11-kit.so.?
%attr(755,root,root) %{_libdir}/libp11-kit.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libp11-kit.so
%{_includedir}/p11-kit-1
%{_pkgconfigdir}/p11-kit-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/p11-kit

