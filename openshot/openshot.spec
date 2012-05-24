Summary:	Non-linear video editor for linux
Name:		openshot
Version:	1.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://launchpad.net/openshot/1.4/1.4.2/+download/%{name}-%{version}.tar.gz
# Source0-md5:	16fea75be6b1fc9d31c6a30a81f85a38
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
Requires(post,postun):	shared-mime-info
Requires:	ffmpeg
Requires:	frei0r
Requires:	mlt
Requires:	python-PIL
Requires:	python-httplib2
Requires:	python-mlt
Requires:	python-pygoocanvas
Requires:	python-pygtk-glade
Requires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Non-linear video editor for linux.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install	\
	--root=$RPM_BUILD_ROOT	\
	--optimize=2

sed -i -e 's|openshot.py|openshot.pyc|g' \
	$RPM_BUILD_ROOT%{_bindir}/*

install openshot/themes/tango/icons/openshot.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}

#%%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/openshot
%attr(755,root,root) %{_bindir}/openshot-render
%{py_sitescriptdir}/%{name}
%{_datadir}/mime/packages/openshot.xml
%{_desktopdir}/openshot.desktop
%{_pixmapsdir}/openshot.png
%{_pixmapsdir}/openshot.svg
%{_mandir}/man1/openshot.1*
%{_mandir}/man1/openshot-render.1*

