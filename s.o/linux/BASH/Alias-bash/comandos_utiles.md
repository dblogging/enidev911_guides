Ver el path por separado con Python:

```bash
$ python -c "import os; print(os.environ['PATH'].replace(':', '\n'))"
```

Variación en su enfoque de python:

```bash
python -c "import sys;print(sys.argv[1].replace(':','\n'))" $PATH
```

Otra variación de Python usando una cadena cruda: 

```bash
python -c "print(r'$PATH'.replace(':', '\n'))"
```

Lo mismo con tr

```bash
tr ':' '\n' <<< "$PATH"
```