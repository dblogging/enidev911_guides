- [Tk](#)



tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

La clase **Tk** se instancia sin argumentos. Esto crea un widget de nivel superior de Tk que suele ser la ventana principal de una aplicación. Cada instancia tiene su propio intérprete **Tcl** asociado.


tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=0)

La función **Tcl()** es una función de fábrica que crea un objeto muy parecido al creado por la clase **Tk**, excepto que no inicializa el subsistema Tk. Esto suele ser útil cuando se maneja le intérprete de Tcl en un entorno en el que no se desea crear ventanas de nivel superior extrañas, o en el que no se puede (como los sistemas Unix/Linux sin un servidor X). Un objeto creado por el objeto **Tcl()** puede tener una ventana de nivel superior creada (y el subsistema Tk inicializado) llamando a su método **loadtk()**.


```py
import tkinter as tk 

app = tk.Tcl()
app.loadtk()
app.mainloop()
```


### Conceptos importantes de Tk


Incluso este sencillo programa ilustra los siguientes conceptos clave de Tk:

**widgets**  
Una interfaz de usuario de Tkinter se compone de *widgets* individuales. Cada widget se representa como un objeto Python, crea una instancia de clases como **ttk.Frame**, **ttk.Label**, y **ttk.Button**.

**jerarquía de widgets**  
Los widgets se organizan en una *jerarquía*. La etiqueta y el botón estaban contenidos dentro de un frame, que a su vez estaba contenido dentro de la ventana raíz. Al crear cada widget *secundarios* o *hijos*, su widget *principal* se pasa como primer argumento al constructor de widget.  

**opciones de configuración**  
Los widgets tienen *opciones de configuración*, que modifican sus apariencia y comportamiento, como el texto a mostrar en una etiqueta o botón. Las diferentes clases de widgets tendrán diferentes conjuntos de opciones.  

**gestión de geometría**  
Los widgets no se agregan automáticamente a la interfaz de usuario cuando se crean. Un *administrador de geometría* como *grid* le dice a los controles de de la interfaz de usuario donde se colocan.


**bucle de eventos**  
Tkinter reacciona a la entrada del usuario, los cambios de su programa e incluso actualiza la pantalla solo cuando se ejecuta activamente un *bucle de eventos*. Si su programa no está ejecutando el ciclo de eventos, su interfaz de usuario no se actualizará.  


### Comprender cómo Tkinter envuelve Tcl/Tk

