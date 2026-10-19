from prettytable import PrettyTable

from negocio.negocio_productos import (
    borrar_producto,
    buscar_producto_por_id,
    crear_producto,
    editar_producto,
    obtener_productos,
)


def _mostrar_tabla_productos(productos):
    tabla = PrettyTable()
    tabla.field_names = [
        'ID',
        'Nombre',
        'Descripción',
        'Precio',
        'Categoría',
        'Proveedor',
    ]
    for producto in productos:
        tabla.add_row([
            producto.id_producto,
            producto.nombre,
            producto.descripcion or '-',
            f'${float(producto.precio_venta):,.2f}',
            producto.categoria,
            producto.proveedor_principal,
        ])
    print(tabla)


def mostrar_productos():
    productos = obtener_productos()
    print('\n--- Productos ---')
    if not productos:
        print('No hay productos registrados.')
        return

    _mostrar_tabla_productos(productos)


def menu_productos():
    while True:
        print('\n=== GESTIÓN DE PRODUCTOS ===')
        print('[1] Listar productos')
        print('[2] Crear producto')
        print('[3] Actualizar producto')
        print('[4] Eliminar producto')
        print('[5] Volver')

        opcion = input('\nSeleccione una opción [1-5]: ')

        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            try:
                nombre = input('Nombre: ').strip()
                descripcion = input('Descripción: ').strip()
                precio = float(input('Precio de venta: ').strip())
                categoria = int(input('ID de categoría: ').strip())
                proveedor = int(input('ID de proveedor principal: ').strip())

                producto = crear_producto(nombre, descripcion, precio, categoria, proveedor)
                print(f'Producto creado correctamente: {producto.id_producto}')
            except ValueError as error:
                print(f'Error: {error}')
            except Exception as error:
                print(f'Error inesperado: {error}')
        elif opcion == '3':
            try:
                producto_id = int(input('ID del producto a actualizar: ').strip())
                producto = buscar_producto_por_id(producto_id)
                if producto is None:
                    print('Producto no encontrado.')
                    continue

                nombre = input(f'Nuevo nombre [{producto.nombre}]: ').strip() or producto.nombre
                descripcion = input(f'Nueva descripción [{producto.descripcion or "-"}]: ').strip()
                precio = input(f'Nuevo precio [{float(producto.precio_venta):,.2f}]: ').strip()
                categoria = input(f'Nueva categoría [{producto.categoria}]: ').strip()
                proveedor = input(f'Nuevo proveedor [{producto.proveedor_principal}]: ').strip()

                producto_actualizado = editar_producto(
                    producto_id,
                    nombre=nombre,
                    descripcion=descripcion if descripcion else producto.descripcion,
                    precio_venta=float(precio) if precio else float(producto.precio_venta),
                    categoria=int(categoria) if categoria else producto.categoria,
                    proveedor_principal=int(proveedor) if proveedor else producto.proveedor_principal,
                )
                print(f'Producto actualizado correctamente: {producto_actualizado.id_producto}')
            except ValueError:
                print('Debe ingresar valores válidos.')
            except Exception as error:
                print(f'Error inesperado: {error}')
        elif opcion == '4':
            try:
                producto_id = int(input('ID del producto a eliminar: ').strip())
                producto = buscar_producto_por_id(producto_id)
                if producto is None:
                    print('Producto no encontrado.')
                    continue

                confirmado = input(f'¿Desea eliminar el producto {producto.nombre}? (s/n): ').strip().lower()
                if confirmado != 's':
                    print('Eliminación cancelada.')
                    continue

                if borrar_producto(producto_id):
                    print('Producto eliminado correctamente.')
                else:
                    print('No se pudo eliminar el producto.')
            except ValueError:
                print('Debe ingresar un ID válido.')
        elif opcion == '5':
            return
        else:
            print('Opción inválida.')
