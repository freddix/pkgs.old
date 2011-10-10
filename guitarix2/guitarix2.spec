Summary:	Simple Linux Rock Guitar Amplifier for JACK
Name:		guitarix2
Version:	0.19.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/guitarix/%{name}-%{version}.tar.bz2
# Source0-md5:	6b103e306225577a479a601c4eff5a30
BuildRequires:	boost-devel
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsndfile-devel
BuildRequires:	zita-convolver-devel
Requires:	jack-audio-connection-kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guitarix is a simple Linux Rock Guitar Amplifier for jack (Jack Audio
Connektion Kit) with one input and two outputs. Designed, with GTK and
faust, to get nice thrash/metal/rock guitar sounds.

%prep
%setup -qn %{name}-%{version}

sed -i -e 's/boost_program_options-mt/boost_program_options/g' \
    -i -e 's/-O3 -DNDEBUG/-DNDEBUG/g' wscript

sed -i 's/Categories.*/Categories=GTK;AudioVideo;Audio;Midi;/' guitarix.desktop

%build
./waf configure \
	--cxxflags="%{rpmcxxflags} -Wall -std=c++0x"	\
	--destdir=$RPM_BUILD_ROOT			\
	--prefix=%{_prefix}
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT
./waf install \
	--destdir=$RPM_BUILD_ROOT

%find_lang guitarix

%clean
rm -rf $RPM_BUILD_ROOT

%files -f guitarix.lang
%defattr(644,root,root,755)
%doc README changelog
%attr(755,root,root) %{_bindir}/guitarix
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/gx_head
%{_datadir}/ladspa/rdf/guitarix.rdf
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

