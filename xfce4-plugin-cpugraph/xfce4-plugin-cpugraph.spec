%define		rname	xfce4-cpugraph-plugin

Summary:	Displays a graph from your latest system load
Name:		xfce4-plugin-cpugraph
Version:	1.0.2
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpugraph-plugin/1.0/%{rname}-%{version}.tar.bz2
# Source0-md5:	93d7658d989ebf110875bc2deb76d7b3
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel
Suggests:	xfce4-taskmanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This systemload plugin offers multiple display modes (LED, gradient,
fire, etc.) to show the current CPU load of the system. The colors and
the size of the plugin are customizable.

%prep
%setup -qn %{rname}-%{version}

# replace defaults
sed -i -e 's|xterm top|xfce4-taskmanager|g' panel-plugin/settings.c

%build
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{rname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor


%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/cpugraph.desktop
%{_iconsdir}/hicolor/*/apps/%{rname}.png

