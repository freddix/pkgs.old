Summary:	Document layout analysis and optical character recognition system
Name:		ocrfeeder
Version:	0.7.6
Release:	1.3
License:	GPL v3
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/ocrfeeder/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	c0095e91ea0f6fb6c3ce798911d21b96
Patch0:		%{name}-build.patch
Patch1:		%{name}-drop-libgnome.patch
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires(post,postun):  desktop-file-utils
%pyrequires_eq	python-modules
Requires:	ghostscript
Requires:	python-ReportLab
Requires:	python-gtkspell
Requires:	python-pyenchant
Requires:	python-pygoocanvas
Requires:	python-pygtk
Requires:	unpaper
Suggests:	cuneiform
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OCRFeeder is a document layout analysis and optical character
recognition system.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# runtime deps
sed -i "s/AX_PYTHON_MODULE.*//g" configure.ac

%build
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%dir %{py_sitescriptdir}/ocrfeeder
%{py_sitescriptdir}/ocrfeeder/*.py*
%{py_sitescriptdir}/ocrfeeder/feeder
%{py_sitescriptdir}/ocrfeeder/odf
%{py_sitescriptdir}/ocrfeeder/studio
%{py_sitescriptdir}/ocrfeeder/util
%{_mandir}/man1/ocrfeeder-cli.1*
%{_mandir}/man1/ocrfeeder.1*

