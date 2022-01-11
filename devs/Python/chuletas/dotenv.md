### Dotenv

Lo mejor es ponerlo en un archivo de configuración, pero ¡OJO!... No incluyas este archivo en el repositorio. Entonces, ¿cómo lo hacemos?

Los archivos `.env` (Dotenv) vienen al rescate y, casi en cualquier lenguaje, puedes encontrar una librería o paquete que te hace la vida más fácil. En python el paquete en cuestión es *python-dotenv*:

**¿Cómo es un archivo .env?**

Es un simple archivo de texto donde, en cada línea, definimos una variable de entorno y le asignamos su valor mediante el operador `=`.

```
PG_USER=postgres
PG_PASSWORD=miclavesupersecreta
PG_DBNAME=labasededatos
PG_HOST=elservidor
API_KEY=la_key_supersecreta
```

Para no guardar estos datos sensibles en nuestro repositorio, es importante agregar el archivo `.gitignore` el archivo `.env` y, para no perder de vista las variables de entorno que podemos configurar, duplicar el archivo como `.env.sample`, eso sí, sin poner los valores reales. De esta forma, cuando descarguemos nuestro proyecto, bastará con copiar el archivo `.env.sample` y renombrarlo a `.env`.


### Instalación

```cmd
pip install python-dotenv
```
