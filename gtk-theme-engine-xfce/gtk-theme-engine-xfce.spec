%define		xfce_version	4.9.0
#
Summary:	Xfce theme engine
Name:		gtk-theme-engine-xfce
Version:	2.99.3
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://archive.xfce.org/src/xfce/gtk-xfce-engine/2.99/gtk-xfce-engine-%{version}.tar.bz2
# Source0-md5:	c5cc3748f64428c082d72afb21e24f77
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce engine and themes.

%prep
%setup -qn gtk-xfce-engine-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libxfce.so
%{_datadir}/themes/Xfce*

