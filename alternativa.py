# alternativa.py

class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        if self.ayuda:
            return f"Contenido: {self.contenido}, Ayuda: {self.ayuda}"
        return f"Contenido: {self.contenido}"
