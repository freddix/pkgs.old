%define		xfce_version	4.10.0

Summary:	Extension library to Xfce developed by os-cillation
Name:		exo
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://archive.xfce.org/src/xfce/exo/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	189bd19210e1d7d8601be1cdf27bf259
Patch0:		%{name}-freddix.patch
URL:		http://www.os-cillation.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	perl-URI
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xorg-libXt-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		basever	0.6

%description
Extension library to Xfce developed by os-cillation.

%package libs
Summary:	exo library
Group:		Libraries

%description libs
exo library.

%package devel
Summary:	Header files for libexo library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfce4util-devel >= %{xfce_version}

%description devel
Header files for libexo library.

%package apidocs
Summary:	exo API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
exo API documentation.

%package -n xfce4-preferred-applications
Summary:	The Xfce Preferred Applications framework
Group:		Applications
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	xfconf

%description -n xfce4-preferred-applications
The Xfce Preferred Applications framework.

%prep
%setup -qn exo-%{version}
%patch0 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\

rm -f $RPM_BUILD_ROOT%{py_sitedir}/exo-*/*.la

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{tl_PH,ur_PK}

%py_postclean

%find_lang %{name}-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n xfce4-preferred-applications
%update_icon_cache hicolor

%postun	-n xfce4-preferred-applications
%update_icon_cache hicolor

%files -f %{name}-1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/exo-csource
%attr(755,root,root) %{_bindir}/exo-open
%{_pixmapsdir}/exo-1

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libexo-1.so.?
%attr(755,root,root) %{_libdir}/libexo-1.so.*.*.*

%files -n xfce4-preferred-applications
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exo-desktop-item-edit
%attr(755,root,root) %{_bindir}/exo-preferred-applications
%dir %{_libdir}/xfce4/exo-1
%attr(755,root,root) %{_libdir}/xfce4/exo-1/exo-compose-mail-1
%attr(755,root,root) %{_libdir}/xfce4/exo-1/exo-helper-1
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/*.rc

%dir %{_datadir}/xfce4/helpers
%{_datadir}/xfce4/helpers/*.desktop
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/applications-internet.png
%{_iconsdir}/hicolor/*/apps/applications-other.png
%{_iconsdir}/hicolor/*/apps/preferences-desktop-default-applications.png
%{_mandir}/man1/*.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/exo-1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexo-1.so
%{_includedir}/exo-1
%{_pkgconfigdir}/*.pc

