Summary:	Fast and easy painting application
Name:		mypaint
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.gna.org/mypaint/%{name}-%{version}.tar.bz2
# Source0-md5:	dcd43933746a4579e7994f506e097823
URL:		http://mypaint.intilinux.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	scons
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gdk-pixbuf
Requires(post,postun):	hicolor-icon-theme
Requires:	pydoc
Requires:	python-numpy-numarray
Requires:	python-protobuf
Requires:	python-pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast and easy painting application.

%prep
%setup -q

sed -i -e "s|python\ =.*|python='%{__python}'|g" SConstruct

%build
%{__scons} \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__scons} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.la

%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}

find $RPM_BUILD_ROOT%{_datadir}/%{name} -name \*.py -exec rm -f {} \;

mv $RPM_BUILD_ROOT%{_datadir}/locale/{nn_NO,nn}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*.so

%dir %{_datadir}/%{name}
%dir %{_libdir}/%{name}

%{_datadir}/%{name}/backgrounds
%{_datadir}/%{name}/brushes
%{_datadir}/%{name}/brushlib
%{_datadir}/%{name}/gui
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/pixmaps

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/a*/*.png
%{_iconsdir}/hicolor/*/a*/*.svg

