Summary:	D-Bus service providing high-level OBEX client and server side functionality
Name:		obex-data-server
Version:	0.4.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: http://www.bluez.org/download.html
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
# Source0-md5:	961ca5db6fe9c97024e133cc6203cc4d
URL:		http://wiki.muiline.com/obex-data-server
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	openobex-devel >= 1.4
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obex-data-server is D-Bus service providing high-level OBEX client and
server side functionality. It currently supports OPP, FTP profiles and
Bluetooth transport.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-bip=gdk-pixbuf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
%{_sysconfdir}/obex-data-server
%{_mandir}/man1/obex-data-server.1*

