Summary:	Pluggable Authentication Modules: modular, incremental authentication
Name:		pam
Version:	1.1.5
Release:	1
License:	GPL or BSD
Group:		Base
#Source0:	http://ftp.kernel.org/pub/linux/libs/pam/library/Linux-PAM-%{version}.tar.bz2
Source0:	https://fedorahosted.org/releases/l/i/linux-pam/Linux-PAM-%{version}.tar.bz2
# Source0-md5:	927ee5585bdec5256c75117e9348aa47
#Source1:	http://ftp.kernel.org/pub/linux/libs/pam/library/Linux-PAM-%{version}.tar.bz2.sign
# Source1-md5:	0b4af346d3107a4d2b08be5ce3dad373
Source2:	dlopen.sh
Source3:	common-account
Source4:	common-auth
Source5:	common-password
Source6:	common-session
Source7:	common-session-noninteractive
Source8:	other
Source9:	limits.conf
Patch0:		%{name}-exec-failok.patch
Patch1:		%{name}-db-gdbm.patch
Patch2:		%{name}-mkhomedir-notfound.patch
URL:		https://fedorahosted.org/linux-pam/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel
# gdbm due to db pulling libpthread
BuildRequires:	gdbm-devel
BuildRequires:	flex
BuildRequires:	glibc-devel
BuildRequires:	libtool
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	w3m
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
PAM (Pluggable Authentication Modules) is a powerful, flexible,
extensible authentication system which allows the system administrator
to configure authentication services individually for every
pam-compliant application without recompiling any of the applications.

%package libs
Summary:	PAM modules and libraries
Group:		Libraries
Requires:	cracklib-dicts

%description libs
Core PAM modules and libraries.

%package devel
Summary:	PAM header files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for developing PAM based applications.

%prep
%setup -qn Linux-PAM-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

install %{SOURCE2} .

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-audit				\
	--disable-prelude			\
	--disable-selinux			\
	--enable-db=gdbm			\
	--enable-isadir=../../%{_lib}/security	\
	--enable-shared				\
	--includedir=%{_includedir}/security	\
	--libdir=/%{_lib}

%{__make} \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},/etc/pam.d,/var/log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d doc/txts
for r in modules/pam_*/README ; do
	cp -f $r doc/txts/README.$(basename $(dirname $r))
done
install -d doc/html
cp -f doc/index.html doc/html/

# fix PAM/pam man page
echo ".so PAM.8" > $RPM_BUILD_ROOT%{_mandir}/man8/pam.8

:> $RPM_BUILD_ROOT/etc/security/opasswd

cd $RPM_BUILD_ROOT/%{_lib}
for f in lib*.la ; do
	sed -e 's|/%{_lib}/libpam|%{_libdir}/libpam|g' $f > $RPM_BUILD_ROOT%{_libdir}/$f
	rm -f $f
	sed -i -e "s|libdir='/%{_lib}|libdir='%{_libdir}|g" $RPM_BUILD_ROOT%{_libdir}/$f
