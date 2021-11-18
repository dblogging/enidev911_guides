
## Guía rápida de Tkinter 8.5

Esta guía rápida sirve para recordar todas las posibilidades que ofrece la librería Tkinter en su versión 8.x, describe el conjunto de widgets de Tkinter. Incluye cobertura de los widgets temáticos de ttk.

---  

A continuación sigue una lista detallada de todas las características que se pueden emplear en Tkinter.

<a name="top"></a>

## tabla de contenido

- [Tkinter](#mark)
    * [¿Que es Tkinter?](#mark-0)
    * [Definiciones](#mark-1)
    * [Una aplicación mínima](./a_minimal_application/readme.md)

- [Gestión de diseño](#mark)
	* [Método **.grid()**]()
	* [Método **.pack()**]()
	

- [Widgets](#mark0)
    * [Entry](./widgets/Entry/readme.md)
    * [Enlaces](#mark2)
    * [Parrafos](#mark3)
    * [Formato](#mark4)
    * [Citas](#mark5)
    * [Listas](#mark6)
    * [Listas de definiciones](#mark7)
    * [Imágines](#mark8)
    * [Tablas](#mark9)
    * [Código](#mark10)
    * [Lineas Horizontales](#mark11)
    * [Escapar caracteres](#mark12)
    * [Notas a pie de página](#mark13)
    * [Abreviaturas](#mark14)
    * [Indentificadores de cabecera](#mark15)
    * [Extras](#mark16)
    

### <a name="mark-0">¿Que es Tkinter?</a>

*Tkinter* es un conjunto de widgets GUI(graphical user interface) para Python, en otras palabras podriamos decir que es un creador de interfaz gráfica de usuario, es multiplataforma quiere decir que es compatible con varios sistemas operativos como Windows, Linux, MacOS.


### <a name="mark-1">Definiciones</a>

Antes de continuar, definamos algunos de los términos comunes.

**window**

Este término tiene diferentes significados en diferentes contextos, pero en general se refiere a un área rectangular en algún lugar de la pantalla de visualización.

**top-level window**

Una ventana que existe de forma independiente en su pantalla. Se decorará con su marco(Frame) y los controles estándar para el administrador de escritorio de su sistema. Puede moverlo en su escritorio. Por lo general, puede cambiar su tamaño, aunque su aplicación puede evitarlo.

**widget**

Término genérico para cualquiera de los componentes básicos que componen una aplicación en una interfaz gráfica de usuario. Ejemplos de widgets: botones de radio, campos de texto, marcos y etiquetas de texto, etc.

**frame**

En *tkinter*, el *widget Frame* es la unidad básica de organización para diseños complejos. Un *frame* es un área rectangular que puede contener otros widgets.

**child, parent**

Cuando se crea un *widget*, se crea una relación *padre-hijo*. Por ejemplo, si se coloca una etiqueta de texto dentro de un *frame*, el *frame* es el padre de la etiqueta.

---

[volver a índice](#top)

---

- <a href="./LabelFrame.md">LabelFrame</a>
- <a href="./Listbox.md">Listbox</a