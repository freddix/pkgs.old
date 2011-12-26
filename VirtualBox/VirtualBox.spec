%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# without userspace part
#
%define		rel	1
#
Summary:	x86 and AMD64/Intel64 hardware virtualizer
Name:		VirtualBox
Version:	4.1.6
Release:	%{rel}
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://download.virtualbox.org/virtualbox/%{version}/VirtualBox-%{version}.tar.bz2
# Source0-md5:	89b979d1b817242c7cdcb489898f166a
Source2:	%{name}.desktop
Source3:	%{name}.sh
Patch1:		%{name}-configure-spaces.patch
Patch2:		%{name}-dri.patch
Patch3:		%{name}-export_modules.patch
Patch4:		%{name}-no-update.patch
Patch5:		%{name}-system-xorg.patch
URL:		http://www.virtualbox.org/
%if %{with userspace}
BuildRequires:	OpenGL-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	bash
BuildRequires:	bcc
BuildRequires:	bin86
BuildRequires:	cdrkit
BuildRequires:	iasl
BuildRequires:	libIDL-devel
BuildRequires:	libuuid-devel
BuildRequires:	libvncserver-devel
BuildRequires:	libxslt-progs
BuildRequires:	makeself
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	texlive-fonts-other
BuildRequires:	texlive-fonts-type1-bitstream
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-ucs
BuildRequires:	which
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-xserver-server-devel
BuildRequires:	zlib-devel
%endif
BuildRequires:	kernel%{_alt_kernel}-module-build
Obsoletes:	xorg-driver-input-vboxmouse
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		outdir	x86
%define		xvers	17

%description
InnoTek VirtualBox is a general-purpose full virtualizer for x86
hardware. Targeted at server, desktop and embedded use, it is now the
only professional-quality virtualization solution that is also Open
Source Software.

Some of the features of VirtualBox are:

Modularity: VirtualBox has an extremely modular design with
well-defined internal programming interfaces and a client/server
design. This makes it easy to control it from several interfaces at
once: for example, you can start a virtual machine in a typical
virtual machine GUI and then control that machine from the command
line. VirtualBox also comes with a full Software Development Kit: even
though it is Open Source Software, you don't have to hack the source
to write a new interface for VirtualBox.

Virtual machine descriptions in XML: the configuration settings of
virtual machines are stored entirely in XML and are independent of the
local machines. Virtual machine definitions can therefore easily be
ported to other computers.

%package guest-utils
Summary:	VirtualBox OSE guest utilities
Group:		Applications
Provides:	group(vbox)
Requires:	udev

%description guest-utils
VirtualBox OSE guest-utilities.

%package -n kernel%{_alt_kernel}-misc-vboxguest
Summary:	Linux kernel module for VirtualBox OSE
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%requires_releq_kernel
Requires(postun):	%releq_kernel
Provides:	kernel(vboxguest) = %{version}-%{rel}
Obsoletes:	kernel%{_alt_kernel}-misc-vboxadd

%description -n kernel%{_alt_kernel}-misc-vboxguest
Linux kernel module vboxguest for VirtualBox OSE.

%package -n kernel%{_alt_kernel}-misc-vboxdrv
Summary:	Linux kernel module for VirtualBox OSE
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%requires_releq_kernel
Requires(postun):	%releq_kernel
Provides:	kernel(vboxdrv) = %{version}-%{rel}

%description -n kernel%{_alt_kernel}-misc-vboxdrv
Linux kernel module vboxdrv for VirtualBox OSE.

%package -n kernel%{_alt_kernel}-misc-vboxsf
Summary:	Linux kernel module for VirtualBox OSE
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%requires_releq_kernel
Provides:	kernel(vboxguest) = %{version}-%{rel}

%description -n kernel%{_alt_kernel}-misc-vboxsf
Linux kernel module vboxsf for VirtualBox OSE.

%package -n kernel%{_alt_kernel}-misc-vboxnet
Summary:	VirtualBox OSE network modules
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	kernel%{_alt_kernel}-misc-vboxdrv
%requires_releq_kernel
Requires(postun):	%releq_kernel
Provides:	kernel(vboxnetflt) = %{version}-%{rel}

%description -n kernel%{_alt_kernel}-misc-vboxnet
VirtualBox OSE network modules.

%package -n kernel%{_alt_kernel}-misc-vboxvideo
Summary:	VirtualBox OSE drm module
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	kernel%{_alt_kernel}-misc-vboxguest
%requires_releq_kernel
Requires(postun):	%releq_kernel
Provides:	kernel(vboxvideo) = %{version}-%{rel}

%description -n kernel%{_alt_kernel}-misc-vboxvideo
VirtualBox OSE drm driver.

