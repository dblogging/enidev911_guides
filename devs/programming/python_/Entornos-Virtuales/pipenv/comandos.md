- Instalación

```bash
pip install --user pipenv
```

Nota: Esto se hace para prevenir romper cualquier paquete de sistema. Si **pipenv** no esta disponible en tu shell después de la instalación, vas a necesitar agregar la carpeta raiz de binarios del usuario a tu **PATH** en mi caso `C:\Users\home\AppData\Roaming\Python\Python38\Scripts`


- Instalar paquetes

```py
cd project
pipenv install requests
```

Ejecutando un script usando pipenv run: 

```bash
pipenv run python main.py
```


También para evitar escribir el comando tan largo podemos activar el entorno virtual simplemente con: 

```bash
pipenv shell
# ahora ejecutar el archivo
python main.py
```

Instalar las dependencias de un archivo **Pipfile**

```bash
pipenv install
```

