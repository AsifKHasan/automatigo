#!/usr/bin/env bash
# wav->text pipeline

# parameters
AUDIO=$1
SEGMENTS=$@

set echo off

pushd ./src
./audio-to-text.py --audio ${AUDIO} --segments "${SEGMENTS}"

if [ ${?} -ne 0 ]; then
  popd && exit 1
else
  popd
fi
