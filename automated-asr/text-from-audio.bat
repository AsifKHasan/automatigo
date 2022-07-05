:: wav->text pipeline

@echo off

:: parameters
set AUDIO=%1

pushd .\src
.\audio-to-text.py  --audio "%AUDIO%" --segments "%*"
if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd
