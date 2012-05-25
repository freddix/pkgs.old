# $Id: TLWinGoo.pm 12372 2009-03-12 23:19:53Z trzeciak $
# TeXLive::TLWinGoo.pm -# Windows nastiness
#
# Copyright 2008, 2009 Siep Kroonenberg, Norbert Preining
# This file is licensed under the GNU General Public License version 2
# or any later version.

# code for broadcast_env adapted from Win32::Env:
# Copyright 2006 Oleg "Rowaa[SR13]" V. Volkov, all rights reserved.
# This program is free software; you can redistribute it and/or modify it
# under the same terms as Perl itself.

package TeXLive::TLWinGoo;

=pod

=head1 NAME

C<TeXLive::TLWinGoo> -- Additional utilities for Windows

=head2 SYNOPSIS

  use TeXLive::TLWinGoo;

=head2 DIAGNOSTICS

  TeXLive::TLWinGoo::win_version;
  TeXLive::TLWinGoo::is_vista;
  TeXLive::TLWinGoo::admin;
  TeXLive::TLWinGoo::non_admin;
  TeXLive::TLWinGoo::reg_country;

=head2 ENVIRONMENT AND REGISTRY

  TeXLive::TLWinGoo::expand_string($s);
  TeXLive::TLWinGoo::global_tmpdir;
  TeXLive::TLWinGoo::get_system_path;
  TeXLive::TLWinGoo::get_user_path;
  TeXLive::TLWinGoo::win_which_dir($prog);
  TeXLive::TLWinGoo::setenv_reg($env_var, $env_data);
  TeXLive::TLWinGoo::unsetenv_reg($env_var);
  TeXLive::TLWinGoo::add_texbindir_to_path($texpath);
  TeXLive::TLWinGoo::remove_texbindirs_from_path;
  TeXLive::TLWinGoo::register_extension($extension, $file_type);
  TeXLive::TLWinGoo::unregister_extension($extension);
  TeXLive::TLWinGoo::register_file_type($file_type, $command);
  TeXLive::TLWinGoo::unregister_file_type($file_type);

=head2 ACTIVATING CHANGES IMMEDIATELY

  TeXLive::TLWinGoo::broadcast_env;
  TeXLive::TLWinGoo::update_assocs;

=head2 SHORTCUTS

  TeXLive::TLWinGoo::desktop_path;
  TeXLive::TLWinGoo::add_desktop_shortcut($texdir, $name, $icon,
    $prog, $args, $batgui);
  TeXLive::TLWinGoo::add_menu_shortcut($place, $name, $icon,
    $prog, $args, $batgui);
  TeXLive::TLWinGoo::init_unshortbat($texdir);
  TeXLive::TLWinGoo::remove_desktop_shortcut($name);
  TeXLive::TLWinGoo::remove_menu_shortcut($place, $name);

=head2 UNINSTALLER

  TeXLive::TLWinGoo::create_uninstaller;
  TeXLive::TLWinGoo::unregister_uninstaller;

All exported functions return forward slashes.

=head2 DESCRIPTION

=over 4

=cut

BEGIN {
  use Exporter;
  use vars qw( @ISA @EXPORT $Registry);
  @ISA = qw( Exporter );
  @EXPORT = qw(
    &win_version
    &is_vista
    &admin
    &non_admin
    &reg_country
    &expand_string
    &global_tmpdir
    &get_system_path
    &get_user_path
    &setenv_reg
    &unsetenv_reg
    &add_texbindir_to_path
    &remove_texbindirs_from_path
    &register_extension
    &unregister_extension
    &register_file_type
    &unregister_file_type
    &broadcast_env
    &update_assocs
    &desktop_path
    &add_desktop_shortcut
    &add_menu_shortcut
    &remove_desktop_shortcut
    &remove_menu_shortcut
    &init_unshortbat
    &create_uninstaller
    &unregister_uninstaller
  );
  # for testing also:
  @EXPORT_OK = qw(
    &admin_again
    &get_system_env
    &get_user_env
    &win_which_dir
    &global_tmpdir
    &is_a_texdir
  );
  if ($^O=~/^MSWin(32|64)$/i) {
    require Win32::API;
    require Win32::TieRegistry;
    Win32::TieRegistry->import( qw( $Registry
      REG_SZ REG_EXPAND_SZ  KEY_READ KEY_WRITE KEY_ALL_ACCESS
         KEY_ENUMERATE_SUB_KEYS ) );
    $Registry->Delimiter('/');
    $Registry->ArrayValues(0);
    $Registry->FixSzNulls(1);
    require Win32::Shortcut;
    Win32::Shortcut->import( qw( SW_SHOWNORMAL SW_SHOWMINNOACTIVE ) );
  }
}

use TeXLive::TLUtils;
TeXLive::TLUtils->import( qw( mkdirhier ) );

my $is_win = $^O=~/^MSWin(32|64)$/i;

=pod

=back

=head2 DIAGNOSTICS

=over 4

=item C<win_version>

C<win_version> returns the Windows version number as stored in the
registry: 5.0 for Windows 2000, 5.1 for Windows XP and 6.0 for Vista.

=cut

my $windows_version = 0;

if ($is_win) {
  my $tempkey = $Registry->Open(
    "LMachine/software/Microsoft/Windows NT/CurrentVersion/",
    {Access => KEY_READ() });
  $windows_version = $tempkey -> { "/CurrentVersion" };
}

sub win_version { return $windows_version; }

=item C<is_vista>

C<is_vista> returns 1 if win_version is >= 6.0, otherwise 0.

=cut

sub is_vista { return $windows_version >= 6; }

# permissions with which we try to access the system environment

my $is_admin = 1;

sub sys_access_permissions {
  $is_admin ? KEY_ALL_ACCESS() : KEY_READ() | KEY_ENUMERATE_SUB_KEYS();
}

sub get_system_env {
  return $Registry -> Open(
    "LMachine/system/currentcontrolset/control/session manager/Environment/",
    {Access => sys_access_permissions()});
}

# $is_admin was set to true originally. With this value,
# sys-access_permissions returns full access permissions. If that
# doesn't work out then apparently we aren't administrator, so we
# set $is_admin to 0.

if ($is_win) {
  $is_admin = 0 if not get_system_env();
}

sub get_user_env {
  return $Registry -> Open("CUser/Environment", {Access => KEY_ALL_ACCESS()});
}

=pod

=item C<admin>

Returns admin status, admin implying having full read-write access
to the system environment.

=cut

sub admin { return $is_admin; }

=pod

=item C<non_admin>

Pretend not to have admin privileges, to enforce a user- rather than
a system install.

Currently only used for testing.

=cut

sub non_admin { $is_admin = 0; }

# just for testing; doesn't check actual user permissions
sub admin_again { $is_admin = 1; }

=pod

=item C<reg_country>

Two-letter country code representing the locale of the current user

=cut

sub reg_country {
  my $value = $Registry -> {"CUser/Control Panel/International//Locale"};
  return 0 unless $value;
  # there might be trailing nulls on Vista
  chop($value) while ($value =~ /\0$/);
  $value = substr $value, -4;
  return 0 unless $value;
  my $lmkey = $Registry -> Open("HKEY_CLASSES_ROOT/MIME/Database/Rfc1766/",
                             {Access => KEY_READ()});
  return 0 unless $lmkey;
  $lm = $lmkey->{"/$value"};
  return 0 unless $lm;
  debug("found lang codes value = $value, lm = $lm...\n");
  if ($lm) {
    if ($lm =~ m/^zh-(tw|hk)$/i) {
      return ("zh-tw");
    } elsif ($lm =~ m/^zh/) {
      # for anything else starting with zh return, that is zh, zh-cn, zh-sg
      # and maybe something else
      return ("zh-cn");
    } else {
      return(substr $lm, 0, 2);
    }
  }
}

=pod

=back

=head2 ENVIRONMENT AND REGISTRY

Most settings can be made for a user and for the system. User
settings override system settings.

For admin users, the functions below affect both user- and system
settings. For non-admin users, only user settings are changed.

An exception is the search path: the effective searchpath consists
of the system searchpath in front concatenated with the user
searchpath at the back.

Note that in a roaming profile network setup, users take only user
settings with them to other systems, not system settings. In this
case, with a TeXLive on the network, a nonadmin install makes the
most sense.

=over 4

=item C<expand_string($s)>

This function replaces substrings C<%env_var%> with their current
values as environment variable and returns the result.

=cut

sub expand_string {
  my ($s) = @_;
  $s =~ s/%([^%;]+)%/$ENV{$1} ? $ENV{$1} : "%$1%"/eg;
  return $s;
}

=pod

=item C<global_tmpdir>

