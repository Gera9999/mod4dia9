# main.py

from usuario import Usuario
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion

# Datos de ejemplo
preguntas = [
    {
        "enunciado": "¿Cuál es tu color favorito?",
        "esRequerida": True,
        "alternativas": [{"contenido": "Rojo"}, {"contenido": "Azul", "ayuda": "Un color calmante"}, {"contenido": "Verde"}],
        "ayuda": "Selecciona solo uno"
    }
]

# Crear instancias de encuestas
encuesta_general = Encuesta("Encuesta de colores", preguntas)
encuesta_edad = EncuestaLimitadaEdad("Encuesta de colores por edad", preguntas, 18, 30)
encuesta_region = EncuestaLimitadaRegion("Encuesta de colores por región", preguntas, [1, 2, 3])

# Crear usuario
usuario = Usuario("test@example.com", 25, 1)

# Usuario contesta las encuestas
respuestas = [2]  # Índice de las respuestas
usuario.contestarEncuesta(encuesta_general, respuestas)
usuario.contestarEncuesta(encuesta_edad, respuestas)
usuario.contestarEncuesta(encuesta_region, respuestas)

# Mostrar resultados
print(encuesta_general.mostrar())
print(encuesta_edad.mostrar())
print(encuesta_region.mostrar())
