Summary:	Advanced color picker
Name:		gpick
Version:	0.2.4
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://gpick.googlecode.com/files/%{name}_%{version}.tar.gz
# Source0-md5:	2c043cb95798c2b078264ed14ca0c6fd
Patch0:		%{name}-build.patch
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	pkg-config
BuildRequires:	scons
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):  desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced color picker.

%prep
%setup -qn %{name}_%{version}
%patch0 -p1

%build
cat > user-config.py << END
CC='%{__cc}'
CFLAGS='%{rpmcflags}'
CXX='%{__cxx}'
CXXFLAGS='%{rpmcxxflags}'
LDFLAGS='%{rpmldflags}'
END
%{__scons}

%install
rm -rf $RPM_BUILD_ROOT

%{__scons} --no-cache install	\
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc share/doc/gpick/copyright
%attr(755,root,root) %{_bindir}/gpick
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_mandir}/man1/gpick.1*