Returns the expanded value of C<%TEMP%> from the system environment,
usually C<%SystemRoot%/Temp>. This value is normally not available
from C<%ENV>.

=cut

if ($is_win) {
  $global_tmp = expand_string(get_system_env()->{'TEMP'}) if $is_win;
}

my $global_tmp = "/tmp";

sub global_tmpdir { return $global_tmp; }

sub is_a_texdir {
  my $d = shift;
  $d =~ s/\\/\//g;
  $d = $d . '/' unless $d =~ m!/$!;
  # don't consider anything under %systemroot% a texdir
  my $sr = uc($ENV{'SystemRoot'});
  $sr =~ s/\\/\//g;
  $sr = $sr . '/' unless $sr =~ m!/$!;
  return 0 if index($d, $sr)==0;
  return (((-e $d.'mktexlsr.exe') or (-e $d.'dvips.exe')) and
    ((-e $d.'tex.exe') or (-e $d.'pdftex.exe') or (-e $d.'xetex.exe')
     or (-e $d.'luatex.exe')));
}

=pod

=item C<get_system_path>

Returns unexpanded system path, as stored in the registry, but with
forward slashes.

=cut

sub get_system_path {
  my $value = get_system_env() -> {'/Path'};
  $value =~ s/\\/\//g;
  # Remove terminating zero bytes; there may be several, at least
  # under w2k, and the FixSzNulls option only removes one.
  $value =~ s/[\s\x00]+$//;
  return $value;
}

=pod

=item C<get_user_path>

Returns unexpanded user path, as stored in the registry, but with
forward slashes. The user path often does not exist, and is rarely
expandable.

=cut

sub get_user_path {
  my $value = get_user_env() -> {'/Path'};
  return "" if not $value;
  $value =~ s/\\/\//g;
  $value =~ s/[\s\x00]+$//;
  return $value;
}

=pod

=item C<win_which_dir>

More or less the same as which, except that 1. it returns a
directory, 2. it consults the path stored in the registry rather
than the path of the current process, and 3. it assumes that the
filename includes an extension. Currently only used for testing.

=cut

sub win_which_dir {
  my $prog = shift;
  my $d;
  # first check system path
  my $path = expand_string(get_system_path());
  my $user_path = expand_string(get_user_path());
  $path = $path . ';' . $user_path if $user_path;
  foreach $d (split (';',$path)) {
    $d =~ s/\/$//;
    return $d if -e $d.'/'.$prog;
  }
  return 0;
}

=pod

=item C<setenv_reg($env_var, $env_data[, $mode]);>

Set an environment variable $env_var to $env_data.

$mode="user": set for current user. $mode="system": set for all
users. Default: both if admin, current user otherwise.

=cut

sub setenv_reg {
  my $env_var = shift;
  my $env_data = shift;
  my $mode = @_ ? shift : "default";
  die "setenv_reg: Invalid mode $mode"
    if ($mode ne "user" and $mode ne "system" and $mode ne "default");
  die "setenv_reg: mode 'system' only available for admin"
    if ($mode eq "system" and !$is_admin);
  my $env;
  if ($mode ne "system") {
    my $env = get_user_env();
    $env->ArrayValues(1);
    $env->{'/'.$env_var} =
       [ $env_data, ($env_data =~ /%/) ? REG_EXPAND_SZ : REG_SZ ];
  }
  if ($mode ne "user" and $is_admin) {
    $env = get_system_env();
    $env->ArrayValues(1);
    $env->{'/'.$env_var} =
       [ $env_data, ($env_data =~ /%/) ? REG_EXPAND_SZ : REG_SZ ];
  }
}

=pod

=item C<unsetenv_reg($env_var[, $mode]);>

Unset an environment variable $env_var

=cut

sub unsetenv_reg {
  my $env_var = shift;
  my $env = get_user_env();
  my $mode = @_ ? shift : "default";
  #print "Unsetenv_reg: unset $env_var with mode $mode\n";
  die "unsetenv_reg: Invalid mode $mode"
    if ($mode ne "user" and $mode ne "system" and $mode ne "default");
  die "unsetenv_reg: mode 'system' only available for admin"
    if ($mode eq "system" and !$is_admin);
  delete get_user_env()->{'/'.$env_var} if $mode ne "system";
  delete get_system_env()->{'/'.$env_var} if ($mode ne "user" and $is_admin);
}

=pod

