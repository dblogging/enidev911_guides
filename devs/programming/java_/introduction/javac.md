### Compilador de Java - 'java'


El comando `javac` se utiliza para compilar archivos fuente de Java a archivos de código de bytes. Los archivos de bytecode son independientes de la plataforma. Esto significa que puede compilar su código en un tipo de hardware y sistema operativo, y luego ejecutar el código en cualquier otra plataforma que admita Java.

Javac viene incluido en el JDK

El compilador de Java y el resto de la cadena de herramientas estándar de Java coloca las siguientes restricciones en el código: 


- El código fuente se guarda en archivos con el sufijo ".java"
- Los códigos de bytes se guardan en archivos con el sufijo ".class"
- Para los archivos de código fuente y bytecode en el sistema de archivos, las rutas de los archivos deben reflejar el nombre del paquete y la clase.

Nota: javac compilador javac no debe confundirse con el compilador  Just In Time (JIT) que compila los códigos de bytes en código nativo.

Ejemplo simple:

```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

Podemos compilar el archivo anterior usando este comando:

```cmd
javac HelloWorld.java
```

Esto produce un archivo llamado "HelloWorld.class", que luego podemos ejecutar de la siguiente manera:

```bash
# sin añadirle la extensión .class
java HelloWorld
```

Puntos claves a tener en cuenta:

1. El nombre de archivo de origen "HelloWorld.java" debe coincidir con el nombre de la clase en el archivo de origen que  es HelloWorld. Si no coinciden, obtendrá un error de compilación.

2. El nombre de archivo "HelloWorld.class" corresponde al nombre de clase. Si tuviera que cambiar el nombre de "HelloWorld.class", obtendrá un error cuando intente ejecutarlo.

3. Al ejecutar una aplicación Java utilizando Java, debe proporcionar el nombre de clase NO el nombre de archivo de bytecode.

**Ejemplo con paquetes** 

El código Java más práctico utiliza paquetes para organizar el espacio de nombres para las clases y reducir el riesgo de colisión accidental de nombres de clases.

Si quisiéramos declarar la clase HelloWorld en un paquete, llame a `com.example`, el "HelloWorld.java" contendría la siguiente fuente Java:

```java
package com.example;

public class HelloWorld{
	public static void main(String[] args){
		System.out.println("Hello World");
	}
}
```

Este archivo de código fuente necesita almacenarse en un árbol de directorio cuya estructura corresponde a la denominación del paquete.

```
.
|
 ---com
    |
     ---example
        |
         -HelloWorld.java
```

Podemos compilar el archivo anterior usando el comando: 

```bash
javac com/example/HelloWorld.java
```

Luego podemos ejecutar la aplicación de la siguiente manera:


```
javac com.example.HelloWorld
```

Los puntos adicionales a tener en cuenta en este ejemplo son:

1. La estructura del directorio debe coincidir con la estructura del nombre del paquete.

2. Cuando ejecuta la clase, se debe proporcionar el nombre completo de la clase; es decir, "com.example.HelloWorld" no "HelloWorld".

3. No es necesario compilar y ejecutar código Java desde el directorio actual. Solo lo estamos haciendo aquí para ilustrar.


**Compilando múltiples archivos a la vez con 'javac'.**

Si su aplicación consta de varios archivos de códigos fuente (y la mayoría lo hace), puede compilarlos uno por uno. Alternativamente, puede compilar varios archivos al mismo tiempo enumerando las rutas de acceso.

```bash
javac Foo.java Bar.java
```

O usando la funcionalidad de comodín de nombre de archivo de su shell de comandos..

```bash
javac *.java
```