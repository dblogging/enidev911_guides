Para usar restricciones de clave externa en SQLite.  

Suponiendo que la biblioteca se compila con las restricciones de clave externa habilitadas, la aplicación aún debe habilitarla en tiempo de ejecución, utilizando el comando **PRAGMA Foreign_keys.** Por ejemplo:  

```
PRAGMA Foreign_keys = ON;
```
Las restricciones de clave foranea están deshabilitada de forma predeterminada. 

