"""
Programa: Calculadora de Presupuesto para Pintura de Interiores
Funcionalidad: Versión con valores predefinidos para demostración.
"""


def calcular_presupuesto_fijo():
    # --- DATOS ASIGNADOS (En lugar de input) ---
    nombre_proyecto = "Remodelación Oficina Central"
    ancho_pared = 8.5  # en metros
    alto_pared = 3.0  # en metros
    costo_por_metro = 15.50
    numero_capas = 2

    # --- PROCESAMIENTO ---
    # Cálculo del área base usando la fórmula: $Area = ancho \times alto$
    area_base = ancho_pared * alto_pared

    # Cálculo del trabajo total (considerando las capas)
    area_total_trabajo = area_base * numero_capas

    # Cálculo del costo financiero
    costo_total = area_total_trabajo * costo_por_metro

    # Verificación de descuento (Si el área es mayor a 50 m2)
    tiene_descuento_volumen = area_total_trabajo > 50.0

    # --- SALIDA DE DATOS ---
    print(f"--- Resumen del Presupuesto: {nombre_proyecto} ---")
    print(f"Dimensiones: {ancho_pared}m de ancho x {alto_pared}m de alto")
    print(f"Capas de pintura: {numero_capas}")
    print("-" * 40)
    print(f"Área total a cubrir: {area_total_trabajo} m2")
    print(f"Costo total estimado: ${costo_total:,.2f}")
    print(f"¿Aplica para descuento por volumen?: {'SÍ' if tiene_descuento_volumen else 'NO'}")


if __name__ == "__main__": calcular_presupuesto_fijo()