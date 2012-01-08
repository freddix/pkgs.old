%define		svnrev	r2018

Summary:	Free FireWire Audio Drivers
Name:		libffado
Version:	2.999.0
Release:	0.%{svnrev}.2
License:	LGPL
Group:		Libraries
# svn checkout http://subversion.ffado.org/ffado/branches/libffado-2.0 libffado-2.0-svn
# mv libffado-2.0-svn libffado-2.0.1
# tar -cf - libffado-2.0.1 | xz -9e -c > libffado-2.0.1.tar.xz
Source0:	%{name}-%{version}-%{svnrev}.tar.xz
# Source0-md5:	786f31facd417e6207e429f50af0e15e
#Source0:	http://www.ffado.org/files/%{name}-%{version}.tar.gz
URL:		http://www.ffado.org/
BuildRequires:	dbus-c++-devel
BuildRequires:	expat-devel
BuildRequires:	glibmm-devel
BuildRequires:	libavc1394-devel
BuildRequires:	libconfig-c++-devel
BuildRequires:	libiec61883-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libxml++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	python-PyQt4-QtDBus
BuildRequires:	python-PyQt4-devel
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free FireWire Audio Drivers.

%package utils
Summary:	FFADO utilities
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus
Requires:	python-PyQt4
Requires:	python-PyQt4-QtDBus

%description utils
FFADO utilities.

%package devel
Summary:	Header files for ffado library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ffado library.

%prep
%setup -q

%build
LDFLAGS="%{rpmldflags} -fPIC"
export LDFLAGS

sed -i -e 's|-O2|%{rpmcflags}|g' SConstruct

%{__scons} \
	BUILD_TESTS=0			\
	DEBUG=0				\
	DESTDIR=$RPM_BUILD_ROOT		\
	DIST_TARGET="%{_target_cpu}"	\
	PREFIX=%{_prefix}		\
	WILL_DEAL_WITH_XDG_MYSELF="True"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__scons} install		\
	DEBUG=0			\
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}	\
	WILL_DEAL_WITH_XDG_MYSELF="True"

%py_ocomp $RPM_BUILD_ROOT%{_datadir}
%py_comp $RPM_BUILD_ROOT%{_datadir}
%py_postclean

install support/xdg/hi64-apps-ffado.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/ffado.png

cat > $RPM_BUILD_ROOT%{_desktopdir}/ffado-mixer.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=ffado-mixer
Icon=ffado
Terminal=false
Name=FFADO mixer
Comment=Mixer for firewire based (semi-) professional audio cards
Categories=Qt;Audio;AudioVideo;Mixer;Settings;HardwareSettings;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libffado.so.?
%attr(755,root,root) %{_libdir}/libffado.so.*.*.*

%files utils
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ffado-bridgeco-downloader
%attr(755,root,root) %{_bindir}/ffado-dbus-server
%attr(755,root,root) %{_bindir}/ffado-diag
%attr(755,root,root) %{_bindir}/ffado-fireworks-downloader
%attr(755,root,root) %{_bindir}/ffado-mixer

%{_datadir}/libffado/configuration
%{_datadir}/dbus-1/services/org.ffado.Control.service

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/python
%{_datadir}/%{name}/*.xml
%{py_sitescriptdir}/ffado

%{_desktopdir}/ffado-mixer.desktop
%{_pixmapsdir}/ffado.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffado.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc

