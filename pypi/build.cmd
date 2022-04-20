setlocal
cd %~dp0\..
del /s /q dist
call venv\Scripts\activate.bat
if %errorlevel% NEQ 0 exit /b %errorlevel%
py -m build
if %errorlevel% neq 0 exit /b %errorlevel%
endlocal