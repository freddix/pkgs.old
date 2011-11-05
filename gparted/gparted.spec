Summary:	GNOME Partition Editor
Name:		gparted
Version:	0.10.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/gparted/%{name}-%{version}.tar.bz2
# Source0-md5:	d5b339eb5bef7a99ff73f750834b37b9
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-pkexec.patch
URL:		http://gparted.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtkmm-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	parted-devel
BuildRequires:	pkgconfig
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	polkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GParted stands for GNOME Partition Editor and is a graphical frontend
to parted. Among other features it supports creating, resizing, moving
and copying of partitions.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f %{name}.desktop

%build
%{__gnome_doc_prepare}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-libparted-dmraid
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not required
rm -rf $RPM_BUILD_ROOT%{_includedir}/GParted

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/gparted
%attr(755,root,root) %{_sbindir}/gpartedbin
%{_datadir}/polkit-1/actions/org.freddix.pkexec.gparted.policy

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_mandir}/man8/gparted.8.*

