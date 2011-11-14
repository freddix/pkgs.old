Summary:	misc fonts
Name:		xorg-font-misc
Version:	1.1.2
Release:	1
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-misc-misc-%{version}.tar.bz2
# Source0-md5:	c88eb44b3b903d79fb44b860a213e623
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-util
BuildRequires:	xorg-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
misc-misc fonts.

%package base
Summary:	Base fonts (fixed)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires(triggerpostun):	fontpostinst
Requires:	fontpostinst

%description base
Base fonts (fixed) needed to start X server.

%package ISO8859-1
Summary:	ISO-8859-1 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-1
ISO-8859-1 basic raster fonts.

%package ISO8859-2
Summary:	ISO-8859-2 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-2
ISO-8859-2 basic raster fonts.

%package ISO8859-3
Summary:	ISO-8859-3 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-3
ISO-8859-3 basic raster fonts.

%package ISO8859-4
Summary:	ISO-8859-4 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-4
ISO-8859-4 basic raster fonts.

%package ISO8859-5
Summary:	ISO-8859-5 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-5
Basic ISO-8859-5 raster fonts.

%description ISO8859-5 -l pl
Podstawowe fonty rastrowe ISO-8859-5.

%package ISO8859-6
Summary:	ISO-8859-6 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-6
ISO-8859-6 basic raster fonts.

%package ISO8859-7
Summary:	ISO-8859-7 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-7
ISO-8859-7 basic raster fonts.

%package ISO8859-8
Summary:	ISO-8859-8 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-8
ISO-8859-8 basic raster fonts.

%package ISO8859-9
Summary:	ISO-8859-9 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-9
ISO-8859-9 basic raster fonts.

%package ISO8859-10
Summary:	ISO-8859-10 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-10
ISO-8859-10 basic raster fonts.

%package ISO8859-11
Summary:	ISO-8859-11 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-11
ISO-8859-11 basic raster fonts.

%package ISO8859-12
Summary:	ISO-8859-12 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-12
ISO-8859-12 basic raster fonts.

%package ISO8859-13
Summary:	ISO-8859-13 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-13
ISO-8859-13 basic raster fonts.

%package ISO8859-14
Summary:	ISO-8859-14 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-14
ISO-8859-14 basic raster fonts.

%package ISO8859-15
Summary:	ISO-8859-15 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-15
ISO-8859-15 basic raster fonts.

%package ISO8859-16
Summary:	ISO-8859-16 basic raster fonts
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc

%description ISO8859-16
ISO-8859-16 basic raster fonts.

%prep
%setup -q -n font-misc-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo 'fixed -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso8859-1' \
    > $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.xorg-fonts-base

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%post base
fontpostinst misc

%postun base
fontpostinst misc

%post ISO8859-1
fontpostinst misc

%postun ISO8859-1
fontpostinst misc

%post ISO8859-2
fontpostinst misc

%postun ISO8859-2
fontpostinst misc

%post ISO8859-3
fontpostinst misc

%postun ISO8859-3
fontpostinst misc

%post ISO8859-4
fontpostinst misc

%postun ISO8859-4
fontpostinst misc

%post ISO8859-5
fontpostinst misc

%postun ISO8859-5
fontpostinst misc

%post ISO8859-6
fontpostinst misc

%postun ISO8859-6
fontpostinst misc

%post ISO8859-7
fontpostinst misc

%postun ISO8859-7
fontpostinst misc

%post ISO8859-8
fontpostinst misc

%postun ISO8859-8
fontpostinst misc

%post ISO8859-9
fontpostinst misc

%postun ISO8859-9
fontpostinst misc

%post ISO8859-10
fontpostinst misc

%postun ISO8859-10
fontpostinst misc

%post ISO8859-11
fontpostinst misc

%postun ISO8859-11
fontpostinst misc

%post ISO8859-12
fontpostinst misc

%postun ISO8859-12
fontpostinst misc

%post ISO8859-13
fontpostinst misc

%postun ISO8859-13
fontpostinst misc

%post ISO8859-14
fontpostinst misc

%postun ISO8859-14
fontpostinst misc

%post ISO8859-15
fontpostinst misc

%postun ISO8859-15
fontpostinst misc

%post ISO8859-16
fontpostinst misc

%postun ISO8859-16
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/misc/*.pcf.gz
%exclude %{_fontsdir}/misc/*-ISO8859-*.pcf.gz

%files base
%defattr(644,root,root,755)
%{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz
%{_fontsdir}/misc/fonts.alias.xorg-fonts-base
%ghost %{_fontsdir}/misc/fonts.dir

%files ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-1.pcf.gz
%exclude %{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz

%files ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-2.pcf.gz
#%{_fontsdir}/misc/fonts.alias.%{name}-ISO8859-2

%files ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-3.pcf.gz

%files ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-4.pcf.gz

%files ISO8859-5
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-5.pcf.gz

#%files ISO8859-6
#%defattr(644,root,root,755)
#%%{_fontsdir}/misc/*ISO8859-6.pcf.gz

%files ISO8859-7
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-7.pcf.gz

%files ISO8859-8
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-8.pcf.gz

%files ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-9.pcf.gz

%files ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-10.pcf.gz

%files ISO8859-11
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-11.pcf.gz

#%files ISO8859-12
#%defattr(644,root,root,755)
#%%{_fontsdir}/misc/*ISO8859-12.pcf.gz

%files ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-13.pcf.gz

%files ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-14.pcf.gz

%files ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-15.pcf.gz

%files ISO8859-16
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-16.pcf.gz

