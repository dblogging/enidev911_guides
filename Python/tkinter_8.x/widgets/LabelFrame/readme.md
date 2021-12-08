

## El widget **LabelFrame**

El widget **LabelFrame** al igual como el widget **Frame**, es un contenedor especial, un área rectangular que puede contener otros widgets. Sin embargo, a diferencia del widget **Frame**. Sin embargo, a diferencia del widget **Frame**, el widget **LabelFrame** le permite mostrar una etíqueta como parte del borde alrededor del área.   


<p align="center">
    <img src="screenshot/01.png" alt="LabelFrame" width="650" height="130">
</p>  

Para crear un nuevo widget LabelFrame dentro de una ventana padre:  

<p align="left">

<code>
    w = tk.LabelFrame(<i>parent, option,...</i>)
</code>

</p>

El constructor retorna el nuevo widget **LabelFrame**, Options:  

## Table de opciones.

|Opción| Descripción|
|------|------------|
|**bg** o **background**| El color de fondo que se mostrará dentro del widget.|
|**bd** o **borderwidth**| Ancho del borde dibujado alrededor del perímetro del widget|
|**height**|La dimensión vertical del nuevo marco. Esto se ignorará a menos que también llame .grid_propagate(0) al marco|
|**hightlightbackground**|Color de resaltado del foco cuando el widget no tiene foco.|
|**highlightcolor**| El color de resaltado del foco cuando el widget tiene foco.|
|**labelanchor**|Esta opción para especificar la posición de la etiqueta en el borde del widget. La posición predeterminada es 'nw' (extremo izquierdo del borde superior). El siguiente diagrama muestra las nueve posiciones posibles:![](screenshot/02.png)|
|**labelwidget**|En lugar de una etiqueta de texto, puede usar cualquier widget como etiqueta pasando ese widget como el valor de esta opción|
|**padx**|Utilice esta opción para agregar relleno adicional dentro de los lados izquierdo y derecho del marco del widget. El valor está en píxeles.|
|**pady**|Utilice esta opción para agregar relleno adicional dentro de la parte inferior e superior del marco del widget. El valoe está en píxeles.|
|**relief**|Esta opción controla la apariencia del borde alrededor del exterior del widget.|


