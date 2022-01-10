## <u style="padding-left:15px;">Gu�a r�pida CMD</u> <img src="assets/img/cmd.ico" width="30" align="left">



- [Rutas](#mark0)
	+ [Rutas absolutas](#)
	+ [Rutas relativas](#)
	+ [Variable](#variables)

<a name="top"></a>

- [Comandos](#mark0)
	* [assoc](#assoc)
    * [at](#at)
    * [attrib](#attrib)
    * [bcdedit](#bcdedit)
    * [break](#break)
    * [cacls](#cacls)
    * [call](#call)
    * [chcp](#chcp)
    * [chdir o cd](#chdir)
    * [chkdsk](#chkdsk)
    * [chkntfs](#chkntfs)
    * [cls](#cls)
    * [cmd](#cmd)
    * [color](#color)
    * [comp](#comp)
    * [compact](#compact)
    * [convert](#convert)
    * [copy](#copy)
    * [date](#date)
    * [dir](#dir)
    * [exit](#exit)
    * [if](#if)
    * [mkdir - md](#mkdir)
    * [rem](#rem)
    * [rmdir](#mark5)
    * [pause](#pause)
    * [prompt](#prompt)
    * [start](#start)
    * [shutdown](#shutdown)
    * [ipconfig](#ipconfig)
    * [time](#time)
    * [title](#title)
    * [type](#type)



### <a name="assoc"><u>Assoc</u></a>

Muestra o modifica las asociaciones de extensiones de archivos. La asociaci�n de las extensiones le permite a Windows saber con qu� aplicaci�n podr� abrir un archivo por ejemplo, la extensi�n *xls* est� asociada a Excel.


```
ASSOC [.ext[=[fileType]]]
```

**Par�metros**

- **.ext**: Especifica la extensi�n con la cual asociar el tipo de archivo
- **fileType**: Especifica el tipo de archivo con el que asociar la extensi�n

**Observaciones**

- Escribir ASSOC sin par�metros para ver las asociaciones de archivo actuales.
- Si ASSOC es llamado con solo la extensi�n de archivo, mostr�r� la asociaci�n actual del archivo para esa extensi�n. Si no especifica nada para el tipo de archivo y el comando se eliminar� la asociaci�n para la extensi�n de archivo.
- Para eliminar una asociaci�n de una extensi�n de archivo agrega un espacio en blanco despues del signo igual =.
- Puedes utilizar el operador de redirecci�n > para enviar la salida del comando **ASSOC** a un archivo de texto.
- Para realizar modificaciones debemos abrir la sesi�n de CMD con permisos de administrador.

**Ejemplos**

Para ver las asociaciones de la extensi�n .xls ejecuta lo siguiente:

```bat
assoc .xls
:: .xls=Excel.Sheet.8
```

Para ver enviar todas las asociaciones a un archivo txt.

```bat
assoc > asociaciones.txt
```

Para borrar la asociaci�n txt, recuerda incluir un espacio en blanco despu�s del signo igual.

```bat
assoc .txt= 
```

Para asociar las extensi�n *.txt* con el programa Word.

```bat
assoc .txt=Word.Document.8
:: Var�a seg�n Versi�n del Producto y del S.O 
```

[volver a �ndice](#top) &#x2934;

---

### <a name="at"><u>At</u></a>


El comando **AT** programa la ejecuci�n de comandos y programas en un equipo a una hora y fecha especificadas. El comando a�n se encuentra disponible por cuestiones de compatibilidad, pero ha sido extendido en el comando [SCHTASKS](#) que permite opciones m�s avanzadas. No obstante es posible emplearlo para la programaci�n de tareas sencillas. Para poder usar esta herramientas necesita  **'Abrir como Administrador'** el s�mbolo de sistema.  


```
at [\Computername][{[ID] [/delete] | /delete [/yes]}]
at [[\Computername] Hours:Minutes [/interactive] [{/every:date[,...] | /next:date[,...]}] command]
```

<p align="center">
	<img src="assets/img/open_admin.png" alt="open_admin"
	width="500">
</p>


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


- **Eliminar todos los comandos programados**

```bash
AT /DELETE /Y
```

- **Cancelar la tarea del ID 2**

```bash
AT 2 /DELETE 
```

[volver a �ndice](#top) &#x2934;

---

### <a name="attrib"><u>Attrib</u></a>


Muestra o cambia los atributos del archivos o directorios. Si se usa sin par�metros, **attrib** muestra los atributos de todos los archivos en el directorio actual.


```
ATTRIB [+R | -R] [+A | -A] [+S | -S] [+H | -H] [+I | -I]
	   [unidad:] [ruta] [nombreArchivo] [/S [/D] [/L]]
```

**Par�metros:**

- **/S**: Procesa archivos que coinciden en la carpeta y todas las subcarpetas actuales.
- **/D**: Tambi�n procesa carpetas.
- **/L**: Se trabaja en los atributos del v�nculo simb�lico en vez de en el destino del v�nculo simb�lico.
- **ruta**: Unidad y/o nombre de archivo, por ejemplo, **C:\*.txt**


**Key**:

- **(+)**: Activar un atributo
- **(-)**: Borrar un atributo 


**Ejemplo:**


<p>
	<img src="assets/img/attrib.png" alt="attrib"/>
</p>


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

<p align="center">
	<img src="assets/img/file1_fail.png" alt="fail"/>
</p>

Estos cambios tambi�n afectan el modo gr�fico en en algunos programas como word:

<p align="center">
	<img src="assets/img/attrib2.png" alt="example"/>
</p>


Si queremos mantener nuestro archivo **file1.txt** adem�s del atributo de solo lectura que sea tambi�n oculto, volvemos a nuestro s�mbolo de sistema y ejecutamos el siguiente comando: 

```bash
attrib +h file1.txt
# Ahora si vemos los atributos nuevamente con:
attrib file1.txt
# Obtendriamos la siguiente salida: 
# A    HR       C:\Users\home\Desktop\file1.txt
```

Si listaramos los archivos y carpetas con el comandor **dir** pasar�a lo siguiente:  

```bat
dir /b
:: repository
:: comandos.txt

:: Ver los archivos ocultos y resumido con:
dir /b/a
:: repository
:: comandos.txt
:: file1.txt

:: Ver solo los archivos oculos y resumido con:
dir /b/a:h
:: file1.txt
```

Una cosa a tener en cuenta es que no podemos tener asignado el **atributo S** con el **atributo H** y viceversa. Lo mismo pasa con **S** y **R**. Para poder asignarlo, debemos primero quitar el atributo correspondiente:

Ejemplo:  

```bat
attrib -r +s file1.txt
:: o en caso contrario
attrib -s +r file1.txt
```

Por otra parte, los atributos tambi�n pueden ser modificados desde el modo gr�fico, simplemente con seleccionar o deseleccionar el atributo, para ello debemos hacer clic derecho en el archivo e ir a sus propiedades:  


<p align="center">
	<img src="assets/img/properties.png" alt="properties"
	width="400">
	<img src="assets/img/properties2.png" alt="properties2"
	width="400" height="510">
</p>

[volver a �ndice](#top) &#x2934;

---

### <a name="bcdedit"><u>Bcdedit</u></a>

**BCDEDIT**: Editor del almac�n de datos de la configuraci�n de arranque (BCD)

La herramienta de la l�nea de comandos Bcdedit.exe modifica el almac�n de datos de la configuraci�n de arranque. El almac�n de datos de la configuraci�n de arranque contiene par�metros de configuraci�n de arranque y controla el modo en que arranca el sistema operativo.

Estos par�metros se encontraban antes en el archivo **Boot.ini** en sistemas operativos BIOS o en las entradas RAM no vol�til en sistemas operativos basados en EFI (Extensible Firmware Interface). Puede usar Bcdedit.exe para agregar, eliminar, editar y anexar entradas en el almac�n de datos de la configuraci�n de arranque.

Para obtener informaci�n detallada sobre comandos y opciones, escriba:

```bat
bcdedit.exe /? <comando>
``` 

Por ejemplo, para mostrar informaci�n detallada sobre el comando **/createstore**, escriba:

```bat
bcdedit.exe /? /createstore
```

Para obtener una lista alfab�tica de temas del archivo de ayuda, ejecute:

```bat
bcdedit /? TOPICS
```

<b><u>Comandos que operan en un almac�n</u></b>


- **/createstore**: Crea un nuevo almac�n de datos de la configuraci�n de arranque vac�o.
- **/export**: Exporta el contenido del almac�n del sistema a un archivo. Este archivo se puede usar m�s adelante para restaurar el estado del almac�n del sistema.
- **/import**: Restaura el estado del almac�n del sistema mediante un archivo de copia de seguridad creado con el comando /export.
- **/sysstore**: Establece el dispositivo de almac�n del sistema (solo afecta a los sistemas EFI, pero no se mantiene entre reinicios y solo se usa en los casos en que el dispositivo de almac�n del sistema es ambiguo).


<b><u>Comandos que operan en entradas de un almac�n</u></b>

- **/copy**: Hace copias de las entradas del almac�n.
- **/create**: Crea nuevas entradas en el almac�n.
- **/delete**: Elimina entradas del almac�n.
- **/mirror**: Crea un reflejo de las entradas del almac�n.

Ejecute bcdedit /? ID para obtener informaci�n sobre los identificadores usados por estos comandos.


<b><u>Comandos que operan en opciones de entrada</u></b>

- **/deletevalue**: Elimina las opciones de entrada del almac�n.
- **/set**: Establece valores de opciones de entrada en el almac�n.


Ejecute bcdedit /? TYPES para ver una lista de tipos de datos usados por estos
comandos.

Ejecute bcdedit /? FORMATS para ver una lista de formatos de datos v�lidos.


<b><u>Comandos que controlan la salida</u></b>

- **/enum**: Muestra la lista de entradas del almac�n.
- **/v**: Opci�n de la l�nea de comandos que muestra identificadores de entrada completos, en lugar de usar nombres para los identificadores conocidos. Use /v por s� solo como comando para mostrar los identificadores de entrada completos para el tipo ACTIVE.

Ejecutar "bcdedit" por s� solo equivale a ejecutar "bcdedit /enum ACTIVE".


<b><u>Comandos que controlan el administrador de arranque</u></b>

- **/bootsequence**: Establece la secuencia de arranque �nica para el administrador de arranque.
- **/default**: Establece la entrada predeterminada que usar� el administrador de arranque.
- **/displayorder**: Establece el orden en que el administrador de arranque muestra el men� de arranque m�ltiple.
- **/timeout**: Establece el valor de tiempo de espera del administrador de arranque.
- **/toolsdisplayorder**: Establece el orden en que el administrador de arranque muestra el men� de herramientas.

<b><u>Comandos que controlan los Servicios de administraci�n de emergencia para una aplicaci�n de arranque</u></b>

- **/bootems**: Habilita o deshabilita los Servicios de administraci�n de emergencia para una aplicaci�n de arranque.
- **/ems**: Habilita o deshabilita los Servicios de administraci�n de emergencia para una entrada del sistema operativo.
- **/emssettings**: Establece los par�metros globales de los Servicios de administraci�n de emergencia.

<b><u>Comandos que controlan la depuraci�n</u></b>

- **/bootdebug**: Habilita o deshabilita la depuraci�n de arranque para una aplicaci�n de arranque.
- **/dbgsettings**: Establece los par�metros globales del depurador.
- **/debug**: Habilita o deshabilita la depuraci�n de kernel para la entrada de un sistema operativo.
- **/hypervisorsettings**: Establece los par�metros para el hipervisor.


<b><u>Resumen:</u></b>

BCDEDIT es un comando disponible en la consola de CMD que permite mediante la herramienta Bcdedit.exe, cambiar, modificar y personalizar la configuraci�n de arranque de Windows. Podemos usarlo de forma sencilla para establecer el orden de los sistemas operativos, su nombre en el men� de arranque, usar sistemas en discos virtuales, habilitar o deshabilitar efectos, etc. 
Es imprescindible en los casos que tenemos instalados dos o m�s versiones de Windows diferentes en un mismo equipo.

**Sistemas de arranque de Windows**

Los par�metros de inicio de Windows se guardan de forma diferente, dependiendo de la versi�n del sistema operativo.

- **Arranque de Windows XP**: En Windows XP y sistemas anteriores se usa NTLDR (abreviatura de NT Loader), que es el gestor de arranque. Su archivo de configuraci�n es **Boot.ini**, un sencillo archivo de texto que se puede ver en la ra�z de la unidad principal. En �l se relacionan los sistemas operativos instalados en el equipo, cu�l de ellos es el predeterminado, el *timeout* o tiempo de espera, etc. Boot.ini se puede modificar usando el Bloc de notas u otro editor de texto.

- **Arranque de Windows Vista y 7**: En Windows Vista se introduce y se usa tambi�n en Windows 7, el nuevo Administrador de arranque de Windows (Windows Boot Manager) BCD (Boot Configuration Data), en ingles: Datos de la Configuraci�n de arranque.
Este sistema m�s moderno permite el arranque en sistemas que no usan BIOS.
La informaci�n se guarda en una base de datos similar al Registro de Windows, en un archivo llamado: **bootmgr** y en **C:\Boot\BCD.LOG.** Para modificarla se usa el comando BCDEDIT

- **Arranque de Windows 8**: Windows 8 incluye un nuevo sistema de arranque, UEFI Secure Boot que seg�n Microsoft ofrece m�s seguridad y aprovecha la nueva funci�n de Inicio r�pido que permite arrancar el sistema con m�s rapidez.
No obstante en caso de desearlo se puede cambiar al anterior Windows Boot Manager.


<b><u>Uso de BCDEDIT:</u></b>


Usando BCDEDIT se puede agregar, eliminar, editar y anexar entradas en el almac�n de datos de la configuraci�n de arranque del equipo. BCDEDIT es necesario usarlo en la consola de CMD con permisos de administrador.

Al usar en la consola el comando BCDEDIT sin ning�n par�metro, solo se muestra la configuraci�n de arranque actual del equipo.

- **En la secci�n Administrador de arranque de Windows**: se muestra el sistema de arranque, el sistema operativo predeterminado (default), etc.
- **En la secci�n Cargador de arranque de Windows**: se muestran los sistemas operativos instalados.

<p align="center">
	<img src="assets/img/bcdedit.png">
</p>

Los principales valores son los siguientes:

- **Identificador**: es el identificador usado para dicha partici�n, encerrado entre dos llaves. Es necesario conocerlo para hacer algunos ajustes usando BCDEDIT. En caso del sistema operativo predeterminado el valor es: {current}. Otro sistema operativo se representa con un identificador �nico global (GUID), es una secuencia alfanum�rica, por ejemplo: {2807aaab-f2a8-11de-8e0c-b4db26ac8165}. Si el sistema es Windows XP o anterior se indica: {ntldr}. Para conocer todos los identificadores usa en la consola: `bcdedit /? ID`
- **Description**: indica el nombre que aparece en el men� de arranque.
- **Bootmenupolicy**: solo en Windows 8, tiene dos valores:
Legacy, sistema de arranque clasico, igual que en Windows 7
Standard, sistema de arranque predeterminado


<b><u>Usos pr�cticos del comando BCDEDIT</u></b>


Crear y guardar un respaldo de la configuraci�n de arranque Usa:

```bat
bcdedit /export C:\respaldo.txt
```

Restaurar el respaldo guardado:


```bat
bcdedit /import C:\respaldo.txt
```

Cambiar el nombre del sistema operativo en el men� de arranque

En caso de tener dos o m�s sistemas instalados en el equipo, cambia los nombres que aparecen en el men� de arranque de la siguiente forma:

```bat
:: bcdedit /set {identificador} description "Nombre"

:: Tres ejemplos:
bcdedit /set {c15d0021-1aec-11dc-b49c-9726d7e2da89} description "Windows 7" 
bcdedit /set {current} description "Windows 8" 
bcdedit /set {ntldr} description "Windows XP"
```

Agregar al men� de arranque otro sistema en una unidad virtual usa:

```bat
bcdedit /set {cea643bf-b4b4-6786-543a-fa67654f5d71} device partition=F:
```

Habilitar en Windows 8 el sistema cl�sico de arranque

Windows 8 usa un sistema de arranque mucho m�s r�pido, pero en caso de tener dos o m�s sistemas operativos en el equipo, esto se vuelve una molestia cuando hay necesidad de alternar entre sistemas diferentes. Para usar el mismo Windows Boot Manager que en Windows 7, usa el siguiente comando:

```bat
bcdedit /set {default} bootmenupolicy legacy
:: Para cambiar al modo predeterminado usa:
bcdedit /set {default} bootmenupolicy standard
```

En ambos casos aseg�rate que aparece el mensaje: La operaci�n se complet� correctamente.



Deshabilitar el logotipo de arranque en Windows 8 usa:

```bat
bcdedit /set {globalsettings} custom:16000067 true
```

Para restaurarlo usa:

```bat
bcdedit /set {globalsettings} custom:16000067 false
:: o
bcdedit /deletevalue {globalsettings} custom:16000067
```

Deshabilitar mensajes de Windows 8 en el arranque usa:

```bat
bcdedit /set {globalsettings} custom:16000068 true
:: Para restaurarlos usa:
bcdedit /set {globalsettings} custom:16000068 false
:: o
bcdedit /deletevalue {globalsettings} custom:16000068
```


[volver a �ndice](#top) &#x2934;

---

### <a name="break"><u>Break</u></a>

Activa o desactiva Ctrl+C extendido en DOS

Est� presente para que haya compatibilidad con sistemas DOS, pero no tiene efecto en Windows.

Si se habilitan las extensiones de comando y se ejecuta en la plataforma de Windows, el comando BREAK insertar� un punto de interrupci�n dentro del c�digo, si est� siendo depurado por un depurador.

[volver a �ndice](#top) &#x2934;

---

### <a name="cacls"><u>Cacls</u></a>


**NOTA**: el comando Cacls est� obsoleto, use Icacls.

Muestra o modifica listas de control de acceso (ACL) de archivos

```
CACLS archivo [/T] [/M] [/L] [/S[:SDDL]] [/E] [/C] [/G usuario:perm]

               [/R usuario [...]] [/P usuario:perm [...]] [/D usuario [...]]
```


- **archivo**: Muestra las ACL.
- **/T**: Cambia las ACL de archivos especificados en el directorio actual y todos los subdirectorios.
- **/L**: Trabaja en el propio v�nculo simb�lico en lugar del destino.
- **/M**: Cambia las ACL de los vol�menes montados en un directorio.
- **/S**: Muestra la cadena SDDL para la DACL.
- **/S:SDDL**: Reemplaza las ACL por las especificadas en la cadena SDDL (no v�lido con /E, /G, /R, /P ni /D).
- **/E**: Edita la ACL en vez de remplazarla.
- **/C**: Contin�a, omitiendo los errores de acceso denegado.
- **/G usuario:perm**: Concede derechos de acceso del usuario. Perm puede ser: 
	+ **R**: Leer
	+ **W**: Escribir
	+ **C**: Cambiar (escribir)
	+ **F**: Control total
- **/R usuario**: Revoca derechos del usuario (solo v�lida con /E).
- **/P usuario:perm**: Reemplaza derechos de acceso del usuario. Perm puede ser: 
	+ **N**: Ninguno
	+ **R**: Leer
	+ **W**: Escribir
	+ **C**: Cambiar (escribir)
	+ **F**: Control total
- **/D usuario**: Deniega acceso al usuario especificado.

Se pueden usar comodines para especificar m�s de un archivo. Puede especificar m�s de un usuario.

<b><u>Abreviaturas:</u></b>

- **CI**: Herencia de contenedor.
- **ACE**: Se heredar� por directorios.
- **OI**: Herencia de objeto.
- **ACE**: se heredar� por archivos.
- **IO**: Solo heredar. ACE no se aplica al archivo o directorio actual.
- **ID**: Heredado. ACE se hered� de la ACL del directorio principal.

[volver a �ndice](#top) &#x2934;

---

### <a name="call"><u>Call</u></a>

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

[volver a �ndice](#top) &#x2934;

---

### <a name="chcp"><u>Chcp</u></a>

Muestra o establece el n�mero de la p�gina de c�digos activa.

```
CHCP [nnn]
```

- **nnn**: Especifica una p�gina de c�digos.

Escriba CHCP sin par�metro para mostrar el n�mero de la p�gina de c�digos activa.


|P�gina de c�digos|	Pa�s o regi�n, o idioma|
|-----------------|------------------------|
|437              |Estados Unidos          |
|850	          |Multiling�e (Latino I)  |
|852	          |Eslavo (Latino II)      |
|855	          |Cir�lico (Ruso)         |
|857	          |Turco                   |
|860	          |Portugu�s               |
|861	          |Island�s                |
|863	          |Franc�s canadiense      |
|865	          |N�rdico                 |
|866	          |Ruso                    |
|869	          |Griego moderno          |


[volver a �ndice](#top) &#x2934;

---

### <a name="chdir"><u>Chdir o cd</u></a>


Muestra el nombre del directorio actual o cambia de directorio.

```
CHDIR [/D] [unidad:][ruta]
CHDIR [..]
CD [/D] [unidad:][ruta]
CD [..]
```

- **CD ..**: Especifica que desea cambiar al directorio superior.
- **CD unidad**: (Ej: CD C:) para ver el directorio actual de la unidad especificada.
- **CD sin par�metros**: para ver la unidad y el directorio actual.
- **/D**: Use el modificador /D para cambiar la unidad actual adem�s del directorio actual para una unidad de disco.


Si las extensiones de comando est�n habilitadas, CHDIR cambia as�:

El uso de may�sculas y min�sculas de la cadena del directorio actual se convierte al mismo uso que se tiene en los nombres de unidades. As�:

```bat
CD C:\Users\username\AppData\Local\Temp
::establecer� Temp como el directorio actual 
:: si �ste es el uso de may�sculas y min�sculas en la unidad.
```

El comando CHDIR no trata los espacios como separadores, as� que es posible usar CD para cambiar a un directorio cuyo nombre de subdirectorio contenga un espacio, sin necesidad de escribir el nombre entre comillas. Por ejemplo:

```bat
CD C:\Users\username\Desktop\Mis repositorios
```

es lo mismo que:

```bat
CD "C:\Users\username\Desktop\Mis repositorios"
```

que ser�a lo que hay que escribir si las extensiones estuvieran
deshabilitadas.

[volver a �ndice](#top) &#x2934;

---

### <a name="cls"><u>Cls</u></a>

Borra la pantalla

[volver a �ndice](#top) &#x2934;

---

### <a name="chkdsk"><u>Chkdsk</u></a>

Comprueba un disco y muestra un informe de estado.


```
CHKDSK [volumen[[ruta]archivo]]] [/F] [/V] [/R] [/X] [/I] [/C] [/L[:tama�o]][/B]
```


- **volumen**: Especifica la letra de unidad (seguida por dos puntos), el punto de montaje o el nombre de volumen.
- **archivo**: s�lo para FAT/FAT32 especifica los archivos en donde se comprobar� la fragmentaci�n.
- **/F**: Corrige los errores del disco.
- **/V**: Para FAT/FAT32 muestra la ruta completa y el nombre de cada archivo en el disco. Para NTFS muestra mensajes de limpieza si hay.
- **/R**: Encuentra sectores da�ados y recupera la informaci�n legible (implica /F).
- **/L**: Tama�o S�lo para NTFS: cambia el tama�o del archivo de registro al n�mero especificado de KB. Si no se especifica ning�n tama�o, muestra el tama�o actual.
- **/X**: Obliga al volumen a desmontarse previamente si es necesario. Todos los identificadores abiertos al volumen no ser�n�v�lidos (implica /F).
- **/I**: S�lo para NTFS: realiza una comprobaci�n menos exhaustiva de entradas de �ndice.
- **/C**: S�lo NTFS omite la comprobaci�n de ciclos dentro de la estructura de carpetas.
- **/B**: S�lo NTFS vuelve a evaluar los cl�steres incorrectos en el volumen (implica el uso de /R). 


Los modificadores /I o /C reducen la cantidad de tiempo necesario para ejecutar Chkdsk ya que omiten ciertas comprobaciones en el volumen.


[volver a �ndice](#top) &#x2934;

---

### <a name="chkntfs"><u>Chkntfs</u></a>

```
CHKNTFS volumen [...]
CHKNTFS /D
CHKNTFS /T[: tiempo]
CHKNTFS /X volumen [...]
CHKNTFS /C volumen [...]
```

- **volumen**: Especifica la letra de unidad (seguida por dos puntos), el punto de montaje o el nombre de volumen.
- **/D**: Restaura el funcionamiento predeterminado del equipo; todas las unidades se comprueban al arrancar y chkdsk se ejecuta en aqu�llas que est�n da�adas.
- **/T: tiempo**: Cambia el tiempo de la cuenta atr�s en el inicio de AUTOCHK a la cantidad de tiempo dada en segundos. Si el tiempo no se espec�fica, se mostrar�la configuraci�n actual.
- **/X**: Excluye una unidad de la comprobaci�n predeterminada al arrancar. Las unidades excluidas no se acumulan entre invocaciones de comandos.
- **/C**: Programa una unidad para ser comprobada al arrancar; chkdsk se ejecutar� si la unidad est� da�ada.


Si no se especifican modificadores, CHKNTFS mostrar� si la unidad especificada est�da�ada o programada para ser revisada al reiniciar el equipo de nuevo.


[volver a �ndice](#top) &#x2934;

---

### <a name="cmd"><u>Cmd</u></a>


Inicia una nueva instancia del int�rprete de comandos de Windows

```
CMD [/A | /U] [/Q] [/D] [/E:ON | /E:OFF] [/F:ON | /F:OFF] [/V:ON | /V:OFF]
    [[/S] [/C | /K] cadena]
```

- **/C**: Ejecuta el comando especificado en cadena y luego finaliza.
- **/K**: Ejecuta el comando especificado en cadena pero sigue activo.
- **/S**: Modifica el tratamiento de cadena despu�s de /C o /K (consultar m�s abajo).
- **/Q**: Desactiva el eco
- **/D**: Deshabilita le ejecuci�n de los comandos de AutoRun del Registro (consultar m�s abajo)
- **/A**: Usa ANSI para la salida de comandos internos hacia una canalizaci�n o un archivo.
- **/U**: Usa Unicode para la salida de comandos internos hacia una canalizaci�n o un archivo.
- **/T:fg** Configura los colores de primer y segundo plano (para obtener m�s informaci�n, consulte COLOR /?) ej:  
`cmd /t:5f`.
- **/E:ON**: Habilita las extensiones de comando (consultar m�s abajo).
- **/E:OFF**: Deshabilita las extensiones de comando (consultar m�s abajo).
- **/F:ON**: Habilita los caracteres de terminaci�n de los nombres de archivos y directorios (consultar m�s abajo)
- **/F:OFF**: Deshabilita los caracteres de terminaci�n de los nombres de archivos y directorios (consultar m�s abajo).
- **/V:ON**: Habilita la extensi�n de variables de entorno retardada con `!` como delimitador. Por ejemplo, /V:ON permitir� que !var! extienda la variable var en tiempo de ejecuci�n.  La sintaxis var extiende variables en tiempo de entrada, lo que es bastante diferente cuando se est� dentro de un bucle FOR.
- **/V:OFF**: Deshabilita la extensi�n de variables de entorno retardada.Tenga en cuenta que los comandos m�ltiples separados por el separador de comandos '&&' se aceptan como cadena si est�n entre comillas. Por razones de compatibilidad, /X equivale a /E:ON, /Y equivale a /E:OFF y /R equivale a
/C. Se omitir� cualquier otro tipo de modificador.

Si se especifica /C o /K, lo que viene despu�s de la l�nea de comandos se ejecuta como l�nea de comandos, siguiendo la l�gica siguiente para procesar caracteres de comillas ("):

1. Se conservan las comillas del comando si se cumplen todas las condiciones siguientes:
    + no aparece el modificador /S
    + hay exactamente dos caracteres de comillas
    + no hay caracteres especiales entre ambas comillas, siendo los, caracteres especiales: `&<>()@^|`
    + hay uno o m�s espacios en blanco entre ambas comillas
    + la cadena entre ambas comillas es el nombre de un archivo ejecutable.

2. En caso contrario, el comportamiento cl�sico es comprobar si el primer car�cter es una comilla y de ser as�, quitar �sta y tambi�n la �ltima comilla de la l�nea de comandos, conservando el texto que venga despu�s de �sta.

Si no se especific� /D en la l�nea de comandos, cuando CMD.EXE se inicie, buscar� las variables del Registro REG_SZ/REG_EXPAND_SZ, y si alguna de ellas est� presente, se ejecutar�n en primer lugar.

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\AutoRun

y (o)

HKEY_CURRENT_USER\Software\Microsoft\Command Processor\AutoRun
```

Las extensiones de comando est�n habilitadas de forma predeterminada. Puede deshabilitar las extensiones de una invocaci�n particular con el modificador /E:OFF. Puede habilitar o deshabilitar las extensiones de todas las
invocaciones de CMD.EXE en una sesi�n de inicio de usuario o de equipo si establece con `REGEDIT.EXE` los dos valores de REG_DWORD del Registro siguientes:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\EnableExtensions

y/o

HKEY_CURRENT_USER\Software\Microsoft\Command Processor\EnableExtensions
```

En 0x1 o 0x0. La configuraci�n espec�fica del usuario tiene preferencia respecto a la del equipo. Los modificadores de la l�nea de comandos tienen prioridad sobre la configuraci�n del Registro. En un archivo por lotes, los argumentos SETLOCAL ENABLEEXTENSIONS o DISABLEEXTENSIONS tienen prioridad sobre los modificadores /E:ON o /E:OFF. Para obtener informaci�n m�s detallada, vea SETLOCAL /?. Las extensiones de comando implican cambios y ampliaciones en los siguientes comandos:

- **DEL o ERASE**
- **COLOR**
- **CD o CHDIR**
- **MD o MKDIR**
- **PROMPT**
- **PUSHD**
- **POPD**
- **SET**
- **SETLOCAL**
- **ENDLOCAL**
- **IF**
- **FOR**
- **CALL**
- **SHIFT**
- **GOTO**
- **START** (tambi�n incluye cambios en la invocaci�n de comandos externos)
- **ASSOC**
- **FTYPE**

Para obtener detalles espec�ficos, escriba nombreDelComando /?.
La expansi�n de variables de entorno retardada NO est� habilitada de forma predeterminada. Puede habilitar o deshabilitar la expansi�n de variables de entorno retardada para una invocaci�n particular de CMD.EXE con los
modificadores /V:ON o /V:OFF. Puede habilitar o deshabilitar la expansi�n retardada para todas las invocaciones de CMD.EXE en una sesi�n de inicio de usuario o equipo si establece con REGEDIT.EXE los dos valores de REG_DWORD del Registro siguientes:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\DelayedExpansion

y/o

HKEY_CURRENT_USER\Software\Microsoft\Command Processor\DelayedExpansion
```

en 0x1 o 0x0. La configuraci�n espec�fica del usuario tiene prioridad sobre la configuraci�n del equipo. Los modificadores de la l�nea de comandos tienen prioridad sobre la configuraci�n del Registro. En un archivo por lotes, los argumentos SETLOCAL ENABLEDELAYEDEXPANSION o DISABLEDELAYEDEXPANSION tienen prioridad sobre los modificadores /V:ON o /V:OFF. Para obtener informaci�n m�s detallada, vea SETLOCAL /?.

Si la expansi�n de variables de entorno retardada est� habilitada, se puede usar el car�cter de exclamaci�n para sustituir el valor de la variable de entorno en tiempo de ejecuci�n.

Puede habilitar o deshabilitar la terminaci�n de un nombre de archivo para una invocaci�n particular de CMD.EXE con el modificador /F:ON o /F:OFF. Se puede habilitar o deshabilitar la terminaci�n para todas las invocaciones de CMD.EXE en una sesi�n de inicio de equipo o de usuario estableciendo cualquiera de los dos siguientes valores REG_DWORD en el Registro con REGEDT.EXE:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\CompletionChar

HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\PathCompletionChar
        
y/o

HKEY_CURRENT_USER\Software\Microsoft\Command Processor\CompletionChar

HKEY_CURRENT_USER\Software\Microsoft\Command Processor\PathCompletionChar
```

con el valor hex de un car�cter de control para usarlo en una funci�n particular (por ej. 0x4 es Ctrl-D y 0x6 es Ctrl-F). La configuraci�n de usuario espec�fica tiene precedencia sobre la configuraci�n de la m�quina. Los modificadores de la l�nea de comandos tiene precedencia sobre la configuraci�n del Registro.
Si la terminaci�n est� habilitada con el modificador /F:ON, los dos caracteres de control usados son Ctrl-D para la terminaci�n del nombre del directorio y Ctrl-F para la terminaci�n del nombre de archivo. Para deshabilitar una
terminaci�n de car�cter determinada en el Registro, use el valor del espacio en blanco (0x20), ya que no es un car�cter de control v�lido.

Se invoca la terminaci�n cuando se escriben cualquiera de los dos caracteres de control. La funci�n de terminaci�n, desplaza el contenido de la ruta de acceso hacia la izquierda del cursor, le anexa un car�cter comod�n si no hay ninguno todav�a presente y genera una lista de rutas de acceso que coincidan. Despu�s muestra la primera ruta de acceso que coincida. Si no
coincide ninguna ruta de acceso, emite un sonido y no muestra nada. Posteriormente, el presionar repetidamente el mismo car�cter de control se desplazar� a trav�s de la lista de las rutas de acceso que coinciden. Si presiona la tecla May�s con el car�cter de control se mover� a trav�s de la lista hacia atr�s. Si se edita la l�nea de cualquier manera y presiona el
car�cter de control de nuevo, la lista de ruta de acceso guardada es anulada y se generar� una nueva. Ocurrir� lo mismo si pasa de una terminaci�n de nombre de archivo a uno de directorio. La �nica diferencia entre los dos caracteres de control es que la terminaci�n del car�cter del archivo
coincide con ambos nombres del archivo y del directorio, mientras que la terminaci�n del car�cter del directorio s�lo coincide con los nombres del directorio. Si la terminaci�n del archivo es usada en cualquier construcci�n de comandos de directorio (CD, MD o RD) entonces se asume la terminaci�n del directorio.

El c�digo de terminaci�n trata adecuadamente con nombres de archivo que contienen espacios u otros caracteres especiales colocando comillas entre la ruta de acceso que coincide. Tambi�n, si se hace una copia de seguridad, se llamar� a una terminaci�n dentro de la misma l�nea, el texto a la derecha
del cursor que fue llamado en el punto de la terminaci�n es descartado.

Los caracteres especiales que requieren comillas son:

```
<espacio>&()[]{}^=;!'+,`~
```

[volver a �ndice](#top) &#x2934;

---

### <a name="color"><u>Color</u></a>


Establece los colores de primer plano y fondo predeterminados de la consola. 

```
COLOR [atr]
```

- **atr**: Especifica el atributo de color de la salida de consola

Los atributos de color est�n especificados con dos d�gitos hex (el primero corresponde al segundo plano; el segundo al pr
imer plano). Los d�gitos pueden
ser cualquiera de los siguientes valores:


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



**Ejemplo:**

```bash
color 17
# 1 = Azul para el fondo
# 7 = Blanco para el primer plano
```

[volver a �ndice](#top) &#x2934;

---

### <a name="comp"><u>Comp</u></a>

Compara el contenido de dos archivos o conjuntos de archivos.

```
COMP [datos1] [datos2] [/D] [/A] [/L] [/N=n�mero] [/C] [/OFF[LINE]]
```

- **datos1**: Especifica la ubicaci�n y los nombres de los primeros archivos que se van a comparar.
- **datos2**: Especifica la ubicaci�n y los nombres de los segundos archivos que se van a comparar.
- **/D**: Muestra las diferencias en formato decimal. Esta es la configuraci�n predeterminada.
- **/A**: Muestra las diferencias en caracteres ASCII.
- **/L**: Muestra los n�meros de l�nea para las diferencias.
- **/N=n�mero**: Compara s�lo el n�mero de l�neas especificado de cada archivo.
- **/C**: Omite las may�sculas/min�sculas de ASCII al comparar archivos.
- **/OFF[LINE]**: No omite archivos con el atributo "sin conexi�n" establecido.

Para comparar conjuntos de archivos, use comodines en datos1 y datos2.

[volver a �ndice](#top) &#x2934;

---

### <a name="compact"><u>Compact</u></a>

Muestra o altera la compresi�n de los archivos en particiones NTFS.

```
COMPACT [/C | /U] [/S[:dir]] [/A] [/I] [/F] [/Q] [archivo [...]]
```

- **/C**: Comprime los archivos especificados. Los directorios ser�n marcados para que los archivos agregados despu�s sean comprimidos.
- **/U**: Descomprime los archivos especificados. Los directorios ser�n marcados para que los archivos agregados despu�s no sean comprimidos.
- **/S**: Efect�a la operaci�n especificada en los archivos del directorio dado y todos los subdirectorios. De forma predeterminada, "dir" es el directorio actual.
- **/A**: Muestra los archivos ocultos o los atributos del sistema. Estos archivos se omiten de manera predeterminada.
- **/I**: Contin�a efectuando la operaci�n especificada incluso despu�s de que hayan ocurrido los errores. De forma predeterminada, COMPACT para cuando se encuentra un error.
- **/F**: Exige la operaci�n de compresi�n en todos los archivos especificados, incluso en los que ya est�n comprimidos. Los archivos ya comprimidos se omiten de manera predeterminada.
- **/Q**: Muestra s�lo la informaci�n m�s esencial.
- **archivo**: Especifica un patr�n, archivo o directorio. Si se usa sin par�metros, COMPACT muestra el estado de la compresi�n del directorio actual y cualquier archivo que contenga. Puede usar m�ltiples nombres de archivo y comodines. Debe poner espacios entre los par�metros.


Comprima un archivo desde la l�nea de comandos:

```bat
compact /c archivo.txt
```

[volver a �ndice](#top) &#x2934;

---

### <a name="convert"><u>Convert</u></a>

Convierte un volumen FAT a NTFS.

```
CONVERT volumen /FS:NTFS [/V] [/CvtArea:nombre_archivo] [/NoSecurity] [/X]
```

- **volumen**: Especifica la letra de unidad (seguida por dos puntos) punto de montaje o nombre de volumen.
- **/FS:NTFS**: Especifica que el volumen se convertir� a NTFS.
- **/V**: Especifica que Convert se ejecutar� en modo detallado.
- **/CvtArea:nombre_archivo**: Especifica un archivo contiguo en el directorio ra�z, que ser el marcador de posici�n para los archivos de sistema NTFS.
- **/NoSecurity**: Especifica que la configuraci�n de seguridad en los archivos y directorios convertidos permitir� que todos los usuarios tengan acceso a ellos.
- **/X**: Fuerza a que el volumen se desmonte primero si es necesario. Todos los identificadores abiertos al volumen no ser�n v�lidos.

[volver a �ndice](#top) &#x2934;

---

### <a name="copy"><u>Copy</u></a>

Copia uno o m�s archivos en otra ubicaci�n.

```
COPY [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B ] origen [/A | /B]
     [+ origen [/A | /B] [+ ...]] [destino [/A | /B]]
```


- **origen**: Especifica el archivo o archivos que deben copiarse.
- **/A**: Indica un archivo de texto ASCII.
- **/B**: Indica un archivo binario.
- **/D**: Permite que el archivo de destino se cree sin cifrar.
- **destino**: Especifica el directorio y/o el nombre de archivo de los nuevos archivos.
- **/V**: Comprueba si los nuevos archivos est�n escritos correctamente.
- **/N**: Si est� disponible, usa un nombre de archivo corto al copiar un archivo cuyo nombre no tiene el formato 8.3.
- **/Y**: Suprime la solicitud de confirmaci�n antes de sobrescribir un archivo de destino existente.
- **/-Y**: Solicita confirmaci�n antes de sobrescribir un archivo de destino existente.
- **/Z**: Copia archivos de red en modo reiniciable.
- **/L**: Si el origen es un v�nculo simb�lico, copia el v�nculo al destino en lugar del archivo real al que apunta el v�nculo.

El modificador /Y puede preestablecerse en la variable de entorno COPYCMD. Esto puede anularse con el modificador /-Y en la l�nea de comando. La confirmaci�n del usuario se solicita de forma predeterminada antes de sobrescribir algo, excepto si el comando COPY se ejecuta desde un script por lotes.

Para anexar archivos, especifique un �nico archivo de destino pero varios archivos de origen (con caracteres comodines o el formato archivo1+archivo2+archivo3).


**Ejemplos:**


Copia el archivo.txt dentro de la carpeta 'Mis textos'


```bat
copy archivo.txt "Mis repositorios"
```


Hace una copia en el directorio actual del archivo `contactos.txt` y lo nombra `contactos.bak.txt`


```bat
copy contactos.txt contactos.bak.txt
```



[volver a �ndice](#top) &#x2934;

---

### <a name="date"><u>Date</u></a>


Muestra o establece la fecha.

```
DATE  [/T | fecha]
```

Escriba DATE sin par�metros para mostrar la fecha actual y poder 
especificar una nueva. Presione <kbd>Enter</kbd> para mantener la misma fecha.

Si est�n habilitadas las extensiones de comandos, el comando DATE admite
el par�metro /T, que indica al comando mostrar tan s�lo la fecha actual
sin pedir una nueva fecha.


[volver a �ndice](#top) &#x2934;

---



### <a name="if"><u>If</u></a>


Realiza el procesamiento condicional de los programas por lotes.
	
```
IF [NOT] ERRORLEVEL n�mero comando
IF [NOT] cadena1==cadena2 comando
IF [NOT] EXIST archivo comando
```


- **NOT**: Especifica que Windows debe llevar a cabo el comando solo si la condici�n es falsa.

- **ERRORLEVEL n�mero**: El n�mero especifica una condici�n verdadera si el �ltimo programa que se ejecut� devolvi� un c�digo de salida igual o mayor que el n�mero especificado.

- **cadena1==cadena2**:  Especifica una condici�n verdadera si las cadenas de texto especificadas coinciden.

- **EXIST archivo**: Especifica una condici�n verdadera si el archivo especificado existe.

- **comando**: Especifica el comando que se va a ejecutar si se cumple la condici�n. El comando puede ir seguido de la palabra clave **ELSE**, que ejecutar� el comando tras las palabra clave ELSE si la condici�n especificada es FALSE.

La cl�usula **ELSE** debe aparecer en la misma l�nea que la del comando que sigue a IF  Por ejemplo:

```bat
IF EXIST archivo. (
    del archivo.
) ELSE (
    echo archivo. no existente.
)
```
Lo siguiente NO funcionar� porque el comando del debe terminar con una nueva l�nea:

```bat
IF EXIST archivo. del archivo. ELSE echo archivo. no existente
```

Tampoco funcionar� lo siguiente, ya que el comando ELSE debe estar en la 
misma l�nea que el comando IF:

```bat
IF EXIST archivo. del archivo.
ELSE echo archivo. no existente
```

Si desea mantenerlo todo en una misma l�nea, lo siguiente funcionar�:

```bat
IF EXIST archivo.txt (del archivo.txt) ELSE echo archivo.txt no existente
```

Si los comandos de extensi�n est�n habilitados, IF cambia as�:

 
 - **IF [/I] cadena1 op-de-comparaci�n cadena2 comando**
 - **IF CMDEXTVERSION n�mero comando**
 - **IF DEFINED variable comando**

donde **op-de-comparaci�n** puede ser:

- **EQU**: igual
- **NEQ**: no igual
- **LSS**: menor que
- **LEQ**: menor que o igual
- **GTR**: mayor que
- **GEQ**: mayor que o igual

Y el modificador **/I**, si se especifica, realiza comparaciones de cadena que
no distinguen entre may�sculas y min�sculas. El modificador **/I** tambi�n puede
usarse en la forma cadena1==cadena2 de IF. Estas comparaciones son gen�ricas,
por lo que si tanto cadena1 como cadena2 se constituyen �nicamente por d�gitos
num�ricos, entonces las cadenas se convierten a n�meros y se realiza una
comparaci�n num�rica.

El condicional CMDEXTVERSION funciona solo como ERRORLEVEL, excepto si se
compara con un n�mero de versi�n interna asociada con las extensiones de
comando. La primera versi�n es 1. Ser� incrementada en uno cuando las
significantes mejoras sean agregadas a las extensiones de comando. El
condicional CMDEXTVERSION nunca es verdadero cuando las extensiones de
comando est�n deshabilitadas.

El condicional DEFINED funciona solo como EXIST excepto cuando toma un
nombre de variable de entorno y vuelve como verdadero si se define la
variable de entorno.

%ERRORLEVEL% se expandir� a una representaci�n de cadena del valor actual
de ERRORLEVEL, siempre y cuando no exista ya una variable de entorno con el 
nombre ERRORLEVEL, en cuyo caso obtendr� su valor. 

Despu�s de ejecutar un programa, lo siguiente ilustrar� el uso de ERRORLEVEL

```bat
goto answer%ERRORLEVEL%
:answer0
echo El programa devolvi� el c�digo 0
:answer1
echo El programa devolvi� el c�digo 1
```

Tambi�n puede usar las comparaciones num�ricas anteriores:

```bat    
IF %ERRORLEVEL% LEQ 1 goto okay
```

%CMDCMDLINE% se expandir� a una l�nea de comandos original pasada al anterior
CMD.EXE a cualquier proceso CMD.EXE, siempre y cuando no exista ya una variable de entorno con el nombre CMDCMDLINE, en cuyo caso obtendr� su valor.

%CMDEXTVERSION% se expandir� a una representaci�n de la cadena del valor actual CMDEXTVERSION, siempre y cuando no exista ya una variable de entorno con el nombre CMDEXTVERSION, en cuyo caso obtendr� su valor




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
comando externo a trav�s de la l�nea de comandos o del comando START se
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


### <a href="#prompt"><u>Prompt</u></a>

Cambia el s�mbolo del sistema de cmd.exe.


```
PROMPT [texto]
```


- **texto**: Especifica un nuevo s�mbolo del sistema.


En el s�mbolo del sistema se pueden escribir caracteres normales y los
siguientes c�digos especiales:

- **$A**: & (S�mbolo de uni�n)
- **$B**: | (barra vertical)
- **$C**: ( (Par�ntesis izquierdo)
- **$D**: Fecha actual
- **$E**: <- C�digo de escape (c�digo ASCII 27)
- **$F**: ) (Par�ntesis derecho)
- **$G**: > (signo mayor que)
- **$H**: Retroceso (elimina el car�cter previo)
- **$L**: < (signo menor que)
- **$N**: Unidad actual
- **$P**: Unidad y ruta de acceso actual
- **$Q**: = (signo igual)
- **$S**: (espacio)
- **$T**: Hora actual
- **$V**: Versi�n de Windows
- **$_**: Retorno de carro y alimentaci�n de l�nea
- **$$**: $ (signo del d�lar)

Si las Extensiones de comando est�n habilitadas, el comando PROMPT
admite los siguientes caracteres de formato adicionales:

- **$+**: Cero o m�s caracteres de signo "m�s" (+) en funci�n de la profundidad del directorio de pila PUSHD, un car�cter por cada nivel insertado.
- **$M**: Muestra el nombre remoto asociado a la letra de unidad actual o la cadena vac�a si la unidad actual no es una unidad de red.



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



### <a href="#rmdir"><u>Rd o rmdir</u></a>


Quita (elimina) un directorio.

```
RMDIR [/S] [/Q] [unidad:]ruta
RD [/S] [/Q] [unidad:]ruta
```

- **/S**: Quita todos los directorios y archivos del directorio adem�s del mismo directorio. Se usa principalmente cuando se desea quitar un �rbol.
- **/Q**:  Modo silencioso, no pide confirmaci�n para quitar un �rbol de directorio con /S






Ejecuta el comando para cada uno de los archivos especificados en el conjunto de archivos.

```
FOR %variable IN (conjunto) DO comando [par�metros]
```
  
- **%variable**: Especifica un par�metro reemplazable de una sola letra.
- **(conjunto)**:  Especifica un conjunto de uno o m�s archivos. Se pueden usar comodines.
- **comando**: Especifica el comando que se ejecutar� para cada archivo. 
- **par�metros**: Especifica los par�metros o modificadores del comando especificado.


Para usar el comando FOR en un programa por lotes, especificar %%variable en vez de %variable. Los nombres de las variables distinguen entre may�sculas y min�sculas, por lo tanto %i no es lo mismo que %I.

Si las extensiones de comandos est�n habilitadas, se admiten las siguientes formas adicionales del comando FOR:


```
FOR /D %variable IN (conjunto) comando DO [par�metros]
```

Si el conjunto contiene comodines, se especifica para coincidir con el nombre del directorio en vez de los nombres de archivo.

```
FOR /R [[unidad:]ruta] %variable IN (set) comando DO [par�metros]
```

Gu�a el directorio del �rbol de ra�z a [unidad:]ruta, ejecutando la instrucci�n FOR en cada directorio del �rbol. Si no se especifica el directorio despu�s de /R entonces se asume que es el directorio actual. Si el conjunto es solamente un simple car�cter de punto (.) entonces enumerar� el �rbol del directorio.

```
FOR /L %variable IN (inicio, paso, fin) comando DO [par�metros]
```

El conjunto es una sucesi�n de n�meros que va desde inicio hasta fin y que aumenta (o disminuye) en funci�n de lo especificado en paso. 

As� (1, 1, 5) generar� la sucesi�n: 1 2 3 4 5 y (5, -1, 1) generar� la sucesi�n: 5 4 3 2 1


```
FOR /F ["opciones"] %variable IN (conjunto de archivos) comando DO
[par�metros]
FOR /F ["opciones"] %variable IN ('cadena') comando DO [comando-par�metros]
FOR /F ["opciones"] %variable IN ('comando') comando DO [comando-par�metros]
```

O, si la opci�n usebackq est� presente:


```
FOR /F ["opciones"] %variable IN (conjunto de archivos) comando DO
       [comando-par�metros]
FOR /F ["opciones"] %variable IN ('cadena') comando DO [comando-par�metros]
FOR /F ["opciones"] %variable IN (`comando`) comando DO [comando-par�metros]
```

Conjunto de archivos es uno o m�s nombres de archivos. Cada archivo es abierto, le�do y procesado antes de ir al siguiente archivo del conjunto de archivos. Procesar consiste en leer el archivo, partirlo en l�neas individuales de texto y analizar cada l�nea en cero o m�s tokens. El cuerpo del bucle se llama con los valores de la variable establecidos para las cadenas de token encontradas. De forma predeterminada, /F pasa el primer token separado en blanco desde cada l�nea. Las l�neas en blanco se omiten. Puede invalidar el comportamiento de an�lisis predeterminado si especifica el par�metro opcional "opciones". Esto es una cadena entre comillas que contiene una o m�s palabras claves para especificar diferentes opciones de an�lisis. Las palabras claves son:

- **eol=c**: especifica un car�cter de comentario al final de la l�nea (solo uno)
- **skip=n**: especifica el n�mero de l�neas que hay que saltarse al principio del archivo.
- **delims=xxx**: especifica un grupo de delimitadores. Esto reemplaza al grupo de delimitadores predeterminados de espacio y tabulaci�n.
- **tokens=x,y,m-n**: especifica qu� token de cada l�nea deben pasarse al cuerpo de la cl�usula "for" en cada iteraci�n. Esto causar� que los nombres de variables adicionales sean asignados. La forma m-n es un intervalo del token m-� al token n-�. Si el �ltimo car�cter en la cadena tokens= es un asterisco, se asigna una variable adicional que recibe el resto del texto en la l�nea posterior al �ltimo token analizado. 
- **usebackq**: especifica que la nueva sem�ntica est� vigente, donde una cadena entre comillas inversas se ejecuta como un comando y una cadena con comillas simples es un comando de cadena literal y permite el uso de comillas dobles para entrecomillar los nombres de archivo en un conjunto de archivos.


Estos ejemplos pueden ayudar:

```
FOR /F "eol=; tokens=2,3* delims=, " %i in (archivo.txt) do @echo %i %j %k
```

analizar� cada l�nea en mi archivo.txt excepto las que se inicien con un punto y coma, pasando el segundo y tercer s�mbolo (token) de cada l�nea al cuerpo de FOR. Los s�mbolos est�n delimitados por comas y/o espacios. Tenga en cuenta que las instrucciones del cuerpo de FOR hacen referencia a %i para obtener el segundo s�mbolo, a %j para obtener el tercero y a %k para obtener el resto de los s�mbolos posteriores al tercero. Para los nombres de archivo que contengan espacios, necesita poner comillas dobles en los nombres de archivos. Para usar comillas dobles de esta manera, tambi�n necesita usar la opci�n usebackq; de lo contrario se interpretar� que las comillas dobles est�n definiendo el an�lisis de una cadena literal. %i est� expl�citamente declarado en la instrucci�n FOR y %j y %k est�n declarados impl�citamente a trav�s de la opci�n =tokens. Puede especificar hasta 26 s�mbolos a trav�s de la l�nea tokens=, siempre y cuando no cause un intento de declarar una variable mayor que la letra 'z' o 'Z'. Recuerde, los nombres de variables de FOR son de una sola letra y distinguen may�sculas de min�sculas. Adem�s, las variables son globales y no puede haber m�s de 52 variables activas al mismo tiempo.

Tambi�n puede usar la l�gica de an�lisis de FOR /F en una cadena inmediata convirtiendo el conjunto de archivos entre par�ntesis en una cadena entre comillas simples. Ser� tratada y analizada como una sola l�nea de entrada de un archivo. Finalmente, puede usar el comando FOR /F para analizar la salida de un comando. Se hace convirtiendo el conjunto de archivos entre par�ntesis una cadena con comillas invertidas. Se tratar� como una l�nea de comandos que se pasa a un CMD.EXE secundario y la salida se captura en memoria y se eval�a como si fuera un archivo. Como en el siguiente ejemplo:

```
FOR /F "usebackq delims==" %i IN (`conjunto`) DO @echo %i
```

enumerar� los nombres de variable de entorno en el entorno actual. Adem�s, la sustituci�n de las referencias de variables FOR ha sido mejorada. Ahora puede usar la siguiente sintaxis opcional:


- **%~I**: expande %I quitando las comillas (") que pudiera haber
- **%~fI**: expande %I a un nombre de ruta calificado
- **%~dI**: expande %I solo a una letra de unidad
- **%~pI**: expande %I solo a una ruta
- **%~nI**: expande %I solo a un nombre de archivo
- **%~xI**: expande %I solo a una extensi�n de archivo
- **%~sI**: ruta expandida contiene solo nombres cortos
- **%~aI**: expande %I a atributos de archivos
- **%~tI**: expande %I a fecha/hora del archivo
- **%~zI**: expande %I a tama�o del archivo
- **%\~$PATH:I**: busca los directorios de la lista de la variablende entorno de PATH y expande %I al nombre totalmente calificado del primero que se encuentre. Si el nombre de la variable de entorno no es definido o no se encuentra el archivo en la b�squeda, el modificador se expande a la cadena vac�a


Los modificadores se pueden combinar para conseguir resultados compuestos:


- **%~dpI**: expande %I solo a una letra de unidad y ruta
- **%~nxI**: expande %I solo a un nombre de archivo y extensi�n
- **%~fsI**: expande %I solo a un nombre de ruta con nombres cortos
- **%~dp$PATH:i**: busca los directorios de la lista de la variable de entorno de PATH para %I y se expande a la letra de unidad y ruta del primero que encuentre.
- **%\~ftzaI**: expande %I a DIR como l�nea de salida.S

En los ejemplos anteriores %I y PATH pueden ser reemplazados por otros valores v�lidos. La sintaxis %~ est� terminada por un nombre de variablem FOR v�lido. El c�digo se vuelve m�s legible si se usan variables en may�scula como %I, adem�s esto evita confundir las variables con los modificadores, los cuales no distinguen entre may�sculas y min�sculas.
Muestra o modifica la comprobaci�n del disco en el tiempo de arranque.


