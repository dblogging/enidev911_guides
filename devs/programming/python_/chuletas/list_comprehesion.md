## Comprensión de listas y otras colecciones

La comprensión de lista en Python es un método sintáctico para crear listas (y por extensión también otras colecciones) a partir de los elementos de otras listas o (colecciones) de una forma rápida de escribir, muy legible y funcionalmente eficiente.


Considere la siguiente lista de lenguajes de programación


```py
languages = ["python", "c", "c++", "java"]
```

Usando la comprensión de lista, podemos crear una nueva lista con las mismas cadenas pero aplicandole una modificación (es decir, aplicar algún método de transformación de cadena como por ejemplo `capitalize()`).


```py
cap_language = [language.capitalize() for language in languages]
```

Que es funcionalmente similar a lo siguiente:


```py
cap_languages = []
for language in languages:
    cap_languages.append(language.capitalize())
```

En ambos casos, la nueva lista resulta en: 

```
['Python', 'C', 'C++', 'Java']
```

Lo interesante del primer método es que, como decíamos al principio, se escribe más rápido y se lee mejor. Por otra parte, a través de este método podríamos incluso haber trabajado sobre la misma lista, sin necesidad de duplicar la información.

```py
languages = [language.capitalize() for language in languages]
print(languages)
# ['Python', 'C', 'C++', 'Java']
```
