- [Rutas](#mark0)
	+ [Rutas absolutas](#)
	+ [Rutas relativas](#)
	+ [Variable](#variables)


- [Comandos](#mark0)
    * [attrib](#mark1)
    * [at](#mark2)
    * [call](#call)
    * [dir](#dir)
    * [exit](#exit)
    * [mkdir - md](#mkdir)
    * [rem](#rem)
    * [rmdir](#mark5)
    * [pause](#pause)
    * [start](#start)
    * [shutdown](#shutdown)
    * [ipconfig](#ipconfig)
    * [time](#time)
    * [title](#title)
    * [type](#type)

### <a name="mark1"><u>Attrib</u></a>


Muestra o cambia los atributos del archivos o directorios. Si se usa sin par�metros, **attrib** muestra los atributos de todos los archivos en el directorio actual.


Ejemplo:  

```bash
attrib
```

<p>
	<img src="assets/img/attrib.png" alt="attrib"/>
</p>

- **Sintaxis**:

```
ATTRIB [+R | -R] [+A | -A] [+S | -S] [+H | -H] [+I | -I]
	   [unidad:] [ruta] [nombreArchivo] [/S [/D] [/L]]
```

- **Key**:
	- **(+)**: Activar un atributo
	- **(-)**: Borrar un atributo 


- **ruta**: Unidad y/o nombre de archivo, por ejemplo, **C:\*.txt**


- **Par�metros:**
	+ **/S**: Procesa archivos que coinciden en la carpeta y todas las subcarpetas actuales.
	+ **/D**: Tambi�n procesa carpetas.
	+ **/L**: Se trabaja en los atributos del v�nculo simb�lico en vez de en el destino del v�nculo simb�lico.




**Comodines**  

Puede utilizar los comodines (**? y ***) con el par�metro de **pathname** para mostrar o cambiar los attributos de un grupo de archivos.

Cuando se crea un archivo suele tener el atributo **'A'**, pero podemos a�adirle otro o quitarle el que tiene. Los atributos son: 


**Atributos**

- **A**: Sirve para saber si se ha modificado o no el directorio. Se suele asignar por defecto cuando se crea un nuevo archivo o directorio.
- **R** (Solo lectura): Sirve para que no se pueda ni borrar ni modificar el contenido de un archivo o directorio. Solo podemos ver lo que contiene.
- **H** (Oculto): Sirve para ocultar archivos y directorios durante las operaciones normales.
- **S** (Sistema): Sirve para asignar a un archivo o directorio como si fuera un archivo del sistema, esto hace que este oculto y sea solo de lectura. Muchos archivos de windows est�n con este atributo con la finalidad de no ser modificados.


Por ejemplo si quisieramos que nuestro archivo fuera de solo lectura, podr�amos asignarle ese atributo de la siguiente manera:  

```bash
attrib +r file1.txt
# Ahora si vemos los atributos nuevamente con:
attrib file1.txt
# Obtendriamos la siguiente salida: 
# A    R       C:\Users\home\Desktop\file1.txt
```

Si quisiera modificar este archivo de texto **file1.txt** y guardarlo con el mismo nombre obtendr� un error como el siguiente: 

<center>![attrib](assets/img/file1_fail.png)</center>

Estos cambios tambi�n afectan el modo gr�fico en en algunos programas como word:

<center>![attrib2](assets/img/attrib2.png)</center>


Si queremos mantener nuestro archivo **file1.txt** adem�s del atributo de solo lectura que sea tambi�n oculto, volvemos a nuestro s�mbolo de sistema y ejecutamos el siguiente comando: 

```bash
attrib +h file1.txt
# Ahora si vemos los atributos nuevamente con:
attrib file1.txt
# Obtendriamos la siguiente salida: 
# A    HR       C:\Users\home\Desktop\file1.txt
```
Si listaramos los archivos y carpetas con el comandor **dir** pasar�a lo siguiente:  


```bash
dir /b
# repository
# comandos.txt
# ====Ver los archivos ocultos y resumido con:
dir /b/a
# repository
# comandos.txt
# file1.txt
# ====Ver solo los archivos oculos y resumido con:
dir /b/a:h
# file1.txt
```

Una cosa a tener en cuenta es que no podemos tener asignado el **atributo S** con el **atributo H** y viceversa. Lo mismo pasa con **S** y **R**. Para poder asignarlo, debemos primero quitar el atributo correspondiente:

Ejemplo:  

```bash
attrib -r +s file1.txt
# o en caso contrario
attrib -s +r file1.txt
```

Por otra parte, los atributos tambi�n pueden ser modificados desde el modo gr�fico, simplemente con seleccionar o deseleccionar el atributo, para ello debemos hacer clic derecho en el archivo e ir a sus propiedades:  


<p align="center">
	<img src="assets/img/properties.png" alt="properties"
	width="400">
	<img src="assets/img/properties2.png" alt="properties2"
	width="400" height="510">
</p>


### <a name="mark2"><u>At</u></a>


El comando **AT** programa la ejecuci�n de comandos y programas en un equipo a una hora y fecha especificadas. El comando a�n se encuentra disponible por cuestiones de compatibilidad, pero ha sido extendido en el comando [SCHTASKS](#) que permite opciones m�s avanzadas. No obstante es posible emplearlo para la programaci�n de tareas sencillas. Para poder usar esta herramientas necesita  **'Abrir como Administrador'** el s�mbolo de sistema.  


<p align="center">
	<img src="assets/img/open_admin.png" alt="open_admin"
	width="500">
</p>


Sintaxis:  

```bash
at [\Computername][{[ID] [/delete] | /delete [/yes]}]
at [[\Computername] Hours:Minutes [/interactive] [{/every:date[,...] | /next:date[,...]}] command]
```

**Par�metros:**

- **\Computername**: utilice este par�metro para especificar una computadora remota. Si omite este par�metro, las tareas est�n programadas para ejecutarse en el equipo local.
- **ID**: Especifica el n�mero de identificaci�n asignado a un comando programado.
- **EVERY:DAY**: Ejecuta el comando el o los d�as especificados, las iniciales de los d�as utilizados tienen que corresponder a los d�as en el idioma correspondiente.
- **/DELETE**: Cancela una tarea programa. Si se omite el **ID**, se cancelan todas las tareas programadas en el equipo.



**Ejemplos:**

- **Listar tareas programas y mostrar su ID**


```bash
AT
```

- **A la 6:55 de la ma�ana inicia el navegador y conecta el equipo a Google.com**

```bash
AT 06:55 cmd /c start http://google.com
```

Si revisamos con el primer comando, obtendr� algo parecido a lo siguiente:

<p align="center">
	<img src="assets/img/at.png" alt="at"
	width="800">
</p>




- **Realiza un respaldo, a las 07:00 de la ma�ana copia todos los archivos de la carpeta Mis Documentos en la carpeta Backup situada en el disco B:**

```bash
AT 07:00 cmd /c copy %USERPROFILE%\Documents\*.* B:\Backup
```

Tener en cuenta que solo copiar� los archivos, no las carpetas ni los archivos que se encuentren en las subcarpetas. A continuaci�n te dejo una ilustraci�n de ejemplo: 

<p align="center">
	<img src="assets/img/at_backup.png" alt="at"
	width="850">
</p>


---


- **Todos los d�as ejecuta a las 11:30 de la ma�ana el script en batch llamado copia_diaria.cmd**


```bash
# En caso de tener la configuraci�n regional en ingl�s
AT 11:30 /EVERY:m,t,w,th,f,s,su c:\backup\copy_daily.cmd
# En caso de tener la configuraci�n regional en espa�ol
AT 11:30 /EVERY:l,m,mi,j,v,s,d c:\backup\copy_daily.cmd

```

Para ver la configuraci�n del teclado e idioma, podemos desde el s�mbolo del sistema ingresar el comando: 

```bash
intl.cpl
```

Esto nos abrir� la ventana de configuraci�n regional e idioma, vamos a la pesta�a que dice teclado e idiomas o en su lugar Keyboards and Languages:  

<p align="center">
	<img src="assets/img/settings_region.png" alt="settings"
	width="450">
</p>



Abreviaturas de los d�as de la semana en espa�ol:

- **lunes**: l
- **martes**: m
- **mi�rcoles**: mi
- **jueves**: j
- **viernes**: v
- **s�bado**: s
- **domingo**: d


Abreviaturas de los d�as de la semana en ingl�s:

- **monday**: m
- **tuesday**: t
- **wednesday**: w
- **thursday**: th
- **friday**: f
- **saturday**: s
- **sunday**: su



Seg�n nuestra configuraci�n regional ingresaremos los valores para el argumento **/EVERY**. A continuaci�n te dejo un ejemplo usando los nombres completos en lugar de sus abreviaturas en espa�ol: 

<p align="center">
	<img src="assets/img/at_every.png" alt="at_every"
	width="880">
</p>

A continuaci�n te dejo un ejemplo usando las abreviaturas en ingl�s, en caso de que la configuraci�n se encuentre en ese idioma: 

<p align="center">
	<img src="assets/img/at_every2.png" alt="at_every"
	width="880">
</p>

---


- **Eliminar todos los comandos programados**

```bash
AT /DELETE /Y
```

- **Cancelar la tarea del ID 2**

```bash
AT 2 /DELETE 
```

### <u>call</u>

Llama a un programa por lotes desde otro sin detener el programa por lotes principal.

El comando **CALL** lanzar� un nuevo contexto de archivo por lotes junto con los par�metros especificados. Cuando se alzanza el final del segundo archivo por lotes (o si se usa EXIT), el control volver� justo despu�s de la instrucci�n CALL inicial.

Los argumentos se pueden pasar como una cadena simple o usando una variable:


```bat
CALL myscrit.cmd "1234"
CALL otherscript.cmd %VARIABLE%

```

**Ejemplo**:

```bat
::----------start main.cmd-----------
@echo off
CALL function.cmd 10 first
Echo  %_description% - %_number%
::---------end main.cmd--------------

::---------start function.cmd--------
@echo off 
:: Add 25 to %1
SET /a _number=%1 + 25
:: Store %2
SET _description=[%2]
::----------end function.cmd--------

```

En muchos casos, tambi�n querr� usar **SETLOCAL** y **ENDLOCAL** para mantener las variables endiferentes archivos por lotes completamente separadas, esto evitar� cualquier problema potencial si dos scripts usan el mismo nombre de variable.

Si ejecuta un segundo archivo por lotes **sin usar CALL**, puede encontrarse con alg�n comportamiento err�neo


**CALL subrutine (:label)**

El comando **CALL** pasar� el control de la declaraci�n despu�s de la etiqueta especificada junto con los par�metros especificados. Para salir de la subrutina especifique **GOTO:** esto transferir� el control al final de la subrutina actual.


Una etiqueta se define de la siguiente manera:

```bat
: myShineLabel
```


### <a href="#net"><u>net</u></a>


>
- **Para listar los usuarios en Windows usamos el comando:**

```bash
net user 
```

- **Para crear un usuario sin privilegio de Administrador:**

```bash
net user <nameUser> /add
```

- **Para agregar una contrase�a a un usuario o quitarsela:**

```bash
net user <nameUser> *
```
Cuando pulsemos <kbd>Enter</kbd> nos pedir� la contrase�a, la debemos de indicar dos veces como medida de precauci�n. Si presionamos dos veces la tecla <kbd>Enter</kbd>, representar� que dejamos la contrase�a vacia; es decir; le quitamos la contrase�a.


- **Para eliminar un usuario del sistema usaremos el comando:**

```bash
net user <userName> /delete
```

- **Nos muestra los grupos que existen en el host local**

```bash
net localgroup
```

- **Nos muestra los servicios que est�n corriendo en Windows**

```bash
net start
```


### <u>break</u>


Este comando establece o elimina la comprobaci�n extendida de <kbd>Ctrl</kbd> + <kbd>C</kbd>



### <a href="#dir"><u>DIR</u></a>

Muestra una lista de archivos y subcarpetas.  


Sintaxis:  

```
DIR [path(s)[display_format][file_attributes][order][time][options]]
```

**Par�metro**

- **/?:** Mostrar la ayuda del comando
- **/A:** Muestra los archivos con los atributos especificados
	- Atributos:
		+ A : Archivos
		+ D : Directorios
		+ H : Archivos ocultos
		+ S : Archivos del sistema
		+ L : Puntos de an�lisis
		+ I : No archivos indizados (enlaces simb�licos)	
		+ R : Archivos de solo lectura
		+ \- : Prefijo de exclusi�n
		

		```bash
		DIR /a:-D 
		```


- **Listar solo los nombres del directorio ra�z**

```bash
DIR /b c:\
# Mostrar solo los nombres de todos los directorio y archivos de la ra�z
# Incluyendo los ocultos
DIR /b/a c:\
```

- **Listar solo los archivos (no carpeta) del directorio ra�z de forma recursiva en todas las subcarpertas e incluye los archivos ocultos:**

```bash
DIR /a:-D /s c:\
```

- **Listar solo las carpetas (no archivos) del directorio ra�z de forma recursiva en todas las subcarpertas e incluye los archivos ocultos:**

```bash
DIR /a:-A /s c:\
```


- **Listar todos los enlaces simb�licos en el perfil de usuario actual:**

```bash
DIR %USERPROFILE% /a:i
```


### <a href="#mkdir"><u>mkdir - md</u></a>

Este comando, nos sirve para crear directorios:


**Ejemplos**  

- **Crear dos carpetas en el Escritorio**

```bat
md folder1 folder2
```

### <a name="exit"><u>Exit</u></a>

Abandona el programa CMD.EXE (int�rprete de comandos) o el script por lotes actual.

```
EXIT [/B] [c�digo]
```

- **/B**: Especifica que se debe abandonar el archivo por lotes actual y no CMD.EXE. Si se ejecuta desde fuera de un archivo por lotes, abandonar� CMD.EXE
- **c�digo**: Especifica un n�mero.  Si se ha especificado /B, establece ERRORLEVEL con este n�mero. Si abandona CMD.EXE, establece el c�digo de salida del proceso con este n�mero.







### <a href="#rem"><u>Rem</u></a>


Registra los comentarios en un archivo por lotes o en CONFIG.SYS. Cabe destacar que tambi�n puede utilizar los siguientes s�mbolos en una l�nea de comentario:


```bat
REM [comentario]
:: [comentario]
% comentario %
```


### <a name="start"><u>Start</u></a>

Inicia una ventana separada para ejecutar un programa o comando especificado.


```
START ["t�tulo"] [/D ruta] [/I] [/MIN] [/MAX] [/SEPARATE | /SHARED]
      [/LOW | /NORMAL | /HIGH | /REALTIME | /ABOVENORMAL | /BELOWNORMAL]
      [/NODE <nodo NUMA>] [/AFFINITY <m�scara de afinidad hex>] [/WAIT] [/B]
      [comando o programa] [par�metros]
```


- **"t�tulo"**: T�tulo que se mostrar� en la barra de t�tulo de la ventana.
- **ruta**: Directorio de inicio.
- **B**: Iniciar la aplicaci�n sin crear una nueva ventana. La aplicaci�n omite el manejo de ^C. A menos que la aplicaci�n habilite el procesamiento de ^C, solo se podr� interrumpir la aplicaci�n con ^Enter. El nuevo entorno ser� el entorno original pasado a cmd.exe, y no el entorno actual.
- **MIN**: Iniciar la ventana minimizada.
- **MAX**: Iniciar la ventana maximizada.
- **SEPARATE**: Iniciar un programa de Windows de 16 bits en un espacio de memoria separado.
- **SHARED**: Iniciar un programa de Windows de 16 bits en un espacio de memoria compartido.
- **LOW**: Iniciar la aplicaci�n en la clase de prioridad Inactiva.
- **NORMAL**: Iniciar la aplicaci�n en la clase de prioridad Normal.
- **HIGH**: Iniciar la aplicaci�n en la clase de prioridad Alta.
- **REALTIME**: Iniciar la aplicaci�n en la clase de prioridad Tiempo real.
- **ABOVENORMAL**: Iniciar la aplicaci�n en la clase de prioridad por encima de lo normal.
- **BELOWNORMAL**: Iniciar la aplicaci�n en la clase de prioridad por debajo de lo normal.
- **NODE**: Especifica el nodo de arquitectura de memoria no uniforme (NUMA) preferido como un entero decimal.
- **AFFINITY**: Especifica la m�scara de afinidad de procesador como un n�mero hexadecimal. La ejecuci�n del proceso se restringe a estos procesadores. La m�scara de afinidad se interpreta de distinta forma si /AFFINITY y /NODE se combinan. Especifique la m�scara de afinidad como si la m�scara del procesador del nodo NUMA estuviera desplazada a la derecha para comenzar por el bit cero. La ejecuci�n del proceso se restringe a los procesadores en com�n entre la m�scara de afinidad especificada y el nodo NUMA. Si no hay ning�n procesador en com�n, la ejecuci�n del proceso se restringe al nodo NUMA especificado.
- **WAIT**: Iniciar aplicaci�n y esperar a que finalice comando o programa. Si se trata de un comando cmd interno o un archivo por lotes, el procesador de comandos se ejecuta con el modificador /K en cmd.exe. Esto significa que la ventana permanecer� despu�s de que el comando se ejecute. Si no es un comando cmd interno ni archivo por lotes, entonces se considera un programa y se ejecutar� como una aplicaci�n de ventana o aplicaci�n de consola.
- **par�metros**:  Par�metros transmitidos al comando o programa.

NOTA: las opciones SEPARATE y SHARED no se admiten en plataformas de 64 bits.

La especificaci�n de /NODE permite crear los procesos de forma que se pueda
aprovechar la ubicaci�n de memoria en los sistemas NUMA. Por ejemplo, se
pueden crear dos procesos con una comunicaci�n estrecha entre s� mediante la
memoria compartida para compartir el mismo nodo NUMA preferido y minimizar las
latencias de memoria. Asignan memoria del mismo nodo NUMA si es posible y se
pueden ejecutar en procesadores externos al nodo especificado.

```cmd
start /NODE 1 application1.exe
start /NODE 1 application2.exe
```

Estos dos procesos se pueden restringir a�n m�s para ejecutarse en
procesadores espec�ficos en el mismo nodo NUMA. En el siguiente ejemplo,
application1 se ejecuta en los dos procesadores de valor inferior del nodo y
application2 se ejecuta en los siguientes dos procesadores del nodo. En este
ejemplo, se da por supuesto que el nodo especificado tiene como m�nimo
cuatro procesadores l�gicos. Tenga en cuenta que el n�mero de nodo se puede
cambiar a cualquier n�mero de nodo v�lido para el equipo sin necesidad de
cambiar la m�scara de afinidad.

```cmd
start /NODE 1 /AFFINITY 0x3 application1.exe
start /NODE 1 /AFFINITY 0xc application2.exe
```

Si las extensiones de comandos est�n habilitadas, la invocaci�n del
comando externo a trav�s de la l�nea de comandos o del comando START
cambia as�:

Se pueden invocar archivos no ejecutables a trav�s de la asociaci�n del
archivo solo con escribir el nombre del archivo como un comando. (por ej.,
WORD.DOC abrir�a la aplicaci�n asociada con la extensi�n de archivo .DOC).
Consulte los comandos ASSOC y FTYPE para saber c�mo crear estas asociaciones
dentro de un script de comandos.

Cuando se ejecuta una aplicaci�n de 32 bits con interfaz gr�fica, CMD.EXE
no espera a que la aplicaci�n termine antes de volver al s�mbolo del sistema.
Este nuevo comportamiento NO ocurre si se ejecuta dentro de un
script. Cuando se ejecuta una l�nea de comandos cuyo primer token es la
cadena "CMD " sin extensi�n o ruta, entonces se reemplaza "CMD" con el valor
de la variable COMSPEC. Esto evita tomar CMD.EXE del directorio actual.

Cuando se ejecuta una l�nea de comandos cuyo primer token NO contiene una
extensi�n, entonces CMD.EXE usa el valor de la variable de entorno PATHEXT
para determinar las extensiones que hay que buscar y en que orden. El valor
predeterminado para la variable PATHEXT es:

.COM;.EXE;.BAT;.CMD

Tenga en cuenta que la sintaxis es la misma que la variable PATH, con los
puntos y comas separando los elementos diferentes.

Cuando se busca un archivo ejecutable, si no hay ninguna coincidencia en
ninguna extensi�n, entonces se comprueba si el nombre coincide con el nombre
de un directorio. Si es as�, el comando START inicia el explorador en esa
ruta. Si se hace desde la l�nea de comandos, es equivalente a hacer CD /D
en esa ruta.

**Observaciones:**

- Puede ejecutar archivos no ejecutable a trav�s de su asociaci�n de archivos escribiendo el nombre del archivo como comando.

<p align="center">
	<img src="assets/img/start_1.png" alt="start"
	width="880">
</p>


El comando **START** es de utilidad para todos los que le guste crear sus propias aplicaciones ejecutables (archivos batch) que puedan usar para facilitar la ejecuci�n de una infinidad de tareas.


**Ejemplos:**


- Si ejecutamos solo el comando **start** junto a un punto "." se nos abre el explorador de archivos en esa ubicaci�n.


```bat
start.
:: Si colocamos dos puntos, retrocede un nivel.
start..
:: Si le pasamos una ruta, una variable con alg�n path abrir� 
:: el explorador en esa ruta:
start %USERPROFILE%
```

<p align="center">
	<img src="assets/img/start_0.png" alt="start"
	width="880">
</p>


**Ejemplos Start | Uso en script**


- En un archivo batch podemos hacer que se ejecute un comando cada cierto intervalo de tiempo, en este ejemplo cada 20 segundo.

```bat
REM "demo_start.bat"
@ECHO OFF
:start
START /B ping google.com
cls
timeout /nobreak 20
goto start
```

<p align="center">
	<img src="assets/img/start_2.png" alt="start"
	width="880">
</p>

- Se inicia la el bloc de notas **notepad** con la ventana maximizada.

```bash
start /max notepad
```


- Se inicia la presentaci�n llamada **cmd.pptx** que est� en la carpeta "Mis documentos".


```bat
rem "demo_start.bat"
@echo off
start "" "%USERPROFILE%\Documents\cmd.pptx"
rem "run demostart.bat"
```
- Escribir un correo electr�nico desde la misma CMD de all� utilizamos **malito** para redactar el correo y **start** para abrir el gestor de correos.

```bat
@echo off
echo.
start /B /MIN "" "mailto:tucorreo@gmail.com?subject=Envio de correo&body=Hola Proyecto Byte! Este correo lo envie desde la CMD de Windows 10 "
exit
```









- **help**:  

- **Ir a otra unidad extraible**: Ingresando la letra del volumen

Ejemplo:

```bash
F:

```

- **cls**: Este comando limpia la ventana de la consola de Windows; es decir, borra todos los comandos que has escrito anteriormente


- **color** : Establece los colores de primer plano y fondo predeterminados de la consola. 


Colores: 

| C�digo | Color    | C�digo | Color          |
|--------|----------|--------|----------------|
|0       |Negro     | 8      |Gris.           |
|1       |Azul      | 9      |Azul claro      |
|2       |Verde     | A      |Verde claro     |
|3       |Aguamarina| B      |Aguamarina claro|
|4       |Rojo      | C      |Rojo Claro      |
|5       |P�rpura   | D      |P�rpura claro   |
|6       |Amarillo  | E      |Amarillo claro  |
|7       |Blanco    | F      |Blanco brillante|



Ejemplo:  

```bash
color 17
# 1 = Azul para el fondo
# 7 = Blanco para el primer plano
```



### <a name="#variables"><u>Variables</u></a>


**SET**

Muestra, establece o quita las variables de entorno de cmd.exe.

```cmd
SET [variable=[cadena]]
```

- **variable**: Especifica el nombre de la variable de entorno.
- **cadena**: Especifica una serie de caracteres que se asignar� a la variable.

Escriba SET sin par�metros para ver las variables de entorno actuales.

<p align="center">
	<img src="assets/img/set_example.png" alt="set"
	width="780" height="560">
</p>


mostrar todas las variables que empiecen con la letra 'P'.

```
SET P
```
El comando SET devuelve�ERRORLEVEL en 1 si no se encuentra el nombre
de la variable en el entorno actual.

El comando SET no permite� que un signo de igual "=" sea parte de una variable.

Se han agregado dos modificadores nuevos al comando SET:

```
SET /A expression
SET /P variable=[promptString]
```

El modificador **/A**:

Especifica que la cadena a la derecha del signo de igual es una expresi�n num�rica que es evaluada. El evaluador de expresiones es bastante simple y es compatible con las siguientes operaciones, en orden de precedencia decreciente:

 - **()** : agrupar
 - **! ~ -** : operadores unarios
 - **+ -** : operadores aritm�ticos
 - **<< >>** : desplazamiento logico
 - **&** : bit a bit 
 - **^** : bit a bit o exclusivo
 - **|** : bit a bit
 - **=, =\*, /=, %=, +=, -=** : asignaci�n 
 - **&=, ^=, |=, <<=, >>=** : separador de expresi�n

El modificador **/P**:

Permite establecer el valor de una variable para una l�nea de entrada escrita por el usuario. Muestra la cadena del s�mbolo del sistema
antes de leer la l�nea de entrada. La cadena del s�mbolo del sistema puede
estar vac�a.

La sustituci�n de variables de entorno ha sido mejorada as�:

```
%PATH:str1=str2%
```

**Pedir la entrada del usuario**

```bat
@echo off
set /p MYNAME="Name :"
rem Mostrar entrada
echo Your name is: %MYNAME%
```





La sintaxis normal del comando FOR es: 

```bat
FOR %var IN (lista) DO (
	comando
	comando
)
```

Pero si lo vamos a usar dentro de un archivo BAT ser� as�:

```bat
FOR %%var IN (lista) DO (
	comando
	comando
	...
)
```

Observa que ahora la variable "var" va precedida por dos simbolos de "%". Adem�s, si este for est� dentro de un archivo BAT el nombre de la variable debe usar UNA SOLA LETRA (p.ej: $$n, %%i, %%j, etc.)

**Ejemplos:**

```bat
@echo off
echo example for: 

FOR %%A IN (uno dos tres cuatro cinco) DO (
	echo %%A
)
pause>nul
```





Si el ciclo "for" est� dentro de un archivo BAT, y tome los valores posicionales que se pasan cuando se llama al archivo desde la consola.

```bat
@echo off
echo example for: 

FOR %%x IN (%*) DO (
	echo %%x
)
pause>nul
```

Cuando lo llamemos debemos hacerlo de la siguiente manera:

```cmd
example_for.bat uno dos tres cuatro cinco
```

Si queremos recorrer una lista de archivos de un determinado directorio (solo archivos, no directorios):

```bat
@echo off
echo example for: 

FOR %%f IN (*) DO (
	echo %%f
)
pause>nul
```

Y si queremos mover a la papelera de reciclaje algunos archivos con determinadas extensiones:

```bat
@echo off
echo example for: 

FOR %%f IN (*.jpg, *.mp3, *.bmp) DO (
	move %%f %UserProfile%\Desktop
)
pause>nul
```

### Mejoras en el for

**Recursivida:**

FOR /R [ruta] %V IN (lista) DO comando

**Directorios:**

FOR /D [ruta] %V IN (lista) DO comando

**Lista con contador:**

FOR /L [ruta] %V IN (inicio, incremento, fin) DO comando

**Recorrido de Tokens en lineas de texto:**

FOR /F ["tokens=... delims=..."] %V IN (inicio, incremento, fin) DO comando


**Ejemplo: parametro/R**

Recorrer y mostrar todos los archivos de la unidad C: empezando en su directorio raiz y recorriendo recursivamente el resto de directorio que contiene:

```bat
@echo off
echo example for: 

FOR /R c:\ %%v IN (*) DO (
	echo %%v
)
pause>nul
```

Una variaci�n de este ejemplo ser�a el buscar un determinado tipo de archivos dentro de un directorio recursivamente. Voy a buscar todos los archivos "dll" y "exe" dentro del directorio "windows":

```bat
@echo off
echo example for: 

FOR /R c:\windows %%v IN (*.dll, *.exe) DO (
	echo %%v
)
pause>nul
```

**Ejemplo: parametro/D**

Si lo que me interesa es listar los directorios en vez de los archivos:

```bat
@echo off
echo example for: 

FOR /D %%v IN (*) DO (
	echo %%v
)
pause>nul
```

Y si lo quiero hacer recursivamente puedo a�adir "/R" al comando anterior:

```bat
@echo off
echo example for: 

FOR /R /D %%v IN (*) DO (
	echo %%v
)
pause>nul
```

Y si quiero hacerlo recursivamente desde un directorio concreto (p.ej: c:\windows):

```bat
@echo off
echo example for: 

FOR /R c:\windows /D %%v IN (*) DO (
	echo %%v
)
pause>nul
```

**Ejemplo: parametro/L**

Para crear un tipico bucle contador 1 a 10, saltando de 1 en 1:

```bat
@echo off
echo example for: 

FOR /L %%x IN (1, 1, 10) DO (
	echo %%x
)
pause>nul
```



Y saltando de 2 en 2:

```bat
@echo off
echo example for: 

FOR /L %%x IN (1, 2, 10) DO (
	echo %%x
)
pause>nul
```

Hay que observar que el primer numero dentro del parentesis es el valor inicial que tomar� la variable "%x", el segundo numero es el incremento que sufrir� dicha variable en la proxima iteracion del FOR, y el tercer n�mero es el valor m�ximo que tomar� dicha variable y que cuando alcance o supere dicho valor, el bucle FOR terminar� de ejecutarse.


**Otro ejemplo**:

Archivo BAT que crea varios archivos vacios y los llama a todos con el mismo nombre, pero terminados en un numero diferente:

```bat
@echo off
cls

set/p nombre=Indica el nombre de los archivos a crear:

set/p num=Cuantos archivos hay que crear?:

for /L %%x in (1, 1, %num%) do (
  echo 2> %%x%nombre%
)
pause>nul
```

**EJEMPLO: (parametro /F)**

Recorrer un archivo y mostrar solo la primera palabra de cada linea:

```bat
@echo off
cls

for /F %%x in (archivo.txt) do (
  echo %%x
)
pause>nul
```

 El FOR va recorriendo todas las lineas, y cada linea se ha dividido en "tokens" (token=palabra). La variable del for almacena la primera palabra de cada linea.


**EJEMPLO: (parametro /F con tokens)**

 Podemos seleccionar varios tokens mediante la clausula tokens=. Los distintos tokens se ir�n guardando autom�ticamente en variables alfabeticamente consecutivas a partir de la variable creada en el for.

 En el siguiente ejemplo nos quedamos con los tokens (palabras) 1,3 y 5 de cada linea:

 ```bat
 @echo off
cls

for /F "tokens=1, 3, 5" %%a in (archivo.txt) do (
  echo %%a %%b %%c
)
pause>nul
 ```

observa que aunque yo solamente he definido la variable "%%a" en el FOR, las variables "b" y "c" se crean automaticamente.

Podemos escoger rangos, como en el siguiente ejemplo, en el que vamos a escoger los tokens del 1 al 3, y adem�s el token 5

 ```bat
 @echo off
cls

for /F "tokens=1-3,5" %%a in (archivo.txt) do (
  echo %%a %%b %%c %%d
)
pause>nul
 ```

 O si queremos capturar la l�nea completa a partir de la septima palabra:

  ```bat
 @echo off
cls

for /F "tokens=7*" %%a in (archivo.txt) do (
  echo %%a
)
pause>nul
 ```

O si queremos capturar la linea completa:


  ```bat
 @echo off
cls

for /F "tokens=*" %%a in (archivo.txt) do (
  echo %%a
)
pause>nul
 ```


 EJEMPLO8: (parametro /F con delimitadores)

Adem�s de la clausula "tokens" con el par�metro "/F", podemos usar la clausula "delims", que indica la separacion entre los distintos tokens. Por defecto, los caracteres delimitadores entre tokens son los espacios en blanco y los tabuladores.

En el siguiente ejemplo anulamos los delimitadores y obtenemos lo mismo que antes:

for /F "delims=" %%a in (fichero.txt) do (
  echo %%a
)

Si queremos usar como delimitadores los simbolos de puntuacion, como el punto, la coma, el punto y coma, etc...:

for /F "delims=.,;:" %%a in (fichero.txt) do (
  echo %%a


http://profesoremiliobarco.blogspot.com/2012/05/comando-for-para-archivos-bat.html




### <a name="time"><u>Time</u></a>


Muestra o establece la hora del sistema.


```
TIME  [/T | hora]
```

Escriba TIME sin par�metros para mostrar la hora actual y poder
especificar una nueva hora. Presione Entrar si no desea cambiar la hora.

Si est�n habilitadas las extensiones de comandos el comando TIME admite
el par�metro **/T** que indica al comando mostrar tan solo la
hora actual, sin pedir una nueva hora.


### <a name="title"><u>Title</u></a>


Fija el t�tulo de la ventana en la ventana del s�mbolo del sistema.


```
TITLE [cadena]
```

- **cadena** : Especifica el t�tulo de la ventana del s�mbolo del sistema.

<p align="center">
	<img src="assets/img/title_command.png" alt="title" width="650" height="350"/>
</p>



### <a name="type"><u>Type</u></a>


Muestra el contenido de uno o m�s archivos de texto.

```
TYPE [unidad:][ruta]archivo
```


<p align="center">
	<img src="assets/img/type_command.png" alt="title" width="650" height="350"/>
</p>



### <a href="#pause"><u>Pause</u></a>

Suspende el proceso de un programa por lotes y muestra el mensaje  
`Presione una tecla para continuar. . .` 

### <a href="#pause"><u>Shutdown</u></a>


```
Uso: shutdown [/i | /l | /s | /r | /g | /a | /p | /h | /e | /o] [/hybrid] [/f]
    [/m \\equipo][/t xxx][/d [p|u:]xx:yy [/c "comentario"]]
```

- **Sin argumentos**: Muestra la ayuda. Es lo mismo que escribir /?.
- **/?**: Muestra la ayuda. Es lo mismo que no especificar argumentos.
- **/i**: Muestra la interfaz gr�fica de usuario (GUI). Debe ser la primera opci�n.
- **/l**: Cierra la sesi�n. No se puede utilizar con las opciones /m o /d.
- **/s**: Apaga el equipo.
- **/r**: Apaga completamente y reinicia el equipo.
- **/g**: Apaga completamente y reinicia el equipo. Despu�s de que el sistema reinicie las aplicaciones registradas.
- **/a**: Anula el apagado del sistema. Solo se puede usar durante el per�odo de tiempo de espera.
- **/p**: Apaga el equipo local sin tiempo de espera ni advertencia. Se puede usar con las opciones /d y /f.
- **/h**: Hiberna el equipo local. Se puede usar con la opci�n /f.
- **/hybrid**: Realiza un apagado del equipo y lo prepara para un inicio r�pido. Debe usarse con la opci�n /s.
- **/e**: Documenta la raz�n del apagado inesperado de un equipo.
- **/o**: Va al men� de opciones de arranque avanzadas y reinicia el equipo. Debe usarse con la opci�n /r.
- **/m \\\\equipo**: Especifica el equipo de destino.
- **/t xxx**: Establece el per�odo de tiempo de espera antes del apagado en xxx segundos. El intervalo v�lido es de 0 a 315360000 (10 a�os); el valor predeterminado es 30. Si el per�odo de tiempo de espera es superior a 0, el par�metro /f es impl�cito.
- **/c "comentario"**: Comentario acerca de la raz�n del reinicio o apagado. Se permiten 512 caracteres como m�ximo.
- **/f**: Fuerza el cierre de las aplicaciones que se ejecutan sin advertir previamente a los usuarios. El par�metro /f es impl�cito cuando se especifica un valor mayor que 0 para el par�metro /t.
- **/d [p|u:]xx:yy**:  Proporciona la raz�n del reinicio o apagado.
	+ **p**: indica que el reinicio o el apagado est� planeado.
	+ **u**: indica que la raz�n est� definida por el usuario. Si no se especifica p ni u, el reinicio o el apagado no estar�n planeados.
	+ **xx**: es el n�mero de raz�n principal (entero positivo inferior a 256).
	+ **yy**: es el n�mero de raz�n secundario (entero positivo inferior a 65536).  
	**Razones en este equipo**:  
	(E = Se esperaba U = No se esperaba P = Planeado, C = Definido por el cliente)

	|Tipo|Princ.|Secund.|T�tulo|
	|----|------|-------|------|
	|U   |0	    |0	    |Otros (no planeado)|
	|E   |0	    |0	    |Otros (no planeado)|
    |E P |0	    |0	    |Otros (planeado)|
    |U   |0	    |5	    |Otro error: el equipo no responde|
    |E   |1	    |1	    |Hardware: mantenimiento (no planeado)|
    |E P |1	    |1	    |Hardware: mantenimiento (planeado)|
    |E   |1	    |2	    |Hardware: instalaci�n (planeada)|
    |E P |1	    |2	    |Hardware: instalaci�n (planeada)|
    |E   |2	    |2	    |Sistema operativo: recuperaci�n (no planeada)|
    |E P |2	    |2	    |Sistema operativo: recuperaci�n (planeada)|
    |P 	 |2	    |3	    |Sistema operativo: actualizaci�n (planeada)|
    |E   |2	    |4	    |Sistema operativo: reconfiguraci�n (no planeada)|
    |E P |2	    |4	    |Sistema operativo: reconfiguraci�n (planeada)|
    |P 	 |2	    |16	    |Sistema operativo: service pack (planeado)|
    |	 |2	    |17	    |Sistema operativo: correcci�n urgente (no planeada)|
    |P 	 |2	    |17	    |Sistema operativo: correcci�n urgente (planeada)|
    |    |2	    |18	    |Sistema operativo: correcci�n de seguridad (no plan.)|
    |P 	 |2	    |18	    |Sistema operativo: correcci�n de seguridad (planeada)|
    |E   |4	    |1	    |Aplicaci�n: mantenimiento (no planeado)|
    |E P |4	    |1	    |Aplicaci�n: mantenimiento (planeado)|
    |E P |4	    |2	    |Aplicaci�n: instalaci�n (planeada)|
    |E   |4	    |5	    |Aplicaci�n: sin respuesta|
    |E   |4	    |6	    |Aplicaci�n: inestable|
    |U   |5	    |15	    |Error del sistema: sistema detenido|
    |U   |5     |19	    |Problema de seguridad (no planeado)|
    |E   |5	    |19	    |Problema de seguridad (no planeado)|
    |E P |5	    |19	    |Problema de seguridad (planeado)|
    |E   |5	    |20	    |P�rdida de conectividad de red (no planeada)|
    |U   |6	    |11	    |Error de alimentaci�n: se desconect� el enchufe|
    |U   |6	    |12	    |Error de alimentaci�n: externo|
    |P 	 |7	    |0	    |Apagado de la API heredada|

