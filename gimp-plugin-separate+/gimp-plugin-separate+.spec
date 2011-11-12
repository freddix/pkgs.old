%define		rname	separate+

Summary:	Plug-in providing rudimentary CMYK support for GIMP
Name:		gimp-plugin-%{rname}
Version:	0.5.8
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Graphics
Source0:	http://iij.dl.sourceforge.jp/separate-plus/47873/%{rname}-%{version}.zip
# Source0-md5:	442e546bb451ab7450ddca79e36e21e8
URL:		http://cimg.sourceforge.net/greycstoration/
BuildRequires:	gimp-devel
BuildRequires:	lcms-devel
BuildRequires:	pkgconfig
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
A plug-in providing rudimentary CMYK support for GIMP.

%prep
%setup -qn %{rname}-%{version}

sed -i -e 's|-O3|%{rpmcflags}|g' Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%find_lang gimp20-separate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gimp20-separate.lang
%defattr(644,root,root,755)
%doc README README_ICC_COLORSPACE
%attr(755,root,root) %{plugindir}/icc_colorspace
%attr(755,root,root) %{plugindir}/separate
%attr(755,root,root) %{plugindir}/separate_import

