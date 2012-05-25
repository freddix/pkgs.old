# $Id: TLPostActions.pm 11288 2008-11-13 15:43:41Z preining $
# TeXLive::TLPostActions.pm - collection post install stuff for installation
# Copyright 2008 Norbert Preining
# This file is licensed under the GNU General Public License version 2
# or any later version.

package TeXLive::TLPostActions;

BEGIN {
  use Exporter ();
  use vars qw( @ISA @EXPORT_OK @EXPORT );
  @ISA = qw(Exporter);
  @EXPORT_OK = qw(
    %PostInstall
    %PostRemove
  );
  @EXPORT = @EXPORT_OK;
}

use TeXLive::TLUtils qw(win32 mkdirhier copy conv_to_w32_path log debug info
                        touch tlwarn);
use TeXLive::TLWinGoo;

my $mainmenu = "TeX Live 2008";

our %PostInstall;
our %PostRemove;

# NOT ENABLED !!!!!
# context post install actions
sub do_install_bin_context {
  my ($texdir, $texdirw, $texmfsysvar) = @_;
  # set up texmfcnf.lua
  my $TMF = "$texdirw/texmf/web2c/texmfcnf.lua";
  if (! -r $TMF) {
    open(TMF, ">$TMF") || die "open($TMF) failed: $!\n";
    print TMF 'local conf = {}', "\n";
    print TMF "conf.TEXMFCACHE = \"$texmfsysvar\"\n";
    #print TMP "conf.CACHEINTDS = 't'\n";
    print TMF "return conf\n";
    close(TMF) || warn "close($TMF) failed: $!";
  }
  # update the luatools cache
  system("luatools", "--generate");
  # build the context formats based on luatex
  system("context", "--make", "--compile", "cont-en");
  # update the font cache
  system("mtxrun", "--script", "fonts", "--reload");
}
#
# That has to be sorted out and maybe changed at a later time, so do NOT
# enable that for now.
###$PostInstall{"bin-context"} = \&do_install_bin_context;


# ATM do the same for luatex as for context
sub do_install_luatex {
  do_install_bin_context(@_);
}
#
# SEE ABOVE
# $PostInstall{"luatex"} = \&do_install_luatex;


