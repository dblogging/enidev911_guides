## ¿Qué es RVM?

RVM es una herramienta que permite tener múltiples versiones de Ruby instaladas en el sistema.  

Instalaremos RVM para poder instalar una versión actualizada de Ruby, pero si en algún momento queremos probar un proyecto que necesite una versión distinta, podremos cambiar la versión sin problemas.  

Las intrucciones a continuación son abreviadas, pero si tiene algún problema puede consultar las **oficiales**.


**Instalar cURL** 

El comando cURL es una abreviatura de **Client URL** y está diseñado para transferir datos. Para instalar debemos ejecutar:  

```bash
sudo apt install curl
```


**Instalando RVM**  

Ahora vamos a instalar RVM (Ruby Version Manager), para manejar las versiones de Ruby. Además, aprovecharemos de configurar la versión de Ruby. Debemos ejecutar:  


```bash
\curl -sSL https://get.rvm.io | bash
```

**Modificando el bash**  

Debemos modificar el bash para inicar RVM cada vez que abrimos la terminal ejecutando lo siguiente:

```bash
echo 'source "$HOME/.rvm/scripts/rvm"' >> ~/.bashrc
```

**Instalando las partes de RVM que faltan**  

Despues de haber instalado RVM le pedimos a la misma herramienta que actualice e instale los programas que faltan en nuestro sistema.  

Esto lo logramos escribiendo en el terminal:  

```bash
rvm requirements
```

## Instalando Ruby

Con RVM instalado dentro del terminal escribimos:  

```bash
rvm install ruby
```



## RVM tiene un paquete dedicado en Ubuntu


**Pre-requisitos**  

Necesita **software-properties-common** instalarlo para agregar PPA repositorios.  

Si no está instalado, abrimos una terminal <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> y ejecute:  

```bash
sudo apt-get install software-properties-common
```

## 1. Agregue el PPA e instale el paquete


```bash
sudo apt-add-repository -y ppa:rael-gc/rvm
sudo apt-get update
sudo apt-get install rvm
```

** Agregue su usuario al grupo rvm ($USEER automáticamente insertará su nombre de usuario)**  


```bash
sudo usermod -a -G rvm $USER
```

## 2. Cambia la ventana de tu terminal

Ahora, para cargar siempre rvm, cambie la Terminal Gnome para que siempre realice un inicio de sesión.  

En la ventana de la terminal, haga clic en Edit> Profile Preferences, haga clic en la Title and Commandpestaña y marque Run command as login shell.


## Habilitar hemas locales


Ahora habilitar los conjuntos de gemas locales. Abra una terminal y ejecute:  

```bash
rvm user gemsets
```