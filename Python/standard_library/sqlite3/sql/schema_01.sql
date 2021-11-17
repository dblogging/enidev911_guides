CREATE TABLE proyectos(
	nombre TEXT PRIMARY KEY,
	descripcion TEXT,
	fecha_termino DATE
);

CREATE TABLE tareas(
	id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
	prioridad TEXT,
	detalle TEXT,
	estado TEXT,
	fecha_termino DATE,
	completado_el DATE,
	proyecto TEXT NOT NULL REFERENCES proyectos(nombre)
);