# xetex
#
sub do_install_xetex {
  my ($texdir, $texdirw, $texmfsysvar) = @_;
  #
  # bin-installs font-config related stuff
  #
  # new version according to Staszek
  if (!defined($texmfsysvar)) {
    $texmfsysvar = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($texmfsysvar);
  }
  if (-r "$texdir/bin/win32/conf/fonts.conf") {
    # we have installed w32, so put it into texmfsysvar
    mkdirhier("$texmfsysvar/fonts");
    TeXLive::TLUtils::rmtree("$texmfsysvar/fonts/conf");
    TeXLive::TLUtils::rmtree("$texmfsysvar/fonts/cache");
    my @cpycmd;
    if (win32()) {
      push @cpycmd, "xcopy", "/e", "/i", "/q", "/y";
    } else {
      push @cpycmd, "cp", "-R";
    }
    system(@cpycmd,
             (win32() ? conv_to_w32_path("$texdir/bin/win32/conf") :
                       "$texdir/bin/win32/conf"),
             (win32() ? conv_to_w32_path("$texmfsysvar/fonts/conf") :
                       "$texmfsysvar/fonts/conf"));
    system(@cpycmd,
             (win32() ? conv_to_w32_path("$texdir/bin/win32/cache") :
                       "$texdir/bin/win32/cache"),
             (win32() ? conv_to_w32_path("$texmfsysvar/fonts/cache") :
                       "$texmfsysvar/fonts/cache"));
    if (open(FONTSCONF, "<$texdir/bin/win32/conf/fonts.conf")) {
      my @lines = <FONTSCONF>;
      close(FONTSCONF);
      if (open(FONTSCONF, ">$texmfsysvar/fonts/conf/fonts.conf")) {
        my $winfontdir;
        if (win32()) {
          $winfontdir = $ENV{'SystemRoot'}.'/fonts';
          $winfontdir =~ s!\\!/!g;
          #mkdirhier("$texmfsysvar/fonts/cache");

          # fc-cache breaks often on w32 in some strange way
          # there are claims that touching a font file in $winfontdir
          # would solve that problem. So lets touch some of them
          if (opendir (WINFONT, $winfontdir)) {
            my @dirents = readdir (WINFONT);
            closedir (WINFONT) || warn "closedir($winfontdir) failed: $!";
            # do not actually touch anything by now, maybe already the
            # opendir is enough ...

            # for my $dirent (@dirents) {
            #   if ($dirent =~ m/\.(ttf|otf)$/i) {
            #     touch("$winfontdir/$dirent");
            #     tlwarn("touching $dirent in $winfontdir to make fc-cache work\n");
            #     # one file touched should be enough
            #     last;
            #   }
            # }
          }
        }
        foreach (@lines) {
          $_ =~ s!c:/Program Files/texlive/2008!$texdir!;
          $_ =~ s!c:/windows/fonts!$winfontdir! if win32();
          # hack around fc-cache problem in from_dvd case:
          #if (win32() and (uc($texdir) ne uc($texdirw)) and
          #    ($_ =~ m!^<dir>.*texmf-dist.*</dir>!)) { $_ = '<!-- '.$_.' -->'; }
          print FONTSCONF;
        }
        close(FONTSCONF);
      } else {
        warn("Cannot open $texmfsysvar/fonts/conf/fonts.conf for writing\n");
      }
    } else {
      warn("Cannot open $texdir/bin/win32/conf/fonts.conf\n");
    }
  }
  # call fc-cache but only when we install on w32!
  if (win32()) {
    info("Running fc-cache -v -r\n");
    log(`fc-cache -v -r 2>&1`);
    #system("fc-cache","-v", "-r");
  }
}
$PostInstall{"xetex"} = \&do_install_xetex;

#
# bin-dviout.win32
#
sub do_install_bin_dviout_win32 {
  my ($texdir, $texdirw) = @_;
  if (win32()) {
    my $texdir_bsl = conv_to_w32_path($texdir);
    add_menu_shortcut(
      $mainmenu,
      'DVIOUT Dvi Viewer',
      $texdir.'/tlpkg/dviout/dviout.exe', # for the icon
      'wscript',
      $texdir_bsl."\\bin\\win32\\dviout.vbs",
      '',
    );
  }
}
sub do_remove_bin_dviout_win32 {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu, 'DVIOUT Dvi Viewer');
  }
}
$PostInstall{'bin-dviout.win32'} = \&do_install_bin_dviout_win32;
$PostRemove{'bin-dviout.win32'} = \&do_remove_bin_dviout_win32;


#
# bin-texdoc
#
sub do_install_bin_texdoc {
  my ($texdir, $texdirw) = @_;
  if (win32()) {
    #add_desktop_shortcut(
    #  $texdirw,
    #  'TeXdoc GUI',
    #  '', # $vars{'TEXDIR'}.'/tlpkg/doc/notes.ico', # the icon
    #  $texdir.'/bin/win32/texdoctk.bat',
    #  '', # no args
    #  'batgui', # any non-null value to hide command-prompt
    #);
    add_menu_shortcut(
      $mainmenu,
      'TeXdoc GUI',
      '', # $vars{'TEXDIR'}.'/tlpkg/doc/notes.ico', # the icon
      $texdir.'/bin/win32/texdoctk.bat',
      '', # no args
      'batgui', # any non-null value to hide command-prompt
    );
  }
}
sub do_remove_bin_texdoc {
  my ($texdir) = @_;
  if (win32()) {
    # remove_desktop_shortcut('TeXdoc GUI');
    remove_menu_shortcut($mainmenu, 'TeXdoc GUI');
  }
}
$PostInstall{'bin-texdoc'} = \&do_install_bin_texdoc;
$PostRemove{'bin-texdoc'} = \&do_remove_bin_texdoc;

#
# bin-tlpsv.win32
#
sub do_install_bin_tlpsv_win32 {
  my ($texdir, $texdirw) = @_;
  if (win32()) {
    add_desktop_shortcut(
      $texdirw,
      'PS_View',
      $texdir.'/tlpkg/tlpsv/psv.exe', # icon, not prog!
      $texdir.'/bin/win32/psv.bat',
      '', # no args
      'batgui', # any non-null value to hide command-prompt
    );
    add_menu_shortcut(
      $mainmenu,
      'PS_View',
      $texdir.'/tlpkg/tlpsv/psv.exe', # icon, not prog!
      $texdir.'/bin/win32/psv.bat',
      '', # no args
      'batgui', # any non-null value to hide command-prompt
    );
    #register_extension(".ps", "PostScript");
    #register_extension(".eps", "PostScript");
    ##register_file_type("PostScript", '"'.$texdir.'/bin/win32/psv.bat"');
    #register_file_type("PostScript",
    #  '"'.$texdir.'/tlpkg/tlpsv/gswxlua.exe" -g '.
    #  '"'.$texdir.'/tlpkg/tlgs/bin/gsdll32.dll" -l '.
    #  '"'.$texdir.'/tlpkg/tlpsv/psv.wx.lua" -p '.
    #  '"'.$texdir.'/tlpkg/tlpsv/psv_view.ps" -sINPUT="%1"');
    #update_assocs();
  }
}
sub do_remove_bin_tlpsv_win32 {
  my ($texdir) = @_;
  if (win32()) {
    remove_desktop_shortcut('PS_View');
    remove_menu_shortcut($mainmenu, 'PS_View');
    #unregister_extension(".ps");
    #unregister_extension(".eps");
    #unregister_file_type("PostScript");
    #update_assocs();
  }
}
$PostRemove{'bin-tlpsv.win32'} = \&do_remove_bin_tlpsv_win32;
$PostInstall{'bin-tlpsv.win32'} = \&do_install_bin_tlpsv_win32;

#
# bin-texlive
#
sub do_install_bin_texlive {
  my ($texdir, $texdirw) = @_;
  if (win32()) {
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manager',
      '', # $texdir.'/tlpkg/doc/dummy.ico',
      $texdir.'/bin/win32/tlmgr.bat',
      'gui',
      'batgui',
    );
    add_menu_shortcut(
      $mainmenu,
      'Release notes',
      '',
      'http://tug.org/texlive/windows.html',
      '',
      '',
    );
    if (uc(TeXLive::TLWinGoo::win_which_dir('tex.exe')) ne
          uc($texdir.'/bin/win32') or
        uc(TeXLive::TLWinGoo::win_which_dir('pdftex.exe')) ne
          uc($texdir.'/bin/win32') or
        uc(TeXLive::TLWinGoo::win_which_dir('luatex.exe')) ne
          uc($texdir.'/bin/win32')) {
      my $texbindir = $texdir."\\bin\\win32";
      $texbindir =~ s!/!\\!g;
      add_menu_shortcut(
        $mainmenu,
        'TeX Live Prompt',
        '',
        $ENV{'COMSPEC'},
       "/k \"path $texbindir;%path%\"",
       '',
      );
      add_desktop_shortcut(
        $texdirw,
        'TeX Live Prompt',
        '',
        $ENV{'COMSPEC'},
       "/k \"path $texbindir;%path%\"",
       '',
      );
    }
  }
}
sub do_remove_bin_texlive {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu, 'TeX Live Manager');
    remove_menu_shortcut($mainmenu, 'Release notes');
    remove_menu_shortcut($mainmenu, 'TeX Live Prompt');
    remove_desktop_shortcut('TeX Live Prompt');
  }
}
$PostInstall{'bin-texlive'} = \&do_install_bin_texlive;
$PostRemove{'bin-texlive'} = \&do_remove_bin_texlive;

#
# texlive.infra
# ships all the readme.html/readme.XX.html files, and the index of all
# documents
sub do_install_texlive_infra {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_infra: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Toplevel Readme Index',
      '', # default pdf icon
      $texdir.'/index.html',
      '',
      '',
    );
  }
}
sub do_remove_texlive_infra {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Toplevel Readme Index');
  }
}
$PostInstall{'texlive.infra'} = \&do_install_texlive_infra;
$PostRemove{'texlive.infra'} = \&do_remove_texlive_infra;

#
# texlive-en
#
sub do_install_texlive_en {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_en: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (en) (HTML)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/english/texlive-en/texlive-en.html',
      '',
      '',
    );
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (en) (PDF)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/english/texlive-en/texlive-en.pdf',
      '',
      '',
    );
  }
}
sub do_remove_texlive_en {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (en) (HTML)');
    remove_menu_shortcut($mainmenu,'TeX Live Manual (en) (PDF)');
  }
}
$PostInstall{'texlive-en'} = \&do_install_texlive_en;
$PostRemove{'texlive-en'} = \&do_remove_texlive_en;

#
# texlive-cz
#
sub do_install_texlive_cz {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_cz: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (cz) (PDF)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/czechslovak/texlive-cz/texlive-cz.pdf',
      '',
      '',
    );
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (cz) (HTML)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/czechslovak/texlive-cz/texlive-cz.html',
      '',
      '',
    );
  }
}
sub do_remove_texlive_cz {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (cz) (PDF)');
    remove_menu_shortcut($mainmenu,'TeX Live Manual (cz) (HTML)');
  }
}
$PostInstall{'texlive-cz'} = \&do_install_texlive_cz;
$PostRemove{'texlive-cz'} = \&do_remove_texlive_cz;

#
# texlive-fr
#
sub do_install_texlive_fr {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_fr: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (fr) (PDF)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/french/texlive-fr/texlive-fr.pdf',
      '',
      '',
    );
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (fr) (HTML)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/french/texlive-fr/texlive-fr.html',
      '',
      '',
    );
  }
}
sub do_remove_texlive_fr {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (fr) (HTML)');
    remove_menu_shortcut($mainmenu,'TeX Live Manual (fr) (PDF)');
  }
}
$PostInstall{'texlive-fr'} = \&do_install_texlive_fr;
$PostRemove{'texlive-fr'} = \&do_remove_texlive_fr;

#
# texlive-de
#
sub do_install_texlive_de {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_de: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (de) (PDF)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/german/texlive-de/texlive-de.pdf',
      '',
      '',
    );
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (de) (HTML)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/german/texlive-de/texlive-de.html',
      '',
      '',
    );
  }
}
sub do_remove_texlive_de {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (de) (PDF)');
    remove_menu_shortcut($mainmenu,'TeX Live Manual (de) (HTML)');
  }
}
$PostInstall{'texlive-de'} = \&do_install_texlive_de;
$PostRemove{'texlive-de'} = \&do_remove_texlive_de;

#
# texlive-pl
#
sub do_install_texlive_pl {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_pl: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (pl) (PDF)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/polish/texlive-pl/texlive-pl.pdf',
      '',
      '',
    );
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (pl) (HTML)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/polish/texlive-pl/texlive-pl.html',
      '',
      '',
    );
  }
}
sub do_remove_texlive_pl {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (pl) (PDF)');
    remove_menu_shortcut($mainmenu,'TeX Live Manual (pl) (HTML)');
  }
}
$PostInstall{'texlive-pl'} = \&do_install_texlive_pl;
$PostRemove{'texlive-pl'} = \&do_remove_texlive_pl;

#
# texlive-ru
#
sub do_install_texlive_ru {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_ru: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (ru) (PDF)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/russian/texlive-ru/texlive-ru.pdf',
      '',
      '',
    );
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (ru) (HTML)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/russian/texlive-ru/texlive-ru.html',
      '',
      '',
    );
  }
}
sub do_remove_texlive_ru {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (ru) (HTML)');
    remove_menu_shortcut($mainmenu,'TeX Live Manual (ru) (PDF)');
  }
}
$PostInstall{'texlive-ru'} = \&do_install_texlive_ru;
$PostRemove{'texlive-ru'} = \&do_remove_texlive_ru;

#
# texlive-zh-cn
#
sub do_install_texlive_zh_cn {
  my ($texdir) = @_;
  if (win32()) {
    if (!defined($texdir)) {
      tlwarn("do_install_texlive_zh_cn: texdir not defined, returning\n");
      return;
    }
    add_menu_shortcut(
      $mainmenu,
      'TeX Live Manual (zh-cn)',
      '', # default pdf icon
      $texdir.'/texmf-doc/doc/chinese/texlive-zh-cn/texlive-zh-cn.pdf',
      '',
      '',
    );
  }
}
sub do_remove_texlive_zh_cn {
  my ($texdir) = @_;
  if (win32()) {
    remove_menu_shortcut($mainmenu,'TeX Live Manual (zh-cn)');
  }
}
$PostInstall{'texlive-zh-cn'} = \&do_install_texlive_zh_cn;
$PostRemove{'texlive-zh-cn'} = \&do_remove_texlive_zh_cn;


#
# FROM HERE ON ONLY DISABLED POST INSTALL AND REMOVE ACTIONS!!!!!!!
#

# disabled
sub do_bin_xdvi {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  copy ("$TEXDIR/texmf/xdvi/XDvi", "$TEXMFSYSVAR/xdvi");
}
# $PostInstall{"bin-xdvi"} = \&do_bin_xdvi;


# disabled
sub do_plain {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  # install some copies from texmf(-dist) into texmf-var
  copy ("$TEXDIR/texmf-dist/tex/generic/config/language.def",
        "$TEXMFSYSVAR/tex/generic/config");
}
# $PostInstall{"plain"} = \&do_plain;


# disabled
sub do_bin_dvipsk {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  # those files must exist
  copy ("$TEXDIR/texmf/dvips/config/config.ps",
        "$TEXMFSYSVAR/dvips/config");
}
# $PostInstall{"bin-dvipsk"} = \&do_bin_dvipsk;

# disabled
sub do_bin_dvipdfm {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  # fix up dvipdfm config file to contain the right # piping command
  mkdirhier("$TEXMFSYSVAR/dvipdfm/config");
  open(DVIPDFMCONFIGDIST, "<$TEXDIR/texmf/dvipdfm/config/config")
    or die("Cannot open $TEXDIR/texmf/dvipdfm/config/config");
  open(DVIPDFMCONFIGINST, ">$TEXMFSYSVAR/dvipdfm/config/config")
    or die("Cannot open $TEXMFSYSVAR/dvipdfm/config/config");
  while (<DVIPDFMCONFIGDIST>) {
    if (m/^D /) {
      print DVIPDFMCONFIGINST 'D "epstopdf --outfile=%o --nocompress %i"', "\n";
    } else {
      print DVIPDFMCONFIGINST;
    }
  }
  close(DVIPDFMCONFIGDIST);
  close(DVIPDFMCONFIGINST);
}
# $PostInstall{"bin-dvipdfm"} = \&do_bin_dvipdfm;

# disabled
sub do_bin_dvipdfmx {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  # dvipdfmx.cfg
  open(DVIPDFMCONFIGDIST, "<$TEXDIR/texmf/dvipdfmx/dvipdfmx.cfg")
    or die("Cannot open $TEXDIR/texmf/dvipdfmx/dvipdfmx.cfg");
  open(DVIPDFMCONFIGINST, ">$TEXMFSYSVAR/dvipdfmx/dvipdfmx.cfg")
    or die("Cannot open $TEXMFSYSVAR/dvipdfmx/dvipdfmx.cfg");
  while (<DVIPDFMCONFIGDIST>) {
    # current dvipdfmx.cfg already contains the right rungs incantation
    # so do just copy the file to texmf-var
    #if (m/^D /) {
    #  print DVIPDFMCONFIGINST "%$_";
    #  print DVIPDFMCONFIGINST "\n%% GhostScript (TeX Live (Unix and Win32)):\n";
    #  print DVIPDFMCONFIGINST 'D  "rungs -q -dNOPAUSE -dBATCH -sPAPERSIZE=a0 -sDEVICE=pdfwrite -dCompatibilityLevel=1.3 -dAutoFilterGrayImages=false -dGrayImageFilter=/FlateEncode -dAutoFilterColorImages=false -dColorImageFilter=/FlateEncode -dUseFlateCompression=true -sOutputFile=%o %i -c quit"', "\n\n";
    #} else {
      print DVIPDFMCONFIGINST;
    #}
  }
  close(DVIPDFMCONFIGDIST);
  close(DVIPDFMCONFIGINST);
}
# $PostInstall{"bin-dvipdfmx"} = \&do_bin_dvipdfmx;


# disabled
sub do_bin_kpathsea {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  copy ("$TEXDIR/texmf/web2c/mktex.cnf",
        "$TEXMFSYSVAR/web2c");
}
# $PostInstall{"bin-kpathsea"} = \&do_bin_kpathsea;

# disabled
sub do_bin_pdftex {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  # the old installer copied from CDDIR, but shouldn't this be installed
  # in ANY case since it is in bin-pdftex???
  copy ("$TEXDIR/texmf/tex/generic/config/pdftexconfig.tex",
        "$TEXMFSYSVAR/tex/generic/config");
}
# $PostInstall{"bin-pdftex"} = \&do_bin_pdftex;

# disabled
sub do_context {
  my ($TEXDIR, $TEXMFSYSVAR) = @_;
  if (!defined($TEXMFSYSVAR)) {
    $TEXMFSYSVAR = `kpsewhich -var-value=TEXMFSYSVAR`;
    chomp($TEXMFSYSVAR);
  }
  # old installer did this, should we do this, TOO????
  copy ("$TEXDIR/texmf-dist/tex/context/config/cont-usr.tex",
        "$TEXMFSYSVAR/tex/context/config");
}
# $PostInstall{"context"} = \&do_context;


1;


=head1 NAME

C<TeXLive::TLPostActions> -- TeX Live Post Installation and Removal Routines

=head1 SYNOPSIS

  use TeXLive::TLPostActions;

=head1 DESCRIPTION

The L<TeXLive::TLPostActions> module exports the C<%PostInstall> and
the C<%PostRemove> hash indexed by package names providing code references.

These code references are called with the root of the installation as
argument (C<$SELFAUTOPARENT>). Additional arguments, but not necessarily
present, are the value of C<TEXMFSYSVAR> and C<TEXMFLOCAL>.

=head1 SEE ALSO

The modules L<TeXLive::TLUtils>, L<TeXLive::TLPSRC>,
L<TeXLive::TLPDB>, L<TeXLive::TLTREE>, L<TeXLive::TeXCatalogue>.

=head1 AUTHORS AND COPYRIGHT

This script and its documentation were written for the TeX Live
distribution (L<http://tug.org/texlive>) and both are licensed under the
GNU General Public License Version 2 or later.

=cut

### Local Variables:
### perl-indent-level: 2
### tab-width: 2
### indent-tabs-mode: nil
### End:
# vim:set tabstop=2 expandtab: #
