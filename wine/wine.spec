Summary:	Program that lets you launch Win applications
Name:		wine
Version:	1.3.28
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Emulators
Source0:	http://downloads.sourceforge.net/wine/%{name}-%{version}.tar.bz2
# Source0-md5:	70574d609161cec8523804cd9364bcd2
Source1:        http://downloads.sourceforge.net/wine/%{name}_gecko-1.2.0-x86.msi
# Source1-md5:	f2ed548494c86c511892b1c02491c8c4
Patch0:		%{name}-fontcache.patch
Patch1:		%{name}-makedep.patch
Patch2:		%{name}-ncurses.patch
Patch3:		%{name}-ca_certificates.patch
Patch4:		%{name}-rt.patch
Patch5:		%{name}-ddraw.patch
URL:		http://www.winehq.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	gnutls-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	openal-soft-devel
BuildRequires:	openjade
BuildRequires:	openldap-devel
BuildRequires:	opensp
BuildRequires:	openssl-devel
BuildRequires:	prelink
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-libXxf86dga-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# link to wine/ntdll.dll.so, without any SONAME
Provides:	libntdll.dll.so
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep		libGL.so.1 libGLU.so.1
%define		no_install_post_strip	1

%define		_winedir		%{_datadir}/%{name}

%define		getsoname()	%((objdump -p %{1} 2>/dev/null || echo SONAME ERROR) | awk '/SONAME/ { print $2; s=1 }; END { if(s==0) print "ERROR" }')

%undefine	debuginfocflags

%description
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix. It
consists of a program loader which loads and executes a Microsoft
Windows binary, and a library that implements Windows API calls using
their Unix or X11 equivalents. The library may also be used for
porting Win32 code into native Unix executables.

%package libs
Summary:	Wine libraries
Group:		Libraries

%description libs
Wine libraries.

%package devel
Summary:	Wine - header files
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Wine - header files.

%package programs
Summary:	Wine - programs
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description programs
Wine - programs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1

%build
%{__autoconf}
%{__autoheader}
%configure \
	--with-x
%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_aclocaldir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p tools/fnt2bdf $RPM_BUILD_ROOT%{_bindir}
cp -a aclocal.m4 $RPM_BUILD_ROOT%{_aclocaldir}/wine.m4

install -d \
	$RPM_BUILD_ROOT%{_winedir}/windows/{system,Desktop,Favorites,Fonts} \
	"$RPM_BUILD_ROOT%{_winedir}/windows/Start Menu/Programs/Startup" \
	$RPM_BUILD_ROOT%{_winedir}/windows/{SendTo,ShellNew,system32,NetHood} \
	$RPM_BUILD_ROOT%{_winedir}/windows/{Profiles/Administrator,Recent} \
	$RPM_BUILD_ROOT%{_winedir}/{"Program Files/Common Files","My Documents"}

touch $RPM_BUILD_ROOT%{_winedir}/{autoexec.bat,config.sys,windows/win.ini}
touch $RPM_BUILD_ROOT%{_winedir}/windows/system/{shell.dll,shell32.dll}
touch $RPM_BUILD_ROOT%{_winedir}/windows/system/{winsock.dll,wsock32.dll}

cat > $RPM_BUILD_ROOT%{_winedir}/windows/system.ini <<'EOF'
[mci]
cdaudio=mcicda.drv
sequencer=mciseq.drv
waveaudio=mciwave.drv
avivideo=mciavi.drv
videodisc=mcipionr.drv
vcr=mciviscd.drv
MPEGVideo=mciqtz.drv
EOF

echo "Strip executable binaries and shared object files."
filelist=`find $RPM_BUILD_ROOT -type f ! -regex ".*ld-[0-9.]*so.*"`
elfexelist=`echo $filelist | xargs -r file | \
	awk '/ELF.*executable/ {print $1}' | cut -d: -f1`
elfsharedlist=`echo $filelist | xargs -r file | \
	awk '/LF.*shared object/ {print $1}' | cut -d: -f1`; \
if [ -n "$elfexelist" ]; then \
	strip -R .note -R .comment $elfexelist
fi
if [ -n "$elfsharedlist" ]; then
	strip --strip-unneeded -R .note -R .comment $elfsharedlist
fi

# /sbin/chstk -e $RPM_BUILD_ROOT%{_bindir}/wine

