#!/bin/sh
TEMP=$(mktemp -d)
cd $TEMP
git clone --depth=1 git://git.videolan.org/ffmpeg.git ffmpeg
cd ffmpeg
git checkout oldabi
NOW=`date +%Y%m%d`
git archive --format=tar --prefix=ffmpeg/ oldabi | xz > ~/rpm/pkgs/ffmpeg/ffmpeg-0.7-rc1-$NOW.tar.xz
rm -rf $TEMP

