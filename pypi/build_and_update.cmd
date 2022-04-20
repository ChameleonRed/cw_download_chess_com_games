call build
if %errorlevel% neq 0 exit /b %errorlevel%
call upload
if %errorlevel% neq 0 exit /b %errorlevel%
