Summary:	aubio - library for audio labelling
Name:		aubio
Version:	0.3.2
Release:	15
License:	GPL v2+
Group:		Libraries
Source0:	http://aubio.piem.org/pub/%{name}-%{version}.tar.gz
# Source0-md5:	ffc3e5e4880fec67064f043252263a44
URL:		http://aubio.piem.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aubio is a library for audio labelling.

%package devel
Summary:	Header files for aubio library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for aubio library.

%package progs
Summary:	Example applications using aubio library
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description progs
A few examples of applications using aubio library:
- aubioonset: outputs the onset detected.
- aubionotes: uses both onset and pitch to extract symbolic music data
    from an audio source and emit MIDI like data.
- aubiocut: a Python script that takes an input sound and creates one
    new sample at each detected onset or beat. The slices produced by
    aubiocut are useful for use with a sequencer such as Hydrogen.
- aubiopitch: a Python script to extract pitch tracks from sound
  files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-alsa		\
	--enable-jack

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitedir}/aubio/_aubiowrapper.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libaubio.so.?
%attr(755,root,root) %ghost %{_libdir}/libaubioext.so.?
%attr(755,root,root) %{_libdir}/libaubio.so.*.*.*
%attr(755,root,root) %{_libdir}/libaubioext.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaubio.so
%attr(755,root,root) %{_libdir}/libaubioext.so
%{_libdir}/libaubio.la
%{_libdir}/libaubioext.la
%{_includedir}/%{name}
%{_pkgconfigdir}/aubio.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aubiocut
%attr(755,root,root) %{_bindir}/aubionotes
%attr(755,root,root) %{_bindir}/aubioonset
%attr(755,root,root) %{_bindir}/aubiopitch
%attr(755,root,root) %{_bindir}/aubiotrack
%{_datadir}/sounds/aubio

