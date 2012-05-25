Summary:	Lightweight addressbook
Name:		contacts
Version:	0.12
Release:	3
License:	GPL v2
Group:		Applications
Source0:	http://download.gnome.org/sources/contacts/0.12/%{name}-%{version}.tar.bz2
# Source0-md5:	0bb01fc7479a497550ea5f2e0035b9d8
Patch0:		%{name}-schemas_install.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	evolution-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contacts is a small, lightweight addressbook that use

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install	\
	--enable-gconf=no		\
	--enable-gnome-vfs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang Contacts

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f Contacts.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/contacts.*
%{_mandir}/man1/contacts.1*

