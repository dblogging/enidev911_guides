[comment]: <> (Author: Marco Contreras Herrera)
[comment]: <> (Email: enidev911@gmail.com)

<h2 align="center">
  <u>Optimizar el servidor MySQL</u>
  <img src="../../../../assets/ico/MySQL_Logo.ico">
</h2>

<br><br>

**¿Para qué queremos optimizar un servidor MySQL?**

- Servir las peticiones más rápido, usando menos recuros de CPU, RAM e I/O de disco.

- Aprovechar mejor los recursos del sistema para garantizar una mejor estabilidad y una mayor velocidad de respuesta al acceder a datos almacenados en las bases de datos.

#### Archivo my.cnf

El 99% de las configuraciones del servidor MySQL se realizan desde un único archivo.


#### Parámetros de optimización de MySQL


- **query_cache_type**: Sirve para activar o desactivar cache, si ponemos el valor de 0 desactivamos el cache de consultas de MySQL, si ponemos el valor de 1 activamos el cache de consultas y si ponemos 2 se activará bajo petición. (Lo recomendable es 1.)

- **max_allowed_packet**: Este parámetro especifica el tamaño máximo de un paquete a la hora de que el servidor MySQL trabaje con él. Este parámetro normalmente lo tenemos que aumentar para importar bases de datos o mover grandes volúmenes de datos en una base de datos.

- **query_cache_size**: Este parámetro especifica el tamaño del cache de consultas, este cache se guarda en RAM y se suele poner 64 MB de RAM por cada 1 GB de memoria física usable que tenga el servidor.

- **key_buffer_size**: Este parámetro especifica el tamaño del cache de los índices, cuanto más grande sea este cache, más rápido se ejecutarán los comandos SQL y más rápido se obtendrá una respuesta del servidor MySQL. Normalmente se configuran 32MB por cada 1GB de memoria física usable. 

- **table_cache**: Especifica el máximo de tablas abiertas entre todos los threads o hilos de ejecución de MySQL, un buen valor es 64, aunque con MySQLTuner podremos ver si necesitamos más o menos número de tablas abiertas.

- **sort_buffer_size**: Con este parámetro configuramos el tamaño del cache de búsquedas de MySQL, lo recomendable es configurar 1MB por cada 1GB de memoría RAM física disponible.

- **read_buffer_size**: Con este parámetro configuramos el tamaño del cache de lecturas de MySQL, lo recomendable es configurar 1MB por cada 1GB de memoria RAM física disponible.

- **read_rnd_buffer_size**: Con este parámetro configuramos el tamaño del cache de lecturas usado tras una acción de búsqueda u ordenado, lo recomendable es configurar 1MB por cada 1GB de memoria RAM física disponible.

- **join_buffer_size**: Con este parámetro configuramos el tamaño del cache de JOIN sin índices, lo recomendable es configurar 1MB por cada 1GB de memoria RAM física disponible.

- **thread_cache_size**: Es el número máximo de hilos de ejecución que se pueden cachear y rehusar, se suelen configurar entre 32 y 64 para un uso normal.

- **tmp_table_size**: Esta variable especifica el tamaño máximo de una tabla temporal en RAM, cuando se alcanza el tamaño máximo especificado en este parámetro la tabla pasa a ser una tabla temporal en MyISAM.

- **max_connections**: Especifica el número máximo de conexiones totales que puede aceptar el servidor MySQL al mismo tiempo.

- **wait_timeout**: Es el tiempo de espera que tarda MySQL en cerrar una conexión.

- **thread_concurrency**: Especifica el número máximo de hijos de ejecución o procesos abiertos de MySQL, lo recomendable es configurar 2 por cada 1 núcleo de CPU disponible.

- **query_cache_limit**: Especifica un límite de tamaño de consulta a partir del cual no se cachearán, el valor por defecto es 1 MB. Si el límite es muy alto podemos llegar a saturar el servidor MySQL.

- **innodb_buffer_pool_size**: Es una variable que solo afecta a innoDB, pero que mejora bastante el rendimiento general de las tablas almacenadas en InnoDB. Un buen valor de configuración sería un valor similar al 70 u 80% de la memoria RAM disponible, pero depende también del tamaño de la base de datos, si trabajamos con bases de datos muy pequeñas no tiene sentido especificar un valor tan grande.

