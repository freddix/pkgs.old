Summary:	nl80211 based CLI
Name:		iw
Version:	3.4
Release:	1
License:	BSD
Group:		Networking/Admin
Source0:	http://wireless.kernel.org/download/iw/%{name}-%{version}.tar.bz2
# Source0-md5:	a8ccfc936eb3603db7b60b67f4261f1f
URL:		http://wireless.kernel.org/en/users/Documentation/iw
BuildRequires:	libnl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
nl80211 based CLI configuration utility for wireless devices.

%prep
%setup -q
sed -i 's|-O2 -g|%{rpmcflags}|g' Makefile

%build

%if 0
# don't depend on git
cat > version.sh <<'EOF'
#!/bin/sh

VERSION="%{version}"
OUT="version.h"
echo "#define IW_VERSION \"$VERSION-nogit\"" > "$OUT"
EOF
%endif

%{__make} V=1 CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install iw $RPM_BUILD_ROOT%{_sbindir}
install iw.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

