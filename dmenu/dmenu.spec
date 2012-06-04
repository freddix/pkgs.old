Summary:	dmenu - a generic menu for X
Name:		dmenu
Version:	4.5
Release:	1
License:	MIT
Group:		Applications
Source0:	http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
# Source0-md5:	9c46169ed703732ec52ed946c27d84b4
URL:		http://tools.suckless.org/dmenu
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXinerama-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It
manages huge amounts (up to 10.000 and more) of user defined menu
items efficiently.

%prep
%setup -q

%build
cat << 'EOF' >> config.mk
PREFIX=%{_prefix}
CFLAGS:=%{rpmcflags} $(CFLAGS)
LDFLAGS:=%{rpmldflags} $(LDFLAGS)
EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dmenu
%attr(755,root,root) %{_bindir}/stest
%attr(755,root,root) %{_bindir}/dmenu_run
%{_mandir}/man1/dmenu.1*
%{_mandir}/man1/stest.1*

