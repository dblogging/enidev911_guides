### Rutas puras


|Propiedad|Descripción|
|---------|-----------|
|PurePath.**name**|Una cadena que representa el componente de ruta final, excluyendo la unidad y la raíz, si corresponde|
|PurePath.**suffix**|La extensión de archivo del componente final, si lo hay|
|PurePath.**suffixes**|Una lista de las extensiones de archivo de ruta Ej: `library.tar.gz` devolvería `['.tar', '.gz']`|
|PurePath.**stem**|El componente de ruta final, sin su sufijo|


|Método|Descripción|
|------|-----------|
|PurePath.**as_posix()**|Devuelve una representación de cadena de la ruta con barras diagonales (`/`)|
|PurePath.**is_uri()**|Representa la ruta como una `fileURI`. Se genera un [ValueError](https://www.journaldev.com/33500/python-valueerror-exception-handling-examples) si la ruta no es absoluta.|
|PurePath.**as_absolute()**|Devuelve **True** en caso de ser una ruta absoluta. Una ruta se considera absoluta si tiene una raíz y (si el sabor lo permite) una unidad.|
|PurePath.**is_relative_to(\*other)**|Devuelve **True** si la ruta es relativa a la otra ruta.|



### Rutas concretas

Las rutas concretas son subclases de **PurePath**. Además de las operaciones por este último, también proporcionan métodos para realizar llamadas al sistemas en objetos de ruta. Hay tres formas de instanciar una ruta concreta:  

- **class pathlib.Path(\*)**
Esta es una subclase de la clase `pathlib.PurePath`. Representa una ruta concreta del sistema. Al instanciar esta clase se creará un `pathlib.PosixPath` o `pathlib.WindowsPath` según corresponda.


- **class pathlib.PosixPath(\*pathsegments)**  
Esta es una subclase de la calse `pathlib.Path` y `pathlib.PurePosixPath`. Esta clase representa las rutas concretas del sistema de archivos que no son Windows.

- **class pathlib.WindowsPath(\*segmentos de ruta)**  
Esta es una subclase de la clase `pathlib.Path` y `pathlib.PureWindowsPath`. Esta clase representa las rutas concretas del sistema de archivos de Windows.


|Métodos|Descripción|
|-------|-----------|
|Path.**cwd()**|Devuelve un nuevo objeto de ruta que representa el directorio actual (tal como lo devuelve `os.getcwd()`)|
|Path.**home()**|Devuelve un nuevo objeto de ruta que representa el directorio de inicio del usuario (como lo devuelve `os.path.expanduser()` with ~construct). Si el directorio de inicio no se puede resolver se genera un [RuntimeError](https://jakevdp.github.io/WhirlwindTourOfPython/09-errors-and-exceptions.html)|
|Path.**stat(\*, follow_symlinks=True)**|Devuelve un objeto `os.stat_result` que contiene la información sobre sta ruta, como `os.stat()`. El resultado se busca en cada llamada a este método. Este método normalmente sigue enlaces simbólicos; para establecer un enlace simbólico, agregue el argumento `follow_symlinks=False` o use `lstat().` en la versión 3.10 se agrego el parámetro  follow_symlinks.|
|Path.**chmod(mode, \*, follow_symlinks=True)**|Cambie el modo de archivo y los permisos, como [os.chmod](https://docs.python.org/3/library/os.html#os.chmod). Este método normalmente sigue enlaces simbólicos. Algunas variantes de Unix admiten el cambio de permisos en el propio enlace simbólico; en estas plataformas puede agregar el argumento `follow_symlinks=False` o usar `lchmod()`.|
|Path.**exists()**|Si la ruta apunta a un archivo o directorio existente. **Nota** Si la ruta apunta a un enlace simbólico, `exists()` devuelve **True** si el enlace simbólico apunta a un archivo o directorio existente.|
|Path.**expanduser()**|Devuelve una ruta con construcciones expandidas `~y` `~user`, tal como lo devuelve `os.path.expanduser()`. Si un directorio de inicio no se puede resolver. Se genera un [RunTimeError](#).|
|Path.**glob(pattern)**|Glob el patrón relativo dado en el directorio representado por esta ruta, produciendo todos los archivos coincidentes (de cualquier tipo) Ej: `sorted(Path('.').glob('**/*.py'))`|
|Path.**group()**|Devuelve el nombre del grupo propietario del archivo. Se genera un **KeyError** si el gid del archivo no se encuentra en la base de datos del sistema.|
|Path.**is_dir()**|Devuelve **True** si la ruta apunta a un directorio (o un enlace simbólico que apunta a un directorio), **False** si apunta a otro tipo de archivo. **False** también se devuelve si la ruta no existe o es un enlace simbólico roto; se propogan otros errores (como errores de permisos).|
|Path.**is_file()**|Devuelve **True** si la ruta apunta a un archivo normal (o un enlace simbólico que apunta a un archivo normal), **False** si apunta a otro tipo de archivos. **False** también se devuelve si la ruta no existe o es un enlace simbólico roto; se propagan otros errores (como errores de permisos).|




