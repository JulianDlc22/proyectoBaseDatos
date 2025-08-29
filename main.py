#clases constructoras de objetos

class Producto:
    def __init__(self,id_producto,nombre,id_categoria, precio, total_compra= 0, total_ventas=0 , stock = 0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = float(precio)
        self.total_compra = int(total_compra)
        self.total_ventas = int(total_ventas)
        self.stock = int(stock)

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
        self.id_detalle_venta = id_detalle_venta
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

class RepositorioProductosGenerico:

    def cargar_productos(self):
        pass
    def guardar_productos(self):
        pass

class RepositorioProductosTxt(RepositorioProductosGenerico):
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



class GestionProductos:
    def __init__(self, repositorio_productos: RepositorioProductosTxt , repositorio_categorias : "RepositorioCategorias"):
        self.repositorio_productos = repositorio_productos
        self.repositorio_categorias = repositorio_categorias
        self.productos = self.repositorio_productos.productos
        self.categorias = self.repositorio_categorias.categorias


    def agregar_producto(self):
        print("\n--Ingreso de Productos--")
        i = 0
        while True:

            print(f"\nProducto No.{i + 1}")

            while True:
                id_producto = input("Codigo del Producto: ")
                if id_producto in self.productos:
                    input("Codigo ingresado ya en existencia, presione para volver a Ingresarlo")
                    continue
                break

            nombre = input("Nombre del Producto: ").lower()

            while True:
                id_categoria = input("ID de la categoria del Producto: ")
                if len(self.categorias) == 0:
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
                    if stock <= 0:
                        input("error- stock no valido, presione para volver a Ingresarlo ")
                        continue

                    break
                except ValueError:
                    input("error- Stock no valido, presione para volver a Ingresarlo")

            producto = Producto(id_producto, nombre, id_categoria, precio, 0 , 0, stock)
            self.productos[id_producto] = producto

            print(" ")
            self.repositorio_productos.guardar_productos()
            print(f"Producto Guardado con codigo {id_producto} agregado y guardado correctamente.")
            confirmacion = input("Desea Ingresar otro producto? presione S para continuar o presione N para salir: ").lower()

            if confirmacion == "s":
                continue
            elif confirmacion == "n":
                break
            else:
                print("error- opcion no valida, se terminara el ingreso")
                break


    def mostrar_todos(self):
        if self.productos:
            print("\nLista de clientes:")
            for id_producto, datos in self.productos.items():
                print(f"\nCodigo: {id_producto}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay clientes registrados.")

class RepositorioCategorias():
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

                print("Categorias importados desde productos.txt")

        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")

    def guardar_categorias(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for id_categoria, datos in self.categorias.items():
                archivo.write(
                    f"{id_categoria}:{datos.nombre}\n")

class GestionCategorias:

    def __init__(self, repositorio: RepositorioCategorias):
        self.repositorio = repositorio
        self.categorias = self.repositorio.categorias

    def agregar_categorias(self):
        print("\n--Ingreso Categorias--")
        i = 0
        while True:

            print(f"\nCategoria No.{i + 1}")

            while True:
                id_categoria = input("Codigo de la categoria: ")
                if id_categoria in self.categorias:
                    input("Codigo ingresado ya en existencia, presione para volver a Ingresarlo")
                    continue
                break

            nombre = input("Nombre del Producto: ").lower()

            categoria = Categoria(id_categoria, nombre)
            self.categorias[id_categoria] = categoria

            print(" ")
            self.repositorio.guardar_categorias()
            print(f"Producto Guardado con codigo {id_categoria} agregado y guardado correctamente.")
            confirmacion = input(
                "Desea Ingresar otro producto? presione S para continuar o presione N para salir: ").lower()

            if confirmacion == "s":
                continue
            elif confirmacion == "n":
                break
            else:
                print("error- opcion no valida, se terminara el ingreso")
                break



#clase menu#

class Menu:
    def __init__(self, gestion_productos: GestionProductos, gestion_categorias: GestionCategorias):
        self.opcionesMenu= {
            "1": MenuAdmin(gestion_productos = gestion_productos,gestion_categorias= gestion_categorias ),
            "2": MenuVendedor()
        }

class OpcionesMenu:
    def ejecutar(self):
        pass

class MenuAdmin(OpcionesMenu):
    def __init__(self, gestion_productos : GestionProductos, gestion_categorias : GestionCategorias):
        self.gestion_productos = gestion_productos
        self.gestion_categorias = gestion_categorias

    def ejecutar(self):

        while True:
            print("--Menu Admin--")
            print("1. Ingresar Producto")
            print("2. Ingresar Empleado")
            print("3. Ingresar Proveedor")
            print("4. Ingresar Compra")
            print("5: Salir")

            opcion = input("eliga una opcion: ")
            try:
                op = int(opcion)

                match op:
                    case 1:
                        self.gestion_productos.agregar_producto()
                    case 2:
                        self.gestion_categorias.agregar_categorias()
                    case 5:
                        break
                    case _:
                        input("opcion fuera de rango permitido, presione enter para continuar...")

            except ValueError:
                input("opcion invalida, presione para continuar...")



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
repositorio_productos = RepositorioProductosTxt()
repositorio_categorias = RepositorioCategorias()
gestiones_productos = GestionProductos(repositorio_productos,repositorio_categorias)
gestiones_categorias = GestionCategorias(repositorio_categorias)
menu = Menu(gestiones_productos, gestiones_categorias)


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
                menu.opcionesMenu["1"].ejecutar()
            case 2:
                pass
            case 3:
                print("Saliendo...")
                break
            case _:
                print("ERROR- opcion fuera del rango permitido")
                input("Presione enter para continuar...")


    except ValueError:
        print("Error- esta Ingresando una opcion invalida")
        input("Presione enter para continuar...")

















