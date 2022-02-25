# Entry

### 10. El widget Entry

El próposito de un widget Entry es permitir que el usuario vea y modifique una _sola_ línea de texto.

* Si desea mostrar _varias_ líneas de texto que se pueden editar, revisa la widget Text.

**Algunas definiciones:**

* La _selección_ es una región resaltada del texto en un **widget** **Entry**, si lo hay.

Normalmente, la selección la realiza el usuario con el ratón y el texto seleccionado se copia en el portapapeles del sistema. Sin embargo, _Tkinter_ le permite controlar si el texto seleccionado se copia o no en el portapapeles. También puede seleccionar texto en un control Entry del programa.

* El _cursor de inserción_ muestra dónde se insertará el nuevo texto. Se muestra solo cuando el usuario hace clic con el mouse en algún lugar del widget. Suele aparecer como una línea vertical parpadeante dentro del widget. Puede personalizar su apariencia de varias formas.
* Las posiciones dentro del texto mostrado del widget se dan como _índice_. Hay varias formas de especificar un índice:
  * Como índices normales de Python, comenzando desde 0
  * La constante tk.END se refiere a la posición después del texto existente.
  * La constante tk.INSERT se refiere a la posición actual del cursor de inserción.
  * La constante tk.ANCHOR se refiere al primer carácter de la selección, si hay una selección.

Para crear un nuevo widget Entry en una ventana raíz o un marco llamado _parent_:

```python
w=Tk.Entry(parent, option,...)
```

Este constructor devuelve un nuevo widget Entry. Las opciones incluyen:

| opción              | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bg o background     | El color de fondo dentro del área de entrada. El valor predeterminado es gris claro                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| bd o borderwidth    | El ancho del borde alrededor del área de entrada; el valor predeterminado son 2px                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| disabledbackground  | El color de fondo que se mostrará cuando el widget esté en estado deshabilitado (state=tk.Disabled)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| disabledforeground  | El color de primer plano que se mostraŕa cuando el widget esté en estado deshabilitado (state=tk.DISABLED)                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| exportselection     | De forma predeterminada, si selecciona texto dentro de un widget Entry, se exporta automáticamente al portapapeles. Para evitar esta exportación, utilice (exportselection=0).                                                                                                                                                                                                                                                                                                                                                                                      |
| font                | La fuente utilizada para el texto ingresado en el widget por el usuario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| highlightbackground | Color del resaltado del foco cuando el widget no tiene foco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| highlightcolor      | Color que se muestra en el resaltado del foco cuando el widget tiene **foco**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| highlightthickness  | Espesor del resaltado de **enfoque**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| insertbackground    | De forma predeterminada, el cursor de inserción es negro. Para obtener un color diferente, configúrelo asignando un color a la propiedad.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| insertofftime       | De forma predeterminada, el cursor de inserción parpadea. Puedes establecer en esta propiedad un valor en **milisegundo** para especificar cuánto tiempo pasa el cursor de inserción. El valor predeterminado es 300.                                                                                                                                                                                                                                                                                                                                               |
| insertontime        | Similar a _insertofftime_, esta opción cuánto tiempo pasa el cursor por parpadeo. El valor predeterminado es 600(milisegundos).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| insertwidth         | De forma predeterminada, el cursor de inserción tiene 2 píxeles de ancho. Puede ajustar esto estableciendo otro valor.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| justify             | Esta opción controla cómo se jutifica el texto cuando el texto no llena el ancho del widget. El valor puede ser tk.LEFT(predeterminado), tk.CENTER, tk.RIGHT.                                                                                                                                                                                                                                                                                                                                                                                                       |
| readonlybackground  | El color de fondo que se mostrará cuando la opción (state='readonly').                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| relief              | Selecciona efectos de sombreado tridimensionales alrededor de la entrada de texto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| show                | Normalmente, los caracteres que escribe el usuario aparecen en la entrada. Para hacer una entrada de "contraseña" que repita cada carácter como un asterisco, establezca show='\*'                                                                                                                                                                                                                                                                                                                                                                                  |
| state               | Utilice esta opción para deshabilitar el widget _Entry_ de modo que el usuario no pueda escribir nada en él. Úselo (state=tk.DISABLED) para deshabilitar el widget, (state=tk.NORMAL) para permitir que el usuario ingrese nuevamente. Su programa también puede averiguar si el cursor está actualmente sobre el widget interrogando esta opción; tendrá el valor tk.ACTIVE cuando el mouse esté sobre él. También puede establecer esta opción en 'disabled', que es como el (state=tk.DISABLED), pero el contenido del widget aún se puede seleccionar o copiar. |
| takefocus           | De forma predeterminada, el foco pasará por los widgets de entrada. Establezca esta opción en 0 para sacar el widget de la secuencia.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| textvariable        | Para poder recuperar el texto actual de su widget de entrada, debe establecer esta opción en una instancia de alguna clase de variables de control como _StringVar()_. Puede recuperar el texto usando _v.get()_, o configurarlo usando _v.set()_, donde _v_ es la variable de control asociada.                                                                                                                                                                                                                                                                    |
| validate            | Puede utilizar esta opción para configurar el widget de modo que su contenido sea verificado por una función de validación en determinados momentos.                                                                                                                                                                                                                                                                                                                                                                                                                |
| validatecommand     | Una devolución de llamada que valida el texto del widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| width               | El tamaño de la entrada de caracteres. El valor predeterminado es 20, para fuentes proporcionales, la longitud física del widget se basará en el ancho promedio de un carácter multiplicado por el valor de la opción width.                                                                                                                                                                                                                                                                                                                                        |
| xscrollcommand      | Si espera que los usuarios a menudo ingresen más que el tamaño en pantalla del widget, puede vincular su widget de entrada a una barra de desplazamiento. Establezca esta opción en el método **.set** de la barra de desplazamiento.                                                                                                                                                                                                                                                                                                                               |

### Los métodos sobre objetos Entry incluyen:

**.delete(**_**first**_**, **_**last=None**_**)**

Elimina caracteres del widget, comenzando con el que está en el índice _first_, hasta el carácer en la posición. Si omite el segundo argumento _first_ elimina el carácter único en la posición.

**.get()**

Devuelve el texto actual de la entrada como una cadena.

**.icursor**

Coloque el cursor de inserción justo antes del carácter _index_ dado.

**.index(**_**index**_**)**

Cambie el contenido de la entrada para que carácter dado sea _index_ el carácter más a la izquierda. No tiene ningún efecto si el texto se ajusta completamente a la entrada.

**.insert(**_**index**_**, **_**s**_**)**

Inserta una cadena _s_ antes del carácter _index_ dado.

Tk nos provee una función específica para retornar el texto seleccionado, pero haciendo uso del metodo _index()_ junto con las constantes tk.SEL\_FIRST y tk.SEL\_LAST que retornan los índices de inicio y fin de la selección podemos construirla manualmente:

```python
#!/usr/bin/env python
# python3
from tkinter import *
from tkinter import ttk

app = Tk()
entry = Entry(app)
entry.pack()

entry.insert(0, 'Hello World!')

def get_selection():
	# Comprobamos que exista una selección
	if entry.select_present():
		# Obtener los índice del inicio y fin de selección
		first = entry.index(SEL_FIRST)
		last = entry.index(SEL_LAST)
		print(entry.get()[first:last])
	else:
		print('No hay selección')

btn = ttk.Button(app, text='Get selection', command=get_selection)		
btn.pack()

app.mainloop()	
```
