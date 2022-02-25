# install\_in\_ubuntu

### Instalación de MySQL en Ubuntu ![](../../../../assets/ico/MySQL\_Logo.ico) ![](../../../../assets/ico/ubuntu\_gr.ico)

\


**- Actualizar el índice de paquetes apt con el siguiente comando:**

```bash
sudo apt update
```

**- Instalar el paquete de MySQL con el comando:**

```bash
sudo apt install mysql-server
```

![](../assets/png/ub/step1\_mysql.png)

**- Concluida la instalación, el demonio de MySQL se iniciará automáticamente. Para verificar si esta ejecutandose el servidor usamos el comando:**

```bash
sudo systemctl status mysql
```

![](../assets/png/ub/status\_mysql.png)

**- Ver en que puerto está abierto**

```bash
cat /etc/services | grep mysql
```

En Debian y derivados, el paquete mysql-server incluye el script Perl **mysql\_secure\_installation**, el cual permite mejorar la seguridad de la instalación por defecto. Es recomendable correr este script en todas las instalaciones de servidores MySQL para sistemas en producción. En resumen nos permite:

* Cambiar la contraseña del usuario "root".
* Deshabilitar el acceso remoto para el usuario "root".
* Eliminar cuentas de usuario anónimas que pueden ingresar sin necesidad de una contraseña.
* Eliminar la base de datos "test" (si existe), y todo privilegio que permita a cualquier usuario el acceso a bases de datos cuyos nombres comienzan con "test\_".

**- Utilizar el script para una configuración segura:**

```bash
sudo mysql_secure_installation
```

La primera pregunta nos solicitará si queremos validar password para conectarnos al servidor sea seguro, si lo deseamos al momento de crear un nuevo usuario en el sistema MySQL nos validará si el password cumple con las condiciones mínimas de seguridad. Si no queremos esto solamente ingresamos **`N`**

![](../assets/png/ub/step1\_mysql\_secure\_install.png)

Luego de acuerdo a la opción que ingresemos nos solicitará ingresar el password para el usuario root (Ojo: esto no tendrá efecto hasta que cambiemos el método de autenticación al usuario root de **auth\_socket** a otro complemento). Una vez ingresamos nuestro password, nos preguntará si deseamos remover a los usuarios ánonimos que se crean por defecto junto a la instalación de MySQL, lo mejor es removerlos.

![](../assets/png/ub/step2\_mysql\_secure\_install.png)

Normalmente, a root solo se le debe permitir conectarse desde 'localhost'. Para así asegurar que no puedan adivinar la password de root desde la red. Así que deshabilitamos el logín remoto.

![](../assets/png/ub/step3\_mysql\_secure\_install.png)

Luego nos preguntá si queremos eliminar la base de datos de prueba, esto es opcional.

![](../assets/png/ub/step4\_mysql\_secure\_install.png)

Luego nos pregunta si queremos recargar la tabla de privilegios. Pondremos si (Y).

![](../assets/png/ub/step5\_mysql\_secure\_install.png)

### Ajustes de autenticación y privilegios de usuario ![](../../../../assets/ico/MySQL\_Logo.ico) ![](../../../../assets/ico/database\_administrators\_group\(48\).ico)

\


En los sistemas Ubuntu con MySQL 5.7 (y versiones posteriores), el usuario **root** de MySQL se configura para la autenticación usando el complemento **auth\_socket** de manera predeterminada en lugar de una contraseña. Esto en muchos casos proporciona mayor seguridad y utilidad, pero también puede generar complicaciones cuando deba permitir que un programa externo (como phpMyAdmin) acceda al usuario.

Para usar un password para conectar a MySQL como **root**, deberemos cambiar el método de autenticación de **auth\_socket** a otro complemento, como **caching\_sha2\_password** o **mysql\_native\_password**. Para hacer esto, abra la consola de MySQL desde su terminal:

```bash
sudo mysql
```

Para ver el método de autenticación utilizado por las cuentas de usuarios de MySQL ejecutamos la siguiente sentencia dentro de la consola de MySQL:

```bash
SELECT user, authentication_string, plugin, host FROM mysql.user;
```

![](../assets/png/ub/auth\_user.png)

Para cambiar el método de autenticación de **root** con una password, utilizaremos el comando **ALTER USER** para cambiar el complemento de autenticación. Lo podriamos hacer todo en una sola línea como lo siguiente:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'password';
```

O realizar el cambio en dos pasos:

1. Cambiamos solo el complemento.

```sql
  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password;
```

1. Cambiamos el password. (La función **`user()`** devuelve al usuario en sessión)

```sql
  ALTER USER user() IDENTIFIED BY 'Strong_Password;
```

Y por último recargamos la tabla de permisos:

```sql
FLUSH PRIVILEGES;
```

Otra opción recomendada es crear un nuevo usuario administrativo con todos los privilegios y acceso a todas las bases de datos:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'admin_user'@'localhost' IDENTIFIED BY 'very_strong_password';
```

Para desinstalar MySQL con:

```bash
sudo apt-get remove --purge mysql-server mysql-client mysql-common
```
