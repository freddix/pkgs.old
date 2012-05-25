Summary:	ICC compatible color management system
Name:		argyllcms
Version:	1.4.0
Release:	1
License:	AGPL v3, MIT, GPL v2+, LGPL v2.1+, FDL v1.3
Group:		X11/Applications/Graphics
Source0:	http://people.freedesktop.org/~hughsient/releases/h%{name}-%{version}.tar.xz
# Source0-md5:	0f1a00fbbd5c458e8791970b414f684f
URL:		http://www.argyllcms.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXxf86vm-devel
Suggests:	shared-color-profiles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Argyll color management system supports accurate ICC profile
creation for acquisition devices, CMYK printers, film recorders and
calibration and profiling of displays.

%prep
%setup -qn h%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# they shouldn't put Makefile.am to ref_DATA
%{__rm} $RPM_BUILD_ROOT%{_datadir}/color/argyll/ref/Makefile.am

# no -devel package (headers not exported)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.{so,la}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/argyll

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Readme.txt
%doc doc/*.html doc/*.jpg doc/*.txt
%attr(755,root,root) %{_bindir}/*

%attr(755,root,root) %ghost %{_libdir}/libargyll.so.?
%attr(755,root,root) %ghost %{_libdir}/libargyllicc.so.?
%attr(755,root,root) %ghost %{_libdir}/libargyllusb.so.?
%attr(755,root,root) %{_libdir}/libargyll.so.*.*.*
%attr(755,root,root) %{_libdir}/libargyllicc.so.*.*.*
%attr(755,root,root) %{_libdir}/libargyllusb.so.*.*.*

%dir %{_datadir}/color/argyll
%{_datadir}/color/argyll/ref
/lib/udev/rules.d/55-Argyll.rules

