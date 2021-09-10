## Borrar el último commit  

Muchas veces nos sucede que realizamos un commit y después nos damos cuenta que no deberíamos haberlo hecho y necesitamos eliminarlo. ¿Como podemos eliminar el commit?  

**solución si NO hemos subido el commit a nuestro repositorio remoto(no hemos realizado push):**

1. opción:  

```bash
git reset --hard HEAD~1
```

**\-\-head:** Con esta opción estamos indicando que retrocedemos a el commit **HEAD~1** y perdemos todas las confirmaciones posteriores. **HEAD~1** es un atajo para apuntar al commit anterior al que nos encontramos. CUIDADO, con la opción **-head**, ya que se borran todos los commits posteriores al commit al que indicamos.  

2. opción:  

```bash
git reset --soft HEAD~1
```

**\-\-soft:** con esta opción estamos indicando que retrocedemos a el commit HEAD~1 y no perdemos los cambios de los commits posteriores. Todos los cambios aparecerán como pendiente para realizar un commit.  

**solución si hemos subido el commit a nuestro repositorio remoto(hemos realizado push):** 

En caso de que queramos borrar un commit que ya hemos subido al servidor remoto, la mejor opción es 


