import tkinter as tk


class AplicacionListaTareas:
    """
    Clase principal de la aplicación GUI para gestionar una lista de tareas.
    Cumple todos los requisitos de la tarea:
    - Interfaz con Tkinter (Entry, botones y Listbox).
    - Manejo de eventos: botones, tecla Enter y doble clic (opcional).
    - Lógica: añadir, marcar como completada y eliminar tareas.
    - Visualización del estado completado mediante prefijos (✓ / □) ya que
      el Listbox estándar no permite estilos individuales por ítem fácilmente.
    """

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Lista de Tareas")
        self.raiz.geometry("520x480")
        self.raiz.resizable(False, False)

        # Estructura interna de datos: lista de diccionarios para mantener
        # el texto y el estado de cada tarea de forma independiente de la UI.
        # Decisión de diseño: usar dicts permite fácil actualización del estado
        # sin depender solo del texto visible en el Listbox.
        self.tareas = []

        # === INTERFAZ GRÁFICA ===

        # Etiqueta y campo de entrada para nuevas tareas
        tk.Label(
            self.raiz,
            text="Nueva tarea:",
            font=("Arial", 12, "bold")
        ).pack(pady=(15, 5))

        self.entrada = tk.Entry(self.raiz, width=55, font=("Arial", 12))
        self.entrada.pack(pady=5, padx=20)

        # Vincular la tecla Enter al método de añadir tarea
        # (requisito específico del manejo de eventos)
        self.entrada.bind("<Return>", self.agregar_tarea)

        # Botón para añadir tarea
        btn_agregar = tk.Button(
            self.raiz,
            text="Añadir Tarea",
            command=self.agregar_tarea,
            font=("Arial", 11),
            width=15
        )
        btn_agregar.pack(pady=8)

        # Listbox para mostrar las tareas
        # Se usa Listbox por simplicidad (cumple el ejemplo dado en los requisitos).
        # Altura y ancho configurados para una buena usabilidad.
        self.lista = tk.Listbox(
            self.raiz,
            width=60,
            height=15,
            font=("Arial", 12),
            selectmode=tk.SINGLE
        )
        self.lista.pack(pady=10, padx=20)

        # Evento doble clic (opcional, mejora la experiencia de usuario)
        # Permite marcar como completada directamente con el ratón.
        self.lista.bind("<Double-Button-1>", self.marcar_completada)

        # Frame para los botones de acción (mejora la organización visual)
        frame_botones = tk.Frame(self.raiz)
        frame_botones.pack(pady=10)

        # Botón Marcar como Completada
        self.btn_marcar = tk.Button(
            frame_botones,
            text="Marcar como Completada",
            command=self.marcar_completada,
            font=("Arial", 11),
            width=20
        )
        self.btn_marcar.pack(side=tk.LEFT, padx=8)

        # Botón Eliminar Tarea
        self.btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar Tarea",
            command=self.eliminar_tarea,
            font=("Arial", 11),
            width=20
        )
        self.btn_eliminar.pack(side=tk.LEFT, padx=8)

        # Cargar la lista inicialmente (vacía)
        self.actualizar_lista()

    def agregar_tarea(self, evento=None):
        """
        Manejador de evento para añadir una nueva tarea.
        Se activa tanto por el botón como por la tecla Enter.
        No permite tareas vacías.
        """
        texto = self.entrada.get().strip()
        if texto:
            # Añadir tarea con estado inicial "no completada"
            self.tareas.append({"texto": texto, "completada": False})
            self.entrada.delete(0, tk.END)  # Limpiar el Entry
            self.actualizar_lista()
        # Si está vacío, no se hace nada (no se muestra mensaje para mantener simplicidad)

    def marcar_completada(self, evento=None):
        """
        Manejador de evento para marcar una tarea como completada.
        Se activa por el botón o por doble clic en el Listbox.
        Solo cambia el estado si aún no estaba completada (según la descripción
        de la tarea: "marcarlas como completadas").
        """
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            # Solo marcar si no está completada ya
            if not self.tareas[indice]["completada"]:
                self.tareas[indice]["completada"] = True
                self.actualizar_lista()

    def eliminar_tarea(self):
        """
        Manejador de evento para eliminar la tarea seleccionada.
        """
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        """
        Reconstruye completamente el contenido del Listbox.
        Se llama después de cualquier cambio (añadir, marcar o eliminar).
        Muestra el estado visual con prefijos ✓ / □ para indicar si está completada.
        Esta es la forma más sencilla y clara de reflejar el cambio de estado
        visualmente sin necesidad de widgets más complejos (Treeview o estilos por ítem).
        """
        self.lista.delete(0, tk.END)
        for tarea in self.tareas:
            prefijo = "✓ " if tarea["completada"] else "□ "
            self.lista.insert(tk.END, prefijo + tarea["texto"])


if __name__ == "__main__":
    # Inicio de la aplicación
    raiz = tk.Tk()
    app = AplicacionListaTareas(raiz)
    raiz.mainloop()