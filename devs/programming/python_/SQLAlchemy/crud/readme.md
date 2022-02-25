# crud

### Conectarse a la base de datos

**create\_engine** utilizado para inicializar la conexión a la base de datos, SQLAlchemy usa una cadena para indicar la información de la conexión.

**Sintaxis**:

```
Tipo de base de datos+nombre del controlador de la base de datos://nombre de usuario:contraseña@dirección de la máquina:número de puerto/nombre de la base de datos
```

Solo necesitamos remplazar el nombre de usuario, la contraseña y otra información según sea necesario. Ejemplo:

```python
engine = create_engine('mysq+pymysql://enidev911:1234@localhost:3306/test')
```

SQLAlchemy también es compatible con los parámetros **connect\_args**, la mayoría de la información de configuración se gestiona por dict. Ejemplo:

```python
connect_args = {
	'user': 'root',
	'password': '1234',
	'database': 'store',
	'host': '127.0.0.1',
	'port': 3306
	}
e = create_engine('mysql+pymysql://', connect_args=connect_args)
```

### Describir la estructura de la tabla.

Con SQLAlchemy, todas las clases declarativas heredan de la clase base creada por **declarative\_base()** (que tradicionalmente se llama Base).

La clase contiene algunas propiedades especiales predefinidas (como \_\_tablename\_\_) Y atributos de clase general personalizables.

* **\_\_tablename\_\_**: Se utiliza para esteblecer el nombre de la tabla
* **Column()**: Utilizado para definir el campo de la tabla de datos, puede especificar el tipo de campo (String, Integer...) y varias restricciones (primary\_key, nullable, ...).

Las categorías correspondientes de la tabla de datos típica son las siguientes:

```python
class User(Base):
	__table__ = 'users'

	id = Column(Integer(), primary_key=True)
	name = Column(String(20))
```

### Definición de relación

Dado que varias tablas de una base de datos relacional también pueden usar claves foráneas para lograr uno a muchos, muchos a muchos, y así sucesivamente, el marco ORM también puede proporcionar relación uno a muchos, muchos a muchos y otras funciones entre dos objetos.

### Relación uno a muchos

Para una aplicación de blog ordinaria, los usuarios y los artículos son obviamente una relación de uno a muchos. Un artículo pertenece a un usuario y un usuario puede escribir muchos artículos. Luego pueden usar la asociación de clave foránea entre ellos:

```python
## Uno a muchos
from sqlalchemy import Column, String, Integer, Text, ForeignKey

class User(Base):
	__table__= 'users'

	id = Column(Integer(), primary_key=True)
	name = Column(String(30), nullable=False)

	def __repr__(self):
		return 'User(id=%s, name=%s)'%(self.id, self.name)

class Article(Base):
	__tablename__ = 'articles'
	id = Column(Integer(), primary_key=True)
	title = Column(String(255))
	content = Column(Text())
	user_id = Column(Integer(), ForeignKey('users.id'))

	def __repr__(self):
		return 'Article(id=%s, title=%s, user_id=%s)' % (self.id, self.title, self.user_id)
```

Cada artículo tiene una clave externa que apunta a la identificación de la clave primaria en la tabla de usuario (la clave foránea se define en el artículo, po lo que varios artículos pueden corresponder a un usuario, es decir, la relación es de muchos a uno de la tabla de artículos).

Primero importemos algunos datos de prueba, 5 usuarios y 100 publicaciones de blog:

```python
from faker import Factory

faker = Factory.create()

```

| Function | MySQL / MariaDB      | PostgreSQL           | SQLite               |
| -------- | -------------------- | -------------------- | -------------------- |
| substr   | :heavy\_check\_mark: | :white\_check\_mark: | :heavy\_check\_mark: |
