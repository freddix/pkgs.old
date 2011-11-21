Summary:	Wammu - Gammu GUI - Mobile phone manager
Name:		wammu
Version:	0.36
Release:	1
License:	GPL v2+
Group:		X11/Applications/Communications
Source0:	http://dl.cihar.com/wammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	065186e6d08bffd7f95ae000046904cb
URL:		http://wammu.eu/
BuildRequires:	gammu-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python = %py_ver
Requires:	gammu
Requires:	python-gammu
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wammu is mobile phone manager running on Linux, Windows and possibly
other platforms, where Gammu and wxPython works. The communication is
made by Gammu library.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/Wammu/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ README
%attr(755,root,root) %{_bindir}/wammu
%attr(755,root,root) %{_bindir}/wammu-configure
%dir %py_sitescriptdir/Wammu
%{py_sitescriptdir}/Wammu/*.py[co]
%{_datadir}/Wammu
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%{_mandir}/man1/%{name}*.*
%lang(cs) %{_mandir}/cs/man1/%{name}*.*
%lang(de) %{_mandir}/de/man1/%{name}*.*
%lang(it) %{_mandir}/it/man1/%{name}*.*
%lang(nl) %{_mandir}/nl/man1/%{name}*.*
%lang(ru) %{_mandir}/ru/man1/%{name}*.*
%lang(sk) %{_mandir}/sk/man1/%{name}*.*
%lang(es) %{_mandir}/es/man1/%{name}*.*
%lang(fr) %{_mandir}/fr/man1/%{name}*.*
%lang(pt_BR) %{_mandir}/pt_BR/man1/%{name}*.*

