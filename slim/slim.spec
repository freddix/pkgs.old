Summary:	SLiM - a desktop-independent graphical login managaer
Name:		slim
Version:	1.3.3
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/slim/%{name}-%{version}.tar.gz
# Source0-md5:	ce53e44c1e4a2eacf5bb7688ee2a5de8
Source1:	%{name}.service
Source2:	%{name}.pamd
Source3:	%{name}-tmpfiles.conf
# freddix default theme
Source10:	background.png
Source11:	panel.png
Source12:	slim.theme
Patch0:		%{name}-config.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-vt.patch
Patch3:		%{name}-fix-pam-authentication-with-pam_unix2.patch
URL:		http://slim.berlios.de/
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libXft-devel
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXrender-devel
Requires(post,preun):	/bin/systemctl
Requires:	mktemp
Requires:	pam
Requires:	xorg-app-xinit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLiM is a Desktop-independent graphical login manager for X11, derived
from Login.app.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake .. \
	-DUSE_CONSOLEKIT=yes	\
	-DUSE_PAM=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/slim/themes/freddix

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT/%{_lib}/systemd/system/%{name}.service
install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/%{name}
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/tmpfiles.d/%{name}.conf

install %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/slim/themes/freddix
install %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/slim/themes/freddix
install %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/slim/themes/freddix

%clean
rm -rf $RPM_BUILD_ROOT

%post
export NORESTART="yes"
%systemd_post slim.service

%preun
%systemd_preun slim.service

%postun
%systemd_reload

%files
%defattr(644,root,root,755)
%doc ChangeLog README THEMES TODO xinitrc.sample
%dir %{_sysconfdir}/slim
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/slim/slim.conf
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/slim
%{_sysconfdir}/tmpfiles.d/%{name}.conf
%attr(755,root,root) %{_bindir}/*
/%{_lib}/systemd/system/slim.service
%{_mandir}/man1/slim.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/themes/default
%{_datadir}/%{name}/themes/freddix

