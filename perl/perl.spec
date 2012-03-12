%define		abi		5.14.0

%define		perlthread	-thread-multi

%define		perl_archlib	%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}
%define		perl_privlib	%{_datadir}/perl5/%{version}
%define		perl_sitearch	%{_usr}/local/lib/perl5/%{abi}/%{_target_platform}%{perlthread}
%define		perl_sitelib	%{_usr}/local/share/perl5
%define		perl_vendorarch	%{_libdir}/perl5/vendor_perl/%{abi}/%{_target_platform}%{perlthread}
%define		perl_vendorlib	%{_datadir}/perl5/vendor_perl

%define		__perl			%{_builddir}/perl-%{version}/runperl
%define		__perl_provides		%{__perl} %{SOURCE2}

%bcond_without	gdbm	# build without the GDBM_File module

Summary:	Practical Extraction and Report Language (Perl)
Name:		perl
Version:	5.14.2
Release:	3
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	3306fbaf976dcebdcd49b2ac0be00eb9
Source2:	%{name}.prov
Source3:	%{name}-modules
Patch0:		%{name}-errno_h-parsing.patch
Patch1:		%{name}-soname.patch
Patch2:		%{name}-test-noproc.patch
Patch3:		%{name}-write-permissions.patch
URL:		http://dev.perl.org/perl5/
%{?with_gdbm:BuildRequires:	gdbm-devel}
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-doc-reference = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	perldoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# extract module version from source
%define		perl_modver()		%([ -f %{SOURCE3} ] && awk -vp=%1 '$1 == p{print $3}' %{SOURCE3} || echo ERROR)
%define		perl_modversion()	%([ -f %{SOURCE3} ] && awk -vp=%1 '$1 == p{m=$1; gsub(/::/, "-", m); printf("perl-%s = %s\\n", m, $3)}END{if (!m) printf("# Error looking up [%s]\\n", p)}' %{SOURCE3} || echo ERROR)

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing
reports based on that information. It's also a good language for many
system management tasks. The language is intended to be practical
(easy to use, efficient, complete) rather than beautiful (tiny,
elegant, minimal).

%package libs
Summary:	Shared Perl library
Group:		Libraries

%description libs
Shared Perl library.

%package base
Summary:	Base Perl components for a minimal installation
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{perl_vendorarch}
Requires:	%{perl_vendorlib}
Provides:	perl(largefiles)
Provides:	%perl_modversion File::Compare
Provides:	%perl_modversion File::Spec
Provides:	%perl_modversion File::Temp
Provides:	%perl_modversion IO
Provides:	%perl_modversion PerlIO::via::QuotedPrint
Provides:	%perl_modversion Safe
Provides:	%perl_modversion Socket
Provides:	%perl_modversion Tie::File

%description base
Base components, files, core modules, etc. -- a minimal usable Perl
installation. You are encouraged to install a full Perl (the perl
package) whenever possible.

%package devel
Summary:	Perl development files
Group:		Development/Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-tools-pod = %{epoch}:%{version}-%{release}
Provides:	%perl_modversion CPAN
Provides:	%perl_modversion Devel::DProf
Provides:	%perl_modversion Devel::PPPort
Provides:	%perl_modversion Devel::Peek
Provides:	%perl_modversion ExtUtils::Embed
Provides:	%perl_modversion ExtUtils::MakeMaker
Provides:	%perl_modversion Module::Build

%description devel
Components required for developing applications which embed a Perl
interpreter and compiling Perl modules.

%package doc-pod
Summary:	Perl documentation in POD format
Group:		Documentation
Requires:	perldoc

%description doc-pod
Practical Extraction and Report Language - POD docs.

%package doc-reference
Summary:	Perl reference documentation
Group:		Documentation

%description doc-reference
Reference documentation for the Practical Extraction and Report
Language and it's interpreter in the man(1) format.

%package modules
Summary:	Modules from the core Perl distribution
Group:		Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Provides:	%perl_modversion Attribute::Handlers
Provides:	%perl_modversion CGI
Provides:	%perl_modversion Digest
Provides:	%perl_modversion Digest::MD5
Provides:	%perl_modversion Filter::Simple
Provides:	%perl_modversion FindBin
Provides:	%perl_modversion I18N::LangTags
Provides:	%perl_modversion IPC::SysV
Provides:	%perl_modversion Locale::Maketext
Provides:	%perl_modversion MIME::Base64
Provides:	%perl_modversion Math::BigInt
Provides:	%perl_modversion Math::BigRat
Provides:	%perl_modversion Math::Trig
Provides:	%perl_modversion Memoize
Provides:	%perl_modversion NEXT
Provides:	%perl_modversion Pod::LaTeX
Provides:	%perl_modversion Pod::Parser
Provides:	%perl_modversion Storable
Provides:	%perl_modversion Term::ANSIColor
Provides:	%perl_modversion Term::Cap
Provides:	%perl_modversion Test
Provides:	%perl_modversion Test::Harness
Provides:	%perl_modversion Test::Simple
Provides:	%perl_modversion Text::Balanced
Provides:	%perl_modversion Text::ParseWords
Provides:	%perl_modversion Text::Soundex
Provides:	%perl_modversion Time::HiRes
Provides:	%perl_modversion UNIVERSAL
Provides:	%perl_modversion Unicode::Collate
Provides:	%perl_modversion Unicode::Normalize
Provides:	%perl_modversion libnet
Provides:	%perl_modversion version

