#!/usr/bin/env bash
# wav->text pipeline

# parameters

# filename of the audio file without extension (which is assumed to be .wav). location is ..\out\audio directory
AUDIO=$1

# range of audio to be processed in the format sss.ms:sss.ms (start in seconds and miliseconds a colon and then end in seconds and miliseconds)
# 0.00:59.783 means from start to 59 seconds 783 miliseconds of audio
# :59.783 means from start to 59 seconds 783 miliseconds of audio. nothing before the colon means from the very begining
# 0.00: means from start to end of audio. nothing after the colon means to the very end
# : means the whole audio
RANGE=$2

# [sss.ms:sss.ms sss.ms:sss.ms sss.ms:sss.ms] a list of sss.ms:sss.ms enclosed in "". The audio will be auto-segmented at ranges spanning the start:end seconds
# NOSEG means no automatic segmentation
SEGMENTS=$3

# if [[ $SEGMENTS = [* ]]; then
#   echo "segments found $SEGMENTS"
# else
#   echo 'segments must be enclosed in []'
#   exit 1
# fi

set echo off

pushd ./src
./audio-to-text.py --audio ${AUDIO} --range ${RANGE} --segments "${SEGMENTS}"

if [ ${?} -ne 0 ]; then
  popd && exit 1
else
  popd
fi
