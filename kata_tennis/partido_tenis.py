

class Tenis(object):
    def __init__(self):
        self.la_puntuacion_jugador_uno_es = 0
        self.la_puntuacion_jugador_dos_es = 0
        self.juegosJ1 = 0
        self.juegosJ2 = 0
        self.setJ1 = 0
        self.setJ2 = 0

    def puntuacion_jugador_uno(self):
        if (self.juegosJ1 != 6 and self.juegosJ2 != 6): # puntuación normal
            if (self.la_puntuacion_jugador_uno_es == 5):
                self.la_puntuacion_jugador_uno_es += 1
            if (self.la_puntuacion_jugador_uno_es == 3 and self.la_puntuacion_jugador_dos_es == 3):
                self.la_puntuacion_jugador_uno_es += 2
            if (self.la_puntuacion_jugador_dos_es == 5):
                self.la_puntuacion_jugador_dos_es -= 2 #volvemos a 40
            if(self.la_puntuacion_jugador_uno_es !=5):
                self.la_puntuacion_jugador_uno_es += 1

        if (self.juegosJ1 == 6 and self.juegosJ2 == 6): # puntuación en tie break
            self.la_puntuacion_jugador_uno_es += 1 #


    def puntuacion_jugador_dos(self):
        if (self.juegosJ1 != 6 and self.juegosJ2 != 6):  # p. normal
            if (self.la_puntuacion_jugador_dos_es == 5):
                self.la_puntuacion_jugador_dos_es += 1
            if (self.la_puntuacion_jugador_dos_es == 3 and self.la_puntuacion_jugador_uno_es == 3):
                self.la_puntuacion_jugador_dos_es += 2
            if (self.la_puntuacion_jugador_uno_es == 5):
                self.la_puntuacion_jugador_uno_es -= 2  #volvemos a 40
            if (self.la_puntuacion_jugador_dos_es != 5):
                self.la_puntuacion_jugador_dos_es += 1

            if (self.juegosJ1 == 6 and self.juegosJ2 == 6):  # p. tie break
                self.la_puntuacion_jugador_dos_es += 1

    def puntuacionJ1(self): # jugador 1
        if (self.juegosJ1 != 6 and self.juegosJ2 != 6):  # mapeo normal
            if self.la_puntuacion_jugador_uno_es == 1:
                return 15
            if self.la_puntuacion_jugador_uno_es == 2:
                return 30
            if self.la_puntuacion_jugador_uno_es == 3:
                return 40
            if self.la_puntuacion_jugador_uno_es == 5:
                return "ADV"
            if self.la_puntuacion_jugador_uno_es == 4:
                return "W"
            if self.la_puntuacion_jugador_uno_es == 7:
                return "W"

        if (self.juegosJ1 == 6 and self.juegosJ2 == 6): #mapeo tie break
            if (self.la_puntuacion_jugador_uno_es >= 7) and  (self.la_puntuacion_jugador_uno_es - self.la_puntuacion_jugador_dos_es)>=2:
                return "W"
            else: return self.la_puntuacion_jugador_uno_es

        return 0

    def puntuacionJ2(self): # jugador 2
        if (self.juegosJ1 != 6 and self.juegosJ2 != 6):  # m.normal
            if self.la_puntuacion_jugador_dos_es == 1:
                return 15
            if self.la_puntuacion_jugador_dos_es == 2:
                return 30
            if self.la_puntuacion_jugador_dos_es == 3:
                return 40
            if self.la_puntuacion_jugador_uno_es == 5:
                return "ADV"
            if self.la_puntuacion_jugador_dos_es == 4:
                return "W"
            if self.la_puntuacion_jugador_dos_es == 7:
                return "W"

        if (self.juegosJ1 == 6 and self.juegosJ2 == 6): #m. tie break
            if (self.la_puntuacion_jugador_dos_es >= 7) and  (self.la_puntuacion_jugador_dos_es - self.la_puntuacion_jugador_uno_es)>=2:
                return "W"
            else: return self.la_puntuacion_jugador_dos_es
        return 0

    def punt_juegos(self, jugador):
        if self.puntuacionJ1() == "W":
            self.juegosJ1 += 1
            self.la_puntuacion_jugador_uno_es = 0
            self.la_puntuacion_jugador_dos_es = 0

        if self.puntuacionJ2() == "W":
            self.juegosJ2 += 1
            self.la_puntuacion_jugador_uno_es = 0
            self.la_puntuacion_jugador_dos_es = 0
        if (jugador == "J1"):
            return self.juegosJ1
        if (jugador == "J2"):
            return self.juegosJ2

    def punt_set(self, jugador):
        if ((self.punt_juegos("J1") == 6 and self.punt_juegos("J2") != 5 and (self.punt_juegos("J2") != 6)) or (self.punt_juegos("J1") == 7)):  # condiciones para ganar un set
            self.setJ1 += 1
            self.juegosJ1=0
            self.juegosJ2=0

        if ((self.punt_juegos("J2") == 6 and ((self.punt_juegos("J1") != 5) and (self.punt_juegos("J1") != 6))) or (self.punt_juegos("J2") == 7)):  # condiciones para ganar un set
            self.setJ2+= 1
            self.juegosJ2 = 0
            self.juegosJ2 = 0

        if (jugador == "J1"):
            return self.setJ1
        if (jugador == "J2"):
            return self.setJ2

