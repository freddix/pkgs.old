Summary:	Video converter
Name:		transmageddon
Version:	0.20
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://www.linuxrising.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ce1cdc366d10c8b3bcc7b73afb08b627
Patch0:		%{name}-brain-damaged-po.patch
URL:		http://www.linuxrising.org/
BuildRequires:	pkg-config
BuildRequires:	rpm-pythonprov
Requires:	gstreamer-ffmpeg
Requires:	gstreamer-fluendo-mpegdemux
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gstreamer-plugins-ugly
Requires:	python-gstreamer >= 0.10.22
Requires:	python-pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program transkodujący pliki wideo.

%prep
%setup -q
%patch0 -p1

sed -i -e 's|transmageddon.py|transmageddon.pyc|' bin/transmageddon.in
sed -i -e 's|Categories.*|Categories=GTK;AudioVideo;Video;|' transmageddon.desktop.in.in

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/transmageddon/*.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/transmageddon

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ui
%{_datadir}/%{name}/*.py[co]
%{_datadir}/%{name}/*.svg
%{_datadir}/%{name}/profiles
%{_datadir}/gstreamer-0.10/presets/*.prs

%{_desktopdir}/transmageddon.desktop
%{_pixmapsdir}/transmageddon.svg
%{_mandir}/man1/transmageddon.1*

