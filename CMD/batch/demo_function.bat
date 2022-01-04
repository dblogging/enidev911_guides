:MYPING
@echo off
set /P MYIP="IP ADRESS: "
ping %MYIP%
pause>nul
EXIT /B 0

@echo off
CALL %MYPING%
EXIT /B %ERRORLEVEL%