Summary:	xinit scripts
Name:		xorg-app-xinit
Version:	1.3.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xinit-%{version}.tar.bz2
# Source0-md5:	9c0943cbd83e489ad1b05221b97efd44
Source10:	%{name}-Xclients
Source11:	%{name}-Xresources
Source12:	%{name}-desktop
Source13:	%{name}-xinitdefs
Source14:	%{name}-xinitrc
Patch0:		%{name}-xwrapper.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-util-macros
Requires:	xorg-app-xauth
Requires:	xorg-app-xmodmap
Requires:	xorg-app-xrdb
Requires:	xsession
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xinit scripts.

%prep
%setup -qn xinit-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--with-xinitdir=/etc/X11/xinit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE10} $RPM_BUILD_ROOT/etc/X11/xinit/Xclients
install %{SOURCE11} $RPM_BUILD_ROOT/etc/X11/xinit/Xresources
install %{SOURCE12} $RPM_BUILD_ROOT/etc/sysconfig/desktop
install %{SOURCE13} $RPM_BUILD_ROOT/etc/X11/xinit/xinitdefs
install %{SOURCE14} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/startx
%attr(755,root,root) %{_bindir}/xinit

%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xclients
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xresources
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitdefs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/desktop

%{_mandir}/man1/startx.1x*
%{_mandir}/man1/xinit.1x*

