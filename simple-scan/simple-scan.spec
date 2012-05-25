Summary:	Simple scanning utility
Name:		simple-scan
Version:	3.4.1
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://launchpad.net/simple-scan/3.4/3.4.1/+download/%{name}-%{version}.tar.gz
# Source0-md5:	72872c66724bc90dc1fb462b40ac21d7
URL:		https://launchpad.net/simple-scan
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	colord-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vala
BuildRequires:	yelp-tools
Requires(post,postun):	glib-gio-gsettings
Requires:	gnome-icon-theme
Suggests:	colord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Scan is an easy-to-use application, designed to let users
connect their scanner and quickly have the image/document in an
appropriate format.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/simple-scan
%{_mandir}/man1/simple-scan.1*
%{_desktopdir}/simple-scan.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/simple-scan

