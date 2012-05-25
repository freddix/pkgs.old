Summary:	Claws Mail is an email client (and news reader) based on GTK+
Name:		claws-mail
Version:	3.8.0
Release:	2
License:	GPL v3
Group:		X11/Applications/Mail
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	df9f1657d7f34959a2205344d952c2e3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	compface-devel
BuildRequires:	enchant-devel
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gpgme-devel
BuildRequires:	gtk+-devel
BuildRequires:	libetpan-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Suggests:	bogofilter
Suggests:	enchant-hunspell
Suggests:	hunspell-dictionaries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Claws Mail is an email client (and news reader), based on GTK+.

%package devel
Summary:        Claws Mail development files.
Group:          X11/Development/Libraries

%description devel
Claws Mail development package.

%prep
%setup -q

# locale fixes
%{__rm} po/stamp-po
mv -f po/{id_ID,id}.po
mv -f po/{pt_PT,pt}.po
%{__sed} -i -e 's,pt_PT,pt,g;s,id_ID,id,g' src/codeconv.c
%{__sed} -i -e 's,pt_PT,pt,g;s,id_ID,id,g' configure.ac

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-dillo-viewer-plugin	\
	--disable-jpilot		\
	--disable-spamassassin-plugin	\
	--disable-static		\
	--enable-bogofilter-plugin	\
	--enable-crash-dialog		\
	--enable-enchant		\
	--enable-gnutls			\
	--enable-ldap			\
	--enable-pgpmime-plugin		\
	--with-config-dir=.config/claws-mail
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE_NOTES TODO
%attr(755,root,root) %{_bindir}/claws-mail
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_mandir}/man1/claws-mail.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

