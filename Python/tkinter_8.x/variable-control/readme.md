<a name="top"></a>

* [declarar variables de control](#mark2)
* [métodos](#mark3)

## Variables de control

Las variables de control son objetos especiales que se asocian a los widgets para almacenar sus valores y facilitar su disponibilidad en otras partes del programa. Pueden ser del tipo númerico, de cadena y booleano.

Cuando una variable de control cambia de valor el widget que la utiliza lo refleja automáticamente, y viceversa.

Las variables de control también se emplean para conectar varios widget del mismo tipo por ejemplo, varios controles del tipo **Radiobutton**. En este caso tomarán un valor de varios posibles.

## <a name="mark2">Declarar variables de control</a>

Las variables de control se declaran de forma diferente en función al tipo de dato que almacenan.

```python
entero = intVar() # Declara variable de tipo entero
flotante = Doublevar() # Declara variable de tipo flotante
cadena = StringVar() # Declara variable de tipo cadena
booleano = BooleanVar() # Declara variable de tipo booleana
```

También, en el momento de declarar una variable es posible asignar un valor inicial.

```python
nombre = StringVar(value="Enidev911")
```

[volver a índice](#top)

---

## <a name="mark3">Métodos</a>

### set()

El método ***set()*** asigna un valor a una variable de control. Se utiliza para modificar el valor o estado de un widget:

```python
nombre = StringVar()
id_usuario = IntVar()
# usando el método set
nombre.set("Marco Contreras")
id_usuario.set(1)
# asociando variables a widgets
Label(ventana, textvariable=id_usuario, width=5)
Label(ventana, textvariable=nombre, width=20)
```

### get()

El método ***get()*** obtiene el valor que tenga una variable de control, en un momento dado. Se utiliza cuando es necesario leer el valor de un control:

```python
# usando el método get
print('Nombre: ' + nombre.get())
print('Id usuario: ' + id_usuario.get())
```

### trace()

El método ***trace()*** se emplea para "detectar" cuando una variable es leída, cambia de valor o es borrada.

**Ej sintaxis:**

```python
widget.trace(type, function)
```
El primer argumento estable el tipo de suceso a comprobar:  

- **'r':** lectura (read)
- **'w':** escritura (write)
- **'u':** borrado

El segundo argumento indica la función que será llamada cuando se produzca el suceso. 

En el siguiente ejemplo se define una variable de control de tipo cadena y con el método ***trace()*** se asocian su lectura y cambio de valor a dos funciones que son llamadas cuando ocurren estos sucesos. Concretamente, cuando se utilice el método ***set()*** se llamará a la función 'change' y cuando se use ***get()*** a la función 'read'.

```python
fullname = StringVar()
def change(*args):
	print('Ha cambiado su valor')

def read(*args):
	print('Ha sido leído su valor')

fullname.trace('w', change)
fullname.trace('r', read)
fullname.set('Enidev911')
print(fullname.get())
```

[volver a índice](#top)

---

## <a name="mark3">Validar y calcular datos</a>

Cuando se construye una ventana con varios widgets se pueden seguir distintas estrategias para validar los datos que se introducen durante la ejecución de un programa.

- Una opción podria validar la información y realizar los cálculos después de que sea introducida, por ejemplo, despues de presionar un botón.

- Otra posibilidad podría ser haciendo uso del método **trace()** y la opción 'command', para validar y calcular la información justo en el momento que un widget y su variable asociada cambien de valor.