done
ln -sf /%{_lib}/$(echo libpam.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /%{_lib}/$(echo libpam_misc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /%{_lib}/$(echo libpamc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpamc.so
cd -

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/common-account
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/common-auth
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/common-password
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/common-session
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/common-session-noninteractive
install %{SOURCE8} $RPM_BUILD_ROOT/etc/pam.d/other
install %{SOURCE9} $RPM_BUILD_ROOT/etc/security

# Make sure every module subdirectory gave us a module.  Yes, this is hackish.
for dir in modules/pam_* ; do

[ ${dir} = "modules/pam_selinux" ] && continue
[ ${dir} = "modules/pam_sepermit" ] && continue
[ ${dir} = "modules/pam_tty_audit" ] && continue
	if [ -d ${dir} ] ; then
		if ! ls -1 $RPM_BUILD_ROOT/%{_lib}/security/`basename ${dir}`*.so ; then
			echo ERROR `basename ${dir}` did not build a module.
			exit 1
		fi
	fi
done

for module in $RPM_BUILD_ROOT/%{_lib}/security/pam*.so ; do
# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
	if ! env LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_lib} \
			./dlopen.sh -ldl -lpam -L$RPM_BUILD_ROOT/%{_lib} ${module} ; then
		echo ERROR module: ${module} cannot be loaded.
		exit 1
	fi
done

# useless - shut up check-files
rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.{la,a}
rm -f $RPM_BUILD_ROOT/%{_lib}/lib*.so
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/Linux-PAM

rm -rf $RPM_BUILD_ROOT{/%{_lib}/security/pam_selinux.so,%{_sbindir}/pam_selinux_check,%{_mandir}/man8/pam_selinux*.8*}

%find_lang Linux-PAM

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f Linux-PAM.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG ChangeLog Copyright NEWS doc/txts/README*
%doc doc/specs/*.txt doc/sag/Linux-PAM_*.txt doc/{sag,}/html

%attr(4755,root,root) /sbin/unix_chkpwd
%attr(4755,root,root) /sbin/unix_update
%attr(755,root,root) %{_sbindir}/mkhomedir_helper
%attr(755,root,root) %{_sbindir}/pam_tally
%attr(755,root,root) %{_sbindir}/pam_tally2
%attr(755,root,root) %{_sbindir}/pam_timestamp_check

%dir %attr(755,root,root) /etc/pam.d
%config(noreplace) %verify(not md5 mtime size) /etc/environment
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/common-account
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/common-auth
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/common-password
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/common-session
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/common-session-noninteractive
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/other
%config(noreplace) %verify(not md5 mtime size) /etc/security/access.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/group.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/limits.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/namespace.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_env.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/time.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/opasswd
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/namespace.init

%{_mandir}/man5/*
%{_mandir}/man8/PAM.*
%{_mandir}/man8/mkhomedir_helper.8*
%{_mandir}/man8/pam.*
%{_mandir}/man8/pam_[a-r]*
%{_mandir}/man8/pam_[t-x]*
%{_mandir}/man8/pam_securetty*
%{_mandir}/man8/pam_shells*
%{_mandir}/man8/pam_succeed_if*
%{_mandir}/man8/unix_chkpwd*
%{_mandir}/man8/unix_update*

%files libs
%defattr(644,root,root,755)

%dir /%{_lib}/security/pam_filter

%attr(755,root,root) %ghost /%{_lib}/libpam.so.?
%attr(755,root,root) %ghost /%{_lib}/libpam_misc.so.?
%attr(755,root,root) %ghost /%{_lib}/libpamc.so.?
%attr(755,root,root) /%{_lib}/libpam.so.*.*.*
%attr(755,root,root) /%{_lib}/libpam_misc.so.*.*.*
%attr(755,root,root) /%{_lib}/libpamc.so.*.*.*

%attr(755,root,root) /%{_lib}/security/pam_access.so
%attr(755,root,root) /%{_lib}/security/pam_cracklib.so
%attr(755,root,root) /%{_lib}/security/pam_debug.so
%attr(755,root,root) /%{_lib}/security/pam_deny.so
%attr(755,root,root) /%{_lib}/security/pam_echo.so
%attr(755,root,root) /%{_lib}/security/pam_env.so
%attr(755,root,root) /%{_lib}/security/pam_exec.so
%attr(755,root,root) /%{_lib}/security/pam_faildelay.so
%attr(755,root,root) /%{_lib}/security/pam_filter.so
%attr(755,root,root) /%{_lib}/security/pam_filter/upperLOWER
%attr(755,root,root) /%{_lib}/security/pam_ftp.so
%attr(755,root,root) /%{_lib}/security/pam_group.so
%attr(755,root,root) /%{_lib}/security/pam_issue.so
%attr(755,root,root) /%{_lib}/security/pam_keyinit.so
%attr(755,root,root) /%{_lib}/security/pam_lastlog.so
%attr(755,root,root) /%{_lib}/security/pam_limits.so
%attr(755,root,root) /%{_lib}/security/pam_listfile.so
%attr(755,root,root) /%{_lib}/security/pam_localuser.so
%attr(755,root,root) /%{_lib}/security/pam_loginuid.so
%attr(755,root,root) /%{_lib}/security/pam_mail.so
%attr(755,root,root) /%{_lib}/security/pam_mkhomedir.so
%attr(755,root,root) /%{_lib}/security/pam_motd.so
%attr(755,root,root) /%{_lib}/security/pam_namespace.so
%attr(755,root,root) /%{_lib}/security/pam_nologin.so
%attr(755,root,root) /%{_lib}/security/pam_permit.so
%attr(755,root,root) /%{_lib}/security/pam_pwhistory.so
%attr(755,root,root) /%{_lib}/security/pam_rhosts.so
%attr(755,root,root) /%{_lib}/security/pam_rootok.so
%attr(755,root,root) /%{_lib}/security/pam_securetty.so
%attr(755,root,root) /%{_lib}/security/pam_shells.so
%attr(755,root,root) /%{_lib}/security/pam_stress.so
%attr(755,root,root) /%{_lib}/security/pam_succeed_if.so
%attr(755,root,root) /%{_lib}/security/pam_tally2.so
%attr(755,root,root) /%{_lib}/security/pam_tally.so
%attr(755,root,root) /%{_lib}/security/pam_time.so
%attr(755,root,root) /%{_lib}/security/pam_timestamp.so
%attr(755,root,root) /%{_lib}/security/pam_umask.so
%attr(755,root,root) /%{_lib}/security/pam_unix.so
%attr(755,root,root) /%{_lib}/security/pam_userdb.so
%attr(755,root,root) /%{_lib}/security/pam_warn.so
%attr(755,root,root) /%{_lib}/security/pam_wheel.so
%attr(755,root,root) /%{_lib}/security/pam_xauth.so

%files devel
%defattr(644,root,root,755)
%doc doc/{adg,mwg}/Linux-PAM_*.txt doc/{adg,mwg,}/html
%attr(755,root,root) %{_libdir}/libpam.so
%attr(755,root,root) %{_libdir}/libpam_misc.so
%attr(755,root,root) %{_libdir}/libpamc.so
%{_libdir}/libpam.la
%{_libdir}/libpam_misc.la
%{_libdir}/libpamc.la
%{_includedir}/security/_pam_*.h
%{_includedir}/security/pam*.h
%{_mandir}/man3/misc_conv.3*
%{_mandir}/man3/pam*.3*

