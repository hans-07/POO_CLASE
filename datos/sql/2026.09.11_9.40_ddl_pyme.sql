CREATE DATABASE IF NOT EXISTS pyme_db;
USE pyme_db;

-- TABLA CATEGORIAS
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL,
    descripcion TEXT NULL,

    CONSTRAINT pk_categorias PRIMARY KEY (id_categoria)
) COMMENT = 'Categorías de productos';

-- TABLA PROVEEDORES
CREATE TABLE proveedores (
    id_proveedor INT AUTO_INCREMENT,
    rut_proveedor VARCHAR(12) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NULL,
    email VARCHAR(255) NULL,

    CONSTRAINT pk_proveedores PRIMARY KEY (id_proveedor),
    CONSTRAINT uq_proveedores_rut UNIQUE (rut_proveedor)
) COMMENT = 'Proveedores de la empresa';

-- TABLA PRODUCTOS
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NULL,
    precio_venta DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    categoria INT NOT NULL,
    proveedor_principal INT NOT NULL,

    CONSTRAINT pk_productos PRIMARY KEY (id_producto),
    CONSTRAINT fk_productos_categorias FOREIGN KEY (categoria) REFERENCES categorias(id_categoria),
    CONSTRAINT fk_productos_proveedores FOREIGN KEY (proveedor_principal) REFERENCES proveedores(id_proveedor)
) COMMENT = 'Productos del inventario';

-- TABLA ALMACENES
CREATE TABLE almacenes (
    id_almacen INT AUTO_INCREMENT,
    nombre_almacen VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT pk_almacen PRIMARY KEY (id_almacen)
) COMMENT = 'Almacenes de la empresa';

-- TABLA UBICACION_ALMACENES
CREATE TABLE ubicacion_almacenes (
    id_ubicacion INT AUTO_INCREMENT,
    id_almacen INT NOT NULL,
    id_producto INT NOT NULL,
    stock_actual INT NOT NULL DEFAULT 0,
    stock_minimo INT NOT NULL DEFAULT 0,

    CONSTRAINT pk_ubicacion_almacen PRIMARY KEY (id_ubicacion),
    CONSTRAINT fk_ubicacion_almacenes FOREIGN KEY (id_almacen) REFERENCES almacenes(id_almacen),
    CONSTRAINT fk_ubicacion_productos FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
) COMMENT = 'Ubicación de productos en almacenes';

-- TABLA DETALLE_MOVIMIENTOS
CREATE TABLE detalle_movimientos (
    id_movimiento INT AUTO_INCREMENT,
    id_ubicacion INT NOT NULL,
    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo_movimiento VARCHAR(20) NOT NULL,
    motivo VARCHAR(255) NULL,
    cantidad INT NOT NULL,
    costo_unitario DECIMAL(10,2) NOT NULL DEFAULT 0.00,

    CONSTRAINT pk_detalle_movimientos PRIMARY KEY (id_movimiento),
    CONSTRAINT fk_detalle_ubicaciones FOREIGN KEY (id_ubicacion) REFERENCES ubicacion_almacenes(id_ubicacion)
) COMMENT = 'Detalle de movimientos de inventario';

-- TABLA ENTRADAS
CREATE TABLE entradas (
    id_entrada INT AUTO_INCREMENT,
    id_movimiento INT NOT NULL,
    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    numero_factura VARCHAR(50) NOT NULL,
    costo_total DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    observacion TEXT NULL,

    CONSTRAINT pk_entradas PRIMARY KEY (id_entrada),
    CONSTRAINT fk_entradas_movimientos FOREIGN KEY (id_movimiento) REFERENCES detalle_movimientos(id_movimiento)
) COMMENT = 'Entradas de mercadería';

-- TABLA SALIDAS
CREATE TABLE salidas (
    id_salida INT AUTO_INCREMENT,
    id_movimiento INT NOT NULL,
    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    motivo VARCHAR(255) NOT NULL,
    monto_total DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    estado_salida VARCHAR(20) NOT NULL DEFAULT 'pendiente',

    CONSTRAINT pk_salidas PRIMARY KEY (id_salida),
    CONSTRAINT fk_salidas_movimientos FOREIGN KEY (id_movimiento) REFERENCES detalle_movimientos(id_movimiento)
) COMMENT = 'Salidas de mercadería';