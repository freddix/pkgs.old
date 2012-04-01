# This shell script is run before Openbox launches.
# Environment variables set here are passed to the Openbox session.

# Run XDG autostart things.  By default don't run anything desktop-specific
# See xdg-autostart --help more info
DESKTOP_ENV="OPENBOX"
/usr/share/openbox/openbox-xdg-autostart $DESKTOP_ENV

