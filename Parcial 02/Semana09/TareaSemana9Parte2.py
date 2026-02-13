class Producto:
    pass


class Inventario:
    def __init__(self):
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        if any(p.obtener_id() == producto.obtener_id() for p in self.productos):
            print(f"  → ERROR: ya existe ID {producto.obtener_id()}")
            return False
        self.productos.append(producto)
        print(f"  → Agregado: {producto.obtener_nombre()}")
        return True

    def eliminar_producto(self, id_producto: str) -> bool:
        id_producto = id_producto.strip()
        for i, prod in enumerate(self.productos):
            if prod.obtener_id() == id_producto:
                nombre = prod.obtener_nombre()
                del self.productos[i]
                print(f"  → Eliminado: {nombre} (ID: {id_producto})")
                return True
        print(f"  → No encontrado ID {id_producto}")
        return False

    def actualizar_producto(self, id_producto: str, cantidad: int | None = None, precio: float | None = None) -> bool:
        id_producto = id_producto.strip()
        for prod in self.productos:
            if prod.obtener_id() == id_producto:
                if cantidad is not None:
                    prod.actualizar_cantidad(cantidad)
                if precio is not None:
                    prod.actualizar_precio(precio)
                print(f"  → Actualizado → {prod}")
                return True
        print(f"  → No encontrado ID {id_producto}")
        return False

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        texto = texto.lower().strip()
        return [p for p in self.productos if texto in p.obtener_nombre().lower()]

    def mostrar_inventario(self):
        if not self.productos:
            print("  El inventario está vacío.\n")
            return

        print("\n" + "═" * 78)
        print("               INVENTARIO ACTUAL")
        print("═" * 78)
        print("   ID   │ Nombre del producto                          │ Cantidad │   Precio  ")
        print("─" * 78)
        for p in self.productos:
            print(p)
        print("═" * 78)
        print(f"  Total productos: {len(self.productos)}\n")
