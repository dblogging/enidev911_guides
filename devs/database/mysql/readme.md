[comment]: <> (Author: Marco Contreras Herrera)
[comment]: <> (Email: enidev911@gmail.com)

<h2 align="center">
  <u>MySQL resumen</u>
  <img src="../../../assets/ico/MySQL_Logo.ico">
</h2>

<br>

MySQL es un sistema open source de administración de bases de datos que actualmente es desarrollado y soportado por Oracle.  

Una base de datos es una colección  estructurada de datos que está organizada para ser usada y extraída de forma sencilla.  

MySQL fue lanzado en 1995. Desde entonces, ha pasado por varios cambios. A pesar de que Oracle está a cargo ahora, MySQL sigue siendo un **software open source**, lo que quiere decir que puede ser usado y modificado por cualquier persona.

Para entender un poco el funcionamiento de MySQL, es importante conocer dos conceptos que van conectados.  

- [Bases de datos relacionales]
- [Modelo de Cliente-Servidor]


<h2 align="center">
  <u>Bases de datos relacionales</u><br><br>
  <img src="../../../assets/png/relationship_database.png" width="350">
</h2>

Cuando se trata de almacenar datos en una base de datos, hay distintos enfoques que se pueden utilizar.

MySQL opta por un enfoque basado en el modelo o esquema relacional. Con una base de datos relacional, sus datos son fragmentados en varias áreas de almacenamiento separadas las denominadas **tablas** en lugar de poner todo junto en una gran unidad de almacenamiento.  

Por ejemplo, quisiera almacenar dos tipos de información:

- **Pedidos**: Nos interesa el producto, el precio, quién hizo la orden, etc. 
- **Cliente**: Su nombre, dirección, detalles, etc.

Si intenta poner todos estos datos juntos en un gran almacen, tendrá algunos problemas como:  

- **Datos distintos**: Los datos que usted necesita para recolectar para una orden son diferentes que lo que son para un cliente. 
- **Datos duplicados**: Cada cliente tiene un nombre, y cada orden también tiene el nombre del cliente. Es algo poco eficiente lidiar con datos repetidos.
- **Sin organización**: La información sin organizar es un problema para obtener información concisa.

Para resolver esos problemas, una base de datos relacional podría almacenar una tabla separada para los clientes y otra tabla separada para las ordenes.



<h2 align="center">
  <u>Modelo Cliente - Servidor</u><br>
  <img src="../../../assets/png/server_client.png" width="350" height="280">
</h2>

MySQL también utiliza una arquitectura conocida como **modelo cliente-servidor.**


La parte del **servidor** es donde reiden realmente sus datos. Pero para poder acceder a esos datos, un **cliente** deberá pedirlos.  

Un cliente realiza peticiones por medio de SQL al servidor para recuperar información almacenada.

---


*[SQL]: Structured Query Language