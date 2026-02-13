def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
    self.id_producto = str(id_producto).strip()
    self.nombre = str(nombre).strip()
    self.cantidad = max(0, int(cantidad))
    self.precio = max(0.0, float(precio))


def obtener_id(self) -> str:
    return self.id_producto


def obtener_nombre(self) -> str:
    return self.nombre


def obtener_cantidad(self) -> int:
    return self.cantidad


def obtener_precio(self) -> float:
    return self.precio


def actualizar_cantidad(self, nueva_cantidad: int):
    self.cantidad = max(0, int(nueva_cantidad))


def actualizar_precio(self, nuevo_precio: float):
    self.precio = max(0.0, float(nuevo_precio))


def __str__(self):
    return (f"{self.id_producto:>6} │ "
            f"{self.nombre:<38} │ "
            f"{self.cantidad:>5} und │ "
            f"${self.precio:>8.2f}")