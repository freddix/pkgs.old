%define		module	PyQt4
#
Summary:	Python bindings for the Qt4 toolkit
Name:		python-%{module}
Version:	4.8.6
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	9bfd7b08b8e438b83cc50d5c58191f97
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	QtAssistant-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtDesigner-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtHelp-devel
BuildRequires:	QtMultimedia-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtScriptTools-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	python-dbus-devel
BuildRequires:	python-sip-devel >= 4.12.2
BuildRequires:	qt4-build
BuildRequires:	qt4-phonon-devel
BuildRequires:	qt4-qmake
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-libs
Requires:	python-sip >= 4.12.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt4 is a set of Python bindings for the Qt4 toolkit. The bindings
are implemented as a set of Python modules: QtAssistant, QtCore,
QtGui, QtNetwork, QtOpenGL, QtSql, QtSvg and QtXml.

%package devel
Summary:	Files needed to build other bindings based on Qt4
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt4 classes (e.g. KDE or your own).

# no extra qt4 Requires, just follow qt4 deps

%package QtAssistant
Summary:        Qt Assistant Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtAssistant
Qt Assistant Python bindings.

%package QtDBus
Summary:        Qt DBus Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus

%description QtDBus
Qt DBus Python bindings.

%package QtDesigner
Summary:        Qt Designer Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtDesigner
Qt Designer Python bindings.

%package QtHelp
Summary:        Qt Help Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtHelp
Qt Help Python bindings.

%package QtNetwork
Summary:        Qt Network Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtNetwork
Qt Network Python bindings.

%package QtOpenGL
Summary:        Qt OpenGL Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtOpenGL
Qt OpenGL Python bindings.

%package QtScript
Summary:        Qt Script Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtScript
Qt Script Python bindings.

%package QtScriptTools
Summary:        Qt ScriptTools Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtScriptTools
Qt ScriptTools Python bindings.

%package QtSql
Summary:        Qt Sql Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtSql
Qt Sql Python bindings.

%package QtSvg
Summary:        Qt Svg Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtSvg
Qt Svg Python bindings.

%package QtTest
Summary:        Qt Test Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtTest
Qt Assistant Python bindings.

%package QtWebKit
Summary:        Qt WebKit Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtWebKit
Qt WebKit Python bindings.

%package QtXmlPatterns
Summary:        Qt Xml Patterns Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description QtXmlPatterns
Qt Xml Patterns Python bindings.

%package phonon
Summary:        Qt phonon bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description phonon
Qt phonon Python bindings.

%prep
%setup -qn PyQt-x11-gpl-%{version}

sed -i 's,pyuic.py,pyuic.pyc,' configure.py
sed -i 's/qt_shared = lines\[.*\]/qt_shared = "y"/' configure.py

%build
echo yes | %{__python} configure.py	\
	-c -j 2				\
	-a				\
	-b %{_bindir}			\
	-d %{py_sitedir}		\
	-q "%{_bindir}/qmake-qt4"	\
	-v %{_sipfilesdir}/%{module}	\
	LIBDIR_QT="%{_libdir}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/PyQt4
%attr(755,root,root) %{py_sitedir}/PyQt4/Qt.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtCore.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtGui.so
%attr(755,root,root) %{py_sitedir}/PyQt4/QtXml.so
%{py_sitedir}/PyQt4/*.py[co]
%{py_sitedir}/PyQt4/uic

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4

%files QtAssistant
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtAssistant.so

%files QtDBus
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/dbus/mainloop/qt.so

%files QtDesigner
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtDesigner.so

%files QtHelp
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtHelp.so

%files QtNetwork
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtNetwork.so

%files QtOpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtOpenGL.so

%files QtScript
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtScript.so

%files QtScriptTools
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtScriptTools.so

%files QtSql
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtSql.so

%files QtSvg
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtSvg.so

%files QtTest
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtTest.so

%files QtWebKit
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtWebKit.so

%files QtXmlPatterns
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/QtXmlPatterns.so

%files phonon
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/phonon.so

