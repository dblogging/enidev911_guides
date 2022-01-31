[comment]: <> (Author: Marco Contreras Herrera)
[comment]: <> (Email: enidev911@gmail.com)

<h2 align="center">
  <u>mysql: el cliente de línea de comandos de MySQL</u>
  <img src="../../../../assets/ico/MySQL_Logo.ico">
</h2>


**mysql** es un simple shell para ejecutar SQL con capacidades de edición. Es compatible con el uso interactivo y no interactivo. Cuando se usa de forma interactiva, los resultados de la consulta se presentan en un formato de tabla ASCII. Cuando se usa de forma no interactiva (por ejemplo, como filtro), el resultado se presenta en formato separado por tabuladores. El formato de salida se puede cambiar usando las opciones de comando.


**mysql** envía cada instrucción SQL que emite al servidor para que se ejecute. También hay un conjunto de comandos que **mysql** interpreta. Para obtener una lista escriba help en el prompt.  


Lista de los comandos del cliente:  

```sql
mysql> help

Lista de todos los comandos de MySQL:  
Tenga en cuenta que todos los comandos de texto deben estar al principio de la línea y terminar con ';'

?         (\?) Sinónimo del comando `help`
clear     (\c) Borra la instrucción de entrada actual.
connect   (\r) Vuelve a conectarse al servidor, Los argumentos opcionales son db y host.
delimiter (\d) Establecer delimitador de declaración.
edit      (\e) Editar el comando con $EDITOR. (no funciona en la versión 8)
ego       (\G) Envía el comando al servidor mysql, muestra el resultado verticalmente.
exit      (\q) Salir de mysql. Lo mismo que `quit`.
go        (\g) Envía el comando mysql server.
help      (\h) Muestra esta ayuda.
nopager   (\n) Deshabilitar paginación de salida. (El comando solo funciona en Unix.)
source    (\.) Ejecuta un archivo de script SQL. Toma un nombre de archivo como argumento.
status    (\s) Obtener información de estado del servidor.
system    (\!) Ejecute un comando, el comando solo funciona en Unix. 
               (desde 8.0.19,funciona en Windows.)
warnings  (\W) Mostrar advertencias después de cada declaración.
nowarning (\w) No mostrar advertencias después de cada declaración.

charset   (\C) Cambiar a otro conjunto de caracteres. Podría ser necesario para el procesamiento
               con juegos de caracteres multi-bytes.

Para obtener ayuda del lado del servidor, escriba `help contents`
```

