Summary:	A user-friendly file manager and visual shell
Name:		mc
Version:	4.7.5.5
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.midnight-commander.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	ef1582651115ca8aa52f8d11e99f7da3
Patch0:		%{name}-elinks.patch
URL:		http://www.ibiblio.org/mc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel
BuildRequires:	gpm-devel
BuildRequires:	xorg-libX11-devel
Requires:	file
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
FTP, view tar, zip files, and poke into RPMs for specific files. :-)

%prep
%setup -q
%patch0 -p1

rm -f po/stamp-po
sed -i 's:|hxx|:|hh|hpp|hxx|:' misc/syntax/Syntax

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

export X11_WWW="xdg-open"
%configure \
	--disable-silent-rules	\
	--enable-charset	\
	--with-edit		\
	--with-gpm-mouse	\
	--with-mcfs		\
	--with-screen=slang	\
	--with-vfs		\
	--with-x 		\
	--without-debug		\
	--without-ext2undel
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,pam.d,shrc.d,sysconfig}} \
	$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/shrc.d

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{be-tarask,fi_FI,it_IT}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README

%dir %{_datadir}/mc
%dir %{_libdir}/mc
%dir %{_libdir}/mc/extfs.d
%dir %{_sysconfdir}/mc

%attr(755,root,root) %{_bindir}/mc*
%attr(755,root,root) %{_libdir}/mc/*.csh
%attr(755,root,root) %{_libdir}/mc/*.sh
%attr(755,root,root) %{_libdir}/mc/cons.saver

%config /etc/shrc.d/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mc/*.*

%{_datadir}/mc/mc.*
%{_datadir}/mc/skins
%{_datadir}/mc/syntax

%dir %{_datadir}/mc/help
%dir %{_datadir}/mc/hints
%{_datadir}/mc/help/mc.hlp
%{_datadir}/mc/hints/mc.hint
%lang(cs) %{_datadir}/mc/hints/mc.hint.cs
%lang(es) %{_datadir}/mc/help/mc.hlp.es
%lang(es) %{_datadir}/mc/hints/mc.hint.es
%lang(hu) %{_datadir}/mc/help/mc.hlp.hu
%lang(hu) %{_datadir}/mc/hints/mc.hint.hu
%lang(it) %{_datadir}/mc/help/mc.hlp.it
%lang(it) %{_datadir}/mc/hints/mc.hint.it
%lang(nl) %{_datadir}/mc/hints/mc.hint.nl
%lang(pl) %{_datadir}/mc/help/mc.hlp.pl
%lang(pl) %{_datadir}/mc/hints/mc.hint.pl
%lang(ru) %{_datadir}/mc/help/mc.hlp.ru
%lang(ru) %{_datadir}/mc/hints/mc.hint.ru
%lang(sr) %{_datadir}/mc/help/mc.hlp.sr
%lang(sr) %{_datadir}/mc/hints/mc.hint.sr
%lang(uk) %{_datadir}/mc/hints/mc.hint.uk
%lang(zh) %{_datadir}/mc/hints/mc.hint.zh

%{_libdir}/mc/extfs.d/README*
%attr(755,root,root) %{_libdir}/mc/extfs.d/a+
%attr(755,root,root) %{_libdir}/mc/extfs.d/apt+
%attr(755,root,root) %{_libdir}/mc/extfs.d/deb*
%attr(755,root,root) %{_libdir}/mc/extfs.d/dpkg+
%attr(755,root,root) %{_libdir}/mc/extfs.d/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs.d/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs.d/rpms+
%attr(755,root,root) %{_libdir}/mc/extfs.d/uzip
%attr(755,root,root) %{_libdir}/mc/extfs.d/audio
%attr(755,root,root) %{_libdir}/mc/extfs.d/bpp
%attr(755,root,root) %{_libdir}/mc/extfs.d/hp48+
%attr(755,root,root) %{_libdir}/mc/extfs.d/iso9660
%attr(755,root,root) %{_libdir}/mc/extfs.d/lslR
%attr(755,root,root) %{_libdir}/mc/extfs.d/rpm
%attr(755,root,root) %{_libdir}/mc/extfs.d/s3+
%attr(755,root,root) %{_libdir}/mc/extfs.d/trpm
%attr(755,root,root) %{_libdir}/mc/extfs.d/u7z
%attr(755,root,root) %{_libdir}/mc/extfs.d/uace
%attr(755,root,root) %{_libdir}/mc/extfs.d/ualz
%attr(755,root,root) %{_libdir}/mc/extfs.d/uar*
%attr(755,root,root) %{_libdir}/mc/extfs.d/uc1541
%attr(755,root,root) %{_libdir}/mc/extfs.d/ucab
%attr(755,root,root) %{_libdir}/mc/extfs.d/uha
%attr(755,root,root) %{_libdir}/mc/extfs.d/ulha
%attr(755,root,root) %{_libdir}/mc/extfs.d/urar
%attr(755,root,root) %{_libdir}/mc/extfs.d/uzoo

%dir %{_libdir}/mc/fish
%{_libdir}/mc/fish/README.fish
%attr(755,root,root) %{_libdir}/mc/fish/[a-z]*

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(sr) %{_mandir}/sr/man1/*

