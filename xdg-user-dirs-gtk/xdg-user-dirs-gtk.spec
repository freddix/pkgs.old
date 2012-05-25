Summary:	Companion to xdg-user-dirs
Name:		xdg-user-dirs-gtk
Version:	0.9
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/xdg-user-dirs-gtk/0.9/%{name}-%{version}.tar.xz
# Source0-md5:	345227186331147fafffbe09d8b0082b
BuildRequires:	intltool
BuildRequires:	autoconf
BuildRequires:	gtk+3-devel
Requires:	xdg-user-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-user-dirs-gtk is a companion to xdg-user-dirs that integrates
it into the Gnome desktop and Gtk+ applications.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	XDG_USER_DIRS_UPDATE=/usr/bin/xdg-user-dirs-update
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{kg,ps}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
/etc/xdg/autostart/*.desktop

