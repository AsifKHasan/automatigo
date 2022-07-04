:: wav->text pipeline

@echo off

:: parameters
set AUDIO=%1

pushd .\src
.\audio-to-text.py  --audio "%AUDIO%" --segments 0.00:23.40 24.80: 

if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd
