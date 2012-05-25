Summary:	GNOME screensaver
Name:		gnome-screensaver
Version:	3.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-screensaver/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	d9349c92ea179e2948cb2ede9e751d5a
Source1:	%{name}.pamd
# Source2-md5:	4ac105bf33c939114d92ce512bd02ed7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	intltool
BuildRequires:	libgnomekbd-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkg-config
BuildRequires:	systemd-devel
BuildRequires:	xmlto
BuildRequires:	xorg-libXScrnSaver-devel
Requires:	gsettings-desktop-schemas
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
A new screensaver solution for GNOME, with better HIG dialogs and a
much better integration into the desktop than the old xscreensaver.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules					\
	--enable-locking					\
	--enable-pam 						\
	--with-console-kit=no					\
	--with-mit-ext						\
	--with-systemd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gnome-screensaver

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gnome-screensaver
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnome-screensaver-dialog
%{_sysconfdir}/xdg/autostart/gnome-screensaver.desktop
%{_mandir}/man1/*.1*

