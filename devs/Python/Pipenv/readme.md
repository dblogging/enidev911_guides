
- Crea un entorno virtual con la versión 3 de Python  
```bash
pipenv --three
```
- Crea un entorno virtual con la versión 2 de Python 
```bash
pipenv --two
```

- Activar un entorno virtual (si no existe, lo crea en el directorio actual) 
```bash
pipenv shell
```

- Eliminar un paquete - o eliminar todos los paquetes
```bash
pipenv uninstall django
#o 
pipenv uninstall--all
```