# Tarea: Aplicación de Conceptos de POO en Python
# Alumno: [Tu Nombre]

class Empleado:
    """Clase Base que representa a un empleado genérico."""

    def __init__(self, nombre, id_empleado, sueldo_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        # ENCAPSULACIÓN: Usamos doble guion bajo para hacer el atributo privado
        self.__sueldo_base = sueldo_base

        # Métodos para acceder al atributo encapsulado (Getter y Setter)

    def get_sueldo_base(self):
        return self.__sueldo_base

    def mostrar_info(self):
        print(f"ID: {self.id_empleado} | Nombre: {self.nombre} | Sueldo Base: ${self.__sueldo_base}")

    def calcular_pago(self):
        """Método que será sobrescrito (Polimorfismo)."""
        return self.__sueldo_base


class Gerente(Empleado):
    """CLASE DERIVADA: Demuestra HERENCIA."""

    def __init__(self, nombre, id_empleado, sueldo_base, bono_gestion):
        # Llamada al constructor de la clase base
        super().__init__(nombre, id_empleado, sueldo_base)
        self.bono_gestion = bono_gestion

    # POLIMORFISMO: Sobrescritura del método calcular_pago
    def calcular_pago(self):
        return self.get_sueldo_base() + self.bono_gestion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cargo: Gerente | Bono: ${self.bono_gestion}")


class Tecnico(Empleado):
    """CLASE DERIVADA: Otra demostración de HERENCIA."""

    def __init__(self, nombre, id_empleado, sueldo_base, especialidad):
        super().__init__(nombre, id_empleado, sueldo_base)
        self.especialidad = especialidad

    # POLIMORFISMO: El pago se calcula diferente para un técnico
    def calcular_pago(self):
        # El técnico recibe un 10% adicional por especialidad
        return self.get_sueldo_base() * 1.10

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cargo: Técnico | Especialidad: {self.especialidad}")


# --- DEMOSTRACIÓN DE FUNCIONALIDAD ---
if __name__ == "__main__":
    print("--- Sistema de Nómina POO ---")

    # Creación de instancias (Objetos)
    gerente_ventas = Gerente("Jeremy Guevara", "G001", 3000, 500)
    tecnico_it = Tecnico("Xavier Barrera", "T502", 2000, "Ciberseguridad")

    # Lista de empleados para demostrar polimorfismo en un ciclo
    nomina = [gerente_ventas, tecnico_it]

    for empleado in nomina:
        empleado.mostrar_info()
        # Aquí ocurre el POLIMORFISMO: cada objeto sabe cómo calcular su propio pago
        print(f"Pago Total a depositar: ${empleado.calcular_pago()}")
        print("-" * 40)