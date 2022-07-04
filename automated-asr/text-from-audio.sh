#!/usr/bin/env bash
# wav->text pipeline

# parameters
AUDIO=$1

set echo off

pushd ./src
./audio-to-text.py --config "../conf/config.yml" --audio ${AUDIO}

if [ ${?} -ne 0 ]; then
  popd && exit 1
else
  popd
fi
