Summary:	Video editor
Name:		pitivi
Version:	0.15.2
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.15/%{name}-%{version}.tar.xz
# Source0-md5:	e0e379fca759025140ac1316819b2173
URL:		http://www.pitivi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	rpm-pythonprov
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	Zope-Interface
Requires:	gstreamer-gnonlin
Requires:	gstreamer-plugins-good
Requires:	python-gstreamer
Requires:	python-pycairo
Requires:	python-pygoocanvas
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
Requires:	python-setuptools
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PiTiVi is a program for video editing based on the GStreamer.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__automake}
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
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pitivi
%{_libdir}/pitivi
%{_datadir}/mime/packages/pitivi.xml
%{_datadir}/pitivi
%{_desktopdir}/pitivi.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/%{name}.1*

