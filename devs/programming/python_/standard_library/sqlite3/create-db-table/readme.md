## Creación de una base de datos y tablas

En principio no se requiere tener más que Python instalado para poder trabajar con SQLite. Podemos desde nuestro propia aplicación crear la base de datos y sus tablas

Primer ejemplo: 

```python
import sqlite3

conexion = sqlite3.connect("bd1.bd")
try:
	conexion.execute("""CREATE TABLE article(
						code INTEGER PRIMARY KEY AUTOINCREMENT,
						desc TEXT,
						price REAL)""")

	print("Se creo la base de datos")
except sqlite3.OperationalError err:
	print("Table already exists")
	conexion.close()
```

Disponemos de un **try/except** al momento de crear la tabla debido a que si ejecutamos por segunda vez este programa se tratará de crear nuevamente la tabla artículos ya existente genera una excepción de tipo **OperationalError**. Si no queremos disponer de la excepción `OperationalError` podemos modificar el comando SQL de la creación de tabla:

```python
import sqlite3

conexion = sqlite3.connect("bd1.bd")
conexion.execute("""CREATE TABLE IF NOT EXISTS article(
						code INTEGER PRIMARY KEY AUTOINCREMENT,
						desc TEXT,
						price REAL)""")

conexion.close()
```

Una forma más practica es ayudandonos con el módulo os y haciendo una comprobación si existe el archivo de base de datos: 

```python
import sqlite3
import os 


if os.path.isfile('bd1.bd'):
	print("Database already exists!")

else:
	conexion = sqlite3.connect("bd1.bd")
	conexion.execute("""CREATE TABLE IF NOT EXISTS article(
						code INTEGER PRIMARY KEY AUTOINCREMENT,
						desc TEXT,
						price REAL)""")
	print("Database created successfully!")
	conexion.close()
```

### Recuperar filas con for

```python
## Recuperar todas las filas 

conexion = sqlite3.connect('bd1.bd')
cursor = conexion.execute('select * from article')

for fila in cursor():
	print(fila)
conexion.close()
```






