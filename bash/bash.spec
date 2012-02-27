%define		ver		4.2
%define		patchlevel	020
#
Summary:	GNU Bourne Again Shell (bash)
Name:		bash
Version:	%{ver}.%{patchlevel}
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	ftp://ftp.gnu.org/gnu/bash/%{name}-%{ver}.tar.gz
# Source0-md5:	3fb927c7c33022f1c327f14a81c0d4b0
Source1:	%{name}rc
Source2:	%{name}-skel-.%{name}_logout
Source3:	%{name}-skel-.%{name}_profile
Source4:	%{name}-skel-.%{name}rc
Patch0:		%{name}-paths.patch
Patch1000:	%{name}-patchlevel-%{patchlevel}.patch
URL:		http://www.gnu.org/software/bash/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	grep
Requires:	readline
Requires:	setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bash is a GNU project sh-compatible shell or command language
interpreter. Bash (Bourne Again shell) incorporates useful features
from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification. Bash offers several improvements
over sh, including command line editing, unlimited size command
history, job control, shell functions and aliases, indexed arrays of
unlimited size and integer arithmetic in any base from two to 64. Bash
is ultimately intended to conform to the IEEE POSIX P1003.2/ISO 9945.2
Shell and Tools standard. Bash is the default shell for Linux
Mandrake. You should install bash because of its popularity and power.
You'll probably end up using it.

%prep
%setup -qn %{name}-%{ver}
%patch1000 -p0

%patch0 -p1

%build
cp -f /usr/share/automake/config.* support
%{__autoconf}
%configure \
	--enable-readline		\
	--with-curses			\
	--with-installed-readline	\
	--without-bash-malloc

%{__make} \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

%if 0
%{__make} tests
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,/etc/skel}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/bash $RPM_BUILD_ROOT/bin

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/bashrc
echo .so bash.1 > $RPM_BUILD_ROOT%{_mandir}/man1/rbash.1

ln -sf bash $RPM_BUILD_ROOT/bin/rbash

install %{SOURCE2} $RPM_BUILD_ROOT/etc/skel/.bash_logout
install %{SOURCE3} $RPM_BUILD_ROOT/etc/skel/.bash_profile
install %{SOURCE4} $RPM_BUILD_ROOT/etc/skel/.bashrc
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

rm -f $RPM_BUILD_ROOT%{_bindir}/bashbug

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p <lua>
%lua_add_etc_shells /bin/bash /bin/rbash
os.execute("/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1")

%preun	-p <lua>
if arg[2] == 0 then
	%lua_remove_etc_shells /bin/bash /bin/rbash
end

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES NEWS README doc/{FAQ,INTRO}

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bashrc
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bash_logout
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bash_profile
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/skel/.bashrc

%attr(755,root,root) /bin/bash
%attr(755,root,root) /bin/rbash

%{_infodir}/bash.info*
%{_mandir}/man1/*

