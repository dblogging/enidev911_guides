# Métodos de transformación de cadenas (string)

\
Recordemos que las cadenas (\*string\*) son inmutables, por ende todos los métodos de a continuación no actuán sobre el objeto original sino que retorna uno nuevo.\


**Capitalize()** - retorna la cadena con su primera letra en mayúsculas

```py
"hola mundo".capitalize()
# output : Hola mundo
```

**Encode** - codifica la cadena con el mapa de caracteres.

```py
"python".encode("utf-8")
# output : b'python'
```

**center()**, **ljust**, **rjust()** - estos métodos alinean una cadena en el centro,a la izquierda o la derecha respectivamente.

Sintaxis: ljust (len, fillchr)

Parámetros: len: el ancho de la cadena para expandirla. fillchr (opcional): el carácter para completar el espacio restante.

```py
"python".center(10, "*")
# output:
```

**swapcase()**

```py
word = 'HeLLoW wOrD'
print(word.swapcase())
# output: hEllOw WoRd
```

**strip(), lstrip(), rstrip()**

```py
s = "     Hello World"
print(s.lstrip)
# output: HelloWorld
```
