# formatear\_cadena

### _Formatear una cadena (string)_ ![](../assets/img/python\(144x144\).png)

El primer método para formatear una cadena y el más primitivo, es usando el operador **`'%'`** (módulo). Dados los `'string' % valores`, las instancias de "%" en los `string` se remplazan con cero o más elementos de `valores`. Esta operación se conoce como interpolación de cadenas.

También tenemos símbolos con porcentajes para diferentes resultados:

%s - remplaza a una cadena de caracteres es uno de los más usado.

```py
print("En las %s se veía todo %s" % ("montañas", "pequeño"))
# output: En las montañas se veía todo pequeño
```

%c – convierte un código ASCII a su representación en carácter.

```py
print("El código ASCII '62' representa el símbolo '%c'" % 62)
# output : El código ASCII '62' representa el símbolo '>' 
```

%d o %i – remplaza un valor decimal entero '%d' es de decimal y'%i' es de integer.

```py
print("Jhon tiene %i años" % 31)
# output: Jhon tiene 31 años
print("%dx%d = %d" % (3,3,9))
# output: 3x3 = 9
```

%o - convierte un número a su equivalente en el sistema octal (con signo).

```py
print("El número '8' es equivalente al valor '%o' en el sistema octal" % 8)
# output El número '8' es equivalente al valor '10' en el sistema octal
```

%x o %X - convierte un número en Hexadecimal (con signo) depende el uso con minúscula o mayúscula.

```py
print("El número '28' es equivalente al valor '%x' en el sistema hexadecimal" % 28)
# output El número '28' es equivalente al valor '1c' en el sistema hexadecimal
print("El número '59' es equivalente al valor '%X' en el sistema hexadecimal" % 59)
# output El número '59' es equivalente al valor '3B' en el sistema hexadecimal
```

%f o %F - convierte un número aunque no tuviera dígitos después.

```py
print('%f' % 1)
# output: 1.000000
```

\


### _Formatear una cadena (string) nuevo método y recomendado_ ![](../assets/img/python\(144x144\).png)

Si bien el sistema anterior es completamente soportado por Python, el lenguaje a partir de su versión 2.6, incluye un nuevo método que pretende ser el estándar y es el más utilizado. En lugar de utilizar el operador **`'%'`** se llama a la función **format()** que es un método de la clase **'str'**.

_Ejemplo:_

```py
nombre = "Marco"
print("El {0} es el problema".format(nombre))
# output: El Marco es el problema
```

Como ves, en lugar de posicionar el operador **`'%'`** seguido del tipo de valor, simplemente se locan llaves **`'{}'`** y no es necesario indicar el tipo de dato (además el método anterior solo soportaba 3 tipos de datos: _string_, _int_, y _float_). Los datos que queremos incluir dentro de la cadena se pasan como argumento a la función **`format()`**. El numero dentro de las llaves indica la posición del argumento, empezando a contar desde cero, entonces ubicado donde corresponde.

```py
nombre = "Marco"
edad = 31
print("El {0} tiene {1} años".format(nombre, edad))
# output: El Marco tiene 31 años
```

Esto resulta bastante práctico ya que podemos alternar la cadena sin necesidad de cambiar el orden de los argumentos.

```py
nombre = "Marco"
edad = 31
print("Tienes {1} años y te llamas {0}, {0} el problema".format(nombre, edad))
# output: Tienes 31 años y te llamas Marco
```

Si te resulta más comodo, a partir de Python 2.7 puedes omitir los números dentro de las llaves. Aunque lógicamente, omitiendo las posiciones no te permitirá realizar las repeticiones.

Otra característica que añade este sistema es la posibilidad de especificar con un nombre determinado los valores que queremos incluir.

```py
print("Tu nombre es {a} y tienes {b} años".format(a="Marco", b=31))
# output: Tu nombre es Marco y tienes 31 años
```

Puedes colocar las llaves tantas veces como quieres sin necesidad de repetir los argumentos, lo que hubiese sido una limitación en el sistema anterior.

Empleando este sistema también incluye las mismas herramientas que descubrimos anteriormente. Simplemente añadimos dos puntos **`':'`** y especificamos los diversos párametros. Por ejemplo:

\
\
\


```py
for i in range(-2, 2):
    print("{0:+}".format(i))
# output: -2, -1 +0, +1
```

Existen algunas diferencias. Por ejemplo, al indicar la cantidad de caracteres que queremos imprimir como mínimo, este sistema por defecto utilizará una alineación a la izquierda, mientras que la anterior era a la derecha. Para cambiar este comportamiento utilizaremos los caracteres "<" (izquierda) y ">" (derecha). Por ejemplo:

```py
for nombre in ("Pedro", "Juan", "Diego"):
    print("{0:>9}".format(nombre))
# output: 
# ....Pedro
# .....Juan
# ....Diego
```

Empleando el caracter **`'^'`** causará que los nombres se centre.

```py
for nombre in ("Pedro", "Juan", "Diego", "Sol"):
	print("{0:^9}".format(nombre))

# output: 
# ..Pedro..
# ..Juan...
# ..Diego..
# ...Sol...
```

\
\


### _Un nuevo método en Python 3.6_ ![](../assets/img/python\(144x144\).png)

Con la idea de mejorar la legibilidad respecto a los sistemas anteriores, en Python 3.6 surgen las denominada `"f-string"` o `"cadenas-f"`. Cuando una cadena esté precedida por una **`f`**, utilizando llaves **`{}`** se podrán ubicar expresiones dentro de la misma cadena que luego serán ejecutadas.

```py
nombre = "Marco"
edad = 31
altura = 1.78
print(f"Te llamas {nombre}, tienes {edad} años y mides {altura} mts.")
# output : Te llamas Marco, tienes 31 años y mides 1.78 mts.
print(f"Tu nombre al revés es {nombre[::-1]}.")
# output : Tu nombre al revés es ocraM.
print(f"Dentro de 5 años tendrás {edad+5} años.")
# output : Dentro de 5 años tendrás 36 años.
```

Notese que son expresiones, no simples identificadores, a diferencia de los métodos anteriores. En versiones anteriores, utilizando `str.format` se intentaba emular este funcionamiento vía el siguiente código.

```py
nombre = "Marco"
edad = 31

print("Tu nombre es {nombre} y tienes {edad} años".format(**locals()))
# output : Tu nombre es Marco y tienes 31 años
```

Ya que `locals()` retorna un diccionario con los nombres de los objetos y sus respectivos valores. Volviendo al nuevo sistema también incluye las características de **str.format** con la misma sintaxys.

```python
for nombre in ("Pedro", "Juan", "Diego"):
	print(f"{nombre:>9}")
# output: 
# ....Pedro
# .....Juan
# ....Diego
```
