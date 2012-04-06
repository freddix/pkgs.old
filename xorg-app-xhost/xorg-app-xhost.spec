Summary:	xhost application
Name:		xorg-app-xhost
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xhost-%{version}.tar.bz2
# Source0-md5:	a0fcd2cb6ddd9f378944cc6f4f83cd7c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libXau-devel
# just xmuu
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-xtrans-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xhost application.

%prep
%setup -qn xhost-%{version}

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
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xhost
%{_mandir}/man1/xhost.1x*

