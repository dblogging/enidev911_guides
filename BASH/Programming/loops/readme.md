## Bucles en bash

Si tienes pocos conocimiento(o ninguno) de programación, con toda seguridad te estás preguntando que es esto de los bucles. Si fueramos Bart Simpson, la operativa en Bash sería la siguiente:  

```bash
echo 'El baño de los chicos no es un parque acuático'
echo 'El baño de los chicos no es un parque acuático'
echo 'El baño de los chicos no es un parque acuático'
...
echo 'El baño de los chicos no es un parque acuático'
```

### Bucles en Bash: While 

La primera de las estructuras que te permite realizar bucles es **While**. Siguiendo con el ejemplo de Bart, esto se podría hacer de la siguiente forma:  


```bash
i=0
while [ $i -lt 1000 ]
do
 echo 'No debo irme sin dejar un comentario en este blog'
 ((i++))
done
```

Se puede incrementar el contador **i** utilizando los dobles paréntesis. Recuerda que las operaciones matemáticas se encerraban entre parentesís dobles.  
Otra observación interesante es que tienes que inicializar la variable i, si utilizas corchetes simple. Si utilizas corchetes dobles, no necesitas inicializar la variable. Sin embargo es recomendable usar los corchetes simples por cuestiones de compatibilidad.  

Si quieres que aparezca el numero de la repitición dentro de la linea. tan solo tienes que modificar la instrucción echo por lo siguiente:  

```bash
 echo $i.- No debo irme sin dejar un comentario en este Blog
```

## Bucles en Bash: Until  

El siguiente tipo de bucle, es muy parecido al anterior. La diferencia entre ambos, estriba, en que con **while** el bucle continuará mientras se cumpla la condición. Sin embargo, en el caso de **Until** el bucle continuará **hasta que se cumpla la condición**.  

```bash
i=10
until [ $i -lt 0 ]
do
    echo $i
    ((i--))
done
```

Este es el mismo ejemplo implementado utilizando while: 

```bash
i=10
while [ $i -gt -1 ]
do
    echo $i
    ((i--))
done
```

## Bucles en Bash : For  

El funcionamiento del bucle for difiere sensiblemente de lo que has visto hasta
el momento. Aunque también puedes simular los anteriores bucles, como while y until.  

Así, para repetir el ejemplo de Bart Simpson, lo podrías hacer como sigue a continuación.  

```bash
for i in {1..100}
do
    echo $i.- No debo irme sin dejar un comentario en este Blog
done
```

Otra forma es realizar el mismo bucle es utilizando una sintaxis similar a la que se utiliza en c. Así:  

```bash
for ((i=1;i<=100;i++))
do
    echo $i.- No debo irme sin dejar un comentario en este Blog
done
```

También puedes iterar sobre cualquier otro rando. Por ejemplo, si quieres iterar sobre los archivos del directorio.  

```bash
cont=0
for i in *
do
    ((cont++))
    echo El archivo numero $cont es $i
done
```

Si quieres imprimir números pares hasta el número que le pases como argumento sería:  

```bash
read -p 'Ingresa un número: ' n
for ((i=1;i<$n;i++))
do
    if ((i%2==0))
    then
        echo $i
    fi
done
```

### Rangos   

Algo interesanteque habrás podido observar en las estructuras **for** son los rangos. Un **rango**, lo puedes expresar con un número de inicio y un número de fin. Sin embargo, Bash es lo suficientemente inteligente, como para interpretar que si el número de inicio, es mayor que el número de fin, lo que tienes que hacer es una cuenta regresiva. Así:  

- {1..1000} contará de 1 a 1000
- {1000..1} contará de 1000 a 1

Pero, no solo puedes decir que cuente de uno en uno, también puedes definir los pasos. Así:  

- {1..1000..2} contará de 1 a 1000, pero de dos en dos.
- {1000..1..-2} lo mismo que en el caso anterior, pero de forma regresiva.

Por supuesto que además de ponerlo en un bucle *for*, también lo puedes utilizar directamente en un **echo**, por ejemplo:  

```bash
echo {1..10..3}
# output: 1 4 7 10
```

## Controlando el flujo con break y continue  

Dos opciones realmente muy interesantes que tienes que controlar el flujo del programa son *break* y *continue*. Como has podido intuir, el primero te permite interrumpir el flujo y el segundo continuarlo.  

Esto te puede ser de gran utilidad por ejemplo para controlar el flujo en el caso de hacer un bucle *while infinito*.  

En el siguiente ejemplo, cuando encuentre el primer valor superior a 5 saldrá del bucle:  

```bash
i=0
while :
do
    echo $i
    ((i++))
    if [ $i -gt 5 ]
    then
        break
    fi
done
echo "Finaliza con $i"
```

