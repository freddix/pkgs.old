Summary:	setxkbmap application - set the keyboard using the X Keyboard Extension
Name:		xorg-app-setxkbmap
Version:	1.3.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/setxkbmap-%{version}.tar.bz2
# Source0-md5:	1001771344608e120e943a396317c33a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libxkbfile-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The setxkbmap command maps the keyboard to use the layout determined
by the options specified on the command line.

%prep
%setup -qn setxkbmap-%{version}

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1x*

