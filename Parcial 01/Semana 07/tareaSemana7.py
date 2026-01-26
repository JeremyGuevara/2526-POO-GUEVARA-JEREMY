class GestorDeArchivo:
    """
    Clase que demuestra el uso de constructores y destructores.
    Simula la apertura y cierre de un recurso de archivo.
    """

    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR: Se activa al crear una nueva instancia de la clase.
        Inicializa los atributos y 'abre' el recurso.
        """
        self.nombre_archivo = nombre_archivo
        print(f"--- [Constructor]: Abriendo el archivo '{self.nombre_archivo}' ---")
        # Aquí se inicializaría el recurso real (ej. open(nombre_archivo, 'w'))

    def escribir_datos(self, datos):
        """Método de instancia para interactuar con el objeto."""
        print(f"Escribiendo en '{self.nombre_archivo}': {datos}")

    def __del__(self):
        """
        DESTRUCTOR: Se activa cuando el objeto está a punto de ser destruido.
        Se utiliza para realizar tareas de limpieza o liberar recursos.
        """
        print(f"--- [Destructor]: Cerrando y liberando recursos de '{self.nombre_archivo}' ---")
        # Aquí se cerraría el archivo o la conexión a la base de datos


# --- Bloque de ejecución principal ---
if __name__ == "__main__":
    print("1. Iniciando creación de objetos...")

    # Se crea el primer objeto (Llamada al constructor)
    archivo1 = GestorDeArchivo("reporte_ventas.txt")
    archivo1.escribir_datos("Venta #102: $45.00")

    print("\n2. Eliminando referencia explícitamente...")
    # Al eliminar el objeto, se dispara el destructor
    del archivo1

    print("\n3. Creando un objeto dentro de un ámbito temporal...")


    def prueba_ambito():
        archivo2 = GestorDeArchivo("temporal.log")
        archivo2.escribir_datos("Entrada de log temporal")
        # Al terminar la función, archivo2 sale de memoria y se activa el destructor


    prueba_ambito()

    print("\n4. Fin del programa.")