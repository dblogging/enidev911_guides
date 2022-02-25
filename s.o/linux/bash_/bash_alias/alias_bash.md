# ALIAS EN BASH

\


Cuando nos encontramos a menudo escribiendo comandos muy largo en la línea de comandos o buscando en el historial un comando escrito previamente. Los **alias de Bash** nos permiten establecer un comando de acceso memorable para un comando más largo.

Los atajos de bash son esencialmente atajos que nos evitan que tengamos que recordar comandos largos y eliminar una gran cantidad de escritura cuando está trabajando con la línea de comandos además de que copiar el mismo comando tantas veces puede reducir la productividad y puede distraerte de lo que realmente estás haciendo. Y como dijo el considerado el fundador de EE.UU Ben Franklin el "el tiempo es oro".

Primero que nada, vamos hacer una breve explicación de cuales son los archivos que debemos manipular para que se habiliten nuestros **alias**. Existen en linux 4 archivos que tienen algo en común pero que afectan de manera diferente las sesiones o instancias de bash, estos archivos son:

* _\~/.bashrc_
* _\~/bash\_profile_
* _/etc/bashrc_
* _/etc/profile_

**Estos archivos tienen en común:**

* Son ficheros de texto.
* Se pueden modificar con cualquier editor de texto.
* Son **shell scripts**. También llamados guiones o archivos por lotes. (Lo que en windows son los archivos \*.bat o \*.cmd pero mucho más potente)
* Son ficheros que el sistema operativo ejecuta de forma automática cuando se da una cierta condición.
* En el fondo lo que hace el sistema operativo es mandar a bash (el programa interprete de comandos más usual de Linux) ejecutar ejecutar los archivos.
* Podemos incluir en ellos cualquier orden de la línea de comandos.

**Estos archivos difieren en:**

* Solo existe una copia de los archivos **/etc/profile** y **/etc/bashrc**
* cada usuario tiene su propia copia de los archivos **.bashrc** y **.bash\_profile**. (Estos archivos se encuentran en el directorio personal de cada usuario (\~)). El punto que precede los nombres hace que estos archivos sean ocultos. Para comprobar la existencia de estos archivos ejecuta el siguiente comando: `ls -a ~`
* Los archivos **/etc/profile** y **/etc/bashrc** afectan a todos los usuarios. Por tanto son gestionados por el administrador del sistema (root).
* Como cada usuario tiene su propia copia de los archivos **.bashrc** y **.bash\_profile**, su copia le pertenece y se la puede autogestionar. Para acceder a su archivo podemos ingresar con nano o vim ejemplo: `vi ~/.bashrc` p `nano ~/.bash_profile`.

Veremos algo parecido a esto:

```bash
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH
unset USERNAME
```

**Lo más importante. Cual de ellos utilizar:**

Podemos clasificar estos cuatro archivos en función de si los comandos que contienen afectan a un solo usuario o contrariamente a todos los usuarios del sistema se ven afectados.

**Para todos los usuarios**: (Se necesita permisos de root para editar/modificar estos archivos)

**/etc/profile** --> Se ejecuta cuando qualquier usuario inicia la sesión.

**/etc/bashrc** --> Se ejecuta cada vez que qualquier usuario ejecuta el programa bash

**Para nuestro usuario:**

**\~/.bash\_profile** --> Se ejecuta el .bash\_profile de fulanito cuando fulanito inicia su sesión.

**\~/.bashrc** --> Se ejecuta el .bashrc de juanito cuando juanito ejecuta el programa bash.

Explicado esto, debemos tener en cuenta que si hemos hecho modificaciones en los archivos y queremos que los cambios surtan efecto inmediatamente, sin necesidad de reiniciar la sesión del usuario, ejecutaremos alguno de los comandos siguientes:

* Recargar el archivo a nivel usuario

```bash
source ~/.bashrc
```

* Para recargar los archivos que afectan a nivel general

```bash
sudo source /etc/bashrc
# o ya sea 
sudo source /etc/bash.bashrc
```

## _Crear un Alias_

Para crear un alias en bash es muy sencillo. Siguiendo la siguiente sintaxis:

```bash
alias alias_name="command_to_run"
```

Una declaración comienza con la palabra reservada **alias** seguido el nombre que se utilizará para invocarlo desde bash y despues del signo igual `=` se le asigna el comando que quieres ejecutar, el comando necesita ir entre comillas `''`y sin espacios entre el signo igual `=` y el último caracter. Cada alias necesita ser declarado en una nueva linea.

Podemos crear dos tipos de **alias**:

* **temporales**
* **permanentes**

## _Creación de alias temporales_

Lo que debemos hacer es escribir la palabra alias en la terminal. Después tendremos que utilizar el nombre que queremos usar para ejecutar un comando. Esto irá seguido por el signo '`=`' y la llamada al comando que queremos utilizar.

Ejemplo:

```bash
alias etc="ls /etc"
```

Una vez definido vamos a poder utilizarlo. El problema con este acceso directo es que **solo estará disponible para tu sesión de terminal actual**. Además podemos eliminar estos alias en la sesión actual con el siguiente comando:

```bash
unalias alias_name
# o el siguiente elimina todos los alias temporales #
unalias -a 
```

## _Creación de alias permanentes_

Para mantener los alias entre sesiones, vamos a tener que editar algunos de los archivos que vimos anteriormente. Dentro del archivo, busca un lugar en el archivo donde agregar los **alias**. Un buen lugar para agregarlos suele ser al final del archivo. Para propósitos de organización, podemos dejar un comentario antes:

![](../assets/img/ex\_alias.png)

El siguiente comando nos listará nuestro alias disponibes en **bash** también nos funcionará si usamos el emulador de shell **git bash** en windows.

