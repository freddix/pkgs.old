%define		git_ver	04f158d5e820c08f615441708371dd1ee99feb20

Summary:	Lightweight, NETWM compliant panel for X11
Name:		bmpanel2
Version:	2.2
Release:	0.%{git_ver}.1
License:	MIT License
Group:		X11/Applications
#Source0:	http://bmpanel2.googlecode.com/files/%{name}-%{version}%{_rc}.tar.gz
#
# git clone --depth=1 git://github.com/nsf/bmpanel2.git
# cd bmpanel2
# git archive --format=tar --prefix=bmpanel2-2.2/ HEAD | xz -9 > bmpanel2-2.2-git_ver.tar.xz
#
Source0:	%{name}-%{version}-%{git_ver}.tar.xz
# Source0-md5:	8d97c5631c9d04c23c48926d40f6d131
URL:		http://code.google.com/p/bmpanel2/
BuildRequires:	cairo-devel
BuildRequires:	cmake
BuildRequires:	docbook-dtd45-xml
BuildRequires:	fontconfig-devel
BuildRequires:	libxml2-progs
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-libX11-devel
Requires:	python-pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight, NETWM compliant panel for X11.

%prep
%setup -q

sed -i 's/position bottom/position top/' themes/*/theme

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

%py_comp $RPM_BUILD_ROOT%{_datadir}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{py_sitescriptdir}/*.py[co]
%{_mandir}/man1/bmpanel2.*

