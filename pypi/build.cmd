setlocal
cd %~dp0\..
del /s /q dist
call venv\Scripts\activate.bat
py -m build
endlocal