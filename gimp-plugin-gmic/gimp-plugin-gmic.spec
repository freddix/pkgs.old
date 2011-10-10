%define		plugin	gmic

Summary:	G'MIC interpreter embedded in a GIMP plugin
Name:		gimp-plugin-%{plugin}
Version:	1.5.0.4
Release:	1
License:	CeCILL FREE SOFTWARE LICENSE
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/sourceforge/gmic/%{plugin}_%{version}.tar.gz
# Source0-md5:	8a1fe1207fb09fa2d515ccd484be521c
Source1:	%{name}-configure.in
Patch0:		%{name}-build.patch
BuildRequires:	GraphicsMagick-c++-devel
BuildRequires:	OpenCV-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	fftw3-devel
BuildRequires:	gimp-devel
BuildRequires:	libstdc++-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
G'MIC interpreter embedded in a GIMP plugin.

%prep
%setup -qn %{plugin}-%{version}
%patch0 -p1

install %{SOURCE1} configure.in

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} -j1 -C src gimp		\
	CC="%{__cxx}"			\
	OPTCXXFLAGS="%{rpmcxxflags}"	\
	OPTLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}

install -D src/gmic_gimp $RPM_BUILD_ROOT%{plugindir}/gmic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{plugindir}/gmic

