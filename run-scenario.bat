REM file-name: run-scenario.bat
@echo off
SETLOCAL EnableDelayedExpansion

REM Get the current timestamp in the format 'yymmddhm'.
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set datetime=%%a
set timestamp=!datetime:~2,2!!datetime:~4,2!!datetime:~6,2!!datetime:~8,2!!datetime:~10,2!

REM Get the scenario name from the command-line argument.
set scenario_name=%1

REM Run Behave with the HTML formatter and specify the output directory.
behave -n "%scenario_name%" --format html -o reports\test-results-!timestamp!.html