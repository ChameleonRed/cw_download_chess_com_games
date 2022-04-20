setlocal
cd %~dp0\..
call venv\Scripts\activate.bat
if %errorlevel% neq 0 exit /b %errorlevel%
py -m twine upload --repository test_cw_download_chess_com_games dist/* --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
endlocal