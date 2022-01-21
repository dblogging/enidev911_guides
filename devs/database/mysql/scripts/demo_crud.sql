-- Crear la base de datos
CREATE SCHEMA 'demo_crud' DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
-- Crear la tabla usuarios con ID auto-incrementable
CREATE TABLE 'demo_crud'.'users'(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name_user` VARCHAR(100) NOT NULL,
	`password` VARCHAR(100) NOT NULL,
	`email` VARCHAR(100) NOT NULL,
	PRIMARY KEY(`id`)
	)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8
COLLATE=utf8_bin;


