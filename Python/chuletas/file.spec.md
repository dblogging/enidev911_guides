Lo primero que hace *PyInstaller* es crear un archivo de especificaciones **myscript.spec**. Ese archivo se almacena en el directorio `--spectpath`, por defecto el directorio actual.

El archivo de especificaciones le dice a *Pyinstaller* cómo procesar su secuencia de comandos. Codifica los nombres de los scripts y la mayoría de las opciones que le da al comando *pyinstaller*. El archivo de especificaciones es en realidad código Python ejecutable. Pyintaller crea la aplicación ejecutando el contenido del archivo de especificaciones.

Hay cuatro casos en los que resulta útil modificar el archivo de especificaciones:

- Cuando desee agrupar archivos de datos con la aplicación.

Las declaraciones en un archivo de especificaciones crea instancia de cuatro clases, `Analysis`, ``PYZ`, `EXE`, `COLLECT`.


### Agregar archivos al paquete

Para agregar archivos al paquete, crea una lista que describe los archivos y la proporciona a la llamada **Analysis**. Cuando se agrupa en una sola carpeta los archivos de datos agregados se copian en la carpeta con el ejecutable. Cuando se agrupa en un solo ejecutable las copias de los archivos agregados se comprimen en el ejecutable y se expanden a la carpeta temporal antes de la ejecución. Esto significa que cualquier cambio que realice un ejecutable de un solo archivo en un archivo agregado se perderá cuando finalice la aplicación.

En cualquier caso, para encontrar los archivos de datos en tiempo de ejecución

### Información en Tiempo de Ejecución

Su aplicación debe ejecutarse 