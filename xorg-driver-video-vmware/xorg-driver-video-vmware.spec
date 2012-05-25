Summary:	X.org video driver for VMware virtual video cards
Name:		xorg-driver-video-vmware
Version:	12.0.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
# Source0-md5:	0743ec7c479603fba60d118858fd5783
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libpciaccess-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VMware virtual video cards. It auto-detects the
version of any virtual VMware SVGA adapter.

%prep
%setup -q -n xf86-video-vmware-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-vmwarectrl-client
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/vmwarectrl
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.4*

