### <u>Configurar llaves SSH en Git y Github</u>

**¿Para que necesitamos la criptografía asimétrica?** 

Cuando enviamos datos por internet, ya sea una imagen, un archivo o sólo mensajes, corremos el riesgos de que nos roben nuestra información en el intento, antes de que llegue al receptor.


**¿Qué es la criptografía asimétrica?**  

La criptografía asimétrica es la forma segura de enviar y recibir un mensaje, ya que si incluso llega a ser interceptado, nunca podrá leer el mensaje.


**¿Como funciona?**

En este caso, Juan le quiere mandar un mensaje a Ana, ambos cuentan con una llave pública y una privada que están ligadas con un algoritmo matemático, Ana le da a Juan su llave pública y Ana conserva su llave privada, Juan manda su mensaje cifrado con la llave pública que le proporciona Ana, Ana recibe el mensaje de Juan y lo desencripta con su llave privada de esta manera Ana y sólo Ana podrá leer el mensaje que le envió Juan.


<p align="center">
    <img src="img_ssh/example_use.png" alt="example use">
</p>



En la línea de comandos para Linux, MacOSX y en Git Bash en Windows, puede generar una clave SSH.  

Comience creando una nueva clave, usando su correo electrónico como etiqueta:

    ssh-keygen -t rsa -b 4096 -C "user@email.com"

- **-t rsa**: Aquí especificamos el algoritmo de encriptación que queremos en este caso el más común es **rsa**
- **-b 4096**: Aquí especificamos que tan compleja es la llave.
- **-C `"user@email.com"`**: Aquí colocamos el email que se va a configurar la llave.

Se le pedirá lo siguiente a través de esta creación:

    Enter file in which to save the key (/c/Users/user/.ssh/id_rsa):

Seleccione una ubicación de archivo o presione enter se creara en la dirección por defecto **/c/Users/Enidev/.ssh/id_rsa**.  

Ingresar una frase de contraseña segura creará una capa adicional de seguridad. Evitar que cualquier persona que obtenga acceso a la pc use esa clave sin la frase de contraseña. Sin embargo, será necesario que proporcione la frase de contraseña cada vez que se utilice la clave SSH.  


```bash
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
Ejemplo:  

<p align="center">
    <img src="img_ssh/01_ssh.png" alt="create pair-key">
</p>


## Agregar al SSH-Agent

Antes de agregar una nueva clave SSH al [SSH-Agent](https://en.wikipedia.org/wiki/Ssh-agent) para gestionar tus claves, debes haber comprobado las claves SSH existente y generado una nueva clave SSH.

En Unix, la comunicación con el agente es a través de una canalización con nombre cuyo nombre de archivo se almacena en una variable de entorno. 


```bash
ssh-agente $SHELL
```

donde $SHELL es la variable de entorno que contiene el nombre de su shell de inicio de sesión. Alternativamente, puede proporcionar el nombre de cualquier otro shell, como [csh](https://es.wikipedia.org/wiki/C_Shell), [zsh](https://es.wikipedia.org/wiki/Zsh), etc. 


1. Verifica que el ssh-agent se esté ejecutando. 


```bash
# correr el ssh-agent en segundo plano
$eval $(ssh-agent -s)
> Agent pid 1412
```

- **eval**: Ejecuta un comando de shell y efectua una doble evaluación en la línea de comandos.



**Ejemplo:**

<p align="center">
    <img src="img_ssh/02_ssh-agent.png" alt="ssh-agent" width="600" height="250">
</p>

2. Agrega tu llave privada SSH al ssh-agent. Si creaste tu llave con un nombre distinto, o si estás agregando una llave existente que tiene un nombre distinto, remplaza **id_rsa** en el comando con el nombre de tu llave.  

```bash
ssh-add /Users/user/.ssh/id_rsa
```

**Ejemplo:**

<p align="center">
    <img src="img_ssh/03_ssh-agent.png" alt="ssh-agent" >
</p>  

Ahora el par de claves SSH está listo para usarse.  

## Agregar una clave SSH nueva a tu cuenta de GitHub.

1. Copia la clave SSH a tu portapapeles. 

Si tu archivo de clave SSH tiene un nombre diferente al código del ejemplo, modifica el nombre de archivo. Al copiar tu clave, no agregues líneas nuevas o espacios en blanco.  


```bash
# copiar el contenido de la clave pública al portapapeles.
clip < ~/.ssh/id_rsa.pub
```

- **~**: es un símbolo llamado virgulilla que en los sistemas operativos UNIX se refiere al valor de la variable $HOME, esto es, el directorio del usuario que está logueado.

**Ejemplo:**

<p align="center">
    <img src="img_ssh/04_copy_key.png" alt="copy key" width="600" height="250">
</p>  


2. En la esquina superior derecha de nuestra página en [GitHub](https://github.com/), das clic en tu foto de perfil y despues da clic en Configuración.


<p align="center">
    <img src="img_ssh/05_settings.png" alt="settings" width="350" height="550" >
</p> 

3. En la barra laterar de configuración de usuario, da clic en LLaves SSH y GPG.  


<p align="center">
    <img src="img_ssh/06_settings_ssh.png" alt="settings" width="600" height="300">
</p>  


4. Haz clic en **New SSH key** o **Add SSH key**.

<p align="center">
    <img src="img_ssh/07_add_ssh.png" alt="add shh" width="800" height="280">
</p>

5. En el campo "Title" (Título), agrega una etiqueta descriptiva para la clave nueva. Por ejemplo, si estás usando tu Mac personal, es posible que llames a esta tecla "Personal MacBook Air".
Copia tu clave en el campo "Key" (Clave).

<p align="center">
    <img src="img_ssh/08_paste_ssh.png" alt="paste" width="850" height="500">
</p>


<p align="center">
    <img src="img_ssh/09_paste_ssh.png" alt="paste" width="850" height="500">
</p>


6. Si se te solicita, confirma tu contraseña GitHub.

<p align="center">
    <img src="img_ssh/10_corfim.png" alt="corfim" width="450" height="500">
</p>

Ya se esta lista nuestra llave para poder utilizarla con GitHub.

## Probar la conexión SSH a GitHub

Ahora podemos probar nuestra conexión a través de SSH a GitHub  

```bash
ssh -T git@github.com
```
<p align="center">
    <img src="img_ssh/11_validate.png" alt="validate" width="850" height="550">
</p>

Si la última línea contiene su nombre de usuario en GitHub, ¡está autenticado correctamente!.




