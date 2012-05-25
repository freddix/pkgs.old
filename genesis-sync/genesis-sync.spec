Summary:	Genesis Sync
Name:		genesis-sync
Version:	0.6.3
Release:	1
License:	GPL v3
Group:		Applications/Networking
Source0:	http://launchpad.net/genesis-sync/0.6/0.6.3/+download/%{name}_%{version}.tar.gz
# Source0-md5:	29cce0cb65f3a4b895c6ca8700db315e
URL:		https://launchpad.net/genesis-sync
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	python-configobj
Requires:	python-dbus
Requires:	python-gnome-desktop-evolution
Requires:	python-gnome-desktop-libwnck
Requires:	python-pygtk-gtk
Requires:	python-pynotify
Requires:	python-pyxdg
Requires:	syncevolution
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genesis Sync is a GUI for the excellent SyncEvolution.

%prep
%setup -qn %{name}

sed -i -e 's|GNOME|GTK;GNOME|g' genesis-sync.desktop.in

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%find_lang %{name}

%py_postclean
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/{Humanity*,ubuntu*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/genesis-sync
%{_datadir}/genesis-sync
%{_desktopdir}/genesis-sync.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/status/*
%dir %{py_sitescriptdir}/genesis_sync
%{py_sitescriptdir}/genesis_sync/*.py[co]

