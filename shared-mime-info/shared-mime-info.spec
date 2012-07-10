Summary:	Shared MIME-info specification
Name:		shared-mime-info
Version:	1.0
Release:	3
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.xz
# Source0-md5:	901b7977dbb2b71d12d30d4d8fb97028
Source1:	audio.list
Source2:	compressed.list
Source3:	document.list
Source4:	image.list
Source5:	video.list
Source6:	misc.list
URL:		http://www.freedesktop.org/wiki/Software/shared-mime-info
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-utils
BuildRequires:	glib-gio-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the freedesktop.org shared MIME info database.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-update-mimedb
%{__make}

db2html shared-mime-info-spec.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_desktopdir}/defaults.list <<EOF
[Default Applications]
EOF

cat %{SOURCE1} >> $RPM_BUILD_ROOT%{_desktopdir}/defaults.list
cat %{SOURCE2} >> $RPM_BUILD_ROOT%{_desktopdir}/defaults.list
cat %{SOURCE3} >> $RPM_BUILD_ROOT%{_desktopdir}/defaults.list
cat %{SOURCE4} >> $RPM_BUILD_ROOT%{_desktopdir}/defaults.list
cat %{SOURCE5} >> $RPM_BUILD_ROOT%{_desktopdir}/defaults.list
cat %{SOURCE6} >> $RPM_BUILD_ROOT%{_desktopdir}/defaults.list

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%preun
# remove dirs and files created by update-mime-database
if [ "$1" = "0" ]; then
	rm -rf /usr/share/mime/*
fi

%files
%defattr(644,root,root,755)
%doc shared-mime-info-spec README NEWS
%attr(755,root,root) %{_bindir}/update-mime-database
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages
%{_datadir}/mime/packages/freedesktop.org.xml
%{_desktopdir}/defaults.list
%{_mandir}/man*/*
%{_npkgconfigdir}/shared-mime-info.pc

