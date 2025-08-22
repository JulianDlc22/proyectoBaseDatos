class Producto:
    def __init__(self,id_producto,nombre,id_categoria, precio, total_compra= 0, total_ventas=0 , stock = 0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = precio
        self.total_compra = total_compra
        self.total_ventas = total_ventas
        self.stock = stock

class Categoria:
    def __init__(self,id_categoria,nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Clientes:
    def __init__(self,nit, nombre, telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Empleados:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class Proveedores:
    def __init__(self, id_proveedor, nombre,empresa, telefono, direccion, correo, id_categoria):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria

class Ventas:
    def __init__(self, id_venta , fecha, nit, id_empleado, total):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit = nit
        self.id_empleado = id_empleado
        self.total = total

class DetalleVentas:
    def __init__(self, id_detalle_venta, id_venta, cantidad, id_producto, precio, subtotal):
        self.id_venta = id_detalle_venta
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.precio = precio
        self.subtotal = subtotal

class Compra:
    def __init__(self, id_compras, fecha, id_proveedor, id_empleado, total):
        self.id_compras = id_compras
        self.fecha = fecha
        self.id_proveedor = id_proveedor
        self.id_empleado = id_empleado
        self.total = total

class DetalleCompra:
    def __init__(self, id_detalle_compra, id_compra, cantidad, id_producto, precio_compra, subtotal, fecha_caducidad):
        self.id_detalle_compra = id_detalle_compra
        self.id_compra = id_compra
        self.cantidad = cantidad
        self.id_producto = id_producto
        self.precio_compra = precio_compra
        self.subtotal = subtotal
        self.fecha_caducidad = fecha_caducidad





