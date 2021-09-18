## DBAPI

La documentación y la información de descarga (si corresponde) para pysqlite están disponible en:  

[https://docs.python.org/library/sqlite3.html](https://docs.python.org/library/sqlite3.html)


### Conectando

**Cadena de conexión:**  

```
sqlite+pysqlite:///file_path
```


**Controlador**  

EL DBAPI Python de sqlite3 es de serie en todas las versiones modernas de Python; para cPython y Pypy, no es necesaria ninguna instalación adicional.  


**Conectar cadenas**  

La especificación del archivo para la base de datos SQLite se toma comomo parte de la base de datos de la URL. Tenga en cuenta que el formato de la URL de SQLAlchemy es:  


```
driver://user:pass@host/database
```

Esto significa que el nombre de archivo real que se utilizará comienza con los caracteres a la **derecha** de la tercera barra. Entonces, conectarse a una ruta de archivo relativa se ve así:  

```python
# relative path
e = create('sqlite3:///path/to/database.db')
```

Una ruta absoluta, que se indica comenzando con una barra, significa que necesita **cuatro barras**:  

```python
# absolute path
e = create_engine('sqlite:////path/to/database.db')
```

Para utilizar una ruta de Windows, se pueden utilizar las especificaciones de disco habituales y las barras diagonales inversas. Probablemente se necesiten barras diagonales inversas dibles:  

```python
e = create_engine('sqlite:///C:\\path\\to\\database.db')
```

El indentificador sqlite **:memory:** es el predeterminado si no hay ruta de archivo presente. Especifique simplemente lo siguiente:  

```python
e = create_engine('sqlite://')
```

## Conexiones URI

Las versiones modernas de SQLite admiten un sistema alternativo de conexiones mediante un **URI de nivel de controlador**, que tiene la ventaja de que se pueden pasar argumentos de nivel de controlador adicionales, incluidas opciones como "read only". El controlador Python sqlite3 admite este modo en las versiones modernas de Python 3. El controlador pysqlite de SQLAlchemy admite este modo de uso especificando "uri=true" en la cadena de consulta de la URL. El "URI" de nivel de SQLite se mantiene como parte de la "base de datos" de la URL de SQLAlchemy (es decir, despues de una barra):  


```python
e = create_engine("sqlite:///file:path/to/database?mode=ro&uri=true")
```



```python