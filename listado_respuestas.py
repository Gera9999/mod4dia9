# listado_respuestas.py

class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario
        self.respuestas = respuestas

    def mostrar(self):
        respuestas_formateadas = '\n    '.join([str(resp) for resp in self.respuestas])
        return f"Usuario: {self.usuario.correo}\n    Respuestas:\n    {respuestas_formateadas}"
