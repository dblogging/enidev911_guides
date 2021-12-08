SQLite en general, es una base de datos server-less que se puede utilizar en casi todos los lenguajes de programación, incluido Python. Server-less significa que no hay necesidad de instalar un sevidor separado para trabajar con SQLite para que pueda conectarse directamente con la base de datos.

SQLite es una base de datos liviana que proporciona un sistema de administración para bases de datos relacionales y sin mucha configuración.  


### <a name="#1">Crear una conexión</a>

Para utilizar SQLite3 en Python, primero deberás importar el módulo *sqlite3* y
luego crear un objeto de conexión para conectarnos a la base de datos. Este nos permitirá ejecutar las sentencias SQL.  

Un objeto de conexión se crea utilizando el método *connect():*  

```python
import sqlite3

con = sqlite3.connect('mydatabase.db')
```

Se creará un nuevo archivo llamado 'mydatabase.db' donde se almacenará nuestra base de datos.

### <a name="#1">Crear un cursor</a>

Para ejecutar una sentencia sql de SQLite en Python, se necesita de un objeto cursor. Puedes crearlo utilizando el método cursor().

El cursor es un método del objeto de conexión.Para ejecutar sentencias de SQLite3, primero se establece una conexión y luego se crea un objeto cursor utilizando el objeto de conexión de la siguiente manera:

```python
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
```
Ahora que tenemos el objeto cursor almacenado en la variable cur podemos llamar al método *execute()* para ejecutar cualquier consulta sql.



### <a name="#2">Crear una base de datos en memoria</a>

Cuando creas una conexión con SQLite, un archivo de base de datos se crea automáticamente si no existe ya. Este archivo de base de datos se crea en el disco, ademas, también podemos crear una base de datos que se carge en la RAM usando el siguiente argumento en el método *connect()*  

```python
con = sqlite.connect(':memory:')
```
Con el método de conexión. Esta base de datos se llama base de datos en memoria.

Considera el código a continuación en el que creamos una base de datos con los bloques **try**, **except** y **finally** para manejar cualquier excepción:  

```python
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Conexión establecida: Base de datos creada en memoria")

    except Error:
        print(Error)

    finally:
        con.close()

sql_connection()
```  

Primero, se importa el módulo *sqlite3*, luego se define una función *sql_connection.* Dentro de la función, tenemos un bloque *try* donde la función *connect()* está devolviendo un objeto de conexión después de establecer la conexión.  

Luego tenemos un bloque *except*, que en caso de excepciones, imprime el mensaje de error. Si no hay errores, se establecerá la conexión y se mostrará un mensaje de la siguiente manera.  


### <a name="#2">Crear una tabla</a>

Para crear una tabla en SQLite3, es similar a cualquier sentencia sql me refiero a la instrucción **CREATE TABLE** toda la sentencia debe ir dentro del método *execute()*.

Considera los siguientes 3 pasos: 
	
1. Se crea un objeto de conexión.
2. El objeto cursor se crea utilizando el objeto de conexión.
3. Usando el objeto cursor, se llama al método *execute()* para ejecutar la consulta.

Vamos a crear una tabla de ejemplo que se llamará **Empleados** y tendrá los siguientes atributos:  

- id
- nombre
- salario
- departamento
- cargo

EL código para ello es el siguiente:  

```python
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con

    except Error as e:
    	print('Error: ', e)

def run_query(sql, params=None):
	con = sql_connection()
	cur = con.cursor()
	try:
		cur.execute(query, params)
		con.commit()
	except Error as e:
		print('Error: ', e)

sql = '''CREATE TABLE empleados(
				id INTEGER AUTOINCREMENT,
				nombre TEXT,
				salario REAL,
				departamemto TEXT,
				cargo TEXT)'''
run_query(sql)
```


### <a name="#7">Excepciones SQLite3</a>

Las excepciones son errores en tiempo de ejecución. En **Python**, todas las excepciones son instancias de la clase derivada BaseException.

En SQLite3, tenemos las siguientes excepciones principales de Python: 


**DatabaseError**  

Cualquier error relacionado con la base de datos genera el DatabaseError.


**IntegrityError**

IntegrityError es una subclase de DatabaseError y se genera cuando hay un problema de integridad de los datos, por ejemplo, los datos foráneos no se actualizan en todas las tablas, lo que resulta en una inconsistencia de los datos.

**ProgrammingError**

La excepción ProgrammingError se produce cuando hay errores de sintaxis o no se encuentra la tabla o se llama a la función con un número incorrecto de parámetros.  


**OperationalError**  

Esta excepción se produce cuando fallan las operaciones de la base de datos, por ejemplo, una desconexión inusual. Esto no es culpa de los programadores


