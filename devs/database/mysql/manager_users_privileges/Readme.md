# manager\_users\_privileges

### Administrar usuarios - ![](../../../../assets/ico/database\_administrators\_group\(48\).ico)

\


Para crear cuentas de usuario en **MySQL** se necesita tener permisos administrativos.

Por medio del comando **`CREATE USER`** podemos crear y configurar un usuario de bases de datos, que es una cuenta a través de la cual puede iniciar sesión y se le puede asignar una contraseña por medio de la cláusula **`IDENTIFIED BY`**, si desea que la contraseña se guarde en texto plano, la contraseña se guardará cifrada con el valor hash que es devuelto por la función **Password()**

**Ejemplo:**

```sql
CREATE USER 'user'@'server' IDENTIFIED BY 'passworduser';
```

![](img/01\_create\_user.png)

El usuario ha sido creado, sin embargo puede conectarse al servidor pero hace falta asignarle los diferentes privilegios, para que pueda realizar cualquier tipo de tarea.

***

### Privilegios de usuarios

\


Para ver una lista de todos los privilegios que pueden ser asignado a una cuenta, se utiliza el siguiente comando:

```sql
SHOW PRIVILEGES;
```

Para ver los privilegios asignados al usuario conectado con el comando:

```sql
SHOW GRANTS;
```

Para consultar los privilegios que tiene otro usuario con el siguiente comando (debe poseer permisos para realizar este comando):

```sql
SHOW GRANTS FOR user;
```

![](img/02\_show\_privileges.png)

*   **Asignar privilegios a un usuarios:**\
    Para asignar privilegios a una cuenta usamos el comando **`GRANT`**, el cual permite asignar a una cuenta diferentes servicios, siendo de tipo:

    * **Globales:** otorga los privilegios a un usuario sobre todo el servidor, esto se realiza por medio de la sentencia:

    ```sql
    GRANT privileges ON *-* TO 'username';
    ```

    Si queremos que el nuevo usuario tenga permisos de administrador (todos los permisos), debemos de ejecutar la siguiente sentencia:

    ```sql
    GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
    ```

    Los asteriscos indican que los permisos serán asignados a todas las bases de datos y a todas las tablas (primer asteriscos bases de datos, segundo asterisco tablas).

    ![](img/03\_assign\_privileges.png)

    Si queremos asignar permisos para ciertas acciones, la sentencia quedaría de la siguiente manera. Reemplazamos ALL PRIVILEGES y colocamos las acciones que queremos asignar.

    ```sql
    mysql>GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP
        -> ON userdb.*
        -> TO 'username'@'localhost';
    ```

    Una vez hayamos finalizado con los permisos, el último paso será refrescarlos.

    ```sql
    mysql>FLUSH PRIVILEGES;
    ```
*   **Revocar privilegios a un usuarios:**

    Para borrar los privilegios de una cuenta con la sentencia:

    ```sql
    REVOKE privileges ON*-*TO 'username';
    ```

    Remover permisos en concreto (Ejemplo create y delete):

    ```sql
    REVOKE CREATE, DELETE ON *.* FROM 'username'@'localhost';
    ```

    Remover todos los privilegios:

    ```sql
    REVOKE ALL PRIVILEGES ON *.* FROM 'username'@'localhost';
    ```

![](img/04\_revoke\_privileges.png)

*   **Borrar usuarios:**

    De igual forma para crear usuarios, necesitamos tener los permisos pertinentes para poder borrarlos. Para borrar a un usuario utilzamos la sentencia **DROP USER**:

    ```sql
    mysql>DROP USER user;
    ```

![](img/05\_delete\_user.png)

### Tipos de autenticaciones ![](../../../../assets/ico/database\_administrators\_group\(48\).ico)

\


MySQL incluye el complemento **mysql\_native\_password** que implementa la autenticación nativa; es decir; autenticación basada en el método de hash.

**Nombres de complementos y bibliotecas para autenticación de contraseña nativa.**

|       Complemento o archivo       | Complemento o nombre de archivo             |
| :-------------------------------: | ------------------------------------------- |
| Complemento del lado del servidor | mysql\_native\_password                     |
|  Complemento del lado del cliente | mysql\_native\_password                     |
|             Biblioteca            | Ninguno (los complementos están integrados) |

* El complemento del lado sel servidor está integrado en el servidor, no es necesario cargarlo explícitamente y no se puede deshabilitar descargándolo.
* El complemento del lado del cliente está integrado en la biblioteca `libmysqlclient` y está disponible para cualquier programa vinculado a libmysqlclient.

En el caso de usar el complemento auth\_socket, este autentica a los clientes que se conectan desde el localhost a través del archivo de socket Unix. Este complemento auth\_socket verifica si el nombre de usuario del socket coincide con el nombre de usuario MySQL del programa cliente con el servidor.
