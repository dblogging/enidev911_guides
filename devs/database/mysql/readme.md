# mysql

### MySQL resumen ![](../../../assets/ico/MySQL\_Logo.ico)

\


MySQL es un sistema open source de administración de bases de datos que actualmente es desarrollado y soportado por Oracle.

Una base de datos es una colección estructurada de datos que está organizada para ser usada y extraída de forma sencilla.

MySQL fue lanzado en 1995. Desde entonces, ha pasado por varios cambios. A pesar de que Oracle está a cargo ahora, MySQL sigue siendo un **software open source**, lo que quiere decir que puede ser usado y modificado por cualquier persona.

Para entender un poco el funcionamiento de MySQL, es importante conocer dos conceptos que van conectados.

* \[Bases de datos relacionales]
* \[Modelo de Cliente-Servidor]

### Bases de datos relacionales  

![](../../../assets/png/relationship\_database.png)

Cuando se trata de almacenar datos en una base de datos, hay distintos enfoques que se pueden utilizar.

MySQL opta por un enfoque basado en el modelo o esquema relacional. Con una base de datos relacional, sus datos son fragmentados en varias áreas de almacenamiento separadas las denominadas **tablas** en lugar de poner todo junto en una gran unidad de almacenamiento.

Por ejemplo, quisiera almacenar dos tipos de información:

* **Pedidos**: Nos interesa el producto, el precio, quién hizo la orden, etc.
* **Cliente**: Su nombre, dirección, detalles, etc.

Si intenta poner todos estos datos juntos en un gran almacen, tendrá algunos problemas como:

* **Datos distintos**: Los datos que usted necesita para recolectar para una orden son diferentes que lo que son para un cliente.
* **Datos duplicados**: Cada cliente tiene un nombre, y cada orden también tiene el nombre del cliente. Es algo poco eficiente lidiar con datos repetidos.
* **Sin organización**: La información sin organizar es un problema para obtener información concisa.

Para resolver esos problemas, una base de datos relacional podría almacenar una tabla separada para los clientes y otra tabla separada para las ordenes.

### Modelo Cliente - Servidor 

![](../../../assets/png/server\_client.png)

MySQL también utiliza una arquitectura conocida como **modelo cliente-servidor.**

La parte del **servidor** es donde reiden realmente sus datos. Pero para poder acceder a esos datos, un **cliente** deberá pedirlos.

Un cliente realiza peticiones por medio de SQL al servidor para recuperar información almacenada.

***

### Pequeña historia de MySQL y MariaDB 

\


El SGBD MySQL fue desarrollado por la empresa sueca de Michael Widenius, MySQL AB, en 1995. Después, la empresa estadounidense Sun Microsystems adquirió MySQL AB en 2009 y siguió desarrollando el sistema de gestión de base de datos **open source**. Sin embargo, un año más tarde, Oracle compró la empresa Sun Microsystems y, junto con otros productos, Oracle se hizo con MySQL.

Michael Widenius decidió fundar MariaDB Foundation y crear el SGBD MariaDB cuando Oracle adquirió la empresa Sun Microsystems. El creador y fundador de MySQL quería asegurarse de que siguiera habiendo un sistema de gestión de base de datos open source, por lo que empezó MariaDB. MariaDB se hizo basándose en la estructura de MySQL lo que hace que haya una gran compatibilidad entre ambos sistemas de gestión de base de datos. Además, el término LAMP funciona cada vez más con el SGBD MariaDB en vez de MySQL.

> ¿Sabías que? Michael Widenius ha creado 3 sistemas de gestión de bases de datos y cada uno de ellos ha recibido el nombre de uno de sus hijos. El sistema de gestión de base de datos MySQL se llama así por la primera hija del desarrollador del sistema, My, y combinándolo con el acrónimo del lenguaje SQL, forma el nombre, MySQL. También desarrolló MaxDB, por su hijo Max, ahora propiedad de SAP y ahora está trabajando en MariaDB, llamado por su hija menor, Maria.

* :link:    [Instalación manual MySQL archivo zip](install\_zip/)
* :link:    [Instalación de MySQL en Ubuntu](install\_in\_ubuntu/)

\*\[SQL]: Structured Query Language
