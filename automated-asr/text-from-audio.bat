:: wav->text pipeline

@echo off

:: parameters

:: filename of the audio file without extension (which is assumed to be .wav). location is ..\out\audio directory
set AUDIO=%1

:: range of audio to be processed in the format sss.ms:sss.ms (start in seconds and miliseconds a colon and then end in seconds and miliseconds)
:: 0.00:59.783 means from start to 59 seconds 783 miliseconds of audio
:: :59.783 means from start to 59 seconds 783 miliseconds of audio. nothing before the colon means from the very begining
:: 0.00: means from start to end of audio. nothing after the colon means to the very end
:: : means the whole audio
set RANGE=%2

:: [sss.ms:sss.ms sss.ms:sss.ms sss.ms:sss.ms] a list of sss.ms:sss.ms enclosed in "". The audio will be auto-segmented at ranges spanning the start:end seconds
:: NOSEG means no automatic segmentation
set SEGMENTS=%~3


pushd .\src
python audio-to-text.py  --audio "%AUDIO%" --range "%RANGE%" --segments "%SEGMENTS%"
if errorlevel 1 (
  popd
  exit /b %errorlevel%
)

popd
