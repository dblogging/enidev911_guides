## <u>*Métodos de transformación de cadenas (string)*</u>  <img src="../assets/img/python(144x144).png" width="30">
<br>
Recordemos que las cadenas (*string*) son inmutables, por ende todos los métodos de a continuación no actuán sobre el objeto original sino que retorna uno nuevo.
<br>

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
