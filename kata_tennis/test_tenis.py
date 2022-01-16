import unittest;

from partido_tenis import Tenis

class PartidoTennis(unittest.TestCase):
    def setUp(self):
        self.tenis = Tenis()

    def test_tenis_puntuacion_juego_0(self):
        self.la_puntuacion_es("0")

    def test_tenis_puntuacion_juego_15_jugador1(self):
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("15")

    def test_tenis_puntuacion_juego_30_jugador1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("30")

    def test_tenis_puntuacion_juego_40_jugador1(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_uno()
        self.la_puntuacion_es("40")



    def test_tenis_puntuacion_juego_15_jugador2(self):
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es("15")

    def test_tenis_puntuacion_juego_30_jugador2(self):
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es("30")

    def test_tenis_puntuacion_juego_40_jugador2(self):
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es("40")


    def test_tenis_puntuacion_15_15(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es("15-15")

    def test_tenis_puntuacion_30_30(self):
        self.tenis.puntuacion_jugador_uno()
        self.tenis.puntuacion_jugador_dos()
        self.la_puntuacion_es("iguales")

    def la_puntuacion_es(self, tiene_que_ser):
        self.assertEqual(self.tenis.puntuacion(), tiene_que_ser)









