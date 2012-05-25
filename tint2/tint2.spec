%define		svnrev	646

Summary:	Simple panel/taskbar made for modern window managers
Name:		tint2
Version:	0.11
Release:	0.%{svnrev}.1
License:	MIT
Group:		X11/Applications
#Source0:	http://tint2.googlecode.com/files/%{name}-%{version}.tar.bz2
#
# svn checkout http://tint2.googlecode.com/svn/trunk/ tint2-read-only
# mv tint2-read-only tint2-0.11
# find tint2-0.11 -name .svn | xargs rm -rf
# tar -c tint2-0.11/ -O | xz > tint2-0.11.tar.xz
Source0:	tint2-0.11.tar.xz
# Source0-md5:	c51d24f3936f15ddbce07d1b3b6f928e
URL:		http://code.google.com/p/tint2/wiki/Welcome
BuildRequires:	imlib2-devel
BuildRequires:	cairo-devel
BuildRequires:	pango-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXcomposite-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
Requires:	python-pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tint2 is a simple panel/taskbar made for modern x window managers.
It was specifically made for openbox3 but should also work with other
window managers (GNOME, KDE, etc...).
It's based on ttm code http://code.google.com/p/ttm/

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/tint2
%attr(755,root,root) %{_bindir}/tintwizard.py
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/%{name}/tint2rc
%{_datadir}/tint2
%{_mandir}/man1/tint2.1*

