## El método grid()

Para mostrar un widget(w) en la pantalla de su aplicación:

Sintaxis:

```python
w.grid(option=value,...)
```

Este método registra un widget(w) con el administrador de geometría de cuadrícula; si no lo hace, el widget existirá internamente, pero no estará visible en la pantalla. Para conocer las opciones veremos la siguiente tabla: 

**Argumentos del administrador de geometría .grid()**

<table>
	<thead>
		<tr>
			<th style="width:10%;">opción</th>
			<th>descripción</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre>column</pre>
			</td>
			<td>
				<p>El número de columna donde desea que se cuadricule el widget, contando desde cero. El valor por defecto es cero.</p>
			</td>
		</tr>
		<tr>
			<td>
				<pre>columnspan</pre>
			</td>
			<td>
				<p>Normalmente, un widget ocupa solo una celda en la cuadrícula. Sin embargo, puede tomar varias celdas de una fila y combinarlas en una celda más grande configurando la opción <i>columnspan</i> en el npumero de celdas. Por ejemplo:<br><pre>w.grid(row=0, column=2, columnspan=3)</pre><br>Colocaría el widget(w) en una celda que abarque las columnas 2, 3 y 4 de la fila 0.</p>
			</td>
		</tr>
		<tr>
			<td>
				<pre>in_</pre>
			</td>
			<td>
				<p>Para registrarse como hijo de algún widget. El nuevo padre debe ser descendiente del widget utilizado cuando se creó.</p>
			</td>
		</tr>
		<tr>
			<td>
				<pre>ipadx</pre>
			</td>
			<td>
				<p>Acholchado interno en el eje x. Esta dimensión se agrega dentro del widget dentro de sus lados izquierdo y derecho.</p>
			</td>
		</tr>
	</tbody>
</table>