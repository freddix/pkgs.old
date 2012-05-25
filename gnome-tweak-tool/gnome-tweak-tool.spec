Summary:	A tool to customize advanced GNOME 3 options
Name:		gnome-tweak-tool
Version:	3.4.0.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tweak-tool/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	f1abe010c2b2235cb86718134c0219ce
URL:		http://live.gnome.org/GnomeTweakTool
BuildRequires:	GConf-devel
BuildRequires:	gettext-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	python-pygobject3-devel >= 3.2.1
BuildArch:	noarch
Requires:	gobject-introspection
Requires:	gsettings-desktop-schemas
Requires:	gtk+3
Requires:	python
Requires:	python-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to customize advanced GNOME 3 options.

%prep
%setup -q

sed -i "s/tweak_*.py/tweak_*.pyc/" gtweak/tweakmodel.py

%build
%configure \
	--disable-schemas-compile	\
	--host=%{_host}			\
	--build=%{_host}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-tweak-tool
%dir %{py_sitescriptdir}/gtweak
%dir %{py_sitescriptdir}/gtweak/tweaks
%{_datadir}/gnome-tweak-tool
%{_desktopdir}/gnome-tweak-tool.desktop
%{py_sitescriptdir}/gtweak/*.py*
%{py_sitescriptdir}/gtweak/tweaks/*.py*

