El módulo *Tkinter* define una serie de constantes de *anchor* (anclas) que puede utilizar para controlar dónde se colocan los elementos en relación con su contexto. Por ejemplo, los anclajes pueden especificar dónde se ubica un widget dentro de un frame cuando el frame es más grande que el widget.  

Estas constantes se dan como puntos cardinales, donde el norte está hacia arriba y el oesta hacia la izquierda. Las constantes de anchor se muestran en el siguiente diagrama.  

<p align="left">
	<img src="assets/img1.png" width="280" height="280">
</p>

Por ejemplo, si crea un widget pequeño dentro de un frame grande y usa la opción `anchor = tk.SE` se colocará en la esquina inferior derecha del frame. Si usara en su lugar lugar `anchor = tk.N`, el widget estaría centrado a lo largo del borde superior.

