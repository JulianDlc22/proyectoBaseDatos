from clases_constructor import Producto, Categoria, Empleados, Clientes, Proveedores, Ventas, DetalleVentas, Compra, DetalleCompra

class RepositorioProductosTxt:
    def __init__(self):
        self.productos = {}
        self.cargar_productos()

    def cargar_productos(self):

        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_producto, nombre, id_categoria, precio, total_compra, total_ventas, stock = linea.split(":")
                        self.productos[id_producto] = Producto(id_producto, nombre, id_categoria, precio, total_compra,total_ventas, stock)

                print("Productos importados desde productos.txt")

        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")


    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for id_producto, datos in self.productos.items():
                archivo.write(f"{id_producto}:{datos.nombre}:{datos.id_categoria}:{datos.precio}:{datos.total_compra}:{datos.total_ventas}:{datos.stock}\n")

class RepositorioCategoriasTxt:
    def __init__(self):
        self.categorias = {}
        self.cargar_categorias()

    def cargar_categorias(self):

        try:
            with open("categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_categoria, nombre = linea.split(":")
                        self.categorias[id_categoria] = Categoria(id_categoria, nombre)

                print("Categorias importados desde categorias.txt")

        except FileNotFoundError:
            print("No existe el archivo categorias.txt, se creará uno nuevo al guardar.")

    def guardar_categorias(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for id_categoria, datos in self.categorias.items():
                archivo.write(
                    f"{id_categoria}:{datos.nombre}\n")

class RepositorioEmpleadosTxt:
    def __init__(self):
        self.empleados= {}
        self.cargar_empleados()

    def cargar_empleados(self):

        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_empleado, nombre, telefono, direccion, correo = linea.split(":")
                        self.empleados[id_empleado] = Empleados(id_empleado, nombre, telefono, direccion, correo)

                print("Empleados importados desde empleados.txt")

        except FileNotFoundError:
            print("No existe el archivo empleados.txt, se creará uno nuevo al guardar.")

    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for id_empleados, datos in self.empleados.items():
                archivo.write(
                    f"{id_empleados}:{datos.nombre}:{datos.telefono}:{datos.direccion}:{datos.correo}\n")

class RepositorioClientesTxt:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):

        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, telefono, direccion, correo = linea.split(":")
                        self.clientes[nit] = Clientes(nit, nombre, telefono, direccion, correo)

                print("Clientes importados desde clientes.txt")

        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.clientes.items():
                archivo.write(
                    f"{nit}:{datos.nombre}:{datos.telefono}:{datos.direccion}:{datos.correo}\n")

class RepositorioProveedoresTxt:
    def __init__(self):
        self.proveedores = {}
        self.cargar_proveedores()

    def cargar_proveedores(self):

        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_proveedor, nombre, empresa,  telefono, direccion, correo , id_categoria = linea.split(":")
                        self.proveedores[id_proveedor] = Proveedores(id_proveedor, nombre, telefono, direccion, correo, id_categoria)

                print("Proveedores importados desde proveedores.txt")

        except FileNotFoundError:
            print("No existe el archivo proveedores.txt, se creará uno nuevo al guardar.")

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for id_proveedor, datos in self.proveedores.items():
                archivo.write(
                    f"{id_proveedor}:{datos.nombre}:{datos.empresa}:{datos.telefono}:{datos.direccion}:{datos.correo}:{datos.id_categoria}\n")

class RepositorioVentasTxt:
    def __init__(self):
        self.ventas = {}
        self.cargar_ventas()

    def cargar_ventas(self):

        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_ventas, fecha, nit, id_empleado, total = linea.split(":")
                        self.ventas[id_ventas] = Ventas(id_ventas, fecha, nit, id_empleado, total)

                print("Ventas importados desde ventas.txt")

        except FileNotFoundError:
            print("No existe el archivo ventas.txt, se creará uno nuevo al guardar.")

    def guardar_ventas(self):
        with open("ventas.txt", "w", encoding="utf-8") as archivo:
            for id_venta, datos in self.ventas.items():
                archivo.write(
                    f"{id_venta}:{datos.fecha}:{datos.nit}:{datos.id_empleado}:{datos.total}\n")

class RepositorioDetalleVentasTxt:
    def __init__(self):
        self.detalle_ventas = {}
        self.cargar_detalle_venta()

    def cargar_detalle_venta(self):

        try:
            with open("detalle_venta.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_detalle_venta, id_venta , cantidad, id_producto, precio, subtotal = linea.split(":")
                        self.detalle_ventas[id_detalle_venta] = DetalleVentas(id_detalle_venta, id_venta, cantidad, id_producto, precio, subtotal)

                print("Detalles de Venta importados desde detalle_venta.txt")

        except FileNotFoundError:
            print("No existe el archivo detalle_venta.txt, se creará uno nuevo al guardar.")

    def guardar_detalle_venta(self):
        with open("detalle_venta.txt", "w", encoding="utf-8") as archivo:
            for id_detalle_venta, datos in self.detalle_ventas.items():
                archivo.write(
                    f"{id_detalle_venta}:{datos.id_venta}:{datos.cantidad}:{datos.id_producto}:{datos.precio}:{datos.subtotal}\n")

class RepositorioCompraTxt:
    def __init__(self):
        self.compra = {}
        self.cargar_compra()

    def cargar_compra(self):

        try:
            with open("compra.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_compra, fecha, id_proveedor, id_empleado, total  = linea.split(":")
                        self.compra[id_compra] = Compra(id_compra, fecha, id_proveedor, id_empleado, total)

                print("Compras importados desde compra.txt")

        except FileNotFoundError:
            print("No existe el archivo compra.txt, se creará uno nuevo al guardar.")

    def guardar_detalle_venta(self):
        with open("compra.txt", "w", encoding="utf-8") as archivo:
            for id_compra, datos in self.compra.items():
                archivo.write(
                    f"{id_compra}:{datos.fecha}:{datos.proveedor}:{datos.id_empleado}:{datos.total}\n")

class RepositorioDetalleCompraTxt:
    def __init__(self):
        self.detalle_compra = {}
        self.cargar_detalle_compra()

    def cargar_detalle_compra(self):

        try:
            with open("detalle_compra.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_detalle_compra, id_compra , cantidad, id_producto, precio_compra, subtotal, fecha_caducidad = linea.split(":")
                        self.detalle_compra[id_detalle_compra] = DetalleCompra(id_detalle_compra, id_compra, cantidad, id_producto, precio_compra, subtotal, fecha_caducidad)

                print("Detalles de Compra importados desde detalle_compra.txt")

        except FileNotFoundError:
            print("No existe el archivo detalle_compra.txt, se creará uno nuevo al guardar.")

    def guardar_detalle_compra(self):
        with open("detalle_compra.txt", "w", encoding="utf-8") as archivo:
            for id_detalle_compra, datos in self.detalle_compra.items():
                archivo.write(
                    f"{id_detalle_compra}:{datos.id_compra}:{datos.cantidad}:{datos.id_producto}:{datos.precio_compra}:{datos.subtotal}:{datos.fecha_caducidad}\n")












