
from repositorios import RepositorioCategoriasTxt, RepositorioProductosTxt, RepositorioEmpleadosTxt
from clases_constructor import Producto, Categoria, Empleados

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


class GestionCategorias:

    def __init__(self, repositorio_categorias: RepositorioCategoriasTxt):
        self.repositorio_categorias = repositorio_categorias
        self.categorias = self.repositorio_categorias.categorias

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

class GestionesEmpleados:

    def __init__(self, repositorio_empleados: RepositorioEmpleadosTxt):
        self.repositorio_empleados = repositorio_empleados
        self.empleados = self.repositorio_empleados.empleados

    def agregar_empleados(self):
        print("\n--Ingreso Empleados--")
        i = 0
        while True:

            print(f"\nEmpleado No.{i + 1}")

            while True:
                id_empleado = input("Codigo de Empleado: ")
                if id_empleado in self.empleados:
                    input("Codigo ingresado ya en existencia, presione para volver a Ingresarlo")
                    continue
                break

            nombre = input("Nombre del Empleado: ").lower()
            telefono = input("Telefono del Empleado: ")
            direccion = input("Direccion del Empleado: ")
            correo = input("Correo del Empleado: ")

            empleado = Empleados(id_empleado, nombre, telefono, direccion, correo)
            self.empleados[id_empleado] = empleado

            print(" ")
            self.repositorio.guardar_categorias()
            print(f"Producto Guardado con codigo {id_empleado} agregado y guardado correctamente.")
            confirmacion = input(
                "Desea Ingresar otro producto? presione S para continuar o presione N para salir: ").lower()

            if confirmacion == "s":
                continue
            elif confirmacion == "n":
                break
            else:
                print("error- opcion no valida, se terminara el ingreso")
                break



