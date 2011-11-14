Summary:	X.org Wacom input driver
Name:		xorg-driver-input-wacom
Version:	0.11.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/linuxwacom/xf86-input-wacom-%{version}.tar.bz2
# Source0-md5:	0aec4a338cc583ed497b6af68d6d80ab
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xserver-server-devel
Obsoletes:	linuxwacom
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org Wacom input driver.

%prep
%setup -qn xf86-input-wacom-%{version}

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
%doc README
%attr(755,root,root) %{_bindir}/xsetwacom
%attr(755,root,root) %{_libdir}/xorg/modules/input/wacom_drv.so
%{_datadir}/X11/xorg.conf.d/50-wacom.conf
%{_mandir}/man4/wacom.4*

