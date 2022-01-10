### Introducción a la tabla de ROW ID

Siempre que crea una tabla sin especificar la opción **WITHOUT ROWID**, obtiene una columna de incremento automático implícita llamada **rowid**. La columna **rowid** almacena un entero de 64 bits con signo que identifica de forma exclusiva una fila en una tabla.

**Ejemplo:**

Primero, cree una nueva tabla nombrada `personas` que tenga dos columnas: 

|first_name|last_name|
|:--------:|:-------:|
|    -     |    -    |




```sql
CREATE TABLE people (
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);

```


<a href="https://www.sqlitetutorial.net/tryit/query/sqlite-autoincrement/#1"><button name="button" style="border-radius: 5%; border: 0; background: #4D80DF; padding: 6px 12px; cursor: pointer; color: #fff">Intentalo</button></a>


En segundo lugar, inserte una fila en la tabla `personas` utilizando la declaración `INSERT`:



```sql
INSERT INTO people (first_name, last_name) VALUES('Will', 'Smith');
```

<a href="https://www.sqlitetutorial.net/tryit/query/sqlite-autoincrement/#1"><button name="button" style="border-radius: 5%; border: 0; background: #4D80DF; padding: 6px 12px; cursor: pointer; color: #fff">Intentalo</button></a>
