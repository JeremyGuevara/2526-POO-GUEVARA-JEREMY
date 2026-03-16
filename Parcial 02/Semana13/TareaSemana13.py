import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):
        # Configuración principal de la ventana
        self.root = root
        self.root.title("Gestor de Inventario Básico")
        self.root.geometry("400x420")
        self.root.config(padx=20, pady=20)

        # --- Diseño de la Interfaz ---

        self.lbl_instruccion = tk.Label(root, text="Ingresa el nombre del nuevo artículo:", font=("Arial", 11))
        self.lbl_instruccion.pack(pady=(0, 5))

        self.entrada_datos = tk.Entry(root, width=35, font=("Arial", 11))
        self.entrada_datos.pack(pady=5)

        self.btn_agregar = tk.Button(root, text="Agregar Artículo", command=self.agregar_dato, bg="#4CAF50", fg="white",
                                     font=("Arial", 10, "bold"))
        self.btn_agregar.pack(pady=5)

        self.btn_limpiar = tk.Button(root, text="Limpiar / Eliminar Selección", command=self.limpiar_dato, bg="#f44336",
                                     fg="white", font=("Arial", 10, "bold"))
        self.btn_limpiar.pack(pady=5)

        self.lbl_separador = tk.Label(root, text="--- Artículos Registrados ---", font=("Arial", 10, "italic"))
        self.lbl_separador.pack(pady=(15, 5))

        self.lista_datos = tk.Listbox(root, width=40, height=10, font=("Arial", 10))
        self.lista_datos.pack(pady=5)

        # --- Carga de Datos por Defecto ---
        # Aquí agregamos los artículos iniciales para que no tengas que hacerlo tú
        articulos_iniciales = [
            "Laptop Dell XPS 15",
            "Monitor Samsung 24 pulgadas",
            "Teclado Mecánico Logitech",
            "Ratón Inalámbrico",
            "Memoria RAM 16GB Corsair",
            "Disco Sólido SSD 1TB"
        ]

        # Insertamos cada artículo en la interfaz
        for articulo in articulos_iniciales:
            self.lista_datos.insert(tk.END, articulo)

    # --- Eventos y Funcionalidad ---

    def agregar_dato(self):
        """Obtiene el texto del campo, lo agrega a la lista y limpia la entrada."""
        nuevo_dato = self.entrada_datos.get().strip()

        if nuevo_dato:
            self.lista_datos.insert(tk.END, nuevo_dato)
            self.entrada_datos.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe un artículo antes de hacer clic en Agregar.")

    def limpiar_dato(self):
        """Borra el texto que se estaba escribiendo o elimina el elemento seleccionado de la lista."""
        if self.entrada_datos.get():
            self.entrada_datos.delete(0, tk.END)
        else:
            seleccion = self.lista_datos.curselection()
            if seleccion:
                self.lista_datos.delete(seleccion)
            else:
                messagebox.showinfo("Información",
                                    "Escribe algo para limpiar o selecciona un ítem de la lista para eliminarlo.")


# --- Bloque de Ejecución Principal ---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AplicacionGUI(ventana_principal)
    ventana_principal.mainloop()