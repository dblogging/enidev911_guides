## <u>Input - Entrada</u> <img src="../assets/img/python(144x144).png" width="30" align="right">

Los desarrolladores a menudo tienen la necesidad de interactuar con los usuarios, ya sea para obtener datos o para proporcionar algún tipo de resultado. La mayoría de los programas actuales utilizan un cuadro de diálogo como una forma de pedirle al usuario que proporcione algún tipo de entrada (*input*). Mientras que python nos proporciona dos funciones incorporadas para leer la entrada desde el teclado.

- `input(prompt)` : Para python en su versión 3.x
- `raw_input(prompt)` : Para python en su versión 2.x

>`prompt` es un argumento opcional recibe una cadena de texto para mostrar al usuario.


Esta función `input()` primero toma la entrada del usuario y luego se evalúa la expresión, lo que significa que Python identifica automáticamente si el usuario ingresó una cadena, un número o una lista. Si la entrada proporcionada no es correcta, Python genera un error de sintaxys o una excepción. Por ejemplo:

```py
val = input("Ingresa un valor: ")
print(val)
```

## Como funciona internante input() en Python

- Primero se ejecuta la función `input()`, el flujo del programa se detendrá hasta que el usuario haya dado la entrada.

- El texto o mensaje que se ingreso a la opción `prompt` muestra en la pantalla de salida para pedirle al usuario que ingrese un valor de entrada (opcional).

- Lo que sea que ingrese como entrada, la función `input()` lo convierte en una cadena, quiere decir, si ingresa un valor entero, será procesado como una cadena. Necesitará convertirlo explícitamente en un número entero en su código usando la **conversión de tipo** Ej: 

```py
num = input("Ingrese un número: ")
print(type(num))
# output: <class 'str'>
# ================================
num = int(input("Ingrese un número: "))
print(type(num))
# output: <class 'int'>
# ================================
# otra opción más legible es:
num = input("Ingrese un número: ")
print(type(int(num)))
```

<br><br><br>

## Tomando múltiples entradas del usuario en Python

En Python se pueden tomar múltiples valores o entradas en una línea mediante dos métodos:

- usando el método `split()`
- usando la comprensión de lista (list comprehension)

## Usando el método split()

Esta función ayuda obtener múltiples entradas de los usuarios rompe la entrada dada por el separador, cualquier espacio en blanco es un separador. Generalmente, los usuarios usan el método `split()` para dividir en una cadena de Python, pero se puede usar para tomar múltiples entradas. 


Sintaxis: 

```py
input().split(separator, maxplit)
```

Ejemplos: 

```py
x, y = input('Ingresa dos valores: ').split()
print('Eje x:', x)
print('Eje y:', y)
# ======== Otra forma
a, b = input('Ingresa dos valores: ').split()
print('Primer número {} y segundo número es {}'.format(a, b))
```





