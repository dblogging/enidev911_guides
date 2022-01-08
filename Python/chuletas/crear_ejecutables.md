Python es uno de mis lenguajes de programación favoritos. Dicho esto, si alguna vez ha tenido que implementar una aplicación escrita en ¨Python, entonces sabe lo doloroso que puede ser.

Afortunadamente, hay algunas herramientas de código abierto bastante impresionantes que de pueden usar para empaquetar un programa Python en un ejecutable binario independiente que contenga todo lo necesario para ejecutar la aplicación (es decir, intérprete de Python, código de programa, bibliotecas, datos, etc.)



### Pyinstaller


```bash
pyinstaller --onefile --windowed --icon=app.ico app.py
```








Uso de "bundle_files" y "zipfile"

Una forma más fácil (y mejor) de crear ejecutables de un solo archivo es para configurar bundle_files en 1 o 2, y para establecer zipfile a Ninguno (None). Este enfoque hace no requiere extraer archivos a un ubicación temporal, que proporciona inicio del programa mucho más rápido.

Los valores válidos para bundle_files son:

3 (predeterminado) no agrupar
2 agrupe todo menos el intérprete de Python
1 agrupe todo, incluido el intérprete de Python
Si zipfile se establece en Ninguno, los archivos se agruparán dentro del ejecutable en lugar de library.zip.


## cxfreeze


```
pip install cx_Freeze
```

```
pipenv install cx_Freeze
pipenv update cx_Freeze
```

**Compilar indicando un directorio para los archivos**


```
cxfreeze script.py: --target-dir ejecutable
```

```py
# setup.py
# Las dependencias se detectan automáticamente, pero es posible que sea necesario ajustarlas.
# "packages": ["os"] se usa solo como ejemplo

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "guifoo",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("guifoo.py", base=base)]
)
```