import unittest;

from partida_bolos import Partida


class PartidaBolos(unittest.TestCase):
    def test_partida_basica(self):
        partida = Partida()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 0)

    def test_partida_1_punto(self):
        partida = Partida()
        ronda = [(0, 0), (0, 0), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 1)

    def test_partida_varios_puntos(self):
        partida = Partida()
        ronda = [(0, 0), (7, 0), (0, 1), (5, 4), (3, 2), (7, 0), (2, 1), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 32)

    def test_partida_con_strike(self):
        partida = Partida()
        ronda = [(0, 0), (10, 0), (2, 1), (5, 4), (3, 2), (7, 0), (2, 1), (10, 0), (4, 5), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 68)

    def test_partida_con_spare(self):
        partida = Partida()
        ronda = [(0, 0), (5, 0), (2, 1), (5, 5), (3, 2), (7, 0), (2, 1), (8, 2), (4, 5), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 59)

    def test_partida_con_2_strike(self):
        partida = Partida()
        ronda = [(0, 0), (10, 0), (10, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 33)

    def test_partida_con_2_spire(self):
        partida = Partida()
        ronda = [(0, 0), (5, 5), (5, 5), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 27)

    def test_partida_con_strike_y_spare_seguido(self):
        partida = Partida()
        ronda = [(0, 0), (10, 0), (5, 5), (2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 34)

    def test_partida_con_spare_y_strike_seguido(self):
        partida = Partida()
        ronda = [(0, 0), (5, 5), (10, 0), (3, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 40)

    def test_partida_con_3_spire_seguidos(self):
        partida = Partida()
        ronda = [(0, 0), (5, 5), (5, 5), (8, 2), (2, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 50)

    def test_partida_con_ronda_3_strike_seguidos(self):
        partida = Partida()
        ronda = [(10, 0), (10, 0), (10, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 65)

    def test_partida_con_que_ronda_extra_normalita(self):
        partida = Partida()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 0), (5, 2)]
        resultado = partida.calcularResultado(ronda)
        self.assertEquals(resultado, 17)

    def test_partida_con_ronda_extra_tras_strike(self):
        partida = Partida()
        ronda = [(0, 0), (5, 0), (2, 1), (5, 5), (3, 2), (7, 0), (2, 1), (8, 2), (4, 5), (10, 0), (5, 4)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 78)

    def test_partida_con_2_rondas_extras_tras_strike(self):
        partida = Partida()
        ronda = [(0, 0), (5, 0), (2, 1), (5, 5), (3, 2), (7, 0), (2, 1), (8, 2), (4, 5), (10, 0), (10, 0),(0,0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 79)

    def test_partida_con_ronda_extra_spare(self):
        partida = Partida()
        ronda = [(0, 0), (5, 0), (2, 1), (5, 5), (3, 2), (7, 0), (2, 1), (8, 2), (4, 5), (5, 5), (5, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 74)

    def test_partida_con_ronda_extra_spare2(self):
        partida = Partida()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 15)

    def test_partida_con_ronda_extra_3_strikes_finales(self):
        partida = Partida()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 0), (10, 0), (10, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 30)

    def test_partida_con_mas_10_bolos(self):
        partida = Partida()
        ronda = [(0, 0), (0, 0), (9, 10), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularResultado(ronda)
        self.assertFalse(resultado, 19) #Excepción

    def test_partida_sucesion_de_strikes_y_spares(self):
        partida = Partida()
        ronda = [(10, 0), (5, 5), (9, 1), (10, 0), (10, 0), (10, 0), (4, 6), (5, 5), (10, 0), (10, 0), (10, 0), (10, 0)]
                # 20       19      20       30       24       20       15      20      30       30
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 228)

    def test_partida_perfecta(self):
        partida = Partida()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0)]
                #30        30(60)   30(90)  30(120)  30(150)  30(180)  30(210)  30(240)  30(270)  10-->10   10       10
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 300)

    def test_partida_casi_perfecta(self):
        partida = Partida()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (9, 0)]
                #30        30(60)   30(90)  30(120)  30(150)  30(180)  30(210)  30(240)  30(270)  10-->10   10       9
        resultado = partida.calcularResultado(ronda)
        self.assertEqual(resultado, 299)