%package -n xorg-driver-video-vboxvideo
Summary:	X.org video driver for VirtualBox OSE guest OS
Group:		X11/Applications
Requires:	xorg-xserver-server >= 1.10.0

%description -n xorg-driver-video-vboxvideo
X.org video driver for VirtualBox guest OS.

%prep
%setup -qn VirtualBox-%{version}_OSE
%if %{with userspace}
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%endif
%patch3 -p1

# don't check for not used libs
sed -i -e "s/&& check_staticlibstdcxx//" configure

# iasl does not like it (?)
sed -i "s/smc-napa/smcnapa/g" src/VBox/Devices/PC/vbox.dsl

# no precompiled binaries will be used
rm -f tools/linux.*/bin/*

install -d kmod-build/{GuestDrivers,HostDrivers}
cd kmod-build
../src/VBox/Additions/linux/export_modules guest-modules.tar.gz
tar -zxf guest-modules.tar.gz -C GuestDrivers

../src/VBox/HostDrivers/linux/export_modules host-modules.tar.gz --without-hardening
tar -zxf host-modules.tar.gz -C HostDrivers
cd -

cat > LocalConfig.kmk <<EOF
VBOX_WITH_INSTALLER		= 1
VBOX_WITH_LINUX_ADDITIONS	= 1
VBOX_WITH_X11_ADDITIONS		= 1
VBOX_WITH_ADDITION_DRIVERS	=

# don't build testcases to save time, they are not needed for the package
VBOX_WITH_TESTCASES	:=
VBOX_WITH_TESTSUITE	:=

# required for VBOX_WITH_RUNPATH
VBOX_WITH_ORIGIN	:=

VBOX_WITH_VNC		:= 1

VBOX_PATH_APP_PRIVATE_ARCH	:= %{_libdir}/%{name}
VBOX_PATH_SHARED_LIBS		:= %{_libdir}/%{name}
VBOX_WITH_RUNPATH		:= %{_libdir}/%{name}
VBOX_PATH_APP_PRIVATE		:= %{_datadir}/%{name}

VBOX_GCC_OPT			= %{rpmcflags}
VBOX_DO_STRIP			:=
VBOX_DO_STRIP_MODULES		:=
VBOX_GCC_FP			= -fomit-frame-pointer
TOOL_YASM_AS			= yasm
KBUILD_VERBOSE			= 3
XSERVER_VERSION			= %{xvers}

VBOX_WITH_REGISTRATION_REQUEST	=
VBOX_WITH_UPDATE_REQUEST	=

EOF

%build
%if %{with userspace}
./configure \
	--with-linux=%{_prefix}	\
	--disable-hardening	\
	--disable-java		\
	--disable-kmods		\
	--ose			\
	--with-g++="%{__cxx}"	\
	--with-gcc="%{__cc}"

build_opts="\
	LOCALCFG=./LocalConfig.kmk	\
	USER=$(id -un)"

. ./env.sh && \
kmk -j1 USER=$(id -un) ${build_opts}
%endif

%if %{with kernel}
cd kmod-build/HostDrivers
%build_kernel_modules -m vboxdrv -C vboxdrv
%build_kernel_modules -m vboxnetadp -C vboxnetadp
%build_kernel_modules -m vboxnetflt -C vboxnetflt

cd ../GuestDrivers
%build_kernel_modules -m vboxguest -C vboxguest
cp -a vboxguest/Module.symvers vboxsf
%build_kernel_modules -m vboxsf -C vboxsf -c
%build_kernel_modules -m vboxvideo -C vboxvideo_drm
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}	\
	$RPM_BUILD_ROOT%{_libdir}/VirtualBox				\
	$RPM_BUILD_ROOT%{_libdir}/VirtualBox/ExtensionPack		\
	$RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,dri}

cp -a$l out/linux.%{outdir}/release/bin/* $RPM_BUILD_ROOT%{_libdir}/VirtualBox

rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/{additions/src,sdk,src,testcase}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/SUPInstall
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/SUPLoggerCtl
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/SUPUninstall
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/{scm,tst*}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/vboxkeyboard.tar.bz2

install %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/VirtualBox/VirtualBox-wrapper.sh

for f in {VBox{BFE,Headless,Manage,SDL,SVC,Tunctl,XPCOMIPCD},VirtualBox}; do
	install out/linux.%{outdir}/release/bin/$f $RPM_BUILD_ROOT%{_libdir}/VirtualBox/$f
	ln -s %{_libdir}/VirtualBox/VirtualBox-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/$f
done

install -d $RPM_BUILD_ROOT/etc/udev/rules.d
cat <<'EOF' > $RPM_BUILD_ROOT/etc/udev/rules.d/60-vboxadd.rules
KERNEL=="vboxdrv", GROUP="vbox", MODE="0660"
KERNEL=="vboxguest", ENV{ID_INPUT}="1", GROUP="vbox", MODE="0660"
KERNEL=="vboxnetctl", GROUP="vbox", MODE="0660"
EOF

mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions/vboxvideo_drv.so,%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so}
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions/VBoxOGL.so,%{_libdir}/xorg/modules/dri/vboxvideo_dri.so}

mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions/VBoxClient,%{_bindir}}
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions/VBoxControl,%{_bindir}}
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions/VBoxService,%{_bindir}}
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions/mount.vboxsf,%{_bindir}}

rm -vf $RPM_BUILD_ROOT%{_libdir}/VirtualBox/additions/vboxvideo_drv*.{o,so}

mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,%{_libdir}}/VBoxOGLarrayspu.so
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,%{_libdir}}/VBoxOGLcrutil.so
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,%{_libdir}}/VBoxOGLerrorspu.so
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,%{_libdir}}/VBoxOGLfeedbackspu.so
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,%{_libdir}}/VBoxOGLpackspu.so
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,%{_libdir}}/VBoxOGLpassthroughspu.so

install -d $RPM_BUILD_ROOT/%{_lib}/security
mv $RPM_BUILD_ROOT{%{_libdir}/VirtualBox/additions,/%{_lib}/security}/pam_vbox.so

install out/linux.%{outdir}/release/bin/VBox.png $RPM_BUILD_ROOT%{_pixmapsdir}/VBox.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
%endif

%if %{with kernel}
%install_kernel_modules -m kmod-build/HostDrivers/vboxdrv/vboxdrv -d misc
%install_kernel_modules -m kmod-build/HostDrivers/vboxnetadp/vboxnetadp -d misc
%install_kernel_modules -m kmod-build/HostDrivers/vboxnetflt/vboxnetflt -d misc
%install_kernel_modules -m kmod-build/GuestDrivers/vboxguest/vboxguest -d misc
%install_kernel_modules -m kmod-build/GuestDrivers/vboxsf/vboxsf -d misc
%install_kernel_modules -m kmod-build/GuestDrivers/vboxvideo_drm/vboxvideo -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre guest-utils
%groupadd -g 221 -r -f vbox

%postun guest-utils
if [ "$1" = "0" ]; then
	%groupremove vbox
fi

%post	-n kernel%{_alt_kernel}-misc-vboxguest
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-misc-vboxguest
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vboxdrv
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-misc-vboxdrv
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vboxsf
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-misc-vboxsf
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vboxnet
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-misc-vboxnet
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vboxvideo
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-misc-vboxvideo
%depmod %{_kernel_ver}

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc out/linux.*/release/bin/UserManual.pdf

