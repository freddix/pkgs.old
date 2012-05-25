Summary:	murrine theme
Name:		gtk-theme-engine-murrine
Version:	0.98.1.1
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/murrine/0.98/murrine-%{version}.tar.bz2
# Source0-md5:	ea2eeb5f83b0b9d730e7f49693a77bcc
Patch0:		%{name}-glib.patch
URL:		http://cimi.netsons.org/pages/murrine.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Murrine" is an Italian word meaning the glass artworks done by
Venicians glass blowers. They're absolutely wonderful and colorful.
Murrine has this object to provide the ability to make your desktop
look like a "Murrina", which is the Italian singular of the name
"Murrine".

%prep
%setup -qn murrine-%{version}
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-animation
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/gtk-engines/*.xml

