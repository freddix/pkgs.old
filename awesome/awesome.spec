Summary:	awesome window manager
Name:		awesome
Version:	3.4.10
Release:	2
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.xz
# Source0-md5:	b91c4d9392d3c3385e6074f4347044e2
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-xcb.patch
URL:		http://awesome.naquadah.org/
BuildRequires:	asciidoc
BuildRequires:	cairo-devel
BuildRequires:	cmake
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	glib-devel
BuildRequires:	gperf
BuildRequires:	imlib2-devel
BuildRequires:	libev-devel
BuildRequires:	libxdg-basedir-devel
BuildRequires:	lua-devel
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	readline-devel
BuildRequires:	sed
BuildRequires:	startup-notification-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xmlto
BuildRequires:	xorg-libICE-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
awesome is a highly configurable, next generation framework window
manager for X. It is very fast, light and extensible. It is primarly
targeted at power user, developer and any people dealing with every
day computing tasks and want to have fine-grained control on its
graphical environment.

%package doc
Summary:	awesome window manager API documentation
Group:		Documentation

%description doc
awesome window manager API documentation.

%package example-config
Summary:	Example config for awesome window manager
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description example-config
Example config for awesome window manager. It can be a good starting
point for those people, who have never used awesome window manager
before.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
	-DAWESOME_DATA_PATH=%{_datadir}/%{name}			\
	-DAWESOME_DOC_PATH=%{_docdir}/%{name}-%{version}	\
	-DLUA_INC_DIR=%{_includedir}/lua			\
	-DPREFIX=%{_prefix}					\
	-DSYSCONFDIR=%{_sysconfdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_docdir}/%{name}-doc-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

for file in $(find $RPM_BUILD_ROOT%{_datadir}/%{name} -iname "*.in"); do
	%{__rm} ${file}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README STYLE
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-client
%attr(755,root,root) %{_bindir}/awsetbg

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/awesome/lib/awful
%dir %{_datadir}/awesome/lib/awful/mouse
%dir %{_datadir}/awesome/themes

%{_datadir}/awesome/lib/awful/*.lua
%{_datadir}/awesome/lib/awful/layout
%{_datadir}/awesome/lib/awful/mouse/finder.lua
%{_datadir}/awesome/lib/awful/mouse/init.lua
%{_datadir}/awesome/lib/awful/widget
%{_datadir}/awesome/lib/beautiful.lua
%{_datadir}/awesome/lib/naughty.lua

%{_datadir}/%{name}/icons
%{_datadir}/awesome/themes/default
%{_datadir}/awesome/themes/sky
%{_datadir}/awesome/themes/zenburn

%{_datadir}/xsessions/%{name}.desktop

%{_mandir}/man[1,5]/*
%lang(de) %{_mandir}/de/man[1,5]/*
%lang(es) %{_mandir}/es/man[1,5]/*
%lang(fr) %{_mandir}/fr/man[1.5]/*

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}

%files example-config
%defattr(644,root,root,755)
%dir %{_sysconfdir}/xdg/awesome
%{_sysconfdir}/xdg/awesome/*

