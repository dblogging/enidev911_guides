@echo off 
tite "directorios del usuario"
echo Bienvenido al programa
echo ----------------------
echo.
cd %USERPROFILE%\Desktop
dir /B 
echo Presione una tecla para continuar...
md "Carpeta nueva"
pause>nul
exit