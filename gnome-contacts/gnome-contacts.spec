Summary:	Contacts manager for GNOME
Name:		gnome-contacts
Version:	3.4.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-contacts/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	e5eb42a24316d247405fd42e872f88ae
URL:		https://live.gnome.org/ThreePointOne/Features/Contacts
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	folks-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libgee-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	telepathy-glib-devel
Requires(post,postun):	glib-gio-gsettings
Requires:	evolution-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%prep
%setup -q

%build
mkdir m4
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_desktopdir}/%{name}.desktop

