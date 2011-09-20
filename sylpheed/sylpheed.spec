%define		pre	%{nil}

Summary:	GTK+ based fast e-mail client
Name:		sylpheed
Version:	3.1.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
%if "%{pre}" == "%{nil}"
Source0:	http://sylpheed.sraoss.jp/sylpheed/v3.1/%{name}-%{version}.tar.bz2
# Source0-md5:	17100ab8ef5ef7e431bdbcff68bbf7b4
%else
Source0:	http://sylpheed.sraoss.jp/sylpheed/v3.1beta/%{name}-%{version}%{pre}.tar.bz2
# Source0-md5:	17100ab8ef5ef7e431bdbcff68bbf7b4
%endif
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-desktop.patch
URL:		http://sylpheed.sraoss.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	compface-devel
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkspell-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires(post,postun):	desktop-file-utils
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is an X based fast e-mail client which has features (or
go for it :-)) like:
- user-friendly and intuitive interface
- integrated NetNews client (partially implemented)
- ability of keyboard-only operation
- Mew/Wanderlust-like key bind
- multipart MIME
- unlimited multiple account handling
- assortment function
- address book
- SSL support

%package libs
Summary:	Sylpheed libraries
Group:		Libraries

%description libs
Sylpheed libraries.

%package devel
Summary:	Header files for Sylpheed libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Sylpheed
libraries.

%prep
%if "%{pre}" == "%{nil}"
%setup -q
%else
%setup -qn %{name}-%{version}%{pre}
%endif
%patch0 -p1
%patch1 -p1

mv -f po/{sr,sr@Latn}.po

%{__perl} -pi -e 's/ sr / sr\@Latn /' configure.in

%build
%{__libtoolize}
%{__aclocal} -I ac
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-updatecheck	\
	--disable-updatecheckplugin	\
	--enable-compface	\
	--enable-gpgme		\
	--enable-gtkspell	\
	--enable-ipv6		\
	--enable-ldap		\
	--enable-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_post

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/faq
%dir %{_datadir}/%{name}/manual

%{_datadir}/%{name}/faq/en
%lang(de) %{_datadir}/%{name}/faq/de
%lang(es) %{_datadir}/%{name}/faq/es
%lang(fr) %{_datadir}/%{name}/faq/fr
%lang(it) %{_datadir}/%{name}/faq/it

%{_datadir}/%{name}/manual/en
%lang(ja) %{_datadir}/%{name}/manual/ja

%{_desktopdir}/sylpheed.desktop
%{_pixmapsdir}/sylpheed.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsylp*.so.?
%attr(755,root,root) %{_libdir}/libsylp*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsylp*.so
%{_libdir}/libsylp*.la
%{_includedir}/sylpheed

