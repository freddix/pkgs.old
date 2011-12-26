Summary:	MirBSD Korn Shell
Name:		mksh
Version:	40d
Release:	1
License:	BSD
Group:		Applications/Shells
Source0:	http://www.mirbsd.org/MirOS/dist/mir/mksh/%{name}-R%{version}.cpio.gz
# Source0-md5:	c6428401103367730a95b99284bf47dc
Source1:	%{name}-mkshrc
Patch0:		%{name}-mkshrc_support.patch
Patch1:		%{name}-no_stop_alias.patch
URL:		https://www.mirbsd.org/mksh.htm
BuildRequires:	ed
BuildRequires:	perl-base
# needed for /etc directory existence
Requires(pre):	FHS
Obsoletes:	pdksh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir			/bin

%description
mksh is the MirBSD enhanced version of the Public Domain Korn shell
(pdksh), a Bourne-compatible shell which is largely similar to the
original AT&T Korn shell. It includes bug fixes and feature
improvements in order to produce a modern, robust shell good for
interactive and especially script use. It has UTF-8 support in the
emacs command line editing mode; corresponds to OpenBSD 4.2-current
ksh sans GNU bash-like $PS1; the build environment requirements are
autoconfigured; throughout code simplification/bugfix/enhancement has
been done, and the shell has extended compatibility to other modern
shells.

%prep
%setup -qcT
gzip -dc %{SOURCE0} | cpio -mid
mv mksh/* .; rmdir mksh

%patch0 -p0
%patch1 -p1

%build
install -d out

CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
chmod +x ./Build.sh
bash ./Build.sh -Q -r -j -c lto

# skip some tests if not on terminal
if ! tty -s; then
	skip_tests="-C regress:no-ctty"
fi

%check
#./test.sh -v $skip_tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p mksh $RPM_BUILD_ROOT%{_bindir}

cp -a mksh.1 $RPM_BUILD_ROOT%{_mandir}/man1/mksh.1
echo ".so mksh.1" > $RPM_BUILD_ROOT%{_mandir}/man1/sh.1

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mkshrc
ln -sf mksh $RPM_BUILD_ROOT%{_bindir}/sh

# some pdksh scripts used that
ln -sf mksh $RPM_BUILD_ROOT%{_bindir}/ksh

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p %add_etc_shells -p /bin/sh /bin/ksh /bin/mksh
%preun  -p %remove_etc_shells -p /bin/sh /bin/ksh /bin/mksh

%posttrans -p %add_etc_shells -p /bin/sh /bin/ksh

%files
%defattr(644,root,root,755)
%doc dot.mkshrc
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/mkshrc
%attr(755,root,root) %{_bindir}/mksh
%attr(755,root,root) %{_bindir}/ksh
%attr(755,root,root) %{_bindir}/sh
%{_mandir}/man1/mksh.1*
%{_mandir}/man1/sh.1*

