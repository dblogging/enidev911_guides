El módulo **subprocess** 

Permite generar nuevos procesos, conectarse a sus tuberías de entrada/salida/error y obtener sus códigos de retorno. Este módulo tiene la intención de remplazar varios módulos y funciones más antiguos.

**[PEP 324](https://www.python.org/dev/peps/pep-0324/)** propone el módulo subprocess 

```python
os.system
os.spawn*
```
S
Entre los métodos más comunes de **subprocess**, podemos encontrar `subprocess.call()`. Este método, suele ser útil, para ejecutar órdenes sencillas, como por ejemplo, limpiar pantalla.

```python
from subprocess import call
call('clear')
```












desaconsejado su uso para órdenes que puedan comprometer susistema.


