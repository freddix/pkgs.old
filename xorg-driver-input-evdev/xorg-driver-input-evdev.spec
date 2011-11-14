Summary:	X.org input driver for Linux generic event devices
Name:		xorg-driver-input-evdev
Version:	2.6.0
Release:	7
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-%{version}.tar.bz2
# Source0-md5:	f33fe9413bde68936d8909206a13e8a1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Linux generic event devices. It supports all
input devices that the kernel knows about, including most mice and
keyboards.

%prep
%setup -qn xf86-input-evdev-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.4*

