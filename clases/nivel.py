# Contiene el nivel de dificultad del juego y la configuración del mismo.

# nivel.py
class Nivel:
    def __init__(self, dificultad):
        self.dificultad = dificultad
        self.num_cintas = self._configurar_cintas()

    def _configurar_cintas(self):
        # Basado en la tabla de dificultad del PDF
        if self.dificultad == "FACIL" or self.dificultad == "CRAZY":
            return 6  # Cintas 0 a 5
        elif self.dificultad == "MEDIO":
            return 8  # Cintas 0 a 7
        elif self.dificultad == "EXTREMO":
            return 10  # Cintas 0 a 9 (Total 10 cintas + suelo base)
        else:
            return 6