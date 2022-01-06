


**range()** es una función incorporada en Python. Devuelve una secuencia de números que comienza desce cero y se incrementa en 1 por defecto y se detiene antes del número dado.


Ahora que conocemos la definición de rango, veamos la sintaxis:

```py
range(start, stop, step)
```

- **start**: Es un parámetro **opcional** que se usa para el punto de inicio de la secuencia. Por defecto, es cero.
- **stop**: Es un parámetro **obligatorio** que se utiliza para definir el punto de parada de la secuencia.
- **step**: También es un parámetro **opcional** que se utiliza para especificar el incremento en cada iteración; de forma predeterminada, el valor es uno.

**Uso General**

Como devuelve una secuencia de números, la mayoría de los desarrolladores usan la función **range** para los bucles. Esto es útil cuando no tiene una lista o tupla, sino un valor específico para implementar el bucle.


Aquí vamos a instrumentar un bucle con solo el parámetro obligatorio **stop**:

```py
x = range(4)
for n in x:
	print(n)
# Output
# 0
# 1
# 2
# 3
```

Aquí implementaremos el bucle usando los parámetros **start** y **stop**:

```py
x = range(10, 15)
for n in x:
	print(n)
# output:
# 10
# 11
# 12
# 13
# 14
```

Ahora, vamos a utilizar los tres parámetros: **start**, **stop** y **step**.

```py
for i in range(10, 20, 2):
	print(i)
# output:
# 10
# 12
# 14
# 16
# 18
```

Junto con los bucles, **range()** también se usa para iterar sobre los tipos de lista usando la función **len()** y acceder a los valores a través de su índice.


```py
lisType = ['US', 'UK', 'China', 'India']
for i in range(len(lisType)):
	print(lisType[i])
# output:
# US
# UK
# China
# India
```


**Rango inverso**

Podemos dar número positivos o negativos para cualquiera para cualquiera de los parámetros del rango. Esta característica ofrece la oportunidad de implementar bucles inversos. Podemos hacer esto pasando un valor negativo al parámetro **step** y un valor mayor en el parámetro **start**:

```py
for i in range(10, 5, -1):
	print(i)
# output:
# 10
# 9
# 8
# 7
# 6
```


**Crear lista, conjunto y tupla usando rango**


range() es útil en muchas situaciones, en lugar de usarlo solo para escribir bucles. Por ejemplo, creamos List, Set y Tuple usando la función de rango en lugar de usar bucles para evitar el código repetitivo:


```py
print(list(range(0, 10, 2))) # Output : [0, 2, 4, 6, 8]
print(set(range(0, 10, 2))) # Output: {0, 2, 4, 6, 8}
print(tuple(range(0, 10, 2)))   #OutPut : (0, 2, 4, 6, 8)
```

Para hacerlo un poco más divertido, podemos pasar valores negativos en el parámetro **step** para crear listas de orden ascendentes. 

```py
print(list(range(10, 0, -2))) #OutPut : [10, 8, 6, 4, 2]
print(tuple(range(10, 0, -2))) #OutPut : (10, 8, 6, 4, 2)
```


**Rango de indexación**

Al igual que la forma en que accedemos a los valores en la lista usando el índice, podemos hacer lo mismo para el rango. La sintaxis también es similar a la del acceso al índice de lista.

```py
A = range(10, 100)[29]
print(A) # output: 39
```

