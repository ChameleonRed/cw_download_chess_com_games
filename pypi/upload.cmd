setlocal
cd %~dp0\..
call venv\Scripts\activate.bat
if %errorlevel% neq 0 exit /b %errorlevel%
py -m twine upload dist/* --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
endlocal