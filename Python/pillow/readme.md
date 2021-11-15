## Instalación

```shell
pip install pillow
# o 
pip install Pillow
```
# Image

**Image** es la clase más importante de Pillow, que implementa la mayoría de las funciones de Pillow. Esta clase se utiliza principalmente para representar objetos de imagen. Hay tres formas principales de crear una instancia de esta clase:  

1. Cargar imagen desde archivo
2. Procesando otras imágenes para obtener
3. Crea una nueva imagen

## Constantes

Image.ANTIALIAS

Cuando ANTIALIAS se agregó inicialmente, era el único filtro de alta calidad basado en convoluciones. Se suponía que su nombre reflejaba esto, A partir de Pillow 2.7.0, todos los métodos de cambio de tamaño se basan en convoluciones. Todos ellos son antialias a partir de ahora. Y el nombre real del filtro ANTIALIAS es  filtro Lanczos.

Ejemplo:  

```python
image = Image.open('assets/image/image_01.png')
image_resized = image.resize((85, 85), Image.ANTIALIAS)
```



## Cambiar tamaño de la imagen

Cambiar el tamañp de la imagen usando el método **resize()**

Sintaxys:  

```python
resized_im = image.resize((width, height))
# widt and height son valores enteros los cuales se representan en pixeles
```

Ejemplo:  

```python
# una forma
image = Image.open('assets/image/image_01.png')
image = image.resize((60, 60))
# otra forma en una sola línea
image = Image.open('assets/image/image_02.png').resize((65, 65))
```

## Método close() Cerrar la imagen

Este método eliminará el objeto de imagen y liberará la memoria.

```python
image.close()
```

