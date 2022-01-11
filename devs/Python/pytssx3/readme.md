### Configuración

La forma correcta de instalar este módulo es clonando el repositorio e instalando a través del archivo de configuración de Python.  

o pip 

```pip
pip install pyttsx3
```

Las funciones de texto a voz de este módulo se basan en los idiomas instalados en su sistema operativo.  

Por defecto, debería venir junto con el paquete de idioma durante la instalación del sistema operativo. Debe instalar el paquete de idioma manualmente si desea utilizar otros idiomas.

### API Básica

En esta sección, exploraremos algunas de las funciones útiles proporcionadas en el módulo. Si instaló este módulo mediante el método pip, algunas de las funciones no estarán disponibles.


### importar

Comencemos con una simple declaración de importación.  

```py
import pyttsx3
```

La inicialización es bastante sencilla, solo puede escribir el siguiente código:  


```py
engine = pyttsx3.init()
```


Probamos el siguiente código para decir algo simple. Guárdelo en un archivo de Python y ejecútelo.  


```python
import pyttsx3

engine = pyttsx3.init()
engine.say('Hola me llamo marco')
engine.runAndWait()
```

### Guardar en un archivo

El desarrollador ha agregado una nueva funcionalidad para guardar la transmisión de audio en un archivo, puede llamarlo fácilmente a través de la función **save_to_file**. Asegúrese de colocarlo antes de la función `engine.runAndWait()`. 

```py
engine.save_to_file('How do you do?', 'output.mp3')
```

Primer argumento **text**

El texto para la conversión de texto a voz

Segundo argumento **filename**

El nombre del archivo. Puede utilizar la extensión mp3 o wav.

