@echo off
REM file-name: run.bat 
SETLOCAL EnableDelayedExpansion

REM Get the current timestamp in the format 'yymmddhm'.
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set datetime=%%a
set timestamp=!datetime:~2,2!!datetime:~4,2!!datetime:~6,2!!datetime:~8,2!!datetime:~10,2!

REM Run Behave with the HTML formatter and specify the output directory.
behave --format html -o reports\test-results-!timestamp!.html