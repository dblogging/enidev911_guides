

Esta librería es un [wrapper](https://es.wikipedia.org/wiki/Wrapper) para tkinter. Estp significa que ofrece una forma más sencilla de utilizar la librería estándar de Python.  

**Instalación**

```bash
pip install guizero
```

Todos los proyectos de guizero comienzan con una ventana principal qie es un widget contenedor llamado **App**. Al final de cada programa debemos indicar al programa que muestra la aplicación:  

```python
app = App(title="Hello World") 
app.display()
```


**Agregar widgets**  

Los widgets son las cosas que aparecen en una [GUI](https://es.wikipedia.org/wiki/Interfaz_gr%C3%A1fica_de_usuario) como cuadro de textos, botones, controles deslizantes e inclusos los textos. Todos los widgets van entre la línea de creación de l aplicación `app = App()` y la línea `app.display()`

