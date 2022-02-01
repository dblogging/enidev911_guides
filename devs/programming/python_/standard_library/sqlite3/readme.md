Python DB-API  

Python DB-API es un conjutno de estándares recomendados por un grupo de interés especial para la estandarización de módulos de base de datos. Los módulos de Python proporcionan funcionalidad  de interfaz de base de datos, todos los productos de base de datos deben cumplir con este estándar. Los estándares DB-API se modificaron aún más a DB-API 2.0 mediante otra propuesta de mejora Python (PEP-249)

Según los estándares prescritos, el primer paso del proceso es obtener la conexión con el objeto que representa la base de datos. Para establecer una conexión con una base de datos SQLite, es necesario importar el módulo sqlite3 y ejecutar la función **connect()**.  

La fuinción **connect()** devuelve un objeto de conexión que hace referencia a la base de datos existente o una nueva base de datos si no existe.  

Los siguientes métodos se definen en la clase de conexión.

| Método | Descripción |
| ------ | ----------- |
|**cursor()**| Devuelve un objeto cursor que usa esta conexión.|
|**commit()**| Compromete explícitamente cualquier transacción pendiente a la base de datos.|
|**rollback()**| Este método opcional hace que una transacción se retrotraiga al punto de partida. Puede que no se implemente en todas partes.|
|**close()**| Cierra la conexión a la base de datos de forma permanente. Los intentos de usar la conexión después de llamar a este método generarán un error DB-API.|

Un cursor es un objeto de Python que le permite trabajar con la base de datos. Actúa como un identificador para una consulta SQL determinada; permite la recuperación de una o más filas del resultado. Por lo tanto, se obtiene un objeto de cursor de la conexión para ejecutar consultas SQL utilizando la siguiente declaración:  

```
cur = db.cursor()
``` 

Los siguientes métodos del objeto cursor son útiles.

| Método | Descripción |
| ------ | ----------- |
|**execute()**| Ejecuta la consulta SQL en un parámetro de cadena.|
|**executemany()**| Ejecuta la consulta SQL usando un conjunto de parámetros en la lista de tuplas.|
|**fetchone()**| Obtiene la siguiente fila del conjunto de resultados de la consulta.|
|**fetchall()**| Obtiene todas las filas restante del conjunto de resultados de la consulta.|
|**close()**| Cierra el objeto cursor.|

Los métodos **`commit()`** y **rollback()** de la clase de conexión garantizan el control de transacciones. El método **execute()** del cursor recibe una cadena que contiene la consulta SQL. Una cadena que tiene una consulta SQL incorrecta genera una excepción, que debe manejarse correctamente. Es por eso que el método **`execute()`** se coloca dentro del bloque **`try`** y el efecto de la consulta SQL se guarda persistentemente usando el método **`commit()`**. Sin embargo, si la consulta SQL falla, el bloque **`except`** procesa la excepción resultante y la transacción pendiente se deshace mediante el método **`rollback()`**. El uso típico del método **`execute()`** es el siguiente:

```py
try:
	cur = db.cursor()
	cur.execute("Query")
	db.commit()
	print("success message")
except:
	print("error")
	db.rollback()
db.close()
```

### <a name="#1">Crear una nueva tabla</a>

Una cadena que encierra la consulta **`CREATE TABLE`** se pasa como parámetros al método **`execute()`** del objeto cursor. El siguiente código crea las tabla **students** en la base de datos **university.db**

```py
import sqlite3
db = sqlite3.connect('university.db')
try:
	cur = db.cursor()
	cur.execute('''CREATE TABLE students(
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT(30) NOT NULL,
					age INTEGER,
					note REAL);
					''')
	print('Table created successfully')
except:
	print('Error in operation')
	db.rollback()
db.close()
```

Esto se puede verificar usando el comando **.tables** en sqlite shell. 

```
sqlite3 univerty.db
===================
Sqlite>.tables
```

### <a name="#1">Insertar un registro</a>

Una vez más, el método **execute()** del objeto cursor debe llamarse con un argumento de cadena que represente la sintaxis de la consulta **`INSERT`** se define de la siguiente forma: 

```py
qry = '''INSERT INTO students (name, age, note) 
		 VALUES ('mark', 31, 6.5);'''
```

Tenemos que usarlo como parámetro del método **execute()**. Para obtener en cuenta las posibles excepciones, la declaración **execute()** se coloca en el bloque **try** como se explicó anteriormente.  

