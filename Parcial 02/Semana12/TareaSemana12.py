class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para (titulo, autor) ya que son datos inmutables
        self.info_fija = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info_fija[0]}' por {self.info_fija[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        # Lista para gestionar los libros actualmente prestados
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        # Diccionario {isbn: Objeto Libro} para búsquedas O(1)
        self.catalogo = {}
        # Conjunto para asegurar IDs de usuario únicos
        self.usuarios_registrados = set()
        # Diccionario para mapear ID con el objeto Usuario
        self.mapa_usuarios = {}

    def añadir_libro(self, libro):
        if libro.isbn not in self.catalogo:
            self.catalogo[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.catalogo:
            eliminado = self.catalogo.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No se encontró el libro para eliminar.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.user_id)
            self.mapa_usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print(f"El ID {usuario.user_id} ya está en uso.")

    def prestar_libro(self, isbn, user_id):
        if isbn in self.catalogo and user_id in self.usuarios_registrados:
            libro = self.catalogo.pop(isbn)  # Se quita del catálogo (está prestado)
            usuario = self.mapa_usuarios[user_id]
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info_fija[0]}' prestado a {usuario.nombre}.")
        else:
            print("Error: Libro no disponible o usuario no registrado.")

    def devolver_libro(self, isbn, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.mapa_usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.catalogo[isbn] = libro  # Vuelve al catálogo
                    print(f"Libro '{libro.info_fija[0]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene ese libro prestado.")
        else:
            print("ID de usuario no válido.")

    def buscar_libro(self, criterio, valor):
        # Búsqueda dinámica por título, autor o categoría
        resultados = []
        for libro in self.catalogo.values():
            if (criterio == "titulo" and valor.lower() in libro.info_fija[0].lower()) or \
                    (criterio == "autor" and valor.lower() in libro.info_fija[1].lower()) or \
                    (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print(f"\nResultados de búsqueda por {criterio} '{valor}':")
            for r in resultados: print(f" - {r}")
        else:
            print(f"\nNo se encontraron libros para {criterio}: {valor}")

    def listar_prestados(self, user_id):
        if user_id in self.usuarios_registrados:
            u = self.mapa_usuarios[user_id]
            print(f"\nLibros prestados a {u.nombre}:")
            if not u.libros_prestados:
                print(" Ninguno.")
            else:
                for l in u.libros_prestados: print(f" - {l}")
        else:
            print("Usuario no encontrado.")


# --- PRUEBAS DEL SISTEMA ---

# 1. Instanciar Biblioteca
mi_biblioteca = Biblioteca()

# 2. Crear Libros
l1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "978-01")
l2 = Libro("1984", "George Orwell", "Distopía", "978-02")
l3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "978-03")

# 3. Añadir libros
mi_biblioteca.añadir_libro(l1)
mi_biblioteca.añadir_libro(l2)
mi_biblioteca.añadir_libro(l3)

# 4. Registrar Usuarios
u1 = Usuario("Ana García", "U001")
u2 = Usuario("Beto Pérez", "U002")
mi_biblioteca.registrar_usuario(u1)
mi_biblioteca.registrar_usuario(u2)

# 5. Operaciones de Préstamo
mi_biblioteca.prestar_libro("978-01", "U001")
mi_biblioteca.prestar_libro("978-02", "U001")

# 6. Listar y Buscar
mi_biblioteca.listar_prestados("U001")
mi_biblioteca.buscar_libro("categoria", "Fantasía")

# 7. Devolución
mi_biblioteca.devolver_libro("978-01", "U001")
mi_biblioteca.listar_prestados("U001")