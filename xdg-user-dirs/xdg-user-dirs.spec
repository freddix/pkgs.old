Summary:	Tool to manage user directories
Name:		xdg-user-dirs
Version:	0.14
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	dc496ecde0e6a1e959bd8a38643f28fd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/user-dirs.*
%attr(755,root,root) %{_bindir}/xdg-user-dir
%attr(755,root,root) %{_bindir}/xdg-user-dirs-update

