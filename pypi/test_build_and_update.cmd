call build
if %errorlevel% neq 0 exit /b %errorlevel%
call test_upload
if %errorlevel% neq 0 exit /b %errorlevel%
