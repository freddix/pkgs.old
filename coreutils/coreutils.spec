Summary:	GNU Core-utils - basic command line utilities
Name:		coreutils
Version:	8.14
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.xz
# Source0-md5:	bcb135ce553493a45aba01b39eb3920a
Source2:	DIR_COLORS
Source3:	fileutils.sh
Source10:	su.pamd
Source11:	su-l.pamd
Patch0:		%{name}-pam.patch
Patch1:		%{name}-getgid.patch
Patch2:		%{name}-su-paths.patch
Patch3:		%{name}-uname-cpuinfo.patch
Patch4:		%{name}-date-man.patch
Patch5:		%{name}-mem.patch
Patch6:		%{name}-7.4-sttytcsadrain.patch
URL:		http://www.gnu.org/software/coreutils/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	help2man
BuildRequires:	libcap-devel
BuildRequires:	pam-devel
BuildRequires:	texinfo
BuildRequires:	xz
Requires:	pam
Requires:	setup
Provides:	fileutils
Provides:	mktemp = %{version}-%{release}
Provides:	sh-utils
Provides:	stat
Provides:	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the GNU core utilities. This package is the union of the GNU
fileutils, sh-utils, and textutils packages.

Most of these programs have significant advantages over their Unix
counterparts, such as greater speed, additional options, and fewer
arbitrary limits.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

sed -i -e 's|GNU/Linux|Freddix|' m4/host-os.m4

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} -DSYSLOG_SUCCESS -DSYSLOG_FAILURE -DSYSLOG_NON_ROOT" 	\
	DEFAULT_POSIX2_VERSION=199209							\
	--disable-silent-rules								\
	--enable-install-program=arch							\
	--enable-no-install-program=hostname,kill,uptime				\
	--enable-pam
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,/sbin,%{_bindir},%{_sbindir},/etc/pam.d,/etc/shrc.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/{arch,basename,cat,chgrp,chmod,chown,cp,date,dd,\
df,echo,false,id,link,ln,ls,mkdir,mknod,mktemp,mv,nice,printf,pwd,rm,rmdir,\
sleep,sort,stat,stty,sync,touch,true,unlink,uname} $RPM_BUILD_ROOT/bin

mv -f $RPM_BUILD_ROOT%{_bindir}/chroot $RPM_BUILD_ROOT%{_sbindir}

# su is missed by "make install" called by non-root
install src/su $RPM_BUILD_ROOT/bin

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/shrc.d

install %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/su
install %{SOURCE11} $RPM_BUILD_ROOT/etc/pam.d/su-l

# unwanted
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man1/{hostname,kill,uptime}.1
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/kk/LC_TIME

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS THANKS-to-translators TODO

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/chroot
%attr(755,root,root) /bin/[!s]*
%attr(755,root,root) /bin/s[!u]*
%attr(4755,root,root) /bin/su

%dir %{_libdir}/coreutils
%attr(755,root,root) %{_libdir}/coreutils/libstdbuf.so

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/su
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/su-l
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/DIR_COLORS
%config(noreplace) /etc/shrc.d/fileutils.*sh

%{_mandir}/man1/*
%{_infodir}/coreutils.info*

