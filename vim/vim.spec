%define		ver		7.3
%define		patchlevel	434
#
# cflags get changed while configuring
%undefine	configure_cache
#
Summary:	Vi IMproved
Name:		vim
Version:	%{ver}.%{patchlevel}
Release:	2
Epoch:		4
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	ftp://ftp.vim.org/pub/vim/unix/%{name}-%{ver}.tar.bz2
# Source0-md5:	5b9510a17074e2b37d8bb38ae09edbf2
# tango icons
Source20:	%{name}-16x16.png
Source21:	%{name}-22x22.png
Source22:	%{name}-32x32.png
Source23:	%{name}-48x48.png
Source30:	%{name}.desktop
#
Source40:	%{name}-color-scheme-borland.vim
Source41:	%{name}-color-scheme-oceanblack.vim
Source42:	%{name}-color-scheme-oceandeep.vim
Source43:	%{name}-color-scheme-zenburn.vim
Source44:	%{name}-color-scheme-moria.vim
# patchset
Source100:	%{name}-%{ver}.%{patchlevel}.patch.xz
#
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-visual.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-no_libelf.patch
Patch4:		%{name}-egrep.patch
Patch5:		%{name}-awk.patch
Patch6:		%{name}-filetype_vim-perl_tests.patch
Patch7:		%{name}-po-syntax.patch
Patch8:		%{name}-modprobe.patch
Patch9:		%{name}-rtdir.patch
Patch10:	%{name}-doubleparenthesis.patch
Patch11:	%{name}-syntax-fstab.patch
Patch12:	%{name}-vixie.patch
Patch13:	%{name}-cron-vars.patch
Patch14:	%{name}-fstab-tmpfs-size.patch
Patch15:	%{name}-fstab-bogus-errors.patch
Patch16:	%{name}-bash-completion.patch
Patch17:	%{name}-automake-substitutions.patch
Patch18:	%{name}-smarty.patch
Patch19:	%{name}-filetypes.patch
Patch20:	%{name}-man_installation.patch
Patch21:	%{name}-locales.patch
Patch22:	%{name}-localedir.patch
URL:		http://www.vim.org/
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-static
BuildRequires:	unzip
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# that's example script
%define		_noautoreq	'/bin/csh'

%description
Text editor similar to Vi. Important improvements: multiple windows,
multi-level undo, block highliting, folding, and many other.

%package doc
Summary:	Context Vim documentation
Group:		Applications/Editors/Vim
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	gzip

%description doc
This package contains Vim documentation accessible from vim itself
using :help command.

%package tutor
Summary:	Vim tutorial
Group:		Applications/Editors/Vim
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mktemp

%description tutor
This package contains Vim tutorial.

%package -n gvim
Summary:	Vim with Gtk+ GUI
Group:		Applications/Editors/Vim
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires:	%{name}-rt = %{epoch}:%{version}-%{release}
Requires:	iconv

%description -n gvim
Vim with Gtk+ GUI.

%package static
Summary:	Statically linked Vim
Group:		Applications/Editors/Vim
Provides:	vi

%description static
Static Vim version with basic features.

%package -n xxd
Summary:	Utility to convert files to hexdump or do the reverse
Group:		Applications/Editors/Vim

