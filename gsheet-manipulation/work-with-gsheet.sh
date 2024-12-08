#!/usr/bin/env bash
PYTHON=python3
# parameters
if [ $# -eq 0 ] 
then
  set echo off
  pushd ./src
  ${PYTHON} work-with-gsheet.py
else
  GSHEET=$1
  set echo off
  pushd ./src
  ${PYTHON} work-with-gsheet.py --gsheet ${GSHEET}
fi


if [ ${?} -ne 0 ]; then
  popd && exit 1
else
  popd
fi
