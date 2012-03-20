Summary:	HDR Image compositor
Name:		luminance-hdr
Version:	2.2.1
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/project/qtpfsgui/luminance/2.2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	9c64d89bda6cea685d1158dd3cbc823b
Patch0:		%{name}-desktop.patch
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	gsl-devel
BuildRequires:	libgomp-devel
BuildRequires:	libraw-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	gtk+
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Luminance HDR is an open source graphical user interface
application that aims to provide a workflow for HDR imaging.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%dir %{_datadir}/luminance-hdr
%dir %{_datadir}/luminance-hdr/i18n
%{_datadir}/luminance-hdr/help
%lang(cs) %{_datadir}/luminance-hdr/i18n/lang_cs.qm
%lang(de) %{_datadir}/luminance-hdr/i18n/lang_de.qm
%lang(es) %{_datadir}/luminance-hdr/i18n/lang_es.qm
%lang(fi) %{_datadir}/luminance-hdr/i18n/lang_fi.qm
%lang(fr) %{_datadir}/luminance-hdr/i18n/lang_fr.qm
%lang(hu) %{_datadir}/luminance-hdr/i18n/lang_hu.qm
%lang(id) %{_datadir}/luminance-hdr/i18n/lang_id.qm
%lang(it) %{_datadir}/luminance-hdr/i18n/lang_it.qm
%lang(pl) %{_datadir}/luminance-hdr/i18n/lang_pl.qm
%lang(ro) %{_datadir}/luminance-hdr/i18n/lang_ro.qm
%lang(ru) %{_datadir}/luminance-hdr/i18n/lang_ru.qm
%lang(tr) %{_datadir}/luminance-hdr/i18n/lang_tr.qm

