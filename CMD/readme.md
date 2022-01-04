## ¿Qué es CMD o Símbolo del sistema ??


CMD o Símbolo del sistema es una herramienta intérprete de comandos de Windows. A través de ella, podremos interactuar con el sistema operativo mediante la introducción de comandos. Podremos ejecutar aplicaciones, copiar, pegar, borrar y crear nuevos archivos, modificar opciones de configuración y prácticamente todo lo que se nos ocurra que podamos hacer desde su entorno gráfico.


## ¿Qué es batch?

Un archivo **batch** es un archivo de texto sin formato guardado con la extensión **.bat** y que contiene un conjunto de ordenes llamadas comandos de DOS. En resumen un archivo batch es un archivo de texto en el que se a escrito un conjunto de código que van a ser ejecutados de forma lineal y ese archivo de texto debe ser guardado con la extensión **.bat**, es decir un nombre **cualquiera.bat**

Es muy útil para automatizar tareas, por ejemplo un programa que nos abra todas las herramientas que necesitamos para trabajar en un determinado proyecto, de esta forma cada vez que queramos trabajar solo tendremos que pulsar un botón y no hará falta abrir una o todas las aplicaciones necesarias, pero su utilidad no se queda en esto.



**echo.** : sirve para dejar un espacio.
**pause** : hace una pausa en la secuencia (pulsa una tecla para continuar...)
**pause>nul** : hace una pausa sin mostrar nada en pantalla.
**exit** : para finalizar.
**cls** : limpiar pantalla.

**%variable%** : para referirnos a una variable
**set name=value** : declarar una variable.
**set /p name=prompt** : declarar una y pedi al usuario la entrada por teclado, se mostrará la cadena que se especifique en **prompt** 




**Operadores**

- **+** : para sumar
- **-** : para restar
- **\*** : para multiplicar
- **/** : para dividir

**Ejemplos de uso**:

```bat
@echo off
echo.
set/p numero1= Dime un numero
cls
echo.
set/p numero2= Dime otro para sumar al anterior
cls
set/a suma= %numero1% + %numero2%
echo.
echo %numero1% + %numero2% = %suma%
echo.
echo Pulsa una tecla para salir.
pause>nul
exit
```