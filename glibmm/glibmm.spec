%include	/usr/lib/rpm/macros.perl

Summary:	A C++ interface for glib library
Name:		glibmm
Version:	2.30.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.30/%{name}-%{version}.tar.xz
# Source0-md5:	152ca53641ee7d4472115020bbab88ed
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mm-common
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	2.4

%description
A C++ interface for glib library.

%package devel
Summary:	Header files for glibmm library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for glibmm library.

%package apidocs
Summary:	Reference documentation and examples for glibmm
Group:		Documentation

%description apidocs
Reference documentation and examples for glibmm.

%prep
%setup -q

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT	\
	libdocdir=%{_gtkdocdir}/%{name}-%{apiver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgiomm-%{apiver}.so.1
%attr(755,root,root) %ghost %{_libdir}/libglibmm-%{apiver}.so.1
%attr(755,root,root) %ghost %{_libdir}/libglibmm_generate_extra_defs-%{apiver}.so.1
%attr(755,root,root) %{_libdir}/libgiomm-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libglibmm-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libglibmm_generate_extra_defs-%{apiver}.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{apiver}/proc/*.pl
%attr(755,root,root) %{_libdir}/%{name}-%{apiver}/proc/gmmproc
%attr(755,root,root) %{_libdir}/libgiomm-%{apiver}.so
%attr(755,root,root) %{_libdir}/libglibmm-%{apiver}.so
%attr(755,root,root) %{_libdir}/libglibmm_generate_extra_defs-%{apiver}.so

%dir %{_libdir}/%{name}-%{apiver}
%dir %{_libdir}/%{name}-%{apiver}/proc
%dir %{_libdir}/giomm-%{apiver}

%{_includedir}/%{name}-%{apiver}
%{_includedir}/giomm-%{apiver}

%{_libdir}/%{name}-%{apiver}/include
%{_libdir}/%{name}-%{apiver}/proc/m4
%{_libdir}/%{name}-%{apiver}/proc/pm

%{_libdir}/giomm-%{apiver}/include

%{_pkgconfigdir}/giomm-%{apiver}.pc
%{_pkgconfigdir}/glibmm-%{apiver}.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-%{apiver}

