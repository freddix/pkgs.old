Summary:	Visual diff and merge tool
Name:		meld
Version:	1.5.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/gnome/sources/meld/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	2f3929551d876ff45acf21b2c1e3e71a
URL:		http://meld.sourceforge.net/
BuildRequires:	gettext-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	rarian
%pyrequires_eq	python-libs
Requires:	python-pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%prep
%setup -q

sed -i -e 's|.py|.pyc|g' meld/vc/__init__.py

# broken
rm po/{hu,ja,ru}.po

%build
%{__make} \
	prefix=/usr	\
	libdir_=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}	\
	libdir_=%{py_sitedir}

%py_postclean

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/meld
%{py_sitedir}/meld
%{_datadir}/meld
%{_desktopdir}/meld.desktop
%{_iconsdir}/hicolor/*/apps/*.*

