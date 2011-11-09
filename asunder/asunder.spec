Summary:	A graphical Audio CD ripper and encoder
Name:		asunder
Version:	2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	05419a29fd31321f0823c3f90ee1b911
URL:		http://littlesvr.ca/asunder/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libcddb-devel
BuildRequires:	pkg-config
Requires:	cdparanoia-III
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It allows to save tracks from an Audio CD as WAV, MP3, Ogg, and/or
FLAC.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/asunder.desktop

mv $RPM_BUILD_ROOT%{_datadir}/locale/ur{_PK,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/asunder
%{_desktopdir}/asunder.desktop
%{_pixmapsdir}/asunder.png

