Summary:	Xfce development tools
Name:		xfce4-dev-tools
Version:	4.10.0
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://archive.xfce.org/src/xfce/xfce4-dev-tools/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	372b74f432e7e02d946c2ea9d3de2805
URL:		http://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build Xfce from CVS. In
addition it contains the Xfce developer's handbook.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	macrodir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4

