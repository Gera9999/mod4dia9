# encuesta.py

from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = [Pregunta(**pregunta) for pregunta in preguntas]
        self.listadosRespuestas = []

    def mostrar(self):
        preguntas_mostradas = '\n  '.join([pregunta.mostrar() for pregunta in self.preguntas])
        listados_mostrados = '\n  '.join([listado.mostrar() for listado in self.listadosRespuestas])
        return f"Nombre: {self.nombre}\nPreguntas:\n  {preguntas_mostradas}\nListados de Respuestas:\n  {listados_mostrados}"

    def agregarListadoRespuestas(self, listadoRespuestas):
        self.listadosRespuestas.append(listadoRespuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas, edadMinima, edadMaxima):
        super().__init__(nombre, preguntas)
        self.edadMinima = edadMinima
        self.edadMaxima = edadMaxima

    def mostrar(self):
        base = super().mostrar()
        return f"{base}\nEdad mínima: {self.edadMinima}, Edad máxima: {self.edadMaxima}"

    def agregarListadoRespuestas(self, listadoRespuestas):
        if self.edadMinima <= listadoRespuestas.usuario.edad <= self.edadMaxima:
            super().agregarListadoRespuestas(listadoRespuestas)

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas, regiones):
        super().__init__(nombre, preguntas)
        self.regiones = regiones

    def mostrar(self):
        base = super().mostrar()
        regiones_formateadas = ', '.join(map(str, self.regiones))
        return f"{base}\nRegiones permitidas: {regiones_formateadas}"

    def agregarListadoRespuestas(self, listadoRespuestas):
        if listadoRespuestas.usuario.region in self.regiones:
            super().agregarListadoRespuestas(listadoRespuestas)
