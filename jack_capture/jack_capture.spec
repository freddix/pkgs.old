Summary:	JACK recorder
Name:		jack_capture
Version:	0.9.57
Release:	2
License:	GPL v2 and BSD
Group:		X11/Applications
Source0:	http://archive.notam02.no/arkiv/src/%{name}-%{version}.tar.gz
# Source0-md5:	c78ddb7d6b9f1bbef20f663d7c3f99a5
Patch0:		%{name}-build.patch
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRequires:	which
Requires:	jack-audio-connection-kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JACK recorder.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -j1 \
	CC=%{__cc}	\
	CPP=%{__cxx}	\
	OPTIMIZE="%{rpmldflags} %{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_desktopdir}/jack_capture.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=jack_capture_gui2
Icon=gtk-media-record
Terminal=false
Name=JACK Capture
Comment=JACK recorder
Categories=GTK;Audio;Recorder;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop

