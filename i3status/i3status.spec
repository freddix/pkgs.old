Summary:	Status bar generator for i3
Name:		i3status
Version:	2.5.1
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://i3wm.org/i3status/%{name}-%{version}.tar.bz2
# Source0-md5:	28c27fc0c2294e12ae6ae390f3d89973
BuildRequires:	alsa-lib-devel
BuildRequires:	libconfuse-devel
BuildRequires:	libiw-devel
BuildRequires:	yajl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i3status is a small program (about 1500 SLOC) for generating a status
bar for i3bar, dzen2, xmobar or similar programs. It is designed to be
very efficient by issuing a very small number of system calls, as one
generally wants to update such a status line every second. This
ensures that even under high load, your status bar is updated
correctly. Also, it saves a bit of energy by not hogging your CPU
as much as spawning the corresponding amount of shell commands would.

%prep
%setup -q

%build
%{__make} \
	EXTRA_CFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/i3status
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i3status.conf
%{_mandir}/man1/i3status.1*

