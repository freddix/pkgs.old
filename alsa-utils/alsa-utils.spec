Summary:	Advanced Linux Sound Architecture (ALSA) - Utils
Name:		alsa-utils
Version:	1.0.24.2
Release:	4
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/utils/%{name}-%{version}.tar.bz2
# Source0-md5:	8238cd57cb301d1c36bcf0ecb59ce6b2
Source1:	alsa-restore.service
Source2:	alsa-store.service
Source3:	alsactl.conf
Source4:	snd-seq-midi.conf
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
Requires:	awk
Requires:	dialog
Requires:	diffutils
Requires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This packages contains ALSA command line utilities.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%configure \
	--disable-alsaconf	\
	--sbindir=/sbin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/alsa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/arecord.1
echo ".so aplay.1" > $RPM_BUILD_ROOT%{_mandir}/man1/arecord.1

install -D %{SOURCE1} $RPM_BUILD_ROOT/%{_lib}/systemd/system/basic.target.wants/alsa-restore.service
install -D %{SOURCE2} $RPM_BUILD_ROOT/%{_lib}/systemd/system/shutdown.target.wants/alsa-store.service
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/alsa/alsactl.conf
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/modules-load.d/snd-seq-midi.conf

install -d $RPM_BUILD_ROOT/%{_lib}/alsa
mv $RPM_BUILD_ROOT%{_datadir}/alsa/init $RPM_BUILD_ROOT/%{_lib}/alsa

ln -s /%{_lib}/alsa/init $RPM_BUILD_ROOT%{_datadir}/alsa/init

install -d $RPM_BUILD_ROOT%{_sbindir}
ln -s /sbin/alsactl $RPM_BUILD_ROOT%{_sbindir}/alsactl

%find_lang alsa-utils --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f alsa-utils.lang
%defattr(644,root,root,755)
%doc README ChangeLog

%dir %{_datadir}/alsa/init
%dir /var/lib/alsa
%dir /%{_lib}/alsa
/%{_lib}/alsa/init

%attr(755,root,root) /sbin/alsactl
%attr(755,root,root) %{_bindir}/aconnect
%attr(755,root,root) %{_bindir}/alsaloop
%attr(755,root,root) %{_bindir}/alsamixer
%attr(755,root,root) %{_bindir}/alsaucm
%attr(755,root,root) %{_bindir}/amidi
%attr(755,root,root) %{_bindir}/amixer
%attr(755,root,root) %{_bindir}/aplay
%attr(755,root,root) %{_bindir}/aplaymidi
%attr(755,root,root) %{_bindir}/arecord
%attr(755,root,root) %{_bindir}/arecordmidi
%attr(755,root,root) %{_bindir}/aseqdump
%attr(755,root,root) %{_bindir}/aseqnet
%attr(755,root,root) %{_bindir}/iecset
%attr(755,root,root) %{_bindir}/speaker-test
%attr(755,root,root) %{_sbindir}/alsactl

%{_sysconfdir}/alsa/alsactl.conf
%{_sysconfdir}/modules-load.d/snd-seq-midi.conf
/%{_lib}/systemd/system/basic.target.wants/alsa-restore.service
/%{_lib}/systemd/system/shutdown.target.wants/alsa-store.service

%{_datadir}/alsa/speaker-test
%{_datadir}/sounds/alsa

%{_mandir}/man1/aconnect.1*
%{_mandir}/man1/alsactl.1*
%{_mandir}/man1/alsaloop.1*
%{_mandir}/man1/alsamixer.1*
%{_mandir}/man1/amidi.1*
%{_mandir}/man1/amixer.1*
%{_mandir}/man1/aplay.1*
%{_mandir}/man1/aplaymidi.1*
%{_mandir}/man1/arecord.1*
%{_mandir}/man1/arecordmidi.1*
%{_mandir}/man1/aseqdump.1*
%{_mandir}/man1/aseqnet.1*
%{_mandir}/man1/iecset.1*
%{_mandir}/man1/speaker-test.1*
%{_mandir}/man7/alsactl_init.7*

