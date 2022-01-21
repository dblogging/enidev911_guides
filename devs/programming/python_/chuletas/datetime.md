Ejemplo 1: fecha y hora a cadena usando **strftime()**

El programa siguiente convierte un objeto `datetime` que contiene la fecha y hora actuales a diferentes formatos: 


```py
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
```



|Directiva|Significado|Ejemplo|
|---------|-----------|-------|
|%a|Nombre abreviado del día de la semana.|Dom, lun, ...|
|%A|Nombre completo del día de la semana.|Domingo Lunes, ...|
|%w|Día de la semana como número decimal.|0, 1, ..., 6|
|%d|Día del mes como decimal con relleno de ceros.|01, 02, ..., 31|
|%-d|Día del mes como número decimal.|1, 2, ..., 30|
|%b|Nombre del mes abreviado.|Ene, feb, ..., dic|
|%B|Nombre del mes completo.|Enero febrero, ...|
|%m|Mes como un número decimal con relleno de ceros.|01, 02, ..., 12|
|%-m|Mes como número decimal.|1, 2, ..., 12|
|%y|Año sin siglo como número decimal con relleno de ceros.|00, 01, ..., 99|
|%-y|Año sin siglo como número decimal.|0, 1, ..., 99|
|%Y|Año con siglo como número decimal.|2013, 2019 etc.|
|%H|Hora (reloj de 24 horas) como un número decimal con relleno de ceros.|00, 01, ..., 23|
|%-H|Hora (reloj de 24 horas) como número decimal.|0, 1, ..., 23|
|%I|Hora (reloj de 12 horas) como un número decimal con relleno de ceros.|01, 02, ..., 12|
|%-I|Hora (reloj de 12 horas) como número decimal.|1, 2, ... 12|
|%p|AM o PM de la configuración regional.|AM PM|
|%M|Minuto como un número decimal con relleno de ceros.|00, 01, ..., 59|
|%-M|Minuto como número decimal.|0, 1, ..., 59|
|%S|Segundo como un número decimal con relleno de ceros.|00, 01, ..., 59|
|%-S|Segundo como número decimal.|0, 1, ..., 59|
|%f|Microsegundos como número decimal, relleno con ceros a la izquierda.|000000 - 999999|
|%z|Desplazamiento UTC en la forma + HHMM o -HHMM.||
|%Z|Nombre de la zona horaria.||
|%j|Día del año como un número decimal con relleno de ceros.|001, 002, ..., 366|
|%-j|Día del año como número decimal.|1, 2, ..., 366|
|%U|Número de semana del año (domingo como primer día de la semana). Todos los días de un año nuevo que preceden al primer domingo se consideran de la semana 0.|00, 01, ..., 53|
|%W|Número de semana del año (el lunes como primer día de la semana). Todos los días de un año nuevo que preceden al primer lunes se consideran de la semana 0.|00, 01, ..., 53|
|%c|Representación adecuada de la fecha y hora de la configuración regional.|Lun 30 de septiembre 07:06:05 2013|
|%x|Representación de fecha apropiada de la configuración regional.|30/09/13|
|%X|Representación de tiempo apropiada de la configuración regional.|07:06:05|
|%%|Un carácter '%' literal.|%|

### ¿Como funciona strftime()?