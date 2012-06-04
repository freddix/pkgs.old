Summary:	Gtkhtml library
Name:		gtkhtml
Version:	4.4.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtkhtml/4.4/%{name}-%{version}.tar.xz
# Source0-md5:	a47f76ec473c69b27af642a0dd6658f7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	enchant-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	4.0

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%package devel
Summary:	Header files etc. neccessary to develop gtkhtml applications
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc. neccessary to develop gtkhtml applications.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

# strange people living on this planet
sed -i -e 's|PKG_CHECK_MODULES(GIT.*||g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-deprecated-warning-flags	\
	--disable-silent-rules			\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-editor-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libgtkhtml-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-%{apiver}.so.*.*.*
%{_datadir}/%{name}-%{apiver}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-%{apiver}.so
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-%{apiver}.so
%{_includedir}/libgtkhtml-%{apiver}
%{_pkgconfigdir}/libgtkhtml-%{apiver}.pc
%{_pkgconfigdir}/gtkhtml-editor-%{apiver}.pc

