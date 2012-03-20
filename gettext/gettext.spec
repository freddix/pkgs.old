Summary:	Utilties for program national language support
Name:		gettext
Version:	0.18.1.1
Release:	3
License:	LGPL (runtime), GPL (tools)
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
# Source0-md5:	3dd55b952826d2b32f51308f2f91aa89
Patch0:		%{name}-non_interactive_gettextize.patch
URL:		http://www.gnu.org/software/gettext/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildConflicts:	libcroco-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU gettext package provides a set of tools and documentation for
producing multi-lingual messages in programs. Tools include a set of
conventions about how programs should be written to support message
catalogs, a directory and file naming organization for the message
catalogs, a runtime library which supports the retrieval of translated
messages, and stand-alone programs for handling the translatable and
the already translated strings. Gettext provides an easy to use
library and tools for creating, using, and modifying natural language
catalogs and is a powerful and simple method for internationalizing
programs.

%package devel
Summary:	Utilties for program national language support
License:	GPL
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	iconv

%description devel
The gettext library provides an easy to use library and tools for
creating, using, and modifying natural language catalogs. It is a
powerfull and simple method for internationalizing programs.

%package libs
Summary:	GNU gettext library
License:	LGPL
Group:		Libraries

%description libs
GNU gettext library.

%package -n libasprintf
Summary:	GNU libasprintf - automatic formatted output to strings in C++
License:	LGPL
Group:		Libraries

%description -n libasprintf
This package makes the C formatted output routines (`fprintf' et al.)
usable in C++ programs, for use with the `<string>' strings and the
`<iostream>' streams.

%package -n libasprintf-devel
Summary:	Header file and documentation for libasprintf
License:	LGPL
Group:		Development/Libraries
Requires:	libasprintf = %{version}-%{release}

%description -n libasprintf-devel
Header file and documentation for libasprintf.

%package autopoint
Summary:	gettextize replacement
License:	GPL
Group:		Development/Tools
Requires:	%{name}-devel
Requires:	cvs

%description autopoint
The `autopoint' program copies standard gettext infrastructure files
into a source package. It extracts from a macro call of the form
`AM_GNU_GETTEXT_VERSION(VERSION)', found in the package's
`configure.in' or `configure.ac' file, the gettext version used by the
package, and copies the infrastructure files belonging to this version
into the package.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
cd gettext-runtime
%{__libtoolize}
%{__aclocal} -I m4 -I ../m4 -I gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd libasprintf
%{__aclocal} -I ../../m4 -I ../m4 -I gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../../gettext-tools
%{__aclocal} -I m4 -I ../gettext-runtime/m4 -I ../m4 -I gnulib-m4 -I libgrep/gnulib-m4 -I libgettextpo/gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-csharp	\
	--disable-java		\
	--disable-static	\
	--enable-nls		\
	--without-included-gettext
%{__make} \
	GMSGFMT=`pwd`/gettext-tools/src/msgfmt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/{,n}gettext $RPM_BUILD_ROOT/bin

rm -r $RPM_BUILD_ROOT%{_docdir}/gettext
rm -r $RPM_BUILD_ROOT%{_docdir}/libasprintf
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}-runtime
%find_lang %{name}-tools

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n libasprintf -p /sbin/ldconfig
%postun	-n libasprintf -p /sbin/ldconfig

%post -n libasprintf-devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -n libasprintf-devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}-runtime.lang
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/envsubst
%{_mandir}/man1/envsubst.1*
%{_mandir}/man1/gettext.1*
%{_mandir}/man1/ngettext.1*
%dir %{_libdir}/gettext
%dir %{_datadir}/gettext

%files libs
%defattr(644,root,root,755)
# libgettextpo is for other programs, not used by gettext tools themselves
%attr(755,root,root) %ghost %{_libdir}/libgettextpo.so.?
%attr(755,root,root) %{_libdir}/libgettextpo.so.*.*.*
%attr(755,root,root) %{_libdir}/libgettext*.so

%files devel -f %{name}-tools.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/autopoint
%exclude %{_bindir}/envsubst
%{_libdir}/libgettext*.la
%attr(755,root,root) %{_libdir}/preloadable_libintl.so
%attr(755,root,root) %{_libdir}/gettext/hostname
%attr(755,root,root) %{_libdir}/gettext/project-id
%attr(755,root,root) %{_libdir}/gettext/urlget
%attr(755,root,root) %{_libdir}/gettext/user-email
%{_includedir}/gettext-po.h
%{_aclocaldir}/*
%{_infodir}/gettext*.info*
%{_mandir}/man1/gettextize.1*
%{_mandir}/man1/msg*.1*
%{_mandir}/man1/recode-sr-latin.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man3/*

%dir %{_datadir}/gettext/intl
%dir %{_datadir}/gettext/projects
%dir %{_datadir}/gettext/projects/GNOME
%dir %{_datadir}/gettext/projects/KDE
%dir %{_datadir}/gettext/projects/TP

%attr(755,root,root) %{_datadir}/gettext/config.rpath
%attr(755,root,root) %{_datadir}/gettext/intl/config.charset
%attr(755,root,root) %{_datadir}/gettext/projects/GNOME/team-address
%attr(755,root,root) %{_datadir}/gettext/projects/GNOME/trigger
%attr(755,root,root) %{_datadir}/gettext/projects/KDE/team-address
%attr(755,root,root) %{_datadir}/gettext/projects/KDE/trigger
%attr(755,root,root) %{_datadir}/gettext/projects/TP/team-address
%attr(755,root,root) %{_datadir}/gettext/projects/TP/trigger
%attr(755,root,root) %{_datadir}/gettext/projects/team-address

%{_datadir}/gettext/ABOUT-NLS
%{_datadir}/gettext/gettext.h
%{_datadir}/gettext/intl/[!c]*
%{_datadir}/gettext/msgunfmt.tcl
%{_datadir}/gettext/po
%{_datadir}/gettext/projects/GNOME/teams.*
%{_datadir}/gettext/projects/KDE/teams.*
%{_datadir}/gettext/projects/TP/teams.*
%{_datadir}/gettext/projects/index
%{_datadir}/gettext/styles

%files -n libasprintf
%defattr(644,root,root,755)
%doc gettext-runtime/libasprintf/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %ghost %{_libdir}/libasprintf.so.?
%attr(755,root,root) %{_libdir}/libasprintf.so.*.*.*

%files -n libasprintf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasprintf.so
%{_libdir}/libasprintf.la
%{_includedir}/autosprintf.h
%{_infodir}/autosprintf.info*

%files autopoint
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/autopoint
%{_datadir}/gettext/archive.dir.tar.gz
%{_mandir}/man1/autopoint.1*

