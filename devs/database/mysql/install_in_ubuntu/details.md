#### - ¿Dónde está instalado MySQL en Ubuntu?

Generalmente, cada distribución tiene su propia forma de desempacar cada programa que instalamos. Sin embargo, Linux tiene alguna convenciones.  

Normalmente, los binaries de MySQL, una vez instalados, son almacenados en la siguiente ubicación:

```
/usr/bin
```

**Finalización**

Ahora que su servidor MySQL está en funcionamiento y sabe cómo conectarse al servidor MySQL desde la línea de comandos, es posible que desee consultar las siguientes guías:

- [Administrar cuentas de usuarios](https://github.com/EniDev911/enidev911_guides/tree/main/devs/database/mysql/manager_users_privileges)


#### - ¿Dónde se almacenan los datos?


El lugar suele ser: var/lib/mysql



Cambiar el directorio donde están los archivos de bases de datos en MySQL – Ubuntu

En una ocasión tuve la necesidad de cambiar el directorio por defecto en donde se guardan los archivos de bases de datos en MySQL, el cual están **var/lib/mysql**. Es muy puntual, pero es muy útil conocer éste dato. 

Para hacerlo, primero debemos detener el servidor.

```bash
sudo service mysql stop
```

Copiamos los archivos de las bases de datos a la nueva ubicación:


```bash
sudo cp -R -p /var/lib/mysql /new/location/
```

>El **-p** es importante porque debemos llevarnos íntegramente la configuración de seguridad, propiedad, etc.

Ahora entramos al archivo de configuración de MySQL.

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Buscamos dentro del archivo mysqld.cnf el parámetro datadir y lo cambiamos por la nueva ruta… así:

```
[mysqld]
datadir = /new/location/mysql
```

Ahora, aquí viene el secreto… debemos cambiar el perfil de seguridad de MySQL mediante AppArmor, modificando la nueva ruta.

```bash
sudo nano /etc/apparmor.d/usr.sbin.mysqld
```

Buscamos los directorios /var/lib/mysql/ y solo hacemos la modificación de la ruta, respetando lo demás; yo generalmente lo pongo como comentario a las líneas originales y agrego las líneas que sean necesarias… quedaría algo así:


```
# Allow data dir access
#  /var/lib/mysql/ r,
#  /var/lib/mysql/** rwk,
  /nueva/ubicacion/mysql/ r,
  /nueva/ubicacion/mysql/** rwk,
```

Ahora recargamos la configuración mediante el servicio AppArmor y luego reiniciamos el servicio MySQL.

```bash
sudo service apparmor reload
sudo service mysql start
```