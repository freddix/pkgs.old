%define		org_name	xfce4-xkb-plugin

Summary:	Displays and switched the current keyboard layout
Name:		xfce4-plugin-xkb
Version:	0.5.4.3
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-xkb-plugin/0.5/%{org_name}-%{version}.tar.bz2
# Source0-md5:	b31144bd50875ec73f0b3101456c97fd
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel
Requires:	gtk+-rsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays and switched the current keyboard layouts. The
new version can display the layout as text label and also as an image
of the corresponding country's flag.

%prep
%setup -qn %{org_name}-%{version}

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-xkb-plugin
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_datadir}/xfce4/xkb

