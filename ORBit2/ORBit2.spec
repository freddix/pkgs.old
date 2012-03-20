Summary:	High-performance CORBA Object Request Broker
Name:		ORBit2
Version:	2.14.19
Release:	3
Epoch:		1
License:	GPL v2+/LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/ORBit2/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	7082d317a9573ab338302243082d10d1
Patch0:		%{name}-pthread.patch
URL:		http://www.gnome.org/projects/ORBit2/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libIDL-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker). It allows programs to send
requests and receive replies from other programs, regardless of the
locations of the two programs. CORBA is an architecture that enables
communication between program objects, regardless of the programming
language they're written in or the operating system they run on.

%package devel
Summary:	Header files, and utilities for ORBit
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
devel ORBit is a high-performance CORBA ORB with support for the C
language. It allows programs to send requests and receive replies from
other programs, regardless of the locations of the two programs.

This package includes the header files and utilities neecessary to
write programs that use CORBA technology.

%package apidocs
Summary:	ORBit2 API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ORBit2 API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static module - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/Everything_module.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ior-decode-2
%attr(755,root,root) %{_bindir}/linc-cleanup-sockets
%attr(755,root,root) %{_bindir}/orbit-idl-2
%attr(755,root,root) %{_bindir}/typelib-dump

%attr(755,root,root) %ghost %{_libdir}/libORBit*.so.?
%attr(755,root,root) %{_libdir}/libORBit*.so.*.*.*

%dir %{_libdir}/orbit-2.0
%{_libdir}/orbit-2.0/Everything_module.so
%{_datadir}/idl/orbit-2.0

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/orbit2-config
%attr(755,root,root) %{_libdir}/libORBit*.so
%{_libdir}/libname-server-2.a
%{_libdir}/libORBit*.la
%{_aclocaldir}/ORBit2.m4
%{_includedir}/orbit-2.0
%{_pkgconfigdir}/ORBit*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

