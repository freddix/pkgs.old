%define		org_name	thunar-volman

Summary:	Volumes manager for Thunar
Name:		thunar-plugin-volman
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/thunar-volman/0.8/%{org_name}-%{version}.tar.bz2
# Source0-md5:	250af757ea629c7c27f554d17119080c
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-volman/
BuildRequires:	Thunar-devel >= 1.4.0
BuildRequires:	dbus-glib-devel
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	gtk+-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	startup-notification-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	Thunar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Thunar Volume Manager is an extension for the Thunar file manager,
which enables automatic management of removable drives and media. For
example, if Thunar-volman is installed and configured properly, and
you plug in your digital camera, it will automatically launch your
preferred photo application and import the new pictures from the
camera into your photo collection.

%prep
%setup -qn %{org_name}-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{org_name}-settings.desktop
%{_iconsdir}/hicolor/*/apps/*

