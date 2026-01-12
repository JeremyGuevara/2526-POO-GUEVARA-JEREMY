# poo.py
# Programa para calcular el promedio semanal de temperaturas usando POO

class RegistroClimaSemanal:
    """
    Clase que representa el registro de temperaturas de una semana.
    Aplica encapsulamiento con atributos privados y métodos para manipularlos.
    """

    def __init__(self):
        """Inicializa la lista de temperaturas y los días de la semana."""
        self._temperaturas = []  # Atributo privado (encapsulamiento)
        self._dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias con validación."""
        print("Ingrese las temperaturas máximas diarias de la semana (en °C):\n")

        for dia in self._dias:
            while True:
                try:
                    temp = float(input(f"{dia}: "))
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un valor numérico válido.")

    def calcular_promedio(self):
        """Método que calcula y retorna el promedio semanal."""
        if len(self._temperaturas) == 0:
            return 0.0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_resumen(self):
        """Método que muestra el resumen completo de la semana."""
        promedio = self.calcular_promedio()
        print("\n" + "=" * 40)
        print("RESUMEN SEMANAL DEL CLIMA (POO)")
        print("=" * 40)
        for i, dia in enumerate(self._dias):
            print(f"{dia}: {self._temperaturas[i]} °C")
        print("-" * 40)
        print(f"Promedio semanal: {promedio:.2f} °C")
        print("=" * 40)

    def obtener_temperaturas(self):
        """Getter para acceder a las temperaturas (encapsulamiento)."""
        return self._temperaturas.copy()


def main():
    """Función principal usando la clase RegistroClimaSemanal."""
    print("=== Calculadora de Promedio Semanal de Temperaturas (POO) ===\n")

    clima = RegistroClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_resumen()


# Ejecutar el programa
if __name__ == "__main__":
    main()