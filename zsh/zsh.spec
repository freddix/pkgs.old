Summary:	Enhanced Bourne shell
Name:		zsh
Version:	4.3.17
Release:	3
License:	BSD-like
Group:		Applications/Shells
Source0:	ftp://ftp.zsh.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	74c5b275544400082a1cde806c98682a
Source3:	%{name}.dotrc
Source4:	%{name}.zlogin
Source5:	%{name}.zlogout
Source6:	%{name}.zprofile
Source7:	%{name}.zshenv
Source8:	%{name}rc
Patch4:		%{name}-nolibs.patch
URL:		http://www.zsh.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%prep
%setup -q

find Functions -type f -exec sed -i -e 's|#!.*/zsh|#!/bin/zsh|g' "{}" ";"

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%{__autoheader}
echo > stamp-h.in
%configure \
	--enable-cppflags="%{rpmcppflags}"		\
	--enable-cflags="%{rpmcflags}"			\
	--enable-ldflags="%{rpmldflags}"		\
	--enable-etcdir=%{_sysconfdir}/zsh		\
	--enable-zshenv=%{_sysconfdir}/zsh/zshenv	\
	--enable-zlogin=%{_sysconfdir}/zsh/zlogin	\
	--enable-zlogout=%{_sysconfdir}/zsh/zlogout	\
	--enable-zprofile=%{_sysconfdir}/zsh/zprofile	\
	--enable-zshrc=%{_sysconfdir}/zsh/zshrc		\
	--enable-cap					\
	--enable-fndir=%{_datadir}/zsh/functions	\
	--enable-function-subdirs			\
	--enable-maildir-support			\
	--enable-multibyte				\
	--enable-pcre					\
	--enable-scriptdir=%{_datadir}/zsh/scripts	\
	--enable-zsh-secure-free			\
	--with-tcsetpgrp				\
	--with-term-lib='ncursesw'
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{skel,zsh},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_sysconfdir}/zsh/{zlogin,zlogout,zprofile,zshenv,zshrc}.zwc
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zshrc
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zlogin
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zlogout
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/zsh/zlogin
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/zsh/zlogout
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/zsh/zprofile
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/zsh/zshenv
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/zsh/zshrc

rm -f Etc/Makefile*
find Functions Util StartupFiles -name .distfiles -o -name .cvsignore | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p <lua>
%lua_add_etc_shells /bin/zsh
os.execute("for i in zlogin zlogout zprofile zshenv zshrc; do [ -f /etc/zsh/$i ] && zsh -c \"zcompile /etc/zsh/$i\"; done")

%preun  -p <lua>
if arg[2] == 0 then
    %lua_remove_etc_shells /bin/zsh
end

%files
%defattr(644,root,root,755)

%doc Etc/* README LICENCE ChangeLog META-FAQ Util StartupFiles

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/scripts
%dir %{_datadir}/zsh/site-functions
%dir %{_libdir}/zsh
%dir %{_libdir}/zsh/%{version}
%dir %{_libdir}/zsh/%{version}/zsh
%dir %{_libdir}/zsh/%{version}/zsh/db
%dir %{_libdir}/zsh/%{version}/zsh/net
%dir %{_sysconfdir}/zsh

%attr(755,root,root) %{_bindir}/zsh
%attr(755,root,root) %{_libdir}/zsh/%{version}/zsh/*.so
%attr(755,root,root) %{_libdir}/zsh/%{version}/zsh/db/*.so
%attr(755,root,root) %{_libdir}/zsh/%{version}/zsh/net/*.so

%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/skel/.zlogin
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/skel/.zlogout
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/skel/.zshrc
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zsh/zlogin
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zsh/zlogout
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zsh/zprofile
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zsh/zshenv
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zsh/zshrc
%ghost %{_sysconfdir}/zsh/*.zwc

%{_datadir}/zsh/functions
%{_datadir}/zsh/scripts/newuser
%{_mandir}/man1/zsh*.1*

