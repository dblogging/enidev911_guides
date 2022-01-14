<h2 align="center"><u>Cómo crear un CRUD en python</u></h2>



```py
import os 
import time
```

- **os**: Librería que nos proporciona funcionalidades del sistema
- **time**: Módulo que proporciona funciones relacionada con el tiempo

Después definimos una función que nos muestra las opciones del crud.

```py

def print_option():
    print('CRUD PYTHON')
    print('*' * 20)
    print('Selecciona una opción:')
    print('[C]rear')
    print('[L]istado')
    print('[M]odificar')
    print('[E]liminar')
    print('[B]uscar')
    print('[S]alir')
```