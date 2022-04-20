setlocal
cd %~dp0\..
call venv\Scripts\activate.bat
py -m twine upload --repository test_cw_download_chess_com_games dist/* --verbose
endlocal