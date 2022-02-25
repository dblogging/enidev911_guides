# pep\_8

#### Guía de estilos para el código

#### Introducción

Este documento brinda las convenciones de escritura de código Python abarcando la librería estándar en la principal distribución de Python.

Este documento y el [PEP 257](./) (convenciones para la documentación del código) fueron adaptados del originario texto de convenciones para el código Python, por Guido van Rossum, con algunas adiciones de la guía de Barry Warsaw.

Una de las ideas claves de Guido es que el código es leído muchas más veces de lo que es escrito. Las pautas que se proveen en este documento tienen como objetivo mejorar la legibilidad del código y hacerlo consistente a través de su amplio espectro en la comunidad Python. Tal como dice el [PEP 20](./) "La legibilidad cuenta".

Una guía de estilo se trata de consistencia. La consistencia con esta guía es importante. La consistencia dentro de un proyecto es más importante. La consistencia dentro de un módulo o función es aún más importante.

Pero lo más importante: saber cuando ser inconsistente - simplemente en ciertas ocasiones la guía de estilo no se aplica. Cuando estés en duda, utiliza tu mejor criterio. Observa otros ejemplos y decide cual se ve mejor. ¡Y no dudes en preguntar!

Dos buenas razones para romper una regla en particular:

1. Cuando el aplicar la regla haga el código menos legible confuso, incluso para alguien que está acostumbrado a leer códigos que se rigen bajo las indicaciones de este documento.
2. Para ser consistente en código que también rompe (tal vez por razones históricas) - aunque esto podría ser una oportunidad para limpiar el "desastre" de otra persona.

#### Diseño del código

Usa 4 (cuatro) espacios por identación.

Para código realmente antiguo que no quieras estropear, puedes continuar usando identaciones de 8 (ocho) espacios.

Las líneas de continuación deben alinearse verticalmente con el carácter que se ha utilizado (paréntesis, llaves, corchetes) o haciendo uso de la "hanging ident" (aplicar tabulaciones en todas las líneas con excepción de la primera). Al utilizar este último método, no debe haber argumentos en la primera línea, y más tabulación debe utilizarse para que la actual se entienda como una (línea) de continuación.

**SI**

```py
# Alineado con el paréntesis que abre la función.
foo = long_function_name(var_one, var_two,
						 var_three, var_four)
# Más identación para distinguirla del resto de las líneas.
def long_function_name(
		var_one, var_two, var_three,
		var_four):
	print(var_one)
```

**NO**

```py
# Argumentos en la primera línea cuando no se está haciendo uso de la alineación vertical
foo = long_function_name(var_one, var_two,
	var_three, var_four)

# La línea de continuación no se distingue del contenido de la función
def long_function_name(
	var_one, var_two, var_three,
	var_four):
	print(var_one)
```

**OPCIONAL:**

```py
# No es necesaria la identación extra
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

El paréntesis / corchete / llave que cierre una asignación debe estar alineado con el primer carácter que no sea un espacio en blanco:

```py
my_list = [
	1, 2, 3,
	4, 5, 6,
	]
result = some_function_that_takes_arguments(
	'a', 'b', 'c',
	'd', 'e', 'f',
	)