Cuando su aplicación usa las clases y métodos de Tkinter, internamente Tkinter ensambla cadenas que representan comandos **Tcl/Tk** (**T**ool-**C**ommand-**L**anguage/**T**ool-**K**it) y ejecuta esos comando en el intérprete Tcl adjunto a la instancia **Tk** de su aplicación.


Ya sea tratando de navegar por la documentación de referencia, tratando de encontrar el método o la opción correctos,  adaptando algún código existente o depurando su aplicación Tkinter, hay ocasiones en las que será útil comprender cómo se ven esos comandos **Tcl/Tk** Subyacentes.


Ejemplo de Tcl, se ejecuta `$tclsh archivo.tcl` para ilustrar el equivalente al script Tkinter anterior.


```tcl
ttk::frame .frm -padding 10
grid .frm
grid [ttk::label .frm.lbl -text "Hello World!"] -column 0 -row 0
grid [ttk::buttom .frm.btn -text "Quit"] -command "destroy ."] -column 1 -row 0
```

La sintaxis de Tcl es similar a la de muchos lenguajes de shell, donde la primera palabra es el comando que se ejecutará, seguido de los argumentos de ese comando, separados por espacios. Sin entrar en demasiados detalles, observe lo siguiente

- Los comandos utilizados para crear widgets (como `ttk::frame`) corresponden a la clases de widgets en Tkinter.
- Las opciones de widget de Tcl (como `-text`) corresponde a argumentos de palabras clave en Tkinter.
- Se hace referencia a los widgets mediante un nombre de ruta en Tcl(como ``.frm.btn`), mientras que en Tkinter no usa nombres sino referencias a objetos.
- En lugar de un widget en la jerarquía de widgets está codificado en su nombre (jerárquico), que utiliza un .(punto) como separador de ruta. El nombre de ruta para la ventana raíz es solo .(punto). Em Tkinter, la jerarquía no se define por el nombre de la ruta sino al especificar el widget principal al crear cada widget secundario.
- Las operaciones que se implementan como *command* separados en Tcl (como `grid` o `destroy`) se representan como métodos en los objetos de widget de Tkinter. Como verá en breve, en otras ocasiones, Tcl usa lo que parecen ser llamadas a métodos en objetos widget, que reflejan más de cerca lo que se usa en Tkinter.

Al buscar cómo usar una API, es útil saber el nombre exacto de la clase, la opción o el método que está usando. La introspección, ya sea en un shell de Python interactivo o con **print()**, puede ayudarlo a identificar lo que necesita.








### Utilidades para ayudar a trabajar con fuentes.


**tkinter.font** Envoltura de fuentes Tkinter

El módulo **tkinter.font** proporciona la clase **Font** para crear y usar fuentes con nomhbres.

Los diferentes pesos e inclinaciones de las fuentes son:

- tkinter.font.NORMAL
- tkinter.font.BOLD
- tkinter.font.ITALIC
- tkinter.font.ROMAN



tkinter.font.Font(root=None, font=None, name=None, exists=False, **options)

La clase **Font** representa una fuente con nombre. Las *instancias* de fuente reciben nombres únicos y se pueden especificar por su familia, tamaño y configuración de estilo. Las fuentes con nombre son el método de Tk para crear e identificar fuentes como un solo objeto, en lugar de especificar una fuente por sus atributos con cada ocurrencia.

- **argumentos**
	+ font: tupla de especificador (familia, tamaño, opciones)
	+ name: nombre de fuente único
	+ exists: apunta a la fuente nombrada existente si es verdadero
	
- **opciones adicionales de palabras clave (se ignora si se especifica la fuente):**
	+ family: familia tipográfica, es decir, Courier, Times, etc.
	+ size: tamaño de fuente:
		* Si el tamaño es positivo se interpreta como tamaño en puntos.
		* Si el tamaño es un número negativo, se trata su valor absoluto.
	+ weight: énfasis de fuente (NORMAL, BOLD)
	+ slant: (ROMAN, ITALIC)
	+ underline: subrayado de fuente (0-None, 1-uniderline)
	+ overstrike: fuente tachada - (0-None, 1-overstrike)
	

**actual**(option=None, displayof=None)  
Devuelve los atributos de la fuente.

**cget**(option)  
Recuperar un atributo de la fuente.


**config**(**options)  
Modificar atributos de la fuente.

**copy**()  
Devuelve una nueva instancia de la fuente actual.

**measure**(text, displayof=None)  
Devuelve la cantidad de espacio que ocuparía el texto en la pantalla especificada cuando se formatea en la fuente actual. Si no se especifica ninguna pantalla, se asume la ventana principal de la aplicación.  

**metrics**(*options, **kw)  
Devuelve datos específicos de la fuente. Las opciones incluyen:  

- ascent: distancia entre la línea de base y el punto más alto que un carácter de la fuente puede ocupar.
- descent: distancia entre la línea de base y el punto más bajo que un carácter de la fuente puede ocupar.
- linespace: separación vertical mínima necesaria entre dos caracteres de la fuente que asegura que no haya superposición vertical entre líneas.
- fixed: 1 si la fuente es de ancho fijo, de lo contrario 0.



tkinter.font.**families**(root=None, displayof=None)  
Devuelve las diferentes familias de las fuentes definidas.


tkinter.font.**names**(root=None)  
Devuelve los nombres de las fuentes definidas.


tkinter.font.**nametofont**(name, root=None)  
Devuelve la representación de  **Font** de una fuente con nombre de tk. 



