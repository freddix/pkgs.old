Summary:	wxWidgets library
Name:		wxWidgets
Version:	2.8.12
Release:	1
License:	wxWidgets Licence (LGPL with exception)
Group:		X11/Libraries
Source0:	http://ftp.wxwidgets.org/pub/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	4103e37e277abeb8aee607b990c215c4
Patch0:		%{name}-samples.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-x11unicode.patch
Patch3:		%{name}-gcc4.patch
URL:		http://www.wxWidgets.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cppunit-devel
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libmspack-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%{_datadir}
%define		skip_post_check_so	libwx_gtk2u_core-2.8.so.* libwx_gtk2u_adv-2.8.so.*

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%package devel
Summary:	wxWidgets header files and development documentation
Group:		X11/Development/Libraries

%description devel
Header files and development documentation for the wxWidgets
libraries.

%package examples
Summary:	wxWidgets example programs
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
wxWidgets example programs.

%package HelpGen
Summary:	Help file generator for wxWidgets programs
Group:		Development/Tools
Requires:	wxBase = %{version}-%{release}

%description HelpGen
Help file generator for wxWidgets programs.

%package -n wxBase
Summary:	wxBase library - non-GUI support classes of wxWidgets toolkit
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n wxBase
wxBase is a collection of C++ classes providing basic data structures
strings, lists, arrays), powerful wxDateTime class for date
manipulations, portable wrappers around many OS-specific functions
allowing to build the same program under all supported folders,
wxThread class for writing multithreaded programs using either Win32
or POSIX threads and much more. wxBase currently supports the
following platforms: Win32, generic Unix (Linux, FreeBSD, Solaris,
HP-UX, ...) and BeOS.

%package -n wxBase-devel
Summary:	wxBase headers needed for developping with wxBase
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase = %{version}-%{release}

%description -n wxBase-devel
Header files for wxBase. You need them to develop programs using
wxBase.

%package -n wxBase-unicode
Summary:	wxBase library - non-GUI support classes of wxWidgets toolkit with UNICODE support
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n wxBase-unicode
wxBase is a collection of C++ classes providing basic data structures
(strings, lists, arrays), powerful wxDateTime class for date
manipulations, portable wrappers around many OS-specific functions
allowing to build the same program under all supported folders,
wxThread class for writing multithreaded programs using either Win32
or POSIX threads and much more. wxBase currently supports the
following platforms: Win32, generic Unix (Linux, FreeBSD, Solaris,
HP-UX, ...) and BeOS. This version is build with UNICODE support.

%package -n wxBase-unicode-devel
Summary:	wxBase headers needed for developping with UNICODE-enabled wxBase
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-unicode = %{version}-%{release}

%description -n wxBase-unicode-devel
Header files for wxBase. You need them to develop programs using
UNICODE-enabled wxBase.

%package -n wxGTK
Summary:	wxGTK library
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n wxGTK
wxWidgets library using GTK widgets.

%package -n wxGTK-devel
Summary:	Header files for wxGTK library
Group:		X11/Development/Libraries
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxGTK = %{version}-%{release}

%description -n wxGTK-devel
Header files for wxGTK library.

%package -n wxGTK-unicode
Summary:	wxGTK library with UNICODE support
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n wxGTK-unicode
wxWidgets library using GTK widgets with UNICODE support.

%package -n wxGTK-unicode-devel
Summary:	Header files for wxGTK library with UNICODE support
Group:		X11/Development/Libraries
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxGTK-unicode = %{version}-%{release}

%description -n wxGTK-unicode-devel
Header files for wxWidgets library using GTK widgets with UNICODE
support.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

echo 'AC_DEFUN([AM_PATH_GTK],[:])' > fake-am_path_gtk.m4

%build
#cp -f /usr/share/automake/config.sub .
#%{__aclocal} -I build/aclocal
#%{__autoconf}

CPPFLAGS="%{rpmcflags} -I`pwd`/include"; export CPPFLAGS
# avoid adding -s to LDFLAGS
LDFLAGS=" "; export LDFLAGS

objdir=`echo obj-gtk2-unicode`
mkdir $objdir
cd $objdir
../%configure \
	--disable-universal	\
	--enable-calendar	\
	--enable-controls	\
	--enable-plugins	\
	--enable-std_iostreams	\
	--enable-tabdialog	\
	--enable-unicode	\
	--with-gtk		\
	--with-opengl		\
	--without-sdl
%{__make}
%{__make} -C contrib/src
cd ..

cd locale
%{__make} allmo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

objdir=`echo obj-gtk2-unicode`

cd $objdir

%{__make} -j1 install \
	prefix=$RPM_BUILD_ROOT%{_prefix}		\
	exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix}	\
	bindir=$RPM_BUILD_ROOT%{_bindir}		\
	datadir=$RPM_BUILD_ROOT%{_datadir}		\
	libdir=$RPM_BUILD_ROOT%{_libdir}		\
	mandir=$RPM_BUILD_ROOT%{_mandir}		\
	includedir=$RPM_BUILD_ROOT%{_includedir}

%{__make} -j1 -C contrib/src install \
	prefix=$RPM_BUILD_ROOT%{_prefix}		\
	exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix}	\
	bindir=$RPM_BUILD_ROOT%{_bindir}		\
	datadir=$RPM_BUILD_ROOT%{_datadir}		\
	libdir=$RPM_BUILD_ROOT%{_libdir}		\
	mandir=$RPM_BUILD_ROOT%{_mandir}		\
	includedir=$RPM_BUILD_ROOT%{_includedir}
cd ..

set -x

for i in $RPM_BUILD_ROOT%{_libdir}/wx/config/*
do
	b=`basename $i`
	cp $i $RPM_BUILD_ROOT%{_bindir}/wx-`echo $b|sed -e 's/\(.*\)-release-.*/\1/'`-config
done

cp -f docs/x11/readme.txt docs/wxX11-readme.txt

%find_lang wxstd

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n wxBase-unicode -p /sbin/ldconfig
%postun -n wxBase-unicode -p /sbin/ldconfig

%post	-n wxGTK-unicode -p /sbin/ldconfig
%postun -n wxGTK-unicode -p /sbin/ldconfig

%files -f wxstd.lang
%defattr(644,root,root,755)
%doc docs/{changes,licence,licendoc,preamble,readme,todo}.txt

%files devel
%defattr(644,root,root,755)
%doc docs/html
%doc docs/tech docs/univ
%{_includedir}/wx*
%dir %{_libdir}/wx
%dir %{_libdir}/wx/include
%dir %{_libdir}/wx/config
%{_aclocaldir}/*.m4

%files -n wxBase-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libwx_baseu*.so.?
%attr(755,root,root) %{_libdir}/libwx_baseu*.so.*.*.*

%files -n wxBase-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_baseu*.so

%files -n wxGTK-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u*.so.?
%attr(755,root,root) %{_libdir}/libwx_gtk2u*.so.*.*.*

%files -n wxGTK-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2u*-*.so
%{_libdir}/wx/config/gtk2-unicode-*
%{_libdir}/wx/include/gtk2-unicode-*
%attr(755,root,root) %{_bindir}/wx-gtk2-unicode-config

