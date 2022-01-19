

````mysql.ini
[mysqld]
# set basedir to your installation path
basedir=E:/mysql
# set datadir to the location of your data directory
datadir=E:/mydata/data
```

Los nombres de las rutas de acceso de Microsoft Windows se especifican en los archivos de opciones mediante barras diagonales (hacia adelante) en lugar de barras diagonales inversas. Si usa barras invertidas, duplíquelas:


```mysql
[mysqld]
# set basedir to your installation path
basedir=E:\\mysql
# set datadir to the location of your data directory
datadir=E:\\mydata\\data
```

El archivo ZIP no incluye un directorio **data**. Para inicializar una instalación de MySQL creando el directorio de datos y llenando las tablas en la base de datos del sistema mysql, inicialice MySQL usando --initialize o --initialize-insecure. 

Si desea utilizar un directorio de datos en una ubicación diferente, debe copiar todo el contenido del directorio data en la nueva ubicación. Por ejemplo, si desea utilizarlo E:\mydatacomo directorio de datos, debe hacer dos cosas:

1. Mueva todo el directorio data y todo su contenido desde la ubicación predeterminada (por ejemplo C:\Program Files\MySQL\MySQL Server 8.0\data), a E:\mydata.

2. Utilice una opción --datadir para especificar la nueva ubicación del directorio de datos cada vez que inicie el servidor.



Instalar como un servicio

```py
mysqld --install "MySQL8"
```

Iniciar el servicio con el comando net

```
net start MySQL8
```

Detener el servicio con el comando:

```
net stop MySQL8
```
