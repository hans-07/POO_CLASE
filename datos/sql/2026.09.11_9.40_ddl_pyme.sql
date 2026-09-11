CREATE DATABASE pyme_db;
USE pyme_db;

-- TABLA COMUNAS
CREATE TABLE comunas(
    id_comuna INT AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL,
    comuna VARCHAR(30) NOT NULL,

    CONSTRAINT pk_comunas PRIMARY KEY (id_comuna)
) COMMENT = 'Listado de comunas de Chile de acuerdo a SUBDERE.';

-- TABLA DIRECCIÓN
CREATE TABLE direcciones (
    id_direccion INT AUTO_INCREMENT,
    comuna INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    departamento VARCHAR(10) NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (comuna) REFERENCES comunas (id_comuna)
) COMMENT = 'Tabla para guardar direcciones asociadas a la empresa, proveedores';