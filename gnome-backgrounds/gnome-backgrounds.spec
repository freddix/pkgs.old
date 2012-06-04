Summary:	Set of backgrounds for GNOME desktop
Name:		gnome-backgrounds
Version:	3.4.2
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-backgrounds/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	eb4c0bd1ada92f2604187198cd483662
URL:		http://www.gnome.org/
BuildRequires:	intltool
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of backgrounds for GNOME desktop.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{as,ca@valencia,en@shaw,sii}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/gnome

