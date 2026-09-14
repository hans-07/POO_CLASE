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

-- TABLA EMPRESA
CREATE TABLE empresas(
     id_empresa INT AUTO_INCREMENT,
     nombre_empresa VARCHAR(30) NOT NULL,
     web VARCHAR(255) NULL,
     correo VARCHAR(255) NULL,
     telefono VARCHAR(20) NULL,
     direccion INT NOT NULL,

     CONSTRAINT pk_empresa PRIMARY KEY (id_empresa),
     CONSTRAINT fk_empresas_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Informarcion de la biblioteca. Incluye informacion de contacto';

-- TABLA PROOVEDORES
CREATE TABLE proveedores(
    id_proovedor INT AUTO_INCREMENT,
    nombre_proovedor VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NULL,
    correo VARCHAR(255) NULL,
    empresa INT NOT NULL,

    CONSTRAINT pk_proovedor PRIMARY KEY (id_proovedor),
    CONSTRAINT fk_proovedores_empresas FOREIGN KEY (empresa) REFERENCES empresas(id_empresa)
)COMMENT = 'Almacena los datos generales e información de contacto de las empresas principales.';

-- TABLA ALMACENES
CREATE TABLE almacenes(
    id_almacen INT AUTO_INCREMENT,
    nombre_almacen VARCHAR(255) NOT NULL,
    empresa INT NOT NULL,

    CONSTRAINT pk_almacen PRIMARY KEY (id_almacen),
    CONSTRAINT fk_almacenes_empresas FOREIGN KEY (empresa) REFERENCES empresas(id_empresa)
);