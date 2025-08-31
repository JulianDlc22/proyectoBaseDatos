from gestiones import GestionProductos, GestionCategorias

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
            print("2. Ingresar Categoria")
            print("3. Ingresar Empleado")
            print("4. Ingresar Proveedor")
            print("5. Ingresar Compra")
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