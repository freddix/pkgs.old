Summary:	Sinclair ZX Spectrum Emulator
Name:		fbzx
Version:	2.9.0
Release:	1
License:	GPL v3+
Group:		Applications/Emulators
Source0:	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
# Source0-md5:	fc815e219d86e40a5780c6cf6a6c2cf3
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.rastersoft.com/programas/fbzxesp.html
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	rsvg
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Sinclair ZX Spectrum Emulator, designed to work both in framebuffer
and X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__sed} -i 's,spectrum-roms,%{_datadir}/%{name}/spectrum-roms,' emulator.c

%build
%{__make} \
	CC="%{__cc}"		\
	OPTFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rsvg-convert %{name}.svg \
	-o $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AMSTRAD CAPABILITIES README* TODO VERSIONS
%attr(755,root,root) %{_bindir}/fbzx
%{_datadir}/%{name}
%{_desktopdir}/fbzx.desktop
%{_pixmapsdir}/fbzx.png

