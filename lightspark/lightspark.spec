Summary:	Open source flash player
Name:		lightspark
Version:	0.5.7
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	http://edge.launchpad.net/lightspark/trunk/lightspark-0.5.7/+download/%{name}-%{version}.tar.gz
# Source0-md5:	613b4baad01159726dd8c5133c6ff526
URL:		http://lightspark.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	ftgl-devel
BuildRequires:	gettext
BuildRequires:	glew-devel
BuildRequires:	gtkglext-devel
BuildRequires:	libtool
BuildRequires:	libxml++-devel
BuildRequires:	llvm-devel
BuildRequires:	nasm
BuildRequires:	pcre-cxx-devel
BuildRequires:	pcre-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%{_libdir}/browser-plugins

%description
Lightspark is a modern, free, open-source flash player implementation.

%package -n browser-plugin-%{name}
Summary:	Browser plugin for Flash rendering
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n browser-plugin-%{name}
Browser plugin for rendering Flash content using Lightspark.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DAUDIO_BACKEND=pulse		\
	-DCOMPILE_PLUGIN=1		\
	-DLIB_INSTALL_DIR=%{_lib}	\
	-DPLUGIN_DIRECTORY=%{plugindir} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/lightspark
%attr(755,root,root) %{_bindir}/tightspark
%dir %{_libdir}/lightspark
%attr(755,root,root) %{_libdir}/lightspark/liblightspark.so.*.*.*
%attr(755,root,root) %{_libdir}/lightspark/liblightspark.so.*.*
%attr(755,root,root) %{_libdir}/lightspark/liblightspark.so
%{_datadir}/lightspark
%{_mandir}/man1/lightspark.1*

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/liblightsparkplugin.so

