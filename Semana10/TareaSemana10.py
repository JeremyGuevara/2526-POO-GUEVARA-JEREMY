# Sistema de Gestión de Inventarios Mejorado
# Autor: Jeremy Guevara
# Fecha: 2026-02-21
# Descripción: Este programa gestiona un inventario de productos, almacenando la información en un archivo de texto.
#              Incluye manejo de excepciones para operaciones de archivo y notificaciones al usuario.

import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = {}  # Diccionario para almacenar productos, clave: id_producto
        self.archivo = archivo
        self.cargar_inventario()  # Cargar inventario al iniciar

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario.
        Maneja excepciones si el archivo no existe o hay problemas de permisos.
        """
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, crearlo vacío
                with open(self.archivo, 'w') as f:
                    pass  # Archivo creado
                print(f"Archivo '{self.archivo}' creado exitosamente.")
                return

            with open(self.archivo, 'r') as f:
                for linea in f:
                    if linea.strip():  # Ignorar líneas vacías
                        id_prod, nombre, cant, prec = linea.strip().split(',')
                        self.productos[int(id_prod)] = Producto(int(id_prod), nombre, int(cant), float(prec))
            print(f"Inventario cargado exitosamente desde '{self.archivo}'.")
        except FileNotFoundError:
            print(f"Error: El archivo '{self.archivo}' no se encontró. Se creará uno nuevo al guardar.")
        except PermissionError:
            print(f"Error: No hay permisos para leer el archivo '{self.archivo}'.")
        except ValueError:
            print(f"Error: El archivo '{self.archivo}' está corrupto o tiene formato incorrecto.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario.
        Maneja excepciones durante la escritura.
        """
        try:
            with open(self.archivo, 'w') as f:
                for prod in self.productos.values():
                    f.write(f"{prod.id_producto},{prod.nombre},{prod.cantidad},{prod.precio}\n")
            print(f"Inventario guardado exitosamente en '{self.archivo}'.")
            return True
        except PermissionError:
            print(f"Error: No hay permisos para escribir en el archivo '{self.archivo}'.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")
            return False

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario y guarda en archivo."""
        if id_producto in self.productos:
            print(f"Error: El producto con ID {id_producto} ya existe.")
            return
        self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        if self.guardar_inventario():
            print(f"Producto '{nombre}' añadido exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto existente y guarda en archivo."""
        if id_producto not in self.productos:
            print(f"Error: El producto con ID {id_producto} no existe.")
            return
        prod = self.productos[id_producto]
        if cantidad is not None:
            prod.cantidad = cantidad
        if precio is not None:
            prod.precio = precio
        if self.guardar_inventario():
            print(f"Producto con ID {id_producto} actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario y guarda en archivo."""
        if id_producto not in self.productos:
            print(f"Error: El producto con ID {id_producto} no existe.")
            return
        del self.productos[id_producto]
        if self.guardar_inventario():
            print(f"Producto con ID {id_producto} eliminado exitosamente.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Productos en el inventario:")
        for prod in self.productos.values():
            print(prod)


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_prod = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(id_prod, nombre, cantidad, precio)
            except ValueError:
                print("Error: Entrada inválida. Asegúrese de ingresar números donde corresponda.")

        elif opcion == '2':
            try:
                id_prod = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (deje en blanco si no cambia): ")
                precio = input("Nuevo precio (deje en blanco si no cambia): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_prod, cantidad, precio)
            except ValueError:
                print("Error: Entrada inválida. Asegúrese de ingresar números donde corresponda.")

        elif opcion == '3':
            try:
                id_prod = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_prod)
            except ValueError:
                print("Error: Entrada inválida. Asegúrese de ingresar un número para el ID.")

        elif opcion == '4':
            inventario.mostrar_productos()

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()

# Ejemplo de uso para añadir productos y mostrar todos:
# Puedes ejecutar el programa y usar la opción 1 para añadir productos como:
# ID: 1, Nombre: Laptop, Cantidad: 10, Precio: 999.99
# ID: 2, Nombre: Mouse, Cantidad: 50, Precio: 19.99
# Luego, usa la opción 4 para mostrar todos los productos.