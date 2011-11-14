%define		bigreqsproto_version		1.1.1
%define		compositeproto_version		0.4.2
%define		damageproto_version		1.2.1
%define		dmxproto_version		2.3.1
%define		dri2proto_version		2.6
%define		evieext_version			1.1.1
%define		fixesproto_version		5.0
%define		fontcacheproto_version		0.1.3
%define		fontsproto_version		2.1.1
%define		glproto_version			1.4.14
%define		inputproto_version		2.0.2
%define		kbproto_version			1.0.5
%define		printproto_version		1.0.4
%define		randrproto_version		1.3.2
%define		recordproto_version		1.14.1
%define		renderproto_version		0.11.1
%define		resourceproto_version		1.2.0
%define		scrnsaverproto_version		1.2.1
%define		trapproto_version		3.4.3
%define		videoproto_version		2.3.1
%define		xcmiscproto_version		1.2.1
%define		xextproto_version		7.2.0
%define		xf86bigfontproto_version	1.2.0
%define		xf86dgaproto_version		2.1
%define		xf86driproto_version		2.1.1
%define		xf86miscproto_version		0.9.3
%define		xf86rushproto_version		1.1.2
%define		xf86vidmodeproto_version	2.3.1
%define		xineramaproto_version		1.2.1
%define		xproto_version			7.0.22
%define		xproxymanagementprotocol_version	1.0.3
#
%define		xcbproto_version		1.6
#
Summary:	Xorg headers
Name:		xorg-proto
Version:	7.6
Release:	4
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-%{bigreqsproto_version}.tar.bz2
# Source0-md5:	6f6c24436c2b3ab235eb14a85b9aaacf
Source1:	http://xorg.freedesktop.org/releases/individual/proto/compositeproto-%{compositeproto_version}.tar.bz2
# Source1-md5:	98482f65ba1e74a08bf5b056a4031ef0
Source2:	http://xorg.freedesktop.org/releases/individual/proto/damageproto-%{damageproto_version}.tar.bz2
# Source2-md5:	998e5904764b82642cc63d97b4ba9e95
Source3:	http://xorg.freedesktop.org/releases/individual/proto/dmxproto-%{dmxproto_version}.tar.bz2
# Source3-md5:	4ee175bbd44d05c34d43bb129be5098a
Source4:	http://xorg.freedesktop.org/releases/individual/proto/evieext-%{evieext_version}.tar.bz2
# Source4-md5:	98bd86a13686f65f0873070fdee6efc7
Source5:	http://xorg.freedesktop.org/releases/individual/proto/fixesproto-%{fixesproto_version}.tar.bz2
# Source5-md5:	e7431ab84d37b2678af71e29355e101d
Source6:	http://xorg.freedesktop.org/releases/individual/proto/fontcacheproto-%{fontcacheproto_version}.tar.bz2
# Source6-md5:	a8a50e5e995bfacb0359575faf7f6906
Source7:	http://xorg.freedesktop.org/releases/individual/proto/fontsproto-%{fontsproto_version}.tar.bz2
# Source7-md5:	37102ffcaa73f77d700acd6f7a25d8f0
Source8:	http://xorg.freedesktop.org/releases/individual/proto/glproto-%{glproto_version}.tar.bz2
# Source8-md5:	f48257daf0017f7a7667e5bf48ca3578
Source9:	http://xorg.freedesktop.org/releases/individual/proto/inputproto-%{inputproto_version}.tar.bz2
# Source9-md5:	07d54ae098ed4e6dce472f6ef3de05ce
Source10:	http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{kbproto_version}.tar.bz2
# Source10-md5:	e7edb59a3f54af15f749e8f3e314ee62
Source11:	http://xorg.freedesktop.org/releases/individual/proto/printproto-%{printproto_version}.tar.bz2
# Source11-md5:	7321847a60748b4d2f1fa16db4b6ede8
Source12:	http://xorg.freedesktop.org/releases/individual/proto/randrproto-%{randrproto_version}.tar.bz2
# Source12-md5:	597491c0d8055e2a66f11350c4985775
Source13:	http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{recordproto_version}.tar.bz2
# Source13-md5:	24541a30b399213def35f48efd926c63
Source14:	http://xorg.freedesktop.org/releases/individual/proto/renderproto-%{renderproto_version}.tar.bz2
# Source14-md5:	a914ccc1de66ddeb4b611c6b0686e274
Source15:	http://xorg.freedesktop.org/releases/individual/proto/resourceproto-%{resourceproto_version}.tar.bz2
# Source15-md5:	cfdb57dae221b71b2703f8e2980eaaf4
Source16:	http://xorg.freedesktop.org/releases/individual/proto/scrnsaverproto-%{scrnsaverproto_version}.tar.bz2
# Source16-md5:	6af0f2e3369f5f74e69345e214f5fd0d
Source17:	http://xorg.freedesktop.org/releases/individual/proto/trapproto-%{trapproto_version}.tar.bz2
# Source17-md5:	3b713239e5e6b269b31cb665563358df
Source18:	http://xorg.freedesktop.org/releases/individual/proto/videoproto-%{videoproto_version}.tar.bz2
# Source18-md5:	c3b348c6e2031b72b11ae63fc7f805c2
Source19:	http://xorg.freedesktop.org/releases/individual/proto/xcmiscproto-%{xcmiscproto_version}.tar.bz2
# Source19-md5:	cd7372cd827bfd7ca7e9238f2ce274b1
Source20:	http://xorg.freedesktop.org/releases/individual/proto/xextproto-%{xextproto_version}.tar.bz2
# Source20-md5:	220732210ceffb01bf1caf970e3b1bfb
Source21:	http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-%{xf86bigfontproto_version}.tar.bz2
# Source21-md5:	120e226ede5a4687b25dd357cc9b8efe
Source22:	http://xorg.freedesktop.org/releases/individual/proto/xf86dgaproto-%{xf86dgaproto_version}.tar.bz2
# Source22-md5:	a036dc2fcbf052ec10621fd48b68dbb1
Source23:	http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-%{xf86driproto_version}.tar.bz2
# Source23-md5:	1d716d0dac3b664e5ee20c69d34bc10e
Source24:	http://xorg.freedesktop.org/releases/individual/proto/xf86miscproto-%{xf86miscproto_version}.tar.bz2
# Source24-md5:	ca63bbb31cf5b7f37b2237e923ff257a
Source25:	http://xorg.freedesktop.org/releases/individual/proto/xf86rushproto-%{xf86rushproto_version}.tar.bz2
# Source25-md5:	b6a96ffdae084e27487a58314008b000
Source26:	http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-%{xf86vidmodeproto_version}.tar.bz2
# Source26-md5:	e793ecefeaecfeabd1aed6a01095174e
Source27:	http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-%{xineramaproto_version}.tar.bz2
# Source27-md5:	9959fe0bfb22a0e7260433b8d199590a
Source28:	http://xorg.freedesktop.org/releases/individual/proto/xproto-%{xproto_version}.tar.bz2
# Source28-md5:	da0b0eb2f432b7cc1d665b05422a0457
Source29:	http://xorg.freedesktop.org/releases/individual/proto/xproxymanagementprotocol-%{xproxymanagementprotocol_version}.tar.bz2
# Source29-md5:	9de22ca1522008c28fb03dfc41ba2d30
Source30:	http://xcb.freedesktop.org/dist/xcb-proto-%{xcbproto_version}.tar.bz2
# Source30-md5:	04313e1d914b44d0e457f6c494fc178b
Source31:	http://xorg.freedesktop.org/releases/individual/proto/dri2proto-%{dri2proto_version}.tar.bz2
# Source31-md5:	2eb74959684f47c862081099059a11ab
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-macros >= 1.3.0
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkgconfigdir	%{_datadir}/pkgconfig
%define		debug_package	%{nil}

%description
Xorg headers.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31

%build
for dir in `ls -1` ; do

cd $dir
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
cd ..

done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/X11/extensions

for dir in `ls -1` ; do

cd $dir
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}
cd ..

done

# provided by Mesa
rm -f $RPM_BUILD_ROOT/%{_includedir}/GL/internal/dri_interface.h

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%dir %{_includedir}/X11/fonts
%dir %{_includedir}/GL
%dir %{_includedir}/X11/dri
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%dir %{_includedir}/X11/PM

%{_includedir}/X11/fonts/*.h
%{_includedir}/GL/*.h
%{_includedir}/GL/internal
%{_includedir}/X11/dri/*.h
%{_includedir}/X11/extensions/*.h
%{_includedir}/X11/*.h
%{_includedir}/X11/PM/*.h
%{_datadir}/xcb
%{_pkgconfigdir}/*.pc

%{py_sitescriptdir}/xcbgen

