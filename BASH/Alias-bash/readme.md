## ALIAS EN BASH  

**Crear un Alias**  

Para crear un alias en bash es muy sencillo. Siguiendo la siguiente sintaxys:  

```bash
alias alias_name="command_to_run"
```

Una declaración comienza con la palabra reservada **alias** seguido el nombre que se utilizará para invocarlo desde bash y despues del signo igual(=) se le asigna el comando que quieres ejecutar, el comando necesita ir entre comillas y sin espacios entre el signo igual(=) y el último caracter. Cada alias necesita ser declarado en una nueva linea.  


**Creando un alias de bash con argumentos (Bash Functions)**  

A veces, es posible que deba crear un alias que acepte uno o más argumentos. Ahí es donde las funciones de bash resultan útiles.  

La sintaxys para crear una función bash es sencilla. Pueden ser declaradas de fos formas diferentes:  

```bash
function_name () {
    [commands]
}
```

```bash
function function_name () {
    [commands]
}
```

Para pasar cualquier número de argumentos a la función bash simplemente, colóquelos justo después del nombre de la función, separados por un espacio. Los parámetros pasados $1, $2, $3, etc., correspondientes a la posición del parámetro después del nombre de la función. La variable $0 está reservada para el nombre de la función.  

Ejemplo:  

Crearemos una función bash simple que creará un directorio y luego navegará hacia él:  

```bash
mkcd()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}
```

Al igual que con los **alias**, agregue la función a su archivo **~/.bashrc** y ejecute **source ~/.bash_profile** para volver a cargar el archivo.

Ahora basta con solo ejecutar el siguiente patrón en el comando:  

```bash
mkcd new_directory
```
Si se pregunta qué son los simbolos **- -** y **&&**, aquí una breve explicación.  

- **- -**: Se asegura de no pasar accidentalmente un argumento adicional al comando. Por ejemplo, si intenta crear un directorio que comience con -(guión) sin usar, el nombre del directorio se interpretará como un argumento de comando.  
- **&&**: Asegura que el segundo comanddo se ejecute solo si el primer comando es exitoso.  


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
alias f="git fetch"
```

