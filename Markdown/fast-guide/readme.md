
## Guía rápida Markdown y Pygments Lexers  

Esta guía rápida sirve para recordar todas las posibilidades que ofrecen markdown y Pygments para editar y formatear texto y comunmente empleo para crear los artículos de Blog. Espero que no solo me sirva de guía a mí, si no a cualquiera que se acerque por primera vez a markdown o Pygments.  

---  

A continuación sigue una lista detallada de todas las características que se pueden emplear en Markdown y Markdown Extra (empleando *Python Markdown*) y los lexers más comunes de Pygments para resaltar el código fuente.  

<a name="top"></a>

- [Markdown]('#')
    * [¿Que es Markdown?]('#')

- [Sintaxys Markdown]('#')
    * [Cabeceras](#mark1)
    * [Enlaces](#mark2)
    * [Parrafos](#mark3)
    * [Formato]('#')
    * [Citas]('#')
    * [Listas]('#')
    * [Listas de definiciones]('#')
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

## Markdown  

Este es el lenguaje de marcado que permite formatear el texto fácilmente sin la necesidad de emplear HTML o emplear un editor visual.  


**¿Que es Markdown?**  

Markdown es un lenguaje de marcado ligero parecido al que se emplea en muchas wikis y basado originalmente en convenciones existentes en el marcado de los correos electronicos. Emplea texto plano, procurando que sea legible pero consiguiendo que se convierte en XHTML correctamente formateado. Aunque no es muy conocido, empieza a ser muy popular y utilizado por programadores y blogueros que escriben sus artículos en este formato.  

---

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
		
[volver a índice](#top)

---

### <a name="mark3">Párrafos</a>

Para crear párrafos se deja una línea en blanco. De este mondo:  




