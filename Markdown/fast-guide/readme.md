
## Guía rápida Markdown y Pygments Lexers  

Esta guía rápida sirve para recordar todas las posibilidades que ofrecen markdown y Pygments para editar y formatear texto y comúnmente empleo para crear los artículos de Blog. Espero que no solo me sirva de guía a mí, si no a cualquiera que se acerque por primera vez a markdown o Pygments.  

---  

A continuación sigue una lista detallada de todas las características que se pueden emplear en Markdown y Markdown Extra (empleando *Python Markdown*) y los lexers más comunes de Pygments para resaltar el código fuente.  

<a name="top"></a>

- [Markdown](#mark)
    * [¿Que es Markdown?](#mark-0)

- [Sintaxys Markdown](#mark0)
    * [Cabeceras](#mark1)
    * [Enlaces](#mark2)
    * [Parrafos](#mark3)
    * [Formato](#mark4)
    * [Citas](#mark5)
    * [Listas](#mark6)
    * [Listas de definiciones](#mark7)
    * [Imágines]('#')
    * [Tablas]('#')
    * [Código]('#')
    * [Lineas Horizontales]('#')
    * [Escapar caracteres]('#')
    * [Notas a pie de página]('#')
    * [Abreviaturas]('#')
    * [Indentificadores de cabecera]('#')

- [Pygments]('#')
    - Lexers de Pygments más comunes para resaltado de sintaxis  

## <a name="mark0">Markdown</a>

Este es el lenguaje de marcado que permite formatear el texto fácilmente sin la necesidad de emplear HTML o emplear un editor visual.  

## <a name="mark-0">¿Que es Markdown?</a>

Markdown es un lenguaje de marcado ligero parecido al que se emplea en muchas wikis y basado originalmente en convenciones existentes en el marcado de los correos electronicos. Emplea texto plano, procurando que sea legible pero consiguiendo que se convierte en XHTML correctamente formateado. Aunque no es muy conocido, empieza a ser muy popular y utilizado por programadores y blogueros que escriben sus artículos en este formato.  

---

<a name="mark0"></a>
Sintaxis Markdown
-----------------  

### <a name='mark1'>Cabeceras</a>

Los encabezamintos HTML se producen colocando un número determinado de almohadillas # antes del texto correspondiente al nivel de encabezamiento deseado (HTML ofrece hasta seis niveles). Los encabezamiento posibles se puedenver en la siguiente tabla:  


<table>
	<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn"># Esto es un h1</pre>
			</td>
			<td>
				<h1>Esto es un h1</h1>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">## Esto es un h2</pre>
			</td>
			<td>
				<h2>Esto es un h2</h2>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">### Esto es un h3</pre>
			</td>
			<td>
				<h3>Esto es un h3</h3>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">#### Esto es un h4</pre>
			</td>
			<td>
				<h4>Esto es un h4</h4>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">##### Esto es un h5</pre>
			</td>
			<td>
				<h5>Esto es un h5</h5>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">###### Esto es un h6</pre>
			</td>
			<td>
				<h6>Esto es un h6</h6>
			</td>
		</tr>
	</tbody>
</table>

Se puede encerrar cada encabezado entre almohadillas, por motivos puramente estéticos, porque no es necesario en absoluto, es decir, se puede hacer esto:  


<table>
		<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">### Esto es un h3 ###</pre>
			</td>
			<td>
				<h3>Esto es un h3</h3>
			</td>
		</tr>
	</tbody>
</table>

Para los encabezamientos de los dos primeros niveles existe también otra manera de hacer lo mismo seria lo siguiente: 

<table>
		<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">Esto es un h1<br>=============</pre>
			</td>
			<td>
				<h1>Esto es un h1</h1>
			</td>
		</tr>
			<tr>
			<td>
				<pre class="no_mrkdwn">Esto es un h2<br>-------------</pre>
			</td>
			<td>
				<h2>Esto es un h2</h2>
			</td>
		</tr>
	</tbody>
</table>

Es decir para los encabezamientos principales se subraya el texto con el signo igual(=). Para los encabezamientos de segundo nivel se utilizan guiones(-) para subrayar. Es indiferente el número de signos iguales o guiones que se empleen, con uno es suficiente.

[volver a índice](#top)

---

### <a name="mark2">Enlaces</a>

Existen también dos maneras de crear enlaces, se pueden ver en la siguiente tabla:  


<table>
		<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">[Con titulo](https://eniblog.com "titulo")</pre>
			</td>
			<td>
				<a href="#mark2" title="titulo">Con titulo</a>
			</td>
		</tr>
			<tr>
			<td>
				<pre class="no_mrkdwn">[Sin titulo](https://eniblog.com)</pre>
			</td>
			<td>
				<a href="#mark2">Sin titulo</a>
			</td>
		</tr>
		</tr>
			<tr>
			<td>
				<pre class="no_mrkdwn">[Enlace 1][1], [Enlace 2][2], [Enlace 3][3]

 [1]: http://eniblog.com/tips
 [2]: http://eniblog.com/tips "Tips"
 [3]: http://eniblog.com/</pre>
			</td>
			<td>
				<a href="#mark2">Enlace1</a>,
				<a href="#mark2" title="Tips">Enlace2</a>,
				<a href="#mark2">Enlace3</a>
			</td>
		</tr> 	
	</tbody>
</table>

Existe una manera adicional de crear enlaces automáticos para direcciones URL, simplemente encerrarla entre los caracteres < que y > que:

<table>
		<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">&lt;http://eniblog.com></pre>
			</td>
			<td>
				<a href="#mark2">http://eniblog.com</a>
			</td>
		</tr>
</table>

>**Consideración**: Markdown no tiene la opción de publicar links que se abran en una nueva pestaña del navegador. Para eso habría que utilizar HTML.
		
[volver a índice](#top)

---

### <a name="mark3">Párrafos</a>

Para crear párrafos se deja una línea en blanco. De este mondo:  

<table>
		<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">Este es el primer párrado&nbsp;<br><br>Este es el segundo párrado</pre>
			</td>
			<td>
				<p>Este es el primer párrafo</p>
				<p>Este es el segundo párrafo</p>
			</td>
		</tr>
	</tbody>
</table>

Para crear un salto de línea dentro de un parráfo, simplemente se dejan dos espacios al final de la última palabra de esa línea, de este modo:  

<table>
		<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">Esta es la primera línea&nbsp;&nbsp;<br>y este es la segunda línea</pre>
			</td>
			<td>
				<p>Esta es la primera línea<br>y este es el salto de línea</p>
			</td>
		</tr>
	</tbody>
</table>

[volver a índice](#top)

---

### <a name="mark4">Formato</a>

El formato básico del texto, es decir negritas y cursivas, se pueden realizar de varias maneras:  

<table>
	<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">**Esto es negrita**</pre>
			</td>
			<td>
				<b>Esto es negrita</b>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">__Esto también es negrita__</pre>
			</td>
			<td>
				<b>Esto también es negrita</b>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">*Esto es cursiva*</pre>
			</td>
			<td>
				<i>Esto es cursiva</i>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">_Esto también es cursiva_</pre>
			</td>
			<td>
				<i>Esto también es cursiva</i>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">***Esto es negrita y cursiva***</pre>
			</td>
			<td>
				<b><i>Esto es negrita y cursiva</i></b>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">___Esto también es negrita y cursiva___</pre>
			</td>
			<td>
				<b><i>Esto también es negrita y cursiva</i></b>
			</td>
		</tr>
	</tbody>
</table>

Se pueden emplear indistintamente tanto el asterisco * como el guión bajo _ siempre y cuando no se mezclen y lo que determina el formato es el número de ellos antes y después del bloque de texto a formatear. Uno es cursiva, dos es negrita, y tres ambas a la vez, así de sencillo.

[volver a índice](#top)

---

### <a name="mark5">Citas</a>

Para crear bloques de cita, se emplea el carácter mayor que > antes del bloque de texto. En la siguiente tabla se pueden ver las opciones para crearlos:  


<table>
	<thead>
		<tr>
			<th style="width: 50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre class="no_mrkdwn">Esto es una línea normal<br><br>>Esto es parte de un bloque de cita.<br>>Esto es parte del mismo bloque de cita.</pre>
			</td>
			<td>
				<p>Esto de una línea normal</p>
				<blockquote>
				<p>Esto es parte de un bloque de cita. Esto es parte del mismo bloque de cita.</p>
				</blockquote>
			</td>
		</tr>
		<tr>
			<td>
				<pre class="no_mrkdwn">>Esto es parte de un bloque de cita. <br>Esto continúa el bloque incluso aunque no hay símbolo 'mayor que'.<br><br>La línea en blanco finaliza el bloque</pre>
			</td>
			<td>
				<blockquote>
					<p>Esto es parte de un bloque de cita. Esto continúa el bloque incluso aunque no hay símbolo 'mayor que'.</p>
				</blockquote>
				<p>La Línea en blanco finaliza el bloque</p>
			</td>
		</tr>
		<tr>
			<td>
				<pre>Esto es una línea normal<br><br>>Esto es parte de un bloque de cita.<br>>Esto es parte del mismo bloque de cita.<br>><br>>>Esto de otro bloque de cita anidado.<br>>>Esto es parte del bloque anidado. <br>><br>>Esto es parte del bloque de cita del primer nivel.
				</pre>
			</td>
			<td>
				<p>Esto es una línea normal</p>
				<blockquote>
					<p>Esto es parte de un bloque de cita. Esto es parte del mismo bloque de cita.</p> <blockquote>
						<p>Esto es otro bloque de cita anidado. Esto es parte del bloque anidado.</p>
					</blockquote>

				<p>Esto de parte del bloque de cita de primer nivel.</p>
				</blockquote>
			</td>
		</tr>
	</tbody>
</table>

[volver a índice](#top)

---

### <a name="mark6">Listas</a>

Markdown permite crear dos tipos de listas, ordenadas y desordenadas, es decir numeradas o listas de puntos. Para distinguir los tipos y como se crean, nada mejor que verlo con ejemplos:  


<table>
	<thead>
		<tr>
			<th style="width:50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre>Lista numerada (ordenada)<br><br>1. Este es el primer elemento<br>2. Este es el segundo elemento<br>3. Este es el tercer elemento
				</pre>
			</td>
			<td>
				<p>Lista numerada (ordenada)</p>
				<ol>
					<li>Este es el primer elemento</li>
					<li>Este es el segundo elemento</li		<li>Este es el tercer elemento</li>
				</ol>
			</td>
		</tr>
		<tr>
			<td>
				<pre>Lista de puntos (desordenada)<br><br>* Un elemento de la lista<br>* Otro elemento de la lista<br>* Tercer elemento de la lista</pre>
			</td>
			<td>
				<p>Lista de puntos (desordenada)</p>
				<ul>
					<li>Un elemento de la lista</li>
					<li>Otro elemento de la lista</li>
					<li>Tercer elemento de la lista</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>
				<pre>Se pueden emplear también + y -<br>en vez de *<br><br>* Un elemento de la lista<br>+ Otro elemento de la lista<br>- Tercer elemento de la lista</pre> 
			</td>
			<td>
				<p>Se pueden emplear también + y - en vez *</p>
				<ul>
					<li>Un elemento de la lista</li>
					<li>Otro elemento de la lista</li>
					<li>Tercer elemento de la lista</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>
				<pre>Se pueden mezclar distintos tipos<br>de listas y anidar unas dentro de<br>otras.<br><br>1. Esto es una lista ordenada<br>2. Segundo elemento de la lista ordenada<br>    1. Esta es una lista ordenada<br> anidada dentro de otra<br>        * Lista desordenada anidada a tercer nivel<br>        * Segundo elemento de esta lista<br>    2. Este es el segundo elemento<br>de la lista ordenada anidada</pre>
			</td>
			<td>
				<p>Se pueden mezclar distintos tipos de listas y anidar unas dentro de otras.</p>
				<ol>
					<li>Esto es una lista ordenada</li>
					<li>Segundo elemento de la lista ordenada</li>
					<ol>
						<li>Esta es una lista ordenada anidada dentro de otra</li>
						<ul>
							<li>Lista desordenada anidada a tercer nivel</li>
							<li>Segundo elemento de esta lista</li>
						</ul>
						<li>Este es el segundo elemento de la lista ordenada anidada</li>
					</ol>

				</ol>
			</td>
		</tr>
	</tbody>
</table>

[volver a índice](#top)

---

### <a name="mark7">Listas de definiciones</a>  

Se pueden crear listas de definiciones, que están compuestas de términos y las definiciones de los mismos, como si fuera un diccionario. Su creación es muy simple:  

<table>
	<thead>
		<tr>
			<th style="width:50%;">Tecleas</th>
			<th>Obtienes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<pre>Primer Termino<br> : Primera definición<br><br>Segundo termino<br> : segunda definición
				</pre>
			</td>
			<td>
				<p><b>Primer término</b><br>&nbsp;&nbsp;&nbsp;Primera definición</p>
				<p><b>Segundo término</b><br>&nbsp;&nbsp;&nbsp;Segunda definición</p>
			</td>
		</tr>
		<tr>
			<td>
			</td>
		</tr>
	</tbody>
</table>


