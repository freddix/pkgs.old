Summary:	SANE - easy local and networked scanner access
Name:		sane-backends
Version:	1.0.22
Release:	5
License:	relaxed LGPL (libraries), and Public Domain (docs)
Group:		Libraries
Source0:	https://alioth.debian.org/frs/download.php/3503/%{name}-%{version}.tar.gz
# Source0-md5:	fadf56a60f4776bfb24491f66b617cf5
Source1:	%{name}.m4
Patch0:		%{name}-mustek-path.patch
Patch1:		%{name}-glibc27.patch
Patch2:		%{name}-udev.patch
URL:		http://www.sane-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	pkg-config
BuildRequires:	texlive-dvips
BuildRequires:	texlive-latex
BuildRequires:	texlive-latex-psnfss
Provides:	scanner-backend = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras.

%package libs
Summary:	SANE library
Group:		Libraries

%description libs
SANE library.

%package devel
Summary:	Development part of SANE
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development part of SANE.

%package common
Summary:	Common part of SANE
Group:		Applications
Requires:	scanner-backend = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description common
Common part of SANE.

%package gphoto2
Summary:	SANE backend for gphoto2 supported cameras
Group:		Applications/System
Provides:	scanner-backend = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description gphoto2
SANE backend for gphoto2 supported cameras.

%package plustek
Summary:	SANE Plustek backend
Group:		Applications/System
Provides:	scanner-backend = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description plustek
SANE Plustek backend.

%prep
%setup -q

# kill libtool.m4 inclusion
grep -v '^m4_include' acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--disable-static	\
	--enable-avahi		\
	--enable-pnm-backend	\
	--enable-translations 	\
	--with-gphoto2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_libexecdir},/var/lock/sane}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_aclocaldir}

install -D tools/udev/libsane.rules \
	$RPM_BUILD_ROOT/lib/udev/rules.d/65-libsane.rules

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

# only shared modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/sane/libsane-*.{so,la}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files common -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS PROBLEMS PROJECTS README README.linux
%dir %{_sysconfdir}/sane.d
%dir %{_libdir}/sane
%attr(755,root,root) %{_bindir}/sane-find-scanner
%attr(755,root,root) %{_bindir}/scanimage
%attr(755,root,root) %{_bindir}/gamma4scanimage
%dir %attr(775,root,usb) /var/lock/sane
/lib/udev/rules.d/65-libsane.rules
%{_mandir}/man1/sane-find-scanner.1*
%{_mandir}/man1/scanimage.1*
%{_mandir}/man1/gamma4scanimage.1*

%files
%defattr(644,root,root,755)
%doc doc/canon doc/gt68xx doc/leo doc/matsushita doc/mustek doc/mustek_usb
%doc doc/sceptre doc/teco doc/umax
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/abaton.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/agfafocus.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/apple.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/artec.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/artec_eplus48u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/avision.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/bh.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon630u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon_dr.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/cardscan.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/coolscan.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/coolscan2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/coolscan3.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dc210.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dc240.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dc25.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dell1600n_net.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dll.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dmc.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/epjitsu.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/epson.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/epson2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/fujitsu.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/genesys.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/gt68xx.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp3900.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp4200.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp5400.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hpsj5s.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hs2p.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/ibm.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/kodak.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/leo.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/lexmark.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/ma1509.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/magicolor.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/matsushita.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/microtek.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/microtek2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek_usb.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/nec.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/net.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/pie.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/pixma.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/qcam.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/ricoh.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/rts8891.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/s9036.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sceptre.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sharp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sm3840.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/snapscan.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sp15c.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/st400.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/stv680.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/tamarack.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/teco1.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/teco2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/teco3.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/test.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/u12.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/umax.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/umax1220u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/umax_pp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/xerox_mfp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/p5.conf

%attr(755,root,root) %{_libdir}/sane/libsane-abaton.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-agfafocus.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-apple.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-artec.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-artec_eplus48u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-as6e.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-avision.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-bh.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon630u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon_dr.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-cardscan.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-coolscan.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-coolscan2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-coolscan3.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dc210.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dc240.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dc25.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dell1600n_net.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dll.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dmc.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-epjitsu.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-epson.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-epson2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-fujitsu.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-genesys.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-gt68xx.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp3500.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp3900.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp4200.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp5400.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp5590.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hpljm1005.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hpsj5s.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hs2p.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-ibm.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-kodak.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-kvs1025.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-kvs20xx.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-leo.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-lexmark.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-ma1509.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-magicolor.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-matsushita.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-microtek.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-microtek2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek_usb.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-nec.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-net.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-niash.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-p5.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-pie.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-pixma.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-pnm.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-qcam.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-ricoh.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-rts8891.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-s9036.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sceptre.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sharp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sm3600.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sm3840.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-snapscan.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sp15c.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-st400.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-stv680.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-tamarack.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-teco1.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-teco2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-teco3.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-test.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-u12.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-umax.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-umax1220u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-umax_pp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-xerox_mfp.so.*

%dir %attr(775,root,usb) /var/lock/sane

