#!/usr/bin/env bash
# selenium based functional testing from gsheet data pipeline

set echo off

# append drivers directory to PATH
export PATH=$PATH:$(pwd)/drivers

# the scripts are in src directory
pushd src
python3 selenium-from-gsheet.py --config "../conf/config.yml"

if [ ${?} -ne 0 ]; then
  popd && exit ${?}
else
  popd
fi