%description modules
Practical Extraction and Report Language - modules from the core
distribution.

%package perldoc
Summary:	perldoc - Look up Perl documentation in pod format
Group:		Development/Tools
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-tools-pod = %{epoch}:%{version}-%{release}
Provides:	perldoc = 3.14_02@%{version}

%description perldoc
perldoc looks up a piece of documentation in .pod format that is
embedded in the Perl installation tree or in a Perl script, and
displays it via "pod2man | nroff -man | $PAGER". This is primarily
used for the documentation for the Perl library modules.

%package tools
Summary:	Various tools from the core Perl distribution
Group:		Applications
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description tools
Various tools from the core Perl distribution:
a2p		- Awk to Perl translator
find2perl	- translate find command lines to Perl code
psed, s2p	- a stream editor
and others.

%package tools-devel
Summary:	Developer's tools from the core Perl distribution
Group:		Development/Tools
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description tools-devel
Various tools from the core Perl distribution:
c2ph, pstruct	- Dump C structures as generated from C<cc -g -S> stabs
dprofpp		- display Perl profile data
h2ph		- convert .h C header files to .ph Perl header files
h2xs		- convert .h C header files to Perl extensions
perlcc		- generate executables from Perl programs
perlivp		- Perl Installation Verification Procedure
pl2pm		- Rough tool to translate Perl4 .pl files to Perl5 .pm modules.
splain		- force verbose warning diagnostics

%package tools-pod
Summary:	Tools for manipulating files in the POD format
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description tools-pod
Tools for manipulating files in the POD (Plain Old Documentation)
format:
pod2html	- convert .pod files to .html files
pod2latex	- convert pod documentation to LaTeX format
pod2man		- convert POD data to formatted *roff input
pod2text	- convert POD data to formatted ASCII text
pod2usage	- print usage messages from embedded pod docs in files
podchecker	- check the syntax of POD format documentation files
podselect	- print selected sections of pod documentation

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
sh Configure \
	-Darchname=%{_target_platform}					\
	-Dcc="%{__cc}"							\
	-Dcccdlflags='-fPIC'						\
	-Dccdlflags='-rdynamic' 					\
	-Dlddlflags="-shared %{rpmldflags}"				\
	-Dldflags="%{rpmldflags}"					\
	-Dldlibpthname=none						\
	-Dlibpth="%{_libdir} /%{_lib}"					\
	-Dlibswanted="dl m c crypt %{?with_gdbm:gdbm}"			\
	-Dman1dir=%{_mandir}/man1 -Dman1ext=1				\
	-Dman3dir=%{_mandir}/man3 -Dman3ext=3perl			\
	-Doptimize="%{rpmcflags}"					\
	-Dprefix=%{_prefix} -Dvendorprefix=%{_prefix} -Dsiteprefix=%{_usr}/local \
	-Dprivlib=%{perl_privlib} -Darchlib=%{perl_archlib}		\
	-Dsitelib=%{perl_sitelib} -Dsitearch=%{perl_sitearch}		\
	-Dsiteman1dir=%{_usr}/local/man/man1 -Dsiteman1ext=1p		\
	-Dsiteman3dir=%{_usr}/local/man/man3 -Dsiteman3ext=3pm		\
	-Duselargefiles							\
	-Duseshrplib							\
	-Dusethreads							\
	-Dvendorlib=%{perl_vendorlib} -Dvendorarch=%{perl_vendorarch}	\
	-Dvendorman1dir=%{_mandir}/man1 -Dvendorman1ext=1p		\
	-Dvendorman3dir=%{_mandir}/man3 -Dvendorman3ext=3pm		\
	-UDEBUGGING							\
	-Ui_db								\
	%{!?with_gdbm: -Ui_dbm -Ui_gdbm -Ui_ndbm}			\
	%{?with_gdbm: -Ui_dbm -Di_gdbm -Ui_ndbm}			\
	-des
%{__make} \
	LIBPERL_SONAME=libperl.so.%{abi} \
	LDDLFLAGS="%{rpmcflags} -shared"

cat > runperl <<'EOF'
#!/bin/sh
LD_PRELOAD="%{_builddir}/%{name}-%{version}/libperl.so.%{abi}" \
PERL5LIB="%{buildroot}%{perl_privlib}:%{buildroot}%{perl_archlib}" \
exec %{buildroot}%{_bindir}/perl ${1:+"$@"}
EOF
chmod a+x runperl

