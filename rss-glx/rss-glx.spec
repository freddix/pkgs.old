Summary:	The Really Slick Screensavers
Name:		rss-glx
Version:	0.9.1
Release:	4
Group:		X11/Applications
License:	GPL
Source0:	http://downloads.sourceforge.net/rss-glx/%{name}_%{version}.tar.bz2
# Source0-md5:	a772bd143cd8d141edf4d9eff9860ab3
URL:		http://rss-glx.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freealut-devel
BuildRequires:	glew-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openal-soft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
GLX screensavers for the X11 windowing system.

%prep
%setup -qn %{name}_%{version}

rm -f config.guess config.sub depcomp install-sh libtool ltmain.sh missing

%build
export CONFIG_SHELL=/bin/bash
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
bash %configure \
	--disable-static	\
	--with-configdir=%{_datadir}/xscreensaver
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/rss-glx_install.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xscreensaver/biof.xml
%{_datadir}/xscreensaver/busyspheres.xml
%{_datadir}/xscreensaver/colorfire.xml
%{_datadir}/xscreensaver/cyclone.xml
%{_datadir}/xscreensaver/drempels.xml
%{_datadir}/xscreensaver/euphoria.xml
%{_datadir}/xscreensaver/feedback.xml
%{_datadir}/xscreensaver/fieldlines.xml
%{_datadir}/xscreensaver/flocks.xml
%{_datadir}/xscreensaver/flux.xml
%{_datadir}/xscreensaver/helios.xml
%{_datadir}/xscreensaver/hufo_smoke.xml
%{_datadir}/xscreensaver/hufo_tunnel.xml
%{_datadir}/xscreensaver/hyperspace.xml
%{_datadir}/xscreensaver/lattice.xml
%{_datadir}/xscreensaver/lorenz.xml
%{_datadir}/xscreensaver/matrixview.xml
%{_datadir}/xscreensaver/pixelcity.xml
%{_datadir}/xscreensaver/plasma.xml
%{_datadir}/xscreensaver/skyrocket.xml
%{_datadir}/xscreensaver/solarwinds.xml
%{_datadir}/xscreensaver/spirographx.xml
%{_datadir}/xscreensaver/sundancer2.xml
%{_mandir}/man1/*

