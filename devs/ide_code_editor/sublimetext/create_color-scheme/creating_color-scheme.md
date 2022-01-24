## Combinación de colores

Hay 2 partes de Sublime Text, la parte en la que haces tu trabajo y escribes tú código, y la parte que es la interfaz de usuario de Sublime Text en sí, por ejemplo, **la barra lateral**, **las pestañas de archivos**, etc.  

Los esquemas de color se aplican a la parte de trabajo y determinan el resaltado de código fuente y sus colores resultantes, cosas como **clases**, **funciones**, **bibliotecas**, **constantes**, lo que sea. Estos esquemas utilizan el formato **.tmTheme** (heredado) o el formato **.sublime-color-scheme** (nuevo desde la compilación 3149). Los archivos **.tmTheme** heredados utilizan el formato **XML**, mientras los **.sublime-color-scheme** usan el formato JSON.

Los temas de la interfaz de usuario tienen extensión **.sublieme-theme** y es un formato JSON que especifica reglas para hacer coincidir elementos y modificar su apariencia. 


Editor para color-scheme : http://tmtheme-editor.herokuapp.com/#!/editor/theme/Chocolate

En su lugar, podemos proceder a editar algunos de los **.tmTheme** que genera esta aplicación web, podemos ver que hay configuraciones generales y estilos de alcances individuales, y de todos los estilos son elemementos **<dict\>** anidados en un elemento **<array\>**.

La configuración global determina los colores generales para el esquema, el primer plano, el fondo y el color de intercalación. Se parece a esto:

```xml
<!-- Global settings-->
<dict>
	<key>settings</key>
	<dict>
		<!-- Color de fondo -->		
		<key>background</key>
		<string>#222222</string>
		<!-- Color de primer plano -->
		<key>foreground</key>
		<string>#EEEEEE</string>
		<!-- Color de cursor -->
		<key>caret</key>
		<string>#FFFFFF</string>
	</dict>	
</dict>
```

Todo lo que sigue s para ámbitos individuales:  

```xml
<!-- Scope styles -->
<dict>
    <key>name</key>
    <string>Comment</string>
    <key>scope</key>
    <string>comment</string>
    <key>settings</key>
    <dict>
        <key>foreground</key>
        <string>#888888</string>
    </dict>
</dict>
<dict>
    <key>name</key>
    <string>String</string>
    <key>scope</key>
    <string>string</string>
    <key>settings</key>
    <dict>
        <key>foreground</key>
        <string>#FFD500</string>
    </dict>
</dict>
```
Cada regla de stilo de alcance consta de una etiqueta <dict/> con 3 pares de etiquetas <key/> / <string/> para el nombre, el alcance y la configuración, donde la etiqueta de configuración puede contener etiquetas <key/> para el primer plano, el fondo y el estilo de fuente.


### Instala tu tema personalizado

Independientemente de si está en una máquina con **Mac** o **Windows**, vamos a **Preferences** > **Browse Packages** y esto nos abrirá la carpeta de **Temas del usuario**, coloque su archivo **.tmTheme** allí; de lo contrario, cree una carpeta con el nombre de **THEMES** y guardelo dentro de ella.


### Compartir con amigos

Algunos de mis colegas también querían probar mi tema, y podría haberles enviado el archivo **.tmTheme**, pero luego senti curiosidad por saber cómo llegaban los paquetes al **Control Packages** para empezar. Entonces, nuevamente

