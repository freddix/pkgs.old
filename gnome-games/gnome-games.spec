Summary:	GNOME games
Name:		gnome-games
Version:	3.4.2
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	4888d77c1fc012ab044bddd305ed32d1
URL:		http://live.gnome.org/GnomeGames
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	librsvg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-pygobject3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel
BuildRequires:	vala
BuildRequires:	yelp-tools
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	hicolor-icon-theme
Requires:	gtk+-rsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var
%define		_gamesdir	%{_localstatedir}/games

%description
Gnome-games is a collection of simple, but addictive, games from the
GNOME desktop project. They represent many of the popular games and
include card games, puzzle games and arcade games.

%package glchess
Summary:	GNOME glChess - a 2D/3D chess interface
Group:		X11/Applications/Games
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme
Suggests:	crafty
Suggests:	gnuchess

%description glchess
glChess is a 2D/3D chess game interfacing via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently
use engines such as GNUChess, Sjeng, Faile, Amy, Crafty and Phalanx.

%package glines
Summary:	Five or more game
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description glines
Remove colored balls from the board by forming lines.

%package gnect
Summary:	Four-in-a-row game
Group:		X11/Applications/Games
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnect
Compete to make lines of the same color.

%package gnibbles
Summary:	GNOME Nibbles
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnibbles
Guide a worm around a maze.

%package gnobots2
Summary:	GNOME Robots
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnobots2
Avoid the robots and make them crash into each other.

%package gnomine
Summary:	GNOME Mines
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnomine
Clear mines from a minefield.

%package gnotravex
Summary:	GNOME Tetravex
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnotravex
Puzzle game.

%package gnotski
Summary:	Gnome Klotski
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnotski
Clone of the Klotski game. The objective is to move the patterned
block to the area bordered by green markers.

%package gtali
Summary:	GNOME Tali
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gtali
Poker-style dice game.

%package iagno
Summary:	GNOME Iagno
Group:		X11/Applications/Games
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description iagno
Reversi like game.

%package lightsoff
Summary:	Lights Off
Group:		X11/Applications/Games
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description lightsoff
Lights Off is a puzzle game, where the objective is to turn off all of
the tiles on the board. Each click toggles the state of the clicked
tile and its non-diagonal neighbors.

%package mahjongg
Summary:	GNOME Mahjongg
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description mahjongg
Disassemble a pile of tiles by removing matching pairs.

%package quadrapassel
Summary:	GNOME Tetris
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description quadrapassel
Tetris like game.

%package sudoku
Summary:	Simple interface for playing, saving, printing and solving Sudoku
Group:		X11/Applications/Games
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme
Requires:	python-pycairo
Requires:	python-pygobject3

%description sudoku
GNOME Sudoku provides a simple interface for playing, saving, printing
and solving Sudoku.

%package swell-foop
Summary:	Swell Foop
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description swell-foop
Remove groups of balls to try and clear the screen.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-games=all	\
	--enable-staging
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%py_postclean

%find_lang %{name}
%find_lang gnect --with-gnome
%find_lang gnomine --with-gnome
%find_lang swell-foop --with-gnome
%find_lang mahjongg --with-gnome
%find_lang glchess --with-gnome
%find_lang gtali --with-gnome
%find_lang gnome-sudoku --with-gnome
%find_lang gnotravex --with-gnome
%find_lang gnotski --with-gnome
%find_lang glines --with-gnome
%find_lang iagno --with-gnome
%find_lang gnobots2 --with-gnome
%find_lang gnibbles --with-gnome
%find_lang quadrapassel --with-gnome
%find_lang lightsoff --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache
%update_icon_cache hicolor

%postun
%update_gsettings_cache
%update_icon_cache hicolor

%post glchess
%update_icon_cache hicolor
%update_desktop_database_post
%update_gsettings_cache

%postun glchess
%update_icon_cache hicolor
%update_desktop_database_postun
%update_gsettings_cache

%post glines
%update_icon_cache hicolor
%update_gsettings_cache

if [ ! -f %{_gamesdir}/glines.scores ]; then
	touch %{_gamesdir}/glines.scores
	chown root:games %{_gamesdir}/glines.scores
	chmod 664 %{_gamesdir}/glines.scores
fi

%postun glines
%update_icon_cache hicolor
%update_gsettings_cache

%post gnect
%update_icon_cache hicolor
%update_gsettings_cache

%postun gnect
%update_icon_cache hicolor
%update_gsettings_cache

%post gnibbles
%update_icon_cache hicolor
%update_gsettings_cache

for i in gnibbles.1.0 gnibbles.1.1 gnibbles.2.0 gnibbles.2.1 gnibbles.3.0 \
	gnibbles.3.1 gnibbles.4.0 gnibbles.4.1; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnibbles
%update_icon_cache hicolor
%update_gsettings_cache

%post gnobots2
%update_gsettings_cache
%update_icon_cache hicolor

