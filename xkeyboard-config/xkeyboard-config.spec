Summary:	X Keyboard Configuration Database
Name:		xkeyboard-config
Version:	2.5.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/data/%{name}-%{version}.tar.bz2
# Source0-md5:	29cbf3980bbe94c3ffc9c233ea638059
URL:		http://www.freedesktop.org/wiki/Software_2fXKeyboardConfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-xkbcomp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The non-arch keyboard configuration database for X Window System. The
goal is to provide the consistent, well-structured, frequently
released open source of X keyboard configuration data for X Window
System implementations (free, open source and commercial). The project
is targeted to XKB-based systems.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--host=%{_host}				\
        --build=%{_host}			\
	--enable-compat-rules			\
	--with-xkb-base=%{_datadir}/X11/xkb	\
	--with-xkb-rules-symlink=xorg
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s /var/lib/xkb $RPM_BUILD_ROOT%{_datadir}/X11/xkb/compiled

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README TODO docs/H* docs/R*
%{_datadir}/X11/xkb
%{_npkgconfigdir}/xkeyboard-config.pc

