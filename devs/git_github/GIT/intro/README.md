<h2 align="center">Introducción a GIT</h2>

## Configuración Básica

- Configurar el nombre que salen en los commits. 
```bash
    git config --global username "your_name"
```
- Confugurar Email
```bash   
    git config --global user.email your_email@mail.com
```
---

## Iniciando un repositorio

- Iniciamos GIT en la carpeta donde está el proyecto  
```bash   
    git init
```
- Añadir todos los archivos para el commit(stage area)
```bash   
    git add .
```
- Añadir un archivo especifíco al stage area
```bash   
    git add <Filename>
```
- Añadir nuestro primer commit con el prefijo "-m" 
```bash   
    git add -m "first commit"
```
- Añadir commit dentro de vim en caso de no colocar el prefijo "-m"
```bash
## Se abre el editor
## Presionamos la tecla i para escribir
Main commit
## Presionamos la tecla esc para cambiar a modo comando
## Y salimos escribiendo wq! y presionando Enter   
```

