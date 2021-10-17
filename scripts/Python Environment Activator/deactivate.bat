@echo off

rem command
set command=WHERE /R "%CD%" /F "deactivate.bat"

rem getting output of command.
For /F "Tokens=*" %%I in ('%command%') Do Set output=%%I

rem Run output file.
%output%