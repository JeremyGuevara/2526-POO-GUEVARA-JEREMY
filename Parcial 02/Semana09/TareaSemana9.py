class Producto:
    """

    Atributos:
        id_producto (str): Identificador único del producto (ej: P001)
        nombre (str): Nombre descriptivo del producto
        cantidad (int): Existencias disponibles (≥ 0)
        precio (float): Precio unitario en dólares (≥ 0)
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.id_producto = str(id_producto).strip()
        self.nombre = str(nombre).strip()
        self.cantidad = max(0, int(cantidad))  # No permitimos negativos
        self.precio = max(0.0, float(precio))

    # Getters
    def obtener_id(self) -> str:
        return self.id_producto

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_cantidad(self) -> int:
        return self.cantidad

    def obtener_precio(self) -> float:
        return self.precio

    # Setters (solo para cantidad y precio – id y nombre no cambian)
    def actualizar_cantidad(self, nueva_cantidad: int):
        self.cantidad = max(0, int(nueva_cantidad))

    def actualizar_precio(self, nuevo_precio: float):
        self.precio = max(0.0, float(nuevo_precio))

    def __str__(self):
        return (f"{self.id_producto:>6} │ "
                f"{self.nombre:<38} │ "
                f"{self.cantidad:>5} und │ "
                f"${self.precio:>8.2f}")

    from producto import producto

    class Inventario:
        """
        Gestiona la colección de productos de la tienda.
        """

        def __init__(self):
            self.productos: list[self] = []

        def agregar_producto(self, producto: producto) -> bool:
            """Añade un producto si el ID no está repetido."""
            if any(p.obtener_id() == producto.obtener_id() for p in self.productos):
                print(f"  → ERROR: ya existe un producto con ID {producto.obtener_id()}")
                return False

            self.productos.append(producto)
            print(f"  → Producto agregado: {producto.obtener_nombre()}")
            return True

        def eliminar_producto(self, id_producto: str) -> bool:
            """Elimina el producto con el ID indicado."""
            for i, prod in enumerate(self.productos):
                if prod.obtener_id() == id_producto.strip():
                    nombre = prod.obtener_nombre()
                    del self.productos[i]
                    print(f"  → Eliminado: {nombre} (ID: {id_producto})")
                    return True
            print(f"  → No se encontró producto con ID {id_producto}")
            return False

        def actualizar_producto(self, id_producto: str, cantidad: int | None = None,
                                precio: float | None = None) -> bool:
            """Actualiza cantidad y/o precio de un producto existente."""
            id_producto = id_producto.strip()
            for prod in self.productos:
                if prod.obtener_id() == id_producto:
                    if cantidad is not None:
                        prod.actualizar_cantidad(cantidad)
                    if precio is not None:
                        prod.actualizar_precio(precio)
                    print(f"  → Actualizado → {prod}")
                    return True
            print(f"  → No se encontró producto con ID {id_producto}")
            return False

        def buscar_por_nombre(self, texto: str) -> list[producto]:
            """Búsqueda parcial (no sensible a mayúsculas)."""
            texto = texto.lower().strip()
            return [p for p in self.productos if texto in p.obtener_nombre().lower()]

        def mostrar_inventario(self):
            """Muestra todos los productos formateados."""
            if not self.productos:
                print("  El inventario está vacío.\n")
                return

            print("\n" + "═" * 78)
            print("               INVENTARIO ACTUAL DE LA TIENDA")
            print("═" * 78)
            print("   ID   │ Nombre del producto                          │ Cantidad │   Precio  ")
            print("─" * 78)

            for p in self.productos:
                print(p)

            print("═" * 78)
            print(f"  Total de productos registrados: {len(self.productos)}\n")

from inventario import Inventario


def mostrar_menu():
    print("\n" + "═" * 50)
    print("       SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("═" * 50)
    print("  1. Agregar nuevo producto")
    print("  2. Eliminar producto por ID")
    print("  3. Actualizar cantidad / precio")
    print("  4. Buscar productos por nombre")
    print("  5. Mostrar inventario completo")
    print("  6. Salir")
    print("═" * 50)


class Producto:
    pass


def cargar_producto_ejemplo(inventario: Inventario):
    # Único producto solicitado
    prod = Producto("E001", "Laptop HP 15s-eq2xxx", 8, 649.90)
    inventario.agregar_producto(prod)
    print("  → Producto de ejemplo cargado correctamente")

def main():
    inventario = Inventario()
    print("\n  Bienvenido al Sistema de Gestión de Inventarios\n")

    # Solo tu producto
    cargar_producto_ejemplo(inventario)

    while True:
        mostrar_menu()
        opcion = input("  Seleccione opción → ").strip()