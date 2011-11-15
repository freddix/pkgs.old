Summary:	Password manager for the GNOME
Name:		revelation
Version:	0.4.12
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://bitbucket.org/erikg/revelation/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	26a8cdfb623010d7f7a719d1b7dfe1c5
URL:		http://revelation.olasagasti.info/index.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cracklib-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires(post,postun):	gtk+
Requires(post,preun):	GConf
Requires:	python-Crypto
Requires:	python-PyXML
Requires:	python-dbus
Requires:	python-libxml2
Requires:	python-pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Revelation is a password manager for the GNOME desktop. It stores all
accounts and passwords in a single, secure place, and gives you access
to it through a user-friendly graphical interface.

%prep
%setup -q

# don't check for runtime deps at build time
sed -i 's|RVL_PYTHON_MODULE.*||' configure.ac
sed -i 's|PKG_CHECK_MODULES(GNOME_PYTHON.*||' acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-desktop-update	\
	--disable-mime-update		\
	--disable-schemas-install	\
	--with-applet=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.py
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*/*.py

mv $RPM_BUILD_ROOT%{_datadir}/locale/{zh,zh_CN}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install revelation.schemas
%update_desktop_database_post
%update_icon_cache hicolor
%update_mime_database

%preun
%gconf_schema_uninstall revelation.schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/revelation
%{_datadir}/%{name}
%{_datadir}/mime/packages/revelation.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/16x16/apps/*.png
%{_iconsdir}/hicolor/24x24/apps/*.png
%{_iconsdir}/hicolor/32x32/apps/*.png
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_iconsdir}/hicolor/48x48/mimetypes/*.png

%dir %{py_sitedir}/%{name}
%dir %{py_sitedir}/%{name}/datahandler
%dir %{py_sitedir}/%{name}/bundle

%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%{py_sitedir}/%{name}/*.py[oc]
%{py_sitedir}/%{name}/datahandler/*.py[co]
%{py_sitedir}/%{name}/bundle/*.py[co]

%{_sysconfdir}/gconf/schemas/revelation.schemas

