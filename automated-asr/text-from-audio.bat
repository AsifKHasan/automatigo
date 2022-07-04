:: wav->text pipeline

@echo off

:: parameters
set AUDIO=%1

pushd .\src
.\audio-to-text.py  --audio "%AUDIO%" --segments 0.00 24.00 48.00 72.00 96.00 120.00 144.00 

if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd
