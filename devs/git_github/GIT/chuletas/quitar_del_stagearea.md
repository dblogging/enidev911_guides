Por error aveces añadimos archivos que no queríamos agregar para el commit. Lo que suele pasar al usar el siguiente comando:  

```git
git add .
```

Una forma es removerlo del index con: 

```
git reset [-q][<tree-ish>][--]<paths>..
```

Esta forma restablece las entradas del "index" para todos los <paths\> a su correspondiente estado en <tree-ish\> (Esto no afecta el "working tree" ni el "branch" actual). 

Esto quiere decir que `git reset <paths>` es lo opuesto a `git add <paths>`