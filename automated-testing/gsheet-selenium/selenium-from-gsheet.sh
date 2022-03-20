#!/usr/bin/env bash
# selenium based functional testing from gsheet data pipeline

set echo off

# the scripts are in src directory
pushd src
./selenium-from-gsheet.py --config '../conf/config.yml'

if [ ${?} -ne 0 ]; then
  popd && exit ${?}
else
  popd
fi
