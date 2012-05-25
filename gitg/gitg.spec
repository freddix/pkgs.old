Summary:	Git repository viewer
Name:		gitg
Version:	0.2.5
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gitg/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	1a1dad94d22946cefe08c98236621442
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-gio-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Git repository viewer.

%package libs
Summary:	gitg library
Group:		Libraries

%description libs
gitg library.

%package devel
Summary:	Header files for gitg library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for gitg library.

%prep
%setup -q

sed -i 's|Icon.*|Icon=gitg|' data/gitg.desktop.in.in

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-maintainer-mode	\
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gitg
%{_datadir}/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%{_desktopdir}/gitg.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg

%dir %{_datadir}/gitg
%{_datadir}/gitg/icons
%{_datadir}/gitg/language-specs
%{_datadir}/gitg/styles
%{_datadir}/gitg/ui

%{_mandir}/man1/gitg.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgitg-1.0.so.?
%attr(755,root,root) %{_libdir}/libgitg-1.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgitg-1.0.so
%{_includedir}/libgitg-1.0
%{_pkgconfigdir}/libgitg-1.0.pc

