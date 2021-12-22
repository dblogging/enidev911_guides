
## <u>Escape de caracteres</u> <img src="../assets/img/python(144x144).png" width="30" align="right">

Cuando use un carácter de escape, Python lo interpretará. Los caracteres de escape usarán comillas simples o dobles. Antes de que pueda usar un carácter de escape, necesitará usar una barra invertida "\\" para que Python sepa lo que esta tratando de hacer.

"\a" – una campana o una alerta

```py
sonido = "\a"
print(sonido)
```

"\b" – salta un espacio (Backspace)

```py
nombre = "Marco\b Contreras\b Herrera\b"
print(nombre) # output: Marc Contrera Herrer
```

"\t" – inserta una tabulación (Tab)

```py
nombre = "Marco\t Contreras\t Herrera"
print(nombre) # output: Marco     Contreras     Herrera
```

"\r" – inserta un retorno de carro (Return)

```py
nombre = "Marco\rContreras Herrera"
print(nombre) # output: Contreras Herrera
```

"\v" – inserta una tabulación vertical

```py
nombre = "Marco\vContreras"
print(nombre) # output bash: Marco
              #                   Contreras
              # output cmd: Marco♂Contreras
```

"\'","\"","\\" – para guardar solo una comilla simple o dobles o barra invertida

```py
frase = "/\\\"Como bien dijo Einstein: \'La estupidez humana es "+\
"infinita\'\"."
print(frase)
# output: /\"Como bien dijo Einstein, 'La estupidez humana es infinita'".
```