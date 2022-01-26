[comment]: <> (Author: Marco Contreras Herrera)
[comment]: <> (Email: enidev911@gmail.com)

<h2 align="center">
  <u>Instalación de MySQL en Ubuntu</u>
  <img src="../../../../assets/ico/MySQL_Logo.ico">
  <img src="../../../../assets/ico/ubuntu_gr.ico" width="48">
</h2>

<br>

**1. Actualizar el índice de paquetes apt con el siguiente comando:**  

```bash
sudo apt update
```


**2. Instalar el paquete de MySQL con el comando:**  

```bash
sudo apt install mysql-server
```

**3. Concluida la instalación, el demonio de MySQL se iniciará automáticamente. Para verificar si esta ejecutandose el servidor usamos el comando:**  

```bash
sudo systemctl status mysql

# output ============================================================================
#● mysql.service - MySQL Community Server
#   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
#   Active: active (running) since Wed 2018-06-20 11:30:23 PDT; 5min ago
# Main PID: 17382 (mysqld)
#    Tasks: 27 (limit: 2321)
#   CGroup: /system.slice/mysql.service
#           `-17382 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
```


**4. Utilizar el script para una configuración segura con el comando:**  

```bash
sudo mysql_secure_installation
```


La primera pregunta nos solicitará si queremos validar que nuestro password para conectarnos al servidor sea seguro, si lo deseamos al momento de crear nuestro password MySQL nos validará si cumple con las condiciones mínimas de seguridad. Si no queremos esto solamente ingresamos **`N`**


```
Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y
```

Luego de acuerdo a la opción que ingresemos nos solicitará ingresar el password para el usuario root:

```bash
New password: 

Re-enter new password: 
```

Una vez ingresamos nuestro password, nos preguntará si deseamos remover a los usuarios ánonimos que se crean por defecto junto a la instalación de MySQL, lo mejor es removerlos.  

```bash
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : Y
```

Normalmente, a root solo se le debe permitir conectarse desde 'localhost'. Para así asegurar que no puedan adivinar la password de root desde la red. Así que deshabilitamos el logín remoto.  

```bash
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : Y 
```

Luego nos preguntá si queremos eliminar la base de datos de prueba, esto es opcional. 

```bash
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : Y
```
Luego nos pregunta si queremos recargar la tabla de privilegios. Pondremos si (Y).  

```bash
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
```


<h2 align="center">
  <u>Ajustes de autenticación y privilegios de usuario</u>
  <img src="../../../../assets/ico/MySQL_Logo.ico">
  <img src="../../../../assets/ico/database_administrators_group(48).ico">
</h2>

<br>

En los sistemas Ubuntu con MySQL 5.7 (y versiones posteriores), el usuario **root** de MySQL se configura para la autenticación usando el complemento **auth_socket** de manera predeterminada en lugar de una contraseña. Esto en muchos casos proporciona mayor seguridad y utilidad, pero también puede generar complicaciones cuando deba permitir que un programa externo (como phpMyAdmin) acceda al usuario.  

Para usar un password para conectar a MySQL como **root**, deberemos cambiar el método de autenticación de **auth_socket** a otro complemento, como **caching_sha2_password** o **mysql_native_password**. Para hacer esto, abra la consola de MySQL desde su terminal:

```bash
sudo mysql
```

Para ver el método de autenticación utilizado por las cuentas de usuarios de MySQL ejecutamos la siguiente sentencia dentro de la consola de MySQL:  

```bash
# shell mysql
SELECT user, authentication_string, plugin, host FROM mysql.user;

Output
+------------------+------------------------------------------------------------------------+-----------------------+-----------+
| user             | authentication_string                                                  | plugin                | host      |
+------------------+------------------------------------------------------------------------+-----------------------+-----------+
| debian-sys-maint | $A$005$lS|M#3K #XslZ.xXUq.crEqTjMvhgOIX7B/zki5DeLA3JB9nh0KwENtwQ4 | caching_sha2_password | localhost |
| mysql.infoschema | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| mysql.session    | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| mysql.sys        | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| root             |                                                                        | auth_socket           | localhost |
+------------------+------------------------------------------------------------------------+-----------------------+-----------+
5 rows in set (0.00 sec)
```

Para configurar la cuenta **root** para autenticar con una password, ejecute una instrucción **ALTER USER** para cambiar qué complemento de autenticación utiliza y establecer una nueva password.  

Cambiamos por un password seguro,la siguiente instrucción cambiará el password de **root**:  

```bash
# Shell de mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'password';
```

Recarga la tabla de permisos:  

```bash
# Shell de mysql
FLUSH PRIVILEGES;
```

Otra opción recomendada es crear un nuevo usuario administrativo con todos los privilegios y acceso a todas las bases de datos:

```bash
# Shell de mysql
GRANT ALL PRIVILEGES ON *.* TO 'admin_user'@'localhost' IDENTIFIED BY 'very_strong_password';
```


**Finalización**

Ahora que su servidor MySQL está en funcionamiento y sabe cómo conectarse al servidor MySQL desde la línea de comandos, es posible que desee consultar las siguientes guías:

- [Administrar cuentas de usuarios](https://github.com/EniDev911/enidev911_guides/tree/main/devs/database/mysql/manager_users_privileges)