for i in gnobots2.classic_robots-safe gnobots2.classic_robots \
	gnobots2.classic_robots-super-safe gnobots2.nightmare-safe \
	gnobots2.nightmare gnobots2.nightmare-super-safe \
	gnobots2.robots2_easy-safe gnobots2.robots2_easy \
	gnobots2.robots2_easy-super-safe gnobots2.robots2-safe \
	gnobots2.robots2 gnobots2.robots2-super-safe \
	gnobots2.robots_with_safe_teleport-safe \
	gnobots2.robots_with_safe_teleport \
	gnobots2.robots_with_safe_teleport-super-safe; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun	gnobots2
%update_gsettings_cache
%update_icon_cache hicolor

%post gnomine
%update_gsettings_cache
%update_icon_cache hicolor

for i in gnomine.Custom gnomine.Large gnomine.Medium gnomine.Small; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnomine
%update_icon_cache hicolor
%update_gsettings_cache

%post gnotravex
%update_gsettings_cache
%update_icon_cache hicolor

for i in gnotravex.2x2 gnotravex.3x3 gnotravex.4x4 gnotravex.5x5 \
	gnotravex.6x6; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnotravex
%update_icon_cache hicolor
%update_gsettings_cache

%post gnotski
%update_gsettings_cache
%update_icon_cache hicolor

for i in 1 2 3 4 5 6 7 11 12 13 14 15 16 17 21 22 23 24 25 26; do
	if [ ! -f %{_gamesdir}/gnotski.$i.scores ]; then
	touch %{_gamesdir}/gnotski.$i.scores
	chown root:games %{_gamesdir}/gnotski.$i.scores
	chmod 664 %{_gamesdir}/gnotski.$i.scores
	fi
done

%postun gnotski
%update_gsettings_cache
%update_icon_cache hicolor

%post gtali
%update_gsettings_cache
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/gtali.scores ]; then
	touch %{_gamesdir}/gtali.scores
	chown root:games %{_gamesdir}/gtali.scores
	chmod 664 %{_gamesdir}/gtali.scores
fi

%postun gtali
%update_gsettings_cache
%update_icon_cache hicolor

%post iagno
%update_gsettings_cache
%update_icon_cache hicolor

%postun iagno
%update_icon_cache hicolor
%update_gsettings_cache

%post lightsoff
%update_icon_cache hicolor
%update_gsettings_cache

%postun lightsoff
%update_icon_cache hicolor
%update_gsettings_cache

%post mahjongg
%update_gsettings_cache
%update_icon_cache hicolor

for i in mahjongg.bridges mahjongg.cloud mahjongg.confounding \
	mahjongg.difficult mahjongg.dragon mahjongg.easy \
	mahjongg.pyramid mahjongg.tictactoe mahjongg.ziggurat; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun mahjongg
%update_icon_cache hicolor
%update_gsettings_cache

%post quadrapassel
%update_icon_cache hicolor
%update_gsettings_cache

if [ ! -f %{_gamesdir}/quadrapassel.scores ]; then
	touch %{_gamesdir}/quadrapassel.scores
	chown root:games %{_gamesdir}/quadrapassel.scores
	chmod 664 %{_gamesdir}/quadrapassel.scores
fi

%postun quadrapassel
%update_icon_cache hicolor
%update_gsettings_cache

%post sudoku
%update_icon_cache hicolor
%update_gsettings_cache

%postun sudoku
%update_icon_cache hicolor
%update_gsettings_cache

%post swell-foop
%update_icon_cache hicolor
%update_gsettings_cache

for i in large normal small; do
	if [ ! -f %{_gamesdir}/swell-foop.$i.scores ]; then
		touch %{_gamesdir}/swell-foop.$i.scores
		chown root:games %{_gamesdir}/swell-foop.$i.scores
		chmod 664 %{_gamesdir}/swell-foop.$i.scores
	fi
done

%postun swell-foop
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libgames-support-gi.so*
%{_libdir}/%{name}/GnomeGamesSupport-1.0.*
%{_datadir}/glib-2.0/schemas/org.gnome.Games.WindowState.gschema.xml
%{_iconsdir}/hicolor/*/*/*.png
%dir %{_datadir}/%{name}

%files glchess -f glchess.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glchess
%{_desktopdir}/glchess.desktop
%{_datadir}/glchess
%{_datadir}/glib-2.0/schemas/org.gnome.glchess.gschema.xml
%{_iconsdir}/hicolor/*/*/glchess.*
%{_mandir}/man6/glchess.6*

%files glines -f glines.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_datadir}/glines
%{_datadir}/glib-2.0/schemas/org.gnome.glines.gschema.xml
%{_desktopdir}/glines.desktop
%{_iconsdir}/hicolor/*/*/glines.*
%attr(664,root,games) %ghost %{_gamesdir}/glines.*
%{_mandir}/man6/glines.6*

