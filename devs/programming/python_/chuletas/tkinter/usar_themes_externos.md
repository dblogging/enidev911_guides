Podemos cargar temas ejecutando algunos comandos tcl: 

1. Debemos decirle a tcl dónde encontrar los temas

```py
root.tk.eval("""
    set base_theme_dir /path/to/downloaded/theme/awthemes-9.2.2/

    package ifneeded awthemes 9.2.2 \
        [list source [file join $base_theme_dir awthemes.tcl]]
    package ifneeded colorutils 4.8 \
        [list source [file join $base_theme_dir colorutils.tcl]]
    package ifneeded awdark 7.7 \
        [list source [file join $base_theme_dir awdark.tcl]]
    # ... (you can add the other themes from the package if you want
    """)
```