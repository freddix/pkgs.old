Summary:	The JACK Audio Connection Kit
Name:		jack-audio-connection-kit
Version:	0.121.3
Release:	2
License:	LGPL v2.1+ (libjack), GPL v2+ (the rest)
Group:		Daemons
Source0:	http://jackaudio.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	35f470f7422c37b33eb965033f7a42e8
Source1:	%{name}-tmpfiles.conf
Patch0:		%{name}-optimized-cflags.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-strip.patch
URL:		http://jackit.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libcap-devel
BuildRequires:	libffado-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	readline-devel
BuildConflicts:	jack-libs
BuildConflicts:	tschack-libs
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	jack
Obsoletes:	tschack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*%{_bindir}/jackd
%define		_noautochrpath	.*%{_libdir}/jackd

%description
JACK is a low-latency audio server, written primarily for the Linux
operating system. It can connect a number of different applications to
an audio device, as well as allowing them to share audio between
themselves. Its clients can run in their own processes (ie. as a
normal application), or can they can run within a JACK server (ie. a
"plugin").

%package libs
Summary:	JACK library
License:	LGPL
Group:		Libraries
Obsoletes:	jack-libs
Obsoletes:	tschack-libs

%description libs
Shared JACK library.

%package devel
Summary:	Header files for JACK
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	jack-devel
Obsoletes:	tschack-devel

%description devel
Header files for the JACK Audio Connection Kit.

%package apidocs
Summary:	JACK API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
JACK  API documentation.

%package driver-firewire
Summary:	FireWire sound driver for JACK
License:	GPL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	jack-driver-firewire
Obsoletes:	tschack-driver-firewire

%description driver-firewire
FreeBoB/FFADO sound driver for JACK.

%package utils
Summary:	JACK utilities
License:	GPL
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Obsoletes:	jack-utils
Obsoletes:	tschack-utils

%description utils
JACK Audio Connection Kit utilities.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoheader}
%{__automake}
%{__autoconf}

%configure \
	--disable-coreaudio		\
	--disable-freebob		\
	--disable-oldtrans		\
	--disable-oss			\
	--disable-portaudio		\
	--disable-static		\
	--enable-dynsimd		\
	--enable-ensure-mlock		\
	--enable-mmx			\
	--enable-posix-shm		\
	--enable-preemption-check	\
	--enable-resize			\
	--enable-sse			\
	--enable-timestamps		\
	--with-default-tmpdir=/run/jack	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/tmpfiles.d/jack.conf

rm -f $RPM_BUILD_ROOT%{_libdir}/jack/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# note: COPYING only specifies which parts fall under GPL and LGPL
%doc AUTHORS TODO COPYING

%dir %{_libdir}/jack
/etc/tmpfiles.d/jack.conf

%attr(755,root,root) %{_bindir}/alsa_in
%attr(755,root,root) %{_bindir}/alsa_out
%attr(755,root,root) %{_bindir}/jack_bufsize
%attr(755,root,root) %{_bindir}/jack_connect
%attr(755,root,root) %{_bindir}/jack_disconnect
%attr(755,root,root) %{_bindir}/jack_freewheel
%attr(755,root,root) %{_bindir}/jack_load
%attr(755,root,root) %{_bindir}/jack_load_test
%attr(755,root,root) %{_bindir}/jack_netsource
%attr(755,root,root) %{_bindir}/jack_samplerate
%attr(755,root,root) %{_bindir}/jack_server_control
%attr(755,root,root) %{_bindir}/jack_session_notify
%attr(755,root,root) %{_bindir}/jack_transport
%attr(755,root,root) %{_bindir}/jack_unload
%attr(755,root,root) %{_bindir}/jack_wait
%attr(755,root,root) %{_bindir}/jackd

%attr(755,root,root) %{_libdir}/jack/a2j_in.so
%attr(755,root,root) %{_libdir}/jack/jack_alsa.so
%attr(755,root,root) %{_libdir}/jack/jack_alsa_midi.so
%attr(755,root,root) %{_libdir}/jack/jack_dummy.so
%attr(755,root,root) %{_libdir}/jack/jack_net.so
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libjack*.so.?
%attr(755,root,root) %{_libdir}/libjack*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjack*.so
%{_includedir}/jack
%{_pkgconfigdir}/jack.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*

%files driver-firewire
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/jack/jack_firewire.so

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jack_alias
%attr(755,root,root) %{_bindir}/jack_evmon
%attr(755,root,root) %{_bindir}/jack_impulse_grabber
%attr(755,root,root) %{_bindir}/jack_iodelay
%attr(755,root,root) %{_bindir}/jack_latent_client
%attr(755,root,root) %{_bindir}/jack_lsp
%attr(755,root,root) %{_bindir}/jack_metro
%attr(755,root,root) %{_bindir}/jack_midi_dump
%attr(755,root,root) %{_bindir}/jack_midiseq
%attr(755,root,root) %{_bindir}/jack_midisine
%attr(755,root,root) %{_bindir}/jack_monitor_client
%attr(755,root,root) %{_bindir}/jack_rec
%attr(755,root,root) %{_bindir}/jack_showtime
%attr(755,root,root) %{_bindir}/jack_simple_client
%attr(755,root,root) %{_bindir}/jack_simple_session_client
%attr(755,root,root) %{_bindir}/jack_transport_client
%attr(755,root,root) %{_libdir}/jack/inprocess.so
%attr(755,root,root) %{_libdir}/jack/intime.so

