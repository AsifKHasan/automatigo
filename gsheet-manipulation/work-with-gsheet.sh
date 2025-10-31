#!/usr/bin/env bash
PYTHON=python

FOLDER=false
for arg in "$@"; do
    if [ "$arg" == "--folder" ]; then
        FOLDER=true
        break # Exit the loop once the argument is found
    fi

    if [ "$arg" == "-f" ]; then
        FOLDER=true
        break # Exit the loop once the argument is found
    fi
done

if [ "$FOLDER" = true ]; then
    set echo off
    pushd ./src
    ${PYTHON} work-with-gsheet.py --folder
else
  # parameters
  if [ $# -eq 0 ]; then
    set echo off
    pushd ./src
    ${PYTHON} work-with-gsheet.py
  else
    GSHEET=$1
    set echo off
    pushd ./src
    ${PYTHON} work-with-gsheet.py --gsheet ${GSHEET}
  fi
fi


if [ ${?} -ne 0 ]; then
  popd && exit 1
else
  popd
fi
