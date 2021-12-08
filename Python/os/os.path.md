## Archivos y directorios

| Descripción | Método |
| ----------- | ------ |
|Saber si se puede acceder a un archivo o directorio|**os.acces**(path, access_mode)|
|Conocer el directorio actual|**os.getcwd**()|
|Cambiar de directorio de trabajo|**os.chdir**(path)|
|Crear un directorio|**os.mkdir**(path[, modo])|
|Crear directorios recursivamente|**os.mkdirs**(path[, modo])|
|Eliminar un archivo|**os.remove**(path)|
|Eliminar un directorio|**os.rmdir**(path)|



**os.getcwd()**

Retorna una cadena que representa el directorio de trabajo actual.

```python
os.getcwd()
## output: C:\\Users\\User
```

**os.chdir(path)**

```python
# Puede usar C:\\Users\\User\\Downloads o C:/Users/User/Downloads 
os.chdir('C:/Users/User/Downloads')
os.getcwd()
## output: C:\\Users\\User\\Downloads
```

**os.chmod(path, permits)**

```python

```


```python

```

## Rutas

El módulo os nos provee el submódulo **path** (os.path) el cual nos permite

