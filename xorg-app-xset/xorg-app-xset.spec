Summary:	xset application
Name:		xorg-app-xset
Version:	1.2.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xset-%{version}.tar.bz2
# Source0-md5:	d44e0057d6722b25d5a314e82e0b7e7c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
# just xmuu
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXp-devel
BuildRequires:	xorg-libXxf86misc-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xset application.

%prep
%setup -qn xset-%{version}

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
%attr(755,root,root) %{_bindir}/xset
%{_mandir}/man1/xset.1x*

