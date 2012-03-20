Summary:	Documentation utilities for GNOME
Name:		gnome-doc-utils
Version:	0.20.7
Release:	1
License:	GPL v2+/LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-doc-utils/0.20/%{name}-%{version}.tar.xz
# Source0-md5:	c07b2759433ec9e337712a20c63113fb
Patch0:		%{name}-no_scrollkeeper_update.patch
URL:		http://www.gnome.org/
BuildRequires:	libxslt-devel
BuildRequires:	python
Requires(post,postun):	rarian
Requires:	libxslt-progs
Requires:	python-libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
%define		_pkgconfigdir		%{_datadir}/pkgconfig

%description
Collection of documentation utilities for GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal} -I m4 -I tools
%{__automake}
%{__autoconf}
%configure \
	--disable-scrollkeeper
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	pkgconfigdir="%{_pkgconfigdir}"

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --all-name --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
%{_datadir}/%{name}
%{_datadir}/xml/gnome
#%{_datadir}/xml/mallard
%{_mandir}/man1/xml2po.1*
%{_pkgconfigdir}/*.pc

%dir %{py_sitescriptdir}/xml2po
%dir %{py_sitescriptdir}/xml2po/modes
%{py_sitescriptdir}/xml2po/*.py[co]
%{py_sitescriptdir}/xml2po/modes/*.py[co]

