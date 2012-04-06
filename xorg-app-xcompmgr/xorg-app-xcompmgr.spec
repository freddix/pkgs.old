Summary:	Composite extension option manager
Name:		xorg-app-xcompmgr
Version:	1.1.6
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/xcompmgr-%{version}.tar.bz2
# Source0-md5:	d45afaf2a153e8a5dd93a92955060c9a
URL:		http://freedesktop.org/Software/xapps
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXcomposite-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite extension option manager.

%prep
%setup -qn xcompmgr-%{version}

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
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

