%define		gitver	9992b32a15392686d86bdc9ca9a965da9addcb5c

Summary:	XRender benchmark
Name:		xorg-app-xrenderbenchmark
Version:	1.0.2
Release:	0.%{gitver}.4
License:	MIT
Group:		X11/Applications
Source0:	http://cgit.freedesktop.org/~aplattner/xrenderbenchmark/snapshot/xrenderbenchmark-%{gitver}.tar.bz2
# Source0-md5:	499e60ec348a01fb7f0e04e49695334b
Patch0:		%{name}-fixes.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XRender benchmarking program.

%prep
%setup -qn xrenderbenchmark-%{gitver}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xrenderbenchmark

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a images/*.png $RPM_BUILD_ROOT%{_datadir}/xrenderbenchmark

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xrenderbenchmark
%{_datadir}/xrenderbenchmark

