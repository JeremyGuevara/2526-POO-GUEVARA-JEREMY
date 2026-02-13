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

        if opcion == "1":
            try:
                id_p     = input("  ID producto: ").strip()
                nombre   = input("  Nombre: ").strip()
                cantidad = int(input("  Cantidad inicial: "))
                precio   = float(input("  Precio unitario ($): "))
                nuevo = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo)
            except ValueError:
                print("  → Error: cantidad debe ser entero, precio debe ser número")

        elif opcion == "2":
            id_p = input("  ID a eliminar: ").strip()
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("  ID del producto: ").strip()
            print("     a) Solo cantidad")
            print("     b) Solo precio")
            print("     c) Ambos")
            sub = input("     → ").strip().lower()

            cant = None
            prec = None

            try:
                if sub in ("a", "c"):
                    cant = int(input("  Nueva cantidad: "))
                if sub in ("b", "c"):
                    prec = float(input("  Nuevo precio ($): "))

                if cant is not None or prec is not None:
                    inventario.actualizar_producto(id_p, cant, prec)
                else:
                    print("  → No se ingresaron cambios")
            except ValueError:
                print("  → Error en formato numérico")

        elif opcion == "4":
            busqueda = input("  Texto a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(busqueda)
            if not resultados:
                print("  → No se encontraron coincidencias")
            else:
                print(f"\n  Encontrados {len(resultados)} producto(s):\n")
                for p in resultados:
                    print("   " + str(p))

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("\n  Gracias por usar el sistema. ¡Éxitos!\n")
            break

        else:
            print("  → Opción inválida")

if __name__ == "__main__":
    main()