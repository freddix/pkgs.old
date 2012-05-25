Summary:	X.org video driver for QXL virtual GPU
Name:		xorg-driver-video-qxl
Version:	0.0.17
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2
# Source0-md5:	c0ee45ce06654b9f2e6ddac478d5fbd6
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpciaccess-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	spice-protocol
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for QXL virtual GPU, which can be found in the
RedHat Enterprise Virtualisation system, and also in the spice
project.

%prep
%setup -qn xf86-video-qxl-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/qxl_drv.so

