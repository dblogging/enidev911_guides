**mysqladmin** es un cliente para realizar operaciones administrativas. Puede usarlo para verificar la configuración y el estado actual del servidor, para crear y eliminar bases de datos, y más.


Invoque mysqladmin así:
```
mysqladmin [options] command [command-arg] [command [command-arg]] 
```

mysqladmin admite los siguientes comandos. Algunos de los comandos toman un argumento después del nombre del comando.


---


- **create db_name**

Cree una nueva base de datos llamada db_name.

- **debug**

Antes de MySQL 8.0.20, dígale al servidor que escriba información de depuración en el registro de errores. El usuario conectado debe tener privilegios administrativos. El formato y el contenido de esta información están sujetos a cambios.

Esto incluye información sobre el programador de eventos.

- **drop db_name**

Elimine la base de datos nombrada db_name y todas sus tablas.

- **extended-status**

Muestra las variables de estado del servidor y sus valores.

- **flush-hosts**

Vacíe toda la información en el caché del host. Consulte la Sección 5.1.12.3, “Búsquedas de DNS y caché del host” .

- **flush-logs [log_type ...]**

Vacíe todos los registros.


- **flush-threads**

Vacíe el caché de subprocesos.  

- **password new_password**

Establecer una nueva contraseña. Esto cambia la contraseña por new_password a la cuenta que usa con mysqladmin para conectarse al servidor. Por lo tanto, la próxima vez que invoque mysqladmin (o cualquier otro programa cliente) usando la misma cuenta, debe especificar la nueva contraseña.



>Advertencia: <br>
Establecer una contraseña usando mysqladmin debe considerarse inseguro . En algunos sistemas, su contraseña se vuelve visible para los programas de estado del sistema, como ps , que pueden ser invocados por otros usuarios para mostrar líneas de comando. Los clientes de MySQL suelen sobrescribir el argumento de la contraseña de la línea de comandos con ceros durante su secuencia de inicialización. Sin embargo, todavía hay un breve intervalo durante el cual el valor es visible. Además, en algunos sistemas, esta estrategia de sobrescritura es ineficaz y la contraseña permanece visible para ps.. (Los sistemas SystemV Unix y quizás otros están sujetos a este problema).


Si el valor de new_password contiene espacios u otros caracteres que son especiales para su intérprete de comandos, debe encerrarlo entre comillas. En Windows, asegúrese de utilizar comillas dobles en lugar de comillas simples; las comillas simples no se eliminan de la contraseña, sino que se interpretan como parte de la contraseña. Por ejemplo:


```
mysqladmin password "my new password"
```

- **ping**

Compruebe si el servidor está disponible. El estado de retorno de mysqladmin es 0 si el servidor se está ejecutando, 1 si no lo está. Esto es 0 incluso en caso de un error como **Access denied**, porque esto significa que el servidor se está ejecutando pero rechazó la conexión, que es diferente a que el servidor no se esté ejecutando.

- **processlist**

Muestra una lista de subprocesos de servidor activos. Esto es como la salida de la declaración **`SHOW PROCESSLIST`**. Si da la opción **`--verbosese`**, la salida es como la de **`SHOW FULL PROCESSLIST`**.

- **reload**  

Vuelve a cargar las tablas de concesión.

- **refresh**

Vaciar todas las tablas y cerrar y abrir archivos de registro.

- **shutdown**

Detenga el servidor.

- **status**

Muestra un breve mensaje de estado del servidor.


- **--plugin-dir=dir_name**

El directorio en el que buscar complementos. Especifique esta opción si la opción **`--default-auth`** se usa para especificar un complemento de autenticación pero mysqladmin no lo encuentra.