%description -n xxd
xxd creates a hex dump of a given file or standard input. It can also
convert a hex dump back to its original binary form. Like uuencode and
uudecode it allows the transmission of binary data in a `mail-safe'
ASCII representation, but has the advantage of decoding to standard
output. Moreover, it can be used to perform binary file patching.

%package rt
Summary:	Vim runtime files
Group:		Applications/Editors/Vim
# mktemp is for vimtutor
Requires:	mktemp

%description rt
This package contains macros, documentation, syntax configuration and
manual pages for Vim. If you want to take advantage of Vim more
powerful features, you should install this package.

%prep
%setup -q -n %{name}73

xz -dc %{SOURCE100} | patch -p0 -s

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p0
%patch17 -p0
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

install %{SOURCE40} runtime/colors/borland.vim
install %{SOURCE41} runtime/colors/oceanblack.vim
install %{SOURCE42} runtime/colors/oceandeep.vim
install %{SOURCE43} runtime/colors/zenburn.vim
install %{SOURCE44} runtime/colors/moria.vim

# remove unsupported locales
rm -f src/po/zh_{CN,TW}.UTF-8.po
rm -f runtime/lang/menu_zh_{cn,tw}.utf-8.vim

# fix nb/no
mv -f src/po/n{o,b}.po
mv -f runtime/tutor/tutor.n{o,b}
mv -f runtime/tutor/tutor.n{o,b}.utf-8
mv -f runtime/lang/menu_n{o,b}.latin1.vim
mv -f runtime/lang/menu_n{o,b}.utf-8.vim
mv -f runtime/lang/menu_n{o,b}_no.latin1.vim
mv -f runtime/lang/menu_n{o,b}_no.utf-8.vim

%build
cd src
%{__autoconf}
# needed to prevent deconfiguring
cp -f configure auto
install -d bin

# vi
LDFLAGS="%{rpmldflags} -static"
%configure \
	--disable-cscope		\
	--disable-gpm			\
	--disable-gui			\
	--disable-multibyte		\
	--disable-nls			\
	--disable-perlinterp		\
	--disable-pythoninterp		\
	--disable-rubyinterp		\
	--disable-tclinterp		\
	--with-features=small		\
	--with-tlib="ncursesw"		\
	--without-x
%{__make} vim
mv vim bin/vi
LDFLAGS="%{rpmldflags}"
%{__make} distclean

# gvim
%configure \
	--disable-acl			\
	--disable-gpm			\
	--disable-gui			\
	--disable-perlinterp		\
	--disable-pythoninterp		\
	--disable-rubyinterp		\
	--disable-tclinterp		\
	--enable-cscope			\
	--enable-gtk2-check		\
	--enable-gui=gtk2		\
	--enable-multibyte 		\
	--enable-nls			\
	--with-compiledby="Freddix"	\
	--with-features=huge		\
	--with-modified-by="Freddix"	\
	--with-tlib="ncursesw"		\
	--with-x
%{__make} vim
mv vim bin/gvim
%{__make} distclean

# vim
%configure \
	--disable-acl			\
	--disable-gui			\
	--disable-perlinterp		\
	--disable-pythoninterp		\
	--disable-rubyinterp		\
	--disable-tclinterp		\
	--enable-cscope			\
	--enable-gpm			\
	--enable-multibyte		\
	--enable-nls			\
	--with-compiledby="Freddix"	\
	--with-features=huge		\
	--with-modified-by="Freddix"	\
	--with-tlib="ncursesw"		\
	--without-x
%{__make} vim

%{__make} xxd/xxd languages

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/vim,%{_bindir}} \
	$RPM_BUILD_ROOT{/bin,%{_mandir}/man1,%{_datadir}/vim/ftdetect} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16/apps,22x22/apps,32x32/apps,48x48/apps}

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/{doc,{after/,}{compiler,ftdetect,ftplugin,indent,plugin,spell,syntax}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

# use compressed docs, see :help gzip-helpfile
%{__gzip} -9 $RPM_BUILD_ROOT%{_datadir}/vim/doc/*.txt
%{__sed} -i -e 's=\(\t.*\.txt\)\t=\1.gz\t=' $RPM_BUILD_ROOT%{_datadir}/vim/doc/tags

%{__rm} $RPM_BUILD_ROOT%{_bindir}/*

install -p src/bin/gvim $RPM_BUILD_ROOT%{_bindir}/gvim
install -p src/bin/vi $RPM_BUILD_ROOT%{_bindir}/vi
install -p src/vim $RPM_BUILD_ROOT%{_bindir}/vim
install -p src/vimtutor $RPM_BUILD_ROOT%{_bindir}/vimtutor
install -p src/xxd/xxd $RPM_BUILD_ROOT%{_bindir}/xxd

# not supported directories
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/??.*/

mv -f $RPM_BUILD_ROOT{%{_datadir}/vim/gvimrc_example.vim,%{_sysconfdir}/vim/gvimrc}

ln -sf gvim $RPM_BUILD_ROOT%{_bindir}/evim
ln -sf gvim $RPM_BUILD_ROOT%{_bindir}/gvimdiff
ln -sf vi  $RPM_BUILD_ROOT%{_bindir}/ex
ln -sf vi  $RPM_BUILD_ROOT%{_bindir}/rview
ln -sf vi  $RPM_BUILD_ROOT%{_bindir}/view
ln -sf vim $RPM_BUILD_ROOT%{_bindir}/rvim
ln -sf vim $RPM_BUILD_ROOT%{_bindir}/vimdiff

> $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/doc/tags

mv -f $RPM_BUILD_ROOT{%{_datadir}/vim/vimrc_example.vim,%{_sysconfdir}/vim/vimrc}

install %{SOURCE20} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/vim.png
install %{SOURCE21} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/apps/vim.png
install %{SOURCE22} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/vim.png
install %{SOURCE23} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/vim.png
install %{SOURCE30} $RPM_BUILD_ROOT%{_desktopdir}/gvim.desktop

# separate package
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/{ftplugin,syntax}/spec.vim

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vim/tools
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/bugreport.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/spell/check_locales.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/spell/cleanadd.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/spell/fixdup.vim
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vim/doc/vim2html.pl

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gvim
%update_desktop_database_post
%update_icon_cache hicolor

%postun -n gvim
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rvim
%attr(755,root,root) %{_bindir}/vim
%attr(755,root,root) %{_bindir}/vimdiff

%{_mandir}/man1/vim.1*
%{_mandir}/man1/vimdiff.1*
%lang(fr) %{_mandir}/fr/man1/rvim.1*
%lang(fr) %{_mandir}/fr/man1/vim.1*
%lang(fr) %{_mandir}/fr/man1/vimdiff.1.*
%lang(it) %{_mandir}/it/man1/vim.1.*
%lang(it) %{_mandir}/it/man1/vimdiff.1.*
%lang(pl) %{_mandir}/pl/man1/rview.1*
%lang(pl) %{_mandir}/pl/man1/view.1*
%lang(pl) %{_mandir}/pl/man1/vimdiff.1*
%lang(ru) %{_mandir}/ru/man1/vim.1.*
%lang(ru) %{_mandir}/ru/man1/vimdiff.1.*

%files -n gvim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evim
%attr(755,root,root) %{_bindir}/gvim
%attr(755,root,root) %{_bindir}/gvimdiff
%{_desktopdir}/gvim.desktop
%{_iconsdir}/hicolor/*/apps/vim.png
%{_mandir}/man1/evim.1*
%{_mandir}/fr/man1/evim.1*
%{_mandir}/pl/man1/evim.1*
%{_mandir}/ru/man1/evim.1*
%{_mandir}/it/man1/evim.1*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex
%attr(755,root,root) %{_bindir}/vi
%attr(755,root,root) %{_bindir}/view
%attr(755,root,root) %{_bindir}/rview

%files doc
%defattr(644,root,root,755)
%dir %{_datadir}/vim/doc

# English
%{_datadir}/vim/doc/*.txt.gz
%verify(not md5 mtime size) %{_datadir}/vim/doc/tags

%files -n xxd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxd
%{_mandir}/man1/xxd.1*
%lang(fr) %{_mandir}/fr/man1/xxd.1*
%lang(it) %{_mandir}/it/man1/xxd.1*
%lang(pl) %{_mandir}/pl/man1/xxd.1*
%lang(ru) %{_mandir}/ru/man1/xxd.1*

%files rt -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vim
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vim/vimrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vim/gvimrc

%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/doc
%dir %{_datadir}/vim/vimfiles/after
%dir %{_datadir}/vim/vimfiles/after/compiler
%dir %{_datadir}/vim/vimfiles/after/ftdetect
%dir %{_datadir}/vim/vimfiles/after/ftplugin
%dir %{_datadir}/vim/vimfiles/after/indent
%dir %{_datadir}/vim/vimfiles/after/plugin
%dir %{_datadir}/vim/vimfiles/after/spell
%dir %{_datadir}/vim/vimfiles/after/syntax
%dir %{_datadir}/vim/vimfiles/compiler
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/ftplugin
%dir %{_datadir}/vim/vimfiles/indent
%dir %{_datadir}/vim/vimfiles/plugin
%dir %{_datadir}/vim/vimfiles/spell
%dir %{_datadir}/vim/vimfiles/syntax
%verify(not md5 mtime size) %{_datadir}/vim/vimfiles/doc/tags

%{_datadir}/vim/*.vim

%dir %{_datadir}/vim/autoload
%dir %{_datadir}/vim/colors
%dir %{_datadir}/vim/ftdetect
%dir %{_datadir}/vim/ftplugin
%dir %{_datadir}/vim/indent
%dir %{_datadir}/vim/keymap
%dir %{_datadir}/vim/lang
%dir %{_datadir}/vim/plugin
%dir %{_datadir}/vim/syntax
%{_datadir}/vim/colors/*.vim
%{_datadir}/vim/ftplugin/*.vim
%{_datadir}/vim/ftplugin/logtalk.dict
%{_datadir}/vim/indent/*.vim
%{_datadir}/vim/keymap/*.vim
%{_datadir}/vim/syntax/*.vim

%doc %{_datadir}/vim/autoload/README.txt
%doc %{_datadir}/vim/colors/README.txt
%doc %{_datadir}/vim/ftplugin/README.txt
%doc %{_datadir}/vim/indent/README.txt
%doc %{_datadir}/vim/keymap/README.txt
%doc %{_datadir}/vim/lang/README*
%doc %{_datadir}/vim/plugin/README.txt
%doc %{_datadir}/vim/syntax/README.txt

%lang(af) %{_datadir}/vim/lang/menu_af*
%lang(ca) %{_datadir}/vim/lang/menu_ca*
%lang(cs) %{_datadir}/vim/lang/menu_cs*
%lang(cs) %{_datadir}/vim/lang/menu_*czech*
%lang(de) %{_datadir}/vim/lang/menu_de*
%lang(de) %{_datadir}/vim/lang/menu_*german*
%lang(en_GB) %{_datadir}/vim/lang/menu_en_gb*
%lang(en_GB) %{_datadir}/vim/lang/menu_*english*
%lang(eo) %{_datadir}/vim/lang/menu_eo.utf-8.vim
%lang(eo) %{_datadir}/vim/lang/menu_eo_eo.utf-8.vim
%lang(eo) %{_datadir}/vim/lang/menu_eo_xx.utf-8.vim
%lang(es) %{_datadir}/vim/lang/menu_es*
%lang(es) %{_datadir}/vim/lang/menu_*spanish*
%lang(fi) %{_datadir}/vim/lang/menu_fi.latin1.vim
%lang(fi) %{_datadir}/vim/lang/menu_fi.utf-8.vim
%lang(fi) %{_datadir}/vim/lang/menu_fi_fi.latin1.vim
%lang(fi) %{_datadir}/vim/lang/menu_fi_fi.utf-8.vim
%lang(fi) %{_datadir}/vim/lang/menu_finnish_finland.1252.vim
%lang(fr) %{_datadir}/vim/lang/menu_fr*
%lang(hu) %{_datadir}/vim/lang/menu_hu*
%lang(it) %{_datadir}/vim/lang/menu_it*
%lang(ja) %{_datadir}/vim/lang/menu_ja*
%lang(ko) %{_datadir}/vim/lang/menu_ko*
%lang(nl) %{_datadir}/vim/lang/menu_nl*
%lang(nb) %{_datadir}/vim/lang/menu_nb*
%lang(pl) %{_datadir}/vim/lang/menu_pl*
%lang(pl) %{_datadir}/vim/lang/menu_*polish*
%lang(pt) %{_datadir}/vim/lang/menu_pt*
%lang(ru) %{_datadir}/vim/lang/menu_ru*
%lang(sk) %{_datadir}/vim/lang/menu_sk*
%lang(sk) %{_datadir}/vim/lang/menu_*slovak*
%lang(sl) %{_datadir}/vim/lang/menu_sl_si*
%lang(sr) %{_datadir}/vim/lang/menu_sr*
%lang(sv) %{_datadir}/vim/lang/menu_sv*
%lang(uk) %{_datadir}/vim/lang/menu_uk*
%lang(vi) %{_datadir}/vim/lang/menu_vi*
%lang(zh_CN) %{_datadir}/vim/lang/menu_zh.cp936*
%lang(zh_CN) %{_datadir}/vim/lang/menu_zh.gb2312*
%lang(zh_CN) %{_datadir}/vim/lang/menu_zh_cn*
%lang(zh_CN) %{_datadir}/vim/lang/menu_*chinese*gb*
%lang(zh_TW) %{_datadir}/vim/lang/menu_zh.cp950*
%lang(zh_TW) %{_datadir}/vim/lang/menu_zh.big5*
%lang(zh_TW) %{_datadir}/vim/lang/menu_zh_tw*
%lang(zh_TW) %{_datadir}/vim/lang/menu_*taiwan*

%dir %{_datadir}/vim/spell
%lang(he) %{_datadir}/vim/spell/he.*
%lang(yi) %{_datadir}/vim/spell/yi.*

%{_datadir}/vim/plugin/*.vim
%{_datadir}/vim/autoload/*.vim
%{_datadir}/vim/autoload/xml
%{_datadir}/vim/compiler
%{_datadir}/vim/macros
%{_datadir}/vim/print

%files tutor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimtutor
%dir %{_datadir}/vim/tutor
%dir %{_datadir}/vim/tutor/tutor

%{_datadir}/vim/tutor/README.txt
%{_datadir}/vim/tutor/tutor.vim
%{_datadir}/vim/tutor/tutor.utf-8
%lang(el) %{_datadir}/vim/tutor/README.el.cp737.txt
%lang(el) %{_datadir}/vim/tutor/README.el.txt

%lang(bj) %{_datadir}/vim/tutor/tutor.bj
%lang(bj) %{_datadir}/vim/tutor/tutor.bj.utf-8
%lang(ca) %{_datadir}/vim/tutor/tutor.ca
%lang(ca) %{_datadir}/vim/tutor/tutor.ca.utf-8
%lang(cs) %{_datadir}/vim/tutor/tutor.cs
%lang(cs) %{_datadir}/vim/tutor/tutor.cs.cp1250
%lang(cs) %{_datadir}/vim/tutor/tutor.cs.utf-8
%lang(de) %{_datadir}/vim/tutor/tutor.de
%lang(de) %{_datadir}/vim/tutor/tutor.de.utf-8
%lang(el) %{_datadir}/vim/tutor/tutor.el
%lang(el) %{_datadir}/vim/tutor/tutor.el.cp737
%lang(el) %{_datadir}/vim/tutor/tutor.el.utf-8
%lang(eo) %{_datadir}/vim/tutor/tutor.eo
%lang(eo) %{_datadir}/vim/tutor/tutor.eo.utf-8
%lang(es) %{_datadir}/vim/tutor/tutor.es
%lang(es) %{_datadir}/vim/tutor/tutor.es.utf-8
%lang(fr) %{_datadir}/vim/tutor/tutor.fr
%lang(fr) %{_datadir}/vim/tutor/tutor.fr.utf-8
%lang(hr) %{_datadir}/vim/tutor/tutor.hr
%lang(hr) %{_datadir}/vim/tutor/tutor.hr.cp1250
%lang(hr) %{_datadir}/vim/tutor/tutor.hr.utf-8
%lang(hu) %{_datadir}/vim/tutor/tutor.hu
%lang(hu) %{_datadir}/vim/tutor/tutor.hu.cp1250
%lang(hu) %{_datadir}/vim/tutor/tutor.hu.utf-8
%lang(it) %{_datadir}/vim/tutor/tutor.it
%lang(it) %{_datadir}/vim/tutor/tutor.it.utf-8
%lang(ja) %{_datadir}/vim/tutor/tutor.ja.euc
%lang(ja) %{_datadir}/vim/tutor/tutor.ja.sjis
%lang(ja) %{_datadir}/vim/tutor/tutor.ja.utf-8
%lang(ko) %{_datadir}/vim/tutor/tutor.ko.euc
%lang(ko) %{_datadir}/vim/tutor/tutor.ko.utf-8
%lang(nb) %{_datadir}/vim/tutor/tutor.nb
%lang(nb) %{_datadir}/vim/tutor/tutor.nb.utf-8
%lang(pl) %{_datadir}/vim/tutor/tutor.pl
%lang(pl) %{_datadir}/vim/tutor/tutor.pl.cp1250
%lang(pl) %{_datadir}/vim/tutor/tutor.pl.utf-8
%lang(pt) %{_datadir}/vim/tutor/tutor.pt
%lang(pt) %{_datadir}/vim/tutor/tutor.pt.utf-8
%lang(ru) %{_datadir}/vim/tutor/tutor.ru
%lang(ru) %{_datadir}/vim/tutor/tutor.ru.cp1251
%lang(ru) %{_datadir}/vim/tutor/tutor.ru.utf-8
%lang(sk) %{_datadir}/vim/tutor/tutor.sk
%lang(sk) %{_datadir}/vim/tutor/tutor.sk.cp1250
%lang(sk) %{_datadir}/vim/tutor/tutor.sk.utf-8
%lang(sv) %{_datadir}/vim/tutor/tutor.sv
%lang(sv) %{_datadir}/vim/tutor/tutor.sv.utf-8
%lang(tr) %{_datadir}/vim/tutor/tutor.tr.iso9
%lang(tr) %{_datadir}/vim/tutor/tutor.tr.utf-8
%lang(vi) %{_datadir}/vim/tutor/tutor.vi.utf-8
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh.big5
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh.euc
%lang(zh_TW) %{_datadir}/vim/tutor/tutor.zh.utf-8

%{_mandir}/man1/vimtutor.1*
%lang(fr) %{_mandir}/fr/man1/vimtutor.1*
%lang(it) %{_mandir}/it/man1/vimtutor.1*
%lang(pl) %{_mandir}/pl/man1/vimtutor.1*
%lang(ru) %{_mandir}/ru/man1/vimtutor.1*

