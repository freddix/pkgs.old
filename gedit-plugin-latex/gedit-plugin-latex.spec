%include	/usr/lib/rpm/macros.perl

Summary:	LaTeX plugin for gedit
Name:		gedit-plugin-latex
Version:	3.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://download.gnome.org/sources/gedit-latex/3.4/gedit-latex-%{version}.tar.xz
# Source0-md5:	fe59264c7bc1c6a3eebfcc8cf4f6725f
URL:		http://live.gnome.org/Gedit/LaTeXPlugin
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
%pyrequires_eq	python-modules
Requires:	gedit-plugins-python
Requires:	ghostscript
Requires:	python-pyenchant
Requires:	python-pygtk-glade
Requires:	rubber
Requires:	tetex-format-pdflatex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX plugin for gedit.

%prep
%setup -qc
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins

cp -R . $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins

%py_comp $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins

find $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins -name "*.py" -exec rm {} \;

rm $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*/{ChangeLog,COPYING,INSTALL}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc GeditLaTeXPlugin/ChangeLog
%{_libdir}/gedit-2/plugins/GeditLaTeXPlugin
%{_libdir}/gedit-2/plugins/GeditLaTeXPlugin.gedit-plugin

