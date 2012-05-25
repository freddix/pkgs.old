Summary:	ID3 tag editor
Name:		easytag
Version:	2.1.6
Release:	13
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/easytag/%{name}-%{version}.tar.bz2
# Source0-md5:	6c5b9dc2bf1f3b0a11bd4efc81aaa9ee
Patch0:		%{name}-desktop.patch
URL:		http://easytag.sourceforge.net/
BuildRequires:	ImageMagick-coders
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	id3lib-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRequires:	wavpack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC, Ogg, MusePack and Monkey's Audio files. Its simple
and nice GTK+ interface makes tagging easier.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--disable-mp4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

convert -geometry 48x48 pixmaps/EasyTAG_icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/easytag.png

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO THANKS USERS-GUIDE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
%{_pixmapsdir}/easytag.png