%install
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT
	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	install -d $RPM_BUILD_ROOT%{_mandir}/{ja,ko,zh_CN,zh_TW}/man1

	install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Encode

	## use symlinks instead of hardlinks
	%{__ln_s} -f perl%{version} $RPM_BUILD_ROOT%{_bindir}/perl
	%{__ln_s} -f c2ph $RPM_BUILD_ROOT%{_bindir}/pstruct
	%{__ln_s} -f psed $RPM_BUILD_ROOT%{_bindir}/s2p

	## Fix library version
	%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so
	mv $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so.%{abi} $RPM_BUILD_ROOT%{_libdir}
	%{__ln_s} ../../../../libperl.so.%{abi} $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so.%{abi}
	%{__ln_s} libperl.so.%{abi} $RPM_BUILD_ROOT%{_libdir}/libperl.so

	# installed as non-executable - let rpm generate deps
	chmod 755 $RPM_BUILD_ROOT%{_libdir}/libperl.so.%{abi}

	## Fix Config.pm: remove buildroot path and change man pages extensions
	%{__perl} -pi -e 's,%{buildroot}/*,/,g'			$RPM_BUILD_ROOT%{perl_archlib}/Config.pm
	%{__perl} -pi -e "s,^man1ext='1',man1ext='1p',"		$RPM_BUILD_ROOT%{perl_archlib}/Config_heavy.pl
	%{__perl} -pi -e "s,^man3ext='3perl',man3ext='3pm',"	$RPM_BUILD_ROOT%{perl_archlib}/Config_heavy.pl

	## Generate the *.ph files
	owd=$(pwd)
	cd /usr/include
	H2PH=$RPM_BUILD_ROOT%{_bindir}/h2ph
	PHDIR=$RPM_BUILD_ROOT%{perl_archlib}
	WANTED='
		syscall.h
		syslog.h
		termios.h
		wait.h
		asm/termios.h
		sys/ioctl.h
		sys/socket.h
		sys/syscall.h
		sys/time.h
		linux/posix_types.h
		linux/stddef.h
	'
	# why it returns non-zero???
	%{__perl} $H2PH -a -d $PHDIR $WANTED || :
	cd "$owd"

	## remove man pages for other operating systems
	%{__rm}	$RPM_BUILD_ROOT%{_mandir}/man1/perl{aix,amiga,beos,bs2000,ce,cygwin,dgux,dos}* \
		$RPM_BUILD_ROOT%{_mandir}/man1/perl{freebsd,hpux,macos,mpeix,os2,os390}* \
		$RPM_BUILD_ROOT%{_mandir}/man1/perl{qnx,solaris,vmesa,vms,vos,win32}*

	## symlink perldelta.1.gz -> perlFOOdelta.1.gz
	[ -e $RPM_BUILD_ROOT%{_mandir}/man1/perl%(echo %{version} | tr -d .)delta.1 ] || exit 1
	rm $RPM_BUILD_ROOT%{_mandir}/man1/perldelta.1
	echo ".so perl%(echo %{version} | tr -d .)delta.1" >$RPM_BUILD_ROOT%{_mandir}/man1/perldelta.1

	## These File::Spec submodules are for non-Unix systems
	rm $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::{Epoc,Mac,OS2,VMS,Win32}.3perl*

	## We already have these *.pod files as man pages
	%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/{Encode,Test,Net,Locale{,/Maketext}}/*.pod
	rm $RPM_BUILD_ROOT%{perl_privlib}/pod/a2p.pod
	%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/*.pod
	%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/*.pod

	## this object file looks unused; why is it there?

	install -d doc-base/{Getopt/Long,Switch} \
		doc-devel/ExtUtils \
		doc-modules/{Attribute/Handlers,Filter/Simple,I18N/LangTags,Locale/{Codes,Maketext},Memoize,NEXT} \
		doc-modules/{Net/Ping,Term/ANSIColor,Test/Simple,Text/{Balanced,TabsWrap},Unicode/Collate,unicore}

	# needed only for tests
	%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/Unicode/Collate/keys.txt
	# cpan tools, we use rpm instead of cpan for managing packages (some search tool would be nice to have but...)
	%{__rm} $RPM_BUILD_ROOT%{_bindir}/cpan*
	%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/cpan*
	# others
	%{__rm} $RPM_BUILD_ROOT%{_bindir}/config_data
	%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/config_data*
	%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/XS::Typemap*

	owd=$(pwd)

	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perlcn.* $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perljp.* $RPM_BUILD_ROOT%{_mandir}/ja/man1
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perlko.* $RPM_BUILD_ROOT%{_mandir}/ko/man1
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perltw.* $RPM_BUILD_ROOT%{_mandir}/zh_TW/man1

	# `perl -MExtUtils::Embed -e ldopts` includes -Wl,--as-needed
	# which is then forced upon anyone embedding perl.
	sed -i -e 's#^\(ld.*=.*\)-Wl,--as-needed\(.*\)#\1 \2#g' $RPM_BUILD_ROOT%{perl_archlib}/Config*.pl

	rm -rf $RPM_BUILD_ROOT%{_mandir}/README.perl-non-english-man-pages

	touch installed.stamp
fi

# update and check perl-modules file
echo '# Module versions from Perl %{version} distribution.' > perl-modules
for m in $(awk '!/^#/ && !/^$/{print $1}' %{SOURCE3}); do
	case $m in
	Devel::DProf)
#		+ perl -ilib -MDevel::DProf -e print 'Devel-DProf = ',$Devel::DProf::VERSION
#		DProf: run perl with -d to use DProf.
#		Compilation failed in require.
#		BEGIN failed--compilation aborted.
		v=$(%{__perl} -e 'do "Devel/DProf.pm"; print $Devel::DProf::VERSION')
		;;
	libnet)
		v=$(awk '/^libnet /{print $2; exit}' cpan/libnet/Changes)
		;;
	*)
		v=$(%{__perl} -M$m -e "print $m->VERSION" )
		;;
	esac
	echo "$m = $v" >> perl-modules
done

egrep -v '^([ 	]*$|[;#])' %{SOURCE3} > .mods1
egrep -v '^([ 	]*$|[;#])' perl-modules > .mods2
if ! cmp -s .mods1 .mods2; then
	: %{SOURCE3} outdated with $(pwd)/perl-modules
	exit 1
fi

%check
%{__make} test -j1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/perlthanks

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libperl.so.%{abi}

%files base
%defattr(644,root,root,755)
%doc doc-base/*
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%{_mandir}/man1/perl.1*

%dir %{perl_archlib}/CORE
%attr(755,root,root) %{perl_archlib}/CORE/libperl.so.%{abi}

%dir %{_datadir}/perl5
%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%dir %{perl_archlib}
%dir %{perl_archlib}/auto
%dir %{perl_privlib}

## pragmas
%{perl_archlib}/lib.pm
%{perl_privlib}/autodie*
%{perl_privlib}/base.pm
%{perl_privlib}/constant.pm
%{perl_privlib}/diagnostics.pm
%{perl_privlib}/feature.pm
%{perl_privlib}/fields.pm
%{perl_privlib}/integer.pm
%{perl_privlib}/overload*
%{perl_privlib}/parent.pm
%{perl_privlib}/sort.pm
%{perl_privlib}/strict.pm
%{perl_privlib}/subs.pm
%{perl_privlib}/vars.pm
%{perl_privlib}/warnings*
%{_mandir}/man3/autodie*
%{_mandir}/man3/base.*
%{_mandir}/man3/constant.*
%{_mandir}/man3/diagnostics.*
%{_mandir}/man3/feature.*
%{_mandir}/man3/fields.*
%{_mandir}/man3/integer.*
%{_mandir}/man3/lib.*
%{_mandir}/man3/overload*
%{_mandir}/man3/parent.*
%{_mandir}/man3/sort.*
%{_mandir}/man3/strict.*
%{_mandir}/man3/subs.*
%{_mandir}/man3/vars.*
%{_mandir}/man3/warnings*

## arch-_IN_dependent modules
%dir %{perl_privlib}/Class
%{perl_privlib}/Auto*
%{perl_privlib}/Carp*
%{perl_privlib}/Class/Struct*
%{perl_privlib}/English*
%{perl_privlib}/Exporter*
%{perl_privlib}/Getopt*
%{perl_privlib}/IPC
%{perl_privlib}/Safe*
%{perl_privlib}/SelectSaver.pm
%{perl_privlib}/Symbol.pm
%{perl_privlib}/Tie
%{perl_privlib}/XSLoader*
%{_mandir}/man3/Auto*
%{_mandir}/man3/Carp*
%{_mandir}/man3/Class::Struct*
%{_mandir}/man3/English*
%{_mandir}/man3/Exporter*
%{_mandir}/man3/Getopt*
%{_mandir}/man3/IPC::Cmd*
%{_mandir}/man3/IPC::Open*
%{_mandir}/man3/Safe*
%{_mandir}/man3/SelectSaver.*
%{_mandir}/man3/Symbol.*
%{_mandir}/man3/Tie::*
%{_mandir}/man3/XSLoader*

## arch-dependent modules
%{_mandir}/man3/Config.*
%{_mandir}/man3/DynaLoader*
%{_mandir}/man3/Errno*
%{perl_archlib}/Config*
%{perl_archlib}/DynaLoader*
%{perl_archlib}/Errno*
%{perl_archlib}/Tie

%attr(755,root,root) %{perl_archlib}/auto/Cwd/*.so
%dir %{perl_archlib}/auto/Cwd
%{perl_archlib}/Cwd.*
%{_mandir}/man3/Cwd.*

%{perl_archlib}/Fcntl.*
%dir %{perl_archlib}/auto/Fcntl
%attr(755,root,root) %{perl_archlib}/auto/Fcntl/*.so
%{_mandir}/man3/Fcntl.*

%{perl_privlib}/File*
%{perl_archlib}/File
%dir %{perl_archlib}/auto/File
%dir %{perl_archlib}/auto/File/*/
%attr(755,root,root) %{perl_archlib}/auto/File/*/*.so
%{_mandir}/man3/File*

%{perl_privlib}/IO
%{perl_archlib}/IO*
%dir %{perl_archlib}/auto/IO
%attr(755,root,root) %{perl_archlib}/auto/IO/*.so
%{_mandir}/man3/IO*

%{perl_archlib}/Opcode.*
%dir %{perl_archlib}/auto/Opcode
%attr(755,root,root) %{perl_archlib}/auto/Opcode/*.so
%{_mandir}/man3/Opcode.*

%{perl_privlib}/PerlIO*
%{perl_archlib}/PerlIO
%dir %{perl_archlib}/auto/PerlIO
%dir %{perl_archlib}/auto/PerlIO/*/
%attr(755,root,root) %{perl_archlib}/auto/PerlIO/*/*.so
%{_mandir}/man3/PerlIO*

%{perl_archlib}/POSIX*
%dir %{perl_archlib}/auto/POSIX
%attr(755,root,root) %{perl_archlib}/auto/POSIX/*.so
%{perl_archlib}/auto/POSIX/*.al
%{perl_archlib}/auto/POSIX/*.ix
%{perl_archlib}/auto/POSIX/SigAction
%{perl_archlib}/auto/POSIX/SigRt
%{_mandir}/man3/POSIX.*

%{perl_archlib}/Socket.*
%dir %{perl_archlib}/auto/Socket
%attr(755,root,root) %{perl_archlib}/auto/Socket/*.so
%{_mandir}/man3/Socket.*

%files devel
%defattr(644,root,root,755)
%doc doc-devel/*
%attr(755,root,root) %{_libdir}/libperl.so
%attr(755,root,root) %{perl_archlib}/auto/B/*.so
%attr(755,root,root) %{perl_archlib}/auto/Devel/*/*.so

