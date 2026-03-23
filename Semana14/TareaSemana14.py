# ================================================
# AGENDA PERSONAL - Tarea de Programación
# Hecho por Jeremy
# Universidad Estatal Amazónica
# Marzo 2026
# ================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
from datetime import datetime


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 Mi Agenda Personal")
        self.root.geometry("820x620")
        self.root.resizable(True, True)

        self.archivo = "mis_eventos.json"

        # ==================== LISTA DE EVENTOS ====================
        frame_lista = ttk.LabelFrame(root, text=" 📋 Mis Eventos y Tareas")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=8)

        self.arbol = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.arbol.heading("Fecha", text="Fecha")
        self.arbol.heading("Hora", text="Hora")
        self.arbol.heading("Descripción", text="Descripción")

        self.arbol.column("Fecha", width=110, anchor="center")
        self.arbol.column("Hora", width=90, anchor="center")
        self.arbol.column("Descripción", width=500)

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.arbol.yview)
        self.arbol.configure(yscrollcommand=scrollbar.set)

        self.arbol.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.pack(side="right", fill="y")

        # ==================== CAMPOS PARA AGREGAR ====================
        frame_entrada = ttk.LabelFrame(root, text=" ➕ Agregar Nuevo Evento")
        frame_entrada.pack(fill="x", padx=10, pady=8)

        ttk.Label(frame_entrada, text="Fecha (AAAA-MM-DD):").grid(row=0, column=0, padx=8, pady=6, sticky="w")
        self.entrada_fecha = ttk.Entry(frame_entrada, width=18)
        self.entrada_fecha.grid(row=0, column=1, padx=8, pady=6)

        ttk.Button(frame_entrada, text="🗓️ Elegir Fecha", command=self.elegir_fecha).grid(row=0, column=2, padx=8)

        ttk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=8, pady=6, sticky="w")
        self.entrada_hora = ttk.Entry(frame_entrada, width=18)
        self.entrada_hora.grid(row=1, column=1, padx=8, pady=6)

        ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=8, pady=6, sticky="w")
        self.entrada_desc = ttk.Entry(frame_entrada, width=55)
        self.entrada_desc.grid(row=2, column=1, columnspan=2, padx=8, pady=6, sticky="ew")

        # ==================== BOTONES ====================
        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=12)

        ttk.Button(frame_botones, text="✅ Agregar Evento", command=self.agregar).grid(row=0, column=0, padx=12)
        ttk.Button(frame_botones, text="🗑️ Eliminar Seleccionado", command=self.eliminar).grid(row=0, column=1, padx=12)
        ttk.Button(frame_botones, text="❌ Salir", command=self.salir).grid(row=0, column=2, padx=12)

        # Cargar eventos + poner ejemplos la primera vez
        self.cargar_eventos()
        self.agregar_ejemplos_iniciales()

    # ====================== CARGAR Y GUARDAR ======================
    def cargar_eventos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                eventos = json.load(f)
                for ev in eventos:
                    self.arbol.insert("", "end", values=(ev["fecha"], ev["hora"], ev["descripcion"]))

    def guardar_eventos(self):
        lista = []
        for item in self.arbol.get_children():
            valores = self.arbol.item(item)["values"]
            lista.append({"fecha": valores[0], "hora": valores[1], "descripcion": valores[2]})
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

    # ====================== EJEMPLOS AUTOMÁTICOS (solo la primera vez) ======================
    def agregar_ejemplos_iniciales(self):
        if len(self.arbol.get_children()) == 0:  # Solo si está vacío
            ejemplos = [
                ("2026-03-24", "09:00", "Entregar actividad GeoGebra (campo de direcciones EDO)"),
                ("2026-03-25", "14:00", "Revisar ejercicios 1 al 5 de EDO a mano"),
                ("2026-03-26", "10:30", "Clase de Ecuaciones Diferenciales - Tema: Soluciones particulares"),
                ("2026-03-27", "20:00", "Terminar y subir Agenda Personal Tkinter a GitHub"),
                ("2026-03-28", "08:00", "Estudiar para el examen parcial de EDO"),
                ("2026-04-01", "15:00", "Entrega final de la Actividad Calificada de EDO")
            ]
            for fecha, hora, desc in ejemplos:
                self.arbol.insert("", "end", values=(fecha, hora, desc))
            self.guardar_eventos()

    # ====================== AGREGAR EVENTO ======================
    def agregar(self):
        fecha = self.entrada_fecha.get().strip()
        hora = self.entrada_hora.get().strip()
        desc = self.entrada_desc.get().strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Atención", "Por favor completa todos los campos")
            return

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
        except:
            messagebox.showwarning("Error", "Formato incorrecto.\nFecha: AAAA-MM-DD\nHora: HH:MM")
            return

        self.arbol.insert("", "end", values=(fecha, hora, desc))
        self.guardar_eventos()

        self.entrada_fecha.delete(0, tk.END)
        self.entrada_hora.delete(0, tk.END)
        self.entrada_desc.delete(0, tk.END)

        messagebox.showinfo("¡Listo!", "Evento agregado correctamente ✓")

    # ====================== ELIMINAR ======================
    def eliminar(self):
        seleccionado = self.arbol.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un evento para eliminar")
            return
        if messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este evento?"):
            self.arbol.delete(seleccionado[0])
            self.guardar_eventos()
            messagebox.showinfo("Eliminado", "Evento borrado correctamente")

    # ====================== ELEGIR FECHA ======================
    def elegir_fecha(self):
        ventana_fecha = tk.Toplevel(self.root)
        ventana_fecha.title("Seleccionar Fecha")
        ventana_fecha.geometry("300x240")
        ventana_fecha.grab_set()

        ttk.Label(ventana_fecha, text="Día:").pack(pady=5)
        spin_dia = ttk.Spinbox(ventana_fecha, from_=1, to=31, width=8)
        spin_dia.pack()

        ttk.Label(ventana_fecha, text="Mes:").pack(pady=5)
        combo_mes = ttk.Combobox(ventana_fecha,
                                 values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
                                 width=8, state="readonly")
        combo_mes.set("03")
        combo_mes.pack()

        ttk.Label(ventana_fecha, text="Año:").pack(pady=5)
        spin_anio = ttk.Spinbox(ventana_fecha, from_=2025, to=2030, width=10)
        spin_anio.set("2026")
        spin_anio.pack()

        def confirmar():
            dia = spin_dia.get().zfill(2)
            mes = combo_mes.get()
            anio = spin_anio.get()
            self.entrada_fecha.delete(0, tk.END)
            self.entrada_fecha.insert(0, f"{anio}-{mes}-{dia}")
            ventana_fecha.destroy()

        ttk.Button(ventana_fecha, text="✅ Usar esta fecha", command=confirmar).pack(pady=15)

    # ====================== SALIR ======================
    def salir(self):
        if messagebox.askokcancel("Salir", " ¿Quieres cerrar la agenda?"):
            self.guardar_eventos()
            self.root.quit()


# ====================== INICIAR ======================
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgendaPersonal(ventana)
    ventana.mainloop()