=item C<add_texbindir_to_path($texpath)>

Remove wrong TeX directories from system path (if possible) and user
path. A directory is a TeX directory if it contains tex.exe or
pdftex.exe and if it is not under %systemroot%.  Then if necessary
add desired TeX directory; to system path if admin, otherwise to
user path.

=cut

sub add_texbindir_to_path {
  my $texbindir = shift;

  my $system_env = get_system_env();
  my $user_env = get_user_env();
  my $d;
  my $d_exp;
  my $found = 0;
  my @newpt;
  my $newp;

  # system path
  if ($is_admin) {
    @newpt = ();
    foreach $d (split (';', get_system_path())) {
      $d_exp = expand_string($d);
      $d_exp =~ s/\\/\//g;
      $d_exp =~ s/\/$//;
      if (uc($d_exp) eq uc($texbindir)) {
        push @newpt, $d unless $found;
        $found = 1;
      } elsif (!is_a_texdir($d_exp)) {
        push @newpt, $d;
      }
    }
    push @newpt, $texbindir unless $found;
    $found = 1;
    $newp = join (';', @newpt);
    $newp =~ s/\//\\/g;
    setenv_reg("Path", $newp, "system");
    #$system_env->ArrayValues(1); # use value_data, value_type pairs
    #$system_env -> {"/Path"} = [ $newp, REG_EXPAND_SZ ];
  } else { # non-admin
    # system path
    foreach $d (split (';', get_system_path())) {
      $d_exp = expand_string($d);
      $d_exp =~ s/\\/\//g;
      $d_exp =~ s/\/$//;
      if (uc($d_exp) eq uc($texbindir)) {
        $found = 1;
      } elsif (is_a_texdir($d_exp)) {
        debug("Warning: possibly conflicting [pdf]TeX program found at $d_exp\n");
      }
    }
  }

  # user path
  @newpt = ();
  foreach $d (split (';', get_user_path())) {
    $d_exp = expand_string($d);
    $d_exp =~ s/\\/\//g;
    $d_exp =~ s/\/$//;
    if (uc($d_exp) eq uc($texbindir)) {
      push @newpt, $d unless $found; # admin case: always $found
      $found = 1;
    } elsif (!is_a_texdir($d_exp)) {
      push @newpt, $d;
    }
  }
  push @newpt, $texbindir unless $found;
  if (@newpt) {
    $newp = join ';', @newpt;
    $newp =~ s/\//\\/g;
    $user_env->ArrayValues(1); # use value_data, value_type pairs
    #$user_env -> {"/Path"} = [ $newp,
    #  ($newp =~ /%/) ? REG_EXPAND_SZ : REG_SZ ];
    setenv_reg("Path", $newp, "user");
  } else {
    unsetenv_reg("PAth", "user");
  }
}

=pod

=item C<remove_texbindirs_from_path>

Remove all directories from the searchpath which contain tex.exe or
pdftex.exe. Do this with the user path and if admin also with the
system path.

=cut

sub remove_texbindirs_from_path {

  my $system_env = get_system_env();
  my $user_env = get_user_env();
  my ($d, $d_exp, @newpt, $newp);

  # system path
  if ($is_admin) {
    @newpt = ();
    foreach $d (split (';', get_system_path())) {
      $d_exp = expand_string($d);
      $d_exp =~ s/\\/\//g;
      $d_exp =~ s/\/$//;
      push @newpt, $d unless is_a_texdir($d_exp);
    }
    $newp = join (';', @newpt);
    $newp =~ s/\//\\/g;
    setenv_reg("Path", $newp, "system");
  }

  # user path
  @newpt = ();
  foreach $d (split (';', get_user_path())) {
    $d_exp = expand_string($d);
    $d_exp =~ s/\\/\//g;
    $d_exp =~ s/\/$//;
    push @newpt, $d unless is_a_texdir($d_exp);
  }
  if (@newpt) {
    $newp = join(';', @newpt);
    $newp =~ s/\//\\/g;
    setenv_reg("Path", $newp, "user");
  } else {
    unsetenv_reg("Path", "user");
  }
}

# delete a registry key recursively.
# the key parameter should be a string, not a registry object.
# We shall use this with file types.

