Summary:	Compiler for the GObject type system
Name:		vala
Version:	0.12.1
Release:	3
License:	LGPL v2.1
Group:		Applications
Source0:	http://download.gnome.org/sources/vala/0.14/%{name}-%{version}.tar.xz
# Source0-md5:	f05263a56c1e328637e4c97a61befdad
URL:		http://live.gnome.org/Vala
BuildRequires:	glib-devel
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib-devel
Requires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	0.12

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared
to applications and libraries written in C.

%package libs
Summary:	Vala library
Group:		Libraries

%description libs
Vala library.

%package vapigen
Summary:	Vala vavpi generator
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description vapigen
Vala vapi generator.

%package devel
Summary:	Header files for Vala library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for vala library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--enable-vapigen
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/vala/vapi

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/vala
%attr(755,root,root) %{_bindir}/vala-%{apiver}
%attr(755,root,root) %{_bindir}/valac
%attr(755,root,root) %{_bindir}/valac-%{apiver}

%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%dir %{_datadir}/vala-%{apiver}
%dir %{_datadir}/vala-%{apiver}/vapi
%{_datadir}/vala-%{apiver}/vapi/*.vapi
%{_datadir}/vala-%{apiver}/vapi/*.deps

%{_mandir}/man1/valac*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libvala-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libvala-%{apiver}.so.*.*.*

%files vapigen
%defattr(644,root,root,755)
%dir %{_libdir}/vala-%{apiver}
%attr(755,root,root) %{_bindir}/vala-gen-introspect
%attr(755,root,root) %{_bindir}/vala-gen-introspect-%{apiver}
%attr(755,root,root) %{_bindir}/vapicheck
%attr(755,root,root) %{_bindir}/vapicheck-%{apiver}
%attr(755,root,root) %{_bindir}/vapigen
%attr(755,root,root) %{_bindir}/vapigen-%{apiver}
%attr(755,root,root) %{_libdir}/vala-%{apiver}/gen-introspect-%{apiver}
%{_mandir}/man1/vala-gen-introspect-*.*
%{_mandir}/man1/vapigen-*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvala-%{apiver}.so
%{_aclocaldir}/vala.m4
%{_includedir}/vala-%{apiver}
%{_pkgconfigdir}/libvala-%{apiver}.pc