%{_mandir}/man1/gamma4scanimage.1*
%{_mandir}/man1/sane-config.1*
%{_mandir}/man1/sane-find-scanner.1*
%{_mandir}/man1/scanimage.1*
%{_mandir}/man5/sane-abaton.5*
%{_mandir}/man5/sane-agfafocus.5*
%{_mandir}/man5/sane-apple.5*
%{_mandir}/man5/sane-artec.5*
%{_mandir}/man5/sane-artec_eplus48u.5*
%{_mandir}/man5/sane-as6e.5*
%{_mandir}/man5/sane-avision.5*
%{_mandir}/man5/sane-bh.5*
%{_mandir}/man5/sane-canon.5*
%{_mandir}/man5/sane-canon630u.5*
%{_mandir}/man5/sane-canon_dr.5*
%{_mandir}/man5/sane-cardscan.5*
%{_mandir}/man5/sane-coolscan.5*
%{_mandir}/man5/sane-coolscan2.5*
%{_mandir}/man5/sane-coolscan3.5*
%{_mandir}/man5/sane-dc210.5*
%{_mandir}/man5/sane-dc240.5*
%{_mandir}/man5/sane-dc25.5*
%{_mandir}/man5/sane-dll.5*
%{_mandir}/man5/sane-dmc.5*
%{_mandir}/man5/sane-epjitsu.5*
%{_mandir}/man5/sane-epson.5*
%{_mandir}/man5/sane-epson2.5*
%{_mandir}/man5/sane-fujitsu.5*
%{_mandir}/man5/sane-genesys.5*
%{_mandir}/man5/sane-gt68xx.5*
%{_mandir}/man5/sane-hp.5*
%{_mandir}/man5/sane-hp3500.5*
%{_mandir}/man5/sane-hp3900.5*
%{_mandir}/man5/sane-hp4200.5*
%{_mandir}/man5/sane-hp5400.5*
%{_mandir}/man5/sane-hp5590.5*
%{_mandir}/man5/sane-hpljm1005.5*
%{_mandir}/man5/sane-hpsj5s.5*
%{_mandir}/man5/sane-hs2p.5*
%{_mandir}/man5/sane-ibm.5*
%{_mandir}/man5/sane-kodak.5.gz
%{_mandir}/man5/sane-kvs1025.5*
%{_mandir}/man5/sane-kvs20xx.5*
%{_mandir}/man5/sane-leo.5*
%{_mandir}/man5/sane-lexmark.5*
%{_mandir}/man5/sane-ma1509.5*
%{_mandir}/man5/sane-magicolor.5*
%{_mandir}/man5/sane-matsushita.5*
%{_mandir}/man5/sane-microtek.5*
%{_mandir}/man5/sane-microtek2.5*
%{_mandir}/man5/sane-mustek.5*
%{_mandir}/man5/sane-mustek_usb.5*
%{_mandir}/man5/sane-nec.5*
%{_mandir}/man5/sane-net.5*
%{_mandir}/man5/sane-niash.5*
%{_mandir}/man5/sane-p5.5*
%{_mandir}/man5/sane-pie.5*
%{_mandir}/man5/sane-pixma.5*
%{_mandir}/man5/sane-pnm.5*
%{_mandir}/man5/sane-qcam.5*
%{_mandir}/man5/sane-ricoh.5*
%{_mandir}/man5/sane-rts8891.5*
%{_mandir}/man5/sane-s9036.5*
%{_mandir}/man5/sane-sceptre.5*
%{_mandir}/man5/sane-scsi.5*
%{_mandir}/man5/sane-sharp.5*
%{_mandir}/man5/sane-sm3600.5*
%{_mandir}/man5/sane-sm3840.5*
%{_mandir}/man5/sane-snapscan.5*
%{_mandir}/man5/sane-sp15c.5*
%{_mandir}/man5/sane-st400.5*
%{_mandir}/man5/sane-stv680.5*
%{_mandir}/man5/sane-tamarack.5*
%{_mandir}/man5/sane-teco1.5*
%{_mandir}/man5/sane-teco2.5*
%{_mandir}/man5/sane-teco3.5*
%{_mandir}/man5/sane-test.5*
%{_mandir}/man5/sane-u12.5*
%{_mandir}/man5/sane-umax.5*
%{_mandir}/man5/sane-umax1220u.5*
%{_mandir}/man5/sane-umax_pp.5*
%{_mandir}/man5/sane-usb.5*
%{_mandir}/man5/sane-xerox_mfp.5*
%{_mandir}/man7/sane.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/libsane.so
%{_libdir}/libsane.la
%{_includedir}/sane
%{_aclocaldir}/sane-backends.m4

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/sane
%attr(755,root,root) %ghost %{_libdir}/libsane.so.?
%attr(755,root,root) %{_libdir}/libsane.so.*.*.*

%files gphoto2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/gphoto2.conf
%attr(755,root,root) %{_libdir}/sane/libsane-gphoto2.so.*
%{_mandir}/man5/sane-gphoto2.5*

%files plustek
%defattr(644,root,root,755)
%doc doc/plustek
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/plustek.conf
%attr(755,root,root) %{_libdir}/sane/libsane-plustek.so.*
%{_mandir}/man5/sane-plustek.5*

# unpackaged files
%if 0
/etc/sane.d/canon_pp.conf
/etc/sane.d/mustek_pp.conf
/etc/sane.d/plustek_pp.conf
/etc/sane.d/saned.conf
/usr/lib/sane/libsane-canon_pp.so.1
/usr/lib/sane/libsane-canon_pp.so.1.0.22
/usr/lib/sane/libsane-mustek_pp.so.1
/usr/lib/sane/libsane-mustek_pp.so.1.0.22
/usr/lib/sane/libsane-plustek_pp.so.1
/usr/lib/sane/libsane-plustek_pp.so.1.0.22
/usr/sbin/saned
/usr/share/man/man5/sane-canon_pp.5.gz
/usr/share/man/man5/sane-mustek_pp.5.gz
/usr/share/man/man5/sane-plustek_pp.5.gz
/usr/share/man/man8/saned.8.gz
%endif