Puede verificar el resultado utilizando la consulta **SELECT** en el shell Sqlite.


```
sqlite3 univerty.db
===================
Sqlite>.SELECT * FROM students;
===============================
1 | Mark | 31 | 6.5,0 
```  

### <a name="#1">Usar parámetros en una consulta</a>

A menudo, los valores de las variables de Python deben usarse en operaciones SQL. Una forma es usar la función **`format()`** de las cadenas de Python para poner los datos de Python en una cadena. Sin embargo, esto puede provocar una brecha de seguridad para ataques de inyección SQL a un programa. En su lugar utilice la sustitución de parámetros como se recomienda en DB-API de Python. El carácter "?" se utiliza como marcador de posición en la cadena de consulta y se proporciona los valores en forma de tupla en el método **execute()**. El siguiente ejemplo inserta un registro utilizando el método de sustitución de parámetros:  

```py
import sqlite3 
db = sqlite3.connect('univerty.db')
qry = """INSERT INTO students (name, age, note) VALUES (?, ?, ?);"""
try:
	cur = db.cursor()
	cur.execute(qry, ('Jhon', 24, 5.5))
	db.commit()
	print("Inserted successfully..")
except:
	print("Error in operation")
	db.rollback()
db.close()
```

El método **`executemany()`** se utiliza para agregar varios registros a la vez. Los datos que se agregarán deben incluirse en una lista de tuplas, y cada tupla debe contener un registro. El objeto de lista (que contiene tuplas) es el parámetro del método **`executemany()`**, junto con la cadena de consulta.  


```py
import sqlite3

db=sqlite3.connect('university.db')
qry="INSERT INTO students (name, age, note) VALUES (?,?,?);"
students = [('angel', 19, 7.0), ('deepak', 25, 4.6)]

try:
	cur=db.cursor()
	cur.executemany(qry, students)
	db.commit()
	print("rows inserted successfully..")
except:
	print("error in operation")
	db.rollback()
db.close()
```

### <a name="#1">Recuperar registros</a>


Cuando la cadena de consulta contiene una consulta **`SELECT`**, el método **`execute()`** forma un objeto de conjunto de resultados que contiene los registros devueltos. Python DB-API define los métodos para recuperar los registros:  

- **`fetchone()`**: recupera el siguiente registro disponible del conjunto de resultados. Es una tupla que consta de valores de cada columna del registro obtenido.
- **`fetchall()`**: recupera todos los registros restantes en forma de lista de tuplas. Cada tupla corresponde a un registro y contiene valores de cada columna de la tabla.

Cuando use el método **`fetchone()`**, use un bucle para iterar a través del conjunto de resultados, como se muestra a continuación:  

```py
import sqlite3
db = sqlite3.conect('university.db')
qry = 'SELECT * FROM students;'

cur = db.cursor()
cur.execute(qry)
while True:
	record = cur.fetchone()
	if record == None:
		break
	print(record)
db.close()
```


### <a name="#1">Actualizar registros</a>


La cadena de consulta en el método **`execute()`** de contener una sintaxis de una consulta para actualizar. Por ejemplo el valor de `age` a 26 para el estudiante con nombre **mark** definiría una cadena de la siguiente manera:  

```py
qry = "UPDATE students SET age = 26 WHERE name = 'mark';"
``` 

También puede utilizar la técnica de sustitución para pasar el parámetro a la consulta **`UPDATE`**.


```py
import sqlite3
db = sqlite3.connect('university.db')
qry = 'UPDATE FROM students SET age=? WHERE name=?;'
try:
	cur = db.cursor()
	cur.execute(qry, (26, 'mark'))
	print('row updated successfully...')
except:
	print('error in operation')
	db.rollback()
db.close()
```

### <a name="#1">Eliminar registros</a>

La cadena de consulta debe contener la sintaxis de consultas **`DELETE`**. Por ejemplo, el siguiente código se utiliza para eliminar a **mark** de la tabla de de `students`.


```py
qry = "DELETE FROM students WHERE name = 'mark'"
```

Usando la sustitución para pasar el parámetro:

```py
import sqlite3
db = sqlite3.connect('university.db')
qry = "DELETE FROM students WHERE name = ?;"

try:
	cur=db.cursor()
	cur.execute(qry, ('mark',))
	db.commit()
	print("Row deleted successfully...")
except:
	print("error in operation")
	db.rollback()
db.close()
```

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


