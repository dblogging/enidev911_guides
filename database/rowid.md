### Introducción a la tabla de ROW ID

Siempre que crea una tabla sin especificar la opción **WITHOUT ROWID**, obtiene una columna de incremento automático implícita llamada **rowid**. La columna **rowid** almacena un entero de 64 bits con signo que identifica de forma exclusiva una fila en una tabla.

**Ejemplo:**

Primero, cree una nueva tabla nombrada `personas` que tenga dos columnas:  


```
 ____________________
|first_name|last_name|
|----------|---------|

```


```sql
CREATE TABLE people (
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);

```

<a class="sql" href="https://www.sqlitetutorial.net/tryit/query/sqlite-autoincrement/#1" target="_blank" rel="noopener noreferrer"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Intentalo</font></font></a>





<a href="https://www.sqlitetutorial.net/tryit/query/sqlite-autoincrement/#1"><button name="button">Click me</button></a>