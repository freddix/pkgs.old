Summary:	Extra plugins for Claws Mail
Name:		claws-mail-extra-plugins
Version:	3.8.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	4776f6e0357a694f384349ac73b6da52
Patch0:		%{name}-geolocation.patch
URL:		http://www.claws-mail.org/plugins.php
BuildRequires:	claws-mail-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	libarchive-devel
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libchamplain-devel
BuildRequires:	libgdata-devel
BuildRequires:	libnotify-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
Requires:	claws-mail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugins_dir	%{_libdir}/claws-mail/plugins

%description
Extra plugins for Claws Mail.

%prep
%setup -q
%patch0 -p1

# id_ID -> id locale hacks
for i in `find -name id_ID.po -print`; do
	i=`echo $i | sed 's,/po/id_ID.po,,'`
	mv -f $i/po/{id_ID,id}.po
	%{__sed} -i -e 's,id_ID,id,g' $i/configure.ac
done

%build
for i in `find * -maxdepth 0 -type d -print`; do
	cd "$i"
	%{__autoconf}
	%configure \
		--disable-static
	%{__make}
	cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
for i in `find * -maxdepth 0 -type d -print`; do
	%{__make} -C "$i" install \
		DESTDIR=$RPM_BUILD_ROOT
done
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}
%{__rm} $RPM_BUILD_ROOT%{plugins_dir}/*.la

%find_lang acpi_notifier
%find_lang address_keeper
%find_lang archive
%find_lang attachwarner
%find_lang bsfilter_plugin
%find_lang clamd
%find_lang fancy
%find_lang geolocation_plugin
%find_lang gtkhtml2_viewer
%find_lang notification_plugin
%find_lang python_plugin
%find_lang rssyl
%find_lang spam_report
%find_lang tnef_parse
%find_lang vcalendar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES
%attr(755,root,root) %{plugins_dir}/*.so