%dir %{_libdir}/VirtualBox
%dir %{_libdir}/VirtualBox/ExtensionPack
%dir %{_libdir}/VirtualBox/components
%dir %{_libdir}/VirtualBox/nls

%attr(755,root,root) %{_bindir}/VBoxBFE
%attr(755,root,root) %{_bindir}/VBoxHeadless
%attr(755,root,root) %{_bindir}/VBoxManage
%attr(755,root,root) %{_bindir}/VBoxSDL
%attr(755,root,root) %{_bindir}/VBoxSVC
%attr(755,root,root) %{_bindir}/VBoxTunctl
%attr(755,root,root) %{_bindir}/VBoxXPCOMIPCD
%attr(755,root,root) %{_bindir}/VirtualBox

%attr(755,root,root) %{_libdir}/VirtualBox/DBGCPlugInDiggers.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxAuth.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxAuthSimple.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxCreateUSBNode.sh
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxDD.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxDD2.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxDDU.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxDbg.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxGuestControlSvc.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxGuestPropSvc.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxKeyboard.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxOGLhostcrutil.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxOGLhosterrorspu.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxOGLrenderspu.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxPython.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxPython2_6.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxREM.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxREM32.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxREM64.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxRT.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxSharedClipboard.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxSharedCrOpenGL.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxSharedFolders.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxVMM.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxXPCOM.so
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxXPCOMC.so

%attr(755,root,root) %{_libdir}/VirtualBox/EfiThunk
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxBFE
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxBalloonCtrl
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxExtPackHelperApp
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxHeadless
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxManage
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxManageHelp
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxNetAdpCtl
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxNetDHCP
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxSDL
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxSVC
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxSysInfo.sh
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxTestOGL
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxTunctl
%attr(755,root,root) %{_libdir}/VirtualBox/VBoxXPCOMIPCD
%attr(755,root,root) %{_libdir}/VirtualBox/VirtualBox
%attr(755,root,root) %{_libdir}/VirtualBox/VirtualBox-wrapper.sh

%{_libdir}/VirtualBox/*.gc
%{_libdir}/VirtualBox/*.r0
%attr(755,root,root) %{_libdir}/VirtualBox/components/*.so
%{_libdir}/VirtualBox/components/*.xpt

%lang(ar) %{_libdir}/VirtualBox/nls/*_ar.qm
%lang(bg) %{_libdir}/VirtualBox/nls/*_bg.qm
%lang(ca) %{_libdir}/VirtualBox/nls/*_ca.qm
%lang(ca_VA) %{_libdir}/VirtualBox/nls/*_ca_VA.qm
%lang(cs) %{_libdir}/VirtualBox/nls/*_cs.qm
%lang(da) %{_libdir}/VirtualBox/nls/*_da.qm
%lang(de) %{_libdir}/VirtualBox/nls/*_de.qm
%lang(el) %{_libdir}/VirtualBox/nls/*_el.qm
%lang(en) %{_libdir}/VirtualBox/nls/*_en.qm
%lang(es) %{_libdir}/VirtualBox/nls/*_es.qm
%lang(eu) %{_libdir}/VirtualBox/nls/*_eu.qm
%lang(fi) %{_libdir}/VirtualBox/nls/*_fi.qm
%lang(fr) %{_libdir}/VirtualBox/nls/*_fr.qm
%lang(gl_ES) %{_libdir}/VirtualBox/nls/*_gl_ES.qm
%lang(hu) %{_libdir}/VirtualBox/nls/*_hu.qm
%lang(id) %{_libdir}/VirtualBox/nls/*_id.qm
%lang(it) %{_libdir}/VirtualBox/nls/*_it.qm
%lang(ja) %{_libdir}/VirtualBox/nls/*_ja.qm
%lang(km_KH) %{_libdir}/VirtualBox/nls/*_km_KH.qm
%lang(ko) %{_libdir}/VirtualBox/nls/*_ko.qm
%lang(lt) %{_libdir}/VirtualBox/nls/*_lt.qm
%lang(nl) %{_libdir}/VirtualBox/nls/*_nl.qm
%lang(pl) %{_libdir}/VirtualBox/nls/*_pl.qm
%lang(pt) %{_libdir}/VirtualBox/nls/*_pt.qm
%lang(pt_BR) %{_libdir}/VirtualBox/nls/*_pt_BR.qm
%lang(ro) %{_libdir}/VirtualBox/nls/*_ro.qm
%lang(ru) %{_libdir}/VirtualBox/nls/*_ru.qm
%lang(sk) %{_libdir}/VirtualBox/nls/*_sk.qm
%lang(sr) %{_libdir}/VirtualBox/nls/*_sr.qm
%lang(sv) %{_libdir}/VirtualBox/nls/*_sv.qm
%lang(tr) %{_libdir}/VirtualBox/nls/*_tr.qm
%lang(uk) %{_libdir}/VirtualBox/nls/*_uk.qm
%lang(zh_CN) %{_libdir}/VirtualBox/nls/*_zh_CN.qm
%lang(zh_TW) %{_libdir}/VirtualBox/nls/*_zh_TW.qm

%{_desktopdir}/*.desktop
%{_libdir}/VirtualBox/icons
%{_libdir}/VirtualBox/virtualbox.xml
%{_pixmapsdir}/VBox.png

%files guest-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/VBoxClient
%attr(755,root,root) %{_bindir}/VBoxControl
%attr(755,root,root) %{_bindir}/VBoxService
%attr(755,root,root) %{_bindir}/mount.vboxsf
%config(noreplace) %verify(not md5 mtime size) /etc/udev/rules.d/60-vboxadd.rules

%files -n xorg-driver-video-vboxvideo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/dri/vboxvideo_dri.so
%attr(755,root,root) %{_libdir}/VBoxOGLarrayspu.so
%attr(755,root,root) %{_libdir}/VBoxOGLcrutil.so
%attr(755,root,root) %{_libdir}/VBoxOGLerrorspu.so
%attr(755,root,root) %{_libdir}/VBoxOGLfeedbackspu.so
%attr(755,root,root) %{_libdir}/VBoxOGLpackspu.so
%attr(755,root,root) %{_libdir}/VBoxOGLpassthroughspu.so
%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-misc-vboxguest
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vboxguest.ko*

%files -n kernel%{_alt_kernel}-misc-vboxdrv
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vboxdrv.ko*

%files -n kernel%{_alt_kernel}-misc-vboxnet
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vboxnetadp.ko*
/lib/modules/%{_kernel_ver}/misc/vboxnetflt.ko*

%files -n kernel%{_alt_kernel}-misc-vboxsf
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vboxsf.ko*

%files -n kernel%{_alt_kernel}-misc-vboxvideo
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vboxvideo.ko*
%endif

