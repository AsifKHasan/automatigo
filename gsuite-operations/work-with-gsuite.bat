:: work with gsheet

@echo off

IF "%1"=="" GOTO WITHOUT_ARG

:: parameters
set GSHEET="%1"

pushd .\src
python work-with-gsheet.py  --gsheet "%GSHEET%"
if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd
goto :EOF

:WITHOUT_ARG
pushd .\src
python work-with-gsheet.py
if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd

:EOF