sub reg_delete_recurse {
  my $parent = shift;
  my $childname = shift;
  ddebug("Deleting $childname regkey\n");
  if ($childname !~ '^/') { # subkey
    my $child = $parent->Open ($childname, {Access => KEY_ALL_ACCESS()});
    return unless $child;
    foreach my $v (keys %$child) {
      if ($v =~ '^/') { # value
        delete $child->{$v};
      } else { # subkey
        reg_delete_recurse ($child, $v);
      }
    }
    delete $child->{'/'};
  }
  delete $parent->{$childname};
}

=pod

=item C<register_extension($extension, $file_type)>

Add registry entry to associate $extension with $file_type. Slashes
are flipped where necessary.

=cut

sub register_extension {
  my $extension = shift;
  $extension = '.'.$extension unless $extension =~ /^\./; # ensure leading dot
  $extension = uc($extension);
  my $file_type = shift;
  debug("Linking $extension to $file_type\n");
  my ($classes_key, $k);

  $extension = lc($extension);
  if ($is_admin) {
    $classes_key = $Registry -> Open("LMachine/Software/Classes/",
      {Access => KEY_ALL_ACCESS()}) or die "Cannot open classpath";
    $k = $classes_key->CreateKey($extension);
    $k -> ArrayValues(0);
    $k -> {"/"} = $file_type;
    # delete possibly conflicting value from HKCU/software
    $classes_key = $Registry -> Open("CUser/Software/Classes/",
        {Access => KEY_ALL_ACCESS()});
    delete $classes_key -> {$extension};
  } else {
    $classes_key = $Registry -> Open("CUser/Software/Classes/",
        {Access => KEY_ALL_ACCESS()});
    $k = $classes_key->CreateKey($extension);
    $k -> ArrayValues(0);
    $k -> {"/"} = $file_type;
  }
}

=pod

=item C<unregister_extension($extension)>

Reversal of register_extension.

=cut

sub unregister_extension {
  # we don't error check; we just do the best we can.
  my $extension = shift;
  $extension = '.'.$extension unless $extension =~ /^\./; # ensure leading dot
  $extension = uc($extension);
  debug("unregistering $extension\n");
  my $classes_key = $Registry -> Open("CUser/Software/Classes/",
    {Access => KEY_ALL_ACCESS()});
  if ($classes_key) {
    reg_delete_recurse ($classes_key, $extension."/");
  } else {
    debug("Cannot open HKCU classes for write\n");
  }
  if ($is_admin) {
    $classes_key = $Registry -> Open("LMachine/Software/Classes/",
    {Access => KEY_ALL_ACCESS()});
    if ($classes_key) {
      reg_delete_recurse ($classes_key, $extension."/");
    } else {
    debug("Cannot open HKLM classes for write\n");
    }
  }
}

=pod

=item C<register_file_type($file_type, $command)>

Add registry entries to associate $file_type with $command. Slashes
are flipped where necessary. Double quotes should be added by the
caller if necessary.

=cut

sub register_file_type {
  my $file_type = shift;
  my $command = shift;
  $command =~s/\//\\/g;
  debug ("Linking $file_type to $command\n");
  my ($classes_key, $k);

  if ($is_admin) {
    $classes_key = $Registry -> Open("LMachine/Software/Classes/",
      {Access => KEY_ALL_ACCESS()}) or die "Cannot open classpath";
    $k = $classes_key->CreateKey($file_type."/Shell/Open/Command/");
    $k -> {"/"} = $command;
    $k -> ArrayValues(0);
    # delete possibly conflicting values from HKCU/software
    $classes_key = $Registry -> Open("CUser/Software/Classes/",
        {Access => KEY_ALL_ACCESS()});
    reg_delete_recurse($classes_key, $file_type);
  } else {
    $classes_key = $Registry -> Open("CUser/Software/Classes/",
        {Access => KEY_ALL_ACCESS()});
    $k = $classes_key->CreateKey($file_type."/Shell/Open/Command/");
    $k -> ArrayValues(0);
    $k -> {"/"} = $command;
  }
}

=pod

=item C<unregister_file_type($file_type)>

Reversal of register_script_type.

=cut

sub unregister_file_type {
  # we don't error check; we just do the best we can.
  my $file_type = shift;
  debug ("unregistering $file_type\n");

  my $classes_key = $Registry -> Open("CUser/Software/Classes/",
    {Access => KEY_ALL_ACCESS()});
  if ($classes_key) {
    reg_delete_recurse ($classes_key, $file_type."/");
  } else {
    tlwarn("Cannot open HKCU classes for write\n");
  }
  if ($is_admin) {
    $classes_key = $Registry -> Open("LMachine/Software/Classes/",
    {Access => KEY_ALL_ACCESS()});
    if ($classes_key) {
      reg_delete_recurse ($classes_key, $file_type."/");
    } else {
    debug ("Cannot open HKLM classes for write\n");
    }
    #reg_delete_recurse ($classes_key, $file_type);
  }
}

=pod

=back

=head2 ACTIVATING CHANGES IMMEDIATELY

=over 4

=item C<broadcast_env>

Broadcasts system message that enviroment has changed. This only has
an effect on newly-started programs, not on running programs and the
processes they spawn.

=cut

sub broadcast_env() {
  use constant HWND_BROADCAST	=> 0xffff;
  use constant WM_SETTINGCHANGE	=> 0x001A;
  my $result = "";
  my $SendMessage;
  debug("Broadcasting \"Enviroment settings changed\" message...\n");
  #$SendMessage = new Win32::API('user32', 'SendMessage', 'LLPP', 'L');
  #$result = $SendMessage->Call(HWND_BROADCAST, WM_SETTINGCHANGE,
  #    0, 'Environment') if $SendMessage;
  $SendMessage = new Win32::API('user32', 'SendMessageTimeout', 'LLPPLLP', 'L');
  my $ans = "12345678"; # room for dword
  $result = $SendMessage->Call(HWND_BROADCAST, WM_SETTINGCHANGE,
      0, 'Environment', 0, 2000, $ans) if $SendMessage;
  debug("Broadcast complete; result: $result.\n");
}

=pod

=item C<update_assocs>

Notifies the system that filetypes have changed.

=cut

sub update_assocs() {
  use constant SHCNE_ASSOCCHANGED	=> 0x8000000;
  use constant SHCNF_IDLIST =>	0;
  my $update_fu = new Win32::API('shell32', 'SHChangeNotify', 'LIPP', 'V');
  if ($update_fu) {
    debug("Notifying changes in filetypes...\n");
    $update_fu->Call (SHCNE_ASSOCCHANGED, SHCNF_IDLIST, 0, 0);
    debug("Done notifying\n");
  } else {
    debug("No update_fu\n");
  }
}

=pod

=back

=head2 SHORTCUTS

=cut

# short path names

my $shortfu;
if ($^O=~/^MSWin(32|64)$/i) {
  $shortfu = new Win32::API('kernel32', 'GetShortPathName', 'PPN', 'N');
}

sub short_name {
  my ($fname) = @_;
  return $fname unless $is_win;
  my $buffer = (' ' x 260);
  my $slength = $shortfu->Call($fname, $buffer, 260);
  if ($slength>0) { return substr $buffer, 0, $slength; }
  else { return ''; }
}

=pod

=over 4

=item C<desktop_path>

Location of desktop directory; if admin then the all users version,
otherwise the user's personal version.

=cut

sub desktop_path() {
  my ($shell_key, $deskpath);
  if (admin()) {
    $shell_key = $Registry->Open(
    "LMachine/software/microsoft/windows/currentversion/explorer/shell folders/",
      {Access => KEY_READ});
    $deskpath = short_name($shell_key -> {"/Common Desktop"});
  } else {
    $shell_key = $Registry->Open(
    "CUser/software/microsoft/windows/currentversion/explorer/shell folders/",
      {Access => KEY_READ});
    $deskpath = short_name($shell_key -> {"/Desktop"});
  }
  $deskpath =~ s!\\!/!g;
  return $deskpath;
}

sub menu_path() {
  my ($shell_key, $menupath);
  if (admin()) {
    $shell_key = $Registry->Open(
    "LMachine/software/microsoft/windows/currentversion/explorer/shell folders/",
      {Access => KEY_READ});
    $menupath = short_name($shell_key -> {"/Common Programs"});
  } else {
    $shell_key = $Registry->Open(
    "CUser/software/microsoft/windows/currentversion/explorer/shell folders/",
      {Access => KEY_READ});
    $menupath = short_name($shell_key -> {"/Programs"});
  }
  $menupath =~ s!\\!/!g;
  return $menupath;
}

=pod

=item C<add_desktop_shortcut($texdir, $name, $icon,
  $prog, $args, $batgui)>

Add a desktop shortcut, with name $name and icon $icon, pointing to
program $prog with parameters $args (a string).  Use a non-null
batgui parameter if the shortcut starts a gui program via a
batchfile. Then the inevitable command prompt will be hidden
rightaway, leaving only the gui program visible.

The parameter $texdir is merely used to locate the batchfile
unshort.bat for uninstalling desktop shortcuts, which needs to be
updated.

=cut

sub add_desktop_shortcut {
  my ($texdir, $name, $icon, $prog, $args, $batgui) = @_;

  # create shortcut
  my ($shc, $shpath, $shfile);
  $shc = new Win32::Shortcut();
  $shc->{'IconLocation'} = $icon if -f $icon;
  $shc->{'Path'} = $prog;
  $shc->{'Arguments'} = $args;
  $shc->{'ShowCmd'} = $batgui ? SW_SHOWMINNOACTIVE : SW_SHOWNORMAL;
  $shfile = desktop_path().'/'.$name.'.lnk';
  $shc->Save($shfile);

  # update batchfile for uninstalling shortcuts
  if (open UNSHORT, ">>$texdir/tlpkg/installer/unshort.bat") {
    $shfile =~ s!/!\\!g;
    print UNSHORT 'del "'.$shfile."\" 2>nul\n";
    close UNSHORT;
  } else {
    warn "Cannot open $texdir/tlpkg/installer/unshort.bat for appending: $!";
  }
}

=pod

=item C<add_menu_shortcut($place, $name, $icon,
  $prog, $args, $batgui)>

Add a menu shortcut at place $place (relative to Start/Programs),
with name $name and icon $icon, pointing to program $prog with
parameters $args. See above for batgui.

=cut

sub add_menu_shortcut {
  my ($place, $name, $icon, $prog, $args, $batgui) = @_;
  $place =~ s!\\!/!g;

  my ($shc, $shpath, $shfile);
  $shc = new Win32::Shortcut();
  $shc->{'IconLocation'} = $icon if -f $icon;
  $shc->{'Path'} = $prog;
  $shc->{'Arguments'} = $args;
  $shc->{'ShowCmd'} = $batgui ? SW_SHOWMINNOACTIVE : SW_SHOWNORMAL;
  $shpath = $place;
  $shpath =~ s!\\!/!g;
  $shpath = '/'.$shpath unless $shpath =~ m!^/!;
  $shpath = menu_path().$shpath;
  if ((-e $shpath) and not (-d $shpath)) {
    next; # fail silently and don't worry about it
  } elsif (not (-d $shpath)) {
    mkdirhier($shpath);
    return unless -d $shpath;
  }
  $shfile = $shpath.'/'.$name.'.lnk';
  $shc->Save($shfile);
}

=pod

=item C<init_unshortbat($texdir)>

Reinitialize unshort.bat, the shortcuts uninstaller.

=cut

sub init_unshortbat {
  my $texdirw = shift;
  my $menupath = menu_path();
  $menupath =~ s!/!\\!g;

  # batchfile for uninstalling shortcuts
  if (open UNSHORT, ">$texdirw/tlpkg/installer/unshort.bat") {
    print UNSHORT 'rmdir /s /q "'.$menupath."\\TeX Live 2008\" 2>nul\n";
    close UNSHORT;
  } else {
    warn "Cannot create $texdirw/tlpkg/installer/unshort.bat: $!";
  }
}

=pod

=item C<remove_desktop_shortcut($name)>

For uninstallation of an individual package. We leave unshort.bat
alone because redundant entries are no big deal.

=cut

sub remove_desktop_shortcut {
  my $name = shift;
  unlink desktop_path().'/'.$name.'.lnk';
}

=pod

=item C<remove_menu_shortcut($place, $name)>

For uninstallation of an individual package.

=cut

sub remove_menu_shortcut {
  my $place = shift;
  my $name = shift;
  $place =~ s!\\!/!g;
  $place = '/'.$place unless $place =~ m!^/!;
  unlink menu_path().$place.'/'.$name.'.lnk';
}

=pod

=back

=head2 UNINSTALLER

=over 4

=item C<create_uninstaller>

Writes registry entries for add/remove programs which  reference
the uninstaller script and creates uninstaller batchfiles to finish
the job.

=cut

sub create_uninstaller {
  my ($tdfw, $tdwfw, $tdsvfw, $tdscfw) = @_;
  # TEXDIR, TEXDIRW, TEXMFSYSVAR, TEXMFSYSCONFIG
  $tdfw =~ s![\\/]$!!;
  my $td = $tdfw;
  $td =~ s!/!\\!g;

  $tdwfw =~ s![\\/]$!!;
  my $tdw = $tdwfw;
  $tdw =~ s!/!\\!g;

  $tdsvfw =~ s![\\/]$!!;
  my $tdsv = $tdsvfw;
  $tdsv =~ s!/!\\!g;

  $tdscfw =~ s![\\/]$!!;
  my $tdsc = $tdscfw;
  $tdsc =~ s!/!\\!g;

  my $uninst_key = $Registry -> Open((admin() ? "LMachine" : "CUser") .
    "/software/microsoft/windows/currentversion/",
    {Access => KEY_ALL_ACCESS()});
  my $k = $uninst_key->CreateKey("uninstall/TeXLive/");
  $k->{"/DisplayName"} = "TeXLive ".$::texlive_release;
  $k->{"/UninstallString"} = "\"$tdw\\tlpkg\\installer\\uninst.bat\"";
  $k->{'/DisplayVersion'} = $::texlive_release;
  $k->{'/URLInfoAbout'} = "http://www.tug.org/texlive";

  mkdirhier("$tdwfw/tlpkg/installer"); # wasn't this done yet?
  if (open UNINST, ">$tdwfw/tlpkg/installer/uninst.bat") {
    print UNINST <<UNEND;
\@echo off
rem This should not be necessary, but sometimes it is:
path $td\\bin\\win32;%path%
set PERL5LIB=
\"$td\\tlpkg\\tlperl\\bin\\perl.exe\" \"$td\\texmf\\scripts\\texlive\\uninstall-win32.pl\"
if errorlevel 1 exit
call \"$tdw\\tlpkg\\installer\\unshort.bat\"
copy \"$tdw\\tlpkg\\installer\\uninst2.bat\" \"\%TEMP\%\"
rem pause
\"\%TEMP\%\\uninst2.bat\"
UNEND
;
  close UNINST;
  } else {
    warn "Cannot open $tdwfw/tlpkg/installer/uninst.bat for append";
  }

  if (open UNINST2, ">$tdwfw/tlpkg/installer/uninst2.bat") {
    print UNINST2 <<UNEND2 if ($td eq $tdw);
rmdir /s /q \"$td\\texmf-dist\"
rmdir /s /q \"$td\\texmf-doc\"
rmdir /s /q \"$td\\texmf\"
rmdir /s /q \"$td\\readme-html.dir\"
rmdir /s /q \"$td\\readme-txt.dir\"
rmdir /s /q \"$td\\bin\"
rmdir /s /q \"$td\\tlpkg\"
del /q \"$td\\README.*\"
del /q \"$td\\LICENSE.*\"
del /q \"$td\\doc.html\"
del \"$td\\index.html\"
del \"$td\\texmf.cnf\"
UNEND2
;
    print UNINST2 <<UNEND2;
rmdir /s /q \"$tdsv\"
rmdir /s /q \"$tdsc\"
rmdir /s /q \"$tdw\\temp\"
rmdir /s /q \"$tdw\\tlpkg\"
del \"$tdw\\install-tl.log\"
del \"$tdw\\texlive.profile\" 2>nul
del \"$tdw\\release-texlive.txt\"
set test=
for \%\%f in (\"$tdw\\*.*\") do \@set test=nonempty
if x\%test\%==x rd \"$tdw\"
\@echo Done uninstalling TeXLive.
rem \@pause
del %0
UNEND2
;
    close UNINST2;
  } else {
    warn "Cannot open $tdwfw/tlpkg/installer/uninst2.bat for writing";
  }
}

=pod

=item C<unregister_uninstaller>

Removes TeXLive from Add/Remove Programs.

=cut

sub unregister_uninstaller {
  my $regkey_uninst;
  $regkey_uninst = $Registry->Open(
    "CUser/software/microsoft/windows/currentversion/uninstall/",
    {Access => KEY_ALL_ACCESS()});
  reg_delete_recurse($regkey_uninst, 'texlive/') if $regkey_uninst;
  return unless admin();
  $regkey_uninst = $Registry->Open(
    "LMachine/software/microsoft/windows/currentversion/uninstall/",
    {Access => KEY_ALL_ACCESS()});
  reg_delete_recurse($regkey_uninst, 'texlive/') if $regkey_uninst;
}

=pod

=back

=cut

# needs a terminal 1 for require to succeed!
1;
