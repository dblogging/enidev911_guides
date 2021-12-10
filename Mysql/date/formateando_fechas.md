### Insertando Fechas con Diferentes Formato en MySQl

**MySql** cuando almacena una fecha lo hace deacuerdo a la norma ISO_8601 esto es YYYY-mm-dd.

**¿Por que `MySql` fecha en ese formato?**

En resumen los puntos más importantes son:

- Evitar formatos ambiguos
- Tener un formato único y universal
- Poder ser organizados de más a menos significativo
- Estar en formato ordenable, incluso si tratáramos a las **fechas** como cadenas de texto, podríamos ordenarlas alfabéticamente.


Si ingresamos una fecha que no cumpla con ese formato, simplemente provocará un error, ya que no sera reconocido como fecha válida.


**¿Como podemos solucionar esto?**

Mysql tiene una función incorporada llamada **GET_FORMAT** con el cual podemos insertar fechas con distinto formato, solo le tenemos que indicar en que formato estamos recibiendo la decha para que MySQL luego lo procese.

Los formatos que acepta **GET_FORMAT** son los siguientes

|**llamada función**|**Resultado**|
|-------------------|-------------|
|GET_FORMAT(DATE,'USA')|'%m.%d.%Y'|
|GET_FORMAT(DATE,'JIS')|'%Y-%m-%d'|
|GET_FORMAT(DATE,'ISO')|'%Y-%m-%d'|
|GET_FORMAT(DATE,'EUR')|'%d.%m.%Y'|
|GET_FORMAT(DATE,'INTERNAL')|'%Y.%m.%d'|
|GET_FORMAT(DATE,'EUR')|'%d.%m.%Y'|
