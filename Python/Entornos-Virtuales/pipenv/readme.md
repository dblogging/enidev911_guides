**Pipenv** es una herramienta que a punta a traer lo mejor del mundo de empaquetado.

Automáticamente crea y maneja un entorno virtual para tus proyectos, también como agregar/remover paquetes desde tu **Pipfile.lock**, que es usado para producir determinado build.

Pipenv está destinado principalmente a proporcionar a usuarios y desarrolladores de aplicaciones con un metodo sencillo para configurar un entorno de trabajo. Para la distinción entre librerias y aplicaciones y el uso de **setup.py** vs **Pipfile** para definir dependencias. mira [Pipfile vs setup.py]


También puedes hacer esto:

$ pipenv install -e .
Esto le dirá a Pipenv para hacer lock a todas tus dependencias declaradas en tu setup.py.


## Cambiando donde **Pipenv guarda los Entornos Virtuales**

Por defecto, Pipenv guarda todos sus entornos virtuales en un solo lugar. Usualmente esto no es un problema, pero si te gustaría cambiarlo para comodidad de desarrollo, o si esta causando *issues* en servidores de construcción puedes setear la variable **PIPENV_VENV_IN_PROJECT** para crear un entorno virtual dentro de la raíz de tu proyecto.




## Cambiando la versión por defecto de Python

 
Por defecto, Pipenv inicializará un proyecto usando cualquier versión de python que tenga python3. Además de iniciar un proyecto con las banderas --three o --two, también puedes usar PIPENV_DEFAULT_PYTHON_VERSION para especificar cual versión usa cuando se inicie un proyecto y --three o --two no son usados.