%include	/usr/lib/rpm/macros.perl
#
Summary:	A C++ interface for the GTK+
Name:		gtkmm
Version:	2.24.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	7f99b5bc384785baf99bd22d4a210f4b
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	atkmm-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairomm-devel
BuildRequires:	glibmm-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mm-common
BuildRequires:	pangomm-devel
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	2.4

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

%package devel
Summary:	GTK-- and GDK-- header files, development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for GTK-- library.

%package apidocs
Summary:	Reference documentation and examples for GTK-- and GDK--
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Reference documentation and examples for GTK-- and GDK--.

%prep
%setup -q

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	--disable-demos		\
	--disable-examples
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT	\
	libdocdir=%{_gtkdocdir}/%{name}-%{apiver}

rm -rf $RPM_BUILD_ROOT%{_datadir}/gtkmm-%{apiver}/demo

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING README
%attr(755,root,root) %ghost %{_libdir}/libg[dt]kmm*.so.?
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so
%{_libdir}/libg[dt]kmm*.la
%{_libdir}/g[dt]kmm-%{apiver}
%{_includedir}/g[dt]kmm-%{apiver}
%{_pkgconfigdir}/g[dt]kmm*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-%{apiver}

