## <u>Escape de caracteres</u> <img src="../assets/img/python(144x144).png" width="30" align="right">

Cuando use un carácter de escape, Python lo interpretará. Los caracteres de escape usarán comillas simples o dobles. Antes de que pueda usar un carácter de escape, necesitará usar una barra invertida "\\" para que Python sepa lo que esta tratando de hacer.
 

"\a" – una campana o una alerta •

```py
sound = "\a"
print(sound)
```

"\b" – salta un espacio <kbd>backspace</kbd>


```py
foo = "Hola\b bienvenido\b suscribet\b"
print(foo) # output: Hol bienvenid suscribet
```

"\t" – inserta una tabulación <kbd>Tab&nbsp;↹</kbd>

```py
t = "Tab\tTab\tTab"
print(t) # output: Tab    Tab    Tab
```

"\r" – inserta un retorno de carro

```py
s = "Primera\rSugunda Tercera"
print(s) # output: Segunda Tercera
```

"\v" – inserta una tabulación vertical (funciona con gitbash o la shell en sistemas unix)

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

<p align="center">
    Sigueme en:<br>
    <a href="https://www.facebook.com/profile.php?id=100009064421475"><img src="assets/ico/_Facebook.ico"
            width="30"></a>
    <a href="https://github.com/EniDev911"><img src="assets/ico/_Github.ico" width="30"></a>
    <a href="https://twitter.com/MarcoContreraas"><img src="assets/ico/_Twitter.ico" width="30"></a><br>
    <a href="https://www.buymeacoffee.com/9111592">
        <img src="assets/png/love_coffe.png" width="95"></a>
</p>

