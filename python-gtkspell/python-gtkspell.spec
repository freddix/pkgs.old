%define		module	gnome-python-extras
#
Summary:	Python GDA bindings
Name:		python-gtkspell
Version:	2.25.3
Release:	2
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-python-extras/2.25/%{module}-%{version}.tar.bz2
# Source0-md5:	9f3b7ec5c57130b96061cb486b79c076
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkspell-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	enchant-hunspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pydefsdir	%(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%prep
%setup -qn %{module}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-eggrecent	\
	--disable-eggtray	\
	--disable-gda		\
	--disable-gdl		\
	--disable-gksu		\
	--disable-gksu2		\
	--disable-gksuui	\
	--disable-gtkhtml2	\
	--disable-gtkmozembed	\
	--enable-gtkspell
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*.la,*/*.la}
%py_postclean /usr/share/pygtk/2.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkspell.so

