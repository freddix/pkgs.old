%include	/usr/lib/rpm/macros.perl

%bcond_with	bootstrap	# bootstrap build
%bcond_with	xindy		# do not build xindy packages

Summary:	TeX typesetting system and MetaFont font formatter
Name:		texlive
Version:	20080816
Release:	3
License:	distributable
Group:		Applications/Publishing/TeX
Source0:	http://tug.org/svn/texlive/branches/branch2008/Master/source/%{name}-%{version}-source.tar.lzma
# Source0-md5:	554287c3e458da776edd684506048d45
Source1:	ftp://tug.org/texlive/historic/2008/%{name}-20080822-texmf.tar.lzma
# Source1-md5:	fa74072e1344e8390eb156bcda61a8b2
Source10:	ftp://ftp.fu-berlin.de/tex/CTAN/macros/latex/contrib/floatflt.zip
# Source10-md5:	5d9fe14d289aa81ebb6b4761169dd5f2
Source11:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-fonts-larm.tar.bz2
# Source11-md5:	df2fcc66f0c2e90785ca6c9b27dacd34
Source12:	ftp://ftp.fu-berlin.de/tex/CTAN/macros/latex/contrib/foiltex.zip
# Source12-md5:	0a6b4e64fb883a68d9b288bf3421db25
Source50:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/Splashscreen.pm
# Source50-md5:	5cc49f49010f27fdb02dd7053797ba19
Source51:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLConfig.pm
# Source51-md5:	947ee29c38c2c2cfd9a25c597a89598a
Source52:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLMedia.pm
# Source52-md5:	9f1e76f3528125691edd4fbcdd69c5cb
Source53:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPDB.pm
# Source53-md5:	47cae437999e98a7bd24f27db7b0fa34
Source54:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPOBJ.pm
# Source54-md5:	c573c407ae3d98f710d65d593a7d1745
Source55:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPSRC.pm
# Source55-md5:	834ae0ac5c59fd00ab6000ba6367a987
Source56:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPaper.pm
# Source56-md5:	326314fc034a5d9ef9d4a60033f7186f
Source57:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPostActions.pm
# Source57-md5:	17c1968725ccf4aaafb7162b7b3609fc
Source58:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLTREE.pm
# Source58-md5:	039cc8878f380cab3b0beffe75870c6c
Source59:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLUtils.pm
# Source59-md5:	4e611075975c0dd62a9170d319258b8f
Source60:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLWinGoo.pm
# Source60-md5:	825121187994692ecda0f48a5b17421a
Source61:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TeXCatalogue.pm
# Source61-md5:	6289d93a12aa246fc2019b0109d2167f
Source62:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/waitVariableX.pm
# Source62-md5:	f0fa0f2fc7aacb1e9b40eb65891a24c8
Patch0:		%{name}-am.patch
Patch1:		%{name}-20080816-kpathsea-ar.patch
Patch2:		%{name}-gcc44.patch
Patch3:		%{name}-getline.patch
Patch4:		%{name}-stdio.patch
Patch5:		%{name}-aclocal.patch
Patch6:		%{name}-libpng.patch
URL:		http://www.tug.org/texlive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
%if %{with xindy}
BuildRequires:	clisp
%endif
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	sed
BuildRequires:	t1lib-devel
BuildRequires:	texinfo
%if %{with bootstrap}
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-latex-cyrillic
BuildRequires:	tetex-tex-babel
BuildRequires:	texconfig
%else
BuildRequires:	%{name}-context
BuildRequires:	%{name}-csplain
BuildRequires:	%{name}-fonts-cmsuper
BuildRequires:	%{name}-format-eplain
BuildRequires:	%{name}-format-mex
BuildRequires:	%{name}-format-pdflatex
BuildRequires:	%{name}-latex
BuildRequires:	%{name}-latex-cyrillic
BuildRequires:	%{name}-metapost
BuildRequires:	%{name}-mex
BuildRequires:	%{name}-omega
BuildRequires:	%{name}-other-utils
BuildRequires:	%{name}-pdftex
BuildRequires:	%{name}-phyzzx
BuildRequires:	%{name}-plain
BuildRequires:	%{name}-tex-babel
BuildRequires:	%{name}-tex-physe
BuildRequires:	%{name}-xetex
BuildRequires:	%{name}-xmltex
%endif
BuildRequires:	/usr/bin/latex
BuildRequires:	unzip
BuildRequires:	xorg-libICE-devel
BuildRequires:	xorg-libXaw-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXpm-devel
BuildRequires:	zlib-devel
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-cm = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}
Requires:	awk
Requires:	dialog
Requires:	kpathsea = %{epoch}:%{version}-%{release}
Requires:	sed
Requires:	sh-utils
Requires:	texconfig = %{epoch}:%{version}-%{release}
Requires:	textutils
Suggests:	tmpwatch
Provides:	tetex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdfetex = %{epoch}:%{version}-%{release}
Provides:	tetex-metafont
Obsoletes:	tetex
Obsoletes:	tetex-afm
Obsoletes:	tetex-doc
Obsoletes:	tetex-doc-latex2e-html
Obsoletes:	tetex-fontinst
Obsoletes:	tetex-fontname
Obsoletes:	tetex-fonts
Obsoletes:	tetex-fonts-pandora
Obsoletes:	tetex-fonts-vcm
Obsoletes:	tetex-format-elatex
Obsoletes:	tetex-format-pdfelatex
Obsoletes:	tetex-format-pdfemex
Obsoletes:	tetex-format-pdfetex
Obsoletes:	tetex-latex-vnps
Obsoletes:	tetex-latex-vnr
Obsoletes:	tetex-metafont
Obsoletes:	tetex-oxdvi
Obsoletes:	tetex-plain-dvips
Obsoletes:	tetex-plain-mathtime
Obsoletes:	tetex-plain-misc
Obsoletes:	tetex-plain-plnfss
Obsoletes:	tetex-tex-hyphen
Obsoletes:	tetex-tex-vietnam
Obsoletes:	texlive-metafont
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texmfdist %{texmf}-dist
%define		texmfdoc %{texmf}-doc
%define		fmtdir	/var/lib/texmf/web2c
%define		texhash	umask 022; [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2;
%define		_localstatedir	/var/lib/texmf
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ;
%define		fmtutil(f:) [ ! \\\( -f %{_localstatedir}/web2c/%{-f*}.fmt.rpmnew -o -f %{_localstatedir}/web2c/%{-f*}.efmt.rpmnew \\\) ] || %{_bindir}/fmtutil-sys --byfmt %{-f*} >/dev/null 2>/dev/null || echo "Regenerating %{-f*} failed. See %{_localstatedir}/web2c/%{-f*}.log for details" 1>&2 && exit 0 ;

%define		_noautoreq 'perl(path_tre)'

%description
TeXLive is an implementation of TeX for Linux or UNIX systems. TeX
takes a text file and a set of formatting commands as input and
creates a typesetter independent .dvi (DeVice Independent) file as
output. Usually, TeX is used in conjunction with a higher level
formatting package like LaTeX or PlainTeX, since TeX by itself is not
very user-friendly.

%package other-utils
Summary:	Other utilities
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-format-cyrtexinfo

%description other-utils
Other utilities.

%package jadetex
Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	jadetex = %{epoch}:%{version}-%{release}
Obsoletes:	jadetex

%description jadetex
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%package other-utils-doc
Summary:	Other utilities documentation
Group:		Applications/Publishing/TeX

%description other-utils-doc
Other utilities documentation.

%package doc
Summary:	Documentation for TeX Live
Group:		Documentation

%description doc
Assorted useful documentation for TeX Live.

%package doc-bg
Summary:	Bulgarian documentation for TeX Live
Group:		Documentation

%description doc-bg
Assorted useful Bulgarian documentation for TeX Live.

%package doc-cs
Summary:	Czech documentation for TeX Live
Group:		Documentation

%description doc-cs
Assorted useful Czech documentation for TeX Live.

%package doc-de
Summary:	German documentation for TeX Live
Group:		Documentation

%description doc-de
Assorted useful German documentation for TeX Live.

%package doc-el
Summary:	Greek documentation for TeX Live
Group:		Documentation

%description doc-el
Assorted useful Greek documentation for TeX Live.

%package doc-es
Summary:	Spanish documentation for TeX Live
Group:		Documentation

%description doc-es
Assorted useful Spanish documentation for TeX Live.

%package doc-fi
Summary:	Finnish documentation for TeX Live
Group:		Documentation

%description doc-fi
Assorted useful Finnish documentation for TeX Live.

%package doc-fr
Summary:	French documentation for TeX Live
Group:		Documentation

%description doc-fr
Assorted useful French documentation for TeX Live.

%package doc-it
Summary:	Italian documentation for TeX Live
Group:		Documentation

%description doc-it
Assorted useful Italian documentation for TeX Live.

%package doc-ja
Summary:	Japanese documentation for TeX Live
Group:		Documentation

%description doc-ja
Assorted useful Japanese documentation for TeX Live.

%package doc-ko
Summary:	Korean documentation for TeX Live
Group:		Documentation

%description doc-ko
Assorted useful Korean documentation for TeX Live.

%package doc-mn
Summary:	Mongolian documentation for TeX Live
Group:		Documentation

%description doc-mn
Assorted useful Mongolian documentation for TeX Live.

%package doc-nl
Summary:	Dutch documentation for TeX Live
Group:		Documentation

%description doc-nl
Assorted useful Dutch documentation for TeX Live.

%package doc-pl
Summary:	Polish documentation for TeX Live
Group:		Documentation

%description doc-pl
Assorted useful Polish documentation for TeX Live.

%package doc-pt
Summary:	Portuguese documentation for TeX Live
Group:		Documentation

%description doc-pt
Assorted useful Portuguese documentation for TeX Live.

%package doc-ru
Summary:	Russian documentation for TeX Live
Group:		Documentation

%description doc-ru
Assorted useful Russian documentation for TeX Live.

%package doc-sk
Summary:	Slovak documentation for TeX Live
Group:		Documentation

%description doc-sk
Assorted useful Slovak documentation for TeX Live.

%package doc-sl
Summary:	Slovenian documentation for TeX Live
Group:		Documentation

%description doc-sl
Assorted useful Slovenian documentation for TeX Live.

%package doc-th
Summary:	Thai documentation for TeX Live
Group:		Documentation

%description doc-th
Assorted useful Thai documentation for TeX Live.

%package doc-tr
Summary:	Turkish documentation for TeX Live
Group:		Documentation

%description doc-tr
Assorted useful Turkish documentation for TeX Live.

%package doc-uk
Summary:	Ukrainian documentation for TeX Live
Group:		Documentation

%description doc-uk
Assorted useful Ukrainian documentation for TeX Live.

%package doc-vi
Summary:	Vietnamese documentation for TeX Live
Group:		Documentation

%description doc-vi
Assorted useful Vietnamese documentation for TeX Live.

%package doc-zh_CN
Summary:	Chinese documentation for TeX Live
Group:		Documentation

%description doc-zh_CN
Assorted useful Chinese documentation for TeX Live.

%package doc-latex
Summary:	Basic LaTeX packages documentation
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-doc-latex

%description doc-latex
Basic LaTeX packages documentation.

# libraries

%package -n kpathsea
Summary:	File name lookup library
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n kpathsea
File name lookup library.

%package -n kpathsea-devel
Summary:	Kpathsea library filename lookup header files and documentation
Group:		Development/Libraries
Requires:	kpathsea = %{epoch}:%{version}-%{release}

%description -n kpathsea-devel
Kpathsea library filename lookup header files and documentation.

# programs

%package dvips
Summary:	DVI to PostScript converter
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-dvips = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-dvips

%description dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%package dvilj
Summary:	DVI to PCL converter
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-dvilj

%description dvilj
DVI to PCL converter.

%package makeindex
Summary:	A general purpose hierarchical index generator
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-makeindex
Obsoletes:	tetex-makeindex
Obsoletes:	tetex-rumakeindex

%description makeindex
A general purpose hierarchical index generator; it accepts one or more
input files (often produced by a text formatter such as TeX or troff),
sorts the entries, and produces an output file which can be formatted.
The formats of the input and output files are specified in a style
file; by default, input is assumed to be an idx file, as generated by
LaTeX.

%package tex-arrayjob
Summary:	Array data structures for (La)TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-arrayjob
Array data structures for (La)TeX.

%package tex-mathdots
Summary:	Commands to produce dots in math that respect font size
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-mathdots
Commands to produce dots in math that respect font size.

%package tex-midnight
Summary:	A set of useful macro tools
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-midnight
A set of useful macro tools.

%package tex-kastrup
Summary:	Convert numbers into binary, octal and hexadecimal
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-kastrup
Convert numbers into binary, octal and hexadecimal.

%package tex-ofs
Summary:	Olsak's Font System
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-ofs
Olsak's Font System.

%package tex-physe
Summary:	The PHYSE format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-physe
The PHYSE format.

%description tex-physe -l hu.UTF-8
PHYSE formátum.

%package tex-velthuis
Summary:	This package provides support for typesetting texts in Devanagari script (Sanskrit and Hindi)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-velthuis
This package provides support for typesetting texts in Devanagari
script (Sanskrit and Hindi).

%package tex-ytex
Summary:	Macro package developed at MIT
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-ytex
Macro package developed at MIT.

%package metapost
Summary:	MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-metapost

%description metapost
MetaPost.

%package metapost-other
Summary:	Various MetaPost utils
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description metapost-other
Various MetaPost utils.

%package mptopdf
Summary:	MetaPost to PDF converter
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-metapost = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-mptopdf

%description mptopdf
MetaPost to PDF converter.

%package texdoctk
Summary:	Easy access to TeX documentation
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-texdoctk

%description texdoctk
A Perl/Tk-based GUI for easy access to package documentation for TeX
on Unix platforms; the databases it uses are based on the texmf/doc
subtrees of teTeX v.1.0.x, but database files for local configurations
with modified/extended directories can be derived from them. Note that
texdoctk is not a viewer itself, but an interface for finding
documentation files and opening them with the appropriate viewer; so
it relies on appropriate programs to be installed on the system.
However, the choice of these programs can be configured by the
sysadmin or user.

%package -n texconfig
Summary:	TeX typesetting system configurator
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-dvips = %{epoch}:%{version}-%{release}
Requires:	xdvi = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-texconfig

%description -n texconfig
TeX typesetting system configurator.

%package -n xdvi
Summary:	X11 previewer
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	%{name}-dvips
Obsoletes:	tetex-xdvi

%description -n xdvi
xdvi is a program which runs under the X window system. It is used to
preview dvi files, such as are produced by tex and latex.

%package -n xindy
Summary:	Xindy creates sorted and tagged index from raw index
Group:		Applications/Publishing/TeX

%description -n xindy
Xindy creates sorted and tagged index from raw index.

%package -n xindy-albanian
Summary:	Xindy albanian language
Group:		Applications/Publishing/TeX

%description -n xindy-albanian
Xindy albanian language

%package -n xindy-belarusian
Summary:	Xindy belarusian language
Group:		Applications/Publishing/TeX

%description -n xindy-belarusian
Xindy belarusian language

%package -n xindy-bulgarian
Summary:	Xindy bulgarian language
Group:		Applications/Publishing/TeX

%description -n xindy-bulgarian
Xindy bulgarian language

%package -n xindy-croatian
Summary:	Xindy croatian language
Group:		Applications/Publishing/TeX

%description -n xindy-croatian
Xindy croatian language

%package -n xindy-czech
Summary:	Xindy czech language
Group:		Applications/Publishing/TeX

%description -n xindy-czech
Xindy czech language

%package -n xindy-danish
Summary:	Xindy danish language
Group:		Applications/Publishing/TeX

%description -n xindy-danish
Xindy danish language

%package -n xindy-dutch
Summary:	Xindy dutch language
Group:		Applications/Publishing/TeX

%description -n xindy-dutch
Xindy dutch language

%package -n xindy-english
Summary:	Xindy english language
Group:		Applications/Publishing/TeX

%description -n xindy-english
Xindy english language

%package -n xindy-esperanto
Summary:	Xindy esperanto language
Group:		Applications/Publishing/TeX

%description -n xindy-esperanto
Xindy esperanto language

%package -n xindy-estonian
Summary:	Xindy estonian language
Group:		Applications/Publishing/TeX

%description -n xindy-estonian
Xindy estonian language

%package -n xindy-finnish
Summary:	Xindy finnish language
Summary(hu.UTF-8):	Xindy finn nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-finnish
Xindy finnish language

%package -n xindy-french
Summary:	Xindy french language
Group:		Applications/Publishing/TeX

%description -n xindy-french
Xindy french language

%package -n xindy-general
Summary:	Xindy general language
Group:		Applications/Publishing/TeX

%description -n xindy-general
Xindy general language

%package -n xindy-georgian
Summary:	Xindy georgian language
Group:		Applications/Publishing/TeX

%description -n xindy-georgian
Xindy georgian language

%package -n xindy-german
Summary:	Xindy german language
Group:		Applications/Publishing/TeX

%description -n xindy-german
Xindy german language

%package -n xindy-greek
Summary:	Xindy greek language
Group:		Applications/Publishing/TeX

%description -n xindy-greek
Xindy greek language

%package -n xindy-gypsy
Summary:	Xindy gypsy language
Group:		Applications/Publishing/TeX

%description -n xindy-gypsy
Xindy gypsy language

%package -n xindy-hausa
Summary:	Xindy hausa language
Group:		Applications/Publishing/TeX

%description -n xindy-hausa
Xindy hausa language

%package -n xindy-hebrew
Summary:	Xindy hebrew language
Group:		Applications/Publishing/TeX

%description -n xindy-hebrew
Xindy hebrew language

%package -n xindy-hungarian
Summary:	Xindy hungarian language
Group:		Applications/Publishing/TeX

%description -n xindy-hungarian
Xindy hungarian language

%package -n xindy-icelandic
Summary:	Xindy icelandic language
Group:		Applications/Publishing/TeX

%description -n xindy-icelandic
Xindy icelandic language

%package -n xindy-italian
Summary:	Xindy italian language
Group:		Applications/Publishing/TeX

%description -n xindy-italian
Xindy italian language

%package -n xindy-klingon
Summary:	Xindy klingon language
Group:		Applications/Publishing/TeX

%description -n xindy-klingon
Xindy klingon language

%package -n xindy-kurdish
Summary:	Xindy kurdish language
Group:		Applications/Publishing/TeX

%description -n xindy-kurdish
Xindy kurdish language

%package -n xindy-latin
Summary:	Xindy latin language
Group:		Applications/Publishing/TeX

%description -n xindy-latin
Xindy latin language

%package -n xindy-latvian
Summary:	Xindy latvian language
Group:		Applications/Publishing/TeX

%description -n xindy-latvian
Xindy latvian language

%package -n xindy-lithuanian
Summary:	Xindy lithuanian language
Group:		Applications/Publishing/TeX

%description -n xindy-lithuanian
Xindy lithuanian language

%package -n xindy-lower-sorbian
Summary:	Xindy lower-sorbian language
Group:		Applications/Publishing/TeX

%description -n xindy-lower-sorbian
Xindy lower-sorbian language

%package -n xindy-macedonian
Summary:	Xindy macedonian language
Group:		Applications/Publishing/TeX

%description -n xindy-macedonian
Xindy macedonian language

%package -n xindy-mongolian
Summary:	Xindy mongolian language
Group:		Applications/Publishing/TeX

%description -n xindy-mongolian
Xindy mongolian language

%package -n xindy-norwegian
Summary:	Xindy norwegian language
Group:		Applications/Publishing/TeX

%description -n xindy-norwegian
Xindy norwegian language

%package -n xindy-polish
Summary:	Xindy polish language
Group:		Applications/Publishing/TeX

%description -n xindy-polish
Xindy polish language

%package -n xindy-portuguese
Summary:	Xindy portuguese language
Group:		Applications/Publishing/TeX

%description -n xindy-portuguese
Xindy portuguese language

%package -n xindy-romanian
Summary:	Xindy romanian language
Group:		Applications/Publishing/TeX

%description -n xindy-romanian
Xindy romanian language

%package -n xindy-russian
Summary:	Xindy russian language
Group:		Applications/Publishing/TeX

%description -n xindy-russian
Xindy russian language

%package -n xindy-serbian
Summary:	Xindy serbian language
Group:		Applications/Publishing/TeX

%description -n xindy-serbian
Xindy serbian language

%package -n xindy-slovak
Summary:	Xindy slovak language
Group:		Applications/Publishing/TeX

%description -n xindy-slovak
Xindy slovak language

%package -n xindy-slovenian
Summary:	Xindy slovenian language
Group:		Applications/Publishing/TeX

%description -n xindy-slovenian
Xindy slovenian language

%package -n xindy-spanish
Summary:	Xindy spanish language
Group:		Applications/Publishing/TeX

%description -n xindy-spanish
Xindy spanish language

%package -n xindy-swedish
Summary:	Xindy swedish language
Group:		Applications/Publishing/TeX

%description -n xindy-swedish
Xindy swedish language

%package -n xindy-turkish
Summary:	Xindy turkish language
Group:		Applications/Publishing/TeX

%description -n xindy-turkish
Xindy turkish language

%package -n xindy-ukrainian
Summary:	Xindy ukrainian language
Group:		Applications/Publishing/TeX

%description -n xindy-ukrainian
Xindy ukrainian language

%package -n xindy-upper-sorbian
Summary:	Xindy upper-sorbian language
Group:		Applications/Publishing/TeX

%description -n xindy-upper-sorbian
Xindy upper-sorbian language

%package -n xindy-vietnamese
Summary:	Xindy vietnamese language
Group:		Applications/Publishing/TeX

%description -n xindy-vietnamese
Xindy vietnamese language


%package pdftex
Summary:	TeX generating PDF files instead DVI
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-bluesky = %{epoch}:%{version}-%{release}
Requires:	ghostscript
Provides:	tetex-format-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-pdftex
Obsoletes:	tetex-format-pdftex
Obsoletes:	tetex-pdftex

%description pdftex
TeX generating PDF files instead DVI.

%package psutils
Summary:	PostScript Utilities
Group:		Applications/Printing
Provides:	psutils
Obsoletes:	psutils
Obsoletes:	texlive-epsutils
Obsoletes:	texlive-filters

%description psutils
This archive contains some utilities for manipulating PostScript
documents. Page selection and rearrangement are supported, including
arrangement into signatures for booklet printing, and page merging for
n-up printing.

%package phyzzx
Summary:	A TeX format for physicists
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description phyzzx
A TeX format for physicists.

%package omega
Summary:	Extended unicode TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-omega = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-omega

%description omega
Omega is a version of the TeX program modified for multilingual
typesetting. It uses unicode, and has additional primitives for (among
other things) bidirectional typesetting.

# formats

%package plain
Summary:	Plain TeX format basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-format-plain
Provides:	tetex-plain
Obsoletes:	tetex-cyrplain
Obsoletes:	tetex-format-cyrplain
Obsoletes:	tetex-format-plain
Obsoletes:	tetex-plain

%description plain
Plain TeX format basic files.

%package mex
Summary:	MeX Plain Format basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	texlive-fonts-pl = %{epoch}:%{version}-%{release}
Requires:	texlive-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-mex

%description mex
MeX Plain Format basic files.

%package format-mex
Summary:	MeX Plain Format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	texlive-mex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-mex

%description format-mex
MeX Plain Format.

%package format-pdfmex
Summary:	PDFMeX Plain Format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfmex

%description format-pdfmex
PDFMeX Plain Format.

%package format-utf8mex
Summary:	MeX Plain Format with UTF-8 encoded source files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-mex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-utf8mex

%description format-utf8mex
MeX Plain Format with UTF-8 encoded source files.

%package amstex
Summary:	AMS macros for Plain TeX basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-format-amstex = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Provides:	tetex-ams
Obsoletes:	tetex-ams
Obsoletes:	tetex-amstex
Obsoletes:	tetex-plain-amsfonts

%description amstex
American Mathematical Society macros for Plain TeX basic files.

%package format-amstex
Summary:	AMS macros for Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-amstex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-amstex
Obsoletes:	tetex-format-cyramstex

%description format-amstex
American Mathematical Society macros for Plain TeX.

%package csplain
Summary:	TeX CSPlain format basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cs = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Provides:	tetex-csplain
Obsoletes:	tetex-csplain

%description csplain
TeX CSPlain format basic files.

%package format-csplain
Summary:	TeX CSPlain format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-csplain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-csplain

%description format-csplain
TeX CSPlain format.

%package format-pdfcsplain
Summary:	PDFTeX CSPlain format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-csplain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfcsplain

%description format-pdfcsplain
PDFTeX CSPlain format.

%package cslatex
Summary:	CSLaTeX format basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cs = %{epoch}:%{version}-%{release}
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Provides:	tetex-cslatex
Obsoletes:	tetex-cslatex

%description cslatex
CSLaTeX format basic files.

%package format-cslatex
Summary:	CSLaTeX format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-cslatex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-cslatex

%description format-cslatex
CSLaTeX format.

%package format-pdfcslatex
Summary:	PDF CSLaTeX format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-cslatex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-pdfcslatex

%description format-pdfcslatex
PDF CSLaTeX format.

%package eplain
Summary:	EPlain format basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-plain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-eplain
Obsoletes:	tetex-etex

%description eplain
EPlain format basic files.

%package format-eplain
Summary:	EPlain format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-eplain = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-eplain

%description format-eplain
EPlain format.

%package context
Summary:	ConTeXt macro package basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-context
Obsoletes:	tetex-context

%define		_noautoreq	'perl(path_tre)'

%description context
A full featured, parameter driven macro package, which fully supports
advanced interactive documents.

This package contains basic files.

%package format-context-de
Summary:	German ConTeXt format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-context-de

%description format-context-de
German ConTeXt format.

%package format-context-en
Summary:	English ConTeXt format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-context-en

%description format-context-en
English ConTeXt format.

%package format-context-nl
Summary:	Dutch ConTeXt format
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-format-context-nl

%description format-context-nl
Dutch ConTeXt format.

%package latex
Summary:	LaTeX macro package basic files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-ruhyphen = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-ukrhyph = %{epoch}:%{version}-%{release}
# for misc/eurosym:
Requires:	%{name}-fonts-eurosym = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-babel = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
Suggests:	%{name}-fonts-jknappen
Suggests:	%{name}-latex-ucs = %{epoch}:%{version}-%{release}
Provides:	tetex-format-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-koma-script
Obsoletes:	tetex-format-latex
Obsoletes:	tetex-latex
Obsoletes:	tetex-latex-SIunits
Obsoletes:	tetex-latex-caption
Obsoletes:	tetex-latex-curves
Obsoletes:	tetex-latex-dinbrief
Obsoletes:	tetex-latex-draftcopy
Obsoletes:	tetex-latex-dstroke
Obsoletes:	tetex-latex-dvilj
Obsoletes:	tetex-latex-eepic
Obsoletes:	tetex-latex-endfloat
Obsoletes:	tetex-latex-fancyhdr
Obsoletes:	tetex-latex-fancyheadings
Obsoletes:	tetex-latex-fancyvrb
Obsoletes:	tetex-latex-fp
Obsoletes:	tetex-latex-graphics
Obsoletes:	tetex-latex-hyperref
Obsoletes:	tetex-latex-koma-script
Obsoletes:	tetex-latex-labels
Obsoletes:	tetex-latex-listings
Obsoletes:	tetex-latex-misc
Obsoletes:	tetex-latex-ms
Obsoletes:	tetex-latex-multirow
Obsoletes:	tetex-latex-mwcls
Obsoletes:	tetex-latex-mwdtools
Obsoletes:	tetex-latex-natbib
Obsoletes:	tetex-latex-ntgclass
Obsoletes:	tetex-latex-oberdiek
Obsoletes:	tetex-latex-pb-diagram
Obsoletes:	tetex-latex-pstricks
Obsoletes:	tetex-latex-qfonts
Obsoletes:	tetex-latex-revtex4
Obsoletes:	tetex-latex-seminar
Obsoletes:	tetex-latex-t2
Obsoletes:	tetex-latex-titlesec
Obsoletes:	tetex-latex-tools
Obsoletes:	tetex-latex-units
Obsoletes:	tetex-mwcls
Obsoletes:	tetex-revtex4

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains basic files.

%package latex-colortab
Summary:	Shade cells of tables and halign
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-colortab
Shade cells of tables and halign.

%package latex-12many
Summary:	Generalising mathematical index sets
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-12many
Generalising mathematical index sets.

%package latex-abstract
Summary:	Control the typesetting of the abstract environment
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-abstract
Control the typesetting of the abstract environment.

%description latex-abstract -l hu.UTF-8
Az "abstract" környezet szedésének irányítása.

%package latex-accfonts
Summary:	Utilities to derive new fonts from existing ones
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description latex-accfonts
Utilities to derive new fonts from existing ones.

%package latex-adrconv
Summary:	BibTeX styles to implement an address database
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-adrconv
BibTeX styles to implement an address database.

%package latex-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ae = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-ae
Obsoletes:	tetex-latex-ae

%description latex-ae
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package is called AE fonts (for Almost
European). The main use of the package is to produce PDF files using
versions of the CM fonts instead of the bitmapped EC fonts.

%package latex-algorithms
Summary:	Floating algorithm environment
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-algorith
Obsoletes:	tetex-latex-algorithms

%description latex-algorithms
Defines a floating algorithm environment designed to work with the
algorithmic package.

%package latex-ams
Summary:	AMS math facilities for LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-ams
Obsoletes:	tetex-latex-ams
Obsoletes:	tetex-latex-amscls
Obsoletes:	tetex-latex-amsfonts
Obsoletes:	tetex-latex-amsmath

%description latex-ams
This package is the principal package in the AMS-LaTeX distribution.
It adapts for use in LaTeX most of the mathematical features found in
AMS-TeX.

%package latex-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-antp = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-antp

%description latex-antp
A replica of Antykwa Poltawskiego font in PostScript Type 1 format
- -- preliminary version. This font was designed in the 'twenties and
  the 'thirties of XX century by a Polish graphic artist and a
  typographer Adam Poltawski. It was widely used by Polish printing
  houses as long as metal types were in use (until ca the 'sixties).
  Perhaps the first complete font family programmed and parametrized in
  METAPOST.

%package latex-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-antt = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-antt

%description latex-antt
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized as Type
1.

%package latex-appendix
Summary:	Extra control of appendices
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-appendix
Extra control of appendices.

%package latex-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbm = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-bbm

%description latex-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%package latex-bardiag
Summary:	LateX package for drawing bar diagrams
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description latex-bardiag
LateX package for drawing bar diagrams.

%package latex-bbold
Summary:	Sans serif blackboard bold for LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbold = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-bbold

%description latex-bbold
A geometric sans serif blackboard bold font, for use in mathematics.

%package latex-bibtex
Summary:	Bibliography management for LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-bibtex
Obsoletes:	tetex-bibtex
Obsoletes:	tetex-latex-bibtex
Obsoletes:	tetex-natbib
Obsoletes:	tetex-rubibtex

%description latex-bibtex
Bibliography management for LaTeX.

%package latex-beamer
Summary:	A LaTeX class for producing presentations and slides
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-beamer

%description latex-beamer
A LaTeX class for producing presentations and slides.

%package latex-bezos
Summary:	Packages by Javier Bezos (additional math tools)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-bezos
Packages by Javier Bezos (additional math tools).

%package latex-bibtex-ams
Summary:	BibTeX style files for American Mathematical Society publications
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-ams
Obsoletes:	tetex-latex-bibtex-ams

%description latex-bibtex-ams
BibTeX style files for American Mathematical Society publications.

%description latex-bibtex-ams -l pl.UTF-8
Pliki stylów BibTeXa do publikacji American Mathematical Society.

%package latex-bibtex-dk
Summary:	Danish variants of the standard BibTeX styles
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-bibtex-dk

%description latex-bibtex-dk
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) into Danish. The files have been
extended with ISBN, ISSN and URL fields which can be enabled through a
LaTeX style file.

%package latex-bibtex-pl
Summary:	Polish bibliography management for LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-plbib
Obsoletes:	tetex-latex-bibtex-pl

%description latex-bibtex-pl
Polish bibliography management for LaTeX.

%package latex-bibtex-german
Summary:	German variants of standard BibTeX styles
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-germbib
Obsoletes:	tetex-latex-bibtex-german

%description latex-bibtex-german
German variants of standard BibTeX styles.

%package latex-bibtex-revtex4
Summary:	BibTeX styles for REVTeX4
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-revtex4
Obsoletes:	tetex-latex-bibtex-revtex4

%description latex-bibtex-revtex4
BibTeX styles for REVTeX4.

%package latex-bibtex-jurabib
Summary:	Extended BibTeX citation support for the humanities and legal texts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-jurabib
Obsoletes:	tetex-latex-bibtex-jurabib

%description latex-bibtex-jurabib
Extended BibTeX citation support for the humanities and legal texts.

%package latex-bibtex-styles
Summary:	Various BibTeX styles
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}

%description latex-bibtex-styles
Various BibTeX styles.

%package latex-bibtex-vancouver
Summary:	Bibliographic style file for Biomedical Journals
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}

%description latex-bibtex-vancouver
Bibliographic style file for Biomedical Journals.

%package latex-booktabs
Summary:	Publication quality tables in LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-booktabs
Publication quality tables in LaTeX.

%package latex-caption
Summary:	Customising captions in floating environments
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-caption
Customising captions in floating environments.

%package latex-carlisle
Summary:	Miscellaneous small packages by David Carlisle
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-carlisle
Obsoletes:	tetex-latex-carlisle

%description latex-carlisle
Miscellaneous small packages by David Carlisle.

%package latex-ccfonts
Summary:	Support for Concrete text and math fonts in LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-ccfonts

%description latex-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX package
for typesetting documents using Concrete as the default font family.
The files support OT1, T1, TS1, and Concrete math including AMS fonts
(Ulrik Vieth's concmath).

%package latex-cite
Summary:	Supports compressed, sorted lists of numerical citations
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-cite

%description latex-cite
Supports compressed, sorted lists of numerical citations.

%package latex-cmbright
Summary:	Support for CM Bright fonts in LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-cmbright = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-cmbright

%description latex-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text fonts of
various shapes as well as all the fonts necessary for mathematical
typesetting, incl. AMS symbols. This collection provides all the
necessary files for using the fonts with LaTeX.

%package latex-comment
Summary:	Selectively include/excludes portions of text
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-comment
Selectively include/excludes portions of text.

%package latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-concmath = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-concmath

%description latex-concmath
LaTeX package and font definition files to access the Concrete math
fonts, which were derived from Computer Modern math fonts using
parameters from Concrete Roman text fonts.

%package latex-currvita
Summary:	Typeset a curriculum vitae
Summary(hu.UTF-8):	Önéletrajzok írása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-currvita
Typeset a curriculum vitae.

%package latex-curves
Summary:	Curves for LaTeX picture environment
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-curves
Curves for LaTeX picture environment.

%package latex-custom-bib
Summary:	Customized BibTeX styles for LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-custom-bib

%description latex-custom-bib
Package generating customized BibTeX bibliography styles from a
generic file using docstrip. Includes support for the Harvard style.

%package latex-cyrillic
Summary:	LaTeX Cyrillic support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-cyrillic
Obsoletes:	tetex-latex-cyrillic

%description latex-cyrillic
LaTeX Cyrillic support.

%package latex-enumitem
Summary:	A package to customize the three basic lists
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-enumitem
A package to customize the three basic lists (enumerate, itemize and
description).

%package latex-exams
Summary:	Various document classes to typeset exams
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-exams
Various document classes to typeset exams.

%package latex-float
Summary:	Tools to manipulate float objects
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-float
Tools to manipulate float objects.

%package latex-foiltex
Summary:	The FoilTeX is a collection of LaTeX files for making foils
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-foiltex
The FoilTeX is a collection of LaTeX files for making foils.

%package latex-formlett
Summary:	Letters to multiple recipients
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-formlett
Letters to multiple recipients.

%package latex-formular
Summary:	Create forms containing field for manual entry
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-formular
Create forms containing field for manual entry.

%package latex-gbrief
Summary:	Letter document class
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-gbrief
Letter document class.

%package latex-keystroke
Summary:	Graphical representation of keys on keyboard
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-keystroke
Graphical representation of keys on keyboard.

%package latex-labbook
Summary:	Typeset laboratory journals
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-labbook
Typeset laboratory journals.

%package latex-lcd
Summary:	Alphanumerical LCD-style displays
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-lcd
Alphanumerical LCD-style displays.

%package latex-leaflet
Summary:	Create small handouts (flyers)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-leaflet
Create small handouts (flyers).

%package latex-leftidx
Summary:	Left and right subscripts and superscripts in math mode
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-leftidx
Left and right subscripts and superscripts in math mode.

%package latex-lewis
Summary:	Draw Lewis structures (chemistry)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-lewis
Draw Lewis structures (chemistry).

%package latex-lm
Summary:	LaTeX styles for Latin Modern family fonts
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-lm = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-lm
Obsoletes:	texlive-fonts-type1-lm

%description latex-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%package latex-lastpage
Summary:	Reference last page for "Page N of M" type footers
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description latex-lastpage
Reference last page for Page N of M type footers.

%package latex-lineno
Summary:	Line numbers on paragraphs
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-lineno

%description latex-lineno
The LaTeX package lineno.sty provides line numbers on paragraphs.
After TeX has broken a paragraph into lines there will be line numbers
attached to them, with the possibility to make references through the
LaTeX \ref, \pageref cross reference mechanism.

%package latex-metre
Summary:	Support for the work of classicists
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-metre
Support for the work of classicists.

%package latex-games
Summary:	Packages for typesetting games
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-games
Chess, chinese chess, crosswords, go, backgammon and more.

%package latex-extend
Summary:	Extensions, patches, improvements of main LaTeX styles, environments
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-ltablex
Obsoletes:	tetex-latex-ltablex

%description latex-extend
Extensions, patches, improvements of main LaTeX styles, environments.

%package latex-effects
Summary:	Additional effects to fonts, texts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-effects
Additional effects to fonts, texts.

%package latex-math-sources
Summary:	Sources of latex-math
Group:		Applications/Publishing/TeX

%description latex-math-sources
Sources of latex-math.

%package latex-math
Summary:	Mathematical packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-bbm = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-stmaryrd = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-carlisle = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-psnfss = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-pst-3dplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-wasysym = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-xkeyval = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-xypic = %{epoch}:%{version}-%{release}
# gnuplottex needs gnuplot
Requires:	gnuplot

%description latex-math
Mathematical packages.

%package latex-misc
Summary:	Misc packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-misc
This packages contains:
- cooking: typeset recipes.
- cuisine: typeset recipes.
- fixme: insert "fixme" notes into draft documents.
- recipecard: typeset recipes in note-card-sized boxes.
- todo: make a to-do list for a document.

%package latex-music
Summary:	Musical packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-music
This package contains:
- abc: support ABC music notation in LaTeX.
- guitar: guitar chords and song texts.
- songbook: package for typesetting song lyrics and chord books.

%package latex-physics
Summary:	Physical packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Suggests:	%{name}-latex-SIstyle
Suggests:	%{name}-latex-SIunits
Suggests:	%{name}-latex-siunitx

%description latex-physics
Physical packages.

%package latex-biology
Summary:	Biological packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-xetex = %{epoch}:%{version}-%{release}

%description latex-biology
This package contains:
- biocon: typesetting biological species names
- dnaseq: format DNA base sequences.

%package latex-presentation
Summary:	Presentations in LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex-foiltex = %{epoch}:%{version}-%{release}
Suggests:	%{name}-latex-prosper = %{epoch}:%{version}-%{release}

%description latex-presentation
Presentations in LaTeX

%package latex-chem
Summary:	Chemical packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Suggests:	%{name}-latex-lewis

%description latex-chem
Chemical packages.

%package latex-informatic
Summary:	Informatical packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-informatic
Informatical packages.

%package latex-pdftools
Summary:	Various tools to pdf output
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-pdftools
Various tools to pdf output

%package latex-microtype
Summary:	An interface to the micro-typographic extensions of pdfTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-microtype

%description latex-microtype
The `microtype' package provides a LaTeX interface to pdfTeX's
micro-typographic extensions: character protrusion and font expansion.
It allows to restrict character protrusion and/or font expansion to a
definable set of fonts, and to configure micro-typographic aspects of
the fonts in a straight-forward and flexible way. Settings for various
fonts are provided.

%package latex-musictex
Summary:	Typesetting music with TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-musictex
Typesetting music with TeX.

%package latex-lucidabr
Summary:	Package to make Lucida Bright fonts usable with LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-lucidabr

%description latex-lucidabr
Package to make Lucida Bright fonts usable with LaTeX.

%package latex-marvosym
Summary:	Styles for Martin Vogel's Symbol (marvosym) font
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-marvosym = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-marvosym
Obsoletes:	tetex-latex-marvosym

%description latex-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%package latex-mflogo
Summary:	LaTeX support for MetaFont and logo fonts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-mflogo = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mflogo

%description latex-mflogo
LaTeX package and font definition file to access the Knuthian `logo'
fonts described in `The MetaFontbook' and the MetaFont and logos in
LaTeX documents.

%package latex-mfnfss
Summary:	Font description files to use extra fonts like yinit and ygoth
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mfnfss

%description latex-mfnfss
Font description files to use extra fonts like yinit and ygoth.

%package latex-minitoc
Summary:	Produce a table of contents for each chapter
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-minitoc

%description latex-minitoc
Produce a table of contents for each chapter.

%package latex-mltex
Summary:	Support for MLTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-mltex

%description latex-mltex
Support for MLTeX, the multilingual TeX extension from Michael J.
Ferguson.

%package latex-multienum
Summary:	Multi-column enumerated lists
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-multienum
Multi-column enumerated lists.

%package latex-moreverb
Summary:	Extended verbatim
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-moreverb
Extended verbatim.

%package latex-ntheorem
Summary:	Enhanced theorem environment
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-ntheorem
Enhanced theorem environment.

%package latex-other
Summary:	Other LaTeX packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-platex

%description latex-other
Other LaTeX packages.

%package latex-other-doc
Summary:	Other LaTeX packages documentation
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-other-doc
Other LaTeX packages documentation.

%package latex-pdfslide
Summary:	Presentation slides using pdftex
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-pdfslide
Presentation slides using pdftex.

%package latex-pgf
Summary:	The TeX Portable Graphic Format
Summary(hu.UTF-8):	TeX Portable Graphic Formátum
Summary(pl.UTF-8):	Przenośny format grafiki dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-xcolor = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-pgf

%description latex-pgf
A macro package for creating graphics directly in TeX and LaTeX.

%package latex-polynom
Summary:	Macros for manipulating polynomials
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-polynom
Macros for manipulating polynomials.

%package latex-polynomial
Summary:	Typeset (univariate) polynomials
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-polynomial
Typeset (univariate) polynomials.

%package latex-programming
Summary:	Additional utilities to programming LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-programming
Additional utilities to programming LaTeX.

%package latex-prosper
Summary:	LaTeX class for high quality slides
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-xetex = %{epoch}:%{version}-%{release}

%description latex-prosper
LaTeX class for high quality slides.

%package latex-pseudocode
Summary:	LaTeX enviroment for specifying algorithms in a natural way
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-pseudocode
LaTeX enviroment for specifying algorithms in a natural way.

%package latex-psnfss
Summary:	LaTeX font support for common PostScript fonts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-adobe = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-psnfss
Obsoletes:	tetex-latex-mathptm
Obsoletes:	tetex-latex-mathptmx
Obsoletes:	tetex-latex-psnfss

%description latex-psnfss
LaTeX font definition files, macros and font metrics for common
PostScript fonts.

%package latex-pst-2dplot
Summary:	A PSTricks package for drawing 2D curves
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-2dplot
A PSTricks package for drawing 2D curves.

%package latex-pst-3dplot
Summary:	Draw 3d curves and graphs using PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-3dplot
Draw 3d curves and graphs using PSTricks.

%package latex-pst-bar
Summary:	Produces bar charts using pstricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-bar
Produces bar charts using pstricks.

%package latex-pst-circ
Summary:	PSTricks package for drawing electric circuits
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-circ
PSTricks package for drawing electric circuits.

%package latex-pst-diffraction
Summary:	Print diffraction patterns from various apertures
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-diffraction
Print diffraction patterns from various apertures.

%package latex-pst-eucl
Summary:	Euclidian geometry with pstricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-eucl
Euclidian geometry with pstricks.

%package latex-pst-fun
Summary:	Draw "funny" objects with PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-fun
Draw "funny" objects with PSTricks.

%package latex-pst-func
Summary:	PSTricks package for plotting mathematical functions
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-func
PSTricks package for plotting mathematical functions.

%package latex-pst-fr3d
Summary:	Draw 3-dimensional framed boxes using PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-fr3d
Draw 3-dimensional framed boxes using PSTricks.

%package latex-pst-fractal
Summary:	Draw fractal sets using PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-fractal
Draw fractal sets using PSTricks.

%package latex-pst-infixplot
Summary:	Using pstricks plotting capacities with infix expressions rather than RPN
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-infixplot
Using pstricks plotting capacities with infix expressions rather than
RPN.

%package latex-pst-math
Summary:	Enhancement of PostScript math operators to use with pstricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-math
Enhancement of PostScript math operators to use with pstricks.

%package latex-pst-ob3d
Summary:	Three dimensional objects using PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-ob3d
Three dimensional objects using PSTricks.

%package latex-pst-optexp
Summary:	Drawing optical experimental setups
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-optexp
Drawing optical experimental setups.

%package latex-pst-optic
Summary:	Drawing optics diagrams
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-optic
Drawing optics diagrams.

%package latex-pst-text
Summary:	Text and character manipulation in PSTricks
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-text
Text and character manipulation in PSTricks.

%package latex-pst-uncategorized
Summary:	Other uncategorized PSTricks packages
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-tex-pstricks = %{epoch}:%{version}-%{release}

%description latex-pst-uncategorized
Other uncategorized PSTricks packages.

%package latex-pxfonts
Summary:	PX fonts LaTeX support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-px = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-pxfonts

%description latex-pxfonts
PX fonts LaTeX support.

%package latex-SIstyle
Summary:	Package to typeset SI units, numbers and angles
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}

%description latex-SIstyle
Package to typeset SI units, numbers and angles.

%package latex-SIunits
Summary:	The SIunits package can be used to standardise the use of units in your writings
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{epoch}:%{version}-%{release}

%description latex-SIunits
The SIunits package can be used to standardise the use of units in
your writings.

%package latex-siunitx
Summary:	A comprehensive (SI) units package
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-siunitx
A comprehensive (SI) units package.

%package latex-sources
Summary:	LaTeX sources
Group:		Applications/Publishing/TeX

%description latex-sources
LaTeX sources.

%package latex-styles
Summary:	Various LaTeX styles
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-styles
Various LaTeX styles.

%package latex-lang
Summary:	LaTeX support for non-english languages
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-lang
LaTeX support for non-english languages.

%package latex-Tabbing
Summary:	Tabbing with accented letters
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description latex-Tabbing
Tabbing with accented letters.

%package latex-txfonts
Summary:	TX fonts LaTeX support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-txfonts

%description latex-txfonts
TX fonts LaTeX support.

%package latex-ucs
Summary:	This package contains support for using UTF-8 as input encoding in LaTeX documents
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}

%description latex-ucs
This package contains support for using UTF-8 as input encoding in
LaTeX documents.

%package latex-umlaute
Summary:	An interface to inputenc for using alternate input encodings
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-umlaute

%description latex-umlaute
An interface to inputenc for using alternate input encodings.

%package latex-wasysym
Summary:	Extra characters from the Waldis symbol fonts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-fonts-wasy = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex-wasysym
Obsoletes:	tetex-latex-wasysym

%description latex-wasysym
Makes some additional characters available that come from the wasy
fonts (Waldis symbol fonts). These fonts are not automatically
included in NFSS2/LaTeX2e since they take up important space and often
aren't necessary if one makes use of the packages amsfonts or amssymb.
Symbols include: join box, diamond, leadsto, sqsubset, lhd, rhd,
apple, ocircle invneg, logof, varint, male, female, phone, clock,
lightning, pointer, sun, bell, permil, smiley, various electrical
symbols, shapes, music notes, circles, signs, astronomy, etc.

%package latex-xcolor
Summary:	Allows for access to color tints, shades, tones etc
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-latex-xcolor

%description latex-xcolor
`xcolor' provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It allows
to select a document-wide target color model and offers tools for
automatic color schemes, conversion between eight color models, and
alternating table row colors.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-jknappen = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-urw = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-psnfss = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdftex = %{epoch}:%{version}-%{release}
Provides:	tetex-format-pdflatex
Obsoletes:	tetex-format-pdflatex

%description format-pdflatex
This package contains PDF LaTeX format.

%package scripts
Summary:	Various scripts
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
Various scripts.

%package tlmgr
Summary:	TeXLive manager
Group:		Applications/Publishing/TeX

%description tlmgr
tlmgr manages an existing TeX Live installation, both packages and
configuration options. It performs many of the same actions as
texconfig, and more besides.

# generic macros

%package tex-babel
Summary:	Multilingual support for TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-babel
Obsoletes:	tetex-tex-babel

%description tex-babel
Multilingual support for TeX.

%package tex-german
Summary:	Supports the new German orthography (neue deutsche Rechtschreibung)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-german
Obsoletes:	tetex-tex-german

%description tex-german
Supports the new German orthography (neue deutsche Rechtschreibung).

%package tex-insbox
Summary:	A TeX macro for inserting pictures/boxes into paragraphs
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-insbox
A TeX macro for inserting pictures/boxes into paragraphs.

%package tex-mfpic
Summary:	Macros which generate Metafont or Metapost for drawing pictures
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-mfpic

%description tex-mfpic
Macros which generate Metafont or Metapost for drawing pictures.

%package tex-misc
Summary:	Miscellaneous TeX macros
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-misc
Obsoletes:	tetex-tex-eijkhout
Obsoletes:	tetex-tex-misc

%description tex-misc
Miscellaneous TeX macros.

%package tex-pictex
Summary:	Picture drawing macros for TeX and LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-pictex

%description tex-pictex
Picture drawing macros for TeX and LaTeX.

%package tex-psizzl
Summary:	A TeX format for physics papers
Summary(hu.UTF-8):	TeX formátum fizikai kiadványokhoz
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-psizzl
A TeX format for physics papers.

%package tex-pstricks
Summary:	PostScript macros for TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name}-dvips = %{epoch}:%{version}-%{release}
Requires:	%{name}-tex-misc = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-pstricks
Obsoletes:	tetex-tex-pstricks

%description tex-pstricks
An extensive collection of PostScript macros that is compatible with
most TeX macro packages, including Plain TeX, LaTeX, AMS-TeX, and
AMS-LaTeX. Included are macros for color, graphics, pie charts,
rotation, trees and overlays. It has many special features, including:
a wide variety of graphics (picture drawing) macros, with a flexible
interface and with color support. There are macros for coloring or
shading the cells of tables.

%package tex-qpxqtx
Summary:	QuasiTimes and TX fonts typesetting support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-qpxqtx = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-qpx
Obsoletes:	tetex-tex-qtx

%description tex-qpxqtx
QuasiTimes and TX fonts typesetting support.

%package tex-huhyphen
Summary:	Hungarian hyphenation
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tex-huhyphen
Hungarian hyphenation.

%package tex-ruhyphen
Summary:	Russian hyphenation
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-ruhyphen
Obsoletes:	tetex-tex-ruhyphen

%description tex-ruhyphen
A collection of Russian hyphenation patterns supporting a number of
Cyrillic font encodings, including T2, UCY (Omega Unicode Cyrillic),
LCY, LWN (OT2), and koi8-r.

%package tex-spanish
Summary:	Various TeX related files for typesetting documents written in Spanish
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-spanish
Obsoletes:	tetex-tex-spanishb

%description tex-spanish
Various TeX related files for typesetting documents written in
Spanish, including hyphenation and dictionaries.

%package tex-texdraw
Summary:	Graphical macros, using embedded PostScript
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-texdraw

%description tex-texdraw
Graphical macros, using embedded PostScript.

%package tex-thumbpdf
Summary:	Thumbnails for PDFTeX and dvips/ps2pdf
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-thumbpdf

%description tex-thumbpdf
Provides support, using Perl, for thumbnails in pdfTeX and
dvips/ps2pdf, using ghostscript to generate the thumbnails which get
represented in a TeX readable file that is read by the package
thumbpdf.sty to automatically include the thumbnails. Works with both
plain TeX and LaTeX.

%package tex-ukrhyph
Summary:	Ukranian hyphenation
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	tetex-tex-ukrhyph
Obsoletes:	tetex-tex-ukrhyph

%description tex-ukrhyph
This package allows the use of different hyphenation patterns for the
Ukrainian language for various Cyrillic font encodings. Contains
packages implementing traditional rules, modern rules, and combined
English-Ukrainian hyphenation.

%package latex-variations
Summary:	Typeset tables of variations of functions
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description latex-variations
Typeset tables of variations of functions.

%package latex-vietnam
Summary:	Vietnamese language support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-latex-urwvn
Obsoletes:	tetex-latex-vietnam
Obsoletes:	tetex-tex-vietnam

%description latex-vietnam
Vietnamese language support.

%package tex-xypic
Summary:	Package for typesetting a variety of graphs and diagrams with TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-xypic = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-xypic
Obsoletes:	tetex-xypic

%description tex-xypic
A package for typesetting a variety of graphs and diagrams with TeX.
Xy-pic works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX,
and plain TeX), in particular Xy-pic is provided as a LaTeX2e
`supported package'.

%package tex-xkeyval
Summary:	Extension to keyval package
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-tex-xkeyval

%description tex-xkeyval
Extension to keyval package.

%package dirs-fonts
Summary:	TeX font directories
Group:		Fonts
Provides:	tetex-dirs-fonts
Obsoletes:	tetex-dirs-fonts

%description dirs-fonts
TeX font directories.

# fonts

%package fonts-adobe
Summary:	Adobe fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-adobe
Obsoletes:	tetex-fonts-adobe

%description fonts-adobe
Adobe fonts.

%package fonts-larm
Summary:	Larm (cyrillic) fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-larm
Larm (cyrillic) fonts.

%package fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-ae

%description fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%package fonts-ams
Summary:	AMS fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex-bibtex = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-ams
Obsoletes:	tetex-fonts-ams

%description fonts-ams
AMS fonts.

%package fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-antp

%description fonts-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%package fonts-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-antt

%description fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%package fonts-arphic
Summary:	Arphic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-arphic
Arphic fonts.

%package fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bbm

%description fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%package fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bbold

%description fonts-bbold
Sans serif blackboard bold for LaTeX.

%package fonts-bitstream
Summary:	Bitstream fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-bitstrea

%description fonts-bitstream
Bitstream fonts.

%package fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cc-pl

%description fonts-cc-pl
Polish version of Computer Concrete fonts.

%package fonts-cg
Summary:	Compugraphic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cg

%description fonts-cg
Compugraphic fonts.

%package fonts-cm
Summary:	Computer Modern fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-cm
Obsoletes:	tetex-fonts-cm

%description fonts-cm
Computer Modern fonts.

%package fonts-cmbright
Summary:	CM Bright fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cmbright

%description fonts-cmbright
CM Bright fonts.

%package fonts-cmsuper
Summary:	CM Super fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-cmsuper
CM Super fonts.

%description fonts-cmsuper -l hu.UTF-8
CM Super betűtípus

%package fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-cmcyr
Obsoletes:	tetex-fonts-cmcyr
Obsoletes:	texlive-fonts-type1-cmcyr

%description fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%package fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-cmextra
Obsoletes:	tetex-fonts-cmextra

%description fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%package fonts-concmath
Summary:	Concrete Math fonts
Group:		Fonts
Obsoletes:	tetex-fonts-concmath

%description fonts-concmath
Concrete Math fonts.

%package fonts-concrete
Summary:	Concrete Roman fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-concrete

%description fonts-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally for use
with Euler math fonts.

%package fonts-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cs

%description fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%package fonts-ecc
Summary:	Sources for the European Concrete fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-ecc

%description fonts-ecc
The MetaFont sources and tfm files of the European Concrete Fonts.
This is the EC implementation of Knuth's Concrete fonts, including
also the corresponding text companion fonts.

%package fonts-eurosym
Summary:	The new European currency symbol for the Euro
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-eurosym

%description fonts-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%package fonts-eulervm
Summary:	The Virtual Euler Math fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-eulervm

%description fonts-eulervm
Euler-VM is a set of _virtual_ math fonts based on Euler and CM. This
approach has several advantages over immediately using the _real_
Euler fonts: Most noticeably, less TeX resources are consumed, the
quality of various math symbols is improved, and a usable \hslash
symbol can be provided.

%package fonts-euxm
Summary:	Fonts similar to EUSM but with two more characters
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-euxm

%description fonts-euxm
Fonts like EUSM but with two more characters needed for Concrete Math
included in TeXLive distribution in fonts3.

%package fonts-gothic
Summary:	Gothic and ornamental initial fonts by Yannis Haralambous
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-gothic

%description fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%package fonts-hoekwater
Summary:	Converted mflogo font
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-hoekwater

%description fonts-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%package fonts-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-jknappen
Obsoletes:	tetex-fonts-jknappen
Obsoletes:	tetex-latex-jknappen
Obsoletes:	texlive-latex-jknappen

%description fonts-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%package fonts-kpfonts
Summary:	A complete set of fonts for text and mathematics
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-kpfonts
A complete set of fonts for text and mathematics.

%package fonts-latex
Summary:	Basic LaTeX fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-latex
Obsoletes:	tetex-fonts-latex

%description fonts-latex
Basic LaTeX fonts.

%package fonts-lh
Summary:	Olga Lapko's LH fonts
Summary(pl.UTF-8):	Fonty LH Olgi Lapko
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-lh

%description fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%package fonts-lm
Summary:	Latin Modern family fonts
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-lm

%description fonts-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%package fonts-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-marvosym

%description fonts-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%package fonts-mflogo
Summary:	Logo fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-mflogo

%description fonts-mflogo
Logo fonts.

%package fonts-misc
Summary:	Miscellaneous fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-misc

%description fonts-misc
Miscellaneous fonts.

%package fonts-monotype
Summary:	Monotype fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-monotype

%description fonts-monotype
Monotype fonts.

%package fonts-omega
Summary:	Fonts for Omega - extended unicode TeX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-omega

%description fonts-omega
Fonts for Omega - extended unicode TeX.

%package fonts-other
Summary:	Other fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-cbgreek
Obsoletes:	tetex-fonts-dstroke
Obsoletes:	tetex-fonts-pazo
Obsoletes:	tetex-fonts-type1-dstroke
Obsoletes:	tetex-fonts-type1-qfonts
Obsoletes:	tetex-fonts-type1-tt2001
Obsoletes:	tetex-qfonts

%description fonts-other
Other fonts.

%package fonts-pl
Summary:	Polish fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-pl

%description fonts-pl
Polish fonts.

%package fonts-px
Summary:	PX fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-px

%description fonts-px
PX fonts.

%package fonts-qpxqtx
Summary:	Additional fonts for QTX package
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
# Requires:	%{name}-fonts-qfonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-tx = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-qpx
Obsoletes:	tetex-fonts-qtx

%description fonts-qpxqtx
Additional fonts for QTX package.

%package fonts-rsfs
Summary:	Fonts of uppercase script letters for scientific and mathematical typesetting
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-rsfs

%description fonts-rsfs
Fonts of uppercase script letters for use as symbols in scientific and
mathematical typesetting, in contrast to the informal script fonts
such as that used for the `calligraphic' symbols in the TeX math
symbol font.

%package fonts-stmaryrd
Summary:	St Mary Road symbols for functional programming
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-stmaryrd
Obsoletes:	tetex-fonts-stmaryrd

%description fonts-stmaryrd
St Mary Road symbols for functional programming.

%package fonts-tx
Summary:	TX fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-tx

%description fonts-tx
TX fonts.

%package fonts-uhc
Summary:	UHC fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-uhc
UHC fonts.

%package fonts-urw
Summary:	URW fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-urw

%description fonts-urw
URW fonts.

%package fonts-urwvn
Summary:	URWVN fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-urwvn

%description fonts-urwvn
URWVN fonts.

%package fonts-vnr
Summary:	VNR fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-vnr

%description fonts-vnr
VNR fonts.

%package fonts-urw35vf
Summary:	urw35vf fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-urw35vf
urw35vf fonts.

%package fonts-wadalab
Summary:	Wadalab fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-wadalab
Wadalab fonts.

%package fonts-wasy
Summary:	Waldis symbol fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-wasy
Obsoletes:	tetex-fonts-wasy

%description fonts-wasy
Waldis symbol fonts.

%package fonts-xypic
Summary:	Xy-pic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-xypic

%description fonts-xypic
Xy-pic fonts.

%package fonts-yandy
Summary:	European Modern fonts from Y&Y
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-yandy

%description fonts-yandy
European Modern fonts from Y&Y.

%package fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-antp

%description fonts-type1-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%package fonts-type1-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-antt

%description fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-type1-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-type1-arphic
Summary:	Type1 Arphic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-arphic
Type1 Arphic fonts.

%package fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-belleek

%description fonts-type1-belleek
Free replacement for basic MathTime fonts.

%package fonts-type1-bitstream
Summary:	Bitstream fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-bitstrea

%description fonts-type1-bitstream
Bitstream fonts.

%package fonts-type1-bluesky
Summary:	Computer Modern family fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-type1-bluesky
Obsoletes:	tetex-fonts-type1-bluesky

%description fonts-type1-bluesky
Computer Modern family fonts.

%package fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-cc-pl

%description fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%package fonts-type1-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-cmcyr

%description fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%package fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-cs

%description fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%package fonts-type1-eurosym
Summary:	The new European currency symbol for the Euro
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-eurosym

%description fonts-type1-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%package fonts-type1-hoekwater
Summary:	Converted mflogo font
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-hoekwater

%description fonts-type1-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%package fonts-type1-fpl
Summary:	SC/OsF fonts for URW Palladio L
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-fpl

%description fonts-type1-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L which
are compatible with respect to metrics with the Palatino SC/OsF fonts
from Adobe. Note that it is not the author's aim to exactly reproduce
the outlines of the original Adobe fonts. The SC and OsF in the FPL
Fonts were designed with the glyphs from URW Palladio L as starting
point. For some glyphs (eg 'o') the author got the best result by
scaling and boldening. For others (eg 'h') shifting selected portions
of the character gave more satisfying results. All this was done using
the free font editor FontForge <http://fontforge.sf.net/>. The kerning
data in these fonts comes from Walter Schmidt's improved Palatino
metrics.

%package fonts-type1-lm
Summary:	Type1 Latin Modern family fonts
Group:		Applications/Publishing/TeX
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-lm

%description fonts-type1-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%package fonts-type1-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-marvosym

%description fonts-type1-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%package fonts-type1-mathpazo
Summary:	Pazo Math fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-mathpazo

%description fonts-type1-mathpazo
Pazo Math fonts.

%package fonts-type1-omega
Summary:	Type1 fonts for Omega - extended unicode TeX
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-omega

%description fonts-type1-omega
Type1 fonts for Omega - extended unicode TeX.

%package fonts-type1-pl
Summary:	Polish fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Requires:	%{name}-fonts-type1-bluesky = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-pl

%description fonts-type1-pl
Polish fonts.

%package fonts-type1-px
Summary:	PX fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-px

%description fonts-type1-px
PX fonts.

%package fonts-type1-tx
Summary:	TX fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-tx

%description fonts-type1-tx
TX fonts.

%package fonts-type1-uhc
Summary:	Type1 UHC fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-uhc
Type1 UHC fonts.

%package fonts-type1-urw
Summary:	URW fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Provides:	tetex-fonts-type1-urw
Obsoletes:	tetex-fonts-type1-urw

%description fonts-type1-urw
URW fonts.

%package fonts-type1-vnr
Summary:	Type1 VNR fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-vnr

%description fonts-type1-vnr
Type1 VNR fonts.

%package fonts-type1-wadalab
Summary:	Type1 Wadalab fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}

%description fonts-type1-wadalab
Type1 Wadalab fonts.

%package fonts-type1-xypic
Summary:	Xy-pic fonts
Group:		Fonts
Requires:	%{name}-dirs-fonts = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-fonts-type1-xypic

%description fonts-type1-xypic
Xy-pic fonts.

# TeXLive-specific packages

%package afm2pl
Summary:	Convert an Adobe font metric file to a TeX font property list
Group:		Fonts

%description afm2pl
Convert an Adobe font metric file to a TeX font property list.

%package bbox
Summary:	bbox prints the bounding box of images
Group:		Applications/Publishing/TeX

%description bbox
bbox reads a rawppm or rawpbm file and prints out the bounding box of
the image.

%package cefutils
Summary:	In cefutils there are CEF-compatible utils
Group:		Applications/Publishing/TeX

%description cefutils
In cefutils there are CEF-compatible (Chinese Encoding Framework)
utils.

%package detex
Summary:	A filter to strip TeX commands from a .tex file
Group:		Applications/Publishing/TeX

%description detex
A filter to strip TeX commands from a .tex file.

%package dviutils
Summary:	Various DVI utils
Group:		Applications/Publishing/TeX
Provides:	dvi2tty
Obsoletes:	dvi2tty

%description dviutils
This package contains various DVI utils.

%package uncategorized-utils
Summary:	Uncategorized utils
Group:		Applications/Publishing/TeX

%description uncategorized-utils
Uncategorized utilities. Needs check and categorizing.

%package tex4ht
Summary:	LaTeX and TeX for hypertext
Group:		Applications/Publishing/TeX

%description tex4ht
A converter from TeX and LaTeX to hypertext (HTML, XML, etc.),
providing a configurable (La)TeX-based authoring system for hypertext.
When converting to XML, you can use MathML instead of images for
equation representation.

%package xetex
Summary:	Extended TeX / LaTeX version for unicode
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-misc = %{epoch}:%{version}-%{release}

%description xetex
XeTeX extends the TeX typesetting system (and macro packages such as
LaTeX and ConTeXt) to have native support for the Unicode character
set, including complex Asian scripts, and for OpenType and TrueType
fonts.

%package xmltex
Summary:	TeX package for processing XML files
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Provides:	passivetex = 1.26
Provides:	xmltex
Obsoletes:	passivetex
Obsoletes:	xmltex

%description xmltex
XMLTeX is a non-validating, namespace-aware XML parser written in TeX.
It allows TeX to directly process XML files.

%prep
%setup -qn %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
CURDIR=$(pwd)

cd utils/xindy/make-rules/alphabets
tar xvf %{SOURCE11}
cp $(find fonts -type f) .
for i in larm?00.tfm; do ln -s $i $(echo $i | sed "s@larm\(.\).*@larm0\100.tfm@") ; done
cd ${CURDIR}

cd libs/teckit
cat ax*.m4 > acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%build
find . -name "config.sub" -exec cp /usr/share/automake/config.sub '{}' ';'
cd texk/kpathsea
%{__sed} -i 's@^TEXMFMAIN =.*@TEXMFMAIN = %{texmf}@' texmf.cnf
%{__sed} -i 's@^TEXMFDIST =.*@TEXMFDIST = %{texmfdist}@' texmf.cnf
%{__sed} -i 's@^TEXMFLOCAL =.*@TEXMFLOCAL = %{texmf}@' texmf.cnf
%{__sed} -i 's@^TEXMFSYSVAR =.*@TEXMFSYSVAR = %{_localstatedir}@' texmf.cnf
%{__sed} -i 's@^TEXMFSYSCONFIG =.*@TEXMFSYSCONFIG = %{_sysconfdir}/%{name}@' texmf.cnf
%{__sed} -i 's@^TEXMFVAR =.*@TEXMFVAR = %{_localstatedir}@' texmf.cnf
%{__sed} -i 's@^trie_size.*@trie_size = 1262000@' texmf.cnf
cd ../..

%ifarch ppc ppc64
# clisp does not work properly on forge
ulimit -s unlimited
%endif

%configure \
	--disable-multiplatform				\
	--disable-static				\
	--enable-a4					\
	--enable-gf					\
	--enable-ipc					\
	--enable-shared					\
	--with%{!?with_xindy:out}-xindy			\
	--with-fontconfig				\
	--with-fonts-dir=/var/cache/fonts		\
	--with-freetype2-include=/usr/include/freetype2	\
	--with-ncurses					\
	--with-system-freetype2				\
	--with-system-gd				\
	--with-system-ncurses				\
	--with-system-pnglib				\
	--with-system-t1lib				\
	--with-system-zlib				\
	--with-xdvi-x-toolkit=xaw			\
	--without-dialog				\
	--without-luatex				\
	--without-t1utils				\
	--without-texinfo				\
	--without-ttf2pk
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_mandir}/man5 \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap\
	$RPM_BUILD_ROOT%{_localstatedir}/fonts/map\
	$RPM_BUILD_ROOT%{fmtdir}/pdftex

lzma -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf $RPM_BUILD_ROOT%{texmf}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-dist $RPM_BUILD_ROOT%{texmfdist}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf/texmf-doc $RPM_BUILD_ROOT%{texmfdoc}
%{__mv} $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots/* $RPM_BUILD_ROOT%{texmfdist}/doc/latex/pgfplots
rmdir $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots
# imho it is unneeded
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/fonts/{ec,fc,utopia}
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/cefconv

# This is an empty directory
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/texlive-20080822-texmf
# Useless binary
%{__rm} $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/splitindex/splitindex{.exe,-Linux-i386,-OpenBSD-i386}

# commented out because of following (non-fatal) error:
# Can't open texmf/web2c/texmf.cnf: No such file or directory.
#perl -pi \
#	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
#	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
#	texmf/web2c/texmf.cnf

install -d $RPM_BUILD_ROOT%{texmf}/fonts/opentype/public

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{texmf} \
	texmfsysvar=$RPM_BUILD_ROOT%{_localstatedir} \
	texmfsysconfig=$RPM_BUILD_ROOT%{texmf}

%{__rm} $RPM_BUILD_ROOT%{texmf}/scripts/texlive/uninstall-win32.pl
# Fix broken symlinks
CURDIR=$(pwd)
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf ../share/texmf/scripts/a2ping/a2ping.pl a2ping
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/context context
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/ctxtools ctxtools
ln -sf ../share/texmf-dist/scripts/dviasm/dviasm.py dviasm
ln -sf ../share/texmf/scripts/tetex/e2pall.pl e2pall
ln -sf ../share/texmf-dist/scripts/bengali/ebong.py ebong
ln -sf ../share/texmf-dist/scripts/epspdf/epspdf epspdf
ln -sf ../share/texmf-dist/scripts/epspdf/epspdftk epspdftk
ln -sf ../share/texmf/scripts/epstopdf/epstopdf.pl epstopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/exatools exatools
ln -sf ../share/texmf/scripts/texlive/getnonfreefonts.pl getnonfreefonts
ln -sf ../share/texmf/scripts/texlive/getnonfreefonts.pl getnonfreefonts-sys
ln -sf ../share/texmf-dist/scripts/tex4ht/ht.sh ht
ln -sf ../share/texmf-dist/scripts/tex4ht/htcontext.sh htcontext
ln -sf ../share/texmf-dist/scripts/tex4ht/htlatex.sh htlatex
ln -sf ../share/texmf-dist/scripts/tex4ht/htmex.sh htmex
ln -sf ../share/texmf-dist/scripts/tex4ht/httex.sh httex
ln -sf ../share/texmf-dist/scripts/tex4ht/httexi.sh httexi
ln -sf ../share/texmf-dist/scripts/tex4ht/htxelatex.sh htxelatex
ln -sf ../share/texmf-dist/scripts/tex4ht/htxetex.sh htxetex
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/luatools luatools
ln -sf ../share/texmf-dist/scripts/glossaries/makeglossaries makeglossaries
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/makempy makempy
ln -sf ../share/texmf-dist/scripts/tex4ht/mk4ht.pl mk4ht
ln -sf ../share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mpstools mpstools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mptopdf mptopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mtxrun mtxrun
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/mtxtools mtxtools
ln -sf ../share/texmf-dist/scripts/oberdiek/pdfatfi.pl pdfatfi
ln -sf ../share/texmf-dist/scripts/pdfcrop/pdfcrop.pl pdfcrop
ln -sf ../share/texmf-dist/scripts/ppower4/pdfthumb.texlua pdfthumb
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftools pdftools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pdftrimwhite pdftrimwhite
ln -sf ../share/texmf-dist/scripts/perltex/perltex.pl perltex
ln -sf ../share/texmf/scripts/pkfix/pkfix.pl pkfix
ln -sf ../share/texmf-dist/scripts/ppower4/ppower4.texlua ppower4
ln -sf ../share/texmf/scripts/ps2eps/ps2eps.pl ps2eps
ln -sf ../share/texmf-dist/scripts/pst-pdf/ps4pdf ps4pdf
ln -sf ../share/texmf-dist/scripts/pst2pdf/pst2pdf.pl pst2pdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/pstopdf pstopdf
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/rlxtools rlxtools
ln -sf ../share/texmf/scripts/texlive/rungs.tlu rungs
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/runtools runtools
ln -sf ../share/texmf/scripts/simpdftex/simpdftex simpdftex
ln -sf ../share/texmf-dist/scripts/texcount/TeXcount.pl texcount
ln -sf ../share/texmf/scripts/texlive/texdoc.tlu texdoc
ln -sf ../share/texmf/scripts/tetex/texdoctk.pl texdoctk
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texexec texexec
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfind texfind
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texfont texfont
ln -sf ../share/texmf-dist/scripts/context/ruby/texmfstart.rb texmfstart
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texshow texshow
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/textools textools
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/texutil texutil
ln -sf ../share/texmf-dist/scripts/thumbpdf/thumbpdf.pl thumbpdf
ln -sf ../share/texmf/scripts/texlive/tlmgr.pl tlmgr
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/tmftools tmftools
ln -sf ../share/texmf-dist/scripts/vpe/vpe.pl vpe
ln -sf ../share/texmf-dist/scripts/context/stubs/unix/xmltools xmltools

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE50} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE51} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE52} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE53} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE54} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE55} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE56} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE57} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE58} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE59} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE60} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE61} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE62} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive


cd $RPM_BUILD_ROOT%{texmfdist}/tex/latex

# floatflt
unzip %{SOURCE10}
cd floatflt
latex floatflt.ins
%{__rm} *.log
install -d $RPM_BUILD_ROOT%{texmfdist}/doc/latex/floatflt
%{__mv} *.txt *.tex *.pdf README $RPM_BUILD_ROOT%{texmfdist}/doc/latex/floatflt
cd ..

# foiltex
unzip %{SOURCE12}
cd foiltex
latex foiltex.ins
%{__rm} *.log
install -d $RPM_BUILD_ROOT%{texmfdist}/doc/latex/foiltex
%{__mv} *.tex *.pdf README $RPM_BUILD_ROOT%{texmfdist}/doc/latex/foiltex
cd ..

# larm fonts
cd $RPM_BUILD_ROOT%{texmfdist}
tar xvf %{SOURCE11}
cd fonts/tfm/la
for i in larm?00.tfm; do ln -s $i $(echo $i | sed "s@larm\(.\).*@larm0\100.tfm@") ; done

# wrong dvi in formlett, should be regenerate
cd $RPM_BUILD_ROOT%{texmfdist}/doc/latex/formlett
cp $RPM_BUILD_ROOT%{texmfdist}/tex/latex/formlett/formlett.sty .
tex user_manual.tex
yes | tex prog_manual.tex
tex example1.tex
tex example2.tex
rm formlett.sty

cd $CURDIR

# some tex-files need xstring.tex and doc/latex isn't in kpathsea search path
cp $RPM_BUILD_ROOT%{texmfdist}/doc/latex/xstring/xstring.tex $RPM_BUILD_ROOT%{texmfdist}/tex/latex/xstring

#install %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}
#touch $RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap/maps.lst

# %{__make} init \
# 	prefix=$RPM_BUILD_ROOT%{_prefix} \
# 	bindir=$RPM_BUILD_ROOT%{_bindir} \
# 	mandir=$RPM_BUILD_ROOT%{_mandir} \
# 	libdir=$RPM_BUILD_ROOT%{_libdir} \
# 	datadir=$RPM_BUILD_ROOT%{_datadir} \
# 	infodir=$RPM_BUILD_ROOT%{_infodir} \
# 	includedir=$RPM_BUILD_ROOT%{_includedir} \
# 	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
# 	texmf=$RPM_BUILD_ROOT%{texmf}

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/texmf
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/texmf-dist
# We don't need it
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/man
%{__rm} -r $RPM_BUILD_ROOT%{texmfdoc}/source

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

# not included in package
rm -f $RPM_BUILD_ROOT%{_datadir}/texinfo/html/texi2html.html
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
rm -f $RPM_BUILD_ROOT%{_infodir}/dvipng*
rm -f $RPM_BUILD_ROOT%{_mandir}/{README.*,hu/man1/readlink.1*}
rm -f $RPM_BUILD_ROOT%{texmf}/doc/Makefile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/fonts/oldgerman/COPYING
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/Catalogue-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/faq/uktug-faq-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpfile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpindex.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.php
rm -f $RPM_BUILD_ROOT%{texmf}/doc/mkhtml*
rm -f $RPM_BUILD_ROOT%{texmf}/doc/programs/texinfo.*
rm -f $RPM_BUILD_ROOT%{texmf}/fonts/pk/ljfour/lh/lh-lcy/*.600pk
rm -f $RPM_BUILD_ROOT%{texmf}/generic/config/pdftex-dvi.tex
rm -f $RPM_BUILD_ROOT%{texmf}/release-tetex-{src,texmf}.txt
rm -f $RPM_BUILD_ROOT%{texmf}/scripts/uniqleaf/uniqleaf.pl
rm -f $RPM_BUILD_ROOT%{texmf}/tex/generic/pdftex/glyphtounicode.tex
rm -rf $RPM_BUILD_ROOT%{_datadir}/lcdf-typetools
rm -rf $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pdf-trans
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/generic/hyph-utf8
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/generic/patch
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/plain/plgraph
rm -rf $RPM_BUILD_ROOT%{texmfdist}/tex/generic/pdf-trans
rm -rf $RPM_BUILD_ROOT%{texmfdist}/tex/generic/xecyr
rm -rf $RPM_BUILD_ROOT%{texmf}/cef5conv
rm -rf $RPM_BUILD_ROOT%{texmf}/cefsconv
rm -rf $RPM_BUILD_ROOT%{texmf}/chktex
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/cef5conv
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/cefsconv
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/chktex
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/gzip

# move format logs to BUILD, so $RPM_BUILD_ROOT is not polluted
# and we can still analyze them
# install -d format-logs
# mv -fv $RPM_BUILD_ROOT%{fmtdir}/*.log format-logs

# xindy files are in %%{texmf}
rm -rf $RPM_BUILD_ROOT%{_datadir}/xindy
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# Create format files
for format in \
	aleph \
	csplain \
	etex \
	lambda \
	lamed \
	latex \
	mex \
	mllatex \
	mptopdf \
	omega \
	pdfcsplain \
	pdfetex \
	pdflatex \
	pdftex \
	pdfxmltex \
	physe \
	phyzzx \
	tex \
	texsis \
	xetex \
	xelatex \
	xmltex; do
%if %{with bootstrap}
	install -d $RPM_BUILD_ROOT%{fmtdir}/${format}
	touch $RPM_BUILD_ROOT%{fmtdir}/${format}/${format}.fmt
	touch $RPM_BUILD_ROOT%{fmtdir}/pdftex/${format}.fmt
%else
	fmtutil --fmtdir $RPM_BUILD_ROOT%{fmtdir} --byfmt=${format}
%endif
done
%if %{with bootstrap}
touch $RPM_BUILD_ROOT%{fmtdir}/xetex/xelatex.fmt
%endif
# We don't need the log files
rm -f $(find $RPM_BUILD_ROOT%{fmtdir} -name "*.log")

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fixinfodir
%texhash

%postun
%fixinfodir
if [ "$1" = "1" ]; then
	%texhash
fi

%post other-utils
%texhash

%postun other-utils
%texhash

%post jadetex
%texhash

%postun jadetex
%texhash

%post -n kpathsea
/sbin/ldconfig
%texhash

%postun -n kpathsea
/sbin/ldconfig
%texhash

%post -n kpathsea-devel
%fixinfodir
%texhash

%postun -n kpathsea-devel
%fixinfodir
%texhash

%post dvips
%fixinfodir
%texhash

%postun dvips
%fixinfodir
%texhash

%post dvilj
%texhash

%postun dvilj
%texhash

%post makeindex
%texhash

%postun makeindex
%texhash

%post scripts
%texhash

%postun scripts
%texhash

%post tex-arrayjob
%texhash

%postun tex-arrayjob
%texhash

%post tex-kastrup
%texhash

%postun tex-kastrup
%texhash

%post tex-insbox
%texhash

%postun tex-insbox
%texhash

%post tex-mathdots
%texhash

%postun tex-mathdots
%texhash

%post tex-midnight
%texhash

%postun tex-midnight
%texhash

%post tex-ofs
%texhash

%postun tex-ofs
%texhash

%post tex-physe
%texhash

%postun tex-physe
%texhash

%post tex-velthuis
%texhash

%postun tex-velthuis
%texhash

%post tex-ytex
%texhash

%postun tex-ytex
%texhash

%post metapost
%texhash

%postun metapost
%texhash

%post metapost-other
%texhash

%postun metapost-other
%texhash

%post mptopdf
%texhash

%postun mptopdf
%texhash

%post texdoctk
%texhash

%postun texdoctk
%texhash

%post -n xdvi
%texhash

%postun -n xdvi
%texhash

%post pdftex
%texhash

%postun pdftex
%texhash

%post phyzzx
%texhash

%postun phyzzx
%texhash

%post omega
%texhash

%postun omega
%texhash

%post plain
%texhash

%postun plain
%texhash

%post mex
%texhash

%postun mex
%texhash

%post format-mex
%texhash

%postun format-mex
%texhash

%post format-pdfmex
%texhash

%postun format-pdfmex
%texhash

%postun format-utf8mex
%texhash

%post amstex
%texhash

%postun amstex
%texhash

%post format-amstex
%texhash

%postun format-amstex
%texhash

%post csplain
%texhash

%postun csplain
%texhash

%post format-csplain
%texhash

%postun format-csplain
%texhash

%post format-pdfcsplain
%texhash

%postun format-pdfcsplain
%texhash

%post cslatex
%texhash

%postun cslatex
%texhash

%post format-cslatex
%texhash

%postun format-cslatex
%texhash

%post format-pdfcslatex
%texhash

%postun format-pdfcslatex
%texhash

%post eplain
%texhash

%postun eplain
%texhash

%post format-eplain
%texhash

%postun format-eplain
%texhash

# ConTeXt format

%post context
%texhash

%postun context
%texhash

%post format-context-de
%texhash

%postun format-context-de
%texhash

%post format-context-en
%texhash

%postun format-context-en
%texhash

%post format-context-nl
%texhash

%postun format-context-nl
%texhash

%post latex
%fixinfodir
%texhash

%postun latex
%fixinfodir
%texhash

%post latex-lang
%texhash

%postun latex-lang
%texhash

%post latex-styles
%texhash

%postun latex-styles
%texhash

%post latex-pdftools
%texhash

%postun latex-pdftools
%texhash

%post latex-extend
%texhash

%postun latex-extend
%texhash

%post latex-presentation
%texhash

%postun latex-presentation
%texhash

%post latex-programming
%texhash

%postun latex-programming
%texhash

%post latex-metre
%texhash

%postun latex-metre
%texhash

%post latex-misc
%texhash

%postun latex-misc
%texhash

%post latex-effects
%texhash

%postun latex-effects
%texhash

%post latex-math
%texhash

%postun latex-math
%texhash

%post latex-music
%texhash

%postun latex-music
%texhash

%post latex-physics
%texhash

%postun latex-physics
%texhash

%post latex-games
%texhash

%postun latex-games
%texhash

%post latex-biology
%texhash

%postun latex-biology
%texhash

%post latex-chem
%texhash

%postun latex-chem
%texhash

%post latex-informatic
%texhash

%postun latex-informatic
%texhash

%post latex-12many
%texhash

%postun latex-12many
%texhash

%post latex-abstract
%texhash

%postun latex-abstract
%texhash

%post latex-accfonts
%texhash

%postun latex-accfonts
%texhash

%post latex-adrconv
%texhash

%postun latex-adrconv
%texhash

%post latex-ae
%texhash

%postun latex-ae
%texhash

%post latex-ams
%texhash

%postun latex-ams
%texhash

%post latex-antp
%texhash

%postun latex-antp
%texhash

%post latex-antt
%texhash

%postun latex-antt
%texhash

%post latex-appendix
%texhash

%postun latex-appendix
%texhash

%post latex-bardiag
%texhash

%postun latex-bardiag
%texhash

%post latex-bbm
%texhash

%postun latex-bbm
%texhash

%post latex-bbold
%texhash

%postun latex-bbold
%texhash

%post latex-beamer
%texhash

%postun latex-beamer
%texhash

%post latex-bezos
%texhash

%postun latex-bezos
%texhash

%post latex-bibtex
%texhash

%postun latex-bibtex
%texhash

%post latex-bibtex-ams
%texhash

%postun latex-bibtex-ams
%texhash

%post latex-bibtex-pl
%texhash

%postun latex-bibtex-pl
%texhash

%post latex-bibtex-german
%texhash

%postun latex-bibtex-german
%texhash

%post latex-bibtex-revtex4
%texhash

%postun latex-bibtex-revtex4
%texhash

%post latex-bibtex-jurabib
%texhash

%postun latex-bibtex-jurabib
%texhash

%post latex-bibtex-styles
%texhash

%postun latex-bibtex-styles
%texhash

%post latex-booktabs
%texhash

%postun latex-booktabs
%texhash

%post latex-caption
%texhash

%postun latex-caption
%texhash

%post latex-carlisle
%texhash

%postun latex-carlisle
%texhash

%post latex-ccfonts
%texhash

%postun latex-ccfonts
%texhash

%post latex-cite
%texhash

%postun latex-cite
%texhash

%post latex-cmbright
%texhash

%postun latex-cmbright
%texhash

%post latex-colortab
%texhash

%postun latex-colortab
%texhash

%post latex-comment
%texhash

%postun latex-comment
%texhash

%post latex-concmath
%texhash

%postun latex-concmath
%texhash

%post latex-currvita
%texhash

%postun latex-currvita
%texhash

%post latex-curves
%texhash

%postun latex-curves
%texhash

%post latex-custom-bib
%texhash

%postun latex-custom-bib
%texhash

%post latex-cyrillic
%texhash

%postun latex-cyrillic
%texhash

%post latex-enumitem
%texhash

%postun latex-enumitem
%texhash

%post latex-exams
%texhash

%postun latex-exams
%texhash

%post latex-float
%texhash

%postun latex-float
%texhash

%post latex-foiltex
%texhash

%postun latex-foiltex
%texhash

%post latex-formlett
%texhash

%postun latex-formlett
%texhash

%post latex-formular
%texhash

%postun latex-formular
%texhash

%post latex-gbrief
%texhash

%postun latex-gbrief
%texhash

%post latex-keystroke
%texhash

%postun latex-keystroke
%texhash

%post latex-labbook
%texhash

%postun latex-labbook
%texhash

%post latex-lcd
%texhash

%postun latex-lcd
%texhash

%post latex-leaflet
%texhash

%postun latex-leaflet
%texhash

%post latex-leftidx
%texhash

%postun latex-leftidx
%texhash

%post latex-lewis
%texhash

%postun latex-lewis
%texhash

%post latex-lm
%texhash

%post latex-lastpage
%texhash

%postun latex-lastpage
%texhash

%postun latex-lm
%texhash

%post latex-lucidabr
%texhash

%postun latex-lucidabr
%texhash

%post latex-marvosym
%texhash

%postun latex-marvosym
%texhash

%post latex-mflogo
%texhash

%postun latex-mflogo
%texhash

%post latex-mfnfss
%texhash

%postun latex-mfnfss
%texhash

%post latex-minitoc
%texhash

%postun latex-minitoc
%texhash

%post latex-mltex
%texhash

%postun latex-mltex
%texhash

%post latex-moreverb
%texhash

%postun latex-moreverb
%texhash

%post latex-multienum
%texhash

%postun latex-multienum
%texhash

%post latex-musictex
%texhash

%postun latex-musictex
%texhash

%post latex-ntheorem
%texhash

%postun latex-ntheorem
%texhash

%post latex-other
%texhash

%postun latex-other
%texhash

%post latex-other-doc
%texhash

%postun latex-other-doc
%texhash

%post latex-pdfslide
%texhash

%postun latex-pdfslide
%texhash

%post latex-pgf
%texhash

%postun latex-pgf
%texhash

%post latex-polynom
%texhash

%postun latex-polynom
%texhash

%post latex-polynomial
%texhash

%postun latex-polynomial
%texhash

%post latex-prosper
%texhash

%postun latex-prosper
%texhash

%post latex-pseudocode
%texhash

%postun latex-pseudocode
%texhash

%post latex-psnfss
%texhash

%postun latex-psnfss
%texhash

%post latex-pst-2dplot
%texhash

%postun latex-pst-2dplot
%texhash

%post latex-pst-3dplot
%texhash

%postun latex-pst-3dplot
%texhash

%post latex-pst-bar
%texhash

%postun latex-pst-bar
%texhash

%post latex-pst-circ
%texhash

%postun latex-pst-circ
%texhash

%post latex-pst-eucl
%texhash

%postun latex-pst-eucl
%texhash

%post latex-pst-diffraction
%texhash

%postun latex-pst-diffraction
%texhash

%post latex-pst-fun
%texhash

%postun latex-pst-fun
%texhash

%post latex-pst-func
%texhash

%postun latex-pst-func
%texhash

%post latex-pst-infixplot
%texhash

%postun latex-pst-infixplot
%texhash

%post latex-pst-fr3d
%texhash

%postun latex-pst-fr3d
%texhash

%post latex-pst-fractal
%texhash

%postun latex-pst-fractal
%texhash

%post latex-pxfonts
%texhash

%post latex-pst-math
%texhash

%postun latex-pst-math
%texhash

%post latex-pst-ob3d
%texhash

%postun latex-pst-ob3d
%texhash

%post latex-pst-optic
%texhash

%postun latex-pst-optic
%texhash

%post latex-pst-optexp
%texhash

%postun latex-pst-optexp
%texhash

%post latex-pst-text
%texhash

%postun latex-pst-text
%texhash

%post latex-pst-uncategorized
%texhash

%postun latex-pst-uncategorized
%texhash

%postun latex-pxfonts
%texhash

%post latex-SIstyle
%texhash

%postun latex-SIstyle
%texhash

%post latex-SIunits
%texhash

%postun latex-SIunits
%texhash

%post latex-siunitx
%texhash

%postun latex-siunitx
%texhash

%post latex-Tabbing
%texhash

%postun latex-Tabbing
%texhash

%post latex-txfonts
%texhash

%postun latex-txfonts
%texhash

%post latex-ucs
%texhash

%postun latex-ucs
%texhash

%post latex-umlaute
%texhash

%postun latex-umlaute
%texhash

%post latex-variations
%texhash

%postun latex-variations
%texhash

%post latex-wasysym
%texhash

%postun latex-wasysym
%texhash

%post latex-xcolor
%texhash

%postun latex-xcolor
%texhash

%post format-pdflatex
%texhash

%postun format-pdflatex
%texhash

%post tex-babel
%texhash

%postun tex-babel
%texhash

%post tex-german
%texhash

%postun tex-german
%texhash

%post tex-mfpic
%texhash

%postun tex-mfpic
%texhash

%post tex-misc
%texhash

%postun tex-misc
%texhash

%post tex-pictex
%texhash

%postun tex-pictex
%texhash

%post tex-psizzl
%texhash

%postun tex-psizzl
%texhash

%post tex-pstricks
%texhash

%postun tex-pstricks
%texhash

%post tex-qpxqtx
%texhash

%postun tex-qpxqtx
%texhash

%post tex-huhyphen
%texhash

%postun tex-huhyphen
%texhash

%post tex-ruhyphen
%texhash

%postun tex-ruhyphen
%texhash

%post tex-spanish
%texhash

%postun tex-spanish
%texhash

%post tex-texdraw
%texhash

%postun tex-texdraw
%texhash

%post tex-thumbpdf
%texhash

%postun tex-thumbpdf
%texhash

%post tex-ukrhyph
%texhash

%postun tex-ukrhyph
%texhash

%post latex-vietnam
%texhash

%postun latex-vietnam
%texhash

%post tex-xypic
%texhash

%postun tex-xypic
%texhash

%post fonts-adobe
%texhash

%postun fonts-adobe
%texhash

%post fonts-larm
%texhash

%postun fonts-larm
%texhash

%post fonts-ae
%texhash

%postun fonts-ae
%texhash

%post fonts-ams
%texhash

%postun fonts-ams
%texhash

%post fonts-antp
%texhash

%postun fonts-antp
%texhash

%post fonts-antt
%texhash

%postun fonts-antt
%texhash

%post fonts-bbm
%texhash

%postun fonts-bbm
%texhash

%post fonts-bbold
%texhash

%postun fonts-bbold
%texhash

%post fonts-bitstream
%texhash

%postun fonts-bitstream
%texhash

%post fonts-cc-pl
%texhash

%postun fonts-cc-pl
%texhash

%post fonts-cg
%texhash

%postun fonts-cg
%texhash

%post fonts-cm
%texhash

%postun fonts-cm
%texhash

%post fonts-cmbright
%texhash

%postun fonts-cmbright
%texhash

%post fonts-cmcyr
%texhash

%postun fonts-cmcyr
%texhash

%post fonts-cmextra
%texhash

%postun fonts-cmextra
%texhash

%post fonts-cmsuper
%texhash

%postun fonts-cmsuper
%texhash

%post fonts-concmath
%texhash

%postun fonts-concmath
%texhash

%post fonts-concrete
%texhash

%postun fonts-concrete
%texhash

%post fonts-cs
%texhash

%postun fonts-cs
%texhash

%post fonts-ecc
%texhash

%postun fonts-ecc
%texhash

%post fonts-eurosym
%texhash

%postun fonts-eurosym
%texhash

%post fonts-euxm
%texhash

%postun fonts-euxm
%texhash

%post fonts-gothic
%texhash

%postun fonts-gothic
%texhash

%post fonts-hoekwater
%texhash

%postun fonts-hoekwater
%texhash

%post fonts-jknappen
%texhash

%postun fonts-jknappen
%texhash

%post fonts-latex
%texhash

%postun fonts-latex
%texhash

%post fonts-kpfonts
%texhash

%postun fonts-kpfonts
%texhash

%post fonts-lh
%texhash

%postun fonts-lh
%texhash

%post fonts-lm
%texhash

%postun fonts-lm
%texhash

%post fonts-marvosym
%texhash

%postun fonts-marvosym
%texhash

%post fonts-mflogo
%texhash

%postun fonts-mflogo
%texhash

%post fonts-misc
%texhash

%postun fonts-misc
%texhash

%post fonts-monotype
%texhash

%postun fonts-monotype
%texhash

%post fonts-omega
%texhash

%postun fonts-omega
%texhash

%post fonts-other
%texhash

%postun fonts-other
%texhash

%post fonts-pl
%texhash

%postun fonts-pl
%texhash

%post fonts-px
%texhash

%postun fonts-px
%texhash

%post fonts-qpxqtx
%texhash

%postun fonts-qpxqtx
%texhash

%post fonts-rsfs
%texhash

%postun fonts-rsfs
%texhash

%post fonts-stmaryrd
%texhash

%postun fonts-stmaryrd
%texhash

%post fonts-tx
%texhash

%postun fonts-tx
%texhash

%post fonts-urw
%texhash

%postun fonts-urw
%texhash

%post fonts-urw35vf
%texhash

%postun fonts-urw35vf
%texhash

%post fonts-vnr
%texhash

%postun fonts-vnr
%texhash

%post fonts-wasy
%texhash

%postun fonts-wasy
%texhash

%post fonts-xypic
%texhash

%postun fonts-xypic
%texhash

%post fonts-yandy
%texhash

%postun fonts-yandy
%texhash

%post fonts-type1-antp
%texhash

%postun fonts-type1-antp
%texhash

%post fonts-type1-antt
%texhash

%postun fonts-type1-antt
%texhash

%post fonts-type1-belleek
%texhash

%postun fonts-type1-belleek
%texhash

%post fonts-type1-bitstream
%texhash

%postun fonts-type1-bitstream
%texhash

%post fonts-type1-bluesky
%texhash

%postun fonts-type1-bluesky
%texhash

%post fonts-type1-cc-pl
%texhash

%postun fonts-type1-cc-pl
%texhash

%post fonts-type1-cmcyr
%texhash

%postun fonts-type1-cmcyr
%texhash

%post fonts-type1-cs
%texhash

%postun fonts-type1-cs
%texhash

%post fonts-type1-eurosym
%texhash

%postun fonts-type1-eurosym
%texhash

%post fonts-type1-hoekwater
%texhash

%postun fonts-type1-hoekwater
%texhash

%post fonts-type1-lm
%texhash

%postun fonts-type1-lm
%texhash

%post fonts-type1-marvosym
%texhash

%postun fonts-type1-marvosym
%texhash

%post fonts-type1-mathpazo
%texhash

%postun fonts-type1-mathpazo
%texhash

%post fonts-type1-omega
%texhash

%postun fonts-type1-omega
%texhash

%post fonts-type1-pl
%texhash

%postun fonts-type1-pl
%texhash

%post fonts-type1-px
%texhash

%postun fonts-type1-px
%texhash

%post fonts-type1-tx
%texhash

%postun fonts-type1-tx
%texhash

%post fonts-type1-urw
%texhash

%postun fonts-type1-urw
%texhash

%post fonts-type1-vnr
%texhash

%postun fonts-type1-vnr
%texhash

%post fonts-type1-xypic
%texhash

%postun fonts-type1-xypic
%texhash

%post -n texconfig
%texhash

%postun -n texconfig
%texhash

%post xetex
%texhash

%postun xetex
%texhash

%post xmltex
%texhash

%postun xmltex
%texhash

%files
%defattr(644,root,root,755)
# There isn't doc/fonts directory
%dir %{texmfdist}/doc/fonts
%doc %{texmfdist}/doc/fontname

%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/cweave
%attr(755,root,root) %{_bindir}/ctangle
%attr(755,root,root) %{_bindir}/ctie
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/dvipng
%attr(755,root,root) %{_bindir}/ebb
%attr(755,root,root) %{_bindir}/fmtutil
%attr(755,root,root) %{_bindir}/fmtutil-sys
%attr(755,root,root) %{_bindir}/fontinst
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/gsftopk
%attr(755,root,root) %{_bindir}/kpseaccess
%attr(755,root,root) %{_bindir}/kpsereadlink
%attr(755,root,root) %{_bindir}/kpsewhere
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/makempx
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%attr(755,root,root) %{_bindir}/mktexfmt
%attr(755,root,root) %{_bindir}/mktexlsr
%attr(755,root,root) %{_bindir}/newer
%attr(755,root,root) %{_bindir}/patgen
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pfb2pfa
%attr(755,root,root) %{_bindir}/pk2bm
%attr(755,root,root) %{_bindir}/pktogf
%attr(755,root,root) %{_bindir}/pktype
%attr(755,root,root) %{_bindir}/pltotf
%attr(755,root,root) %{_bindir}/pooltype
%attr(755,root,root) %{_bindir}/ps2frag
%attr(755,root,root) %{_bindir}/ps2pk
# move this file to correct subpackage ?
%attr(755,root,root) %{_bindir}/ps4pdf
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/ttf2afm
%attr(755,root,root) %{_bindir}/updmap
%attr(755,root,root) %{_bindir}/updmap-sys
%attr(755,root,root) %{_bindir}/vftovp
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave

%attr(755,root,root) %{texmf}/web2c/mktexnam
%attr(755,root,root) %{texmf}/web2c/mktexdir
%attr(755,root,root) %{texmf}/web2c/mktexupd

%ghost %{texmf}/ls-R
%ghost %{texmfdist}/ls-R

%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/cslatex/base/fonttext.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.def
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.us
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.us.def
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/fontmath.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/fonttext.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmfdist}/tex/latex/base/preload.cfg

%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexnam.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/texmf.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap-hdr.cfg

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*

# Directories
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map
%attr(1777,root,root) %dir %{fmtdir}

%dir %{fmtdir}/tex
%dir %{texmfdist}
%dir %{texmfdist}/doc
%dir %{texmfdist}/doc/generic
%dir %{texmfdist}/doc/generic/enctex
%dir %{texmfdist}/doc/latex
%dir %{texmfdist}/doc/latex/localloc
%dir %{texmfdist}/mft
%dir %{texmfdist}/tex
%dir %{texmfdist}/tex/cslatex
%dir %{texmfdist}/tex/cslatex/base
%dir %{texmfdist}/tex/generic
%dir %{texmfdist}/tex/generic/dehyph-exptl
%dir %{texmfdist}/tex/generic/enctex
%dir %{texmfdist}/tex/generic/hyph-utf8
%dir %{texmfdist}/tex/generic/misc
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/latex/base
%dir %{texmfdist}/scripts
%dir %{texmfdist}/source
%dir %{texmfdist}/source/latex
%dir %{texmfdist}/source/generic
%dir %{texmf}
%dir %{texmf}/doc
%dir %{texmf}/doc/generic
%dir %{texmf}/doc/tetex
%dir %{texmf}/dvips
%dir %{texmf}/dvips/config
%dir %{texmf}/dvips/tetex
%dir %{texmf}/fmtutil
%dir %{texmf}/fonts/enc
%dir %{texmf}/fonts/enc/dvips
%dir %{texmf}/fonts/enc/dvips/tetex
%dir %{texmf}/fonts/map
%dir %{texmf}/fonts/map/dvips
%dir %{texmf}/fonts/map/dvips/tetex
%dir %{texmf}/fonts/map/dvips/updmap
%dir %{texmf}/scripts
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%dir %{texmf}/web2c

# Docs
%doc %{texmfdist}/README
%doc %{texmfdist}/doc/generic/epsf
%doc %{texmfdist}/doc/generic/hyph-utf8
%doc %{texmfdist}/doc/generic/tex-ps
%doc %{texmfdist}/source/fontinst
%doc %{texmf}/README
%doc %{texmf}/doc/dvipng
%doc %{texmf}/doc/tetex/TETEXDOC.*
%doc %{texmf}/doc/tetex/teTeX-FAQ
%doc %{texmf}/doc/texinfo
%doc %{texmf}/doc/web2c

%{texmf}/doc/info

%{texmfdist}/fonts/map/dvips/vntex/urwvn.map
%{texmfdist}/fonts/map/fontname
%{texmfdist}/fonts/enc/dvips/vntex/t5.enc

%{texmf}/fonts/enc/dvips/tetex/09fbbfac.enc
%{texmf}/fonts/enc/dvips/tetex/0ef0afca.enc
%{texmf}/fonts/enc/dvips/tetex/10037936.enc
%{texmf}/fonts/enc/dvips/tetex/1b6d048e.enc
%{texmf}/fonts/enc/dvips/tetex/71414f53.enc
%{texmf}/fonts/enc/dvips/tetex/74afc74c.enc
%{texmf}/fonts/enc/dvips/tetex/aae443f0.enc
%{texmf}/fonts/enc/dvips/tetex/b6a4d7c7.enc
%{texmf}/fonts/enc/dvips/tetex/bbad153f.enc
%{texmf}/fonts/enc/dvips/tetex/d9b29452.enc
%{texmf}/fonts/enc/dvips/tetex/f7b6d320.enc
%{texmf}/fonts/map/dvips/tetex/ps2pk35.map

%{texmfdist}/metafont
%{texmfdist}/mft/base
%{texmfdist}/source/metafont
%{texmfdist}/tex/fontinst
%{texmfdist}/tex/generic/dehyph-exptl/*
%{texmfdist}/tex/generic/encodings
%{texmfdist}/tex/generic/epsf
%{texmfdist}/tex/generic/hyph-utf8/*
%{texmfdist}/tex/generic/genmisc
%{texmfdist}/tex/generic/misc/null*
%{texmfdist}/tex/generic/misc/texnames.sty
%{texmfdist}/tex/generic/tap
%{texmfdist}/tex/generic/tex-ps
%{texmfdist}/tex/texinfo
%{texmf}/tex/fontinst
%{texmf}/tex/generic/hyphen
%{texmf}/fmtutil/format.metafont.cnf
%{texmf}/fonts/map/dvips/updmap/*
%{texmf}/web2c/*.tcx

%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvipdft.1*
%{_mandir}/man1/dvipng.1*
%{_mandir}/man1/ebb.1*
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/makempy.1*
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/newer.1*
%{_mandir}/man1/patgen.1*
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/pooltype.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/ps2pk.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
%{_mandir}/man5/fmtutil.cnf.5*
%{_mandir}/man5/updmap.cfg.5*
%{fmtdir}/pdftex/pdfetex.fmt
%{fmtdir}/tex/tex.fmt

%files other-utils
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/mkjobtexmf
%attr(755,root,root) %{_bindir}/bg5+latex
%attr(755,root,root) %{_bindir}/bg5+pdflatex
%attr(755,root,root) %{_bindir}/bg5conv
%attr(755,root,root) %{_bindir}/bg5latex
%attr(755,root,root) %{_bindir}/bg5pdflatex
%attr(755,root,root) %{_bindir}/bibtex8
%attr(755,root,root) %{_bindir}/cfftot1
%attr(755,root,root) %{_bindir}/ebong
%attr(755,root,root) %{_bindir}/extconv
%attr(755,root,root) %{_bindir}/extractbb
%attr(755,root,root) %{_bindir}/gbklatex
%attr(755,root,root) %{_bindir}/gbkpdflatex
%attr(755,root,root) %{_bindir}/getnonfreefonts
%attr(755,root,root) %{_bindir}/getnonfreefonts-sys
%attr(755,root,root) %{_bindir}/hbf2gf
%attr(755,root,root) %{_bindir}/lamed
%attr(755,root,root) %{_bindir}/makeglossaries
%attr(755,root,root) %{_bindir}/metafun
%attr(755,root,root) %{_bindir}/mkjobtexmf
%attr(755,root,root) %{_bindir}/mllatex
%attr(755,root,root) %{_bindir}/mltex
%attr(755,root,root) %{_bindir}/mmafm
%attr(755,root,root) %{_bindir}/mmpfb
%attr(755,root,root) %{_bindir}/musixflx
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/otfinfo
%attr(755,root,root) %{_bindir}/otftotfm
%attr(755,root,root) %{_bindir}/oxdvi
%attr(755,root,root) %{_bindir}/pdfatfi
%attr(755,root,root) %{_bindir}/pdfclose
%attr(755,root,root) %{_bindir}/pdfopen
%attr(755,root,root) %{_bindir}/pdftosrc
%attr(755,root,root) %{_bindir}/perltex
%attr(755,root,root) %{_bindir}/physe
%attr(755,root,root) %{_bindir}/pkfix
%attr(755,root,root) %{_bindir}/rungs
%attr(755,root,root) %{_bindir}/simpdftex
%attr(755,root,root) %{_bindir}/sjisconv
%attr(755,root,root) %{_bindir}/sjislatex
%attr(755,root,root) %{_bindir}/sjispdflatex
%attr(755,root,root) %{_bindir}/synctex
%attr(755,root,root) %{_bindir}/t1dotlessj
%attr(755,root,root) %{_bindir}/t1lint
%attr(755,root,root) %{_bindir}/t1reencode
%attr(755,root,root) %{_bindir}/t1testpage
%attr(755,root,root) %{_bindir}/texcount
%attr(755,root,root) %{_bindir}/texsis
%attr(755,root,root) %{_bindir}/tpic2pdftex
%attr(755,root,root) %{_bindir}/ttftotype42
%attr(755,root,root) %{_bindir}/vlna
%attr(755,root,root) %{_bindir}/vpe
%attr(755,root,root) %{texmfdist}/scripts/mkjobtexmf/mkjobtexmf.pl
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/getnonfreefonts-sys.1
%{_mandir}/man1/getnonfreefonts.1*
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/mkjobtexmf.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
%{_mandir}/man1/oxdvi.1
%{_mandir}/man1/pdftosrc.1*
%{_mandir}/man1/synctex.1*
%{_mandir}/man1/t1dotlessj.1*
%{_mandir}/man1/t1lint.1*
%{_mandir}/man1/t1reencode.1*
%{_mandir}/man1/t1testpage.1*
%{_mandir}/man1/ttftotype42.1*
%{_mandir}/man1/vlna.1*
%{_mandir}/man5/synctex.5*
%{texmfdist}/source/startex
%{texmfdist}/tex/texsis
%{texmfdist}/tex/startex
%{texmf}/fmtutil/fmtutil-hdr.cnf
%{texmf}/fmtutil/format.cyrtex.cnf
%{texmf}/fmtutil/format.cyrtexinfo.cnf
%{texmf}/fmtutil/format.mltex.cnf
%{texmfdist}/tex/generic/abbr
%{texmfdist}/tex/generic/abstyles/
%{texmfdist}/tex/generic/barr
%{texmfdist}/tex/generic/borceux
%{texmfdist}/source/generic/borceux
%{texmfdist}/tex/generic/c-pascal
%{texmfdist}/tex/generic/cirth
%{texmfdist}/tex/generic/dratex
%{texmfdist}/tex/generic/ean
%{texmfdist}/tex/generic/edmac
%{texmfdist}/tex/generic/elvish
%{texmfdist}/tex/generic/fenixpar
%{texmfdist}/tex/generic/fltpoint
%{texmfdist}/source/generic/fltpoint
%{texmfdist}/tex/generic/musixtex
%{texmfdist}/source/generic/hyphenex
%{texmfdist}/source/generic/mkjobtexmf
%{texmf}/hbf2gf
%{texmf}/fmtutil/format.texsis.cnf
%{fmtdir}/pdftex/texsis.fmt

%files jadetex
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/jadetex
%doc %{texmfdist}/doc/jadetex/base
%doc %{texmfdist}/source/jadetex/base/ChangeLog*
%attr(755,root,root) %{_bindir}/jadetex
%attr(755,root,root) %{_bindir}/pdfjadetex
%{texmfdist}/source/jadetex
%exclude %{texmfdist}/source/jadetex/base/ChangeLog*
%{texmfdist}/tex/jadetex
%{texmf}/fmtutil/format.jadetex.cnf

%files other-utils-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/abbr
%doc %{texmfdist}/doc/texsis
%doc %{texmfdist}/doc/startex
%doc %{texmfdist}/doc/generic/c-pascal
%doc %{texmfdist}/doc/generic/barr
%doc %{texmfdist}/doc/generic/borceux
%doc %{texmfdist}/doc/generic/dratex
%doc %{texmfdist}/doc/generic/mkjobtexmf
%doc %{texmfdist}/doc/support/texcount
%doc %{texmf}/doc/tpic2pdftex
%doc %{texmf}/doc/extconv
%doc %{texmfdist}/doc/generic/fenixpar
%doc %{texmfdist}/doc/generic/fltpoint
%doc %{texmf}/doc/bg5conv
%doc %{texmf}/doc/pkfix
%doc %{texmf}/doc/hbf2gf
%doc %{texmf}/doc/sjisconv
%doc %{texmf}/doc/vlna

%files dirs-fonts
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts
%dir %{texmfdist}/fonts/afm
%dir %{texmfdist}/fonts/afm/public
%dir %{texmfdist}/fonts/afm/vntex
%dir %{texmfdist}/fonts/enc
%dir %{texmfdist}/fonts/enc/dvips
%dir %{texmfdist}/fonts/enc/dvips/vntex
%dir %{texmfdist}/fonts/map
%dir %{texmfdist}/fonts/map/dvipdfm
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/map/dvips/vntex
%dir %{texmfdist}/fonts/map/fontname
%dir %{texmfdist}/fonts/map/public
%dir %{texmfdist}/fonts/map/vtex
%dir %{texmfdist}/fonts/ofm
%dir %{texmfdist}/fonts/ofm/public
%dir %{texmfdist}/fonts/ovf
%dir %{texmfdist}/fonts/ovf/public
%dir %{texmfdist}/fonts/ovp
%dir %{texmfdist}/fonts/ovp/public
%dir %{texmfdist}/fonts/opentype
%dir %{texmfdist}/fonts/opentype/public
%dir %{texmfdist}/fonts/pk
%dir %{texmfdist}/fonts/pk/ljfour
%dir %{texmfdist}/fonts/source
%dir %{texmfdist}/fonts/source/public
%dir %{texmfdist}/fonts/source/vntex
%dir %{texmfdist}/fonts/tfm
%dir %{texmfdist}/fonts/tfm/public
%dir %{texmfdist}/fonts/tfm/vntex
%dir %{texmfdist}/fonts/truetype
%dir %{texmfdist}/fonts/type1
%dir %{texmfdist}/fonts/type1/public
%dir %{texmfdist}/fonts/type1/vntex
%dir %{texmfdist}/fonts/vf
%dir %{texmfdist}/fonts/vf/public
%dir %{texmfdist}/fonts/vf/vntex
%dir %{texmfdist}/source/fonts
%dir %{texmf}/fonts
%dir %{texmf}/fonts/opentype
%dir %{texmf}/fonts/opentype/public

%files doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/dehyph-exptl
%dir %{texmfdoc}
%dir %{texmfdoc}/doc
%{texmfdoc}/README
%{texmfdoc}/ls-R
%{texmfdoc}/doc/english
%{texmfdist}/doc/fontinst

%files doc-bg
%defattr(644,root,root,755)
%{texmfdoc}/doc/bulgarian

%files doc-cs
%defattr(644,root,root,755)
%{texmfdoc}/doc/czechslovak

%files doc-de
%defattr(644,root,root,755)
%{texmfdoc}/doc/german

%files doc-el
%defattr(644,root,root,755)
%{texmfdoc}/doc/greek
%{texmf}/doc/generic/elhyphen

%files doc-es
%defattr(644,root,root,755)
%{texmfdoc}/doc/spanish

%files doc-fi
%defattr(644,root,root,755)
%{texmfdoc}/doc/finnish

%files doc-fr
%defattr(644,root,root,755)
%{texmfdoc}/doc/french

%files doc-it
%defattr(644,root,root,755)
%{texmfdoc}/doc/italian

%files doc-ja
%defattr(644,root,root,755)
%{texmfdoc}/doc/japanese

%files doc-ko
%defattr(644,root,root,755)
%{texmfdoc}/doc/korean

%files doc-mn
%defattr(644,root,root,755)
%{texmfdoc}/doc/mongolian

%files doc-nl
%defattr(644,root,root,755)
%{texmfdoc}/doc/dutch

%files doc-pl
%defattr(644,root,root,755)
%{texmfdoc}/doc/polish

%files doc-pt
%defattr(644,root,root,755)
%{texmfdoc}/doc/portuguese

%files doc-ru
%defattr(644,root,root,755)
%{texmfdoc}/doc/russian

%files doc-sk
%defattr(644,root,root,755)
%{texmfdoc}/doc/slovak

%files doc-sl
%defattr(644,root,root,755)
%{texmfdoc}/doc/slovenian

%files doc-th
%defattr(644,root,root,755)
%{texmfdoc}/doc/thai

%files doc-tr
%defattr(644,root,root,755)
%{texmfdoc}/doc/turkish

%files doc-uk
%defattr(644,root,root,755)
%{texmfdoc}/doc/ukrainian

%files doc-vi
%defattr(644,root,root,755)
%{texmfdoc}/doc/vietnamese

%files doc-zh_CN
%defattr(644,root,root,755)
%{texmfdoc}/doc/chinese

%files doc-latex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/calrsfs
%doc %{texmfdist}/doc/generic/encxvlna
%doc %{texmfdist}/doc/generic/shapepar
%doc %{texmfdist}/doc/generic/textmerg
%doc %{texmfdist}/doc/latex/acronym
%doc %{texmfdist}/doc/latex/aeguill
%doc %{texmfdist}/doc/latex/anysize
%doc %{texmfdist}/doc/latex/base
%doc %{texmfdist}/doc/latex/beton
%doc %{texmfdist}/doc/latex/concmath
%doc %{texmfdist}/doc/latex/crop
%doc %{texmfdist}/doc/latex/draftcopy
%doc %{texmfdist}/doc/latex/eepic
%doc %{texmfdist}/doc/latex/endfloat
%doc %{texmfdist}/doc/latex/eso-pic
%doc %{texmfdist}/doc/latex/euler
%doc %{texmfdist}/doc/latex/eulervm
%doc %{texmfdist}/doc/latex/extsizes
%doc %{texmfdist}/doc/latex/fancybox
%doc %{texmfdist}/doc/latex/fancyhdr
%doc %{texmfdist}/doc/latex/fancyvrb
%doc %{texmfdist}/doc/latex/filecontents
%doc %{texmfdist}/doc/latex/float
%doc %{texmfdist}/doc/latex/floatflt
%doc %{texmfdist}/doc/latex/footmisc
%doc %{texmfdist}/doc/latex/footnpag
%doc %{texmfdist}/doc/latex/fp
%doc %{texmfdist}/doc/latex/geometry
%doc %{texmfdist}/doc/latex/graphics
%doc %{texmfdist}/doc/latex/hyperref
%doc %{texmfdist}/doc/latex/hyphenat
%doc %{texmfdist}/doc/latex/index
%doc %{texmfdist}/doc/latex/koma-script
%doc %{texmfdist}/doc/latex/labels
%doc %{texmfdist}/doc/latex/layouts
%doc %{texmfdist}/doc/latex/listings
%doc %{texmfdist}/doc/latex/ltabptch
%doc %{texmfdist}/doc/latex/mdwtools
%doc %{texmfdist}/doc/latex/memoir
%doc %{texmfdist}/doc/latex/mh
%doc %{texmfdist}/doc/latex/mparhack
%doc %{texmfdist}/doc/latex/ms
%doc %{texmfdist}/doc/latex/multibib
%doc %{texmfdist}/doc/latex/mwcls
%doc %{texmfdist}/doc/latex/nomencl
%doc %{texmfdist}/doc/latex/ntgclass
%doc %{texmfdist}/doc/latex/oberdiek
%doc %{texmfdist}/doc/latex/overpic
%doc %{texmfdist}/doc/latex/paralist
%doc %{texmfdist}/doc/latex/pb-diagram
%doc %{texmfdist}/doc/latex/pdfpages
%doc %{texmfdist}/doc/latex/picinpar
%doc %{texmfdist}/doc/latex/pict2e
%doc %{texmfdist}/doc/latex/placeins
%doc %{texmfdist}/doc/latex/preprint
%doc %{texmfdist}/doc/latex/preview
%doc %{texmfdist}/doc/latex/program
%doc %{texmfdist}/doc/latex/psfrag
%doc %{texmfdist}/doc/latex/rotating
%doc %{texmfdist}/doc/latex/rotfloat
%doc %{texmfdist}/doc/latex/scale
%doc %{texmfdist}/doc/latex/sectsty
%doc %{texmfdist}/doc/latex/seminar
%doc %{texmfdist}/doc/latex/showlabels
%doc %{texmfdist}/doc/latex/sidecap
%doc %{texmfdist}/doc/latex/slashbox
%doc %{texmfdist}/doc/latex/soul
%doc %{texmfdist}/doc/latex/stdclsdv
%doc %{texmfdist}/doc/latex/subfig
%doc %{texmfdist}/doc/latex/subfigure
%doc %{texmfdist}/doc/latex/textfit
%doc %{texmfdist}/doc/latex/textpos
%doc %{texmfdist}/doc/latex/titlesec
%doc %{texmfdist}/doc/latex/tocbibind
%doc %{texmfdist}/doc/latex/tocloft
%doc %{texmfdist}/doc/latex/tools
%doc %{texmfdist}/doc/latex/totpages
%doc %{texmfdist}/doc/latex/type1cm
%doc %{texmfdist}/doc/latex/units
%doc %{texmfdist}/doc/latex/vmargin
%doc %{texmfdist}/doc/latex/was
%doc %{texmfdist}/doc/latex/wrapfig
%doc %{texmfdist}/doc/latex/xtab
%doc %{texmfdist}/doc/latex/yfonts

%files -n kpathsea
%defattr(644,root,root,755)
%doc %{texmf}/doc/kpathsea
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_libdir}/libkpathsea.so.*
%{_libdir}/libkpathsea.la
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkpathsea.so
%{_includedir}/kpathsea
%{_infodir}/kpathsea.info*

%files dvips
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts/map/dvips/cmex
%dir %{texmf}/dvipdfm
%dir %{texmf}/fonts/map/dvipdfm
%dir %{texmf}/fonts/map/dvips
%dir %{texmf}/fonts/map/dvips/tetex
%doc %{texmf}/doc/dvips
%doc %{texmf}/doc/dvipdfm
# dvi2fax requires ghostscript
%attr(755,root,root) %{_bindir}/dvi2fax
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvipdfm
%attr(755,root,root) %{_bindir}/dvipdft
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%{_infodir}/dvips.info*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%{texmf}/dvips/base
%{texmf}/dvips/config
%{texmf}/dvips/getafm
%{texmf}/dvips/gsftopk
%{texmfdist}/fonts/enc/dvips/base
%{texmfdist}/fonts/map/dvips/allrunes
%{texmfdist}/fonts/map/dvips/cmex/ttcmex.map
%{texmfdist}/tex/generic/dvips
%{texmfdist}/dvips
%{texmf}/dvipdfm/config
%{texmf}/dvips/tetex/config.*
%{texmf}/fonts/enc/dvips/tetex/mtex.enc
%{texmf}/fonts/enc/dvips/afm2pl
%{texmf}/fonts/map/dvipdfm/updmap
%{texmf}/fonts/map/dvipdfm/dvipdfmx
%{texmf}/fonts/map/dvipdfm/tetex
%{texmf}/fonts/map/dvips/tetex/dvipdfm35.map
%{texmf}/fonts/map/dvips/tetex/dvips35.map
%{texmf}/fonts/map/dvips/tetex/mathpple.map
%{texmf}/fonts/map/dvips/tetex/mt-belleek.map
%{texmf}/fonts/map/dvips/tetex/mt-plus.map
%{texmf}/fonts/map/dvips/tetex/mt-yy.map
%{texmf}/fonts/map/dvips/tetex/pdftex35.map

%files dvilj
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvihp
%attr(755,root,root) %{_bindir}/dvilj
%attr(755,root,root) %{_bindir}/dvilj2p
%attr(755,root,root) %{_bindir}/dvilj4
%attr(755,root,root) %{_bindir}/dvilj4l
%attr(755,root,root) %{_bindir}/dvilj6
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*

%files makeindex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/makeindex
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/rumakeindex
%{texmfdist}/makeindex
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files tlmgr
%defattr(644,root,root,755)
%dir %{texmf}/scripts/texlive
%dir %{texmf}/scripts/texlive/gswin32
%dir %{texmf}/scripts/texlive/lua
%dir %{texmf}/scripts/texlive/lua/texlive
%dir %{texmf}/scripts/texlive/tlmgrgui
%attr(755,root,root) %{texmf}/scripts/texlive/*.pl
%attr(755,root,root) %{texmf}/scripts/texlive/*.tlu
%attr(755,root,root) %{texmf}/scripts/texlive/gswin32/*
%attr(755,root,root) %{texmf}/scripts/texlive/lua/texlive/*
%attr(755,root,root) %{texmf}/scripts/texlive/tlmgrgui/*.pl
%attr(755,root,root) %{_bindir}/tlmgr
%{perl_vendorlib}/TeXLive
%{texmf}/scripts/texlive/tlmgrgui/lang

%files scripts
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/bengali
%dir %{texmfdist}/scripts/glossaries
%dir %{texmfdist}/scripts/oberdiek
%dir %{texmfdist}/scripts/perltex
%dir %{texmfdist}/scripts/pgfplots
%dir %{texmfdist}/scripts/pst2pdf
%dir %{texmfdist}/scripts/shipunov
%dir %{texmfdist}/scripts/texcount
%dir %{texmfdist}/scripts/vpe
%dir %{texmf}/scripts/a2ping
%dir %{texmf}/scripts/pkfix
%dir %{texmf}/scripts/simpdftex
%dir %{texmf}/scripts/tetex
%attr(755,root,root) %{texmfdist}/scripts/bengali/*
%attr(755,root,root) %{texmfdist}/scripts/glossaries/*
%attr(755,root,root) %{texmfdist}/scripts/oberdiek/*
%attr(755,root,root) %{texmfdist}/scripts/perltex/perltex*
%attr(755,root,root) %{texmfdist}/scripts/pgfplots/*
%attr(755,root,root) %{texmfdist}/scripts/pst2pdf/pst2pdf*
%attr(755,root,root) %{texmfdist}/scripts/shipunov/*
%attr(755,root,root) %{texmfdist}/scripts/texcount/*
%attr(755,root,root) %{texmfdist}/scripts/vpe/vpe.pl
%attr(755,root,root) %{texmf}/scripts/a2ping/a2ping*
%attr(755,root,root) %{texmf}/scripts/pkfix/pkfix*
%attr(755,root,root) %{texmf}/scripts/simpdftex/simpdftex*
%attr(755,root,root) %{texmf}/scripts/tetex/*
%attr(755,root,root) %{_bindir}/a2ping
%attr(755,root,root) %{_bindir}/e2pall
%{_mandir}/man1/e2pall.1*
%dir %{texmf}/texdoc
%doc %{texmf}/doc/texdoc
%attr(755,root,root) %{_bindir}/texdoc
%config(noreplace) %verify(not md5 mtime size) %{texmf}/texdoc/texdoc.cnf

%files tex-arrayjob
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/arrayjob
%{texmfdist}/tex/generic/arrayjob

%files tex-insbox
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/insbox
%{texmfdist}/tex/generic/insbox

%files tex-kastrup
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/kastrup
%{texmfdist}/source/generic/kastrup
%{texmfdist}/tex/generic/kastrup

%files tex-mathdots
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mathdots
%{texmfdist}/source/generic/mathdots
%{texmfdist}/tex/generic/mathdots

%files tex-ofs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ofs
%{texmfdist}/tex/generic/ofs

%files tex-physe
%defattr(644,root,root,755)
%{texmfdist}/tex/physe
%{texmf}/fmtutil/format.physe.cnf
%{fmtdir}/pdftex/physe.fmt

%files tex-velthuis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/velthuis
%{texmfdist}/tex/generic/velthuis

%files tex-ytex
%defattr(644,root,root,755)
%{texmfdist}/tex/ytex

%files metapost
%defattr(644,root,root,755)
%dir %{texmfdist}/metapost
%doc %{texmfdist}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%{texmfdist}/metapost/base
%{texmfdist}/metapost/config
%{texmfdist}/metapost/mfpic
%{texmfdist}/metapost/misc
%{texmfdist}/metapost/support
%{texmfdist}/source/metapost
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{texmf}/fmtutil/format.metapost.cnf

%files metapost-other
%defattr(644,root,root,755)
%{texmfdist}/metapost/automata
%{texmfdist}/metapost/bbcard
%{texmfdist}/metapost/blockdraw_mp
%{texmfdist}/metapost/bpolynomial
%{texmfdist}/metapost/cmarrows
%{texmfdist}/metapost/dviincl
%{texmfdist}/metapost/epsincl
%{texmfdist}/metapost/expressg
%{texmfdist}/metapost/exteps
%{texmfdist}/metapost/featpost
%{texmfdist}/metapost/frcursive
%{texmfdist}/metapost/hatching
%{texmfdist}/metapost/metaobj
%{texmfdist}/metapost/metaplot
%{texmfdist}/metapost/metauml
%{texmfdist}/metapost/mp3d
%{texmfdist}/metapost/mpattern
%{texmfdist}/metapost/nkarta
%{texmfdist}/metapost/piechartmp
%{texmfdist}/metapost/slideshow
%{texmfdist}/metapost/splines
%{texmfdist}/metapost/tabvar
%{texmfdist}/metapost/textpath
%{texmfdist}/metapost/venn

%files mptopdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mptopdf
%{_mandir}/man1/mptopdf.1*
%{texmfdist}/tex/mptopdf
%{fmtdir}/pdftex/mptopdf.fmt

%files texdoctk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texdoctk
%{texmf}/texdoctk
%{_mandir}/man1/texdoctk.1*

%files -n texconfig
%defattr(644,root,root,755)
%dir %{texmf}/texconfig
%doc %{texmf}/texconfig/README
%attr(755,root,root) %{_bindir}/texconfig
%attr(755,root,root) %{_bindir}/texconfig-dialog
%attr(755,root,root) %{_bindir}/texconfig-sys
%attr(755,root,root) %{texmf}/texconfig/tcfmgr
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texconfig-sys.1*
%{texmf}/texconfig/g
%{texmf}/texconfig/generic
%{texmf}/texconfig/tcfmgr.map
%{texmf}/texconfig/v
%{texmf}/texconfig/x

%if %{with xindy}
%files -n xindy
%defattr(644,root,root,755)
%doc %{texmf}/doc/xindy
%dir %{texmf}/xindy
%dir %{texmf}/xindy/lang
%dir %{texmf}/scripts/xindy
%attr(755,root,root) %{texmf}/scripts/xindy/*
%attr(755,root,root) %{_bindir}/tex2xindy
%attr(755,root,root) %{_bindir}/xindy
%attr(755,root,root) %{_bindir}/texindy
%{_libdir}/xindy
%{texmf}/xindy/base
%{texmf}/xindy/class
%{texmf}/xindy/ord
%{texmf}/xindy/rules
%{texmf}/xindy/styles
%{texmf}/xindy/tex
%{_mandir}/man1/tex2xindy.1*
%{_mandir}/man1/texindy.1*
%{_mandir}/man1/xindy.1*

%files -n xindy-albanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/albanian

%files -n xindy-belarusian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/belarusian

%files -n xindy-bulgarian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/bulgarian

%files -n xindy-croatian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/croatian

%files -n xindy-czech
%defattr(644,root,root,755)
%{texmf}/xindy/lang/czech

%files -n xindy-danish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/danish

%files -n xindy-dutch
%defattr(644,root,root,755)
%{texmf}/xindy/lang/dutch

%files -n xindy-english
%defattr(644,root,root,755)
%{texmf}/xindy/lang/english

%files -n xindy-esperanto
%defattr(644,root,root,755)
%{texmf}/xindy/lang/esperanto

%files -n xindy-estonian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/estonian

%files -n xindy-finnish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/finnish

%files -n xindy-french
%defattr(644,root,root,755)
%{texmf}/xindy/lang/french

%files -n xindy-general
%defattr(644,root,root,755)
%{texmf}/xindy/lang/general

%files -n xindy-georgian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/georgian

%files -n xindy-german
%defattr(644,root,root,755)
%{texmf}/xindy/lang/german

%files -n xindy-greek
%defattr(644,root,root,755)
%{texmf}/xindy/lang/greek

%files -n xindy-gypsy
%defattr(644,root,root,755)
%{texmf}/xindy/lang/gypsy

%files -n xindy-hausa
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hausa

%files -n xindy-hebrew
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hebrew

%files -n xindy-hungarian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hungarian

%files -n xindy-icelandic
%defattr(644,root,root,755)
%{texmf}/xindy/lang/icelandic

%files -n xindy-italian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/italian

%files -n xindy-klingon
%defattr(644,root,root,755)
%{texmf}/xindy/lang/klingon

%files -n xindy-kurdish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/kurdish

%files -n xindy-latin
%defattr(644,root,root,755)
%{texmf}/xindy/lang/latin

%files -n xindy-latvian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/latvian

%files -n xindy-lithuanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/lithuanian

%files -n xindy-lower-sorbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/lower-sorbian

%files -n xindy-macedonian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/macedonian

%files -n xindy-mongolian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/mongolian

%files -n xindy-norwegian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/norwegian

%files -n xindy-polish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/polish

%files -n xindy-portuguese
%defattr(644,root,root,755)
%{texmf}/xindy/lang/portuguese

%files -n xindy-romanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/romanian

%files -n xindy-russian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/russian

%files -n xindy-serbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/serbian

%files -n xindy-slovak
%defattr(644,root,root,755)
%{texmf}/xindy/lang/slovak

%files -n xindy-slovenian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/slovenian

%files -n xindy-spanish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/spanish

%files -n xindy-swedish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/swedish

%files -n xindy-turkish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/turkish

%files -n xindy-ukrainian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/ukrainian

%files -n xindy-upper-sorbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/upper-sorbian

%files -n xindy-vietnamese
%defattr(644,root,root,755)
%{texmf}/xindy/lang/vietnamese/
%endif

%files -n xdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvi-xaw
%attr(755,root,root) %{_bindir}/xdvi
%{_mandir}/man1/xdvi.1*
%{texmf}/xdvi

%files pdftex
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/pdftexconfig.tex
%dir %{texmfdist}/doc/support
%dir %{texmf}/fonts/map/pdftex
%dir %{texmf}/scripts/epstopdf
%doc %{texmfdist}/doc/pdftex
%doc %{texmfdist}/doc/support/pdfcrop
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdfcrop
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{texmf}/scripts/epstopdf/epstopdf*
%dir %{fmtdir}/pdftex
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdftex.1*
%{texmfdist}/fonts/enc/pdftex
%{texmfdist}/fonts/map/pdftex
%{texmfdist}/scripts/pdfcrop
%{texmf}/fmtutil/format.pdftex.cnf
%{texmf}/fonts/map/pdftex/updmap
%{fmtdir}/pdftex/pdftex.fmt

%files phyzzx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phyzzx
%dir %{texmfdist}/doc/phyzzx
%dir %{texmfdist}/tex/phyzzx
%doc %{texmfdist}/doc/phyzzx/base
%{texmfdist}/tex/phyzzx/base
%{texmfdist}/tex/phyzzx/config
%{texmf}/fmtutil/format.phyzzx.cnf
%{fmtdir}/pdftex/phyzzx.fmt

%files omega
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/aleph
%doc %{texmfdist}/doc/omega
%doc %{texmfdist}/doc/lambda
%dir %{texmfdist}/omega
%dir %{texmfdist}/dvips/omega
%attr(755,root,root) %{_bindir}/aleph
%attr(755,root,root) %{_bindir}/lambda
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvips
%attr(755,root,root) %{_bindir}/odvitype
%attr(755,root,root) %{_bindir}/omega
%attr(755,root,root) %{_bindir}/omfonts
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
%{texmfdist}/dvips/omega/config.omega
%{texmfdist}/dvips/omega/omega.cfg
%{texmfdist}/fonts/map/dvips/omega
%{texmfdist}/tex/generic/omegahyph
%{texmfdist}/omega/ocp
%{texmfdist}/omega/otp
%{texmfdist}/tex/lambda
%{texmfdist}/source/lambda
%{texmf}/fmtutil/format.omega.cnf
%{texmf}/fmtutil/format.aleph.cnf
%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvips.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%{fmtdir}/aleph
%{fmtdir}/omega

%files plain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/plain
%{texmfdist}/tex/plain
%exclude %{texmfdist}/tex/plain/config/xetex.ini
%{texmf}/fmtutil/format.tex.cnf

%files mex
%defattr(644,root,root,755)
%dir %{texmfdist}/tex/mex
%dir %{texmfdist}/tex/mex/config
%doc %{texmfdist}/doc/mex
%{texmfdist}/source/mex
%{texmfdist}/tex/mex/base
%{texmf}/fmtutil/format.mex.cnf
%{texmf}/fmtutil/format.utf8mex.cnf

%files format-mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mex
%{texmfdist}/tex/mex/config/mex.ini
%{fmtdir}/pdftex/mex.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfmex
%{texmfdist}/tex/mex/config/pdfmex.ini

%files format-utf8mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/utf8mex
%{texmfdist}/tex/mex/utf8mex

%files amstex
%defattr(644,root,root,755)
%{texmfdist}/tex/amstex/config
%{texmfdist}/tex/plain/amsfonts

%files format-amstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amstex
%doc %{texmfdist}/doc/amstex
%{texmfdist}/tex/amstex
%{texmf}/fmtutil/format.amstex.cnf
%{texmf}/fmtutil/format.cyramstex.cnf
%{_mandir}/man1/amstex.1*

%files csplain
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/cslatex
%doc %{texmfdist}/doc/cslatex/base
%attr(755,root,root) %{_bindir}/csplain
%{texmfdist}/tex/csplain
%{texmf}/fmtutil/format.csplain.cnf

%files format-csplain
%defattr(644,root,root,755)
%{fmtdir}/pdftex/csplain.fmt

%files format-pdfcsplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcsplain
%{fmtdir}/pdftex/pdfcsplain.fmt

%files cslatex
%defattr(644,root,root,755)
%{texmfdist}/tex/cslatex
%{texmfdist}/tex/latex/cslatex

%files format-cslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cslatex
%{texmf}/fmtutil/format.cslatex.cnf

%files format-pdfcslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcslatex

%files eplain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/etex
%doc %{texmfdist}/doc/eplain
%{texmfdist}/tex/plain/etex
%{texmfdist}/tex/eplain
%dir %{texmfdist}/source/eplain
%{texmfdist}/source/eplain/eplain-source-3.2.zip

%files format-eplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eplain
%attr(755,root,root) %{_bindir}/etex
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{texmf}/fmtutil/format.eplain.cnf
%{fmtdir}/pdftex/etex.fmt

%files context
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/context
%doc %{texmfdist}/doc/luatex
%attr(755,root,root) %{_bindir}/context
%attr(755,root,root) %{_bindir}/ctxtools
%attr(755,root,root) %{_bindir}/exatools
%attr(755,root,root) %{_bindir}/luatools
%attr(755,root,root) %{_bindir}/makempy
%attr(755,root,root) %{_bindir}/mpstools
%attr(755,root,root) %{_bindir}/mtxrun
%attr(755,root,root) %{_bindir}/mtxtools
%attr(755,root,root) %{_bindir}/pdftools
%attr(755,root,root) %{_bindir}/pdftrimwhite
%attr(755,root,root) %{_bindir}/pstopdf
%attr(755,root,root) %{_bindir}/rlxtools
%attr(755,root,root) %{_bindir}/runtools
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texfind
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texmfstart
%attr(755,root,root) %{_bindir}/texshow
%attr(755,root,root) %{_bindir}/textools
%attr(755,root,root) %{_bindir}/texutil
%attr(755,root,root) %{_bindir}/tmftools
%attr(755,root,root) %{_bindir}/xmltools
%{_mandir}/man1/ctxtools.1*
%{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pstopdf.1*
%{_mandir}/man1/texfind.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texmfstart.1*
%{_mandir}/man1/textools.1*
%{_mandir}/man1/texutil.1*
%{texmfdist}/context
%{texmfdist}/fonts/enc/dvips/context
%{texmfdist}/metapost/context
%{texmfdist}/scripts/context
%{texmfdist}/tex/context
%exclude %{texmfdist}/tex/context/config/cont-de.ini
%exclude %{texmfdist}/tex/context/config/cont-en.ini
%exclude %{texmfdist}/tex/context/config/cont-nl.ini
%exclude %{texmfdist}/tex/context/config/cont-uk.ini
%{texmfdist}/tex/generic/context
%{texmfdist}/tex/latex/context
%{texmfdist}/bibtex/bst/context
%{texmf}/fmtutil/format.context.cnf
%{texmf}/fmtutil/format.luatex.cnf
%{texmf}/web2c/context.cnf

%files format-context-de
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-de.ini

%files format-context-en
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-en.ini
# what is the difference betwen uk and en in this particular situation?
%{texmfdist}/tex/context/config/cont-uk.ini

%files format-context-nl
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-nl.ini

%files latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lacheck
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
%dir %{texmfdist}/scripts/pst-pdf
%dir %{texmfdist}/source/generic
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/latex/latexconfig
%dir %{texmfdist}/tex/plain
%dir %{texmf}/tex/latex
%{_mandir}/man1/lacheck.1*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%{texmf}/fmtutil/format.latex.cnf
%{texmfdist}/tex/latex/floatflt
%{texmfdist}/scripts/pst-pdf/ps4pdf
%{texmfdist}/tex/generic/pstricks
%{texmfdist}/tex/generic/shapepar
%{texmfdist}/tex/generic/textmerg
%{texmfdist}/source/generic/textmerg
%{texmfdist}/tex/latex/12many
%{texmfdist}/tex/latex/AkkTeX
%{texmfdist}/tex/latex/GuIT
%{texmfdist}/tex/latex/IEEEtran
%{texmfdist}/tex/latex/Tabbing
%{texmfdist}/tex/latex/a0poster
%{texmfdist}/tex/latex/acmtrans
%{texmfdist}/tex/latex/acronym
%{texmfdist}/tex/latex/adrlist
%{texmfdist}/tex/latex/aeguill
%{texmfdist}/tex/latex/afthesis
%{texmfdist}/tex/latex/aguplus
%{texmfdist}/tex/latex/akletter
%{texmfdist}/tex/latex/algorithm2e
%{texmfdist}/tex/latex/algorithmicx
%{texmfdist}/tex/latex/allrunes
%{texmfdist}/tex/latex/altfont
%{texmfdist}/tex/latex/ametsoc
%{texmfdist}/tex/latex/amsaddr
%{texmfdist}/tex/latex/amsrefs
%{texmfdist}/tex/latex/animate
%{texmfdist}/tex/latex/answers
%{texmfdist}/tex/latex/antiqua
%{texmfdist}/tex/latex/anyfontsize
%{texmfdist}/tex/latex/anysize
%{texmfdist}/tex/latex/apa
%{texmfdist}/tex/latex/apl
%{texmfdist}/tex/latex/ar
%{texmfdist}/tex/latex/arabi
%{texmfdist}/tex/latex/arabtex
%{texmfdist}/tex/latex/archaic
%{texmfdist}/tex/latex/arev
%{texmfdist}/tex/latex/armenian
%{texmfdist}/tex/latex/ascelike
%{texmfdist}/tex/latex/ascii
%{texmfdist}/tex/latex/assignment
%{texmfdist}/tex/latex/augie
%{texmfdist}/tex/latex/auncial-new
%{texmfdist}/tex/latex/aurical
%{texmfdist}/tex/latex/authoraftertitle
%{texmfdist}/tex/latex/authorindex
%{texmfdist}/tex/latex/auto-pst-pdf
%{texmfdist}/tex/latex/autoarea
%{texmfdist}/tex/latex/autotab
%{texmfdist}/tex/latex/avantgar
%{texmfdist}/tex/latex/bangtex
%{texmfdist}/tex/latex/barcodes
%{texmfdist}/tex/latex/base
%{texmfdist}/tex/latex/bayer
%{texmfdist}/tex/latex/bbding
%{texmfdist}/tex/latex/bbm-macros
%{texmfdist}/tex/latex/begriff
%{texmfdist}/tex/latex/bengali
%{texmfdist}/tex/latex/bera
%{texmfdist}/tex/latex/betababel
%{texmfdist}/tex/latex/beton
%{texmfdist}/tex/latex/bibarts
%{texmfdist}/tex/latex/bibleref
%{texmfdist}/tex/latex/biblist
%{texmfdist}/tex/latex/bigfoot
%{texmfdist}/tex/latex/bizcard
%{texmfdist}/tex/latex/blacklettert1
%{texmfdist}/tex/latex/blindtext
%{texmfdist}/tex/latex/boisik
%{texmfdist}/tex/latex/boldtensors
%{texmfdist}/tex/latex/bookest
%{texmfdist}/tex/latex/bookhands
%{texmfdist}/tex/latex/bookman
%{texmfdist}/tex/latex/bophook
%{texmfdist}/tex/latex/boxhandler
%{texmfdist}/tex/latex/braille
%{texmfdist}/tex/latex/breakurl
%{texmfdist}/tex/latex/bridge
%{texmfdist}/tex/latex/brushscr
%{texmfdist}/tex/latex/burmese
%{texmfdist}/tex/latex/bussproofs
%{texmfdist}/tex/latex/calrsfs
%{texmfdist}/tex/latex/calxxxx
%{texmfdist}/tex/latex/captcont
%{texmfdist}/tex/latex/casyl
%{texmfdist}/tex/latex/catechis
%{texmfdist}/tex/latex/cbcoptic
%{texmfdist}/tex/latex/cbfonts
%{texmfdist}/tex/latex/cclicenses
%{texmfdist}/tex/latex/cd-cover
%{texmfdist}/tex/latex/cd
%{texmfdist}/tex/latex/cdpbundl
%{texmfdist}/tex/latex/cellspace
%{texmfdist}/tex/latex/changepage
%{texmfdist}/tex/latex/changes
%{texmfdist}/tex/latex/chapterfolder
%{texmfdist}/tex/latex/cherokee
%{texmfdist}/tex/latex/chicago
%{texmfdist}/tex/latex/china2e
%{texmfdist}/tex/latex/citeref
%{texmfdist}/tex/latex/cjhebrew
%{texmfdist}/tex/latex/cjk
%{texmfdist}/tex/latex/classicthesis
%{texmfdist}/tex/latex/cleveref
%{texmfdist}/tex/latex/clock
%{texmfdist}/tex/latex/clrscode
%{texmfdist}/tex/latex/cm-lgc
%{texmfdist}/tex/latex/cm-super
%{texmfdist}/tex/latex/cmap
%{texmfdist}/tex/latex/cmcyralt
%{texmfdist}/tex/latex/cmdstring
%{texmfdist}/tex/latex/cmsd
%{texmfdist}/tex/latex/codepage
%{texmfdist}/tex/latex/colorinfo
%{texmfdist}/tex/latex/commath
%{texmfdist}/tex/latex/compactbib
%{texmfdist}/tex/latex/complexity
%{texmfdist}/tex/latex/concprog
%{texmfdist}/tex/latex/confproc
%{texmfdist}/tex/latex/courier-scaled
%{texmfdist}/tex/latex/courier
%{texmfdist}/tex/latex/courseoutline
%{texmfdist}/tex/latex/coursepaper
%{texmfdist}/tex/latex/coverpage
%{texmfdist}/tex/latex/covington
%{texmfdist}/tex/latex/crop
%{texmfdist}/tex/latex/crossreference
%{texmfdist}/tex/latex/csbulletin
%{texmfdist}/tex/latex/csquotes
%{texmfdist}/tex/latex/ctib
%{texmfdist}/tex/latex/cursor
%{texmfdist}/tex/latex/cv
%{texmfdist}/tex/latex/cweb-latex
%{texmfdist}/tex/latex/cyklop
%{texmfdist}/tex/latex/dateiliste
%{texmfdist}/tex/latex/datetime
%{texmfdist}/tex/latex/dcpic
%{texmfdist}/tex/latex/decimal
%{texmfdist}/tex/latex/diagnose
%{texmfdist}/tex/latex/dichokey
%{texmfdist}/tex/latex/dictsym
%{texmfdist}/tex/latex/digiconfigs
%{texmfdist}/tex/latex/dingbat
%{texmfdist}/tex/latex/directory
%{texmfdist}/tex/latex/dlfltxb
%{texmfdist}/tex/latex/docmfp
%{texmfdist}/tex/latex/doi
%{texmfdist}/tex/latex/doipubmed
%{texmfdist}/tex/latex/dotarrow
%{texmfdist}/tex/latex/dottex
%{texmfdist}/tex/latex/doublestroke
%{texmfdist}/tex/latex/dpfloat
%{texmfdist}/tex/latex/drac
%{texmfdist}/tex/latex/draftcopy
%{texmfdist}/tex/latex/dramatist
%{texmfdist}/tex/latex/duerer-latex
%{texmfdist}/tex/latex/dvdcoll
%{texmfdist}/tex/latex/dvipdfmx-def
%{texmfdist}/tex/latex/eCards
%{texmfdist}/tex/latex/ean13isbn
%{texmfdist}/tex/latex/easy
%{texmfdist}/tex/latex/ebezier
%{texmfdist}/tex/latex/ebsthesis
%{texmfdist}/tex/latex/ecclesiastic
%{texmfdist}/tex/latex/ecltree
%{texmfdist}/tex/latex/eco
%{texmfdist}/tex/latex/economic
%{texmfdist}/tex/latex/ed
%{texmfdist}/tex/latex/edmargin
%{texmfdist}/tex/latex/ednotes
%{texmfdist}/tex/latex/eemeir
%{texmfdist}/tex/latex/eepic
%{texmfdist}/tex/latex/egameps
%{texmfdist}/tex/latex/eiad
%{texmfdist}/tex/latex/ellipsis
%{texmfdist}/tex/latex/elpres
%{texmfdist}/tex/latex/elsevier
%{texmfdist}/tex/latex/em
%{texmfdist}/tex/latex/emp
%{texmfdist}/tex/latex/emulateapj
%{texmfdist}/tex/latex/encxvlna
%{texmfdist}/tex/latex/endfloat
%{texmfdist}/tex/latex/endheads
%{texmfdist}/tex/latex/engpron
%{texmfdist}/tex/latex/engrec
%{texmfdist}/tex/latex/envbig
%{texmfdist}/tex/latex/envlab
%{texmfdist}/tex/latex/epigrafica
%{texmfdist}/tex/latex/epigraph
%{texmfdist}/tex/latex/epiolmec
%{texmfdist}/tex/latex/epsdice
%{texmfdist}/tex/latex/epspdfconversion
%{texmfdist}/tex/latex/eqname
%{texmfdist}/tex/latex/eqparbox
%{texmfdist}/tex/latex/errata
%{texmfdist}/tex/latex/esint
%{texmfdist}/tex/latex/eskdx
%{texmfdist}/tex/latex/eso-pic
%{texmfdist}/tex/latex/etex-pkg
%{texmfdist}/tex/latex/ethiop
%{texmfdist}/tex/latex/etoolbox
%{texmfdist}/tex/latex/eukdate
%{texmfdist}/tex/latex/euler
%{texmfdist}/tex/latex/eulervm
%{texmfdist}/tex/latex/euproposal
%{texmfdist}/tex/latex/euro
%{texmfdist}/tex/latex/eurofont
%{texmfdist}/tex/latex/europecv
%{texmfdist}/tex/latex/eurosans
%{texmfdist}/tex/latex/eurosym
%{texmfdist}/tex/latex/everypage
%{texmfdist}/tex/latex/examplep
%{texmfdist}/tex/latex/exceltex
%{texmfdist}/tex/latex/exercise
%{texmfdist}/tex/latex/expl3
%{texmfdist}/tex/latex/extarrows
%{texmfdist}/tex/latex/extract
%{texmfdist}/tex/latex/extsizes
%{texmfdist}/tex/latex/facsimile
%{texmfdist}/tex/latex/fancybox
%{texmfdist}/tex/latex/fancyhdr
%{texmfdist}/tex/latex/fancynum
%{texmfdist}/tex/latex/fancyref
%{texmfdist}/tex/latex/fancytooltips
%{texmfdist}/tex/latex/fancyvrb
%{texmfdist}/tex/latex/fax
%{texmfdist}/tex/latex/fc
%{texmfdist}/tex/latex/feyn
%{texmfdist}/tex/latex/fge
%{texmfdist}/tex/latex/figbib
%{texmfdist}/tex/latex/figsize
%{texmfdist}/tex/latex/filecontents
%{texmfdist}/tex/latex/fink
%{texmfdist}/tex/latex/fixfoot
%{texmfdist}/tex/latex/flabels
%{texmfdist}/tex/latex/flacards
%{texmfdist}/tex/latex/flagderiv
%{texmfdist}/tex/latex/flashcards
%{texmfdist}/tex/latex/float
%{texmfdist}/tex/latex/floatrow
%{texmfdist}/tex/latex/fmp
%{texmfdist}/tex/latex/fnbreak
%{texmfdist}/tex/latex/fncychap
%{texmfdist}/tex/latex/foekfont
%{texmfdist}/tex/latex/foilhtml
%{texmfdist}/tex/latex/fonetika
%{texmfdist}/tex/latex/fontinst
%{texmfdist}/tex/latex/fonttable
%{texmfdist}/tex/latex/footmisc
%{texmfdist}/tex/latex/footnpag
%{texmfdist}/tex/latex/fourier
%{texmfdist}/tex/latex/fouriernc
%{texmfdist}/tex/latex/fp
%{texmfdist}/tex/latex/frankenstein
%{texmfdist}/tex/latex/frcursive
%{texmfdist}/tex/latex/frenchle
%{texmfdist}/tex/latex/fribrief
%{texmfdist}/tex/latex/frletter
%{texmfdist}/tex/latex/frontespizio
%{texmfdist}/tex/latex/fullblck
%{texmfdist}/tex/latex/fullpict
%{texmfdist}/tex/latex/fundus
%{texmfdist}/tex/latex/gaceta
%{texmfdist}/tex/latex/gastex
%{texmfdist}/tex/latex/gatech-thesis
%{texmfdist}/tex/latex/gauss
%{texmfdist}/tex/latex/gb4e
%{texmfdist}/tex/latex/gcard
%{texmfdist}/tex/latex/gcite
%{texmfdist}/tex/latex/genmpage
%{texmfdist}/tex/latex/geometry
%{texmfdist}/tex/latex/geomsty
%{texmfdist}/tex/latex/germbib
%{texmfdist}/tex/latex/gfsartemisia
%{texmfdist}/tex/latex/gfsbaskerville
%{texmfdist}/tex/latex/gfsbodoni
%{texmfdist}/tex/latex/gfscomplutum
%{texmfdist}/tex/latex/gfsdidot
%{texmfdist}/tex/latex/gfsneohellenic
%{texmfdist}/tex/latex/gfsporson
%{texmfdist}/tex/latex/gfssolomos
%{texmfdist}/tex/latex/gloss
%{texmfdist}/tex/latex/glossaries
%{texmfdist}/tex/latex/gmdoc
%{texmfdist}/tex/latex/gmeometric
%{texmfdist}/tex/latex/gmiflink
%{texmfdist}/tex/latex/gmutils
%{texmfdist}/tex/latex/gmverb
%{texmfdist}/tex/latex/graphics
%{texmfdist}/tex/latex/graphicx-psmin
%{texmfdist}/tex/latex/greek-inputenc
%{texmfdist}/tex/latex/greekdates
%{texmfdist}/tex/latex/greektex
%{texmfdist}/tex/latex/grfpaste
%{texmfdist}/tex/latex/grnumalt
%{texmfdist}/tex/latex/grotesq
%{texmfdist}/tex/latex/grverb
%{texmfdist}/tex/latex/gu
%{texmfdist}/tex/latex/guitbeamer
%{texmfdist}/tex/latex/hanging
%{texmfdist}/tex/latex/har2nat
%{texmfdist}/tex/latex/harmony
%{texmfdist}/tex/latex/harpoon
%{texmfdist}/tex/latex/harvard
%{texmfdist}/tex/latex/hc
%{texmfdist}/tex/latex/helvetic
%{texmfdist}/tex/latex/hep
%{texmfdist}/tex/latex/hepnames
%{texmfdist}/tex/latex/hepparticles
%{texmfdist}/tex/latex/hepthesis
%{texmfdist}/tex/latex/hepunits
%{texmfdist}/tex/latex/hexgame
%{texmfdist}/tex/latex/hfoldsty
%{texmfdist}/tex/latex/hilowres
%{texmfdist}/tex/latex/histogr
%{texmfdist}/tex/latex/hitec
%{texmfdist}/tex/latex/hpsdiss
%{texmfdist}/tex/latex/hvfloat
%{texmfdist}/tex/latex/hypdvips
%{texmfdist}/tex/latex/hyper
%{texmfdist}/tex/latex/hyperref
%{texmfdist}/tex/latex/hyperxmp
%{texmfdist}/tex/latex/hyphenat
%{texmfdist}/tex/latex/ibycus-babel
%{texmfdist}/tex/latex/icsv
%{texmfdist}/tex/latex/ieeepes
%{texmfdist}/tex/latex/ifmslide
%{texmfdist}/tex/latex/ifplatform
%{texmfdist}/tex/latex/ifsym
%{texmfdist}/tex/latex/ijmart
%{texmfdist}/tex/latex/imac
%{texmfdist}/tex/latex/image-gallery
%{texmfdist}/tex/latex/imtekda
%{texmfdist}/tex/latex/index
%{texmfdist}/tex/latex/initials
%{texmfdist}/tex/latex/inlinebib
%{texmfdist}/tex/latex/inlinedef
%{texmfdist}/tex/latex/interactiveworkbook
%{texmfdist}/tex/latex/invoice
%{texmfdist}/tex/latex/ipa
%{texmfdist}/tex/latex/iso
%{texmfdist}/tex/latex/iso10303
%{texmfdist}/tex/latex/isodate
%{texmfdist}/tex/latex/isodoc
%{texmfdist}/tex/latex/isonums
%{texmfdist}/tex/latex/itnumpar
%{texmfdist}/tex/latex/itrans
%{texmfdist}/tex/latex/iwona
%{texmfdist}/tex/latex/jhep
%{texmfdist}/tex/latex/jknapltx
%{texmfdist}/tex/latex/jneurosci
%{texmfdist}/tex/latex/jpsj
%{texmfdist}/tex/latex/jura
%{texmfdist}/tex/latex/juraabbrev
%{texmfdist}/tex/latex/juramisc
%{texmfdist}/tex/latex/jurarsp
%{texmfdist}/tex/latex/koma-script
%{texmfdist}/tex/latex/labels
%{texmfdist}/tex/latex/latexconfig/latex.ini
%{texmfdist}/tex/latex/latexconfig/lualatex.ini
%{texmfdist}/tex/latex/latexconfig/mllatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflualatex.ini
%{texmfdist}/tex/latex/layouts
%{texmfdist}/tex/latex/listings
%{texmfdist}/tex/latex/ltabptch
%{texmfdist}/tex/latex/localloc
%{texmfdist}/tex/latex/ltxmisc
%{texmfdist}/tex/latex/mathcomp
%{texmfdist}/tex/latex/mdwtools
%{texmfdist}/tex/latex/memoir
%{texmfdist}/tex/latex/mh
%{texmfdist}/tex/latex/misc209
%{texmfdist}/tex/latex/mmap
%{texmfdist}/tex/latex/mnsymbol
%{texmfdist}/tex/latex/moderncv
%{texmfdist}/tex/latex/modroman
%{texmfdist}/tex/latex/mongolian-babel
%{texmfdist}/tex/latex/montex
%{texmfdist}/tex/latex/mparhack
%{texmfdist}/tex/latex/ms
%{texmfdist}/tex/latex/multibib
%{texmfdist}/tex/latex/multirow
%{texmfdist}/tex/latex/mwcls
%{texmfdist}/tex/latex/natbib
%{texmfdist}/tex/latex/ncclatex
%{texmfdist}/tex/latex/ncctools
%{texmfdist}/tex/latex/ncntrsbk
%{texmfdist}/tex/latex/nddiss
%{texmfdist}/tex/latex/newalg
%{texmfdist}/tex/latex/newfile
%{texmfdist}/tex/latex/newlfm
%{texmfdist}/tex/latex/newspaper
%{texmfdist}/tex/latex/newthm
%{texmfdist}/tex/latex/nomencl
%{texmfdist}/tex/latex/ntgclass
%{texmfdist}/tex/generic/oberdiek
%{texmfdist}/tex/latex/oberdiek
%{texmfdist}/tex/latex/overpic
%{texmfdist}/tex/latex/paralist
%{texmfdist}/tex/latex/pb-diagram
%{texmfdist}/tex/latex/pdftex-def
%{texmfdist}/tex/latex/pdfpages
%{texmfdist}/tex/latex/picinpar
%{texmfdist}/tex/latex/pict2e
%{texmfdist}/tex/latex/placeins
%{texmfdist}/tex/latex/preprint
%{texmfdist}/tex/latex/preview
%{texmfdist}/tex/latex/program
%{texmfdist}/tex/latex/psfrag
%{texmfdist}/tex/latex/pslatex
%{texmfdist}/tex/latex/revtex
%{texmfdist}/tex/latex/rotating
%{texmfdist}/tex/latex/rotfloat
%{texmfdist}/tex/latex/scale
%{texmfdist}/tex/latex/sectsty
%{texmfdist}/tex/latex/seminar
%{texmfdist}/tex/latex/setspace
%{texmfdist}/tex/latex/showdim
%{texmfdist}/tex/latex/showlabels
%{texmfdist}/tex/latex/sidecap
%{texmfdist}/tex/latex/slashbox
%{texmfdist}/tex/latex/soul
%{texmfdist}/tex/latex/stdclsdv
%{texmfdist}/tex/latex/stmaryrd
%{texmfdist}/tex/latex/subfig
%{texmfdist}/tex/latex/subfigure
%{texmfdist}/tex/latex/supertabular
%{texmfdist}/tex/latex/t2
%{texmfdist}/tex/latex/t-angles
%{texmfdist}/tex/latex/tableaux
%{texmfdist}/tex/latex/tablists
%{texmfdist}/tex/latex/tablor
%{texmfdist}/tex/latex/tabto-ltx
%{texmfdist}/tex/latex/tabulary
%{texmfdist}/tex/latex/tabvar
%{texmfdist}/tex/latex/talk
%{texmfdist}/tex/latex/taupin
%{texmfdist}/tex/latex/tcldoc
%{texmfdist}/tex/latex/tdsfrmath
%{texmfdist}/tex/latex/technics
%{texmfdist}/tex/latex/ted
%{texmfdist}/tex/latex/tengwarscript
%{texmfdist}/tex/latex/tensor
%{texmfdist}/tex/latex/teubner
%{texmfdist}/tex/latex/tex-gyre
%{texmfdist}/tex/latex/texilikecover
%{texmfdist}/tex/latex/texlogos
%{texmfdist}/tex/latex/texmate
%{texmfdist}/tex/latex/texpower
%{texmfdist}/tex/latex/texshade
%{texmfdist}/tex/latex/textcase
%{texmfdist}/tex/latex/textfit
%{texmfdist}/tex/latex/textopo
%{texmfdist}/tex/latex/textpath
%{texmfdist}/tex/latex/textpos
%{texmfdist}/tex/latex/theoremref
%{texmfdist}/tex/latex/thesis-titlepage-fhac
%{texmfdist}/tex/latex/thinsp
%{texmfdist}/tex/latex/thmtools
%{texmfdist}/tex/latex/thumb
%{texmfdist}/tex/latex/thuthesis
%{texmfdist}/tex/latex/ticket
%{texmfdist}/tex/latex/tikz-inet
%{texmfdist}/tex/latex/times
%{texmfdist}/tex/latex/timesht
%{texmfdist}/tex/latex/tipa
%{texmfdist}/tex/latex/titlefoot
%{texmfdist}/tex/latex/titlesec
%{texmfdist}/tex/latex/titling
%{texmfdist}/tex/latex/tocbibind
%{texmfdist}/tex/latex/tocloft
%{texmfdist}/tex/latex/tools
%{texmfdist}/tex/latex/totpages
%{texmfdist}/tex/latex/type1cm
%{texmfdist}/tex/latex/undertilde
%{texmfdist}/tex/latex/units
%{texmfdist}/tex/latex/unitsdef
%{texmfdist}/tex/latex/universa
%{texmfdist}/tex/latex/unroman
%{texmfdist}/tex/latex/upmethodology
%{texmfdist}/tex/latex/upquote
%{texmfdist}/tex/latex/varindex
%{texmfdist}/tex/latex/varsfromjobname
%{texmfdist}/tex/latex/vector
%{texmfdist}/tex/latex/velthuis
%{texmfdist}/tex/latex/verse
%{texmfdist}/tex/latex/versions
%{texmfdist}/tex/latex/vhistory
%{texmfdist}/tex/latex/vita
%{texmfdist}/tex/latex/vmargin
%{texmfdist}/tex/latex/volumes
%{texmfdist}/tex/latex/vpe
%{texmfdist}/tex/latex/vrsion
%{texmfdist}/tex/latex/vwcol
%{texmfdist}/tex/latex/vxu
%{texmfdist}/tex/latex/wallpaper
%{texmfdist}/tex/latex/warning
%{texmfdist}/tex/latex/warpcol
%{texmfdist}/tex/latex/was
%{texmfdist}/tex/latex/williams
%{texmfdist}/tex/latex/wnri
%{texmfdist}/tex/latex/wordlike
%{texmfdist}/source/wordlike
%{texmfdist}/tex/latex/wrapfig
%{texmfdist}/tex/latex/wsuipa
%{texmfdist}/source/generic/wsuipa
%{texmfdist}/tex/latex/xargs
%{texmfdist}/tex/latex/xcolor
%{texmfdist}/tex/latex/xdoc
%{texmfdist}/tex/latex/xfor
%{texmfdist}/tex/latex/xifthen
%{texmfdist}/tex/latex/xkeyval
%{texmfdist}/tex/latex/xmpincl
%{texmfdist}/tex/latex/xnewcommand
%{texmfdist}/tex/latex/xoptarg
%{texmfdist}/tex/latex/xpackages
%{texmfdist}/tex/latex/xq
%{texmfdist}/tex/latex/xskak
%{texmfdist}/tex/latex/xstring
%{texmfdist}/tex/latex/xtab
%{texmfdist}/tex/latex/xtcapts
%{texmfdist}/tex/latex/xyling
%{texmfdist}/tex/latex/xytree
%{texmfdist}/tex/latex/yafoot
%{texmfdist}/tex/latex/yfonts
%{texmfdist}/tex/latex/yhmath
%{texmfdist}/tex/latex/yi4latex
%{texmfdist}/tex/latex/york-thesis
%{texmfdist}/tex/latex/youngtab
%{texmfdist}/tex/latex/yplan
%{texmfdist}/tex/latex/zapfchan
%{texmfdist}/tex/latex/zapfding
%{texmfdist}/tex/latex/zed-csp
%{texmfdist}/tex/latex/zefonts
%{texmfdist}/tex/latex/ziffer
%{texmfdist}/tex/latex/zwgetfdate
%{texmfdist}/tex/plain/etex
%{texmf}/tex/latex/config
%{texmf}/tex/latex/dvipdfm
%{fmtdir}/pdftex/latex.fmt
%{fmtdir}/pdftex/mllatex.fmt

%files latex-12many
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/12many
%{texmfdist}/source/latex/12many

%files latex-abstract
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/abstract
%{texmfdist}/tex/latex/abstract
%{texmfdist}/source/latex/abstract

%files latex-accfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/accfonts
%{texmfdist}/tex/latex/accfonts

%files latex-adrconv
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/adrconv
%{texmfdist}/doc/latex/adrconv

%files latex-algorithms
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/algorithms
%{texmfdist}/tex/latex/algorithms

%files latex-ae
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/ae

%files latex-ams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/amsfonts
%doc %{texmfdist}/doc/latex/amscls
%doc %{texmfdist}/doc/latex/amsmath
%doc %{texmfdist}/doc/latex/onlyamsmath
%{texmfdist}/tex/latex/amscls
%{texmfdist}/tex/latex/amsmath
%{texmfdist}/tex/latex/amsfonts
%{texmfdist}/tex/latex/onlyamsmath
%{texmfdist}/source/latex/onlyamsmath
%{texmfdist}/source/latex/amsaddr
%{texmfdist}/source/latex/amscls
%{texmfdist}/source/latex/amsfonts
%{texmfdist}/source/latex/amsmath
%{texmfdist}/source/latex/amsrefs

%files latex-antp
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/antp

%files latex-antt
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/antt

%files latex-appendix
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/appendix
%{texmfdist}/tex/latex/appendix
%{texmfdist}/source/latex/appendix

%files latex-bardiag
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bardiag
%{texmfdist}/tex/latex/bardiag

%files latex-bbm
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/bbm

%files latex-bbold
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bbold
%{texmfdist}/tex/latex/bbold
%{texmfdist}/source/latex/bbold

%files latex-beamer
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/beamer
%{texmfdist}/tex/latex/beamer-contrib
%{texmfdist}/tex/latex/beamer

%files latex-bezos
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bezos
%{texmfdist}/tex/latex/bezos

%files latex-bibtex
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex
%dir %{texmfdist}/bibtex/bib
%dir %{texmfdist}/bibtex/bst
%dir %{texmfdist}/bibtex/csf
%dir %{texmfdist}/doc/bibtex
%dir %{texmf}/bibtex
%doc %{texmfdist}/doc/bibtex/base
%doc %{texmfdist}/doc/latex/bibtopic
%doc %{texmfdist}/doc/latex/bibunits
%doc %{texmfdist}/doc/latex/footbib
%doc %{texmfdist}/doc/latex/natbib
%doc %{texmf}/doc/bibtex8
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/rubibtex
%{texmfdist}/bibtex/bib/adrconv
%{texmfdist}/bibtex/bib/base
%{texmfdist}/bibtex/bst/adrconv
%{texmfdist}/bibtex/bst/base
%{texmfdist}/bibtex/bst/natbib
%{texmfdist}/bibtex/csf/base
%{texmfdist}/source/latex/adrconv
%{texmfdist}/source/latex/bibtopic
%{texmfdist}/source/latex/bibunits
%{texmfdist}/source/latex/footbib
%{texmfdist}/tex/latex/bibtopic
%{texmfdist}/tex/latex/bibunits
%{texmfdist}/tex/latex/footbib
%{texmfdist}/tex/latex/natbib
%{texmf}/bibtex/csf

%files latex-bibtex-ams
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bst/ams
%{texmfdist}/bibtex/bib/ams

%files latex-bibtex-pl
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/gustlib
%{texmfdist}/bibtex/bib/gustlib/plbib.bib

%files latex-bibtex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/bibtex/germbib
%{texmfdist}/bibtex/bst/germbib
%{texmfdist}/tex/latex/germbib

%files latex-bibtex-revtex4
%defattr(644,root,root,755)
%dir %{texmfdist}/source/latex/revtex
%dir %{texmfdist}/doc/latex
%doc %{texmfdist}/doc/latex/revtex
%{texmfdist}/source/latex/revtex/revtex4.dtx
%{texmfdist}/source/latex/revtex/revtex4.ins
%{texmfdist}/tex/latex/revtex/revtex4.cls

%files latex-bibtex-jurabib
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/jurabib
%{texmfdist}/bibtex/bst/jurabib
%{texmfdist}/bibtex/bib/jurabib
%{texmfdist}/source/latex/jurabib
%{texmfdist}/tex/latex/jurabib

%files latex-bibtex-dk
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/dk-bib
%{texmfdist}/bibtex/bst/dk-bib
%{texmfdist}/bibtex/csf/dk-bib
%{texmfdist}/bibtex/bib/dk-bib
%{texmfdist}/source/latex/dk-bib
%{texmfdist}/tex/latex/dk-bib

%files latex-bibtex-styles
%defattr(644,root,root,755)
%dir %{texmfdist}/source/bibtex
%doc %{texmfdist}/doc/bibtex/abstyles
%doc %{texmfdist}/doc/bibtex/bibhtml
%doc %{texmfdist}/doc/bibtex/dinat
%doc %{texmfdist}/doc/bibtex/economic
%doc %{texmfdist}/doc/bibtex/elsevier-bib
%doc %{texmfdist}/doc/bibtex/gost
%doc %{texmfdist}/doc/bibtex/ijqc
%doc %{texmfdist}/doc/bibtex/iopart-num
%doc %{texmfdist}/doc/generic/t2
%doc %{texmfdist}/doc/latex/IEEEtran
%{texmfdist}/bibtex/bib/IEEEtran
%{texmfdist}/bibtex/bib/abstyles
%{texmfdist}/bibtex/bib/achemso
%{texmfdist}/bibtex/bib/acmtrans
%{texmfdist}/bibtex/bib/ascelike
%{texmfdist}/bibtex/bib/beebe
%{texmfdist}/bibtex/bib/bibhtml
%{texmfdist}/bibtex/bib/bibtopic
%{texmfdist}/bibtex/bib/din1505
%{texmfdist}/bibtex/bib/directory
%{texmfdist}/bibtex/bib/figbib
%{texmfdist}/bibtex/bib/frankenstein
%{texmfdist}/bibtex/bib/gatech-thesis
%{texmfdist}/bibtex/bib/geomsty
%{texmfdist}/bibtex/bib/gloss
%{texmfdist}/bibtex/bib/harvard
%{texmfdist}/bibtex/bib/ieeepes
%{texmfdist}/bibtex/bib/ijmart
%{texmfdist}/bibtex/bib/imac
%{texmfdist}/bibtex/bib/index
%{texmfdist}/bibtex/bib/lsc
%{texmfdist}/bibtex/bib/msc
%{texmfdist}/bibtex/bib/nostarch
%{texmfdist}/bibtex/bib/revtex
%{texmfdist}/bibtex/bib/spie
%{texmfdist}/bibtex/bib/urlbst
%{texmfdist}/bibtex/bst/IEEEtran
%{texmfdist}/bibtex/bst/abstyles
%{texmfdist}/bibtex/bst/achemso
%{texmfdist}/bibtex/bst/acmtrans
%{texmfdist}/bibtex/bst/afthesis
%{texmfdist}/bibtex/bst/aguplus
%{texmfdist}/bibtex/bst/aichej
%{texmfdist}/bibtex/bst/ametsoc
%{texmfdist}/bibtex/bst/ascelike
%{texmfdist}/bibtex/bst/beebe
%{texmfdist}/bibtex/bst/bibhtml
%{texmfdist}/bibtex/bst/chem-journal
%{texmfdist}/bibtex/bst/chicago
%{texmfdist}/bibtex/bst/confproc
%{texmfdist}/bibtex/bst/datatool
%{texmfdist}/bibtex/bst/din1505
%{texmfdist}/bibtex/bst/dinat
%{texmfdist}/bibtex/bst/directory
%{texmfdist}/bibtex/bst/dvdcoll
%{texmfdist}/bibtex/bst/economic
%{texmfdist}/bibtex/bst/elsevier-bib
%{texmfdist}/bibtex/bst/fbs
%{texmfdist}/bibtex/bst/figbib
%{texmfdist}/bibtex/bst/finbib
%{texmfdist}/bibtex/bst/frankenstein
%{texmfdist}/bibtex/bst/gatech-thesis
%{texmfdist}/bibtex/bst/gloss
%{texmfdist}/bibtex/bst/gost
%{texmfdist}/bibtex/bst/gustlib
%{texmfdist}/bibtex/bst/harvard
%{texmfdist}/bibtex/bst/hc
%{texmfdist}/bibtex/bst/ieeepes
%{texmfdist}/bibtex/bst/ijmart
%{texmfdist}/bibtex/bst/ijqc
%{texmfdist}/bibtex/bst/imac
%{texmfdist}/bibtex/bst/index
%{texmfdist}/bibtex/bst/inlinebib
%{texmfdist}/bibtex/bst/iopart-num
%{texmfdist}/bibtex/bst/jneurosci
%{texmfdist}/bibtex/bst/jurarsp
%{texmfdist}/bibtex/bst/kluwer
%{texmfdist}/bibtex/bst/mslapa
%{texmfdist}/bibtex/bst/multibib
%{texmfdist}/bibtex/bst/munich
%{texmfdist}/bibtex/bst/nature
%{texmfdist}/bibtex/bst/nddiss
%{texmfdist}/bibtex/bst/opcit
%{texmfdist}/bibtex/bst/perception
%{texmfdist}/bibtex/bst/revtex
%{texmfdist}/bibtex/bst/savetrees
%{texmfdist}/bibtex/bst/shipunov
%{texmfdist}/bibtex/bst/smflatex
%{texmfdist}/bibtex/bst/sort-by-letters
%{texmfdist}/bibtex/bst/spie
%{texmfdist}/bibtex/bst/stellenbosch
%{texmfdist}/bibtex/bst/swebib
%{texmfdist}/bibtex/bst/texsis
%{texmfdist}/bibtex/bst/thuthesis
%{texmfdist}/bibtex/bst/tugboat
%{texmfdist}/bibtex/bst/urlbst
%{texmfdist}/bibtex/csf/gost
%{texmfdist}/source/bibtex/gost

%files latex-bibtex-vancouver
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/vancouver
%dir %{texmfdist}/bibtex/bst/vancouver
%dir %{texmfdist}/doc/bibtex/vancouver
%doc %{texmfdist}/doc/bibtex/vancouver/README
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.pdf
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.tex
%{texmfdist}/bibtex/bib/vancouver/vancouver.bib
%{texmfdist}/bibtex/bst/vancouver/vancouver.bst

%files latex-booktabs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/booktabs
%{texmfdist}/source/latex/booktabs
%{texmfdist}/tex/latex/booktabs

%files latex-caption
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/caption
%{texmfdist}/tex/latex/caption
%{texmfdist}/source/latex/caption

%files latex-carlisle
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/carlisle
%{texmfdist}/tex/latex/carlisle
%{texmfdist}/source/latex/carlisle

%files latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccfonts
%{texmfdist}/source/latex/ccfonts
%{texmfdist}/tex/latex/ccfonts

%files latex-cite
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/cite

%files latex-cmbright
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cmbright
%{texmfdist}/tex/latex/cmbright

%files latex-colortab
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/colortab
%{texmfdist}/tex/latex/colortab
%{texmfdist}/tex/generic/colortab

%files latex-comment
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/comment
%{texmfdist}/tex/latex/comment
%{texmfdist}/source/latex/comment

%files latex-concmath
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/concmath

%files latex-currvita
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/currvita
%{texmfdist}/tex/latex/currvita
%{texmfdist}/source/latex/currvita
%doc %{texmfdist}/doc/latex/curve
%{texmfdist}/source/latex/curve
%{texmfdist}/tex/latex/curve
%doc %{texmfdist}/doc/latex/ecv
%{texmfdist}/source/latex/ecv
%{texmfdist}/tex/latex/ecv
%doc %{texmfdist}/doc/latex/simplecv
%{texmfdist}/source/latex/simplecv
%{texmfdist}/tex/latex/simplecv

%files latex-curves
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/curves
%{texmfdist}/source/latex/curves
%{texmfdist}/tex/latex/curves

%files latex-custom-bib
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/custom-bib
%{texmfdist}/source/latex/custom-bib
%{texmfdist}/tex/latex/custom-bib

%files latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cyrillic
%{texmfdist}/source/latex/cyrillic
%{texmfdist}/tex/latex/cyrillic

%files latex-enumitem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/enumitem
%{texmfdist}/tex/latex/enumitem

%files latex-exams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/exam
%doc %{texmfdist}/doc/latex/examdesign
%doc %{texmfdist}/doc/latex/mathexam
%doc %{texmfdist}/doc/latex/probsoln
%doc %{texmfdist}/doc/latex/qcm
%doc %{texmfdist}/doc/latex/uebungsblatt
%{texmfdist}/source/latex/examdesign
%{texmfdist}/source/latex/mathexam
%{texmfdist}/source/latex/probsoln
%{texmfdist}/source/latex/qcm
%{texmfdist}/tex/latex/exam
%{texmfdist}/tex/latex/examdesign
%{texmfdist}/tex/latex/mathexam
%{texmfdist}/tex/latex/probsoln
%{texmfdist}/tex/latex/qcm
%{texmfdist}/tex/latex/uebungsblatt

%files latex-float
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccaption
%doc %{texmfdist}/doc/latex/photo
%doc %{texmfdist}/doc/latex/topfloat
%{texmfdist}/source/latex/ccaption
%{texmfdist}/source/latex/photo
%{texmfdist}/tex/latex/ccaption
%{texmfdist}/tex/latex/photo
%{texmfdist}/tex/latex/topfloat

%files latex-foiltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/foiltex
%{texmfdist}/tex/latex/foiltex

%files latex-formlett
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/formlett
%{texmfdist}/tex/latex/formlett

%files latex-formular
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/formular
%{texmfdist}/tex/latex/formular
%{texmfdist}/source/latex/formular

%files latex-gbrief
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/g-brief
%{texmfdist}/source/latex/g-brief
%{texmfdist}/tex/latex/g-brief

%files latex-keystroke
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/keystroke
%doc %{texmfdist}/doc/latex/keystroke

%files latex-labbook
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/labbook
%{texmfdist}/source/latex/labbook
%{texmfdist}/tex/latex/labbook

%files latex-lastpage
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lastpage
%{texmfdist}/tex/latex/lastpage
%{texmfdist}/source/latex/lastpage

%files latex-lcd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lcd
%{texmfdist}/source/latex/lcd
%{texmfdist}/tex/latex/lcd

%files latex-leaflet
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leaflet
%{texmfdist}/source/latex/leaflet
%{texmfdist}/tex/latex/leaflet

%files latex-leftidx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leftidx
%{texmfdist}/tex/latex/leftidx
%{texmfdist}/source/latex/leftidx

%files latex-lewis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lewis
%{texmfdist}/tex/latex/lewis

%files latex-lm
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
%{texmfdist}/source/fonts/lm

%files latex-lucidabr
%defattr(644,root,root,755)
%dir %{texmfdist}/vtex
%{texmfdist}/vtex/config

%files latex-lineno
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lineno
%{texmfdist}/tex/latex/lineno

%files latex-metre
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/metre
%{texmfdist}/source/latex/metre
%{texmfdist}/tex/latex/metre

%files latex-marvosym
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/marvosym

%files latex-microtype
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/microtype
%{texmfdist}/source/latex/microtype
%{texmfdist}/tex/latex/microtype

%files latex-misc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/fixme
%{texmfdist}/source/latex/fixme
%{texmfdist}/tex/latex/fixme
%doc %{texmfdist}/doc/latex/recipecard
%{texmfdist}/source/latex/recipecard
%{texmfdist}/tex/latex/recipecard
%doc %{texmfdist}/doc/latex/cooking
%{texmfdist}/source/latex/cooking
%{texmfdist}/tex/latex/cooking
%doc %{texmfdist}/doc/latex/cuisine
%{texmfdist}/source/latex/cuisine
%{texmfdist}/tex/latex/cuisine
%doc %{texmfdist}/doc/latex/todo
%{texmfdist}/source/latex/todo
%{texmfdist}/tex/latex/todo

%files latex-mflogo
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mflogo
%{texmfdist}/tex/latex/mflogo

%files latex-mfnfss
%defattr(644,root,root,755)
%{texmfdist}/source/latex/mfnfss
%{texmfdist}/tex/latex/mfnfss

%files latex-minitoc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/minitoc
%{texmfdist}/bibtex/bst/minitoc
%{texmfdist}/makeindex/minitoc
%{texmfdist}/scripts/minitoc
%{texmfdist}/source/latex/minitoc
%{texmfdist}/tex/latex/minitoc

%files latex-mltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mltex
%{texmfdist}/tex/latex/mltex
%dir %{texmfdist}/tex/mltex
%{texmfdist}/tex/mltex/config

%files latex-moreverb
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/moreverb
%{texmfdist}/tex/latex/moreverb
%{texmfdist}/source/latex/moreverb

%files latex-multienum
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/multenum
%dir %{texmfdist}/tex/latex/multenum
%{texmfdist}/tex/latex/multenum/*

%files latex-musictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/musictex
%{texmfdist}/fonts/source/public/musictex
%{texmfdist}/fonts/tfm/public/musictex
%{texmfdist}/tex/generic/musictex
%{texmfdist}/tex/latex/musictex

%files latex-ntheorem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ntheorem
%{texmfdist}/tex/latex/ntheorem
%{texmfdist}/source/latex/ntheorem

%files latex-other-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/alatex
%doc %{texmfdist}/doc/generic/wsuipa
%doc %{texmfdist}/doc/latex/ANUfinalexam
%doc %{texmfdist}/doc/latex/AkkTeX
%doc %{texmfdist}/doc/latex/GuIT
%doc %{texmfdist}/doc/latex/a0poster
%doc %{texmfdist}/doc/latex/acmtrans
%doc %{texmfdist}/doc/latex/adrlist
%doc %{texmfdist}/doc/latex/afthesis
%doc %{texmfdist}/doc/latex/aguplus
%doc %{texmfdist}/doc/latex/akletter
%doc %{texmfdist}/doc/latex/algorithm2e
%doc %{texmfdist}/doc/latex/algorithmicx
%doc %{texmfdist}/doc/latex/altfont
%doc %{texmfdist}/doc/latex/ametsoc
%doc %{texmfdist}/doc/latex/amsaddr
%doc %{texmfdist}/doc/latex/amsrefs
%doc %{texmfdist}/doc/latex/animate
%doc %{texmfdist}/doc/latex/answers
%doc %{texmfdist}/doc/latex/anyfontsize
%doc %{texmfdist}/doc/latex/apa
%doc %{texmfdist}/doc/latex/ar
%doc %{texmfdist}/doc/latex/arabi
%doc %{texmfdist}/doc/latex/arabtex
%doc %{texmfdist}/doc/latex/ascelike
%doc %{texmfdist}/doc/latex/assignment
%doc %{texmfdist}/doc/latex/augie
%doc %{texmfdist}/doc/latex/aurical
%doc %{texmfdist}/doc/latex/authorindex
%doc %{texmfdist}/doc/latex/autoarea
%doc %{texmfdist}/doc/latex/autotab
%doc %{texmfdist}/doc/latex/bangtex
%doc %{texmfdist}/doc/latex/barcodes
%doc %{texmfdist}/doc/latex/bayer
%doc %{texmfdist}/doc/latex/bbm-macros
%doc %{texmfdist}/doc/latex/beamer-contrib
%doc %{texmfdist}/doc/latex/begriff
%doc %{texmfdist}/doc/latex/betababel
%doc %{texmfdist}/doc/latex/bibarts
%doc %{texmfdist}/doc/latex/bibleref
%doc %{texmfdist}/doc/latex/biblist
%doc %{texmfdist}/doc/latex/bigfoot
%doc %{texmfdist}/doc/latex/bizcard
%doc %{texmfdist}/doc/latex/blindtext
%doc %{texmfdist}/doc/latex/boldtensors
%doc %{texmfdist}/doc/latex/bookest
%doc %{texmfdist}/doc/latex/boxhandler
%doc %{texmfdist}/doc/latex/braille
%doc %{texmfdist}/doc/latex/breakurl
%doc %{texmfdist}/doc/latex/brushscr
%doc %{texmfdist}/doc/latex/bussproofs
%doc %{texmfdist}/doc/latex/calxxxx
%doc %{texmfdist}/doc/latex/captcont
%doc %{texmfdist}/doc/latex/casyl
%doc %{texmfdist}/doc/latex/catechis
%doc %{texmfdist}/doc/latex/cbcoptic
%doc %{texmfdist}/doc/latex/cclicenses
%doc %{texmfdist}/doc/latex/cd-cover
%doc %{texmfdist}/doc/latex/cd
%doc %{texmfdist}/doc/latex/cdpbundl
%doc %{texmfdist}/doc/latex/cellspace
%doc %{texmfdist}/doc/latex/changes
%doc %{texmfdist}/doc/latex/chapterfolder
%doc %{texmfdist}/doc/latex/china2e
%doc %{texmfdist}/doc/latex/cite
%doc %{texmfdist}/doc/latex/classicthesis
%doc %{texmfdist}/doc/latex/cleveref
%doc %{texmfdist}/doc/latex/clock
%doc %{texmfdist}/doc/latex/clrscode
%doc %{texmfdist}/doc/latex/cm-lgc
%doc %{texmfdist}/doc/latex/cmap
%doc %{texmfdist}/doc/latex/cmcyralt
%doc %{texmfdist}/doc/latex/cmdstring
%doc %{texmfdist}/doc/latex/codepage
%doc %{texmfdist}/doc/latex/colorinfo
%doc %{texmfdist}/doc/latex/commath
%doc %{texmfdist}/doc/latex/complexity
%doc %{texmfdist}/doc/latex/concprog
%doc %{texmfdist}/doc/latex/confproc
%doc %{texmfdist}/doc/latex/courier-scaled
%doc %{texmfdist}/doc/latex/courseoutline
%doc %{texmfdist}/doc/latex/coursepaper
%doc %{texmfdist}/doc/latex/coverpage
%doc %{texmfdist}/doc/latex/covington
%doc %{texmfdist}/doc/latex/crossreference
%doc %{texmfdist}/doc/latex/cryst
%doc %{texmfdist}/doc/latex/csbulletin
%doc %{texmfdist}/doc/latex/csquotes
%doc %{texmfdist}/doc/latex/ctib
%doc %{texmfdist}/doc/latex/cursor
%doc %{texmfdist}/doc/latex/cv
%doc %{texmfdist}/doc/latex/cweb-latex
%doc %{texmfdist}/doc/latex/dateiliste
%doc %{texmfdist}/doc/latex/datetime
%doc %{texmfdist}/doc/latex/dcpic
%doc %{texmfdist}/doc/latex/diagnose
%doc %{texmfdist}/doc/latex/dichokey
%doc %{texmfdist}/doc/latex/digiconfigs
%doc %{texmfdist}/doc/latex/din1505
%doc %{texmfdist}/doc/latex/directory
%doc %{texmfdist}/doc/latex/dlfltxb
%doc %{texmfdist}/doc/latex/docmfp
%doc %{texmfdist}/doc/latex/doi
%doc %{texmfdist}/doc/latex/doipubmed
%doc %{texmfdist}/doc/latex/dotarrow
%doc %{texmfdist}/doc/latex/dottex
%doc %{texmfdist}/doc/latex/dpfloat
%doc %{texmfdist}/doc/latex/drac
%doc %{texmfdist}/doc/latex/dramatist
%doc %{texmfdist}/doc/latex/dtxgallery
%doc %{texmfdist}/doc/latex/duerer-latex
%doc %{texmfdist}/doc/latex/dvdcoll
%doc %{texmfdist}/doc/latex/eCards
%doc %{texmfdist}/doc/latex/ean13isbn
%doc %{texmfdist}/doc/latex/easy
%doc %{texmfdist}/doc/latex/ebezier
%doc %{texmfdist}/doc/latex/ebong
%doc %{texmfdist}/doc/latex/ebsthesis
%doc %{texmfdist}/doc/latex/ecclesiastic
%doc %{texmfdist}/doc/latex/ecltree
%doc %{texmfdist}/doc/latex/ed
%doc %{texmfdist}/doc/latex/edmac
%doc %{texmfdist}/doc/latex/edmargin
%doc %{texmfdist}/doc/latex/ednotes
%doc %{texmfdist}/doc/latex/eemeir
%doc %{texmfdist}/doc/latex/egameps
%doc %{texmfdist}/doc/latex/ellipsis
%doc %{texmfdist}/doc/latex/elpres
%doc %{texmfdist}/doc/latex/elsevier
%doc %{texmfdist}/doc/latex/em
%doc %{texmfdist}/doc/latex/emp
%doc %{texmfdist}/doc/latex/emulateapj
%doc %{texmfdist}/doc/latex/endheads
%doc %{texmfdist}/doc/latex/engpron
%doc %{texmfdist}/doc/latex/engrec
%doc %{texmfdist}/doc/latex/envlab
%doc %{texmfdist}/doc/latex/epigraph
%doc %{texmfdist}/doc/latex/epiolmec
%doc %{texmfdist}/doc/latex/epsdice
%doc %{texmfdist}/doc/latex/epspdfconversion
%doc %{texmfdist}/doc/latex/eqparbox
%doc %{texmfdist}/doc/latex/errata
%doc %{texmfdist}/doc/latex/eskdx
%doc %{texmfdist}/doc/latex/etex-pkg
%doc %{texmfdist}/doc/latex/ethiop-t1
%doc %{texmfdist}/doc/latex/ethiop
%doc %{texmfdist}/doc/latex/etoolbox
%doc %{texmfdist}/doc/latex/eukdate
%doc %{texmfdist}/doc/latex/euproposal
%doc %{texmfdist}/doc/latex/euro
%doc %{texmfdist}/doc/latex/europecv
%doc %{texmfdist}/doc/latex/eurosans
%doc %{texmfdist}/doc/latex/everypage
%doc %{texmfdist}/doc/latex/examplep
%doc %{texmfdist}/doc/latex/exceltex
%doc %{texmfdist}/doc/latex/exercise
%doc %{texmfdist}/doc/latex/expl3
%doc %{texmfdist}/doc/latex/extarrows
%doc %{texmfdist}/doc/latex/extract
%doc %{texmfdist}/doc/latex/facsimile
%doc %{texmfdist}/doc/latex/fancynum
%doc %{texmfdist}/doc/latex/fancyref
%doc %{texmfdist}/doc/latex/fancytooltips
%doc %{texmfdist}/doc/latex/fax
%doc %{texmfdist}/doc/latex/figbib
%doc %{texmfdist}/doc/latex/figsize
%doc %{texmfdist}/doc/latex/fink
%doc %{texmfdist}/doc/latex/fixfoot
%doc %{texmfdist}/doc/latex/flabels
%doc %{texmfdist}/doc/latex/flacards
%doc %{texmfdist}/doc/latex/flagderiv
%doc %{texmfdist}/doc/latex/flashcards
%doc %{texmfdist}/doc/latex/floatrow
%doc %{texmfdist}/doc/latex/fmp
%doc %{texmfdist}/doc/latex/fnbreak
%doc %{texmfdist}/doc/latex/fncychap
%doc %{texmfdist}/doc/latex/foekfont
%doc %{texmfdist}/doc/latex/fonttable
%doc %{texmfdist}/doc/latex/frankenstein
%doc %{texmfdist}/doc/latex/frenchle
%doc %{texmfdist}/doc/latex/fribrief
%doc %{texmfdist}/doc/latex/frletter
%doc %{texmfdist}/doc/latex/frontespizio
%doc %{texmfdist}/doc/latex/fullblck
%doc %{texmfdist}/doc/latex/fullpict
%doc %{texmfdist}/doc/latex/fundus
%doc %{texmfdist}/doc/latex/gaceta
%doc %{texmfdist}/doc/latex/gastex
%doc %{texmfdist}/doc/latex/gatech-thesis
%doc %{texmfdist}/doc/latex/gauss
%doc %{texmfdist}/doc/latex/gb4e
%doc %{texmfdist}/doc/latex/gcard
%doc %{texmfdist}/doc/latex/gcite
%doc %{texmfdist}/doc/latex/genmpage
%doc %{texmfdist}/doc/latex/geomsty
%doc %{texmfdist}/doc/latex/gloss
%doc %{texmfdist}/doc/latex/glossaries
%doc %{texmfdist}/doc/latex/gmdoc
%doc %{texmfdist}/doc/latex/gmeometric
%doc %{texmfdist}/doc/latex/gmiflink
%doc %{texmfdist}/doc/latex/gmutils
%doc %{texmfdist}/doc/latex/gmverb
%doc %{texmfdist}/doc/latex/graphicx-psmin
%doc %{texmfdist}/doc/latex/greek-inputenc
%doc %{texmfdist}/doc/latex/greekdates
%doc %{texmfdist}/doc/latex/greektex
%doc %{texmfdist}/doc/latex/grfpaste
%doc %{texmfdist}/doc/latex/grnumalt
%doc %{texmfdist}/doc/latex/grverb
%doc %{texmfdist}/doc/latex/gu
%doc %{texmfdist}/doc/latex/guitbeamer
%doc %{texmfdist}/doc/latex/hanging
%doc %{texmfdist}/doc/latex/har2nat
%doc %{texmfdist}/doc/latex/harmony
%doc %{texmfdist}/doc/latex/harpoon
%doc %{texmfdist}/doc/latex/harvard
%doc %{texmfdist}/doc/latex/hc
%doc %{texmfdist}/doc/latex/hep
%doc %{texmfdist}/doc/latex/hepnames
%doc %{texmfdist}/doc/latex/hepparticles
%doc %{texmfdist}/doc/latex/hepthesis
%doc %{texmfdist}/doc/latex/hepunits
%doc %{texmfdist}/doc/latex/hexgame
%doc %{texmfdist}/doc/latex/histogr
%doc %{texmfdist}/doc/latex/hitec
%doc %{texmfdist}/doc/latex/hpsdiss
%doc %{texmfdist}/doc/latex/hvfloat
%doc %{texmfdist}/doc/latex/hypdvips
%doc %{texmfdist}/doc/latex/hyperref-docsrc
%doc %{texmfdist}/doc/latex/hyperxmp
%doc %{texmfdist}/doc/latex/ibycus-babel
%doc %{texmfdist}/doc/latex/icsv
%doc %{texmfdist}/doc/latex/ieeepes
%doc %{texmfdist}/doc/latex/ifmslide
%doc %{texmfdist}/doc/latex/ifplatform
%doc %{texmfdist}/doc/latex/ijmart
%doc %{texmfdist}/doc/latex/imac
%doc %{texmfdist}/doc/latex/image-gallery
%doc %{texmfdist}/doc/latex/imtekda
%doc %{texmfdist}/doc/latex/inlinebib
%doc %{texmfdist}/doc/latex/inlinedef
%doc %{texmfdist}/doc/latex/interactiveworkbook
%doc %{texmfdist}/doc/latex/invoice
%doc %{texmfdist}/doc/latex/ipa
%doc %{texmfdist}/doc/latex/iso
%doc %{texmfdist}/doc/latex/iso10303
%doc %{texmfdist}/doc/latex/isodate
%doc %{texmfdist}/doc/latex/isodoc
%doc %{texmfdist}/doc/latex/itnumpar
%doc %{texmfdist}/doc/latex/jknapltx
%doc %{texmfdist}/doc/latex/jneurosci
%doc %{texmfdist}/doc/latex/jpsj
%doc %{texmfdist}/doc/latex/jura
%doc %{texmfdist}/doc/latex/juraabbrev
%doc %{texmfdist}/doc/latex/juramisc
%doc %{texmfdist}/doc/latex/jurarsp
%doc %{texmfdist}/doc/latex/karnaugh
%doc %{texmfdist}/doc/latex/kerkis
%doc %{texmfdist}/doc/latex/kerntest
%doc %{texmfdist}/doc/latex/kluwer
%doc %{texmfdist}/doc/latex/lazylist
%doc %{texmfdist}/doc/latex/lcyw
%doc %{texmfdist}/doc/latex/ledmac
%doc %{texmfdist}/doc/latex/lgreek
%doc %{texmfdist}/doc/latex/lhelp
%doc %{texmfdist}/doc/latex/linguex
%doc %{texmfdist}/doc/latex/lipsum
%doc %{texmfdist}/doc/latex/listbib
%doc %{texmfdist}/doc/latex/lkproof
%doc %{texmfdist}/doc/latex/logic
%doc %{texmfdist}/doc/latex/ltxindex
%doc %{texmfdist}/doc/latex/mafr
%doc %{texmfdist}/doc/latex/magyar
%doc %{texmfdist}/doc/latex/mailing
%doc %{texmfdist}/doc/latex/makebarcode
%doc %{texmfdist}/doc/latex/makedtx
%doc %{texmfdist}/doc/latex/makeglos
%doc %{texmfdist}/doc/latex/mathdesign
%doc %{texmfdist}/doc/latex/mathpazo
%doc %{texmfdist}/doc/latex/mceinleger
%doc %{texmfdist}/doc/latex/memexsupp
%doc %{texmfdist}/doc/latex/metaplot
%doc %{texmfdist}/doc/latex/mff
%doc %{texmfdist}/doc/latex/mftinc
%doc %{texmfdist}/doc/latex/minutes
%doc %{texmfdist}/doc/latex/mmap
%doc %{texmfdist}/doc/latex/mnsymbol
%doc %{texmfdist}/doc/latex/moderncv
%doc %{texmfdist}/doc/latex/modroman
%doc %{texmfdist}/doc/latex/mongolian-babel
%doc %{texmfdist}/doc/latex/montex
%doc %{texmfdist}/doc/latex/moresize
%doc %{texmfdist}/doc/latex/msg
%doc %{texmfdist}/doc/latex/mslapa
%doc %{texmfdist}/doc/latex/mtgreek
%doc %{texmfdist}/doc/latex/multibbl
%doc %{texmfdist}/doc/latex/multirow
%doc %{texmfdist}/doc/latex/munich
%doc %{texmfdist}/doc/latex/muthesis
%doc %{texmfdist}/doc/latex/mxd
%doc %{texmfdist}/doc/latex/mxedruli
%doc %{texmfdist}/doc/latex/ncclatex
%doc %{texmfdist}/doc/latex/ncctools
%doc %{texmfdist}/doc/latex/nddiss
%doc %{texmfdist}/doc/latex/newalg
%doc %{texmfdist}/doc/latex/newfile
%doc %{texmfdist}/doc/latex/newlfm
%doc %{texmfdist}/doc/latex/newspaper
%doc %{texmfdist}/doc/latex/nomentbl
%doc %{texmfdist}/doc/latex/nonfloat
%doc %{texmfdist}/doc/latex/numname
%doc %{texmfdist}/doc/latex/ocr-latex
%doc %{texmfdist}/doc/latex/ogham
%doc %{texmfdist}/doc/latex/ogonek
%doc %{texmfdist}/doc/latex/opcit
%doc %{texmfdist}/doc/latex/ordinalpt
%doc %{texmfdist}/doc/latex/otibet
%doc %{texmfdist}/doc/latex/outline
%doc %{texmfdist}/doc/latex/outliner
%doc %{texmfdist}/doc/latex/pagenote
%doc %{texmfdist}/doc/latex/papercdcase
%doc %{texmfdist}/doc/latex/paresse
%doc %{texmfdist}/doc/latex/parrun
%doc %{texmfdist}/doc/latex/pauldoc
%doc %{texmfdist}/doc/latex/pdfwin
%doc %{texmfdist}/doc/latex/pecha
%doc %{texmfdist}/doc/latex/perception
%doc %{texmfdist}/doc/latex/perltex
%doc %{texmfdist}/doc/latex/pgf-soroban
%doc %{texmfdist}/doc/latex/pgfopts
%doc %{texmfdist}/doc/latex/philex
%doc %{texmfdist}/doc/latex/plates
%doc %{texmfdist}/doc/latex/plweb
%doc %{texmfdist}/doc/latex/pmgraph
%doc %{texmfdist}/doc/latex/polski
%doc %{texmfdist}/doc/latex/polyglot
%doc %{texmfdist}/doc/latex/postcards
%doc %{texmfdist}/doc/latex/prettyref
%doc %{texmfdist}/doc/latex/proba
%doc %{texmfdist}/doc/latex/procIAGssymp
%doc %{texmfdist}/doc/latex/protex
%doc %{texmfdist}/doc/latex/protocol
%doc %{texmfdist}/doc/latex/psfragx
%doc %{texmfdist}/doc/latex/psgo
%doc %{texmfdist}/doc/latex/pspicture
%doc %{texmfdist}/doc/latex/pst2pdf
%doc %{texmfdist}/doc/latex/qobitree
%doc %{texmfdist}/doc/latex/qstest
%doc %{texmfdist}/doc/latex/quotmark
%doc %{texmfdist}/doc/latex/r_und_s
%doc %{texmfdist}/doc/latex/randbild
%doc %{texmfdist}/doc/latex/rcs
%doc %{texmfdist}/doc/latex/rcsinfo
%doc %{texmfdist}/doc/latex/rectopma
%doc %{texmfdist}/doc/latex/refcheck
%doc %{texmfdist}/doc/latex/refstyle
%doc %{texmfdist}/doc/latex/relenc
%doc %{texmfdist}/doc/latex/repeatindex
%doc %{texmfdist}/doc/latex/rlepsf
%doc %{texmfdist}/doc/latex/rmpage
%doc %{texmfdist}/doc/latex/robustindex
%doc %{texmfdist}/doc/latex/rst
%doc %{texmfdist}/doc/latex/rtkinenc
%doc %{texmfdist}/doc/latex/rtklage
%doc %{texmfdist}/doc/latex/sagetex
%doc %{texmfdist}/doc/latex/sanskrit
%doc %{texmfdist}/doc/latex/sauerj
%doc %{texmfdist}/doc/latex/sauterfonts
%doc %{texmfdist}/doc/latex/savefnmark
%doc %{texmfdist}/doc/latex/savetrees
%doc %{texmfdist}/doc/latex/scalebar
%doc %{texmfdist}/doc/latex/scientificpaper
%doc %{texmfdist}/doc/latex/sciwordconv
%doc %{texmfdist}/doc/latex/semioneside
%doc %{texmfdist}/doc/latex/seqsplit
%doc %{texmfdist}/doc/latex/sf298
%doc %{texmfdist}/doc/latex/sffms
%doc %{texmfdist}/doc/latex/sfg
%doc %{texmfdist}/doc/latex/shorttoc
%doc %{texmfdist}/doc/latex/show2e
%doc %{texmfdist}/doc/latex/showexpl
%doc %{texmfdist}/doc/latex/slantsc
%doc %{texmfdist}/doc/latex/smalltableof
%doc %{texmfdist}/doc/latex/smartref
%doc %{texmfdist}/doc/latex/smflatex
%doc %{texmfdist}/doc/latex/snapshot
%doc %{texmfdist}/doc/latex/sort-by-letters
%doc %{texmfdist}/doc/latex/soyombo
%doc %{texmfdist}/doc/latex/sparklines
%doc %{texmfdist}/doc/latex/spie
%doc %{texmfdist}/doc/latex/splitbib
%doc %{texmfdist}/doc/latex/spotcolor
%doc %{texmfdist}/doc/latex/sprite
%doc %{texmfdist}/doc/latex/srcltx
%doc %{texmfdist}/doc/latex/ssqquote
%doc %{texmfdist}/doc/latex/statistik
%doc %{texmfdist}/doc/latex/stdpage
%doc %{texmfdist}/doc/latex/stellenbosch
%doc %{texmfdist}/doc/latex/stex
%doc %{texmfdist}/doc/latex/struktex
%doc %{texmfdist}/doc/latex/sttools
%doc %{texmfdist}/doc/latex/stubs
%doc %{texmfdist}/doc/latex/sugconf
%doc %{texmfdist}/doc/latex/supertabular
%doc %{texmfdist}/doc/latex/svgcolor
%doc %{texmfdist}/doc/latex/svn-multi
%doc %{texmfdist}/doc/latex/svn
%doc %{texmfdist}/doc/latex/svninfo
%doc %{texmfdist}/doc/latex/swebib
%doc %{texmfdist}/doc/latex/swimgraf
%doc %{texmfdist}/doc/latex/synproof
%doc %{texmfdist}/doc/latex/syntax
%doc %{texmfdist}/doc/latex/syntrace
%doc %{texmfdist}/doc/latex/synttree
%doc %{texmfdist}/doc/latex/t-angles
%doc %{texmfdist}/doc/latex/tableaux
%doc %{texmfdist}/doc/latex/tablists
%doc %{texmfdist}/doc/latex/tablor
%doc %{texmfdist}/doc/latex/tabto-ltx
%doc %{texmfdist}/doc/latex/tabulary
%doc %{texmfdist}/doc/latex/tabvar
%doc %{texmfdist}/doc/latex/talk
%doc %{texmfdist}/doc/latex/tapir
%doc %{texmfdist}/doc/latex/tcldoc
%doc %{texmfdist}/doc/latex/tdsfrmath
%doc %{texmfdist}/doc/latex/technics
%doc %{texmfdist}/doc/latex/ted
%doc %{texmfdist}/doc/latex/tengwarscript
%doc %{texmfdist}/doc/latex/tensor
%doc %{texmfdist}/doc/latex/teubner
%doc %{texmfdist}/doc/latex/texmate
%doc %{texmfdist}/doc/latex/texpower
%doc %{texmfdist}/doc/latex/texshade
%doc %{texmfdist}/doc/latex/textcase
%doc %{texmfdist}/doc/latex/textopo
%doc %{texmfdist}/doc/latex/theoremref
%doc %{texmfdist}/doc/latex/thesis-titlepage-fhac
%doc %{texmfdist}/doc/latex/thinsp
%doc %{texmfdist}/doc/latex/thmtools
%doc %{texmfdist}/doc/latex/thumb
%doc %{texmfdist}/doc/latex/thuthesis
%doc %{texmfdist}/doc/latex/ticket
%doc %{texmfdist}/doc/latex/tikz-inet
%doc %{texmfdist}/doc/latex/timesht
%doc %{texmfdist}/doc/latex/titling
%doc %{texmfdist}/doc/latex/tocvsec2
%doc %{texmfdist}/doc/latex/tokenizer
%doc %{texmfdist}/doc/latex/toolbox
%doc %{texmfdist}/doc/latex/toptesi
%doc %{texmfdist}/doc/latex/trajan
%doc %{texmfdist}/doc/latex/translator
%doc %{texmfdist}/doc/latex/trivfloat
%doc %{texmfdist}/doc/latex/turnstile
%doc %{texmfdist}/doc/latex/twoup
%doc %{texmfdist}/doc/latex/typogrid
%doc %{texmfdist}/doc/latex/umlaute
%doc %{texmfdist}/doc/latex/undertilde
%doc %{texmfdist}/doc/latex/unitsdef
%doc %{texmfdist}/doc/latex/unroman
%doc %{texmfdist}/doc/latex/upmethodology
%doc %{texmfdist}/doc/latex/urlbst
%doc %{texmfdist}/doc/latex/varindex
%doc %{texmfdist}/doc/latex/varsfromjobname
%doc %{texmfdist}/doc/latex/vector
%doc %{texmfdist}/doc/latex/verse
%doc %{texmfdist}/doc/latex/vhistory
%doc %{texmfdist}/doc/latex/vita
%doc %{texmfdist}/doc/latex/volumes
%doc %{texmfdist}/doc/latex/vpe
%doc %{texmfdist}/doc/latex/vrsion
%doc %{texmfdist}/doc/latex/vwcol
%doc %{texmfdist}/doc/latex/vxu
%doc %{texmfdist}/doc/latex/wadalab
%doc %{texmfdist}/doc/latex/wallpaper
%doc %{texmfdist}/doc/latex/warpcol
%doc %{texmfdist}/doc/latex/wnri
%doc %{texmfdist}/doc/latex/wordlike
%doc %{texmfdist}/doc/latex/xargs
%doc %{texmfdist}/doc/latex/xdoc
%doc %{texmfdist}/doc/latex/xfor
%doc %{texmfdist}/doc/latex/xifthen
%doc %{texmfdist}/doc/latex/xmpincl
%doc %{texmfdist}/doc/latex/xnewcommand
%doc %{texmfdist}/doc/latex/xoptarg
%doc %{texmfdist}/doc/latex/xpackages
%doc %{texmfdist}/doc/latex/xskak
%doc %{texmfdist}/doc/latex/xstring
%doc %{texmfdist}/doc/latex/xtcapts
%doc %{texmfdist}/doc/latex/xyling
%doc %{texmfdist}/doc/latex/xytree
%doc %{texmfdist}/doc/latex/yafoot
%doc %{texmfdist}/doc/latex/yhmath
%doc %{texmfdist}/doc/latex/york-thesis
%doc %{texmfdist}/doc/latex/yplan
%doc %{texmfdist}/doc/latex/zed-csp
%doc %{texmfdist}/doc/latex/zefonts
%doc %{texmfdist}/doc/latex/ziffer
%doc %{texmfdist}/doc/latex/zwgetfdate

%files latex-math-sources
%defattr(644,root,root,755)
%{texmfdist}/source/latex/bez123
%{texmfdist}/source/latex/binomexp
%{texmfdist}/source/latex/cmll
%{texmfdist}/source/latex/constants
%{texmfdist}/source/latex/coordsys
%{texmfdist}/source/latex/dotseqn
%{texmfdist}/source/latex/egplot
%{texmfdist}/source/latex/eqlist
%{texmfdist}/source/latex/eqnarray
%{texmfdist}/source/latex/esdiff
%{texmfdist}/source/latex/esvect
%{texmfdist}/source/latex/extpfeil
%{texmfdist}/source/latex/fouridx
%{texmfdist}/source/latex/functan
%{texmfdist}/source/latex/galois
%{texmfdist}/source/latex/gnuplottex
%{texmfdist}/source/latex/hhtensor
%{texmfdist}/source/latex/logpap
%{texmfdist}/source/latex/noitcrul
%{texmfdist}/source/latex/permute
%{texmfdist}/source/latex/qsymbols
%{texmfdist}/source/latex/subdepth
%{texmfdist}/source/latex/faktor
%{texmfdist}/source/latex/sseq
%{texmfdist}/source/latex/trsym
%{texmfdist}/source/latex/petri-nets
%{texmfdist}/source/latex/mlist
%{texmfdist}/source/latex/numprint

%files latex-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eco
%doc %{texmfdist}/doc/latex/bez123
%doc %{texmfdist}/doc/latex/binomexp
%doc %{texmfdist}/doc/latex/cmll
%doc %{texmfdist}/doc/latex/constants
%doc %{texmfdist}/doc/latex/coordsys
%doc %{texmfdist}/doc/latex/egplot
%doc %{texmfdist}/doc/latex/eqlist
%doc %{texmfdist}/doc/latex/eqnarray
%doc %{texmfdist}/doc/latex/esdiff
%doc %{texmfdist}/doc/latex/esvect
%doc %{texmfdist}/doc/latex/extpfeil
%doc %{texmfdist}/doc/latex/faktor
%doc %{texmfdist}/doc/latex/fouridx
%doc %{texmfdist}/doc/latex/functan
%doc %{texmfdist}/doc/latex/galois
%doc %{texmfdist}/doc/latex/gnuplottex
%doc %{texmfdist}/doc/latex/hhtensor
%doc %{texmfdist}/doc/latex/logpap
%doc %{texmfdist}/doc/latex/makeplot
%doc %{texmfdist}/doc/latex/maybemath
%doc %{texmfdist}/doc/latex/mfpic4ode
%doc %{texmfdist}/doc/latex/mhequ
%doc %{texmfdist}/doc/latex/mlist
%doc %{texmfdist}/doc/latex/nath
%doc %{texmfdist}/doc/latex/noitcrul
%doc %{texmfdist}/doc/latex/numprint
%doc %{texmfdist}/doc/latex/permute
%doc %{texmfdist}/doc/latex/petri-nets
%doc %{texmfdist}/doc/latex/qsymbols
%doc %{texmfdist}/doc/latex/qtree
%doc %{texmfdist}/doc/latex/sdrt
%doc %{texmfdist}/doc/latex/semantic
%doc %{texmfdist}/doc/latex/simplewick
%doc %{texmfdist}/doc/latex/sseq
%doc %{texmfdist}/doc/latex/subdepth
%doc %{texmfdist}/doc/latex/subeqn
%doc %{texmfdist}/doc/latex/subeqnarray
%doc %{texmfdist}/doc/latex/trfsigns
%doc %{texmfdist}/doc/latex/trsym
%doc %{texmfdist}/doc/latex/ulsy
%{texmfdist}/fonts/map/dvips/cmll
%{texmfdist}/fonts/map/dvips/esvect
%{texmfdist}/fonts/source/public/cmll
%{texmfdist}/fonts/source/public/esvect
%{texmfdist}/fonts/source/public/trsym
%{texmfdist}/fonts/source/public/ulsy
%{texmfdist}/fonts/tfm/public/cmll
%{texmfdist}/fonts/tfm/public/eco
%{texmfdist}/fonts/tfm/public/esvect
%{texmfdist}/fonts/tfm/public/trsym
%{texmfdist}/fonts/tfm/public/ulsy
%{texmfdist}/fonts/type1/public/cmll
%{texmfdist}/fonts/type1/public/esvect
%{texmfdist}/fonts/vf/public/eco
%{texmfdist}/source/fonts/eco
%{texmfdist}/source/latex/makeplot
%{texmfdist}/source/latex/mfpic4ode
%{texmfdist}/source/latex/semantic
%{texmfdist}/source/latex/simplewick
%{texmfdist}/source/latex/subeqn
%{texmfdist}/source/latex/subeqnarray
%{texmfdist}/source/latex/trfsigns
%{texmfdist}/source/latex/ulsy
%{texmfdist}/tex/latex/bez123
%{texmfdist}/tex/latex/binomexp
%{texmfdist}/tex/latex/cmll
%{texmfdist}/tex/latex/constants
%{texmfdist}/tex/latex/coordsys
%{texmfdist}/tex/latex/dotseqn
%{texmfdist}/tex/latex/egplot
%{texmfdist}/tex/latex/eqlist
%{texmfdist}/tex/latex/eqnarray
%{texmfdist}/tex/latex/esdiff
%{texmfdist}/tex/latex/esvect
%{texmfdist}/tex/latex/extpfeil
%{texmfdist}/tex/latex/faktor
%{texmfdist}/tex/latex/fouridx
%{texmfdist}/tex/latex/functan
%{texmfdist}/tex/latex/galois
%{texmfdist}/tex/latex/gnuplottex
%{texmfdist}/tex/latex/hhtensor
%{texmfdist}/tex/latex/logpap
%{texmfdist}/tex/latex/makeplot
%{texmfdist}/tex/latex/maybemath
%{texmfdist}/tex/latex/mfpic4ode
%{texmfdist}/tex/latex/mhequ
%{texmfdist}/tex/latex/mhs
%{texmfdist}/tex/latex/mlist
%{texmfdist}/tex/latex/nath
%{texmfdist}/tex/latex/noitcrul
%{texmfdist}/tex/latex/numprint
%{texmfdist}/tex/latex/permute
%{texmfdist}/tex/latex/petri-nets
%{texmfdist}/tex/latex/qsymbols
%{texmfdist}/tex/latex/qtree
%{texmfdist}/tex/latex/sdrt
%{texmfdist}/tex/latex/semantic
%{texmfdist}/tex/latex/sfmath
%{texmfdist}/tex/latex/simplewick
%{texmfdist}/tex/latex/sseq
%{texmfdist}/tex/latex/subdepth
%{texmfdist}/tex/latex/subeqn
%{texmfdist}/tex/latex/subeqnarray
%{texmfdist}/tex/latex/trfsigns
%{texmfdist}/tex/latex/trsym
%{texmfdist}/tex/latex/ulsy
%doc %{texmfdist}/doc/latex/tree-dvips
%{texmfdist}/source/latex/tree-dvips
%{texmfdist}/tex/latex/tree-dvips

%files latex-physics
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/circ
%doc %{texmfdist}/doc/latex/colorwav
%doc %{texmfdist}/doc/latex/dyntree
%doc %{texmfdist}/doc/latex/feynmf
%doc %{texmfdist}/doc/latex/formula
%doc %{texmfdist}/doc/latex/listofsymbols
%doc %{texmfdist}/doc/latex/miller
%doc %{texmfdist}/doc/latex/susy
%{texmfdist}/metapost/feynmf
%{texmfdist}/source/latex/circ
%{texmfdist}/source/latex/colorwav
%{texmfdist}/source/latex/dyntree
%{texmfdist}/source/latex/feynmf
%{texmfdist}/source/latex/formula
%{texmfdist}/source/latex/isotope
%{texmfdist}/source/latex/miller
%{texmfdist}/tex/latex/circ
%{texmfdist}/tex/latex/colorwav
%{texmfdist}/tex/latex/dyntree
%{texmfdist}/tex/latex/feynmf
%{texmfdist}/tex/latex/formula
%{texmfdist}/tex/latex/isotope
%{texmfdist}/tex/latex/listofsymbols
%{texmfdist}/tex/latex/miller
%{texmfdist}/tex/latex/susy
%{texmfdist}/fonts/source/public/circ
%{texmfdist}/fonts/tfm/public/circ

%files latex-chem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/achemso
%doc %{texmfdist}/doc/latex/bpchem
%doc %{texmfdist}/doc/latex/chemstyle
%doc %{texmfdist}/doc/latex/mhchem
%doc %{texmfdist}/doc/fonts/chemarrow
%doc %{texmfdist}/doc/latex/chemcompounds
%doc %{texmfdist}/doc/latex/chemcono
%{texmfdist}/fonts/afm/public/chemarrow
%{texmfdist}/fonts/map/dvips/chemarrow
%{texmfdist}/fonts/source/public/chemarrow
%{texmfdist}/fonts/tfm/public/chemarrow
%{texmfdist}/fonts/type1/public/chemarrow
%{texmfdist}/source/latex/achemso
%{texmfdist}/source/latex/bpchem
%{texmfdist}/source/latex/chemcompounds
%{texmfdist}/source/latex/chemstyle
%{texmfdist}/tex/latex/achemso
%{texmfdist}/tex/latex/bpchem
%{texmfdist}/tex/latex/chemarrow
%{texmfdist}/tex/latex/chemcompounds
%{texmfdist}/tex/latex/chemcono
%{texmfdist}/tex/latex/chemstyle
%{texmfdist}/tex/latex/mhchem

%files latex-biology
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/biocon
%doc %{texmfdist}/doc/latex/dnaseq
%{texmfdist}/bibtex/bib/biocon
%{texmfdist}/source/latex/biocon
%{texmfdist}/source/latex/dnaseq
%{texmfdist}/tex/latex/biocon
%{texmfdist}/tex/latex/dnaseq

%files latex-pdftools
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/attachfile
%doc %{texmfdist}/doc/latex/cooltooltips
%doc %{texmfdist}/doc/latex/movie15
%doc %{texmfdist}/doc/latex/pdfcprot
%doc %{texmfdist}/doc/latex/pdfscreen
%doc %{texmfdist}/doc/latex/pdfsync
%doc %{texmfdist}/doc/latex/pdftricks
%{texmfdist}/source/latex/attachfile
%{texmfdist}/source/latex/cooltooltips
%{texmfdist}/source/latex/pdfcprot
%{texmfdist}/tex/latex/attachfile
%{texmfdist}/tex/latex/cooltooltips
%{texmfdist}/tex/latex/movie15
%{texmfdist}/tex/latex/pdfcprot
%{texmfdist}/tex/latex/pdfscreen
%{texmfdist}/tex/latex/pdfsync
%{texmfdist}/tex/latex/pdftricks

%files latex-informatic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/alg
%doc %{texmfdist}/doc/latex/bytefield
%doc %{texmfdist}/doc/latex/lsc
%doc %{texmfdist}/doc/latex/method
%doc %{texmfdist}/doc/latex/msc
%doc %{texmfdist}/doc/latex/progkeys
%doc %{texmfdist}/doc/latex/register
%doc %{texmfdist}/doc/latex/uml
%{texmfdist}/source/latex/alg
%{texmfdist}/source/latex/bytefield
%{texmfdist}/source/latex/method
%{texmfdist}/source/latex/progkeys
%{texmfdist}/source/latex/register
%{texmfdist}/source/latex/uml
%{texmfdist}/tex/latex/alg
%{texmfdist}/tex/latex/bytefield
%{texmfdist}/tex/latex/lsc
%{texmfdist}/tex/latex/method
%{texmfdist}/tex/latex/msc
%{texmfdist}/tex/latex/progkeys
%{texmfdist}/tex/latex/register
%{texmfdist}/tex/latex/uml

%files latex-games
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/backgammon
%doc %{texmfdist}/doc/latex/chessboard
%doc %{texmfdist}/doc/latex/chessfss
%doc %{texmfdist}/doc/latex/crosswrd
%doc %{texmfdist}/doc/latex/cwpuzzle
%doc %{texmfdist}/doc/latex/jeopardy
%doc %{texmfdist}/doc/latex/othello
%doc %{texmfdist}/doc/latex/sgame
%doc %{texmfdist}/doc/latex/skak
%doc %{texmfdist}/doc/latex/sudoku
%doc %{texmfdist}/doc/latex/sudokubundle
%{texmfdist}/fonts/enc/dvips/chessfss
%{texmfdist}/fonts/map/dvips/skak
%{texmfdist}/fonts/source/public/backgammon
%{texmfdist}/fonts/source/public/cchess
%{texmfdist}/fonts/source/public/chess
%{texmfdist}/fonts/source/public/go
%{texmfdist}/fonts/source/public/othello
%{texmfdist}/fonts/source/public/skak
%{texmfdist}/fonts/tfm/public/backgammon
%{texmfdist}/fonts/tfm/public/cchess
%{texmfdist}/fonts/tfm/public/go
%{texmfdist}/fonts/tfm/public/othello
%{texmfdist}/fonts/tfm/public/skak
%{texmfdist}/source/latex/backgammon
%{texmfdist}/source/latex/chessboard
%{texmfdist}/source/latex/chessfss
%{texmfdist}/source/latex/crosswrd
%{texmfdist}/source/latex/cwpuzzle
%{texmfdist}/source/latex/go
%{texmfdist}/source/latex/jeopardy
%{texmfdist}/source/latex/othello
%{texmfdist}/source/latex/sudoku
%{texmfdist}/source/latex/sudokubundle
%{texmfdist}/tex/latex/backgammon
%{texmfdist}/tex/latex/cchess
%{texmfdist}/tex/latex/chess
%{texmfdist}/tex/latex/chessboard
%{texmfdist}/tex/latex/chessfss
%{texmfdist}/tex/latex/crosswrd
%{texmfdist}/tex/latex/cwpuzzle
%{texmfdist}/tex/latex/go
%{texmfdist}/tex/latex/jeopardy
%{texmfdist}/tex/latex/othello
%{texmfdist}/tex/latex/sgame
%{texmfdist}/tex/latex/skak
%{texmfdist}/tex/latex/sudoku
%{texmfdist}/tex/latex/sudokubundle

%files latex-sources
%defattr(644,root,root,755)
%{texmfdist}/source/latex/acronym
%{texmfdist}/source/latex/adrlist
%{texmfdist}/source/latex/altfont
%{texmfdist}/source/latex/answers
%{texmfdist}/source/latex/ascii
%{texmfdist}/source/latex/augie
%{texmfdist}/source/latex/barcodes
%{texmfdist}/source/latex/bbding
%{texmfdist}/source/latex/bbm-macros
%{texmfdist}/source/latex/bengali
%{texmfdist}/source/latex/beton
%{texmfdist}/source/latex/bibarts
%{texmfdist}/source/latex/bibleref
%{texmfdist}/source/latex/biblist
%{texmfdist}/source/latex/bigfoot
%{texmfdist}/source/latex/bizcard
%{texmfdist}/source/latex/blindtext
%{texmfdist}/source/latex/bookhands
%{texmfdist}/source/latex/bophook
%{texmfdist}/source/latex/boxhandler
%{texmfdist}/source/latex/braille
%{texmfdist}/source/latex/breakurl
%{texmfdist}/source/latex/brushscr
%{texmfdist}/source/latex/burmese
%{texmfdist}/source/latex/captcont
%{texmfdist}/source/latex/catechis
%{texmfdist}/source/latex/cclicenses
%{texmfdist}/source/latex/cd
%{texmfdist}/source/latex/cd-cover
%{texmfdist}/source/latex/cdpbundl
%{texmfdist}/source/latex/changes
%{texmfdist}/source/latex/chapterfolder
%{texmfdist}/source/latex/cleveref
%{texmfdist}/source/latex/cmcyralt
%{texmfdist}/source/latex/cmsd
%{texmfdist}/source/latex/codepage
%{texmfdist}/source/latex/confproc
%{texmfdist}/source/latex/coverpage
%{texmfdist}/source/latex/crop
%{texmfdist}/source/latex/crossreference
%{texmfdist}/source/latex/ctib
%{texmfdist}/source/latex/cweb-latex
%{texmfdist}/source/latex/dateiliste
%{texmfdist}/source/latex/datetime
%{texmfdist}/source/latex/decimal
%{texmfdist}/source/latex/diagnose
%{texmfdist}/source/latex/docmfp
%{texmfdist}/source/latex/doipubmed
%{texmfdist}/source/latex/dotarrow
%{texmfdist}/source/latex/dottex
%{texmfdist}/source/latex/drac
%{texmfdist}/source/latex/draftcopy
%{texmfdist}/source/latex/dramatist
%{texmfdist}/source/latex/eCards
%{texmfdist}/source/latex/ebezier
%{texmfdist}/source/latex/ebsthesis
%{texmfdist}/source/latex/ecclesiastic
%{texmfdist}/source/latex/edmargin
%{texmfdist}/source/latex/eemeir
%{texmfdist}/source/latex/eiad
%{texmfdist}/source/latex/ellipsis
%{texmfdist}/source/latex/em
%{texmfdist}/source/latex/emp
%{texmfdist}/source/latex/endfloat
%{texmfdist}/source/latex/endheads
%{texmfdist}/source/latex/engpron
%{texmfdist}/source/latex/engrec
%{texmfdist}/source/latex/envlab
%{texmfdist}/source/latex/epigraph
%{texmfdist}/source/latex/epiolmec
%{texmfdist}/source/latex/epsdice
%{texmfdist}/source/latex/eqparbox
%{texmfdist}/source/latex/errata
%{texmfdist}/source/latex/eso-pic
%{texmfdist}/source/latex/ethiop
%{texmfdist}/source/latex/eukdate
%{texmfdist}/source/latex/euproposal
%{texmfdist}/source/latex/euro
%{texmfdist}/source/latex/everypage
%{texmfdist}/source/latex/exercise
%{texmfdist}/source/latex/expl3
%{texmfdist}/source/latex/extract
%{texmfdist}/source/latex/facsimile
%{texmfdist}/source/latex/fancynum
%{texmfdist}/source/latex/fancyref
%{texmfdist}/source/latex/fancytooltips
%{texmfdist}/source/latex/fancyvrb
%{texmfdist}/source/latex/figsize
%{texmfdist}/source/latex/filecontents
%{texmfdist}/source/latex/fink
%{texmfdist}/source/latex/flabels
%{texmfdist}/source/latex/flagderiv
%{texmfdist}/source/latex/flashcards
%{texmfdist}/source/latex/float
%{texmfdist}/source/latex/floatrow
%{texmfdist}/source/latex/fmp
%{texmfdist}/source/latex/fnbreak
%{texmfdist}/source/latex/foilhtml
%{texmfdist}/source/latex/fonttable
%{texmfdist}/source/latex/footmisc
%{texmfdist}/source/latex/footnpag
%{texmfdist}/source/latex/frankenstein
%{texmfdist}/source/latex/frontespizio
%{texmfdist}/source/latex/fullblck
%{texmfdist}/source/latex/fundus
%{texmfdist}/source/latex/gcite
%{texmfdist}/source/latex/genmpage
%{texmfdist}/source/latex/geometry
%{texmfdist}/source/latex/geomsty
%{texmfdist}/source/latex/glossaries
%{texmfdist}/source/latex/graphics
%{texmfdist}/source/latex/graphicx-psmin
%{texmfdist}/source/latex/greekdates
%{texmfdist}/source/latex/grnumalt
%{texmfdist}/source/latex/grverb
%{texmfdist}/source/latex/hanging
%{texmfdist}/source/latex/harvard
%{texmfdist}/source/latex/hc
%{texmfdist}/source/latex/hepthesis
%{texmfdist}/source/latex/hilowres
%{texmfdist}/source/latex/histogr
%{texmfdist}/source/latex/hpsdiss
%{texmfdist}/source/latex/hyper
%{texmfdist}/source/latex/hyperref
%{texmfdist}/source/latex/hyperxmp
%{texmfdist}/source/latex/hyphenat
%{texmfdist}/source/latex/ibycus-babel
%{texmfdist}/source/latex/icsv
%{texmfdist}/source/latex/ifmslide
%{texmfdist}/source/latex/ifplatform
%{texmfdist}/source/latex/ijmart
%{texmfdist}/source/latex/imtekda
%{texmfdist}/source/latex/index
%{texmfdist}/source/latex/inlinedef
%{texmfdist}/source/latex/iso
%{texmfdist}/source/latex/iso10303
%{texmfdist}/source/latex/isodate
%{texmfdist}/source/latex/isodoc
%{texmfdist}/source/latex/itnumpar
%{texmfdist}/source/latex/jura
%{texmfdist}/source/latex/juraabbrev
%{texmfdist}/source/latex/jurarsp
%{texmfdist}/source/latex/kdgreek
%{texmfdist}/source/latex/koma-script
%{texmfdist}/source/latex/labels
%{texmfdist}/source/latex/layouts
%{texmfdist}/source/latex/listings
%{texmfdist}/source/latex/localloc
%{texmfdist}/source/latex/mathcomp
%{texmfdist}/source/latex/mathpazo
%{texmfdist}/source/latex/mdwtools
%{texmfdist}/source/latex/memoir
%{texmfdist}/source/latex/mh
%{texmfdist}/source/latex/mnsymbol
%{texmfdist}/source/latex/modroman
%{texmfdist}/source/latex/mongolian-babel
%{texmfdist}/source/latex/montex
%{texmfdist}/source/latex/mparhack
%{texmfdist}/source/latex/ms
%{texmfdist}/source/latex/multibib
%{texmfdist}/source/latex/mwcls
%{texmfdist}/source/latex/natbib
%{texmfdist}/source/latex/ncctools
%{texmfdist}/source/latex/nddiss
%{texmfdist}/source/latex/newalg
%{texmfdist}/source/latex/newfile
%{texmfdist}/source/latex/newlfm
%{texmfdist}/source/latex/newspaper
%{texmfdist}/source/latex/nomencl
%{texmfdist}/source/latex/ntgclass
%{texmfdist}/source/latex/oberdiek
%{texmfdist}/source/latex/paralist
%{texmfdist}/source/latex/pdfpages
%{texmfdist}/source/latex/pict2e
%{texmfdist}/source/latex/preprint
%{texmfdist}/source/latex/preview
%{texmfdist}/source/latex/psfrag
%{texmfdist}/source/latex/pslatex
%{texmfdist}/source/latex/revtex
%{texmfdist}/source/latex/rotating
%{texmfdist}/source/latex/rotfloat
%{texmfdist}/source/latex/scale
%{texmfdist}/source/latex/sectsty
%{texmfdist}/source/latex/showlabels
%{texmfdist}/source/latex/sidecap
%{texmfdist}/source/latex/soul
%{texmfdist}/source/latex/stdclsdv
%{texmfdist}/source/latex/subfig
%{texmfdist}/source/latex/subfigure
%{texmfdist}/source/latex/supertabular
%{texmfdist}/source/latex/tablists
%{texmfdist}/source/latex/tabulary
%{texmfdist}/source/latex/tabvar
%{texmfdist}/source/latex/talk
%{texmfdist}/source/latex/tcldoc
%{texmfdist}/source/latex/tdsfrmath
%{texmfdist}/source/latex/technics
%{texmfdist}/source/latex/ted
%{texmfdist}/source/latex/tengwarscript
%{texmfdist}/source/latex/tensor
%{texmfdist}/source/latex/teubner
%{texmfdist}/source/latex/texmate
%{texmfdist}/source/latex/texpower
%{texmfdist}/source/latex/texshade
%{texmfdist}/source/latex/textcase
%{texmfdist}/source/latex/textfit
%{texmfdist}/source/latex/textopo
%{texmfdist}/source/latex/textpos
%{texmfdist}/source/latex/thesis-titlepage-fhac
%{texmfdist}/source/latex/thmtools
%{texmfdist}/source/latex/thumb
%{texmfdist}/source/latex/thuthesis
%{texmfdist}/source/latex/timesht
%{texmfdist}/source/latex/titling
%{texmfdist}/source/latex/tocbibind
%{texmfdist}/source/latex/tocloft
%{texmfdist}/source/latex/tools
%{texmfdist}/source/latex/totpages
%{texmfdist}/source/latex/type1cm
%{texmfdist}/source/latex/undertilde
%{texmfdist}/source/latex/units
%{texmfdist}/source/latex/unitsdef
%{texmfdist}/source/latex/unroman
%{texmfdist}/source/latex/upmethodology
%{texmfdist}/source/latex/urlbst
%{texmfdist}/source/latex/varindex
%{texmfdist}/source/latex/vector
%{texmfdist}/source/latex/verse
%{texmfdist}/source/latex/vmargin
%{texmfdist}/source/latex/volumes
%{texmfdist}/source/latex/vrsion
%{texmfdist}/source/latex/vwcol
%{texmfdist}/source/latex/vxu
%{texmfdist}/source/latex/warning
%{texmfdist}/source/latex/warpcol
%{texmfdist}/source/latex/was
%{texmfdist}/source/latex/xargs
%{texmfdist}/source/latex/xdoc
%{texmfdist}/source/latex/xfor
%{texmfdist}/source/latex/xmpincl
%{texmfdist}/source/latex/xpackages
%{texmfdist}/source/latex/xskak
%{texmfdist}/source/latex/xtab
%{texmfdist}/source/latex/xtcapts
%{texmfdist}/source/latex/yafoot
%{texmfdist}/source/latex/yfonts
%{texmfdist}/source/latex/yhmath
%{texmfdist}/source/latex/york-thesis
%{texmfdist}/source/latex/youngtab

%files latex-styles
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/IEEEconf
%doc %{texmfdist}/doc/latex/aastex
%doc %{texmfdist}/doc/latex/acmconf
%doc %{texmfdist}/doc/latex/active-conf
%doc %{texmfdist}/doc/latex/aiaa
%doc %{texmfdist}/doc/latex/apacite
%doc %{texmfdist}/doc/latex/asaetr
%doc %{texmfdist}/doc/latex/computational-complexity
%doc %{texmfdist}/doc/latex/dtk
%doc %{texmfdist}/doc/latex/elsarticle
%doc %{texmfdist}/doc/latex/lettre
%doc %{texmfdist}/doc/latex/lexikon
%doc %{texmfdist}/doc/latex/lps
%doc %{texmfdist}/doc/latex/manuscript
%doc %{texmfdist}/doc/latex/maple
%doc %{texmfdist}/doc/latex/mentis
%doc %{texmfdist}/doc/latex/nature
%doc %{texmfdist}/doc/latex/nih
%doc %{texmfdist}/doc/latex/nostarch
%doc %{texmfdist}/doc/latex/nrc
%doc %{texmfdist}/doc/latex/octavo
%doc %{texmfdist}/doc/latex/paper
%doc %{texmfdist}/doc/latex/papertex
%doc %{texmfdist}/doc/latex/pbsheet
%doc %{texmfdist}/doc/latex/petiteannonce
%doc %{texmfdist}/doc/latex/philosophersimprint
%doc %{texmfdist}/doc/latex/pittetd
%doc %{texmfdist}/doc/latex/plari
%doc %{texmfdist}/doc/latex/play
%doc %{texmfdist}/doc/latex/poemscol
%doc %{texmfdist}/doc/latex/pracjourn
%doc %{texmfdist}/doc/latex/ptptex
%doc %{texmfdist}/doc/latex/refman
%doc %{texmfdist}/doc/latex/rsc
%doc %{texmfdist}/doc/latex/screenplay
%doc %{texmfdist}/doc/latex/script
%doc %{texmfdist}/doc/latex/shipunov
%doc %{texmfdist}/doc/latex/sides
%doc %{texmfdist}/doc/latex/siggraph
%doc %{texmfdist}/doc/latex/stage
%doc %{texmfdist}/doc/latex/tufte-latex
%doc %{texmfdist}/doc/latex/tugboat
%doc %{texmfdist}/doc/latex/uaclasses
%doc %{texmfdist}/doc/latex/ucthesis
%doc %{texmfdist}/doc/latex/uiucthesis
%doc %{texmfdist}/doc/latex/umich-thesis
%doc %{texmfdist}/doc/latex/umthesis
%doc %{texmfdist}/doc/latex/uwthesis
%{texmfdist}/bibtex/bib/aiaa
%{texmfdist}/bibtex/bib/apacite
%{texmfdist}/bibtex/bib/asaetr
%{texmfdist}/bibtex/bib/computational-complexity
%{texmfdist}/bibtex/bib/dtk
%{texmfdist}/bibtex/bib/philosophersimprint
%{texmfdist}/bibtex/bst/aiaa
%{texmfdist}/bibtex/bst/apacite
%{texmfdist}/bibtex/bst/asaetr
%{texmfdist}/bibtex/bst/computational-complexity
%{texmfdist}/bibtex/bst/dtk
%{texmfdist}/bibtex/bst/rsc
%{texmfdist}/source/latex/IEEEconf
%{texmfdist}/source/latex/aastex
%{texmfdist}/source/latex/acmconf
%{texmfdist}/source/latex/active-conf
%{texmfdist}/source/latex/aiaa
%{texmfdist}/source/latex/apacite
%{texmfdist}/source/latex/asaetr
%{texmfdist}/source/latex/computational-complexity
%{texmfdist}/source/latex/dtk
%{texmfdist}/source/latex/elsarticle
%{texmfdist}/source/latex/lexikon
%{texmfdist}/source/latex/lps
%{texmfdist}/source/latex/manuscript
%{texmfdist}/source/latex/mentis
%{texmfdist}/source/latex/menu
%{texmfdist}/source/latex/nostarch
%{texmfdist}/source/latex/nrc
%{texmfdist}/source/latex/octavo
%{texmfdist}/source/latex/paper
%{texmfdist}/source/latex/papertex
%{texmfdist}/source/latex/pbsheet
%{texmfdist}/source/latex/philosophersimprint
%{texmfdist}/source/latex/pittetd
%{texmfdist}/source/latex/plari
%{texmfdist}/source/latex/play
%{texmfdist}/source/latex/poemscol
%{texmfdist}/source/latex/pracjourn
%{texmfdist}/source/latex/refman
%{texmfdist}/source/latex/rsc
%{texmfdist}/source/latex/screenplay
%{texmfdist}/source/latex/siggraph
%{texmfdist}/source/latex/tugboat
%{texmfdist}/source/latex/uaclasses
%{texmfdist}/source/latex/uiucthesis
%{texmfdist}/tex/latex/IEEEconf
%{texmfdist}/tex/latex/aastex
%{texmfdist}/tex/latex/acmconf
%{texmfdist}/tex/latex/active-conf
%{texmfdist}/tex/latex/aiaa
%{texmfdist}/tex/latex/apacite
%{texmfdist}/tex/latex/asaetr
%{texmfdist}/tex/latex/computational-complexity
%{texmfdist}/tex/latex/dtk
%{texmfdist}/tex/latex/elsarticle
%{texmfdist}/tex/latex/lettre
%{texmfdist}/tex/latex/lexikon
%{texmfdist}/tex/latex/lps
%{texmfdist}/tex/latex/manuscript
%{texmfdist}/tex/latex/maple
%{texmfdist}/tex/latex/mentis
%{texmfdist}/tex/latex/menu
%{texmfdist}/tex/latex/muthesis
%{texmfdist}/tex/latex/nature
%{texmfdist}/tex/latex/nih
%{texmfdist}/tex/latex/nostarch
%{texmfdist}/tex/latex/nrc
%{texmfdist}/tex/latex/octavo
%{texmfdist}/tex/latex/paper
%{texmfdist}/tex/latex/papertex
%{texmfdist}/tex/latex/pbsheet
%{texmfdist}/tex/latex/petiteannonce
%{texmfdist}/tex/latex/philosophersimprint
%{texmfdist}/tex/latex/pittetd
%{texmfdist}/tex/latex/plari
%{texmfdist}/tex/latex/play
%{texmfdist}/tex/latex/poemscol
%{texmfdist}/tex/latex/pracjourn
%{texmfdist}/tex/latex/ptptex
%{texmfdist}/tex/latex/refman
%{texmfdist}/tex/latex/rsc
%{texmfdist}/tex/latex/screenplay
%{texmfdist}/tex/latex/script
%{texmfdist}/tex/latex/shipunov
%{texmfdist}/tex/latex/sides
%{texmfdist}/tex/latex/siggraph
%{texmfdist}/tex/latex/stage
%{texmfdist}/tex/latex/tufte-latex
%{texmfdist}/tex/latex/tugboat
%{texmfdist}/tex/latex/uaclasses
%{texmfdist}/tex/latex/ucthesis
%{texmfdist}/tex/latex/uiucthesis
%{texmfdist}/tex/latex/umich-thesis
%{texmfdist}/tex/latex/umthesis
%{texmfdist}/tex/latex/uwthesis

%files latex-lang
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ESIEEcv
%doc %{texmfdist}/doc/latex/chletter
%doc %{texmfdist}/doc/latex/dinbrief
%doc %{texmfdist}/doc/latex/disser
%doc %{texmfdist}/doc/latex/elmath
%doc %{texmfdist}/doc/latex/eskd
%doc %{texmfdist}/doc/latex/ginpenc
%doc %{texmfdist}/doc/latex/hrlatex
%doc %{texmfdist}/doc/latex/mla-paper
%{texmfdist}/source/latex/ESIEEcv
%{texmfdist}/source/latex/chletter
%{texmfdist}/source/latex/dinbrief
%{texmfdist}/source/latex/disser
%{texmfdist}/source/latex/elmath
%{texmfdist}/source/latex/eskd
%{texmfdist}/source/latex/ginpenc
%{texmfdist}/source/latex/hrlatex
%{texmfdist}/tex/latex/ESIEEcv
%{texmfdist}/tex/latex/chletter
%{texmfdist}/tex/latex/dinbrief
%{texmfdist}/tex/latex/disser
%{texmfdist}/tex/latex/elmath
%{texmfdist}/tex/latex/eskd
%{texmfdist}/tex/latex/ginpenc
%{texmfdist}/tex/latex/hrlatex
%{texmfdist}/tex/latex/mla-paper

%files latex-music
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/musixps
%doc %{texmfdist}/doc/latex/abc
%doc %{texmfdist}/doc/latex/guitar
%doc %{texmfdist}/doc/latex/musixlyr
%doc %{texmfdist}/doc/latex/songbook
%{texmfdist}/fonts/source/public/musixps
%{texmfdist}/fonts/tfm/public/musixps
%{texmfdist}/source/latex/abc
%{texmfdist}/source/latex/guitar
%{texmfdist}/source/latex/songbook
%{texmfdist}/tex/generic/musixlyr
%{texmfdist}/tex/generic/musixps
%{texmfdist}/tex/latex/abc
%{texmfdist}/tex/latex/guitar
%{texmfdist}/tex/latex/songbook

%files latex-extend
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/HA-prosper
%doc %{texmfdist}/doc/latex/addlines
%doc %{texmfdist}/doc/latex/alnumsec
%doc %{texmfdist}/doc/latex/arydshln
%doc %{texmfdist}/doc/latex/babelbib
%doc %{texmfdist}/doc/latex/bibtopicprefix
%doc %{texmfdist}/doc/latex/boites
%doc %{texmfdist}/doc/latex/booklet
%doc %{texmfdist}/doc/latex/bullcntr
%doc %{texmfdist}/doc/latex/chappg
%doc %{texmfdist}/doc/latex/clefval
%doc %{texmfdist}/doc/latex/colortbl
%doc %{texmfdist}/doc/latex/combine
%doc %{texmfdist}/doc/latex/contour
%doc %{texmfdist}/doc/latex/ctable
%doc %{texmfdist}/doc/latex/curve2e
%doc %{texmfdist}/doc/latex/dashrule
%doc %{texmfdist}/doc/latex/etaremune
%doc %{texmfdist}/doc/latex/expdlist
%doc %{texmfdist}/doc/latex/leading
%doc %{texmfdist}/doc/latex/listliketab
%doc %{texmfdist}/doc/latex/makebox
%doc %{texmfdist}/doc/latex/makecell
%doc %{texmfdist}/doc/latex/marginnote
%doc %{texmfdist}/doc/latex/mcaption
%doc %{texmfdist}/doc/latex/mcite
%doc %{texmfdist}/doc/latex/mciteplus
%doc %{texmfdist}/doc/latex/minipage-marginpar
%doc %{texmfdist}/doc/latex/miniplot
%doc %{texmfdist}/doc/latex/multicap
%doc %{texmfdist}/doc/latex/newvbtm
%doc %{texmfdist}/doc/latex/notes2bib
%doc %{texmfdist}/doc/latex/ntabbing
%doc %{texmfdist}/doc/latex/pbox
%doc %{texmfdist}/doc/latex/pinlabel
%doc %{texmfdist}/doc/latex/polytable
%doc %{texmfdist}/doc/latex/rccol
%doc %{texmfdist}/doc/latex/romannum
%doc %{texmfdist}/doc/latex/schedule
%doc %{texmfdist}/doc/latex/subfloat
%doc %{texmfdist}/doc/latex/umoline
%doc %{texmfdist}/doc/latex/underlin
%{texmfdist}/bibtex/bst/babelbib
%{texmfdist}/bibtex/bst/mciteplus
%{texmfdist}/source/latex/HA-prosper
%{texmfdist}/source/latex/addlines
%{texmfdist}/source/latex/alnumsec
%{texmfdist}/source/latex/arydshln
%{texmfdist}/source/latex/babelbib
%{texmfdist}/source/latex/bibtopicprefix
%{texmfdist}/source/latex/boites
%{texmfdist}/source/latex/booklet
%{texmfdist}/source/latex/bullcntr
%{texmfdist}/source/latex/chappg
%{texmfdist}/source/latex/cjw
%{texmfdist}/source/latex/clefval
%{texmfdist}/source/latex/colortbl
%{texmfdist}/source/latex/combine
%{texmfdist}/source/latex/contour
%{texmfdist}/source/latex/ctable
%{texmfdist}/source/latex/curve2e
%{texmfdist}/source/latex/dashbox
%{texmfdist}/source/latex/dashrule
%{texmfdist}/source/latex/etaremune
%{texmfdist}/source/latex/expdlist
%{texmfdist}/source/latex/leading
%{texmfdist}/source/latex/listliketab
%{texmfdist}/source/latex/makebox
%{texmfdist}/source/latex/makecell
%{texmfdist}/source/latex/marginnote
%{texmfdist}/source/latex/mcaption
%{texmfdist}/source/latex/mcite
%{texmfdist}/source/latex/minipage-marginpar
%{texmfdist}/source/latex/multicap
%{texmfdist}/source/latex/newvbtm
%{texmfdist}/source/latex/notes2bib
%{texmfdist}/source/latex/pbox
%{texmfdist}/source/latex/polytable
%{texmfdist}/source/latex/rccol
%{texmfdist}/source/latex/romannum
%{texmfdist}/source/latex/schedule
%{texmfdist}/source/latex/subfloat
%{texmfdist}/source/latex/umoline
%{texmfdist}/source/latex/underlin
%{texmfdist}/tex/latex/HA-prosper
%{texmfdist}/tex/latex/addlines
%{texmfdist}/tex/latex/alnumsec
%{texmfdist}/tex/latex/arydshln
%{texmfdist}/tex/latex/babelbib
%{texmfdist}/tex/latex/bibtopicprefix
%{texmfdist}/tex/latex/boites
%{texmfdist}/tex/latex/booklet
%{texmfdist}/tex/latex/bullcntr
%{texmfdist}/tex/latex/chappg
%{texmfdist}/tex/latex/cjw
%{texmfdist}/tex/latex/clefval
%{texmfdist}/tex/latex/colortbl
%{texmfdist}/tex/latex/combine
%{texmfdist}/tex/latex/contour
%{texmfdist}/tex/latex/ctable
%{texmfdist}/tex/latex/curve2e
%{texmfdist}/tex/latex/dashbox
%{texmfdist}/tex/latex/dashrule
%{texmfdist}/tex/latex/etaremune
%{texmfdist}/tex/latex/expdlist
%{texmfdist}/tex/latex/leading
%{texmfdist}/tex/latex/listliketab
%{texmfdist}/tex/latex/ltablex
%{texmfdist}/tex/latex/makebox
%{texmfdist}/tex/latex/makecell
%{texmfdist}/tex/latex/marginnote
%{texmfdist}/tex/latex/mcaption
%{texmfdist}/tex/latex/mcite
%{texmfdist}/tex/latex/mciteplus
%{texmfdist}/tex/latex/minipage-marginpar
%{texmfdist}/tex/latex/miniplot
%{texmfdist}/tex/latex/multicap
%{texmfdist}/tex/latex/newvbtm
%{texmfdist}/tex/latex/notes2bib
%{texmfdist}/tex/latex/ntabbing
%{texmfdist}/tex/latex/numline
%{texmfdist}/tex/latex/pbox
%{texmfdist}/tex/latex/pinlabel
%{texmfdist}/tex/latex/polytable
%{texmfdist}/tex/latex/rccol
%{texmfdist}/tex/latex/romannum
%{texmfdist}/tex/latex/schedule
%{texmfdist}/tex/latex/subfloat
%{texmfdist}/tex/latex/umoline
%{texmfdist}/tex/latex/underlin

%files latex-presentation
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppower4
%attr(755,root,root) %{_bindir}/pdfthumb
%doc %{texmfdist}/doc/latex/powerdot
%doc %{texmfdist}/doc/latex/ppower4
%doc %{texmfdist}/doc/latex/sciposter
%doc %{texmfdist}/doc/latex/tpslifonts
%{texmfdist}/scripts/ppower4
%{texmfdist}/source/latex/powerdot
%{texmfdist}/tex/latex/powerdot
%{texmfdist}/tex/latex/ppower4
%{texmfdist}/tex/latex/sciposter
%{texmfdist}/tex/latex/tpslifonts

%files latex-programming
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cool
%doc %{texmfdist}/doc/latex/coollist
%doc %{texmfdist}/doc/latex/coolstr
%doc %{texmfdist}/doc/latex/csvtools
%doc %{texmfdist}/doc/latex/datatool
%doc %{texmfdist}/doc/latex/datenumber
%doc %{texmfdist}/doc/latex/delimtxt
%doc %{texmfdist}/doc/latex/dialogl
%doc %{texmfdist}/doc/latex/dprogress
%doc %{texmfdist}/doc/latex/environ
%doc %{texmfdist}/doc/latex/export
%doc %{texmfdist}/doc/latex/fmtcount
%doc %{texmfdist}/doc/latex/forarray
%doc %{texmfdist}/doc/latex/forloop
%doc %{texmfdist}/doc/latex/inversepath
%doc %{texmfdist}/doc/latex/labelcas
%doc %{texmfdist}/doc/latex/makecmds
%doc %{texmfdist}/doc/latex/nag
%doc %{texmfdist}/doc/latex/namespc
%doc %{texmfdist}/doc/latex/progress
%doc %{texmfdist}/doc/latex/randtext
%doc %{texmfdist}/doc/latex/regcount
%doc %{texmfdist}/doc/latex/robustcommand
%doc %{texmfdist}/doc/latex/splitindex
%doc %{texmfdist}/doc/latex/stringstrings
%doc %{texmfdist}/doc/latex/substr
%doc %{texmfdist}/doc/latex/typedref
%{texmfdist}/source/latex/cmdtrack
%{texmfdist}/source/latex/cool
%{texmfdist}/source/latex/coollist
%{texmfdist}/source/latex/coolstr
%{texmfdist}/source/latex/csvtools
%{texmfdist}/source/latex/datatool
%{texmfdist}/source/latex/datenumber
%{texmfdist}/source/latex/delimtxt
%{texmfdist}/source/latex/dialogl
%{texmfdist}/source/latex/dprogress
%{texmfdist}/source/latex/environ
%{texmfdist}/source/latex/export
%{texmfdist}/source/latex/fmtcount
%{texmfdist}/source/latex/forarray
%{texmfdist}/source/latex/forloop
%{texmfdist}/source/latex/inversepath
%{texmfdist}/source/latex/labelcas
%{texmfdist}/source/latex/lcg
%{texmfdist}/source/latex/makecmds
%{texmfdist}/source/latex/nag
%{texmfdist}/source/latex/namespc
%{texmfdist}/source/latex/patchcmd
%{texmfdist}/source/latex/regcount
%{texmfdist}/source/latex/robustcommand
%{texmfdist}/source/latex/splitindex
%{texmfdist}/source/latex/stack
%{texmfdist}/source/latex/stringstrings
%{texmfdist}/source/latex/typedref
%{texmfdist}/tex/latex/cmdtrack
%{texmfdist}/tex/latex/cool
%{texmfdist}/tex/latex/coollist
%{texmfdist}/tex/latex/coolstr
%{texmfdist}/tex/latex/csvtools
%{texmfdist}/tex/latex/datatool
%{texmfdist}/tex/latex/datenumber
%{texmfdist}/tex/latex/delimtxt
%{texmfdist}/tex/latex/dialogl
%{texmfdist}/tex/latex/dprogress
%{texmfdist}/tex/latex/environ
%{texmfdist}/tex/latex/export
%{texmfdist}/tex/latex/fmtcount
%{texmfdist}/tex/latex/forarray
%{texmfdist}/tex/latex/forloop
%{texmfdist}/tex/latex/inversepath
%{texmfdist}/tex/latex/labelcas
%{texmfdist}/tex/latex/lcg
%{texmfdist}/tex/latex/makecmds
%{texmfdist}/tex/latex/multido
%{texmfdist}/tex/latex/nag
%{texmfdist}/tex/latex/namespc
%{texmfdist}/tex/latex/patchcmd
%{texmfdist}/tex/latex/progress
%{texmfdist}/tex/latex/randtext
%{texmfdist}/tex/latex/regcount
%{texmfdist}/tex/latex/robustcommand
%{texmfdist}/tex/latex/splitindex
%{texmfdist}/tex/latex/stack
%{texmfdist}/tex/latex/stringstrings
%{texmfdist}/tex/latex/substr
%{texmfdist}/tex/latex/typedref

%files latex-effects
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/umrand
%doc %{texmfdist}/doc/latex/arcs
%doc %{texmfdist}/doc/latex/blowup
%doc %{texmfdist}/doc/latex/changebar
%doc %{texmfdist}/doc/latex/draftwatermark
%doc %{texmfdist}/doc/latex/flippdf
%doc %{texmfdist}/doc/latex/flowfram
%doc %{texmfdist}/doc/latex/isorot
%doc %{texmfdist}/doc/latex/lettrine
%doc %{texmfdist}/doc/latex/niceframe
%doc %{texmfdist}/doc/latex/notes
%doc %{texmfdist}/doc/latex/objectz
%doc %{texmfdist}/doc/latex/parallel
%doc %{texmfdist}/doc/latex/quotchap
%doc %{texmfdist}/doc/latex/rotpages
%doc %{texmfdist}/doc/latex/sectionbox
%doc %{texmfdist}/doc/latex/shadethm
%doc %{texmfdist}/doc/latex/ushort
%{texmfdist}/fonts/source/public/niceframe
%{texmfdist}/fonts/source/public/umrand
%{texmfdist}/fonts/tfm/public/niceframe
%{texmfdist}/fonts/tfm/public/umrand
%{texmfdist}/source/latex/arcs
%{texmfdist}/source/latex/blowup
%{texmfdist}/source/latex/changebar
%{texmfdist}/source/latex/draftwatermark
%{texmfdist}/source/latex/flippdf
%{texmfdist}/source/latex/flowfram
%{texmfdist}/source/latex/isorot
%{texmfdist}/source/latex/lettrine
%{texmfdist}/source/latex/niceframe
%{texmfdist}/source/latex/notes
%{texmfdist}/source/latex/objectz
%{texmfdist}/source/latex/parallel
%{texmfdist}/source/latex/quotchap
%{texmfdist}/source/latex/ushort
%{texmfdist}/tex/latex/arcs
%{texmfdist}/tex/latex/blowup
%{texmfdist}/tex/latex/changebar
%{texmfdist}/tex/latex/draftwatermark
%{texmfdist}/tex/latex/flippdf
%{texmfdist}/tex/latex/flowfram
%{texmfdist}/tex/latex/isorot
%{texmfdist}/tex/latex/lettrine
%{texmfdist}/tex/latex/niceframe
%{texmfdist}/tex/latex/notes
%{texmfdist}/tex/latex/objectz
%{texmfdist}/tex/latex/parallel
%{texmfdist}/tex/latex/quotchap
%{texmfdist}/tex/latex/rotpages
%{texmfdist}/tex/latex/sectionbox
%{texmfdist}/tex/latex/shadethm
%{texmfdist}/tex/latex/umrand
%{texmfdist}/tex/latex/ushort

# I don't sort them, because maybe can splitting and grouping them
%files latex-other
%defattr(644,root,root,755)
%{texmfdist}/metapost/latexmp
%{texmfdist}/metapost/makecirc
%dir %{texmfdist}/source/alatex
%{texmfdist}/source/alatex/base
%dir %{texmfdist}/source/cslatex
%{texmfdist}/source/cslatex/base
%{texmfdist}/source/generic/xypic
%{texmfdist}/source/latex/GuIT
# Definitive source of Plain TeX on CTAN.
%{texmfdist}/source/latex/base
%{texmfdist}/source/latex/bayer
# A small collection of minimal DTX examples.
%{texmfdist}/source/latex/dtxgallery
# Editorial Notes for LaTeX documents.
%{texmfdist}/source/latex/ed
# Typeset scholarly edition.
%{texmfdist}/source/latex/edmac
# Use AMS Euler fonts for math.
%{texmfdist}/source/latex/euler
# Ridgeway's fonts.
%{texmfdist}/source/latex/wnri
%dir %{texmfdist}/source/plain
%{texmfdist}/source/plain/jsmisc
%{texmfdist}/source/xelatex
%{texmfdist}/tex/alatex
%{texmfdist}/tex/generic/enctex
# Create a calendar, in German.
%{texmfdist}/tex/latex/kalender
# Typeset Karnaugh-Veitch-maps.
%{texmfdist}/tex/latex/karnaugh
# Kerkis (Greek) font family.
%{texmfdist}/tex/latex/kerkis
# Print tables and generate control files to adjust kernings.
%{texmfdist}/source/latex/kerntest
%{texmfdist}/tex/latex/kerntest
%{texmfdist}/tex/latex/kluwer
%{texmfdist}/source/latex/kluwer
# A two-element sans-serif typeface.
%{texmfdist}/tex/latex/kurier
# Lists in TeX's "mouth".
%{texmfdist}/tex/latex/lazylist
# This package makes available Classic Cyrillic CM fonts
%{texmfdist}/source/latex/lcyw
%{texmfdist}/tex/latex/lcyw
# Typeset scholarly editions in parallel texts.
%{texmfdist}/source/latex/ledmac
%{texmfdist}/tex/latex/ledmac
%{texmfdist}/tex/latex/levy
# Macros for using Silvio Levy's Greek fonts.
%{texmfdist}/tex/latex/lgreek
# A non-standard Cyrillic input scheme.
%{texmfdist}/source/latex/lhcyr
%{texmfdist}/tex/latex/lhcyr
# Miscellaneous helper packages.
%{texmfdist}/source/latex/lhelp
%{texmfdist}/tex/latex/lhelp
# Use the font Libertine with LaTeX.
%{texmfdist}/tex/latex/libertine
# Typeset maps and blocks according to the Information Mapping
%{texmfdist}/source/latex/limap
%{texmfdist}/tex/latex/limap
%{texmfdist}/tex/latex/linearA
# Format linguists' examples.
%{texmfdist}/tex/latex/linguex
# Easy access to the Lorem Ipsum dummy text.
%{texmfdist}/source/latex/lipsum
%{texmfdist}/tex/latex/lipsum
# Lists contents of BibTeX files.
%{texmfdist}/source/latex/listbib
%{texmfdist}/tex/latex/listbib
# LK Proof figure macros.
%{texmfdist}/tex/latex/lkproof
# A font for electronic logic design.
%{texmfdist}/tex/latex/logic
# A LaTeX package to typeset indices with GNU's Texindex.
%{texmfdist}/source/latex/ltxindex
%{texmfdist}/tex/latex/ltxindex
# Set of slide fonts based on CM.
%{texmfdist}/tex/latex/lxfonts
# Support for LY1 LaTeX encoding.
%{texmfdist}/tex/latex/ly1
# Mathematics in accord with French usage.
%{texmfdist}/tex/latex/mafr
# Macros for mail merging.
%{texmfdist}/source/latex/mailing
%{texmfdist}/tex/latex/mailing
# Print various kinds 2/5 and Code 39 bar codes.
%{texmfdist}/tex/latex/makebarcode
# Perl script to help generate dtx and ins files
%{texmfdist}/source/latex/makedtx
%{texmfdist}/tex/latex/makedtx
# Include a glossary into a document.
%{texmfdist}/tex/latex/makeglos
# LaTeX support for the TeX book symbols.
%{texmfdist}/source/latex/manfnt
%{texmfdist}/tex/latex/manfnt
# Support for multiple character sets and encodings.
%{texmfdist}/source/latex/mapcodes
%{texmfdist}/tex/latex/mapcodes
# Mathematical fonts to fit with particular text fonts.
%{texmfdist}/tex/latex/mathdesign
# Creating covers for music cassettes.
%{texmfdist}/tex/latex/mceinleger
# Experimental memoir support.
%{texmfdist}/tex/latex/memexsupp
# Multiple font formats.
%{texmfdist}/source/latex/mff
%{texmfdist}/tex/latex/mff
# Pretty-print Metafont source.
%{texmfdist}/source/latex/mftinc
%{texmfdist}/tex/latex/mftinc
# Package for writing minutes of meetings.
%{texmfdist}/source/latex/minutes
%{texmfdist}/tex/latex/minutes
# Allows font sizes up to 35.83pt.
%{texmfdist}/source/latex/moresize
%{texmfdist}/tex/latex/moresize
# A package for LaTeX localisation.
%{texmfdist}/source/latex/msg
%{texmfdist}/tex/latex/msg
# Michael Landy's APA citation style.
%{texmfdist}/tex/latex/mslapa
# Use italic and upright greek letters with mathtime.
%{texmfdist}/source/latex/mtgreek
%{texmfdist}/tex/latex/mtgreek
# Multiple bibliographies.
%{texmfdist}/source/latex/multibbl
%{texmfdist}/tex/latex/multibbl
# Support for Mongolian "horizontal" (Xewtee Dorwoljin) script.
%{texmfdist}/source/latex/mxd
%{texmfdist}/tex/latex/mxd
# A pair of Georgian fonts.
%{texmfdist}/tex/latex/mxedruli
# Nomenclature typeset in a longtable
%{texmfdist}/source/latex/nomentbl
%{texmfdist}/tex/latex/nomentbl
# Non-floating table and figure captions.
%{texmfdist}/source/latex/nonfloat
%{texmfdist}/tex/latex/nonfloat
# Convert a number to its English expression.
%{texmfdist}/tex/latex/numname
# LaTeX support for ocr fonts.
%{texmfdist}/tex/latex/ocr-latex
# Support for Polish typography and the ogonek.
%{texmfdist}/source/latex/ogonek
%{texmfdist}/tex/latex/ogonek
# Old style numbers in OT1 encoding.
%{texmfdist}/source/latex/oldstyle
%{texmfdist}/tex/latex/oldstyle
# Footnote-style bibliographical references.
%{texmfdist}/source/latex/opcit
%{texmfdist}/tex/latex/opcit
# Counters as ordinal numbers in Portuguese.
%{texmfdist}/source/latex/ordinalpt
%{texmfdist}/tex/latex/ordinalpt
# Macros, metrics, etc., to use the OT2 Cyrillic encoding.
%{texmfdist}/tex/latex/ot2cyr
%{texmfdist}/tex/latex/otibet
%{texmfdist}/source/latex/otibet
# List environment for making outlines.
%{texmfdist}/tex/latex/outline
# Change section levels easily.
%{texmfdist}/tex/latex/outliner
# Fonts designed by Fra Luca de Pacioli in 1497.
%{texmfdist}/source/latex/pacioli
%{texmfdist}/tex/latex/pacioli
# Page number-only page styles.
%{texmfdist}/source/latex/pageno
%{texmfdist}/tex/latex/pageno
# Notes at end of document.
%{texmfdist}/source/latex/pagenote
%{texmfdist}/tex/latex/pagenote
%{texmfdist}/tex/latex/palatino
# Origami-style folding paper CD case.
%{texmfdist}/source/latex/papercdcase
%{texmfdist}/tex/latex/papercdcase
# Defines simple macros for greek letters.
%{texmfdist}/source/latex/paresse
%{texmfdist}/tex/latex/paresse
# Typesets (two) streams of text running parallel.
%{texmfdist}/source/latex/parrun
%{texmfdist}/tex/latex/parrun
# German LaTeX package documentation.
%{texmfdist}/source/latex/pauldoc
%{texmfdist}/tex/latex/pauldoc
# Using graphics from PAW.
%{texmfdist}/source/latex/pawpict
%{texmfdist}/tex/latex/pawpict
# Font support for current PCL printers.
%{texmfdist}/tex/latex/pclnfss
%{texmfdist}/tex/latex/pdfwin
# Print Tibetan text in the classic pecha layout style.
%{texmfdist}/tex/latex/pecha
# Define LaTeX macros in terms of Perl code
%{texmfdist}/source/latex/perltex
%{texmfdist}/tex/latex/perltex
# Create images of the soroban using TikZ/PGF.
%{texmfdist}/tex/latex/pgf-soroban
# Disk of Phaistos font.
%{texmfdist}/tex/latex/phaistos
# Cross references for named and numbered environments.
%{texmfdist}/tex/latex/philex
# MetaFont Phonetic fonts, based on Computer Modern.
%{texmfdist}/tex/latex/phonetic
# Adds relative coordinates and improves the \plot command.
%{texmfdist}/tex/latex/pictex2
# Arrange for "plates" sections of documents.
%{texmfdist}/tex/latex/plates
%{texmfdist}/source/latex/plweb
%{texmfdist}/tex/latex/plweb
# "Poor man's" graphics.
%{texmfdist}/tex/latex/pmgraph
# Typeset Polish documents with LaTeX and Polish fonts.
%{texmfdist}/source/latex/polski
%{texmfdist}/tex/latex/polski
%{texmfdist}/source/latex/polyglot
%{texmfdist}/tex/latex/polyglot
# Facilitates mass-mailing of postcards (junkmail).
%{texmfdist}/tex/latex/postcards
# Make label references "self-identify".
%{texmfdist}/source/latex/prettyref
%{texmfdist}/tex/latex/prettyref
# Shortcuts commands to symbols used in probability texts.
%{texmfdist}/source/latex/proba
%{texmfdist}/tex/latex/proba
%{texmfdist}/tex/latex/procIAGssymp
# Literate programming package.
%{texmfdist}/tex/latex/protex
# A class for typesetting minutes (only german).
%{texmfdist}/source/latex/protocol
%{texmfdist}/tex/latex/protocol
# A psfrag eXtension.
%{texmfdist}/source/latex/psfragx
%{texmfdist}/tex/latex/psfragx
%{texmfdist}/tex/latex/psgo
# PostScript picture support.
%{texmfdist}/source/latex/pspicture
%{texmfdist}/tex/latex/pspicture
# LaTeX macros for typesetting trees.
%{texmfdist}/tex/latex/qobitree
# Bundle for unit tests and pattern matching.
%{texmfdist}/source/latex/qstest
%{texmfdist}/tex/latex/qstest
# Consistent quote marks.
%{texmfdist}/source/latex/quotmark
%{texmfdist}/tex/latex/quotmark
%{texmfdist}/tex/latex/r_und_s
# Marginal pictures.
%{texmfdist}/source/latex/randbild
%{texmfdist}/tex/latex/randbild
# Use RCS (revision control system) tags in LaTeX documents.
%{texmfdist}/source/latex/rcs
%{texmfdist}/tex/latex/rcs
# Support for the revision control system.
%{texmfdist}/source/latex/rcsinfo
%{texmfdist}/tex/latex/rcsinfo
# Recycle top matter.
%{texmfdist}/tex/latex/rectopma
# Check references (in figures, table, equations, etc).
%{texmfdist}/tex/latex/refcheck
# Advanced formatting of cross references.
%{texmfdist}/source/latex/refstyle
%{texmfdist}/tex/latex/refstyle
# A "relaxed" font encoding.
%{texmfdist}/source/latex/relenc
%{texmfdist}/tex/latex/relenc
# Repeat items in an index after a page or column break
%{texmfdist}/tex/latex/repeatindex
%{texmfdist}/tex/latex/resume
# Rewrite labels in EPS graphics.
%{texmfdist}/tex/latex/rlepsf
# A package to help change page layout parameters in LaTeX.
%{texmfdist}/source/latex/rmpage
%{texmfdist}/tex/latex/rmpage
# Create index with pagerefs.
%{texmfdist}/tex/latex/robustindex
# Drawing rhetorical structure analysis diagrams in LaTeX.
%{texmfdist}/source/latex/rst
%{texmfdist}/tex/latex/rst
# Input encoding with fallback procedures.
%{texmfdist}/source/latex/rtkinenc
%{texmfdist}/tex/latex/rtkinenc
%{texmfdist}/tex/latex/rtklage
# Embed Sage code and plots into LaTeX.
%{texmfdist}/source/latex/sagetex
%{texmfdist}/tex/latex/sagetex
# Sanskrit support.
%{texmfdist}/source/latex/sanskrit
%{texmfdist}/tex/latex/sanskrit
# A bundle of utilities by Jonathan Sauer.
%{texmfdist}/source/latex/sauerj
%{texmfdist}/tex/latex/sauerj
# Use sauter fonts in LaTeX.
%{texmfdist}/source/latex/sauterfonts
%{texmfdist}/tex/latex/sauterfonts
# Save name of the footnote mark for reuse.
%{texmfdist}/source/latex/savefnmark
%{texmfdist}/tex/latex/savefnmark
# Redefine symbols where names conflict.
%{texmfdist}/tex/latex/savesym
# Pack as much as possible onto each page of a LaTeX document.
%{texmfdist}/source/latex/savetrees
%{texmfdist}/tex/latex/savetrees
# Create scalebars for maps, diagrams or photos.
%{texmfdist}/source/latex/scalebar
%{texmfdist}/tex/latex/scalebar
# Format a scientific paper for journal
%{texmfdist}/tex/latex/scientificpaper
# Use Scientific Word/WorkPlace files with another TeX.
%{texmfdist}/source/latex/sciwordconv
%{texmfdist}/tex/latex/sciwordconv
# Semaphore alphabet font.
%{texmfdist}/tex/latex/semaphor
# Put only special contents on left-hand pages in two sided layout.
%{texmfdist}/source/latex/semioneside
%{texmfdist}/tex/latex/semioneside
# Split long sequences of characters in a neutral way.
%{texmfdist}/source/latex/seqsplit
%{texmfdist}/tex/latex/seqsplit
%{texmfdist}/source/latex/sf298
%{texmfdist}/tex/latex/sf298
# Typesetting science fiction/fantasy manuscripts.
%{texmfdist}/source/latex/sffms
%{texmfdist}/tex/latex/sffms
# Draw signal flow graphs.
%{texmfdist}/tex/latex/sfg
# Shade the background of any box.
%{texmfdist}/tex/latex/shadbox
# Table of contents with different depths.
%{texmfdist}/source/latex/shorttoc
%{texmfdist}/tex/latex/shorttoc
# Variants of \show for LaTeX2e.
%{texmfdist}/source/latex/show2e
%{texmfdist}/tex/latex/show2e
%{texmfdist}/source/latex/showexpl
%{texmfdist}/tex/latex/showexpl
# A font to draw a skull.
%{texmfdist}/source/latex/skull
%{texmfdist}/tex/latex/skull
# Access different-shaped small-caps fonts.
%{texmfdist}/source/latex/slantsc
%{texmfdist}/tex/latex/slantsc
# Create listoffigures etc. in a single chapter.
%{texmfdist}/tex/latex/smalltableof
# Extend LaTeX's \ref capability.
%{texmfdist}/tex/latex/smartref
# Classes for Société mathématique de France publications.
%{texmfdist}/tex/latex/smflatex
# List the external dependencies of a LaTeX document.
%{texmfdist}/source/latex/snapshot
%{texmfdist}/tex/latex/snapshot
# Fonts and a macro for Soyombo under LaTeX.
%{texmfdist}/tex/latex/soyombo
# Drawing sparklines: intense, simple, wordlike graphics.
%{texmfdist}/tex/latex/sparklines
# Support for formatting SPIE Proceedings manuscripts.
%{texmfdist}/tex/latex/spie
# Split and reorder your bibliography.
%{texmfdist}/source/latex/splitbib
%{texmfdist}/tex/latex/splitbib
# Macros to typeset simple bitmaps with LaTeX.
%{texmfdist}/tex/latex/sprite
# Jump between DVI and TeX files.
%{texmfdist}/source/latex/srcltx
%{texmfdist}/tex/latex/srcltx
# Use the cmssq fonts.
%{texmfdist}/source/latex/ssqquote
%{texmfdist}/tex/latex/ssqquote
# Statistics style.
%{texmfdist}/tex/latex/statex2
# Store statistics of a document.
%{texmfdist}/source/latex/statistik
%{texmfdist}/tex/latex/statistik
# Typeset Icelandic staves and runic letters.
%{texmfdist}/source/latex/staves
%{texmfdist}/tex/latex/staves
# Standard pages with n lines of at most m characters each.
%{texmfdist}/source/latex/stdpage
%{texmfdist}/tex/latex/stdpage
# Stellenbosch thesis bundle.
%{texmfdist}/source/latex/stellenbosch
%{texmfdist}/tex/latex/stellenbosch
# An Infrastructure for Semantic Preloading of LaTeX Documents.
%{texmfdist}/source/latex/stex
%{texmfdist}/tex/latex/stex
# Draw Nassi-Schneidermann charts
%{texmfdist}/source/latex/struktex
%{texmfdist}/tex/latex/struktex
# Various macros.
%{texmfdist}/tex/latex/sttools
# Create tear-off stubs at the bottom of a page.
%{texmfdist}/tex/latex/stubs
# SAS(R) user group conference proceedings document class.
%{texmfdist}/tex/latex/sugconf
# Define SVG named colours.
%{texmfdist}/tex/latex/svgcolor
# Subversion keywords in multi-file LaTeX documents
%{texmfdist}/source/latex/svn-multi
%{texmfdist}/tex/latex/svn-multi
# Typeset Subversion keywords.
%{texmfdist}/source/latex/svn
%{texmfdist}/tex/latex/svn
# Typeset Subversion Keywords.
%{texmfdist}/source/latex/svninfo
%{texmfdist}/tex/latex/svninfo
# Graphical/textual representations of swimming performances
%{texmfdist}/source/latex/swimgraf
%{texmfdist}/tex/latex/swimgraf
%{texmfdist}/tex/latex/symbol
# Easy drawing of syntactic proofs.
%{texmfdist}/tex/latex/synproof
%{texmfdist}/tex/latex/syntax
# Labels for tracing in a syntax tree.
%{texmfdist}/source/latex/syntrace
%{texmfdist}/tex/latex/syntrace
# Typeset syntactic trees.
%{texmfdist}/source/latex/synttree
%{texmfdist}/tex/latex/synttree
# Fonts and macro package for drawing timing diagrams.
%{texmfdist}/tex/latex/timing
# Section numbering and table of contents control.
%{texmfdist}/source/latex/tocvsec2
%{texmfdist}/tex/latex/tocvsec2
# A tokenizer.
%{texmfdist}/tex/latex/tokenizer
# Macros for writing indices, glossaries.
%{texmfdist}/source/latex/toolbox
%{texmfdist}/tex/latex/toolbox
# Bundle of files for typsetting theses.
%{texmfdist}/source/latex/toptesi
%{texmfdist}/tex/latex/toptesi
# Adjust tracking of strings.
%{texmfdist}/tex/latex/tracking
# Fonts from the Trajan column in Rome.
%{texmfdist}/source/latex/trajan
%{texmfdist}/tex/latex/trajan
# Provide an open platform for packages to be localized.
%{texmfdist}/tex/latex/translator
# Quick float definitions in LaTeX.
%{texmfdist}/source/latex/trivfloat
%{texmfdist}/tex/latex/trivfloat
# Typeset the (logic) turnstile notation.
%{texmfdist}/source/latex/turnstile
%{texmfdist}/tex/latex/turnstile
%{texmfdist}/source/latex/twoup
%{texmfdist}/tex/latex/twoup
# Print a typographic grid.
%{texmfdist}/source/latex/typogrid
%{texmfdist}/tex/latex/typogrid
# Time printing, in German.
%{texmfdist}/tex/latex/uhrzeit

%files latex-pdfslide
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/pdfslide
%{texmfdist}/tex/latex/pdfslide

%files latex-pgf
%defattr(644,root,root,755)
%dir %{texmfdist}/source/context
%dir %{texmfdist}/source/context/third
%doc %{texmfdist}/doc/generic/pgf
%doc %{texmfdist}/doc/latex/pgfplots
%{texmfdist}/source/context/third/pgfplots
%{texmfdist}/source/latex/pgfopts
%{texmfdist}/source/latex/pgfplots
%{texmfdist}/tex/generic/pgf
%{texmfdist}/tex/generic/pgfplots
%{texmfdist}/tex/latex/pgf
%{texmfdist}/tex/latex/pgfopts
%{texmfdist}/tex/latex/pgfplots

%files latex-prosper
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ppr-prv
%doc %{texmfdist}/doc/latex/prosper
%{texmfdist}/source/latex/ppr-prv
%{texmfdist}/source/latex/prosper
%{texmfdist}/tex/latex/ppr-prv
%{texmfdist}/tex/latex/prosper

%files latex-polynom
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/polynom
%{texmfdist}/source/latex/polynom
%{texmfdist}/tex/latex/polynom

%files latex-polynomial
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/polynomial
%{texmfdist}/source/latex/polynomial
%{texmfdist}/tex/latex/polynomial

%files latex-pseudocode
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/pseudocode
%{texmfdist}/tex/latex/pseudocode

%files latex-pst-2dplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-2dplot
%{texmfdist}/tex/latex/pst-2dplot

%files latex-pst-3dplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-3d
%doc %{texmfdist}/doc/generic/pst-3dplot
%{texmfdist}/source/generic/pst-3d
%{texmfdist}/source/generic/pst-3dplot
%{texmfdist}/tex/generic/pst-3d
%{texmfdist}/tex/generic/pst-3dplot
%{texmfdist}/tex/latex/pst-3d
%{texmfdist}/tex/latex/pst-3dplot

%files latex-pst-bar
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/pst-bar
%{texmfdist}/tex/latex/pst-bar

%files latex-pst-circ
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-circ
%{texmfdist}/tex/generic/pst-circ
%{texmfdist}/tex/latex/pst-circ

%files latex-pst-diffraction
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-diffraction
%{texmfdist}/tex/generic/pst-diffraction
%{texmfdist}/tex/latex/pst-diffraction

%files latex-pst-eucl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-eucl
%{texmfdist}/tex/generic/pst-eucl
%{texmfdist}/tex/latex/pst-eucl

%files latex-pst-fun
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fun
%{texmfdist}/tex/generic/pst-fun
%{texmfdist}/tex/latex/pst-fun

%files latex-pst-func
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-func
%{texmfdist}/tex/generic/pst-func
%{texmfdist}/tex/latex/pst-func

%files latex-pst-infixplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-infixplot
%{texmfdist}/tex/generic/pst-infixplot
%{texmfdist}/tex/latex/pst-infixplot

%files latex-pst-fr3d
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fr3d
%{texmfdist}/source/generic/pst-fr3d
%{texmfdist}/tex/generic/pst-fr3d
%{texmfdist}/tex/latex/pst-fr3d

%files latex-pst-fractal
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fractal
%{texmfdist}/tex/generic/pst-fractal
%{texmfdist}/tex/latex/pst-fractal

%files latex-pst-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-math
%{texmfdist}/tex/generic/pst-math
%{texmfdist}/tex/latex/pst-math

%files latex-pst-ob3d
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-ob3d
%{texmfdist}/source/generic/pst-ob3d
%{texmfdist}/tex/generic/pst-ob3d
%{texmfdist}/tex/latex/pst-ob3d

%files latex-pst-optexp
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-optexp
%{texmfdist}/tex/generic/pst-optexp
%{texmfdist}/tex/latex/pst-optexp

%files latex-pst-optic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-optic
%{texmfdist}/tex/generic/pst-optic
%{texmfdist}/tex/latex/pst-optic

%files latex-pst-text
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-text
%{texmfdist}/tex/generic/pst-text
%{texmfdist}/tex/latex/pst-text

%files latex-pst-uncategorized
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-asr
%doc %{texmfdist}/doc/generic/pst-bar
%doc %{texmfdist}/doc/generic/pst-barcode
%doc %{texmfdist}/doc/generic/pst-blur
%doc %{texmfdist}/doc/generic/pst-coil
%doc %{texmfdist}/doc/generic/pst-cox
%doc %{texmfdist}/doc/generic/pst-dbicons
%doc %{texmfdist}/doc/generic/pst-eps
%doc %{texmfdist}/doc/generic/pst-fill
%doc %{texmfdist}/doc/generic/pst-geo
%doc %{texmfdist}/doc/generic/pst-ghsb
%doc %{texmfdist}/doc/generic/pst-gr3d
%doc %{texmfdist}/doc/generic/pst-grad
%doc %{texmfdist}/doc/generic/pst-jtree
%doc %{texmfdist}/doc/generic/pst-labo
%doc %{texmfdist}/doc/generic/pst-lens
%doc %{texmfdist}/doc/generic/pst-light3d
%doc %{texmfdist}/doc/generic/pst-osci
%doc %{texmfdist}/doc/generic/pst-pad
%doc %{texmfdist}/doc/generic/pst-pdgr
%doc %{texmfdist}/doc/generic/pst-poly
%doc %{texmfdist}/doc/generic/pst-qtree
%doc %{texmfdist}/doc/generic/pst-slpe
%doc %{texmfdist}/doc/generic/pst-solides3d
%doc %{texmfdist}/doc/generic/pst-soroban
%doc %{texmfdist}/doc/generic/pst-spectra
%doc %{texmfdist}/doc/generic/pst-stru
%doc %{texmfdist}/doc/generic/pst-uml
%doc %{texmfdist}/doc/generic/pst-vue3d
%doc %{texmfdist}/doc/latex/auto-pst-pdf
%doc %{texmfdist}/doc/latex/pst-pdf
%{texmfdist}/scripts/pst-pdf
%{texmfdist}/source/generic/pst-barcode
%{texmfdist}/source/generic/pst-blur
%{texmfdist}/source/generic/pst-circ
%{texmfdist}/source/generic/pst-coil
%{texmfdist}/source/generic/pst-dbicons
%{texmfdist}/source/generic/pst-diffraction
%{texmfdist}/source/generic/pst-eps
%{texmfdist}/source/generic/pst-fill
%{texmfdist}/source/generic/pst-fractal
%{texmfdist}/source/generic/pst-fun
%{texmfdist}/source/generic/pst-func
%{texmfdist}/source/generic/pst-lens
%{texmfdist}/source/generic/pst-light3d
%{texmfdist}/source/generic/pst-optic
%{texmfdist}/source/generic/pst-pad
%{texmfdist}/source/generic/pst-pdgr
%{texmfdist}/source/generic/pst-slpe
%{texmfdist}/source/generic/pst-soroban
%{texmfdist}/source/generic/pst-text
%{texmfdist}/source/generic/pst-uml
%{texmfdist}/source/generic/pst-vue3d
%{texmfdist}/source/latex/auto-pst-pdf
%{texmfdist}/source/latex/pst-gr3d
%{texmfdist}/source/latex/pst-pdf
%{texmfdist}/source/latex/pst-poly
%{texmfdist}/tex/generic/pst-asr
%{texmfdist}/tex/generic/pst-barcode
%{texmfdist}/tex/generic/pst-blur
%{texmfdist}/tex/generic/pst-coil
%{texmfdist}/tex/generic/pst-cox
%{texmfdist}/tex/generic/pst-eps
%{texmfdist}/tex/generic/pst-fill
%{texmfdist}/tex/generic/pst-geo
%{texmfdist}/tex/generic/pst-ghsb
%{texmfdist}/tex/generic/pst-gr3d
%{texmfdist}/tex/generic/pst-grad
%{texmfdist}/tex/generic/pst-jtree
%{texmfdist}/tex/generic/pst-labo
%{texmfdist}/tex/generic/pst-lens
%{texmfdist}/tex/generic/pst-light3d
%{texmfdist}/tex/generic/pst-osci
%{texmfdist}/tex/generic/pst-pad
%{texmfdist}/tex/generic/pst-pdgr
%{texmfdist}/tex/generic/pst-poly
%{texmfdist}/tex/generic/pst-qtree
%{texmfdist}/tex/generic/pst-slpe
%{texmfdist}/tex/generic/pst-solides3d
%{texmfdist}/tex/generic/pst-spectra
%{texmfdist}/tex/generic/pst-stru
%{texmfdist}/tex/generic/pst-vue3d
%{texmfdist}/tex/latex/pst-asr
%{texmfdist}/tex/latex/pst-barcode
%{texmfdist}/tex/latex/pst-blur
%{texmfdist}/tex/latex/pst-coil
%{texmfdist}/tex/latex/pst-cox
%{texmfdist}/tex/latex/pst-dbicons
%{texmfdist}/tex/latex/pst-eps
%{texmfdist}/tex/latex/pst-fill
%{texmfdist}/tex/latex/pst-geo
%{texmfdist}/tex/latex/pst-ghsb
%{texmfdist}/tex/latex/pst-gr3d
%{texmfdist}/tex/latex/pst-grad
%{texmfdist}/tex/latex/pst-jtree
%{texmfdist}/tex/latex/pst-labo
%{texmfdist}/tex/latex/pst-lens
%{texmfdist}/tex/latex/pst-light3d
%{texmfdist}/tex/latex/pst-osci
%{texmfdist}/tex/latex/pst-pad
%{texmfdist}/tex/latex/pst-pdf
%{texmfdist}/tex/latex/pst-pdgr
%{texmfdist}/tex/latex/pst-poly
%{texmfdist}/tex/latex/pst-qtree
%{texmfdist}/tex/latex/pst-slpe
%{texmfdist}/tex/latex/pst-solides3d
%{texmfdist}/tex/latex/pst-soroban
%{texmfdist}/tex/latex/pst-spectra
%{texmfdist}/tex/latex/pst-stru
%{texmfdist}/tex/latex/pst-uml
%{texmfdist}/tex/latex/pst-vue3d

%files latex-psnfss
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/psnfss
%{texmfdist}/fonts/map/dvips/psnfss
%{texmfdist}/source/latex/psnfss
%{texmfdist}/source/latex/latex-tds
%{texmfdist}/tex/latex/psnfss

%files latex-pxfonts
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/pxfonts
%{texmfdist}/fonts/type1/public/pxfonts
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts

%files latex-SIstyle
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIstyle
%{texmfdist}/source/latex/SIstyle
%{texmfdist}/tex/latex/SIstyle

%files latex-SIunits
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIunits
%{texmfdist}/tex/latex/SIunits
%{texmfdist}/source/latex/SIunits

%files latex-siunitx
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/siunitx
%{texmfdist}/tex/latex/siunitx
%{texmfdist}/source/latex/siunitx

%files latex-Tabbing
%defattr(644,root,root,755)
%{texmfdist}/source/latex/Tabbing
%{texmfdist}/doc/latex/Tabbing

%files latex-txfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/txfonts
%{texmfdist}/fonts/type1/public/txfonts
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/enc/dvips/txfonts
%{texmfdist}/fonts/vf/public/txfonts
%{texmfdist}/fonts/map/dvips/txfonts
%{texmfdist}/tex/latex/txfonts

%files latex-ucs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ucs
%{texmfdist}/tex/latex/ucs

%files latex-umlaute
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/umlaute
%{texmfdist}/source/latex/umlaute

%files latex-variations
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/variations
%{texmfdist}/tex/generic/variations

%files latex-wasysym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/wasysym
%{texmfdist}/tex/latex/wasysym
%{texmfdist}/source/latex/wasysym

%files latex-xcolor
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xcolor
%{texmfdist}/source/latex/xcolor

%files format-pdflatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdflatex
%{fmtdir}/pdftex/pdflatex.fmt
%{_mandir}/man1/pdflatex.1*

%files tex-babel
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/babel
%{texmfdist}/source/generic/babel
%{texmfdist}/tex/generic/babel

%files tex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/german
%{texmfdist}/tex/generic/german
%{texmfdist}/source/generic/german

%files tex-mfpic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mfpic
%{texmfdist}/tex/generic/mfpic
%{texmfdist}/source/generic/mfpic

%files tex-midnight
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/midnight
%{texmfdist}/tex/generic/midnight

%files tex-misc
%defattr(644,root,root,755)
%{texmfdist}/source/generic/tap
%doc %{texmfdist}/doc/generic/multido
%doc %{texmfdist}/doc/generic/tap
%doc %{texmfdist}/doc/generic/vrb

%{texmfdist}/tex/generic/eijkhout
%{texmfdist}/tex/generic/multido
%{texmfdist}/tex/generic/misc
%{texmfdist}/tex/generic/vrb

%files tex-pictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pictex
%{texmfdist}/tex/generic/pictex

%files tex-psizzl
%defattr(644,root,root,755)
%{texmfdist}/doc/psizzl
%{texmfdist}/source/psizzl
%{texmfdist}/tex/psizzl

%files tex-pstricks
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pstricks
%doc %{texmfdist}/doc/generic/pstricks-add
%{texmfdist}/tex/generic/pstricks
%{texmfdist}/tex/latex/pstricks-add
%{texmfdist}/source/generic/pstricks-add
%{texmfdist}/tex/generic/pstricks-add

%files tex-qpxqtx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/qpxqtx
%{texmfdist}/fonts/vf/public/qpxqtx
%{texmfdist}/tex/generic/qpxqtx

%files tex-ruhyphen
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/ruhyphen
%{texmfdist}/source/generic/ruhyphen

%files tex-huhyphen
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/huhyphen

%files tex-spanish
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/spanish-mx
%dir %{texmfdist}/source/latex/mapcodes
%dir %{texmfdist}/source/latex/polyglot
%dir %{texmfdist}/source/latex/polyglot/langs
%dir %{texmfdist}/tex/latex/babelbib
%dir %{texmfdist}/tex/latex/dvdcoll/dcl
%dir %{texmfdist}/tex/texsis
%dir %{texmfdist}/tex/texsis/base
%{texmfdist}/source/generic/babel/spanish.ins
%{texmfdist}/source/generic/babel/spanish.dtx
%{texmfdist}/source/latex/polyglot/langs/spanish.ld
%{texmfdist}/source/latex/polyglot/langs/spanish.ot1
%{texmfdist}/source/latex/mapcodes/spanish.map
%{texmfdist}/source/latex/mapcodes/spanish.dtx
%{texmfdist}/tex/texsis/base/Spanish.txs
%{texmfdist}/tex/generic/babel/spanish.sty
%{texmfdist}/tex/generic/babel/spanish.ldf
%{texmfdist}/tex/latex/spanish-mx
%{texmfdist}/tex/latex/custom-bib/spanish.mbs
%{texmfdist}/tex/latex/babelbib/spanish.bdf
%{texmfdist}/tex/latex/dvdcoll/dcl/spanish.dcl

%files tex-texdraw
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/texdraw
%{texmfdist}/tex/generic/texdraw

%files tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{_mandir}/man1/thumbpdf.1*
%{texmfdist}/tex/generic/thumbpdf
%{texmfdist}/scripts/thumbpdf

%files tex-ukrhyph
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ukrhyph
%{texmfdist}/tex/generic/ukrhyph

%files latex-vietnam
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/vntex
%{texmfdist}/tex/latex/vntex

%files tex-xypic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/xypic
%{texmfdist}/tex/generic/xypic

%files tex-xkeyval
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xkeyval
%{texmfdist}/source/latex/xkeyval
%{texmfdist}/tex/generic/xkeyval
%{texmfdist}/tex/latex/xkeyval

%files fonts-adobe
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/adobe
%{texmfdist}/fonts/afm/adobe
%{texmfdist}/fonts/tfm/adobe
%{texmfdist}/fonts/vf/adobe

%files fonts-larm
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/la
%{texmfdist}/fonts/type1/la/
%{texmfdist}/fonts/enc/larm.enc

%files fonts-ae
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ae
%{texmfdist}/fonts/tfm/public/ae
%{texmfdist}/fonts/vf/public/ae
%{texmfdist}/source/fonts/ae

%files fonts-ams
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/ams
%{texmfdist}/fonts/tfm/public/ams
%{texmfdist}/fonts/map/dvips/ams

%files fonts-antp
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antp
%{texmfdist}/fonts/enc/dvips/antp
%{texmfdist}/fonts/map/dvips/antp
%{texmfdist}/fonts/afm/public/antp
%{texmfdist}/fonts/tfm/public/antp

%files fonts-antt
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antt
%{texmfdist}/fonts/afm/public/antt
%{texmfdist}/fonts/opentype/public/antt
%{texmfdist}/fonts/enc/dvips/antt
%{texmfdist}/fonts/tfm/public/antt
%{texmfdist}/fonts/map/dvips/antt
%{texmfdist}/tex/plain/antt
%{texmfdist}/tex/latex/antt

%files fonts-arphic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/arphic
%{texmfdist}/fonts/afm/arphic
%{texmfdist}/fonts/tfm/arphic
%{texmfdist}/fonts/vf/arphic

%files fonts-bbm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/bbm
%{texmfdist}/fonts/source/public/bbm
%{texmfdist}/fonts/tfm/public/bbm
%{texmfdist}/source/latex/bbm
%{texmfdist}/tex/latex/bbm

%files fonts-bbold
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/bbold
%{texmfdist}/fonts/tfm/public/bbold

%files fonts-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/bitstrea
%{texmfdist}/fonts/tfm/bitstrea
%{texmfdist}/fonts/vf/bitstrea

%files fonts-cc-pl
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cc-pl
%{texmfdist}/fonts/enc/dvips/cc-pl
%{texmfdist}/fonts/tfm/public/cc-pl
%{texmfdist}/fonts/map/dvips/cc-pl

%files fonts-cg
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/cg
%{texmfdist}/fonts/vf/cg

%files fonts-cm
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/fonts
%dir %{texmfdist}/fonts/afm/bluesky
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/pk/ljfour/public
%doc %{texmfdist}/doc/fonts/cm
%{texmfdist}/fonts/afm/bluesky/cm
%{texmfdist}/fonts/map/dvips/cm
%{texmfdist}/fonts/pk/ljfour/public/cm
%{texmfdist}/fonts/source/public/cm
%{texmfdist}/fonts/tfm/public/cm

%files fonts-cmbright
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmbright
%{texmfdist}/fonts/tfm/public/cmbright
%{texmfdist}/source/latex/cmbright
%{texmfdist}/tex/latex/cmbright

%files fonts-cmcyr
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cmcyr
%{texmfdist}/fonts/source/public/cmcyr
%{texmfdist}/fonts/type1/public/cmcyr
%{texmfdist}/fonts/tfm/public/cmcyr
%{texmfdist}/fonts/vf/public/cmcyr
%{texmfdist}/fonts/map/dvips/cmcyr

%files fonts-cmextra
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmextra
%{texmfdist}/fonts/tfm/public/cmextra

%files fonts-cmsuper
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cm-super
%{texmfdist}/fonts/afm/public/cm-super
%{texmfdist}/fonts/enc/dvips/cm-super
%{texmfdist}/fonts/map/dvips/cm-super
%{texmfdist}/fonts/map/vtex/cm-super
%{texmfdist}/fonts/type1/public/cm-super

%files fonts-concmath
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concmath
%{texmfdist}/fonts/source/public/concmath
%{texmfdist}/fonts/tfm/public/concmath
%{texmfdist}/source/latex/concmath
%{texmfdist}/tex/latex/concmath

%files fonts-concrete
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concrete
%{texmfdist}/fonts/source/public/concrete
%{texmfdist}/fonts/tfm/public/concrete

%files fonts-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cs
%{texmfdist}/fonts/enc/dvips/cs
%{texmfdist}/fonts/tfm/public/cs
%{texmfdist}/fonts/map/dvips/cs

%files fonts-ecc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ecc
%{texmfdist}/fonts/source/public/ecc
%{texmfdist}/fonts/tfm/public/ecc

%files fonts-eurosym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eurosym
%{texmfdist}/fonts/source/public/eurosym
%{texmfdist}/fonts/tfm/public/eurosym
%{texmfdist}/fonts/map/dvips/eurosym
%{texmfdist}/source/fonts/eurosym
%{texmfdist}/tex/latex/eurosym

%files fonts-eulervm
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/public/eulervm
%{texmfdist}/fonts/vf/public/eulervm
%{texmfdist}/source/latex/eulervm
%{texmfdist}/tex/latex/eulervm

%files fonts-euxm
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/euxm
%{texmfdist}/fonts/tfm/public/euxm

%files fonts-gothic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/gothic
%{texmfdist}/fonts/source/public/gothic
%{texmfdist}/fonts/type1/public/gothic
%{texmfdist}/fonts/afm/public/gothic
%{texmfdist}/fonts/tfm/public/gothic
%{texmfdist}/fonts/vf/public/gothic
%{texmfdist}/fonts/map/dvips/gothic

%files fonts-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/hoekwater
%{texmfdist}/fonts/tfm/hoekwater
%{texmfdist}/fonts/truetype/hoekwater

%files fonts-jknappen
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/jknappen
%{texmfdist}/fonts/tfm/jknappen

%files fonts-kpfonts
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/fonts
%doc %{texmfdist}/doc/fonts/kpfonts
%{texmfdist}/fonts/afm/public/kpfonts
%{texmfdist}/fonts/map/public/kpfonts
%{texmfdist}/fonts/source/public/kpfonts
%{texmfdist}/fonts/tfm/public/kpfonts
%{texmfdist}/fonts/type1/public/kpfonts
%{texmfdist}/fonts/vf/public/kpfonts
%{texmfdist}/tex/latex/kpfonts

%files fonts-latex
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts/afm/bluesky/latex-fonts
%dir %{texmfdist}/fonts/map/dvips/latex-fonts
%dir %{texmfdist}/fonts/source/public/latex-fonts
%dir %{texmfdist}/fonts/tfm/public/latex-fonts
%doc %{texmfdist}/doc/latex/esint
%{texmfdist}/fonts/afm/bluesky/latex-fonts/*
%{texmfdist}/fonts/map/dvips/latex-fonts/*
%{texmfdist}/fonts/source/public/esint
%{texmfdist}/fonts/source/public/latex-fonts/*
%{texmfdist}/fonts/tfm/public/esint
%{texmfdist}/fonts/tfm/public/latex-fonts/*
%{texmfdist}/source/latex/esint
%{texmfdist}/tex/latex/esint

%files fonts-lh
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lh
%{texmfdist}/fonts/source/lh
%{texmfdist}/metapost/support/charlib/LH
%{texmfdist}/source/fonts/lh
%{texmfdist}/source/latex/lh

%files fonts-lm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lm
%{texmfdist}/fonts/type1/public/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/opentype/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/tfm/public/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
%{texmfdist}/source/fonts/lm
%{texmfdist}/tex/latex/lm

%files fonts-marvosym
%defattr(644,root,root,755)
%dir %{texmfdist}/source/fonts/eurofont
%dir %{texmfdist}/source/fonts/eurofont/marvosym
%dir %{texmfdist}/tex/latex
%doc %{texmfdist}/doc/latex/marvosym
%{texmfdist}/fonts/type1/public/marvosym
%{texmfdist}/fonts/afm/public/marvosym
%{texmfdist}/fonts/tfm/public/marvosym
%{texmfdist}/fonts/map/dvips/marvosym
%{texmfdist}/source/fonts/eurofont/marvosym/*
%{texmfdist}/tex/latex/marvosym

%files fonts-mflogo
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/mflogo
%{texmfdist}/fonts/afm/hoekwater/mflogo
%{texmfdist}/fonts/tfm/public/mflogo
%{texmfdist}/fonts/map/dvips/mflogo
%{texmfdist}/source/latex/mflogo
%{texmfdist}/tex/latex/mflogo

%files fonts-misc
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/misc
%{texmfdist}/fonts/tfm/public/misc
%{texmfdist}/fonts/misc

%files fonts-monotype
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/monotype
%{texmfdist}/fonts/vf/monotype

%files fonts-other
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/yi4latex
%{texmf}/fonts/sfd
%{texmfdist}/fonts/afm/itc
%{texmf}/fonts/map/glyphlist
%{texmfdist}/fonts/map/glyphlist
%{texmfdist}/fonts/source/public/knuthotherfonts
%{texmfdist}/fonts/source/public/yi4latex
%{texmfdist}/fonts/tfm/public/yi4latex

%{texmfdist}/fonts/tfm/public/pslatex
%{texmfdist}/fonts/map/dvips/pslatex
%{texmfdist}/fonts/vf/public/pslatex

%doc %{texmfdist}/doc/fonts/allrunes
%{texmfdist}/fonts/source/public/allrunes
%{texmfdist}/fonts/tfm/public/allrunes
%{texmfdist}/fonts/type1/public/allrunes
%{texmfdist}/source/fonts/allrunes

%doc %{texmfdist}/doc/fonts/antiqua
%{texmfdist}/fonts/map/dvips/antiqua

%{texmfdist}/fonts/source/public/apl
%{texmfdist}/fonts/tfm/public/apl
%{texmfdist}/source/fonts/apl

%{texmfdist}/fonts/afm/arabi
%{texmfdist}/fonts/tfm/arabi
%{texmfdist}/fonts/type1/arabi
%{texmfdist}/fonts/enc/dvips/arabi
%{texmfdist}/fonts/map/dvips/arabi

%{texmfdist}/fonts/map/dvips/arabtex
%{texmfdist}/fonts/source/public/arabtex
%{texmfdist}/fonts/tfm/public/arabtex
%{texmfdist}/fonts/type1/public/arabtex

%doc %{texmfdist}/doc/fonts/archaic
%{texmfdist}/fonts/afm/public/archaic
%{texmfdist}/fonts/map/dvips/archaic
%{texmfdist}/fonts/source/public/archaic
%{texmfdist}/fonts/tfm/public/archaic
%{texmfdist}/fonts/type1/public/archaic
%{texmfdist}/source/fonts/archaic

%doc %{texmfdist}/doc/fonts/arev
%{texmfdist}/fonts/afm/public/arev
%{texmfdist}/fonts/enc/dvips/arev
%{texmfdist}/fonts/map/dvips/arev
%{texmfdist}/fonts/tfm/public/arev
%{texmfdist}/fonts/type1/public/arev
%{texmfdist}/fonts/vf/public/arev
%{texmfdist}/source/fonts/arev

%{texmfdist}/fonts/tfm/vntex/arevvn
%{texmfdist}/fonts/type1/vntex/arevvn

%{texmfdist}/fonts/source/public/ar
%{texmfdist}/fonts/tfm/public/ar

%doc %{texmfdist}/doc/fonts/armenian
%{texmfdist}/fonts/source/public/armenian
%{texmfdist}/fonts/tfm/public/armenian

%{texmfdist}/fonts/map/dvips/arphic

%doc %{texmfdist}/doc/fonts/malayalam
%doc %{texmfdist}/doc/fonts/Asana-Math
%{texmfdist}/fonts/opentype/public/Asana-Math

%doc %{texmfdist}/doc/fonts/ascii
%{texmfdist}/fonts/map/dvips/ascii
%{texmfdist}/fonts/tfm/public/ascii
%{texmfdist}/fonts/type1/public/ascii

%doc %{texmfdist}/doc/fonts/astro
%{texmfdist}/fonts/source/public/astro
%{texmfdist}/fonts/tfm/public/astro

%{texmfdist}/fonts/afm/public/augie
%{texmfdist}/fonts/map/dvips/augie
%{texmfdist}/fonts/tfm/public/augie
%{texmfdist}/fonts/type1/public/augie
%{texmfdist}/fonts/vf/public/augie

%doc %{texmfdist}/doc/fonts/auncial-new
%{texmfdist}/fonts/afm/public/auncial-new
%{texmfdist}/fonts/map/dvips/auncial-new
%{texmfdist}/fonts/tfm/public/auncial-new
%{texmfdist}/fonts/type1/public/auncial-new
%{texmfdist}/source/fonts/auncial-new

%{texmfdist}/fonts/afm/public/aurical
%{texmfdist}/fonts/map/dvips/aurical
%{texmfdist}/fonts/source/public/aurical
%{texmfdist}/fonts/tfm/public/aurical
%{texmfdist}/fonts/type1/public/aurical

%{texmfdist}/fonts/map/dvips/avantgar

%{texmfdist}/fonts/source/public/bangtex
%{texmfdist}/fonts/tfm/public/bangtex

%{texmfdist}/fonts/source/public/barcodes
%{texmfdist}/fonts/tfm/public/barcodes

%{texmfdist}/fonts/source/public/bayer
%{texmfdist}/fonts/tfm/public/bayer

%{texmfdist}/fonts/source/public/bbding
%{texmfdist}/fonts/tfm/public/bbding

%{texmfdist}/fonts/truetype/public

%{texmfdist}/fonts/source/public/bengali
%{texmfdist}/fonts/tfm/public/bengali

%doc %{texmfdist}/doc/fonts/bera
%{texmfdist}/fonts/afm/public/bera
%{texmfdist}/fonts/map/dvips/bera
%{texmfdist}/fonts/map/vtex/bera
%{texmfdist}/fonts/tfm/public/bera
%{texmfdist}/fonts/type1/public/bera
%{texmfdist}/fonts/vf/public/bera

%doc %{texmfdist}/doc/fonts/blacklettert1
%{texmfdist}/fonts/tfm/public/blacklettert1
%{texmfdist}/fonts/vf/public/blacklettert1
%{texmfdist}/source/fonts/blacklettert1

%doc %{texmfdist}/doc/fonts/boisik
%{texmfdist}/fonts/source/public/boisik

%doc %{texmfdist}/doc/fonts/bookhands
%{texmfdist}/fonts/source/public/bookhands

%{texmfdist}/fonts/map/dvips/bookman

%{texmfdist}/fonts/afm/public/brushscr
%{texmfdist}/fonts/map/dvips/brushscr
%{texmfdist}/fonts/tfm/public/brushscr
%{texmfdist}/fonts/type1/public/brushscr
%{texmfdist}/fonts/vf/public/brushscr

%doc %{texmfdist}/doc/fonts/burmese
%{texmfdist}/fonts/map/dvips/burmese
%{texmfdist}/fonts/tfm/public/burmese
%{texmfdist}/fonts/type1/public/burmese

%doc %{texmfdist}/doc/fonts/cns
%{texmfdist}/fonts/tfm/cns

%{texmfdist}/fonts/enc/dvips/c90enc

%{texmfdist}/fonts/source/public/calligra
%{texmfdist}/fonts/tfm/public/calligra

%doc %{texmfdist}/doc/fonts/carolmin-ps
%{texmfdist}/fonts/afm/public/carolmin-ps
%{texmfdist}/fonts/map/dvips/carolmin-ps
%{texmfdist}/fonts/type1/public/carolmin-ps

%{texmfdist}/fonts/source/public/casyl
%{texmfdist}/fonts/tfm/public/casyl

%{texmfdist}/fonts/source/public/cbcoptic
%{texmfdist}/fonts/tfm/public/cbcoptic
%{texmfdist}/fonts/type1/public/cbcoptic

%doc %{texmfdist}/doc/fonts/cbfonts
%{texmfdist}/fonts/enc/dvips/cbfonts
%{texmfdist}/fonts/map/dvips/cbfonts
%{texmfdist}/fonts/source/public/cbfonts
%{texmfdist}/fonts/tfm/public/cbfonts
%{texmfdist}/fonts/type1/public/cbfonts

%doc %{texmfdist}/doc/fonts/charter
%{texmfdist}/fonts/afm/vntex/chartervn
%{texmfdist}/fonts/tfm/vntex/chartervn
%{texmfdist}/fonts/type1/vntex/chartervn
%{texmfdist}/fonts/vf/vntex/chartervn

%{texmfdist}/fonts/source/public/cherokee
%{texmfdist}/fonts/tfm/public/cherokee

%{texmfdist}/fonts/source/public/china2e
%{texmfdist}/fonts/tfm/public/china2e

%doc %{texmfdist}/doc/fonts/cirth
%{texmfdist}/fonts/source/public/cirth
%{texmfdist}/fonts/tfm/public/cirth

%doc %{texmfdist}/doc/fonts/cjhebrew
%{texmfdist}/fonts/afm/public/cjhebrew
%{texmfdist}/fonts/enc/dvips/cjhebrew
%{texmfdist}/fonts/map/dvips/cjhebrew
%{texmfdist}/fonts/tfm/public/cjhebrew
%{texmfdist}/fonts/type1/public/cjhebrew
%{texmfdist}/fonts/vf/public/cjhebrew

%{texmfdist}/fonts/source/public/clock
%{texmfdist}/fonts/tfm/public/clock

%doc %{texmfdist}/doc/fonts/cmastro
%{texmfdist}/fonts/source/public/cmastro
%{texmfdist}/fonts/tfm/public/cmastro

%{texmfdist}/fonts/tfm/vntex/cmbrightvn
%{texmfdist}/fonts/type1/vntex/cmbrightvn

%{texmfdist}/fonts/type1/public/cmex

%{texmfdist}/fonts/afm/public/cm-lgc
%{texmfdist}/fonts/enc/dvips/cm-lgc
%{texmfdist}/fonts/map/dvips/cm-lgc
%{texmfdist}/fonts/ofm/public/cm-lgc
%{texmfdist}/fonts/ovf/public/cm-lgc
%{texmfdist}/fonts/tfm/public/cm-lgc
%{texmfdist}/fonts/type1/public/cm-lgc
%{texmfdist}/fonts/vf/public/cm-lgc

%doc %{texmfdist}/doc/fonts/cmpica
%{texmfdist}/fonts/source/public/cmpica
%{texmfdist}/fonts/tfm/public/cmpica


%{texmfdist}/fonts/tfm/vntex/comicsansvn
%{texmfdist}/fonts/type1/vntex/comicsansvn
%{texmfdist}/fonts/vf/vntex/comicsansvn

%{texmfdist}/fonts/tfm/vntex/concretevn
%{texmfdist}/fonts/type1/vntex/concretevn

%{texmfdist}/fonts/afm/ibm
%{texmfdist}/fonts/tfm/ibm
%{texmfdist}/fonts/vf/ibm
%{texmfdist}/fonts/map/dvips/courier
%{texmfdist}/fonts/tfm/cspsfonts-adobe
%{texmfdist}/fonts/vf/cspsfonts-adobe

%doc %{texmfdist}/doc/fonts/croatian
%{texmfdist}/fonts/source/public/croatian

%{texmfdist}/fonts/afm/public/cryst
%{texmfdist}/fonts/source/public/cryst
%{texmfdist}/fonts/tfm/public/cryst
%{texmfdist}/fonts/type1/public/cryst

%{texmfdist}/fonts/source/public/ctib
%{texmfdist}/fonts/tfm/public/ctib

%doc %{texmfdist}/doc/fonts/cyklop
%{texmfdist}/fonts/afm/public/cyklop
%{texmfdist}/fonts/enc/dvips/cyklop
%{texmfdist}/fonts/map/dvips/cyklop
%{texmfdist}/fonts/opentype/public/cyklop
%{texmfdist}/fonts/tfm/public/cyklop
%{texmfdist}/fonts/type1/public/cyklop

%{texmfdist}/fonts/source/public/dancers
%{texmfdist}/fonts/tfm/public/dancers

%doc %{texmfdist}/doc/fonts/dice
%{texmfdist}/fonts/source/public/dice
%{texmfdist}/fonts/tfm/public/dice

%doc %{texmfdist}/doc/fonts/dictsym
%{texmfdist}/fonts/afm/public/dictsym
%{texmfdist}/fonts/map/dvips/dictsym
%{texmfdist}/fonts/map/vtex/dictsym
%{texmfdist}/fonts/tfm/public/dictsym
%{texmfdist}/fonts/type1/public/dictsym

%doc %{texmfdist}/doc/fonts/dingbat
%{texmfdist}/fonts/tfm/public/dingbat
%{texmfdist}/source/fonts/dingbat

%doc %{texmfdist}/doc/fonts/doublestroke
%{texmfdist}/fonts/map/dvips/doublestroke
%{texmfdist}/fonts/source/public/doublestroke
%{texmfdist}/fonts/tfm/public/doublestroke
%{texmfdist}/fonts/type1/public/doublestroke

%doc %{texmfdist}/doc/fonts/duerer
%{texmfdist}/fonts/source/public/duerer
%{texmfdist}/fonts/tfm/public/duerer

%doc %{texmfdist}/doc/fonts/ean
%{texmfdist}/fonts/source/public/ean
%{texmfdist}/fonts/tfm/public/ean

%doc %{texmfdist}/doc/fonts/eiad
%{texmfdist}/fonts/source/public/eiad
%{texmfdist}/fonts/tfm/public/eiad

%doc %{texmfdist}/doc/fonts/elvish
%{texmfdist}/fonts/source/public/elvish
%{texmfdist}/fonts/tfm/public/elvish

%doc %{texmfdist}/doc/fonts/epigrafica
%{texmfdist}/fonts/afm/public/epigrafica
%{texmfdist}/fonts/enc/dvips/epigrafica
%{texmfdist}/fonts/map/dvips/epigrafica
%{texmfdist}/fonts/tfm/public/epigrafica
%{texmfdist}/fonts/type1/public/epigrafica
%{texmfdist}/fonts/vf/public/epigrafica

%{texmfdist}/fonts/map/dvips/epiolmec
%{texmfdist}/fonts/tfm/public/epiolmec
%{texmfdist}/fonts/type1/public/epiolmec

%doc %{texmfdist}/doc/fonts/esint-type1
%{texmfdist}/fonts/map/dvips/esint-type1
%{texmfdist}/fonts/type1/public/esint-type1

%{texmfdist}/fonts/ofm/public/ethiop
%{texmfdist}/fonts/ovf/public/ethiop
%{texmfdist}/fonts/ovp/public/ethiop
%{texmfdist}/fonts/source/public/ethiop
%{texmfdist}/fonts/tfm/public/ethiop

%{texmfdist}/fonts/map/dvips/ethiop-t1
%{texmfdist}/fonts/type1/public/ethiop-t1

%doc %{texmfdist}/doc/fonts/euro-ce
%{texmfdist}/fonts/source/public/euro-ce
%{texmfdist}/fonts/tfm/public/euro-ce

%doc %{texmfdist}/doc/fonts/eurofont
%{texmfdist}/fonts/map/dvips/eurofont
%{texmfdist}/source/fonts/eurofont

%doc %{texmfdist}/doc/fonts/feyn
%{texmfdist}/fonts/source/public/feyn
%{texmfdist}/fonts/tfm/public/feyn
%{texmfdist}/source/fonts/feyn

%doc %{texmfdist}/doc/fonts/fge
%{texmfdist}/fonts/source/public/fge
%{texmfdist}/fonts/tfm/public/fge
%{texmfdist}/source/fonts/fge

%{texmfdist}/fonts/map/dvips/foekfont
%{texmfdist}/fonts/tfm/public/foekfont
%{texmfdist}/fonts/type1/public/foekfont

%doc %{texmfdist}/doc/fonts/fonetika
%{texmfdist}/fonts/afm/public/fonetika
%{texmfdist}/fonts/map/dvips/fonetika
%{texmfdist}/fonts/tfm/public/fonetika
%{texmfdist}/fonts/type1/public/fonetika

%doc %{texmfdist}/doc/fonts/fourier
%{texmfdist}/fonts/afm/public/fourier
%{texmfdist}/fonts/map/dvips/fourier
%{texmfdist}/fonts/tfm/public/fourier
%{texmfdist}/fonts/type1/public/fourier
%{texmfdist}/fonts/vf/public/fourier
%{texmfdist}/source/fonts/fourier

%doc %{texmfdist}/doc/fonts/fouriernc
%{texmfdist}/fonts/afm/public/fouriernc
%{texmfdist}/fonts/tfm/public/fouriernc
%{texmfdist}/fonts/vf/public/fouriernc

%doc %{texmfdist}/doc/fonts/frcursive
%{texmfdist}/fonts/source/public/frcursive
%{texmfdist}/fonts/tfm/public/frcursive
%{texmfdist}/source/fonts/frcursive

%doc %{texmfdist}/doc/fonts/futhark
%{texmfdist}/fonts/source/public/futhark
%{texmfdist}/fonts/tfm/public/futhark

%{texmfdist}/fonts/afm/public/garuda
%{texmfdist}/fonts/map/dvips/garuda
%{texmfdist}/fonts/tfm/public/garuda
%{texmfdist}/fonts/type1/public/garuda

%doc %{texmfdist}/doc/fonts/genealogy
%{texmfdist}/fonts/source/public/genealogy
%{texmfdist}/fonts/tfm/public/genealogy

%doc %{texmfdist}/doc/fonts/gfsartemisia
%{texmfdist}/fonts/afm/public/gfsartemisia
%{texmfdist}/fonts/enc/dvips/gfsartemisia
%{texmfdist}/fonts/map/dvips/gfsartemisia
%{texmfdist}/fonts/opentype/public/gfsartemisia
%{texmfdist}/fonts/tfm/public/gfsartemisia
%{texmfdist}/fonts/type1/public/gfsartemisia
%{texmfdist}/fonts/vf/public/gfsartemisia

%doc %{texmfdist}/doc/fonts/gfsbaskerville
%{texmfdist}/fonts/afm/public/gfsbaskerville
%{texmfdist}/fonts/enc/dvips/gfsbaskerville
%{texmfdist}/fonts/map/dvips/gfsbaskerville
%{texmfdist}/fonts/opentype/public/gfsbaskerville
%{texmfdist}/fonts/tfm/public/gfsbaskerville
%{texmfdist}/fonts/type1/public/gfsbaskerville
%{texmfdist}/fonts/vf/public/gfsbaskerville

%doc %{texmfdist}/doc/fonts/gfsbodoni
%{texmfdist}/fonts/afm/public/gfsbodoni
%{texmfdist}/fonts/enc/dvips/gfsbodoni
%{texmfdist}/fonts/map/dvips/gfsbodoni
%{texmfdist}/fonts/opentype/public/gfsbodoni
%{texmfdist}/fonts/tfm/public/gfsbodoni
%{texmfdist}/fonts/type1/public/gfsbodoni
%{texmfdist}/fonts/vf/public/gfsbodoni

%doc %{texmfdist}/doc/fonts/gfscomplutum
%{texmfdist}/fonts/afm/public/gfscomplutum
%{texmfdist}/fonts/enc/dvips/gfscomplutum
%{texmfdist}/fonts/map/dvips/gfscomplutum
%{texmfdist}/fonts/opentype/public/gfscomplutum
%{texmfdist}/fonts/tfm/public/gfscomplutum
%{texmfdist}/fonts/type1/public/gfscomplutum
%{texmfdist}/fonts/vf/public/gfscomplutum

%doc %{texmfdist}/doc/fonts/gfsdidot
%{texmfdist}/fonts/afm/public/gfsdidot
%{texmfdist}/fonts/enc/dvips/gfsdidot
%{texmfdist}/fonts/map/dvips/gfsdidot
%{texmfdist}/fonts/opentype/public/gfsdidot
%{texmfdist}/fonts/tfm/public/gfsdidot
%{texmfdist}/fonts/type1/public/gfsdidot
%{texmfdist}/fonts/vf/public/gfsdidot

%doc %{texmfdist}/doc/fonts/gfsneohellenic
%{texmfdist}/fonts/afm/public/gfsneohellenic
%{texmfdist}/fonts/enc/dvips/gfsneohellenic
%{texmfdist}/fonts/map/dvips/gfsneohellenic
%{texmfdist}/fonts/opentype/public/gfsneohellenic
%{texmfdist}/fonts/tfm/public/gfsneohellenic
%{texmfdist}/fonts/type1/public/gfsneohellenic
%{texmfdist}/fonts/vf/public/gfsneohellenic

%doc %{texmfdist}/doc/fonts/gfsporson
%{texmfdist}/fonts/afm/public/gfsporson
%{texmfdist}/fonts/enc/dvips/gfsporson
%{texmfdist}/fonts/map/dvips/gfsporson
%{texmfdist}/fonts/opentype/public/gfsporson
%{texmfdist}/fonts/tfm/public/gfsporson
%{texmfdist}/fonts/type1/public/gfsporson
%{texmfdist}/fonts/vf/public/gfsporson

%doc %{texmfdist}/doc/fonts/gfssolomos
%{texmfdist}/fonts/afm/public/gfssolomos
%{texmfdist}/fonts/enc/dvips/gfssolomos
%{texmfdist}/fonts/map/dvips/gfssolomos
%{texmfdist}/fonts/opentype/public/gfssolomos
%{texmfdist}/fonts/tfm/public/gfssolomos
%{texmfdist}/fonts/type1/public/gfssolomos
%{texmfdist}/fonts/vf/public/gfssolomos

%doc %{texmfdist}/doc/fonts/greenpoint
%{texmfdist}/fonts/source/public/greenpoint
%{texmfdist}/fonts/tfm/public/greenpoint

%{texmfdist}/fonts/afm/groff
%{texmfdist}/fonts/enc/dvips/groff
%{texmfdist}/fonts/map/dvips/groff
%{texmfdist}/fonts/tfm/groff
%{texmfdist}/fonts/type1/groff

%doc %{texmfdist}/doc/fonts/grotesq
%{texmfdist}/fonts/map/dvips/grotesq

%{texmfdist}/fonts/afm/vntex/grotesqvn
%{texmfdist}/fonts/tfm/vntex/grotesqvn
%{texmfdist}/fonts/type1/vntex/grotesqvn

%{texmfdist}/fonts/afm/public/grverb
%{texmfdist}/fonts/map/dvips/grverb
%{texmfdist}/fonts/tfm/public/grverb
%{texmfdist}/fonts/type1/public/grverb
%{texmfdist}/fonts/vf/public/grverb

%{texmfdist}/fonts/source/public/hands
%{texmfdist}/fonts/tfm/public/hands

%{texmfdist}/fonts/afm/jmn
%{texmfdist}/fonts/tfm/jmn
%{texmfdist}/fonts/type1/jmn

%{texmfdist}/fonts/map/dvips/helvetic

%doc %{texmfdist}/doc/fonts/hfbright
%{texmfdist}/fonts/afm/public/hfbright
%{texmfdist}/fonts/enc/dvips/hfbright
%{texmfdist}/fonts/map/dvips/hfbright
%{texmfdist}/fonts/type1/public/hfbright
%{texmfdist}/source/fonts/hfbright

%doc %{texmfdist}/doc/fonts/hfoldsty
%{texmfdist}/fonts/tfm/public/hfoldsty
%{texmfdist}/fonts/vf/public/hfoldsty
%{texmfdist}/source/fonts/hfoldsty

%doc %{texmfdist}/doc/fonts/ibygrk
%{texmfdist}/tex/generic/ibygrk
%{texmfdist}/fonts/afm/public/ibygrk
%{texmfdist}/fonts/enc/dvips/ibygrk
%{texmfdist}/fonts/map/dvips/ibygrk
%{texmfdist}/fonts/source/public/ibygrk
%{texmfdist}/fonts/tfm/public/ibygrk
%{texmfdist}/fonts/type1/public/ibygrk

%doc %{texmfdist}/doc/fonts/ifsym
%{texmfdist}/fonts/source/public/ifsym
%{texmfdist}/fonts/tfm/public/ifsym

%doc %{texmfdist}/doc/fonts/initials
%{texmfdist}/fonts/afm/public/initials
%{texmfdist}/fonts/map/dvips/initials
%{texmfdist}/fonts/tfm/public/initials
%{texmfdist}/fonts/type1/public/initials

%doc %{texmfdist}/doc/fonts/itrans
%{texmfdist}/fonts/afm/public/itrans
%{texmfdist}/fonts/source/public/itrans
%{texmfdist}/fonts/tfm/public/itrans
%{texmfdist}/fonts/type1/public/itrans

%doc %{texmfdist}/doc/fonts/iwona
%{texmfdist}/fonts/afm/public/iwona
%{texmfdist}/fonts/enc/dvips/iwona
%{texmfdist}/fonts/map/dvips/iwona
%{texmfdist}/fonts/opentype/public/iwona
%{texmfdist}/fonts/tfm/public/iwona
%{texmfdist}/fonts/type1/public/iwona

%{texmfdist}/fonts/enc/dvips/jmn
%{texmfdist}/fonts/map/dvips/jmn

%doc %{texmfdist}/doc/fonts/kdgreek
%{texmfdist}/fonts/source/public/kdgreek
%{texmfdist}/fonts/tfm/public/kdgreek

%{texmfdist}/fonts/afm/public/kerkis
%{texmfdist}/fonts/enc/dvips/kerkis
%{texmfdist}/fonts/map/dvips/kerkis
%{texmfdist}/fonts/tfm/public/kerkis
%{texmfdist}/fonts/type1/public/kerkis
%{texmfdist}/fonts/vf/public/kerkis

%doc %{texmfdist}/doc/fonts/kixfont
%{texmfdist}/fonts/source/public/kixfont
%{texmfdist}/fonts/tfm/public/kixfont

%dir %{texmfdist}/fonts/map/public
%doc %{texmfdist}/doc/fonts/kurier
%{texmfdist}/fonts/afm/public/kurier
%{texmfdist}/fonts/enc/dvips/kurier
%{texmfdist}/fonts/map/dvips/kurier
%{texmfdist}/fonts/opentype/public/kurier
%{texmfdist}/fonts/tfm/public/kurier
%{texmfdist}/fonts/type1/public/kurier

%doc %{texmfdist}/doc/fonts/levy
%{texmfdist}/fonts/source/public/levy

%doc %{texmfdist}/doc/fonts/lfb
%{texmfdist}/fonts/source/public/lfb
%{texmfdist}/fonts/tfm/public/lfb

%doc %{texmfdist}/doc/fonts/libertine
%{texmfdist}/fonts/afm/public/libertine
%{texmfdist}/fonts/enc/dvips/libertine
%{texmfdist}/fonts/map/dvips/libertine
%{texmfdist}/fonts/tfm/public/libertine
%{texmfdist}/fonts/type1/public/libertine
%{texmfdist}/fonts/vf/public/libertine

%doc %{texmfdist}/doc/fonts/linearA
%{texmfdist}/fonts/afm/public/linearA
%{texmfdist}/fonts/map/dvips/linearA
%{texmfdist}/fonts/tfm/public/linearA
%{texmfdist}/fonts/type1/public/linearA
%{texmfdist}/source/fonts/linearA

%{texmfdist}/fonts/source/public/logic
%{texmfdist}/fonts/tfm/public/logic

%doc %{texmfdist}/doc/fonts/lxfonts
%{texmfdist}/fonts/map/dvips/lxfonts
%{texmfdist}/fonts/source/public/lxfonts
%{texmfdist}/fonts/tfm/public/lxfonts
%{texmfdist}/fonts/type1/public/lxfonts

%doc %{texmfdist}/doc/fonts/ly1
%{texmfdist}/fonts/map/dvips/ly1

%{texmfdist}/fonts/source/public/malayalam
%{texmfdist}/fonts/tfm/public/malayalam

%{texmfdist}/fonts/map/dvips/manfnt

%{texmfdist}/fonts/map/dvips/mathdesign

%{texmfdist}/fonts/tfm/public/mathpazo
%{texmfdist}/fonts/vf/public/mathpazo

%{texmfdist}/fonts/afm/mathdesign
%{texmfdist}/fonts/tfm/mathdesign
%{texmfdist}/fonts/type1/mathdesign
%{texmfdist}/fonts/vf/mathdesign

%{texmfdist}/fonts/enc/dvips/mnsymbol
%{texmfdist}/fonts/map/dvips/mnsymbol
%dir %{texmfdist}/fonts/map/vtex
%{texmfdist}/fonts/map/vtex/mnsymbol
%{texmfdist}/fonts/opentype/public/mnsymbol
%{texmfdist}/fonts/source/public/mnsymbol
%{texmfdist}/fonts/tfm/public/mnsymbol
%{texmfdist}/fonts/type1/public/mnsymbol

%{texmfdist}/fonts/map/dvips/montex
%{texmfdist}/fonts/source/public/montex
%{texmfdist}/fonts/tfm/public/montex
%{texmfdist}/fonts/type1/public/montex

%{texmfdist}/fonts/tfm/vntex/mscorevn
%{texmfdist}/fonts/vf/vntex/mscorevn

%doc %{texmfdist}/doc/generic/musixtex
%{texmfdist}/fonts/map/dvips/musixtex
%{texmfdist}/fonts/source/public/musixtex
%{texmfdist}/fonts/tfm/public/musixtex
%{texmfdist}/fonts/type1/public/musixtex

%{texmfdist}/fonts/source/public/mxd
%{texmfdist}/fonts/tfm/public/mxd

%{texmfdist}/fonts/source/public/mxedruli
%{texmfdist}/fonts/tfm/public/mxedruli

%{texmfdist}/fonts/map/dvips/ncntrsbk

%doc %{texmfdist}/doc/fonts/nkarta
%{texmfdist}/fonts/source/public/nkarta
%{texmfdist}/fonts/tfm/public/nkarta

%{texmfdist}/fonts/afm/public/norasi
%{texmfdist}/fonts/map/dvips/norasi
%{texmfdist}/fonts/tfm/public/norasi
%{texmfdist}/fonts/type1/public/norasi

%{texmfdist}/fonts/source/public/oca

%{texmfdist}/fonts/afm/public/ocherokee
%{texmfdist}/fonts/map/dvips/ocherokee
%{texmfdist}/fonts/ofm/public/ocherokee
%{texmfdist}/fonts/ovf/public/ocherokee
%{texmfdist}/fonts/ovp/public/ocherokee
%{texmfdist}/fonts/tfm/public/ocherokee
%{texmfdist}/fonts/type1/public/ocherokee

%{texmfdist}/fonts/source/public/ogham
%{texmfdist}/fonts/tfm/public/ogham

%doc %{texmfdist}/doc/fonts/oinuit
%{texmfdist}/fonts/map/dvips/oinuit
%{texmfdist}/fonts/ofm/public/oinuit
%{texmfdist}/fonts/ovf/public/oinuit
%{texmfdist}/fonts/tfm/public/oinuit
%{texmfdist}/fonts/type1/public/oinuit

%{texmfdist}/fonts/source/public/osmanian

%doc %{texmfdist}/doc/fonts/ot2cyr
%{texmfdist}/fonts/map/dvips/ot2cyr
%{texmfdist}/source/fonts/ot2cyr

%{texmfdist}/fonts/ofm/public/otibet
%{texmfdist}/fonts/ovf/public/otibet
%{texmfdist}/fonts/ovp/public/otibet
%{texmfdist}/fonts/source/public/otibet
%{texmfdist}/fonts/tfm/public/otibet

%doc %{texmfdist}/doc/fonts/pacioli
%{texmfdist}/fonts/source/public/pacioli
%{texmfdist}/fonts/tfm/public/pacioli

%{texmfdist}/fonts/map/dvips/palatino

%doc %{texmfdist}/doc/fonts/phaistos
%{texmfdist}/fonts/afm/public/phaistos
%{texmfdist}/fonts/map/dvips/phaistos
%{texmfdist}/fonts/opentype/public/phaistos
%{texmfdist}/fonts/tfm/public/phaistos
%{texmfdist}/fonts/type1/public/phaistos
%{texmfdist}/source/fonts/phaistos

%{texmfdist}/fonts/opentype/public/philokalia

%doc %{texmfdist}/doc/fonts/phonetic
%{texmfdist}/fonts/source/public/phonetic
%{texmfdist}/fonts/tfm/public/phonetic
%{texmfdist}/source/fonts/phonetic

%{texmfdist}/source/fonts/malayalam

%{texmfdist}/fonts/source/public/punk
%{texmfdist}/fonts/tfm/public/punk

%{texmfdist}/fonts/tfm/public/relenc
%{texmfdist}/fonts/vf/public/relenc

%doc %{texmfdist}/doc/fonts/rsfs
%{texmfdist}/fonts/map/dvips/rsfs

%{texmfdist}/fonts/map/dvips/sanskrit
%{texmfdist}/fonts/source/public/sanskrit
%{texmfdist}/fonts/tfm/public/sanskrit
%{texmfdist}/fonts/type1/public/sanskrit

%{texmfdist}/fonts/source/public/sauter

%doc %{texmfdist}/doc/fonts/semaphor
%{texmfdist}/fonts/afm/public/semaphor
%{texmfdist}/fonts/enc/dvips/semaphor
%{texmfdist}/fonts/map/dvips/semaphor
%{texmfdist}/fonts/opentype/public/semaphor
%{texmfdist}/fonts/source/public/semaphor
%{texmfdist}/fonts/tfm/public/semaphor
%{texmfdist}/fonts/type1/public/semaphor

%{texmfdist}/fonts/source/public/simpsons

%doc %{texmfdist}/doc/fonts/skaknew
%{texmfdist}/fonts/afm/public/skaknew
%{texmfdist}/fonts/map/dvips/skaknew
%{texmfdist}/fonts/map/vtex/skaknew
%{texmfdist}/fonts/tfm/public/skaknew
%{texmfdist}/fonts/type1/public/skaknew

%{texmfdist}/fonts/source/public/skull

%{texmfdist}/fonts/source/public/soyombo
%{texmfdist}/fonts/tfm/public/soyombo

%doc %{texmfdist}/doc/fonts/staves
%{texmfdist}/fonts/map/dvips/staves
%{texmfdist}/fonts/tfm/public/staves
%{texmfdist}/fonts/type1/public/staves

%{texmfdist}/fonts/map/dvips/stmaryrd
%{texmfdist}/fonts/source/public/stmaryrd

%{texmfdist}/fonts/map/dvips/symbol

%{texmfdist}/fonts/afm/public/tabvar
%{texmfdist}/fonts/map/dvips/tabvar
%{texmfdist}/fonts/tfm/public/tabvar
%{texmfdist}/fonts/type1/public/tabvar


%{texmfdist}/fonts/source/public/tapir
%{texmfdist}/fonts/type1/public/tapir

%{texmfdist}/fonts/enc/dvips/tengwarscript
%{texmfdist}/fonts/map/dvips/tengwarscript
%{texmfdist}/fonts/tfm/public/tengwarscript
%{texmfdist}/fonts/vf/public/tengwarscript

%{texmfdist}/doc/fonts/pclnfss
%{texmfdist}/source/fonts/pclnfss

%doc %{texmfdist}/doc/fonts/tex-gyre
%{texmfdist}/fonts/afm/public/tex-gyre
%{texmfdist}/fonts/enc/dvips/tex-gyre
%{texmfdist}/fonts/map/dvips/tex-gyre
%{texmfdist}/fonts/opentype/public/tex-gyre
%{texmfdist}/fonts/tfm/public/tex-gyre
%{texmfdist}/fonts/type1/public/tex-gyre

%{texmfdist}/fonts/map/dvips/times


%doc %{texmfdist}/doc/fonts/timing
%{texmfdist}/fonts/source/public/timing
%{texmfdist}/fonts/tfm/public/timing

%doc %{texmfdist}/doc/fonts/tipa
%{texmfdist}/fonts/map/dvips/tipa
%{texmfdist}/fonts/source/public/tipa
%{texmfdist}/fonts/tfm/public/tipa
%{texmfdist}/fonts/type1/public/tipa

%{texmfdist}/fonts/afm/public/trajan
%{texmfdist}/fonts/map/dvips/trajan
%{texmfdist}/fonts/tfm/public/trajan
%{texmfdist}/fonts/type1/public/trajan


%{texmfdist}/fonts/tfm/vntex/txttvn
%{texmfdist}/fonts/type1/vntex/txttvn

%{texmfdist}/fonts/map/dvips/uhc

%doc %{texmfdist}/doc/fonts/umtypewriter
%{texmfdist}/fonts/opentype/public/umtypewriter

%doc %{texmfdist}/doc/fonts/universa
%{texmfdist}/fonts/source/public/universa
%{texmfdist}/fonts/tfm/public/universa
%{texmfdist}/source/fonts/universa

%{texmfdist}/fonts/afm/public/velthuis
%{texmfdist}/fonts/map/dvips/velthuis
%{texmfdist}/fonts/source/public/velthuis
%{texmfdist}/fonts/tfm/public/velthuis
%{texmfdist}/fonts/type1/public/velthuis

%{texmfdist}/fonts/enc/dvips/vntex/*

%{texmfdist}/fonts/afm/vntex/vntopia
%{texmfdist}/fonts/tfm/vntex/vntopia
%{texmfdist}/fonts/type1/vntex/vntopia
%{texmfdist}/fonts/vf/vntex/vntopia

%{texmfdist}/fonts/map/dvips/wadalab

%doc %{texmfdist}/doc/fonts/wasy
%{texmfdist}/fonts/afm/public/wasy
%{texmfdist}/fonts/map/dvips/wasy
%{texmfdist}/fonts/type1/public/wasy

%{texmfdist}/fonts/source/public/wnri
%{texmfdist}/fonts/tfm/public/wnri

%{texmfdist}/fonts/source/public/wsuipa
%{texmfdist}/fonts/tfm/public/wsuipa

%{texmfdist}/fonts/source/public/xbmc
%{texmfdist}/fonts/tfm/public/xbmc

%doc %{texmfdist}/doc/fonts/xq
%{texmfdist}/fonts/source/public/xq
%{texmfdist}/fonts/tfm/public/xq

%{texmfdist}/fonts/source/public/yannisgr

%{texmfdist}/fonts/map/dvips/yhmath
%{texmfdist}/fonts/source/public/yhmath
%{texmfdist}/fonts/tfm/public/yhmath
%{texmfdist}/fonts/type1/public/yhmath
%{texmfdist}/fonts/vf/public/yhmath

%{texmfdist}/fonts/map/dvips/zapfchan
%{texmfdist}/fonts/tfm/urw35vf

%{texmfdist}/fonts/map/dvips/zapfding

%{texmfdist}/fonts/map/dvips/zefonts
%{texmfdist}/fonts/tfm/public/zefonts
%{texmfdist}/fonts/vf/public/zefonts

%files fonts-omega
%defattr(644,root,root,755)
%dir %{texmfdist}/omega
%dir %{texmfdist}/omega/ocp
%dir %{texmfdist}/omega/otp
%{texmfdist}/fonts/ofm/public/omega
%{texmfdist}/fonts/type1/public/omega
%{texmfdist}/fonts/afm/public/omega
%{texmfdist}/fonts/ovp/public/omega
%{texmfdist}/fonts/tfm/public/omega
%{texmfdist}/fonts/ovf/public/omega
%{texmfdist}/fonts/map/dvips/omega
%{texmfdist}/omega/ocp/omega
%{texmfdist}/omega/otp/omega
%{texmfdist}/tex/plain/omega

%files fonts-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pl
%dir %{texmf}/scripts/texlive
%{texmfdist}/fonts/source/public/pl
%{texmfdist}/fonts/type1/public/pl
%{texmfdist}/fonts/afm/public/pl
%{texmfdist}/fonts/enc/dvips/pl
%{texmfdist}/fonts/tfm/public/pl
%{texmfdist}/fonts/map/dvips/pl

%files fonts-px
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pxfonts
%dir %{texmfdist}/fonts/map/dvips/pxfonts
%dir %{texmfdist}/tex/latex/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts/pxfonts.map
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/tfm/public/pxfonts
%{texmfdist}/fonts/type1/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts
%{texmfdist}/tex/latex/pxfonts/pxfonts.sty

%files fonts-qpxqtx
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/public/qpxqtx
%{texmfdist}/fonts/vf/public/qpxqtx

%files fonts-rsfs
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/rsfs
%{texmfdist}/fonts/tfm/public/rsfs

%files fonts-stmaryrd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/stmaryrd
%{texmfdist}/source/fonts/stmaryrd
%{texmfdist}/fonts/tfm/public/stmaryrd

%files fonts-tx
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/txfonts/txfonts.map
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/tfm/public/txfonts
%{texmfdist}/fonts/vf/public/txfonts

%files fonts-uhc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/uhc
%{texmfdist}/fonts/afm/uhc
%{texmfdist}/fonts/tfm/uhc
%{texmfdist}/fonts/vf/uhc

%files fonts-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/urw
%{texmfdist}/fonts/tfm/urw
%{texmfdist}/fonts/vf/urw

%files fonts-urwvn
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/vntex/urwvn
%{texmfdist}/fonts/tfm/vntex/urwvn
%{texmfdist}/fonts/type1/vntex/urwvn
%{texmfdist}/fonts/vf/vntex/urwvn

%files fonts-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/vntex
%{texmfdist}/fonts/source/vntex/vnr
%{texmfdist}/fonts/tfm/vntex/vnr

%files fonts-urw35vf
%defattr(644,root,root,755)
%{texmfdist}/fonts/vf/urw35vf

%files fonts-wadalab
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/wadalab
%{texmfdist}/fonts/afm/wadalab
%{texmfdist}/fonts/tfm/wadalab
%{texmfdist}/fonts/vf/wadalab

%files fonts-wasy
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/wasy
%{texmfdist}/fonts/tfm/public/wasy

%files fonts-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/xypic
%{texmfdist}/fonts/source/public/xypic
%{texmfdist}/fonts/tfm/public/xypic

%files fonts-yandy
%defattr(644,root,root,755)
%{texmfdist}/source/fonts/eurofont/marvosym/tfmfiles/yandy

%files fonts-type1-antp
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/antp

%files fonts-type1-antt
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/antt

%files fonts-type1-arphic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/arphic

%files fonts-type1-belleek
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/belleek
%{texmfdist}/source/latex/belleek
%{texmfdist}/fonts/type1/public/belleek
%{texmfdist}/fonts/map/dvips/belleek

%files fonts-type1-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/bitstrea

%files fonts-type1-bluesky
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/bluesky

%files fonts-type1-cc-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cc-pl
%{texmfdist}/fonts/type1/public/cc-pl

%files fonts-type1-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/cs

%files fonts-type1-eurosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/eurosym

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/hoekwater

%files fonts-type1-fpl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/fpl
%{texmfdist}/fonts/afm/public/fpl
%{texmfdist}/fonts/type1/public/fpl
%{texmfdist}/source/fonts/fpl

%files fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/mathpazo
%{texmfdist}/fonts/type1/public/mathpazo

%files fonts-type1-omega
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/omega

%files fonts-type1-pl
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pl

%files fonts-type1-px
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pxfonts

%files fonts-type1-tx
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/txfonts

%files fonts-type1-uhc
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/uhc

%files fonts-type1-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/urw

%files fonts-type1-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/vntex/vnr

%files fonts-type1-wadalab
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/wadalab

%files fonts-type1-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/xypic

%files afm2pl
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex
%attr(755,root,root) %{_bindir}/afm2pl
%{_mandir}/man1/afm2pl*
%dir %{texmf}/fonts/lig
%{texmf}/fonts/lig/afm2pl
%{texmf}/tex/latex/afm2pl

%files bbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bbox
%{_mandir}/man1/bbox*

%files cefutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cef*
%dir %{texmfdist}/tex/latex/cjk
%dir %{texmfdist}/doc/latex/cjk
%doc %{texmfdist}/doc/latex/cjk/doc
%doc %{texmfdist}/doc/latex/cjk/examples
%{texmfdist}/source/latex/cjk
%{texmfdist}/tex/latex/cjk/CEF

%files detex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/detex
%{_mandir}/man1/detex*

%files dviutils
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/dviasm
%dir %{texmf}/fonts/cmap
%doc %{texmf}/fonts/cmap/README
%attr(755,root,root) %{_bindir}/disdvi
%attr(755,root,root) %{_bindir}/dt2dv
%attr(755,root,root) %{_bindir}/dv2dt
%attr(755,root,root) %{_bindir}/dvi2tty
%attr(755,root,root) %{_bindir}/dviasm
%attr(755,root,root) %{_bindir}/dvibook
%attr(755,root,root) %{_bindir}/dviconcat
%attr(755,root,root) %{_bindir}/dvidvi
%attr(755,root,root) %{_bindir}/dvigif
%attr(755,root,root) %{_bindir}/dvipdfmx
%attr(755,root,root) %{_bindir}/dvipos
%attr(755,root,root) %{_bindir}/dviselect
%attr(755,root,root) %{_bindir}/dvitodvi
%attr(755,root,root) %{texmfdist}/scripts/dviasm/dviasm*
%{_mandir}/man1/dt2dv*
%{_mandir}/man1/dv2dt*
%{_mandir}/man1/dvi2tty*
%{_mandir}/man1/dvibook*
%{_mandir}/man1/dviconcat*
%{_mandir}/man1/dvidvi*
%{_mandir}/man1/dvigif*
%{_mandir}/man1/dvipos*
%{_mandir}/man1/dviselect*
%{_mandir}/man1/dvitodvi*
%{texmf}/dvipdfmx
%{texmf}/fonts/cmap/dvipdfmx
%{texmf}/fonts/map/dvipdfmx

%files psutils
%defattr(644,root,root,755)
%dir %{texmf}/scripts/ps2eps
%doc %{texmfdist}/doc/epspdf
%attr(755,root,root) %{_bindir}/epsffit
%attr(755,root,root) %{_bindir}/epspdf
%attr(755,root,root) %{_bindir}/epspdftk
%attr(755,root,root) %{_bindir}/extractres
%attr(755,root,root) %{_bindir}/fix*
%attr(755,root,root) %{_bindir}/getafm
%attr(755,root,root) %{_bindir}/includeres
%attr(755,root,root) %{_bindir}/ps2eps
%attr(755,root,root) %{_bindir}/psbook
%attr(755,root,root) %{_bindir}/psmerge
%attr(755,root,root) %{_bindir}/psnup
%attr(755,root,root) %{_bindir}/psresize
%attr(755,root,root) %{_bindir}/psselect
%attr(755,root,root) %{_bindir}/pst2pdf
%attr(755,root,root) %{_bindir}/pstops
%attr(755,root,root) %{_bindir}/showchar
%attr(755,root,root) %{texmf}/scripts/ps2eps/ps2eps*
%{_mandir}/man1/epsffit*
%{_mandir}/man1/extractres*
%{_mandir}/man1/fix*
%{_mandir}/man1/getafm*
%{_mandir}/man1/includeres*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/psbook*
%{_mandir}/man1/psmerge*
%{_mandir}/man1/psnup*
%{_mandir}/man1/psresize*
%{_mandir}/man1/psselect*
%{_mandir}/man1/pstops*
%{texmfdist}/scripts/epspdf
%{texmf}/dvips/psutils

%files uncategorized-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devnag

%files tex4ht
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/tex4ht
%doc %{texmfdist}/doc/generic/tex4ht
%attr(755,root,root) %{_bindir}/ht
%attr(755,root,root) %{_bindir}/htcontext
%attr(755,root,root) %{_bindir}/htlatex
%attr(755,root,root) %{_bindir}/htmex
%attr(755,root,root) %{_bindir}/httex
%attr(755,root,root) %{_bindir}/httexi
%attr(755,root,root) %{_bindir}/htxelatex
%attr(755,root,root) %{_bindir}/htxetex
%attr(755,root,root) %{_bindir}/mk4ht
%attr(755,root,root) %{_bindir}/t4ht
%attr(755,root,root) %{_bindir}/tex4ht
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/ht.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htcontext.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htlatex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htmex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/httex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/httexi.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htxelatex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/htxetex.sh
%attr(755,root,root) %{texmfdist}/scripts/tex4ht/mk4ht.pl
%{texmfdist}/tex/generic/tex4ht
%{texmfdist}/tex4ht
%{texmf}/scripts/tex4ht

%files xetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvipdfmx
%attr(755,root,root) %{_bindir}/xelatex
%attr(755,root,root) %{_bindir}/xetex
%dir %{fmtdir}/xetex
%doc %{texmfdist}/doc/generic/ifxetex
%doc %{texmfdist}/doc/generic/xetex-pstricks
%doc %{texmfdist}/doc/xelatex
%doc %{texmfdist}/doc/xetex
%{texmfdist}/scripts/xetex
%{texmfdist}/tex/generic/ifxetex
%{texmfdist}/tex/generic/xetexconfig
%{texmfdist}/tex/latex/latexconfig/xelatex.ini
%{texmfdist}/tex/plain/config/xetex.ini
%{texmfdist}/tex/xelatex
%{texmfdist}/tex/xetex
%{texmf}/fmtutil/format.xetex.cnf
%{fmtdir}/xetex/xetex.fmt
%{fmtdir}/xetex/xelatex.fmt

%files xmltex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfxmltex
%attr(755,root,root) %{_bindir}/xmltex
%doc %{texmfdist}/doc/xmltex
%{texmfdist}/source/xmltex
%{texmfdist}/tex/xmltex
%{texmf}/fmtutil/format.xmltex.cnf
%{fmtdir}/pdftex/pdfxmltex.fmt
%{fmtdir}/pdftex/xmltex.fmt

