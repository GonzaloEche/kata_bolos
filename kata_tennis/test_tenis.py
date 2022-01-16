import unittest;

from partido_tenis import Tenis

class PartidoTennis(unittest.TestCase):
    def setUp(self):
        self.tenis = Tenis()

    def test_tenis_puntuacion_juego_0(self):
        self.la_puntuacion_es(0,0)

    def test_tenis_puntuacion_juego_15_jugador1(self):
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es(15,0)

    def test_tenis_puntuacion_juego_30_jugador1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es(30,0)

    def test_tenis_puntuacion_juego_40_jugador1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es(40,0)



    def test_tenis_puntuacion_juego_15_jugador2(self):
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(0,15)

    def test_tenis_puntuacion_juego_30_jugador2(self):
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(0,30)

    def test_tenis_puntuacion_juego_40_jugador2(self):
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(0,40)


    def test_tenis_puntuacion_15_15(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(15,15)

    def test_tenis_puntuacion_30_30(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(30,30)

    def test_tenis_puntuacion_40_40(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(40,40)

    def test_tenis_puntuacion_40_15(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(40,15)

    def test_tenis_puntuacion_ADV_J1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("ADV", 40)

    def test_tenis_puntuacion_Deuce_despues_de_ADVJ1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(40, 40)

    def test_tenis_puntuacion_ADV_despues_de_DEUCE(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es(40, "ADV")

    def test_tenis_puntuacion_W_15(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("W",15)

    def test_tenis_puntuacion_ADV_J1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("ADV", 40)
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("W",40)

    def test_tenis_puntuacion_Juego_1_J1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("ADV", 40)
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("W",40)
        self.los_juegos_son(1,0)
        self.sets_son(0,0)

    def test_tenis_puntuacion_partido_set_1_0(self):
        self.tenis.juegosJ1=6
        self.tenis.juegosJ2=0
        self.los_juegos_son(6,0)
        self.sets_son(1,0)


    def la_puntuacion_es(self, J1,J2):
       self.assertEqual(self.tenis.puntuacionJ1(), J1) and self.assertEqual(self.tenis.puntuacionJ2(), J2)

    def los_juegos_son(self,juegos_J1,juegos_J2):
        self.assertEqual(self.tenis.punt_juegos("J1"),juegos_J1) and self.assertEqual(self.tenis.punt_juegos("J2"),juegos_J2)

    def sets_son(self,sets_J1,sets_J2):
        self.assertEqual(self.tenis.punt_set("J1"), sets_J1) and self.assertEqual(self.tenis.punt_set("J2"), sets_J2)