%dir %{perl_archlib}/auto/B
%dir %{perl_archlib}/auto/Devel
%dir %{perl_archlib}/auto/Devel/*/
%dir %{perl_privlib}/App

%{perl_archlib}/B
%{perl_archlib}/B.pm
%{perl_archlib}/CORE/*.h
%{perl_archlib}/Devel
%{perl_archlib}/O.*
%{perl_privlib}/App/Cpan.pm
%{perl_privlib}/B
%{perl_privlib}/CPAN*
%{perl_privlib}/DB.*
%{perl_privlib}/Devel
%{perl_privlib}/ExtUtils
%{perl_privlib}/Module/Build*
%{perl_privlib}/inc
%{perl_privlib}/vmsish.pm
%{_mandir}/man3/App::Cpan*
%{_mandir}/man3/B[.:]*
%{_mandir}/man3/CORE*
%{_mandir}/man3/CPAN*
%{_mandir}/man3/DB.*
%{_mandir}/man3/Devel::*
%{_mandir}/man3/ExtUtils*
%{_mandir}/man3/Module::Build*
%{_mandir}/man3/O.*
%{_mandir}/man3/inc::latest*
%{_mandir}/man3/vmsish.*

%files doc-pod
%defattr(644,root,root,755)
%{perl_privlib}/pod/perl.pod
%{perl_privlib}/pod/perl[5abceghijklmnopqrstuvwx]*.pod
%{perl_privlib}/pod/perld[!i]*.pod
%{perl_privlib}/pod/perlf[!au]*.pod

%files doc-reference
%defattr(644,root,root,755)
%{_mandir}/man1/perl[5aefghlmnoprstuvwx]*
%{_mandir}/man1/perlbo*
%{_mandir}/man1/perlcall.*
%{_mandir}/man1/perlcheat.*
%{_mandir}/man1/perlclib.*
%{_mandir}/man1/perlcommunity.*
%{_mandir}/man1/perlcompile.*
%{_mandir}/man1/perld[!o]*
%{_mandir}/man1/perli[!v]*

%lang(zh_CN) %{_mandir}/zh_CN/man1/perlcn.*
%lang(ja) %{_mandir}/ja/man1/perljp.*
%lang(ko) %{_mandir}/ko/man1/perlko.*
%lang(zh_TW) %{_mandir}/zh_TW/man1/perltw.*

%files modules
%defattr(644,root,root,755)
%doc doc-modules/*

%{perl_privlib}/unicore

## pragmas
%{perl_privlib}/autouse.pm
%{perl_privlib}/big*.pm
%{perl_privlib}/blib.pm
%{perl_privlib}/bytes.pm
%{perl_privlib}/charnames.pm
%{perl_privlib}/deprecate*.pm
%{perl_privlib}/encoding
%{perl_privlib}/filetest.pm
%{perl_privlib}/if.pm
%{perl_privlib}/less.pm
%{perl_privlib}/locale.pm
%{perl_privlib}/open.pm
%{perl_privlib}/sigtrap.pm
%{perl_privlib}/utf8.pm
%{perl_privlib}/version.pm
%{_mandir}/man3/autouse.*
%{_mandir}/man3/big*
%{_mandir}/man3/blib.*
%{_mandir}/man3/bytes.*
%{_mandir}/man3/charnames.*
%{_mandir}/man3/deprecate*
%{_mandir}/man3/encoding::*
%{_mandir}/man3/filetest.*
%{_mandir}/man3/if.*
%{_mandir}/man3/less.*
%{_mandir}/man3/locale.*
%{_mandir}/man3/open.*
%{_mandir}/man3/sigtrap.*
%{_mandir}/man3/utf8.*
%{_mandir}/man3/version*

%attr(755,root,root) %{perl_archlib}/auto/attributes/*.so
%dir %{perl_archlib}/auto/attributes
%{perl_archlib}/attributes.pm
%{_mandir}/man3/attributes.*

%attr(755,root,root) %{perl_archlib}/auto/mro/*.so
%attr(755,root,root) %{perl_archlib}/auto/re/*.so
%dir %attr(755,root,root) %{perl_archlib}/auto/mro
%dir %{perl_archlib}/auto/re
%{perl_archlib}/mro.pm
%{perl_archlib}/ops.pm
%{perl_archlib}/re.pm
%{_mandir}/man3/mro.*
%{_mandir}/man3/ops.*
%{_mandir}/man3/re.*

%attr(755,root,root) %{perl_archlib}/auto/threads/*.so
%attr(755,root,root) %{perl_archlib}/auto/threads/shared/*.so
%dir %{perl_archlib}/auto/threads
%dir %{perl_archlib}/auto/threads/shared
%{perl_archlib}/threads*
%{_mandir}/man3/t*

## old *.pl files
%{perl_privlib}/*.pl

## *.ph files (could be made a separate package, but an autohelper's support is needed)
%{perl_archlib}/*.ph
%{perl_archlib}/asm
%{perl_archlib}/asm-generic
%{perl_archlib}/bits
%{perl_archlib}/gnu
%{perl_archlib}/linux
%{perl_archlib}/sys

%attr(755,root,root) %{perl_archlib}/auto/Tie/Hash/NamedCapture/NamedCapture.so
%dir %{perl_archlib}/auto/Tie
%dir %{perl_archlib}/auto/Tie/Hash
%dir %{perl_archlib}/auto/Tie/Hash/NamedCapture

%attr(755,root,root) %{perl_archlib}/auto/Compress/Raw/*/*.so
%dir %{perl_archlib}/auto/Compress
%dir %{perl_archlib}/auto/Compress/Raw
%dir %{perl_archlib}/auto/Compress/Raw/*/
%{perl_archlib}/Compress
%{perl_archlib}/auto/Compress/Raw/*/*.ix
%{perl_privlib}/Compress
%{_mandir}/man3/Compress*

%attr(755,root,root) %{perl_archlib}/auto/Data/Dumper/*.so
%dir %{perl_archlib}/auto/Data
%dir %{perl_archlib}/auto/Data/Dumper
%{perl_archlib}/Data
%{_mandir}/man3/Data*

%attr(755,root,root) %{perl_archlib}/auto/Digest/*/*.so
%dir %{perl_archlib}/auto/Digest
%dir %{perl_archlib}/auto/Digest/*/
%{perl_archlib}/Digest
%{perl_privlib}/Digest*
%{_mandir}/man3/Digest*

%{perl_privlib}/DBM_Filter*
%{_mandir}/man3/DBM_Filter*

%attr(755,root,root) %{_bindir}/enc2xs
%attr(755,root,root) %{_bindir}/piconv
%{perl_privlib}/Encode
%{perl_archlib}/Encode*
%{perl_archlib}/encoding.pm
%dir %{perl_archlib}/auto/Encode
%dir %{perl_archlib}/auto/Encode/*/
%dir %{perl_vendorlib}/Encode
%attr(755,root,root) %{perl_archlib}/auto/Encode/*/*.so
%{_mandir}/man1/enc2xs.*
%{_mandir}/man1/piconv.*
%{_mandir}/man3/Encode*
%{_mandir}/man3/encoding.*

%attr(755,root,root) %{perl_archlib}/auto/Filter/Util/Call/*.so
%dir %{perl_archlib}/auto/Filter
%dir %{perl_archlib}/auto/Filter/Util
%dir %{perl_archlib}/auto/Filter/Util/Call
%{perl_archlib}/Filter
%{perl_privlib}/Filter
%{_mandir}/man3/Filter*

%if %{with gdbm}
%{perl_archlib}/GDBM_File.*
%dir %{perl_archlib}/auto/GDBM_File
%attr(755,root,root) %{perl_archlib}/auto/GDBM_File/*.so
%{_mandir}/man3/GDBM_File.*
%endif

%attr(755,root,root) %{perl_archlib}/auto/Hash/*/*.so
%attr(755,root,root) %{perl_archlib}/auto/Hash/*/*/*.so
%dir %{perl_archlib}/auto/Hash
%dir %{perl_archlib}/auto/Hash/*/
%dir %{perl_archlib}/auto/Hash/*/FieldHash
%{perl_archlib}/Hash
%{_mandir}/man3/Hash::*