dir=$(pwd)
> files.so
> files.programs
cd $RPM_BUILD_ROOT%{_libdir}/wine
for f in *.so; do
	case $f in
	d3d8.dll.so|d3d9.dll.so|d3dx8.dll.so|glu32.dll.so|opengl32.dll.so|sane.ds.so|twain.dll.so|twain_32.dll.so|winealsa.drv.so|winenas.drv.so)
		;;
	*)
		echo "%attr(755,root,root) %{_libdir}/wine/$f" >> $dir/files.so
	esac
done
cd -

programs="notepad regedit regsvr32 wineconsole winefile winemine winepath"
for p in $programs; do
	echo "%attr(755,root,root) %{_bindir}/$p" >> files.programs
	echo "%attr(755,root,root) %{_libdir}/wine/$p.exe.so" >> files.programs
	echo "%{_mandir}/man1/$p.1*" >> files.programs
	grep -v "$p\.exe\.so$" files.so > files.so.
	mv -f files.so. files.so
done

install -d $RPM_BUILD_ROOT%{_winedir}/gecko
install %{SOURCE1} $RPM_BUILD_ROOT%{_winedir}/gecko

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f files.so
%defattr(644,root,root,755)
%doc README README.WINE-RT AUTHORS ANNOUNCE
%lang(de) %doc documentation/README.de
%lang(es) %doc documentation/README.es
%lang(fr) %doc documentation/README.fr
%lang(it) %doc documentation/README.it
%lang(ko) %doc documentation/README.ko
%lang(nb) %doc documentation/README.no
%lang(pt) %doc documentation/README.pt
%lang(pt_BR) %doc documentation/README.pt_br

%attr(755,root,root) %{_bindir}/msiexec
%attr(755,root,root) %{_bindir}/wine
%attr(755,root,root) %{_bindir}/wine-preloader
%attr(755,root,root) %{_bindir}/wineboot
%attr(755,root,root) %{_bindir}/winecfg
%attr(755,root,root) %{_bindir}/winedbg
%attr(755,root,root) %{_bindir}/wineserver
%{_desktopdir}/wine.desktop

%attr(755,root,root) %{_libdir}/wine/d3d8.dll.so
%attr(755,root,root) %{_libdir}/wine/d3d9.dll.so
%attr(755,root,root) %{_libdir}/wine/glu32.dll.so
%attr(755,root,root) %{_libdir}/wine/opengl32.dll.so
%attr(755,root,root) %{_libdir}/wine/sane.ds.so
%attr(755,root,root) %{_libdir}/wine/twain*.dll.so
%attr(755,root,root) %{_libdir}/wine/winealsa.drv.so
%attr(755,root,root) %{_libdir}/wine/fakedlls/*

%{_mandir}/man1/wine.1*
%{_mandir}/man1/msiexec.1*
%{_mandir}/man1/wineboot.1*
%{_mandir}/man1/winecfg.1*
%{_mandir}/man1/winedbg.1*
%{_mandir}/man1/wineserver.1*
%{_winedir}

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/wine
%dir %{_libdir}/wine/fakedlls
%attr(755,root,root) %ghost %{_libdir}/libwine.so.1
%attr(755,root,root) %{_libdir}/libwine.so.*.*

%files programs -f files.programs
%defattr(644,root,root,755)

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fnt2bdf
%attr(755,root,root) %{_bindir}/function_grep.pl
%attr(755,root,root) %{_bindir}/widl
%attr(755,root,root) %{_bindir}/winebuild
%attr(755,root,root) %{_bindir}/winecpp
%attr(755,root,root) %{_bindir}/winedump
%attr(755,root,root) %{_bindir}/wineg++
%attr(755,root,root) %{_bindir}/winegcc
%attr(755,root,root) %{_bindir}/winemaker
%attr(755,root,root) %{_bindir}/wmc
%attr(755,root,root) %{_bindir}/wrc
%attr(755,root,root) %{_libdir}/libwine.so

%{_libdir}/wine/lib*.def

# no shared variants, so not separated
%{_libdir}/wine/lib*.def.a
%{_libdir}/wine/libadsiid.a
%{_libdir}/wine/libdx*.a
%{_libdir}/wine/libstrmiids.a
%{_libdir}/wine/libuuid.a
%{_libdir}/wine/libwinecrt0.a
%{_includedir}/wine
%{_aclocaldir}/*.m4

%{_mandir}/man1/widl.1*
%{_mandir}/man1/winebuild.1*
%{_mandir}/man1/winedump.1*
%{_mandir}/man1/wineg++.1
%{_mandir}/man1/winegcc.1*
%{_mandir}/man1/winemaker.1*
%{_mandir}/man1/wmc.1*
%{_mandir}/man1/wrc.1*

