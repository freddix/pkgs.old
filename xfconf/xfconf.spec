%define		xfce_version	4.10.0

Summary:	Xfce configuration manager
Name:		xfconf
Version:	4.10.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfconf/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	4ed48150a03fb5f42b455494307b7f28
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce configuration manager.

%package libs
Summary:	xfconf library
Group:		Libraries

%description libs
xfconf library.

%package devel
Summary:	Development files for xfconf library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development files for xfconf library.

%package apidocs
Summary:	xfconf API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
xfconf API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-perl-bindings	\
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xfconf-query
%dir %{_libdir}/xfce4/xfconf
%attr(755,root,root) %{_libdir}/xfce4/xfconf/xfconfd
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service

%files libs
%defattr(644,root,root,755)
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%attr(755,root,root) %ghost %{_libdir}/libxfconf-*.so.?
%attr(755,root,root) %{_libdir}/libxfconf-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfconf-*.so
%{_includedir}/xfce4/xfconf-*
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

