import tkinter as tk
from tkinter import ttk, messagebox


class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - con Atajos de Teclado")
        self.root.geometry("650x550")
        self.root.configure(bg="#f0f0f0")

        # ==================== LISTA DE TAREAS PRE-CARGADA ====================
        self.tareas = [
            ["Comprar leche y pan", False],  # Pendiente
            ["Estudiar para el examen de matemáticas", True],  # Completada
            ["Llamar al dentista para cita", False],  # Pendiente
            ["Terminar la tarea de programación", True],  # Completada
            ["Hacer ejercicio 30 minutos", False],  # Pendiente
            ["Enviar el informe al profesor", False],  # Pendiente
            ["Revisar correos electrónicos", True]  # Completada
        ]
        # =====================================================================

        self.crear_interfaz()
        self.configurar_atajos_teclado()

        # Cargar las tareas iniciales en la lista
        self.actualizar_lista()

        self.entry_tarea.focus()

    def crear_interfaz(self):
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Gestor de Tareas",
                  font=("Helvetica", 18, "bold")).pack(pady=(0, 15))

        # Añadir nueva tarea
        frame_add = ttk.Frame(main_frame)
        frame_add.pack(fill=tk.X, pady=8)

        ttk.Label(frame_add, text="Nueva tarea:", font=("Helvetica", 11)).pack(side=tk.LEFT)

        self.entry_tarea = ttk.Entry(frame_add, font=("Helvetica", 11), width=45)
        self.entry_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
        self.entry_tarea.bind("<Return>", self.agregar_tarea_enter)

        ttk.Button(frame_add, text="Añadir", command=self.agregar_tarea).pack(side=tk.LEFT)

        # Botones de acción
        frame_botones = ttk.Frame(main_frame)
        frame_botones.pack(fill=tk.X, pady=10)

        ttk.Button(frame_botones, text="Marcar como Completada (C)",
                   command=self.marcar_completada).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar (Delete / D)",
                   command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar Completadas",
                   command=self.limpiar_completadas).pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        frame_lista = ttk.LabelFrame(main_frame, text=" Lista de tareas ", padding=10)
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=10)

        columnas = ("tarea", "estado")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=15)

        self.tree.heading("tarea", text="Tarea")
        self.tree.heading("estado", text="Estado")

        self.tree.column("tarea", width=420, anchor="w")
        self.tree.column("estado", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<Double-1>", lambda e: self.marcar_completada())

        # Instrucciones de atajos
        ttk.Label(main_frame,
                  text="Atajos de teclado:\n"
                       "• Enter → Añadir tarea\n"
                       "• C → Marcar como completada\n"
                       "• Delete o D → Eliminar tarea seleccionada\n"
                       "• Escape → Cerrar la aplicación",
                  font=("Helvetica", 10), foreground="#444444", justify="left").pack(pady=12, anchor="w")

    def configurar_atajos_teclado(self):
        self.root.bind("<KeyPress-c>", lambda e: self.marcar_completada())
        self.root.bind("<KeyPress-C>", lambda e: self.marcar_completada())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())
        self.root.bind("<KeyPress-d>", lambda e: self.eliminar_tarea())
        self.root.bind("<KeyPress-D>", lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<Control-n>", lambda e: self.entry_tarea.focus())

    def agregar_tarea(self):
        texto = self.entry_tarea.get().strip()
        if not texto:
            messagebox.showwarning("⚠️ Advertencia", "Escribe una tarea antes de añadirla.")
            return
        self.tareas.append([texto, False])
        self.actualizar_lista()
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus()

    def agregar_tarea_enter(self, event=None):
        self.agregar_tarea()

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for texto, completada in self.tareas:
            estado = "✓ Completada" if completada else "Pendiente"
            tag = "completada" if completada else "pendiente"
            self.tree.insert("", tk.END, values=(texto, estado), tags=(tag,))

        self.tree.tag_configure("completada", foreground="#888888")
        self.tree.tag_configure("pendiente", foreground="#000000")

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("ℹ️ Información", "Selecciona una tarea para marcarla como completada.")
            return
        indice = self.tree.index(seleccion[0])
        self.tareas[indice][1] = not self.tareas[indice][1]
        self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("ℹ️ Información", "Selecciona una tarea para eliminar.")
            return
        if messagebox.askyesno("❌ Confirmar", "¿Estás seguro de eliminar esta tarea?"):
            indice = self.tree.index(seleccion[0])
            del self.tareas[indice]
            self.actualizar_lista()

    def limpiar_completadas(self):
        if not any(t[1] for t in self.tareas):
            messagebox.showinfo("ℹ️ Información", "No hay tareas completadas para limpiar.")
            return
        if messagebox.askyesno("🧹 Confirmar", "¿Eliminar todas las tareas completadas?"):
            self.tareas = [t for t in self.tareas if not t[1]]
            self.actualizar_lista()


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()