```

\*\*O puede ser alineado con el carácter inicial de la primera línea: \*\*

```py
my_list = [
	1, 2, 3,
	4, 5, 6,
]
result = some_function_that_takes_arguments(
	'a', 'b', 'c',
	'd', 'e', 'f',
)
```

**¿Tabulaciones o espacios?**

Nunca mezcles tabulaciones y espacios.

El método de identación más popular en Python es con espacios. El segundo más popular es con tabulaciones, sin mezclar unos con otros. Cualquier código indentado con una mezcla de espacios y tabulaciones debe ser convertido a espacios exclusivamente. Al iniciar la línea de comandos del intérprete con la opción "-t", informa en modo de advertencias si se está utilizando un código que mezcla tabulaciones y espacios. Al utilizar la opción "-tt", estas advertencias se vuelven errores. ¡Estas opciones son altamente recomendadas!

Para proyectos nuevos, únicamente espacios es preferible y recomendado antes que tabulaciones. La mayoría de los editores presentan características para realizar esta tarea de manera sencilla.

#### Máxima longitud de líneas

Limita todas las líneas a un máximo de 79 caracteres.

Todavía hay varios dispositivos que limitan las líneas a 80 caracteres; más, limitado las ventanas a 80 caracteres hace posible tener varias ventanas de lado a lado. El estilo en estos dispositivos corrompe la estructura o aspecto visual del código, haciéndolo más dificultoso para comprenderlo. Por lo tanto, limita todas las líneas a 79 caracteres. En el caso de largos bloques de texto ("docstring" o comentarios), limitarlos a 72 caracteres es recomendado.

El método preferido método parar "cortar" líneas largas es utilizando la continuación implícita dentro de paréntesis. corchetes o llaves. Además, éstas pueden ser divididas en múltiples líneas envolviéndolas en paréntesis. Esto debe ser aplicado en preferencia a usar la barra invertida ("").

La barra invertida aún puede ser apropiado en diversar ocasiones. Por ejmplo, largas, múltiples sentencias **with** no pueden utilizar continuación implícita, por lo que dicho carácter es aceptable:

```py
with open('/path/to/some/file/you/want/to/read') as file_1,
\
		open('/path/to/some/file/being/written', 'w') as
file_2:
	file_2.write(file_1.read())
```

Otro caso de esta índole es la sentencia **assert**.

Asegúrate de identar la línea continuada apropiadamente. El lugar preferido para "cortar" alrededor de un operador binario es después del operador, no antes.

**Algunos ejemplos:**

```py
class Rectangle(Blob):
	def __init__(self, width, height,
				 color='black', emphasis=None, highlight=0):
		if (width == 0 and height == 0 and
			color == 'red' and emphasis == 'strong' or
			highlight > 100):
			raise ValueError("sorry, you lose")
		if width == 0 and height == 0 and (color == 'red' or
										   emphasis is 
None):
			raise ValueError("I don't think so --values are
%s, %s" %
							 (width, height))
		Blob.__init__(self, width, height,
					  color, emphasis, highlight)
```

#### Líneas en blanco

Separa funciones de alto nivel y definiciones de clase con dos líneas en blanco.

Definiciones de métodos dentro de una clase son separadas por una línea en blanco.

Líneas en blanco adicionales pueden ser utilizadas (escasamente) para separar grupos de funciones relacionadas. Se pueden omitir entre un grupo (de funciones) de una línea relacionadas (por ejempplo, un conjunto de implementaciones ficticias).

Usa líneas en blanco en funciones, escasamente, para indicar secciones lógicas.

Python acepta el carácter control-L (^L) como una espacio en blanco; muchas herramientas tratan a estos caracteres como separadores de página, por lo que puedes utilizarlos para separar páginas de secciones relacionadas en un archivo. Nota: algunos editores y visores de código basados en la web pueden no reconocer control-L como dicho carácter y mostrarán otro glifo en su lugar.

#### Codificaciones (PEP\_263)

El código en el núcleo de la distribución de Python siempre debería utilizar la codificación ASCII o Latin-1 (alias ISO-8859-1). Para python 3.0 y en adelante, UTF-8 es preferible ante Latin-1, véase PEP\_3120.

Archivos usando ASCII no deberían tener una "coding cookie" (especificación de la codificación al comienzo del archivo); de lo contrario, usar \x, \u o \U es la manera preferida para incluir carácteres que no correspondan a dicha codificación en cadenas (strings).

Para Python 3.0 y en adelante, la siguiente política es prescrita para la líbrería estándar (véase PEP\_3131): todos los identificadores en la librería estándar de Python DEBENM
