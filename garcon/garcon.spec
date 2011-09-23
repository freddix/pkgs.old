%define		xfce_version	4.8.0
#
Summary:	freedesktop.org compliant menu implementation
Name:		garcon
Version:	0.1.9
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://archive.xfce.org/src/libs/garcon/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	a3ca1e54ad731c98f688900f6398fc20
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freedesktop.org compliant menu implementation for Xfce.

%package apidocs
Summary:	libxfce4mcs API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4mcs API documentation.

%package devel
Summary:	Development files for libxfce4mcs libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the libxfce4mcs libraries.

%prep
%setup -q

sed -i -e 's|nb_NO|nb|' -e 's|pt_PT|pt|' configure.in
mv po/{nb_NO,nb}.po
mv po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgarcon-1.so.?
%attr(755,root,root) %{_libdir}/libgarcon-1.so.*.*.*
# runtime deps, separte it!
%{_datadir}/desktop-directories/*.directory
%{_sysconfdir}/xdg/menus/xfce-applications.menu

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-1*.so
%{_libdir}/libgarcon-1.la
%{_includedir}/garcon-1
%{_pkgconfigdir}/*.pc

