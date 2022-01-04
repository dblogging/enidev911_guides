### Función map()

Esta función trabaja de una forma muy similar a **filter()** con la diferencia que en lugar de aplicar una condición a un elemento de una lista  o secuencia, aplica una función sobre todos los elementos y como resultado se devuelve un iterable de tipo map.


```py
def doblar(numero):
	return numero*2

numeros = [2, 5, 10, 23, 20]
map(doblar, numeros)

# Dvuelve
# <map object at 0x0000027873f>
```

Facilmente podremos transformar este iterable en una lista:

```py

list(map(doblar, numeros))
```

Y podemos simplificarlo con una función **lambda** para sustituir la llamada a una función definida.

```py
list(map(lambda x: x*2, numeros))
```

La función **map()** se utiliza junto a expresiones **lambda** ya que permite ahorrarnos esl esfuerzo de crear bucles for.