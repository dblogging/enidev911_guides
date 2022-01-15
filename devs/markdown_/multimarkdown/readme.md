## Uso de MultiMarkdown

En la línea de comando:  


Verificar que tenemos instalado MultiMarkdown correctamente: 


```bash
multimarkdown --v
```


Obtener más información sobre las opciones de la línea de comandos para multimarkdown.  


```bash
multimarkdown --h
```

Una vez instalado, podemos hacer algo como lo siguiente: 


```bash
multimarkdown file.txt
# En caso de no existir nos mostrará algo parecido a:
# Error reading file 'file.txt'
```
convertirá el archivo de texto sin formato file.txt en salida XHTML. Para guardar los resultados en un archivo:


```bash
multiMarkdown file.txt > file.html
```

Un atajo para usar el modo por lotes de MultiMarkdown, que guardará la salida en el mismo nombre de archivo base que se ingresa, con la extensión .html (o .tex para salida de LaTex)


```
multimarkdown -b file.txt
```

Una ventaja del modo por lotes es que puede procesar varios archivos a la vez:  


```bash
multiMarkdown -b file.txt file2.txt file3.txt

```

También hay varios scripts de conveniencia incluidos con MultiMarkdown:  


```bash
mmd file.txt
mmd2tex file.txt
mmd2opml file.txt
mmd2odf file.txt
```


