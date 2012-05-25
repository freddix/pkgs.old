Summary:	freedesktop.org standard compliant icons
Name:		tango-icon-theme
Version:	0.8.90
Release:	5
License:	Creative Commons License (see COPYING)
Group:		Themes
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	0795895d2f20eddcbd2bffe94ed431a6
Patch0:		%{name}-convert.patch
Patch1:		%{name}-rsvg.patch
URL:		http://tango.freedesktop.org/
BuildRequires:	ImageMagick-coders
BuildRequires:	ImageMagick-devel
BuildRequires:	icon-naming-utils >= 0.8.90
BuildRequires:	pkg-config
BuildRequires:	rsvg
BuildArch:	noarch
Provides:	xdg-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freedesktop.org standard compliant icons.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-png-creation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/Tango

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_iconsdir}/Tango

