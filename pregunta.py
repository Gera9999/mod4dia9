# pregunta.py

from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, esRequerida, alternativas, ayuda=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.esRequerida = esRequerida
        self.alternativas = [Alternativa(**alt) for alt in alternativas]

    def mostrar(self):
        alternativas_mostradas = '\n    '.join([alt.mostrar() for alt in self.alternativas])
        return f"Enunciado: {self.enunciado}\n    Ayuda: {self.ayuda}\n    Alternativas:\n    {alternativas_mostradas}"
