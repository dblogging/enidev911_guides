## ¿Como formatear una moneda usando Python?

**Redondear un número con la función round()**

El primer paso para formatear el número es redondearlo, una solución simple a esto se logra como parámetro el número a redonear y la cantidad de cifras decimales que queremos: 


```python
valor = 12.1736783
valor_redondeado = round(valor, 2)
print(valor_redondeado)
# output: 12.17
```

**Reemplazando un carácter de un string con el método replace()**  

Si quisieramos remplazar el "." en ",", para seguir el estándar. Para esto, podemos usar el método **replace()** de objetos string, especificando **qué** y **para qué** queremos remplazar en los parámetros, así: 

```python
valor_texto_formateado = valor_redondeado.replace('.', ',')
print(valor_texto_formateado)
```

Probando este método nos lanzaría una excepción de tipo AttributeError, debido que el tipo flotante no tiene atributos ni métodos **replace()**. Eso ocurre dado que el método **replace()** es un método de la clase string, es decir, tenemos que tranformar nuestro valor convertido de float en string. Veamos como:

```python
valor_texto_formateado = str(valor_redondeado).replace('.', ',')
print(valor_texto_formateado)
## output: 12,17
```







