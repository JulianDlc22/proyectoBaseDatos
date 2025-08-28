#clases constructoras de objetos

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

#clase ingreso

class Gestiones:
    def __init__(self):
        pass

class RepositorioGeneral:

    def cargar(self):
        pass
    def guardar(self):
        pass

class RepositorioProductos(RepositorioGeneral):

    def cargar(self):
     pass


class GestionProductos:
    def __init__(self):
        self.productos = {}
        self.cargar_clientes()

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_producto, nombre, id_categoria, precio, total_compra, total_ventas, stock = linea.split(":")
                        self.productos[id_producto] = {
                            "nombre": nombre,
                            "id_categoria": id_categoria,
                            "precio": precio,
                            "total_compra": total_compra,
                            "total_ventas": total_ventas,
                            "stock": stock

                        }
            print("Productos importados desde productos.txt")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")

    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for id_producto, datos in self.productos.items():
                archivo.write(f"{id_producto}:{datos['nombre']}:{datos['id_categoria']}:{datos['precio']}:{datos['total_compra']}:{datos['total_ventas']}:{datos['stock']}\n")

    def agregar_producto(self):
        print("\n--Ingreso de Productos--")
        i = 0
        while True:

            print(f"\nProducto No.{i + 1}")

            while True:
                id_producto = input("Codigo del Producto: ")
                if id_producto in self.productos:
                    input("Codigo ingresado ya en exitencia, presione para volver a Ingresarlo")
                    continue
                break

            nombre = input("Nombre del Producto: ").lower()

            while True:
                id_categoria = input("ID de la categoria del Producto: ")
                if len(self.categoria) == 0:
                    input("Aun no hay categorias ingresadas, presione para volver a Ingresarlo")
                    continue
                else:
                    break

            while True:
                try:
                    precio = float(input("Precio del Producto: "))
                    if precio < 0:
                        input("error- precio no valido, presione para volver a Ingresarlo")
                        continue  # vuelve al inicio del while para pedir de nuevo el precio.

                    break  # se ejecuta si el precio es correcto y te saca del while
                except ValueError:
                    input("error- precio no valido, presione para volver a Ingresarlo")

            while True:
                try:
                    stock = int(input("Stock del Producto: "))
                    if precio <= 0:
                        input("error- stock no valido, presione para volver a Ingresarlo ")
                        continue

                    break
                except ValueError:
                    input("error- Stock no valido, presione para volver a Ingresarlo")

            self.productos[id_producto] = Producto(id_producto, nombre, id_categoria, precio, 0 , 0, stock)
            print("\nProducto Agregado Exitosamente...")

            print(" ")
            self.guardar_productos()
            print(f"Producto Guardado con codigo {id_producto} agregado y guardado correctamente.")

    def mostrar_todos(self):
        if self.productos:
            print("\nLista de clientes:")
            for id_producto, datos in self.productos.items():
                print(f"\nCodigo: {id_producto}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay clientes registrados.")

#clase menu#

class Menu:
    def __init__(self):
        self.opcionesMenu= {
            "1": MenuAdmin(),
            "2": MenuVendedor()
        }

class OpcionesMenu:
    def ejecutar(self):
        pass

class MenuAdmin(OpcionesMenu):
    def ejecutar(self):
        print("--Menu Admin--")
        print("1. Ingresar Producto")
        print("2. Ingresar Empleado")
        print("3. Ingresar Proveedor")
        print("4. Ingresar Compra")
        print("5: Salir")

class MenuVendedor(OpcionesMenu):
    def ejecutar(self):
        print("--Menu Empleado--")
        print("1. Ingresar Venta")
        print("2. Salir")

class IngresoUsuario:
    def validacion_admin(self):

        usuario = "admin01"
        contraseña = "Administrador01"
        cont = 3
        while True:
            validacionUsuario = input("Ingrese Usuario: ")
            validacionContraseña = input("Ingrese la Contraseña: ")

            if validacionUsuario == usuario and validacionContraseña == contraseña:
                print("Usuario Valido, Bienvenido Admin")
                input("Presione enter para continuar...")
                return 1
                break

            else:
                cont -= 1
                if cont > 0:
                    print(f"Error- Usario o Contraseña Incorrectos(Intentos Restantes: {cont})")
                    input("Presione enter para continuar...")
                else:
                    print("Intentos maximos alcanzados")
                    input("Presione enter para Continuar...")
                    break




#programa Principal
admin = IngresoUsuario()
menu = Menu()
while True:
    print("1. Administrador")
    print("2. Vendedor")
    print("3. Salir")

    opcion = input("Ingrese una opcion: ")

    try:
        opcion = int(opcion)
        match opcion:
            case 1:
                admin.validacion_admin()

                if IngresoUsuario == 1:
                    while True:
                        menu.opcionesMenu["1"].ejecutar()

            case 2:
                pass
            case 3:
                pass
            case _:
                print("ERROR- opcion fuera del rango permitido")
                input(print("Presione enter para continuar..."))





    except ValueError:
        print("Error- esta Ingresando una opcion invalida")
        input(print("Presione enter para continuar..."))

















