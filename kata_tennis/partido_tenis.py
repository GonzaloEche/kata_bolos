class Tenis(object):
    def __init__(self):
        self.la_puntuacion_jugador_uno_es = 0
        self.la_puntuacion_jugador_dos_es = 0

    def puntuacion(self):

        #ambos jugadores

        if (self.la_puntuacion_jugador_uno_es == 1 and self.la_puntuacion_jugador_dos_es == 1):
            return "15-15"


        #jugador 1
        if self.la_puntuacion_jugador_uno_es == 1:
            return "15"
        if self.la_puntuacion_jugador_uno_es == 2:
            return "30"
        if self.la_puntuacion_jugador_uno_es == 3:
            return "40"

        #jugador 2
        if self.la_puntuacion_jugador_dos_es == 1:
            return "15"
        if self.la_puntuacion_jugador_dos_es == 2:
            return "30"
        if self.la_puntuacion_jugador_dos_es == 3:
            return "40"

        return "0"

    def puntuacion_jugador_uno(self):
        self.la_puntuacion_jugador_uno_es += 1


    def puntuacion_jugador_dos(self):
        self.la_puntuacion_jugador_dos_es += 1
