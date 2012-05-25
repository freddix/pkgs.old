%define		pre	pre5
#
Summary:	Experimantal Links (text WWW browser)
Name:		elinks
Version:	0.12
Release:	0.%{pre}.2
Epoch:		1
License:	GPL
Group:		Applications/Networking
Source0:	http://elinks.or.cz/download/%{name}-%{version}%{pre}.tar.bz2
# Source0-md5:	92790144290131ac5e63b44548b45e08
URL:		http://elinks.or.cz/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gpm-devel
BuildRequires:	libidn-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/elinks

%description
This is the elinks tree - intended to provide feature-rich version of
links, however not rock-stable and dedicated mainly for testing. Its
purpose is to make alternative to links, until Mikulas will have some
time to maintain it, and to test and tune various patches for Mikulas
to be able to include them in the official links releases.

%prep
%setup -qn %{name}-%{version}%{pre}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	HAVE_SMBCLIENT=yes	\
	--disable-no-root	\
	--enable-256-colors	\
	--enable-exmode		\
	--enable-fastmem	\
	--enable-finger		\
	--enable-gopher		\
	--enable-html-highlight	\
	--enable-marks		\
	--enable-nntp		\
	--with-gnutls		\
	--with-x		\
	--without-openssl	\
	--without-spidermonkey
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install V=1 \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README SITES TODO
%doc contrib/{keybind*,wipe-out-ssl*,lua/elinks-remote}
%doc contrib/conv/{*awk,*.pl,*.sh}
%doc doc/html/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*

