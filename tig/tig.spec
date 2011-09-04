Summary:	Text-mode interface for git
Name:		tig
Version:	0.18
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
# Source0-md5:	4fa9e33c5daa76b6fed11e068405356f
URL:		http://jonas.nitro.dk/tig/
BuildRequires:	ncurses-devel
Requires:	git
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tig is a git repository browser that additionally can act as a
pager for output from various git commands.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags} -I/usr/include/ncursesw" \
	LDLIBS=-lncursesw

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-doc-man \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO *.html contrib/tigrc
%attr(755,root,root) %{_bindir}/tig
%{_mandir}/man*/*

