**Pipfile**:


```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[dev-packages]

[packages]
django = "*"

[requires]
python_version = "3.5"
```


- **source**:  nos muestra el enlace de donde se descargan los paquetes.
- **dev-packages**: aquí se registran las librerías solo para desarrollo.
- **packages**: aquí se registran todos los paquetes requeridos para el proyecto, cuando instalemos los paquetes con el comando : `pipenv install` se descarán los paquetes que fueron leidos en esta sección.

