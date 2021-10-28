## ¿Qué es Jekyll?

Jekyll es un generador de páginas estáticas para la construcción de webs, principalmente enfocado a blogs. Está escrito en **Ruby** y desarrollado por *Tom Preston-Werner*, uno de los cofundadores de **GitHub**.   

Jekill es utilizado como el motor de creación de todas las páginas que se sirven en **GitHub Pages.**  

La idea de Jekyll no es la de utilizar una base de datos para almacenar el contenido como hacen los CMS o Gestores de Contenidos tradicionales, si no que el contenido de nuestra web se define mediante ficheros de texto en formatos markdown.

## Cómo utilizar Jekyll

Para poder empezar a trabajar con jekyll simplemente necesitamos tener instalado *Ruby* en nuestro pc. Si ya cuentas con *Ruby* puedes instalar jekyll como una gema. Es tan sencillo como ejecutar lo siguiente:  

```bash
gem install bundler jekyll
jekyll new mi-web
cd mi-web
bundle exec jekyll serve
```

## Generar sitio web

Renderizar el sitio web

```bash
jekill serve
```

Renderizar en tiempo real  

```bash
jekill serve --watch 
```

Permitir el acceso público a Internet

```bash
jekill serve --detach --host 0.0.0.0
# o 
jekill serve --force_polling -H 0.0.0.0 -P 4000
```




## Estructura de carpetas Jekill


- archivo **_config.yml**: esto es lo primero que necesita modificar. La configuración general de todo sitio web se guarda aquí, como el tema del sitio web, el nombre, la introducción, el nombre de dominio, el nombre de usuario de Github, etc.

- Carpeta **_site**: esta carpeta almacena su sitio web estático completo, pero esta es una carpeta que no necesita tocar. Es un sitio web estático generado automáticamente por Jekill en función de sus configuraciones y plantillas.  


- Carpeta **_posts**: almacena todos los archivos en formato Markdown. Todo el contenido de su blog de Markdown está aquí. También se prescribe el nombre de archivo, por ejemplo, debe ser **data-filename.md**






