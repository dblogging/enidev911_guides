## <u>WITH - PYTHON</u> <img src="../assets/img/python(144x144).png" width="30" align="right">


La sentencia **with** en Python es usado en el manejo de excepciones para hacer que el código sea más limpio y mucho más legible. Simplifica la gestión de recursos comunes como el flujo de archivos. En el siguiente ejemplo de código sobre cómo el uso de la instrucción with:


```py
# Sin el uso de with:
file = open('file_path', 'w')
file.write('Hello World!')
file.close()
```

En esta implementación una excepción durante la llamada a **file.write()** puede evitar que el archivo se cierre correctamente, lo que puede producir varios errores en el código, es decir muchos cambios en los archivos no entran en vigor hasta que el archivo se cierra correctamente.

---

```py
# Sin el uso de with:
file = open('file_path', 'w')
try:
    file.write('Hello World!')
finally:
    file.close()
```

En este enfoque se encarga de todas las excepciones.

---

```py
# Con with:
with open('file_path', 'w') as file:
    file.write('Hello World')
```

Tenga en cuenta que, a diferencia de las dos primeras implementaciones, no es necesario llamar al método **close()**. La instrucción **with** garantiza la adquisición y liberación adecuado de recursos. El uso de la declaración **with** hace que el código sea más compacto y mucho más legible. Por lo tanto **with** mps ayuda a evitar errores y fugas al garantizar que un recurso de libere correctamente.

## <p align="left"><u>Apoyando la declaración with con objetos definidos por el usuario</u><p>

<br>

Para usar la instrucción **with** en objetos definidos por el usuario. La declaración en respaldo en sus objetos asegurará que nunca deje nungún recurso abierto. Para ello necesitamos agregar los métodos **\_\_enter\_\_()** y **\_\_exit\_\_()**.

```py
class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename
    
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file 

    def __exit__(self):
        self.file.close()

# Usando with en un objeto
with MessageWriter('my_file.txt') as xfile:
    xfile.writer('Hello World!')
```

Vemos que seguido de **with** sigue el constructor de **MessageWriter** tan projnto como la ejecución ingresa al contexto de la declaración **with**, **MessageWriter** crea un objeto y Python llama al método **\_\_enter\_\_()** en este método inicializa el recurso que desea utilizar en el objeto. Esté método también siempre debe devolver un descriptor del recurso adquirido. Un descriptor de recurso son identificadores que proporciona el sistema operativo para acceder a los recursos solicitados por nuestra clase, se utiliza para hacer referencia al descriptor del objeto devuelto por **\_\_enter\_\_()**. Tan pronto el bloque se ejecuta se llama a **\_\_exit\_\_()** y se libera los recursos. 

---