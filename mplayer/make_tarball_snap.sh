#!/bin/sh
NOW=`date +%Y%m%d`
TEMP=$(mktemp -d)
cd $TEMP
svn checkout svn://svn.mplayerhq.hu/mplayer/trunk mplayer
cd mplayer
git clone --depth=1 git://git.videolan.org/ffmpeg.git ffmpeg
cd ..
tar --exclude .svn --exclude .git --exclude .gitignore --group 0 -cf - mplayer | xz -c > ~/rpm/pkgs/mplayer/mplayer-1.0rc5-$NOW.tar.xz
rm -rf $TEMP

