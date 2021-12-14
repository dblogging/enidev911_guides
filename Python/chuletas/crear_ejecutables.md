Uso de "bundle_files" y "zipfile"

Una forma más fácil (y mejor) de crear ejecutables de un solo archivo es para configurar bundle_files en 1 o 2, y para establecer zipfile a Ninguno (None). Este enfoque hace no requiere extraer archivos a un ubicación temporal, que proporciona inicio del programa mucho más rápido.

Los valores válidos para bundle_files son:

3 (predeterminado) no agrupar
2 agrupe todo menos el intérprete de Python
1 agrupe todo, incluido el intérprete de Python
Si zipfile se establece en Ninguno, los archivos se agruparán dentro del ejecutable en lugar de library.zip.