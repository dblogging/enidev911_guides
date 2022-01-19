### Ejemplos comandos en Pandoc.


Para crear una salida en HTML a partir de un archivo MARKDOWN. 

```cmd
pandoc readme.md -o example1.html
```


Archivo HTML independiente:


```cmd
pandoc -s MANUAL.txt -o example2.html
```


De Markdown a PDF:


```cmd
pandoc MANUAL.txt --pdf-engine=xelatex -o example13.pdf
```
