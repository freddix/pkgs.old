Summary:	A graphical Audio CD ripper and encoder
Name:		asunder
Version:	2.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	4996860f552879fd8abdc87d1c6c7530
URL:		http://littlesvr.ca/asunder/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libcddb-devel
BuildRequires:	pkg-config
Requires:	cdparanoia-III
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asunder is a graphical Audio CD ripper and encoder for Linux.

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
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/bs_BA

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/asunder
%{_desktopdir}/asunder.desktop
%{_pixmapsdir}/asunder.png

