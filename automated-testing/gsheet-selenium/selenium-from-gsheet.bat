:: selenium based functional testing from gsheet data pipeline

@echo off

:: append drivers directory to PATH
set PATH=%PATH%;%cd%\drivers

:: the scripts are in src directory
pushd src
selenium-from-gsheet.py --config "../conf/config.yml"

if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd
