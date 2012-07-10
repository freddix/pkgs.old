Summary:	The Qt GUI application framework
Name:		qt
Version:	4.8.2
Release:	5
License:	GPL/QPL
Group:		X11/Libraries
Source0:	http://releases.qt-project.org/qt4/source/qt-everywhere-opensource-src-%{version}.tar.gz
# Source0-md5:	3c1146ddf56247e16782f96910a8423b
Source2:	%{name}-qtconfig.desktop
Patch1:		%{name}-buildsystem.patch
Patch2:		%{name}-improve-cups-support.patch
Patch3:		%{name}-support-cflags-with-commas.patch
Patch4:		%{name}-build-lib-static.patch
Patch5:		%{name}-x11_fonts.patch
Patch6:		%{name}-no-hardcoded-font-aliases.patch
Patch7:		%{name}-enable-lcdfilter.patch
Patch8:		%{name}-glib.patch
Patch9:		%{name}-dont-use-ld-gold.patch
URL:		http://www.qtsoftware.com/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
#BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
#BuildRequires:	postgresql-devel
BuildRequires:	sed
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-libSM-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-libXtst-devel
BuildRequires:	zlib-devel
# when building it tries to link with system qt instead of built one
BuildConflicts:	QtCore-devel <= %{version}
BuildConflicts:	QtScript-devel <= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%description
Qt is a complete C++ application development framework, which includes
a class library and tools for multiplatform development and
internationalization. Using Qt, a single source code tree can build
applications that run natively on different platforms (Windows,
Unix/Linux, Mac OS X, embedded Linux).

%package -n Qt3Support
Summary:	Qt3 compatibility library
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description -n Qt3Support
Qt3 compatibility library.

%package -n Qt3Support-devel
Summary:	Qt3 compatibility library - development files
Group:		X11/Development/Libraries
Requires:	Qt3Support = %{version}-%{release}
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtNetwork-devel = %{version}-%{release}
Requires:	QtSql-devel = %{version}-%{release}
Requires:	QtXml-devel = %{version}-%{release}

%description -n Qt3Support-devel
Qt3 compatibility library - development files.

%package -n QtCLucene
Summary:	QtCLucene full text search library wrapper
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}

%description -n QtCLucene
QtCLucene full text search library wrapper.

%package -n QtCLucene-devel
Summary:	QtCLucene full text search library wrapper - development files
Group:		X11/Development/Libraries
Requires:	QtCLucene = %{version}-%{release}
Requires:	QtCore-devel = %{version}-%{release}

%description -n QtCLucene-devel
QtCLucene full text search library wrapper - development files.

%package -n QtCore
Summary:	Core classes used by other modules
Group:		X11/Libraries
Obsoletes:	QtAssistant

%description -n QtCore
Core classes used by other modules.

%package -n QtCore-devel
Summary:	Core classes used by other modules - development files
Group:		X11/Development/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	glib-devel
Requires:	libstdc++-devel
Requires:	zlib-devel
Obsoletes:      QtAssistant-devel

%description -n QtCore-devel
Core classes used by other modules - development files.

%package -n QtDBus
Summary:	Qt classes for D-BUS support
Group:		X11/Libraries
Requires:	QtXml = %{version}-%{release}

%description -n QtDBus
This module provides classes for D-BUS support. D-BUS is an
Inter-Process Communication (IPC) and Remote Procedure Calling (RPC)
mechanism originally developed for Linux to replace existing and
competing IPC solutions with one unified protocol.

%package -n QtDBus-devel
Summary:	Qt classes for D-BUS support - development files
Group:		X11/Development/Libraries
Requires:	QtDBus = %{version}-%{release}
Requires:	QtXml-devel = %{version}-%{release}

%description -n QtDBus-devel
Qt classes for D-BUS support - development files.

%package -n QtDeclarative
Summary:	QtDeclarative - QML language engine library
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtOpenGL = %{version}-%{release}
Requires:	QtScript = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}
Requires:	QtSvg = %{version}-%{release}
Requires:	QtXmlPatterns = %{version}-%{release}
# for qmlwebkitplugin plugin
Requires:	QtWebKit = %{version}-%{release}

%description -n QtDeclarative
QtDeclarative is the QML language engine library. QML is a declarative
language oriented on JavaScript.

%description -n QtDeclarative -l pl.UTF-8
QtDeclarative to biblioteka języka QML. QML jest deklaratywnym
językiem zorientowanym na JavaScript.

%package -n QtDeclarative-devel
Summary:	Development files for QtDeclarative - QML language engine library
Group:		X11/Development/Libraries
Requires:	QtDeclarative = %{version}-%{release}
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtNetwork-devel = %{version}-%{release}
Requires:	QtScript-devel = %{version}-%{release}

%description -n QtDeclarative-devel
Development files for QtDeclarative - QML language engine library.

%description -n QtDeclarative-devel -l pl.UTF-8
Pliki programistyczne QtDeclarative - biblioteki języka QML.

%package -n QtDeclarative-static
Summary:	Static version of QtDeclarative - QML language engine library
Summary(pl.UTF-8):	Statycza wersja QtDeclarative - biblioteki języka QML
Group:		X11/Development/Libraries
Requires:	QtDeclarative-devel = %{version}-%{release}

%description -n QtDeclarative-static
Static version of QtDeclarative - QML language engine library.

%description -n QtDeclarative-static -l pl.UTF-8
Statycza wersja QtDeclarative - biblioteki języka QML.

%package -n QtDesigner
Summary:	Qt classes for extending Qt Designer
Group:		X11/Libraries
Requires:	QtGui = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtScript = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}
# for plugins
Requires:	Qt3Support = %{version}-%{release}
Requires:	QtDBus = %{version}-%{release}
Requires:	QtDeclarative = %{version}-%{release}
Requires:	QtOpenGL = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}
Requires:	QtSvg = %{version}-%{release}
Requires:	QtWebKit = %{version}-%{release}
Requires:	QtXmlPatterns = %{version}-%{release}
Obsoletes:	qt4-designer-libs

%description -n QtDesigner
This module provides classes that allow you to create your own custom
widget plugins for Qt Designer, and classes that enable you to access
Qt Designer's components.

%package -n QtDesigner-devel
Summary:	Qt classes for extending Qt Designer - development files
Group:		X11/Development/Libraries
Requires:	QtDesigner = %{version}-%{release}
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtScript-devel = %{version}-%{release}
Requires:	QtXml-devel = %{version}-%{release}

%description -n QtDesigner-devel
Qt classes for extending Qt Designer - development files.

%package -n QtGui
Summary:	Graphical User Interface components
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
# for qtracegraphicssystem plugin
Requires:	QtNetwork = %{version}-%{release}

%description -n QtGui
Graphical User Interface components.

%package -n QtGui-devel
Summary:	Graphical User Interface components - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 1:2.0.0
Requires:	libpng-devel >= 2:1.0.8
Requires:	xorg-libSM-devel
Requires:	xorg-libXcursor-devel
Requires:	xorg-libXext-devel
Requires:	xorg-libXfixes-devel
Requires:	xorg-libXi-devel
Requires:	xorg-libXinerama-devel
Requires:	xorg-libXrandr-devel
Requires:	xorg-libXrender-devel

%description -n QtGui-devel
Graphical User Interface components - development files.

%package -n QtHelp
Summary:	Qt classes for integrating online documentation in applications
Group:		X11/Libraries
Requires:	QtCLucene = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description -n QtHelp
QtHelp module includes tools for generating and viewing Qt help files.
In addition it provides classes for accessing help contents
programatically to be able to integrate online help into Qt
applications.

%package -n QtHelp-devel
Summary:	Qt classes for integrating online documentation in applications - development files
Group:		X11/Development/Libraries
Requires:	QtCLucene-devel = %{version}-%{release}
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtHelp = %{version}-%{release}
Requires:	QtSql-devel = %{version}-%{release}
Requires:	QtXml-devel = %{version}-%{release}

%description -n QtHelp-devel
Qt classes for integrating online documentation in applications -
development files.

%package -n QtMultimedia
Summary:	Qt classes for multimedia programming
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}

%description -n QtMultimedia
Qt classes for multimedia programming.

%package -n QtMultimedia-devel
Summary:	Qt classes for multimedia programming - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtMultimedia = %{version}-%{release}

%description -n QtMultimedia-devel
Qt classes for multimedia programming - development files.

%package -n QtNetwork
Summary:	Qt classes for network programming
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
# the rest for qnmbearer plugin
Requires:	QtDBus = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description -n QtNetwork
Qt classes for network programming.

%package -n QtNetwork-devel
Summary:	Qt classes for network programming - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}

%description -n QtNetwork-devel
Qt classes for network programming - development files.

%package -n QtOpenGL
Summary:	OpenGL support classes
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}

%description -n QtOpenGL
OpenGL support classes.

%package -n QtOpenGL-devel
Summary:	OpenGL support classes - development files
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtOpenGL = %{version}-%{release}

%description -n QtOpenGL-devel
OpenGL support classes - development files.

%package -n QtScript
Summary:	Qt classes for scripting applications
Group:		X11/Development/Libraries
Requires:	QtCore = %{version}-%{release}

%description -n QtScript
The QtScript module provides classes to handle scripts inside
applications.

%package -n QtScript-devel
Summary:	Qt classes for scripting applications - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtScript = %{version}-%{release}

%description -n QtScript-devel
Qt classes for scripting applications - development files.

%package -n QtScriptTools
Summary:	Qt classes for scripting applications
Group:		X11/Development/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtScript = %{version}-%{release}

%description -n QtScriptTools
The QtScriptTools module provides classes to handle scripts inside
applications.

%package -n QtScriptTools-devel
Summary:	Qt classes for scripting applications - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtScript-devel = %{version}-%{release}
Requires:	QtScriptTools = %{version}-%{release}

%description -n QtScriptTools-devel
Qt classes for scriptin applications - development files.

%package -n QtSql
Summary:	Qt classes for database integration using SQL
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}

%description -n QtSql
Qt classes for database integration using SQL.

%package -n QtSql-devel
Summary:	Qt classes for database integration using SQL - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}

%description -n QtSql-devel
Qt classes for database integration using SQL - development files.

%package -n QtSql-mysql
Summary:	Database plugin for MySQL Qt support
Group:		X11/Libraries
Requires:	QtSql = %{version}-%{release}
Provides:	QtSql-backend = %{version}-%{release}

%description -n QtSql-mysql
This package contains a plugin for using MySQL.

%package -n QtSql-postgresql
Summary:	Database plugin for Postgresql Qt support
Group:		X11/Libraries
Requires:	QtSql = %{version}-%{release}
Provides:	QtSql-backend = %{version}-%{release}

%description -n QtSql-postgresql
This package contains a plugin for using Postgresql.

%package -n QtSql-sqlite3
Summary:	Database plugin for SQLite3 Qt support
Group:		X11/Libraries
Requires:	QtSql = %{version}-%{release}
Provides:	QtSql-backend = %{version}-%{release}

%description -n QtSql-sqlite3
This package contains a plugin for using the SQLite3 library (which
allows to acces virtually any SQL database) via the QSql classes.

%package -n QtSvg
Summary:	SVG support
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
# for svg plugins
Requires:	QtXml = %{version}-%{release}

%description -n QtSvg
SVG support.

%package -n QtSvg-devel
Summary:	SVG support - development files
Group:		X11/Development/Libraries
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtSvg = %{version}-%{release}

%description -n QtSvg-devel
SVG support - development files.

%package -n QtTest
Summary:	Test framework
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}

%description -n QtTest
Test framework.

%package -n QtTest-devel
Summary:	Test framework - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtTest = %{version}-%{release}

%description -n QtTest-devel
Test framework - development files.

%package -n QtUiTools
Summary:	Qt classes for handling Qt Designer forms in applications
Group:		X11/Libraries
Requires:	QtGui = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description -n QtUiTools
The QtUiTools module provides classes to handle forms created with Qt
Designer.

%package -n QtUiTools-devel
Summary:	Qt classes for handling Qt Designer forms in applications - development files
Group:		X11/Development/Libraries
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtUiTools = %{version}-%{release}
Requires:	QtXml-devel = %{version}-%{release}

%description -n QtUiTools-devel
Qt classes for handling Qt Designer forms in applications - development
files.

%package -n QtWebKit
Summary:	Qt classes for rendering HTML, XHTML and SVG documents
Group:		X11/Libraries
Requires:	QtDBus = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description -n QtWebKit
QtWebKit provides a Web browser engine that makes it easy to embed
content from the World Wide Web into your Qt application. At the same
time Web content can be enhanced with native controls. QtWebKit
provides facilities for rendering of HyperText Markup Language (HTML),
Extensible HyperText Markup Language (XHTML) and Scalable Vector
Graphics (SVG) documents, styled using Cascading Style Sheets (CSS)
and scripted with JavaScript.

%package -n QtWebKit-devel
Summary:	Qt classes for rendering HTML, XHTML and SVG documents - development files
Group:		X11/Development/Libraries
Requires:	QtGui-devel = %{version}-%{release}
Requires:	QtNetwork-devel = %{version}-%{release}
Requires:	QtScript-devel = %{version}-%{release}
Requires:	QtWebKit = %{version}-%{release}

%description -n QtWebKit-devel
Qt classes for rendering HTML, XHTML and SVG documents - development
files.

%package -n QtXml
Summary:	Qt classes for handling XML
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}

%description -n QtXml
Qt classes for handling XML.

%package -n QtXml-devel
Summary:	Qt classes for handling XML - development files
Group:		X11/Development/Libraries
Requires:	QtCore-devel = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description -n QtXml-devel
Qt classes for handling XML - development files.

%package -n QtXmlPatterns
Summary:	QtXmlPatterns XQuery engine
Group:		X11/Libraries
Requires:	QtCore = %{version}-%{release}

%description -n QtXmlPatterns
QtXmlPatterns XQuery engine.

%package -n QtXmlPatterns-devel
Summary:	QtXmlPatterns XQuery engine - development files
Group:		X11/Development/Libraries
Requires:	QtNetwork-devel = %{version}-%{release}
Requires:	QtXmlPatterns = %{version}-%{release}

%description -n QtXmlPatterns-devel
QtXmlPatterns XQuery engine - development files.

%package assistant
Summary:	Qt documentation browser
Group:		X11/Development/Tools
Requires:	QtGui = %{version}-%{release}
Requires:	QtHelp = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}
Requires:	QtSql-sqlite3 = %{version}-%{release}
Requires:	QtWebKit = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}
Requires:	hicolor-icon-theme

%description assistant
Qt Assistant is a tool for browsing on-line documentation with
indexing, bookmarks and full-text search.

%package build
Summary:	Build tools for Qt
Group:		X11/Development/Tools
Requires:	QtCore = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}

%description build
This package includes the Qt resource compiler (rcc), meta objects
compiler (moc), user interface compiler (uic) and qt3to4 include names
converter.

%package designer
Summary:	IDE used for GUI designing with Qt library
Group:		X11/Applications
Requires:	QtDesigner = %{version}-%{release}

%description designer
An advanced tool used for GUI designing with Qt library.

%package linguist
Summary:	Translation helper for Qt
Group:		X11/Development/Tools
Requires:	QtUiTools = %{version}-%{release}

%description linguist
This program provides an interface that shortens and helps systematize
the process of translating GUIs. Qt Linguist takes all of the text of
a UI that will be shown to the user, and presents it to a human
translator in a simple window. When one UI text is translated, the
program automatically progresses to the next, until they are all
completed.

%package qmake
Summary:	Qt makefile generator
Group:		X11/Development/Tools

%description qmake
A powerful makefile generator. It can create makefiles on any platform
from a simple .pro definitions file.

%package config
Summary:	Qt widgets configuration tool
Group:		X11/Applications
Requires:	Qt3Support = %{version}-%{release}
Requires:	QtDBus = %{version}-%{release}
Requires:	QtGui = %{version}-%{release}
Requires:	QtNetwork = %{version}-%{release}
Requires:	QtSql = %{version}-%{release}
Requires:	QtXml = %{version}-%{release}
Requires:	desktop-file-utils

%description config
A tool for configuring look and behavior of Qt widgets.

%package doc
Summary:	Qt Documentation in HTML format
Group:		X11/Development/Libraries
Suggests:	%{name}-assistant = %{version}-%{release}

%description doc
Qt documentation in HTML format.

%prep
%setup -qn qt-everywhere-opensource-src-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

# adapt QMAKE FLAGS
%{__sed} -i -e '
	s|QMAKE_CC.*=.*gcc|QMAKE_CC\t\t= %{__cc}|;
	s|QMAKE_CFLAGS_DEBUG.*|QMAKE_CFLAGS_DEBUG\t+= %{debugcflags}|;
	s|QMAKE_CFLAGS_RELEASE.*|QMAKE_CFLAGS_RELEASE\t+= %{rpmcppflags} %{rpmcflags}|;
	s|QMAKE_CXX.*=.*g++|QMAKE_CXX\t\t= %{__cxx}|;
	s|QMAKE_CXXFLAGS_DEBUG.*|QMAKE_CXXFLAGS_DEBUG\t+= %{debugcflags}|;
	s|QMAKE_CXXFLAGS_RELEASE.*|QMAKE_CXXFLAGS_RELEASE\t+= %{rpmcppflags} %{rpmcxxflags}|;
	s|QMAKE_LFLAGS_RELEASE.*|QMAKE_LFLAGS_RELEASE\t+= %{rpmldflags}|;
	s|QMAKE_LINK.*=.*g++|QMAKE_LINK\t\t= %{__cxx}|;
	s|QMAKE_LINK_SHLIB.*=.*g++|QMAKE_LINK_SHLIB\t= %{__cxx}|;
	' mkspecs/common/{g++,gcc}-base.conf

# undefine QMAKE_STRIP, for useful debuginfo
%{__sed} -i -e '
	s|^QMAKE_STRIP.*=.*|QMAKE_STRIP\t\t=|;
	' mkspecs/common/linux.conf

# build fix
rm -r src/3rdparty/webkit/Source/WebKit/qt/tests

# some warining are still there
%{__sed} -i '/-Werror/d' src/3rdparty/webkit/Source/WebKit.pri

%build
# pass OPTFLAGS to build qmake itself with optimization
export OPTFLAGS="%{rpmcflags}"
export PATH=$PWD/bin:$PATH

COMMONOPT=" \
	-bindir %{_bindir}			\
	-datadir %{_datadir}/qt			\
	-docdir %{_docdir}/qt			\
	-headerdir %{_includedir}/qt		\
	-importdir %{_libdir}/qt/imports	\
	-libdir %{_libdir}			\
	-plugindir %{_libdir}/qt/plugins	\
	-prefix %{_prefix}			\
	-sysconfdir %{_sysconfdir}/xdg		\
	-translationdir %{_datadir}/qt/translations	\
	-confirm-license			\
	-opensource				\
	-continue				\
	-dbus-linked				\
	-fast					\
	-no-nas-sound				\
	-no-openvg				\
	-no-pch					\
	-no-phonon				\
	-no-phonon-backend			\
	-no-rpath				\
	-no-separate-debug-info			\
	-nomake demos				\
	-nomake docs				\
	-nomake examples			\
	-openssl-linked				\
	-optimized-qmake			\
	-reduce-relocations			\
	-release				\
	-system-libjpeg				\
	-system-libmng				\
	-system-libpng				\
	-system-sqlite				\
	-system-zlib				\
	-verbose"

SQL=" \
	-no-sql-ibase		\
	-no-sql-mysql		\
	-no-sql-odbc		\
	-no-sql-psql		\
	-no-sql-sqlite2		\
	-plugin-sql-sqlite"

./configure $COMMONOPT $SQL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_pkgconfigdir}}
install -d $RPM_BUILD_ROOT%{_libdir}/qt/plugins/{crypto,network}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# kill -L/inside/builddir from *.la and *.pc (bug #77152)
%{__sed} -i -e "s,-L$PWD/lib,,g" $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/qtconfig.desktop
install tools/qtconfig/images/appicon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/qtconfig.png

# Locale
#
for f in translations/*.ts ; do
	LD_LIBRARY_PATH=lib bin/lrelease $f -qm translations/$(basename $f .ts).qm
done

for f in $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc; do
	HAVEDEBUG=`echo $f | grep _debug | wc -l`
	MODULE=`echo $f | basename $f | cut -d. -f1 | cut -d_ -f1`
	MODULE2=`echo $MODULE | tr a-z A-Z | sed s:QT::`
	DEFS="-D_REENTRANT"

	if [ "$MODULE2" == "3SUPPORT" ]; then
		DEFS="$DEFS -DQT3_SUPPORT -DQT_QT3SUPPORT_LIB"
	else
		DEFS="$DEFS -DQT_"$MODULE2"_LIB"
	fi
	[ "$HAVEDEBUG" -eq 0 ] && DEFS="$DEFS -DQT_NO_DEBUG"

	sed -i -e "s:-DQT_SHARED:-DQT_SHARED $DEFS:" $f
done

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or direcotry!"
		return 1
	fi
}

mkdevfl() {
	set -x
	MODULE=$1; shift
	echo "%%defattr(644,root,root,755)" > $MODULE-devel.files
	ifecho $MODULE-devel "%{_libdir}/lib$MODULE*.so"
	ifecho $MODULE-devel "%{_pkgconfigdir}/$MODULE*.pc"
	if [ -d "$RPM_BUILD_ROOT%{_includedir}/qt/$MODULE" ]; then
		ifecho $MODULE-devel %{_includedir}/qt/$MODULE
	fi
	for f in `find $RPM_BUILD_ROOT%{_includedir}/qt/$MODULE -printf "%%P "`; do
		ifecho $MODULE-devel %{_includedir}/qt/$MODULE/$f
		if [ -a "$RPM_BUILD_ROOT%{_includedir}/qt/Qt/$f" ]; then
			ifecho $MODULE-devel %{_includedir}/qt/Qt/$f
		fi
	done
	for f in $@; do ifecho $MODULE-devel $f; done
}

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,prl}

mkdevfl QtCore %{_includedir}/qt %{_includedir}/qt/Qt
mkdevfl QtDBus %{_bindir}/qdbuscpp2xml %{_bindir}/qdbusxml2cpp
mkdevfl	QtDeclarative
mkdevfl QtGui
mkdevfl QtMultimedia
mkdevfl QtNetwork
mkdevfl QtOpenGL
mkdevfl QtScript
mkdevfl QtScriptTools
mkdevfl QtSql
mkdevfl QtSvg
mkdevfl QtTest
mkdevfl QtHelp
mkdevfl QtWebKit
mkdevfl QtCLucene
mkdevfl QtXml
mkdevfl QtXmlPatterns
mkdevfl Qt3Support

# without *.la *.pc etc.
mkdevfl QtDesigner || /bin/true
mkdevfl QtUiTools || /bin/true

# without glob (exclude QtScriptTools* QtXmlPatterns*)
%{__sed} -i 's,QtScript\*,QtScript,g' QtScript-devel.files
%{__sed} -i 's,QtXml\*,QtXml,g' QtXml-devel.files

rm -f $RPM_BUILD_ROOT%{_datadir}/qt/translations/qvfb_*

%find_lang assistant --with-qm --without-mo
%find_lang designer --with-qm --without-mo
%find_lang linguist --with-qm --without-mo
%find_lang qt --with-qm --without-mo
%find_lang qt_help --with-qm --without-mo
%find_lang qtconfig --with-qm --without-mo

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt3Support -p /sbin/ldconfig
%postun	-n Qt3Support -p /sbin/ldconfig

%post	-n QtCLucene -p /sbin/ldconfig
%postun	-n QtCLucene -p /sbin/ldconfig

%post	-n QtCore -p /sbin/ldconfig
%postun	-n QtCore -p /sbin/ldconfig

%post	-n QtDBus -p /sbin/ldconfig
%postun	-n QtDBus -p /sbin/ldconfig

%post	-n QtDeclarative -p /sbin/ldconfig
%postun	-n QtDeclarative -p /sbin/ldconfig

%post	-n QtDesigner -p /sbin/ldconfig
%postun	-n QtDesigner -p /sbin/ldconfig

%post	-n QtGui -p /sbin/ldconfig
%postun	-n QtGui -p /sbin/ldconfig

%post	-n QtHelp -p /sbin/ldconfig
%postun	-n QtHelp -p /sbin/ldconfig

%post	-n QtMultimedia -p /sbin/ldconfig
%postun	-n QtMultimedia -p /sbin/ldconfig

%post	-n QtNetwork -p /sbin/ldconfig
%postun	-n QtNetwork -p /sbin/ldconfig

%post	-n QtOpenGL -p /sbin/ldconfig
%postun	-n QtOpenGL -p /sbin/ldconfig

%post   -n QtScript -p /sbin/ldconfig
%postun -n QtScript -p /sbin/ldconfig

%post   -n QtScriptTools -p /sbin/ldconfig
%postun -n QtScriptTools -p /sbin/ldconfig

%post	-n QtSql -p /sbin/ldconfig
%postun	-n QtSql -p /sbin/ldconfig

%post	-n QtSvg -p /sbin/ldconfig
%postun	-n QtSvg -p /sbin/ldconfig

%post	-n QtTest -p /sbin/ldconfig
%postun	-n QtTest -p /sbin/ldconfig

%post	-n QtUiTools -p /sbin/ldconfig
%postun	-n QtUiTools -p /sbin/ldconfig

%post	-n QtWebKit -p /sbin/ldconfig
%postun	-n QtWebKit -p /sbin/ldconfig

%post	-n QtXml -p /sbin/ldconfig
%postun	-n QtXml -p /sbin/ldconfig

%post   -n QtXmlPatterns -p /sbin/ldconfig
%postun -n QtXmlPatterns -p /sbin/ldconfig

%post config
%update_desktop_database

%postun config
%update_desktop_database

%files -n Qt3Support
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt3Support.so.?
%attr(755,root,root) %{_libdir}/libQt3Support.so.*.*

%files -n QtCLucene
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtCLucene.so.?
%attr(755,root,root) %{_libdir}/libQtCLucene.so.*.*

%files -n QtCore -f qt.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtCore.so.?
%attr(755,root,root) %{_libdir}/libQtCore.so.*.*
%dir %{_bindir}
%dir %{_libdir}/qt
%dir %{_libdir}/qt/plugins
%dir %{_libdir}/qt/plugins/accessible
%dir %{_libdir}/qt/plugins/codecs
%dir %{_libdir}/qt/plugins/crypto
%dir %{_libdir}/qt/plugins/graphicssystems
%dir %{_libdir}/qt/plugins/iconengines
%dir %{_libdir}/qt/plugins/imageformats
%dir %{_libdir}/qt/plugins/inputmethods
%dir %{_libdir}/qt/plugins/network
%dir %{_libdir}/qt/plugins/sqldrivers
%dir %{_libdir}/qt/plugins/script
%dir %{_datadir}/qt
%dir %{_datadir}/qt/translations

%files -n QtDBus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qdbus
%attr(755,root,root) %{_bindir}/qdbusviewer
%attr(755,root,root) %{_libdir}/libQtDBus.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtDBus.so.?
# ?? is this the proper place?
%attr(755,root,root) %{_libdir}/qt/plugins/script/libqtscriptdbus.so

%files -n QtDeclarative
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmlviewer
%attr(755,root,root) %{_bindir}/qmlplugindump
%attr(755,root,root) %{_libdir}/libQtDeclarative.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtDeclarative.so.4
%dir %{_libdir}/qt/imports
%dir %{_libdir}/qt/imports/Qt
%dir %{_libdir}/qt/imports/Qt/labs
%dir %{_libdir}/qt/imports/Qt/labs/folderlistmodel
%dir %{_libdir}/qt/imports/Qt/labs/gestures
%dir %{_libdir}/qt/imports/Qt/labs/particles
%dir %{_libdir}/qt/imports/Qt/labs/shaders
%attr(755,root,root) %{_libdir}/qt/imports/Qt/labs/*/*.so
%{_libdir}/qt/imports/Qt/labs/*/qmldir
%dir %{_libdir}/qt/plugins/qmltooling
%attr(755,root,root) %{_libdir}/qt/plugins/qmltooling/libqmldbg_tcp.so
%attr(755,root,root) %{_libdir}/qt/plugins/qmltooling/libqmldbg_inspector.so
%dir %{_libdir}/qt/imports/QtWebKit
%attr(755,root,root) %{_libdir}/qt/imports/QtWebKit/*.so
%{_libdir}/qt/imports/QtWebKit/qmldir

%files -n QtDesigner
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtDesigner.so.?
%attr(755,root,root) %ghost %{_libdir}/libQtDesignerComponents.so.?
%attr(755,root,root) %{_libdir}/libQtDesigner.so.*.*
%attr(755,root,root) %{_libdir}/libQtDesignerComponents.so.*.*
%dir %{_libdir}/qt/plugins/designer
%attr(755,root,root) %{_libdir}/qt/plugins/designer/*.so

%files -n QtGui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGui.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGui.so.?
%attr(755,root,root) %{_libdir}/qt/plugins/accessible/*.so
%attr(755,root,root) %{_libdir}/qt/plugins/codecs/*.so
%attr(755,root,root) %{_libdir}/qt/plugins/graphicssystems/*.so
%attr(755,root,root) %{_libdir}/qt/plugins/iconengines/*.so
%attr(755,root,root) %{_libdir}/qt/plugins/imageformats/*.so
%attr(755,root,root) %{_libdir}/qt/plugins/inputmethods/*.so

%files -n QtHelp -f qt_help.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qhelpconverter
%attr(755,root,root) %{_bindir}/qhelpgenerator
%attr(755,root,root) %ghost %{_libdir}/libQtHelp.so.?
%attr(755,root,root) %{_libdir}/libQtHelp.so.*.*

%files -n QtMultimedia
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtMultimedia.so.?
%attr(755,root,root) %{_libdir}/libQtMultimedia.so.*.*

%files -n QtNetwork
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtNetwork.so.?
%attr(755,root,root) %{_libdir}/libQtNetwork.so.*.*
%dir %{_libdir}/qt/plugins/bearer
%attr(755,root,root) %{_libdir}/qt/plugins/bearer/*.so

%files -n QtOpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtOpenGL.so.?
%attr(755,root,root) %{_libdir}/libQtOpenGL.so.*.*

%files -n QtScript
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtScript.so.?
%attr(755,root,root) %{_libdir}/libQtScript.so.*.*

%files -n QtScriptTools
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtScriptTools.so.?
%attr(755,root,root) %{_libdir}/libQtScriptTools.so.*.*

%files -n QtSql
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtSql.so.?
%attr(755,root,root) %{_libdir}/libQtSql.so.*.*

%if 0
%files -n QtSql-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins/sqldrivers/libqsqlmysql.so

%files -n QtSql-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins/sqldrivers//libqsqlpsql.so
%endif

%files -n QtSql-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins/sqldrivers/libqsqlite.so

%files -n QtSvg
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtSvg.so.?
%attr(755,root,root) %{_libdir}/libQtSvg.so.*.*

%files -n QtTest
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtTest.so.?
%attr(755,root,root) %{_libdir}/libQtTest.so.*.*

%files -n QtUiTools
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtUiTools.so.?
%attr(755,root,root) %{_libdir}/libQtUiTools.so.*.*

%files -n QtWebKit
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtWebKit.so.?
%attr(755,root,root) %{_libdir}/libQtWebKit.so.*.*

%files -n QtXml
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQtXml.so.?
%attr(755,root,root) %{_libdir}/libQtXml.so.*.*

%files -n QtXmlPatterns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlpatterns
%attr(755,root,root) %{_bindir}/xmlpatternsvalidator
%attr(755,root,root) %ghost %{_libdir}/libQtXmlPatterns.so.?
%attr(755,root,root) %{_libdir}/libQtXmlPatterns.so.*.*

%files assistant -f assistant.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pixeltool
%attr(755,root,root) %{_bindir}/qcollectiongenerator
%attr(755,root,root) %{_bindir}/assistant

%files build
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/moc
%attr(755,root,root) %{_bindir}/qdoc3
%attr(755,root,root) %{_bindir}/qt3to4
%attr(755,root,root) %{_bindir}/rcc
%attr(755,root,root) %{_bindir}/uic
#find better place?
%attr(755,root,root) %{_bindir}/qttracereplay
%{_datadir}/qt/q3porting.xml

%files designer -f designer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/designer

%files linguist -f linguist.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/linguist
%attr(755,root,root) %{_bindir}/lconvert
%attr(755,root,root) %{_bindir}/lrelease
%attr(755,root,root) %{_bindir}/lupdate
%{_datadir}/qt/phrasebooks

%files qmake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmake
%{_datadir}/qt/mkspecs

%files config -f qtconfig.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtconfig
%{_desktopdir}/qtconfig.desktop
%{_pixmapsdir}/qtconfig.png

%if 0
%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc
%{_libdir}/qt/doc
%endif

%files -n QtCLucene-devel -f QtCLucene-devel.files
%defattr(644,root,root,755)

%files -n Qt3Support-devel -f Qt3Support-devel.files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uic3

%files -n QtCore-devel -f QtCore-devel.files
%defattr(644,root,root,755)

%files -n QtDBus-devel -f QtDBus-devel.files
%defattr(644,root,root,755)

%files -n QtDeclarative-devel -f QtDeclarative-devel.files
%defattr(644,root,root,755)

%files -n QtDesigner-devel -f QtDesigner-devel.files
%defattr(644,root,root,755)

%files -n QtGui-devel -f QtGui-devel.files
%defattr(644,root,root,755)

%files -n QtHelp-devel -f QtHelp-devel.files
%defattr(644,root,root,755)

%files -n QtMultimedia-devel -f QtMultimedia-devel.files
%defattr(644,root,root,755)

%files -n QtNetwork-devel -f QtNetwork-devel.files
%defattr(644,root,root,755)

%files -n QtOpenGL-devel -f QtOpenGL-devel.files
%defattr(644,root,root,755)

%files -n QtScript-devel -f QtScript-devel.files
%defattr(644,root,root,755)

%files -n QtScriptTools-devel -f QtScriptTools-devel.files
%defattr(644,root,root,755)

%files -n QtSql-devel -f QtSql-devel.files
%defattr(644,root,root,755)

%files -n QtSvg-devel -f QtSvg-devel.files
%defattr(644,root,root,755)

%files -n QtTest-devel -f QtTest-devel.files
%defattr(644,root,root,755)

%files -n QtUiTools-devel -f QtUiTools-devel.files
%defattr(644,root,root,755)

%files -n QtWebKit-devel -f QtWebKit-devel.files
%defattr(644,root,root,755)

%files -n QtXml-devel -f QtXml-devel.files
%defattr(644,root,root,755)

%files -n QtXmlPatterns-devel -f QtXmlPatterns-devel.files
%defattr(644,root,root,755)

