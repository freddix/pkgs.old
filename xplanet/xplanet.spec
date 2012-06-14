Summary:	Render a planetary image into an X window
Name:		xplanet
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://downloads.sourceforge.net/xplanet/%{name}-%{version}.tar.gz
# Source0-md5:	41f7db2ccd1d8b4b989cacaf9adfe692
URL:		http://xplanet.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window. Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively. The other terrestrial planets
may also be displayed. The Xplanet home page has links to locations
with map files.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# force using nl_langinfo interface instead of libcharset
%configure \
	ac_cv_header_localcharset_h=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/xplanet

