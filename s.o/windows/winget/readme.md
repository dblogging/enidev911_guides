### Uso


Uno de los escenarios más comunes es buscar e instalar una herramienta favorita. 

1. Para buscar una herramienta, escriba `winget search <appname>`.  
2. Una vez que hayas confirmado que la herramienta que desea está disponible, puede instalarla escribiendo `winget install <appname>`. La herramienta **winget** iniciará el instalador e instalará la aplicación en su PC.  


Puede crear un script por lotes y scripts de PowerShell para instalar varias aplicaciones.  

```bat
:: tools.bat
@echo off  
Echo Install Powertoys and Terminal  
REM Powertoys  
winget install Microsoft.Powertoys  
if %ERRORLEVEL% EQU 0 Echo Powertoys installed successfully.  
REM Terminal  
winget install Microsoft.WindowsTerminal  
if %ERRORLEVEL% EQU 0 Echo Terminal installed successfully.   %ERRORLEVEL%
```

