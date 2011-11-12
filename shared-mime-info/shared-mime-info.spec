Summary:	Shared MIME-info specification
Name:		shared-mime-info
Version:	0.91
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.xz
# Source0-md5:	982a211560ba4c47dc791ccff34e8fbc
Source1:	audio.list
Source2:	compressed.list
Source3:	document.list
Source4:	image.list
Source5:	video.list
Source6:	x-handlers.list
URL:		http://www.freedesktop.org/wiki/Software/shared-mime-info
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-utils
BuildRequires:	glib-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types
of files. Frequently, it is necessary to work out the correct MIME
type for a file. This is generally done by examining the file's name
or contents, and looking up the correct MIME type in a database.

For interoperability, it is useful for different programs to use the
same database so that different programs agree on the type of a file,
and new rules for determining the type apply to all programs.

This specification attempts to unify the type-guessing systems
currently in use by GNOME, KDE and ROX. Only the name-to-type and
contents-to-type mappings are covered by this spec; other MIME type
information, such as the default handler for a particular type, or the
icon to use to display it in a file manager, are not covered since
these are a matter of style.

In addition, freedesktop.org provides a shared database in this format
to avoid inconsistencies between desktops. This database has been
created by converting the existing KDE and GNOME databases to the new
format and merging them together.

%package devel
Summary:	Pkgconfig file
Group:		Development
Requires:	pkgconfig

%description devel
Pkgconfig file.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-update-mimedb
%{__make}

db2html shared-mime-info-spec.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

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

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc

