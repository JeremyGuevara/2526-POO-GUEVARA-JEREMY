import json
import os


class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto  # Privado: El ID no debería cambiar
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # --- Getters ---
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # --- Setters ---
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    # --- Métodos Auxiliares para Serialización ---
    def to_dict(self):
        """Convierte el objeto a un diccionario para guardarlo en JSON."""
        return {
            "id": self.__id_producto,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }


class Inventario:
    """Clase que gestiona la colección de productos y la persistencia en archivos."""

    def __init__(self, archivo_datos="inventario.json"):
        # Utilizamos un diccionario. La clave será el ID y el valor el objeto Producto.
        self.productos = {}
        self.archivo_datos = archivo_datos
        self.cargar_datos()

    def guardar_datos(self):
        """Serializa el diccionario de productos y lo guarda en un archivo JSON."""
        try:
            # Convertimos cada objeto Producto a un diccionario básico
            datos_a_guardar = {id_prod: prod.to_dict() for id_prod, prod in self.productos.items()}
            with open(self.archivo_datos, 'w') as archivo:
                json.dump(datos_a_guardar, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self):
        """Deserializa el archivo JSON o carga datos de ejemplo si es la primera vez."""
        if not os.path.exists(self.archivo_datos):
            print("Iniciando sistema por primera vez. Cargando productos de ejemplo...\n")
            # --- PRODUCTOS DE EJEMPLO ---
            self.productos["P001"] = Producto("P001", "Laptop HP Pavilion", 15, 850.50)
            self.productos["P002"] = Producto("P002", "Mouse Inalámbrico Logitech", 50, 25.00)
            self.productos["P003"] = Producto("P003", "Teclado Mecánico Corsair", 30, 120.00)
            self.productos["P004"] = Producto("P004", "Monitor Dell 24 pulgadas", 20, 199.99)
            self.productos["P005"] = Producto("P005", "Cable HDMI 2m", 100, 8.50)
            # Guardamos estos ejemplos inmediatamente en el archivo
            self.guardar_datos()
            return

        try:
            with open(self.archivo_datos, 'r') as archivo:
                datos_cargados = json.load(archivo)
                # Reconstruimos los objetos Producto a partir de los diccionarios
                for id_prod, datos in datos_cargados.items():
                    producto = Producto(datos["id"], datos["nombre"], datos["cantidad"], datos["precio"])
                    self.productos[id_prod] = producto
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

    def agregar_producto(self, producto):
        """Añade un producto si su ID no existe previamente."""
        if producto.get_id() in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_datos()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario mediante su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_datos()
            print("Producto eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad y/o el precio de un producto existente."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_datos()
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        """Busca y muestra productos cuyo nombre coincida o contenga el texto buscado."""
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

        if resultados:
            print(f"\n--- Resultados de búsqueda para '{nombre}' ---")
            for p in resultados:
                print(
                    f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """Muestra todos los productos registrados en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- Inventario Actual ---")
        for p in self.productos.values():
            print(
                f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")


def mostrar_menu():
    print("\n" + "=" * 30)
    print(" GESTIÓN DE INVENTARIO ")
    print("=" * 30)
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("=" * 30)


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_prod = input("Ingrese el ID único del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Error: La cantidad debe ser un número entero y el precio un número válido.")

        elif opcion == '2':
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            if id_prod in inventario.productos:
                cant_input = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
                precio_input = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")

                cant = int(cant_input) if cant_input else None
                prec = float(precio_input) if precio_input else None

                inventario.actualizar_producto(id_prod, cantidad=cant, precio=prec)
            else:
                print("Error: Producto no encontrado.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema de gestión. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()