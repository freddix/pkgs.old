Summary:	Screen capture application for XFCE
Name:		xfce4-screenshooter
Version:	1.8.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-screenshooter/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	d0ffea2052a8e70154cf13789070711f
Patch0:		%{name}-plugin.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-panel-devel
BuildRequires:	xorg-libXfixes-devel
Requires(pre,post):	gtk+-update-icon-cache
Requires(pre,post):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Screen capture application for XFCE.

%package -n xfce4-plugin-screenshooter
Summary:	Screenshooter plugin for Xfce Panel
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	xfce4-panel

%description -n xfce4-plugin-screenshooter
Screenshooter plugin for Xfce Panel.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-screenshooter
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/applets-*.*
%{_mandir}/man1/xfce4-screenshooter.1*

%files -n xfce4-plugin-screenshooter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/screenshooter.desktop

