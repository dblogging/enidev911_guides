## Creando el script

Este es script es muy sencillo el cual no tiene dependencias con otras librerías, sólo utilizando los módulos del **core de Python**.  

Primero, importamos los módulos que utilizaremos y que nos permitirán hacer el manejo de archivos, ejecutar comandos directamente en el sistema y más.


```python
import os 
import shutil
import sys
```

Breve explicación de los módulos importados:  

**os**: nos permite utilizar de manera efectiva y simple, funciones propias del sistema operativo

**shutil**: nos ofrece una serie de operaciones de alto nivel para archivos y colecciones.

**sys**: provee acceso a funciones y objetos mantenidos por el interprete.

Ahora ya es tiempo de comenzar directamente con la funcionalidad del script, como puedes notar, son pocos módulos, que incluso podríamos omitir el módulo **sys** y quedaría en sólo 2 pero, m+as adelante se puede ampliar el script.


A continuación, vamos a definir una función la cual nos permitirá saber con base a un tipo de extensión dada, retornará el nombre del directorio/folder al que pertenece o debe estar.  


```python
def directory(file_extension: str) -> str:
	if not file_extension:
		return

	folder_by_extension = {
		"exe": "Software",
		"txt": "Texts",
		"pdf": "PDF Documents",
		"epub": "Books",
		"jpg": "Images",
		"jpeg": "Images",
		"png": "Images",
		"raw": "Images",
		"mp3": "Music",
		"mp4": "Videos",
		"mkv": "Videos",
		"xlsx": "Excel Files",
		"ppt": "Slides",
		"doc": "Documents",
		"rar": "Compressed Files",
		"zip": "Compressed Files",
		"iso": "Iso Files"
	}
	return folder_by_extension.get(file_extension, 'Extras')
```


Como saben un diccionario se conforma por {key: value}, dónde **key** es la extensión del archivo y **value** es el nombre del directorio al que pertenece. Por ende definimos que, si por ejemplo a la función le pasamos una extensión **zip**, retornará **Compressed Files** y así consecuentemente con cada extensión definida.

Entendiendo lo anterior, ya tenemos la primera parte de nuestro script, para obtener el nombre del directorio en el guardaremos nuestros archivos.


### Primera parte función organizer

Y es hora de llegar a la parte interesante, la función principal de nuestro script, para ello definimos una función **organizer**, iremos por pasos, ya que es un poco largo, y así, explicar cada parte.

```python
def organizer(path: str):
	if not os.path.exists(path):
		print(f"ERROR. Not found {path} or not exists.")
		return
	files = os.listdisr(path)
	extensions = [os.path.splitext(file)[1].strip(".") for file in files]
```

Primero en nuestra función vamos a requerir de un parametro nombre **path** y de tipo string. Esta será la URL/locación de la carpeta en donde organizarás los archivos, por ejemplo (C:\\Users\\User\\Documents). Seguido, utilizamos el módulo os, para saber si existe la dirección que le hemos indicado, de lo contrario, imprimimos un error y nos salimos del ciclo de ejecución.

Si existe, entonces con una variable de nombre `files`, guardamos una lista que va a contener los nombres de las **entradas/archivos** en el directorio dado por la **ruta/path**. 

Seguido, vamos a definir una variable **extensions** que contendrá todas las extensiones de los archivos que se encuentren en el directorio, por ejemplo [<<exe>>, <<pdf>>, <<epub>>] etc.

### Segunda parte función organizer


Ya tenemos la primera parte, ahora toca la segunda parte.  
Para esto, haremos dos iteraciones a las extensiones que obtuvimos arriba.

```python
	for ext in extensions:
		dir = directory(ext) or ""
		new_directory = os.path.join(path, dir)
		if dir and not os.path.exists(new_directory):
			os.makedirs(new_directory)

	for file in files:
		ext = os.path.splitext(file)[1].strip(".")
		_dir = directory(ext)
		if not _dir:
			continue

		source_filepath = os.path.join(path, file)
		destination_filepath = os.path.join(path, _dir, file)

		if not os.path.exists(destination_filepath):
			shutil.move(source_filepath, destination_filepath)
			print(f'Was moved {file} into {_dir} directory. \n')


	print(f"All the files was organized sucessfully in {path}")
```

En la primera iteración, recorremos la lista de las extensiones y, por cada extensión, se la pasaremos a nuestra función **directory**, para así con la extensión dada, obtener el nombre del directorio al que pertenece.

Después, entramos a la dirección que proporcionamos a path, y pasamos también, el nombre del directorio que nos regresó nuestra función directory, si existe no hace nada, de lo contrario, creamos el directorio con `os.makedirs(new_directory)`

En la segunda iteración, recorremos los archivos que se encuentran en el directorio, hacemos un split para obtener la extensión de cada archivo en el ciclo y obtenemos el nombre de su respectiva carpeta de destino. Si la función no devuelve nada, damos un continue.

Seguido, declaramos dos variables, una con el nombre de `source_filepath`, la cual es la **dirección/path**