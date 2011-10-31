Summary:	Convolution Engine for JACK
Name:		jconvolver
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	f1a33f0f455961a7b21b56bdb0f725b1
Source1:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-reverbs.tar.bz2
# Source1-md5:	a33ec6a97fac039400f7674f3bde4ca9
Patch0:		%{name}-make.patch
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zita-convolver-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-O3

%description
Jconv is a Convolution Engine for JACK, based on FFT convolution and
using non-uniform partition sizes: small ones at the start of the IR
and building up to the most efficient size further on. It can perform
zero-delay processing with moderate CPU load. Jconv uses the
convolution engine designed for Aella, a convolution application for
reverberation processing (to be announced later). This distributes the
calculation over up to five threads, one for each partition size,
running at priorities just below the the one of JACK's processing
thread. This engine will become a separate library as soon as I can
find the time to write the user documentation.

%prep
%setup -q -a1
%patch0 -p1

%build
%{__make} -C source \
	CXX="%{__cxx}"		\
	CXXFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

cp -aR config-files/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -aR reverbs $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README README.CONFIG
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

