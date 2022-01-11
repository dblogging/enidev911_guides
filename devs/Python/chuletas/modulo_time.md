### Funciones


```
time.asctime([t])
```

Convertir una tupla o **struct_time** que representa un tiempo tal como lo devuelve ``gmtime()` o `localtime()` en una cadena de la siguiente forma:

- El campo días es de dos caracteres de longitud y se rellena el espacio si el día es un solo dígito (por ejemplo: `'Sun Jun 20 23:21:05 1993''Wed Jun  9 04:26:40 1993'`) Si no se proporciona **[t\]**, se utiliza la hora actual devuelta por **localtime()**. La información de configuración regional no es utilizada por **asctime()**.


**Ejemplos**

```py
t = time.asctime()
print(t)
# output: Sun Jan  9 03:45:15 2022
```

--- 


```
time.pthread_getcpuclockid( thread_id ) 
```
Devuelve el **clk_id** del reloj de tiempo de CPU específico del subproceso para el **thread_id** especificado.

Utilice `threading.get_ident()` o el atributo `ident` del objeto `threading.Thread` para obtener un valor adecuado para thread_id.



```
time.strftime(format[, t])
```

Convierta una tupla o **struct_time** que represente una hora como devuelve `gmtime()` o `localtime()` en una cadena