<h2 align="center">SQLCMD SQL SERVER</h2>  

<b>SQLCMD</b> es una utilidad para el manejo de bases de datos relacionales (SGBD) basado en el lenguaje <b title="Transact-SQL">T-SQL</b> mediante la línea de comandos utilizando la línea de comandos o <b title="Command Prompt">CMD</b> podemos hacer uso de esta utilidad para:  

- Mandar instrucciones T-SQL a la base de datos SQL Server. 
- Crear scripts y procedimiento. 

**Conexión dedicada de Administración**  

<b>SQLCMD</b> también es uno de los últimos recursos cuando el sistema falla (Por ejemplo cuando la base de datos principal del sistema llamada master se corrompe). Cuando se cuelgue el sistema o que no este diponible. La conexión dedicada de administración (DAC en inglés) es uno de los recursos. <b>SQLCMD</b> permite una conexión dedicada de administración utilizando el parámetro <b>-A</b> como sigue:  

```bash
sqlcmd -A
```

<b>SQLCMD</b> utiliza  el <b>OLE-DB</b> para su conexión con la base de datos. Las herramientas visuales de SQL Server como("Managment Studio", "Azure Data Studio") utiliza sqlclient para sus conexiones.  

<b>SQLCMD</b> surge como herramienta para ejecutar sentencias en T-SQL en SQLServer 2005 también incorporada en SQLServer 2008. Su antecesor es <b>Ojal</b> de la versión SQLSeerver 2000.  

<b>SQLCMD</b> puede ser utilizado como un lenguaje de programación, el paso de datos dinámicamente está permitido al igual que la interacción con scripts generados en archivos <b>.sql</b>


## Opciones de sqlcmd:

- **opción del servidor <b>(-S)</b>: Que identifica la instancia de MSSQLServer a la que se conecta <b>SQLCMD</b> 


## ¿Cuándo utilizar sqlcmd??

Después de ver las capacidades de SQLCMD seguro que tienes muchas ideas en mente, y si no, también puedes revisar alternativas de uso de SQLCMD.

Si bien las opciones son muchas, uno de los factores que puede influir en decidir usar tareas programadas con SQLCMD, es el no poder utilizar SQL Server Agent. El motivo más común, alcances del licenciamiento de SQL Server en su edición Express. Es importante que conozcas las ediciones y características soportadas de cada una de ellas.  

## ¿Y cómo programas una tarea sin SQL Server Agent?

Nos apoyaremos con Task Scheduler de Windows. Ingenioso. 

Si esa es su función: Programar una acción y asignar una hora de ejecución o repetir la tarea. (Exactamente lo mismo que hace el servicio del Agent). Entonces, ¿por qué no programar una acción de SQL Server?


### ¿Qué necesitas para hacer tareas programadas con SQLCMD?

Simple. Una acción sobre SQL Server y un disparador de esa acción.

Lo puedes resumir en dos archivos.

- 1 archivo .sql que realiza una acción en SQL Server
- 1 archivo .bat que será disparado por el Task Scheduler 


**ARCHIVO .sql**  

Contiene la acción que quieres realizar en SQL Server. ¿Qué tal la ejecución de backup?

Voy a hacer algo muy estándar sobre una base de datos; sin mucha configuración adicional.

```sql
BACKUP DATABASE [WideWorldImporters] 
TO DISK = N'C:\BACKUPS\WideWorldImporters-Full.bak' 
WITH NOFORMAT, NOINIT,  
NAME = N'WideWorldImporters-Full Database Backup', 
SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO
```

Este código lo guarda en un archivo llamado BKP_WWI.sql

**ARCHIVO .bat**  

Simplemente realiza un llamado a la acción del primer archivo con la ayuda de SQLCMD.


```bat
sqlcmd -S.\SQL19 -iC:\DEMOS\Scheduler\BKP_WWI.sql
```

Fíjate bien que no está explícito un usuario y un password de conexión a la base de datos. Esto significa que se utilizará el usuario de Windows (o del dominio) con el que se está configurando la tarea.

Si quieres utilizar un usuario local de SQL, solamente deben adicionar los parámetros correspondientes a usuario y password. 

```bat
sqlcmd -S.\SQL19 -UNombreUsuario -PPassword -iC:\DEMOS\Scheduler\BKP_WWI.sql 
```

Este código lo guardo en un archivo llamado Call_BKP_WWI.bat

## Consideraciones importantes en las tareas programadas con SQLCMD

- Tener claros los permisos que requieres tanto a nivel de Sistema Operativo como en SQL Server.  

- Los accesos a las carpetas utilizadas también deben estar claros.  
- Por cualquier problema que tengas, puedes acudir al Event Viewer, al Log de SQL Server o incluso adicionar el parámetro output (-o) a sqlcmd para generar un archivo de salida.  
- Si vas a utilizar un usuario local de SQL Server en el archivo bat, ten en cuenta que debes proteger las credenciales que se encuentran ahí. Lo mejor sería que pienses en utilizar una cuenta de Windows o de Dominio.