%attr(755,root,root) %{perl_archlib}/auto/I18N/*/*.so
%dir %{perl_archlib}/auto/I18N
%dir %{perl_archlib}/auto/I18N/*/
%{perl_archlib}/I18N
%{perl_privlib}/I18N
%{_mandir}/man3/I18N::*

%attr(755,root,root) %{perl_archlib}/auto/IPC/*/*.so
%dir %{perl_archlib}/auto/IPC
%dir %{perl_archlib}/auto/IPC/*/
%{perl_archlib}/IPC
%{_mandir}/man3/IPC::[MS]*

%attr(755,root,root) %{perl_archlib}/auto/List/*/*.so
%dir %{perl_archlib}/auto/List
%dir %{perl_archlib}/auto/List/*/
%{perl_archlib}/List
%{_mandir}/man3/List::*

%attr(755,root,root) %{perl_archlib}/auto/Math/*/*/*.so
%dir %{perl_archlib}/auto/Math
%dir %{perl_archlib}/auto/Math/*/
%dir %{perl_archlib}/auto/Math/*/*/
%{perl_archlib}/Math
%{perl_privlib}/Math
%{_mandir}/man3/Math::*

%attr(755,root,root) %{perl_archlib}/auto/MIME/Base64/*.so
%dir %{perl_archlib}/auto/MIME
%dir %{perl_archlib}/auto/MIME/Base64
%{perl_archlib}/MIME
%{_mandir}/man3/MIME::*

%attr(755,root,root) %{perl_archlib}/auto/SDBM_File/*.so
%dir %{perl_archlib}/auto/SDBM_File
%{perl_archlib}/SDBM_File.*
%{_mandir}/man3/SDBM_File.*

%attr(755,root,root) %{perl_archlib}/auto/Storable/*.so
%dir %{perl_archlib}/auto/Storable
%{perl_archlib}/Storable.*
%{_mandir}/man3/Storable.*

%attr(755,root,root) %{perl_archlib}/auto/Sys/*/*.so
%dir %{perl_archlib}/auto/Sys
%dir %{perl_archlib}/auto/Sys/*/
%{perl_archlib}/Sys
%{_mandir}/man3/Sys::*

%attr(755,root,root) %{perl_archlib}/auto/Text/Soundex/*.so
%dir %{perl_archlib}/auto/Text
%dir %{perl_archlib}/auto/Text/Soundex
%{perl_archlib}/Text

%attr(755,root,root) %{perl_archlib}/auto/Time/*/*.so
%dir %{perl_archlib}/auto/Time
%dir %{perl_archlib}/auto/Time/*/
%{perl_archlib}/Time
%{perl_privlib}/Time
%{_mandir}/man3/Time::*

%attr(755,root,root) %{perl_archlib}/auto/Unicode/*/*.so
%dir %{perl_archlib}/auto/Unicode
%dir %{perl_archlib}/auto/Unicode/*
%dir %{perl_privlib}/Unicode
%{perl_archlib}/Unicode
%{perl_privlib}/Unicode/*.pm
%{perl_privlib}/Unicode/Collate
%{_mandir}/man3/Unicode::*

%dir %{perl_privlib}/HTTP
%dir %{perl_privlib}/Module
%dir %{perl_privlib}/Net
%dir %{perl_privlib}/Perl
%dir %{perl_privlib}/Version
%{perl_archlib}/Scalar
%{perl_privlib}/AnyDBM*
%{perl_privlib}/App
%{perl_privlib}/Archive*
%{perl_privlib}/Attribute
%{perl_privlib}/Benchmark*
%{perl_privlib}/CGI*
%{perl_privlib}/Config
%{perl_privlib}/DirHandle*
%{perl_privlib}/Dumpvalue.*
%{perl_privlib}/Env.*
%{perl_privlib}/Fatal.*
%{perl_privlib}/FindBin.*
%{perl_privlib}/HTTP/Tiny.pm
%{perl_privlib}/IPC
%{perl_privlib}/Locale
%{perl_privlib}/Log
%{perl_privlib}/Memoize*
%{perl_privlib}/Module/[CLMP]*
%{perl_privlib}/NEXT.pm
%{perl_privlib}/Net/*.pm
%{perl_privlib}/Net/FTP
%{perl_privlib}/Object
%{perl_privlib}/Package
%{perl_privlib}/Params
%{perl_privlib}/Parse
%{perl_privlib}/Perl/OSType.pm
%{perl_privlib}/Pod
%{perl_privlib}/Search
%{perl_privlib}/SelfLoader.*
%{perl_privlib}/Shell.*
%{perl_privlib}/TAP
%{perl_privlib}/Term
%{perl_privlib}/Test*
%{perl_privlib}/Text
%{perl_privlib}/Thread*
%{perl_privlib}/UNIVERSAL.*
%{perl_privlib}/User
%{perl_privlib}/Version/Requirements.pm
%{_mandir}/man3/AnyDBM*
%{_mandir}/man3/App::Prove*
%{_mandir}/man3/Archive*
%{_mandir}/man3/Attribute*
%{_mandir}/man3/Benchmark*
%{_mandir}/man3/CGI*
%{_mandir}/man3/Config::*
%{_mandir}/man3/DirHandle*
%{_mandir}/man3/Dumpvalue.*
%{_mandir}/man3/Env.*
%{_mandir}/man3/Fatal.*
%{_mandir}/man3/FindBin.*
%{_mandir}/man3/HTTP::Tiny.*
%{_mandir}/man3/Locale::*
%{_mandir}/man3/Log::*
%{_mandir}/man3/Memoize*
%{_mandir}/man3/Module::[CLMP]*
%{_mandir}/man3/NEXT*
%{_mandir}/man3/Net::*
%{_mandir}/man3/Object::*
%{_mandir}/man3/Package::*
%{_mandir}/man3/Params::*
%{_mandir}/man3/Parse::CPAN::Meta*
%{_mandir}/man3/Perl::OSType.*
%{_mandir}/man3/Pod::*
%{_mandir}/man3/Scalar::*
%{_mandir}/man3/Search::*
%{_mandir}/man3/SelfLoader.*
%{_mandir}/man3/Shell.*
%{_mandir}/man3/TAP::*
%{_mandir}/man3/Term::*
%{_mandir}/man3/Test*
%{_mandir}/man3/Text::*
%{_mandir}/man3/Thread*
%{_mandir}/man3/UNIVERSAL.*
%{_mandir}/man3/User::*
%{_mandir}/man3/Version::Requirements.*

%attr(755,root,root) %{_bindir}/json_pp
%{perl_privlib}/JSON
%{_mandir}/man1/json_pp.1*
%{_mandir}/man3/JSON::PP.*
%{_mandir}/man3/JSON::PP::Boolean.*

%files perldoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldoc
%dir %{perl_privlib}/pod
%{perl_privlib}/pod/perldiag.pod
%{perl_privlib}/pod/perlfaq*.pod
%{perl_privlib}/pod/perlfunc.pod
%{_mandir}/man1/perldoc.*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2p
%attr(755,root,root) %{_bindir}/corelist
%attr(755,root,root) %{_bindir}/find2perl
%attr(755,root,root) %{_bindir}/instmodsh
%attr(755,root,root) %{_bindir}/libnetcfg
%attr(755,root,root) %{_bindir}/psed
%attr(755,root,root) %{_bindir}/ptar
%attr(755,root,root) %{_bindir}/ptardiff
%attr(755,root,root) %{_bindir}/ptargrep
%attr(755,root,root) %{_bindir}/s2p
%attr(755,root,root) %{_bindir}/shasum
%{_mandir}/man1/a2p.*
%{_mandir}/man1/corelist.*
%{_mandir}/man1/find2perl.*
%{_mandir}/man1/instmodsh.*
%{_mandir}/man1/libnetcfg.*
%{_mandir}/man1/psed.*
%{_mandir}/man1/ptar.*
%{_mandir}/man1/ptardiff.*
%{_mandir}/man1/ptargrep.*
%{_mandir}/man1/s2p.*
%{_mandir}/man1/shasum.*

%files tools-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/c2ph
%attr(755,root,root) %{_bindir}/dprofpp
%attr(755,root,root) %{_bindir}/h2ph
%attr(755,root,root) %{_bindir}/h2xs
%attr(755,root,root) %{_bindir}/perlbug
%attr(755,root,root) %{_bindir}/perlivp
%attr(755,root,root) %{_bindir}/pl2pm
%attr(755,root,root) %{_bindir}/prove
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/splain
%attr(755,root,root) %{_bindir}/xsubpp
%{_mandir}/man1/c2ph.*
%{_mandir}/man1/dprofpp.*
%{_mandir}/man1/h2ph.*
%{_mandir}/man1/h2xs.*
%{_mandir}/man1/perlbug.*
%{_mandir}/man1/perlivp.*
%{_mandir}/man1/pl2pm.*
%{_mandir}/man1/prove.*
%{_mandir}/man1/pstruct.*
%{_mandir}/man1/splain.*
%{_mandir}/man1/xsubpp.*

%files tools-pod
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pod*
%{_mandir}/man1/pod*

