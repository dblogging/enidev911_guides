- **Abrir script de Python con CMD**


```json
//Python3_CMD.sublime-build
{
  	"encoding":"utf-8",
    "shell_cmd": "start cmd /C \"(C:/Users/{userName}/AppData/Local/Programs/Python/Python38/python.exe \"$file\" || set /p = Ejecución fallida. Presiona Enter para salir...) && set /p = Ejecución exitosa. Presiona Enter para salir...\"",
    "selector": "source.python",
    "working_dir": "$file_dir"
}
```