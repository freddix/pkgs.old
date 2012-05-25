Summary:	GTK+ Bluetooth Manager
Name:		blueman
Version:	1.23
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://download.tuxfamily.org/blueman/%{name}-%{version}.tar.gz
# Source0-md5:	f0bee59589f4c23e35bf08c2ef8acaef
URL:		http://blueman-project.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	startup-notification-devel
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
%pyrequires_eq  python-libs
Requires:	bluez
Requires:	obex-data-server
Requires:	polkit
Requires:	python-dbus
Requires:	python-pygobject
Requires:	python-pynotify
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ Bluetooth Manager.

%prep
%setup -q

sed -i 's|AM_PATH_PYTHON(2.7)||' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static	\
	--with-no-runtime-deps-check
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/blueman-*
%attr(755,root,root) %{_libdir}/blueman-mechanism
%{_datadir}/%{name}
%{_desktopdir}/blueman-manager.desktop
%{_iconsdir}/hicolor/*/apps/blueman.*
%{_mandir}/man1/blueman-*.1*

%{_datadir}/dbus-1/services/blueman-applet.service
%{_datadir}/dbus-1/system-services/org.blueman.Mechanism.service
%{_datadir}/polkit-1/actions/org.blueman.policy
%{_sysconfdir}/dbus-1/system.d/org.blueman.Mechanism.conf

%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitescriptdir}/blueman

