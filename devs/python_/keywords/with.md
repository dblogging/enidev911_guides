La declaración **with** en Python es una herramienta bastante útil para administrar adecuadamente los recursos externos en sus programas. Le permite aprovechar los **administradores de contexto** existente para manejar automáticamente las fases de configuracíon y desmontaje siempre que esté tratando con recursos externos o con operaciones que requieran esas fases.

Además, el protocolo de administración de contexto le permite crear sus propios administradores de contexto para que pueda personalizar la forma en que maneja los recursos del sistema.

Con este conocimiento, escribirá código más expresivo y evitará perdidas de recursos en sus programas. La declaración **with** lo ayuda a implementar algunos patrones comunes de administración de recursos al abstraer su funcionalidad y permite que se eliminen y reutilicen.  

### Gestión de recursos en Python

Una problema común que enfrentará en la programación es cómo administrar adecuadamente **los recursos externos**, como archivos, bloqueos y conexiones de red. A veces, un programa retendrá esos recursos para siempre, incluso si ya no lo necesita. Este tipo de problema se denomina pérdida de memoria porque la memoria disponible se reduce cada vez que crea y abre una nueva instancia de un recurso determinado sin cerrar una existente.  

La gestión adecuada de los recursos suele ser un problema complicado. Requiere tanto una fase de preparación como una fase de desmontaje. La última fase requiere que realice algunas acciones de limpieza, como cerrar un archivo
