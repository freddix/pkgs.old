%define		org_name	xfce4-mailwatch-plugin

Summary:	Mailwatch plugin for XFCE panel
Name:		xfce4-plugin-mailwatch
Version:	1.1.0
Release:	16
License:	GPL v2
Group:		X11/Applications
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{org_name}-%{version}.tar.bz2
# Source0-md5:	f84dce86be1d7f25f169f262aaacee4e
Patch0:		%{name}-xfce4ui.patch
Patch1:		%{name}-gnutls.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-mbox-refresh.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/template
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template plugin for XFCE panel.

%prep
%setup -qn %{org_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i -e 's|nb_NO|nb|' -e 's|pt_PT|pt|' po/LINGUAS
mv po/{pt_PT,pt}.po
mv po/{nb_NO,nb}.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/%{org_name}
%{_datadir}/xfce4/panel-plugins/mailwatch.desktop
%{_iconsdir}/hicolor/*/*/*

