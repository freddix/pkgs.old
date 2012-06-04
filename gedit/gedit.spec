Summary:	GNOME text editor
Name:		gedit
Version:	3.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/gedit/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	1f3e9f255fc16609ca8598a82da18cff
URL:		http://gedit.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	enchant-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libpeas-gtk-devel
BuildRequires:	libtool
BuildRequires:	libzeitgeist-devel
BuildRequires:	pkg-config
BuildRequires:	python-pygobject3-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
gedit is a small but powerful text editor for GTK+ and/or GNOME. It
includes such features as split-screen mode, a plugin API, which
allows gedit to be extended to support many features while remaining
small at its core, multiple document editing and many more functions.

%package plugins-python
Summary:	Gedit plugins written in python
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject3

%description plugins-python
Gedit plugins written in python.

%package plugin-zeitgeist
Summary:	Gedit zeitgeist plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Suggests:	zeitgeist
Suggests:	zeitgeist-datahub

%description plugin-zeitgeist
Logs access and leave event for documents used with gedit.

%package libs
Summary:	gedit libraries
Group:		X11/Libraries

%description libs
gedit libraries.

%package devel
Summary:	gedit header files
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
gedit header files

%package apidocs
Summary:	gedit API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gedit API documentation.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-updater		\
	--enable-python			\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,en@shaw,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/*/*.py

%py_postclean

%find_lang gedit --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_gsettings_cache

%postun
%update_desktop_database_postun
%update_gsettings_cache

%post plugins-python
%update_gsettings_cache

%postun plugins-python
%update_gsettings_cache

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f gedit.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%dir %{_libdir}/gedit/plugins
%attr(755,root,root) %{_bindir}/gedit
%attr(755,root,root) %{_bindir}/gnome-text-editor
%attr(755,root,root) %{_libdir}/gedit/plugins/*.so
%exclude %{_libdir}/gedit/plugins/libzeitgeistplugin.so
%{_libdir}/gedit/plugins/changecase.plugin
%{_libdir}/gedit/plugins/docinfo.plugin
%{_libdir}/gedit/plugins/filebrowser.plugin
%{_libdir}/gedit/plugins/modelines.plugin
%{_libdir}/gedit/plugins/sort.plugin
%{_libdir}/gedit/plugins/spell.plugin
%{_libdir}/gedit/plugins/time.plugin
%{_datadir}/gedit
%{_datadir}/GConf/gsettings/gedit.convert
%{_datadir}/dbus-1/services/org.gnome.gedit.service
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.filebrowser.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.time.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.time.gschema.xml
%{_desktopdir}/gedit.desktop
%{_mandir}/man1/gedit.1*

%files plugins-python
%defattr(644,root,root,755)
%dir %{_libdir}/gedit/plugins/externaltools
%dir %{_libdir}/gedit/plugins/pythonconsole
%dir %{_libdir}/gedit/plugins/quickopen
%dir %{_libdir}/gedit/plugins/snippets
%{_libdir}/gedit/plugins/externaltools.plugin
%{_libdir}/gedit/plugins/pythonconsole.plugin
%{_libdir}/gedit/plugins/quickopen.plugin
%{_libdir}/gedit/plugins/snippets.plugin
%{_libdir}/gedit/plugins/externaltools/*.py[co]
%{_libdir}/gedit/plugins/pythonconsole/*.py[co]
%{_libdir}/gedit/plugins/quickopen/*.py[co]
%{_libdir}/gedit/plugins/snippets/*.py[co]
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.externaltools.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.pythonconsole.gschema.xml
%{py_sitedir}/gi/overrides/*.py[co]

%files plugin-zeitgeist
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gedit/plugins/libzeitgeistplugin.so
%{_libdir}/gedit/plugins/zeitgeist.plugin

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/girepository-1.0
%attr(755,root,root) %{_libdir}/gedit/libgedit-private.so
%{_libdir}/gedit/girepository-1.0/Gedit-3.0.typelib

%files devel
%defattr(644,root,root,755)
%{_includedir}/gedit-3.0
%{_pkgconfigdir}/gedit.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gedit