%files gnect -f gnect.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_datadir}/gnect
%{_datadir}/glib-2.0/schemas/org.gnome.gnect.gschema.xml
%{_desktopdir}/gnect.desktop
%{_iconsdir}/hicolor/*/*/gnect.*
%{_mandir}/man6/gnect.6*

%files gnibbles -f gnibbles.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnibbles
%{_datadir}/gnibbles
%{_datadir}/glib-2.0/schemas/org.gnome.gnibbles.gschema.xml
%{_desktopdir}/gnibbles.desktop
%{_iconsdir}/hicolor/*/*/gnibbles.*
%attr(664,root,games) %ghost %{_gamesdir}/gnibbles.*
%{_mandir}/man6/gnibbles.6*

%files gnobots2 -f gnobots2.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnobots2
%{_datadir}/gnobots2
%{_datadir}/glib-2.0/schemas/org.gnome.gnobots2.gschema.xml
%{_desktopdir}/gnobots2.desktop
%{_iconsdir}/hicolor/*/*/gnobots2.*
%attr(664,root,games) %ghost %{_gamesdir}/gnobots2.*
%{_mandir}/man6/gnobots2.6*

%files gnomine -f gnomine.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_datadir}/gnomine
%{_datadir}/glib-2.0/schemas/org.gnome.gnomine.gschema.xml
%{_desktopdir}/gnomine.desktop
%{_iconsdir}/hicolor/*/*/gnomine.*
%attr(664,root,games) %ghost %{_gamesdir}/gnomine.*
%{_mandir}/man6/gnomine.6*

%files gnotravex -f gnotravex.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_datadir}/glib-2.0/schemas/org.gnome.gnotravex.gschema.xml
%{_desktopdir}/gnotravex.desktop
%{_datadir}/gnotravex
%{_iconsdir}/hicolor/*/*/gnotravex.*
%attr(664,root,games) %ghost %{_gamesdir}/gnotravex.*
%{_mandir}/man6/gnotravex.6*

%files gnotski -f gnotski.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_desktopdir}/gnotski.desktop
%{_datadir}/gnotski
%{_datadir}/glib-2.0/schemas/org.gnome.gnotski.gschema.xml
%{_iconsdir}/hicolor/*/*/gnotski.*
%attr(664,root,games) %ghost %{_gamesdir}/gnotski.*
%{_mandir}/man6/gnotski.6*

%files gtali -f gtali.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_datadir}/gtali
%{_datadir}/glib-2.0/schemas/org.gnome.gtali.gschema.xml
%{_desktopdir}/gtali.desktop
%{_iconsdir}/hicolor/*/*/gtali.*
%attr(664,root,games) %ghost %{_gamesdir}/gtali.*
%{_mandir}/man6/gtali.6*

%files iagno -f iagno.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_datadir}/iagno
%{_datadir}/glib-2.0/schemas/org.gnome.iagno.gschema.xml
%{_desktopdir}/iagno.desktop
%{_iconsdir}/hicolor/*/*/iagno.*
%{_mandir}/man6/iagno.6*

%files lightsoff -f lightsoff.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lightsoff
%{_datadir}/lightsoff
%{_datadir}/glib-2.0/schemas/org.gnome.lightsoff.gschema.xml
%{_desktopdir}/lightsoff.desktop
%{_iconsdir}/hicolor/*/*/lightsoff.*

%files mahjongg -f mahjongg.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_datadir}/glib-2.0/schemas/org.gnome.mahjongg.gschema.xml
%{_desktopdir}/mahjongg.desktop
%{_iconsdir}/hicolor/*/*/mahjongg.*
%{_datadir}/mahjongg
%attr(664,root,games) %ghost %{_gamesdir}/mahjongg.*
%{_mandir}/man6/mahjongg.6*

%files quadrapassel -f quadrapassel.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/quadrapassel
%{_datadir}/quadrapassel
%{_datadir}/glib-2.0/schemas/org.gnome.quadrapassel.gschema.xml
%{_desktopdir}/quadrapassel.desktop
%{_iconsdir}/hicolor/*/*/quadrapassel.*
%attr(664,root,games) %ghost %{_gamesdir}/quadrapassel.*
%{_mandir}/man6/quadrapassel.6*

%files sudoku -f gnome-sudoku.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%dir %{py_sitescriptdir}/gnome_sudoku
%{py_sitescriptdir}/gnome_sudoku/*.py[co]
%dir %{py_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py[co]
%{_datadir}/gnome-sudoku
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-sudoku.gschema.xml
%{_iconsdir}/hicolor/*/*/gnome-sudoku.*
%{_mandir}/man6/gnome-sudoku.6*

%files swell-foop -f swell-foop.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/swell-foop
%{_desktopdir}/swell-foop.desktop
%{_datadir}/gnome-games/swell-foop
%{_datadir}/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
%{_iconsdir}/hicolor/*/*/swell-foop.*
%attr(664,root,games) %ghost %{_gamesdir}/swell-foop.*

