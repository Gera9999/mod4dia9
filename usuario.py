# usuario.py

from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestarEncuesta(self, encuesta, respuestas):
        listadoRespuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregarListadoRespuestas(listadoRespuestas)
