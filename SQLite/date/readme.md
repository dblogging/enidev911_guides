La función **date()** acepta una cadena de fecha y tiempo (string time) y cero más modificadores como argumentos. Devuelve una cadena de fecha en el formato YYYY-MM-DD

Sintaxis:

```sql
DATE(timestring, modifier, modifier, ...)
```

En esta sintaxis, cada modificador se usa para aplicar una transformación al valor de tiempo a su izquierda. Los modificadores se aplicande izquierda a derecha, por lo que sus órdenes son importantes. 

Por ejemplo, la siguiente declaración devuelve el último día del mes:

```sql
SELECT
	DATE('now',
		'start of month',
		'+1 month',
		'-1 day');
```

En este ejemplo:

- **now** es una cadena de tiempo que especifica la fecha actual.
- **start of month**, **+1 month** y **-1 day** son los modificadores.

La función funciona de la siguiente manera:

- Primero, **start of month** se aplica a la fecha actual especificada por la cadena que especifica que devuelve **now**, por lo que el resultado es el primer día del mes actual.
- En segundo lugar, **+1 month** se aplica al primer día del mes actual que resulta del primer día del mes siguiente.
- En tercer lugar, **-1 day** se aplica al primer día del mes siguient, lo que da como resultado el último día del mes anterior


Mas ejemplos:

Obtener la fecha actual en hora UTC.

```sql
SELECT DATE('now');
```

Obtener la fecha local actual:

```sql
SELECT DATE('now', 'localtime');
```

Restar un día de una fecha:

```sql
SELECT DATE('now', 'localtime');
```

Restar un mes de una fecha:

```python
SELECT DATE('2019-11-05', '-1 month');
```


Restar un año de una fecha:

```python
SELECT DATE('2019-11-05', '-1 year');
```