![](../assets/img/ex\_output\_alias.png)

## Creando un alias de bash con argumentos (Bash Functions)

\


A veces, es posible que deba crear un alias que acepte uno o más argumentos. Ahí es donde las funciones de bash resultan útiles.

La sintaxys para crear una función bash es sencilla. Pueden ser declaradas de fos formas diferentes:

```bash
function_name () {
    [commands]
}
## o también:
function function_name () {
    [commands]
}

## aquí el formato de una sola línea:
function_name () { commands; }
function function_name { commands; }
```

Algunos puntos a destacar:

* Los comandos entre llaves '`{}`' se denominan cuerpo de la función. Las llaves deben estar separadas del cuerpo por espacios o líneas nuevas.
* Definir una función no la ejecuta. Para invocar una función bash, simplemente use el nombre de la función. Los comandos entre llaves se ejecutan siempre que se llama a la función en el script de shell.
* La definición de la función debe colocarse antes de cualquier llamada a la función.
* Cuando se utiliza funciones "compactadas" de una sola líneam un punto y coma '`;`' debe seguir al último comando de la función.
* Intente siempre que los nombres de sus funciones sean descriptivos.

Para entender esto mejor, eche un vistazo al siguiente ejemplo:

```bash
#!/bin/bash
hello_world(){
	echo 'hello, world'
}
```

Analicemos el código línea por línea:

* En la línea 2, definimos la función dandole un nombre. La llave '`{`' marca el inicio del cuerpo de la función.
* La línea 3 es el cuerpo de la función. El cuerpo de la función puede contener varios comandos, declaraciones y declaraciones de variables.
* La línea 4, el corchete de cierre '`}`', define el final de la función.

**Alcances de las variables**

Las variables globales son variables a las que se puede acceder desde cualquier lugar del script, independientemente del alcance. En Bash, todas las variables por defecto se definen como globales, incluso si se declaran dentro de la función.

Las variables locales se pueden declarar dentro del cuerpo de la función con la palabra clave '`local`' y solo se pueden usar dentro de la función. Puede tener variables locales con el mismo nombre en diferentes funciones.

Para ilustar mejor cómo funciona el alcance de las variables en Bash, consideremos este ejemplo:

```bash
#!/bin/bash

var1='A'
var2='B'

my_function(){
	local var1='C'
	var2='D'
	echo "Dentro de la función: var1: $var1, var2: $var2"
}

echo "Antes de ejecutar la función: var1: $var1, var2: $var2"

my_function

echo "Despues de ejecutar la función: var1: $var1, var2: $var2"
```

El script comienza definiendo dos variables globales `var1` y `var2`. Luego hay una función que establece una variable local `var1` y modifica la variable global`var2`.

Si ejecutamos el script, debería ver el siguiente resultado:

![](../assets/img/ex\_output\_function.png)

**Valores devueltos**

A diferencia de los lenguajes de programación "reales", las funciones Bash no le permite devolver un valor cuando se las llama. Cuando se completa una función bash, su valor de retorno es el estado de la última instrucción ejecutada en la función, sería algunos de los siguientes valores:

* 0 : para indicar que todo se ejecuto con exito.
* 1 - 255: un número decimal distinto a 0 para el fracaso.

El estado de retorno se puede especificar mediante la palabra clave `return` y se asigna a la variable `$?`. La declaración `return` termina la función.

```bash
#!/bin/bash
my_function(){
	echo "some result"
	return 101
}

my_function
echo $?
```

Para devolver un valor arbitrario de una función, necesitamos usar otros métodos. La opción más simple es asignar el resultado de la función a una variable global:

```bash
#!/bin/bash
my_function(){
	func_result=20
}

my_function

echo $func_result
```

Otra mejor opción para devolver un valor de una función es enviar el valor `stdout` usando `echo` o `printf` como se muestra a continuación.

```bash
#!/bin/bash

my_function(){
	local func_result="some result"
	echo "$func_result"
}

func_result="$(my_function)"
echo $func_result
```

En lugar de simplemente ejecutar la función que imprimirá el mensaje en stdout, estamos asignando la salida de la función a la variable `func_result` usando la `$()` sustitución del comando. La variable se puede utilizar posteriormente según sea necesario.

Para pasar cualquier número de argumentos a la función bash simplemente, colóquelos justo después del nombre de la función, separados por un espacio. Los parámetros pasados deben respetar la siguiente regla:

* $1, $2, $3, etc. Correspondientes a la posición del parámetro después del nombre de la función. La variable $0 está reservada para el nombre de la función.

Ejemplo:

Crearemos una función bash simple que creará un directorio y luego navegará hacia él:

```bash
#.bashrc
mkcd()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}
```

Al igual que con los **alias**, agregue la función a su archivo **\~/.bashrc** y ejecute **source \~/.bash\_profile** para volver a cargar el archivo.

Ahora basta con solo ejecutar el siguiente patrón en el comando:

```bash
mkcd new_directory
```

Si se pregunta qué son los simbolos **- -** y **&&**, aquí una breve explicación.

* **- -**: Se asegura de no pasar accidentalmente un argumento adicional al comando. Por ejemplo, si intenta crear un directorio que comience con guión `-` sin usar, el nombre del directorio se interpretará como un argumento de comando.
* **&&**: Asegura que el segundo comando se ejecute solo si el primer comando es exitoso.

Algunos ejemplos de mis alias:

Para GIT:

```
#.bashrc
# MY ALIAS GIT
alias c="git clone"
alias s="git status"
alias v="git remote -v"
alias ci="git commit -m"
alias a="git add ."
alias p="git push origin"
alias pl="git pull"
alias f="git fetch"
alias l="git log"
```
