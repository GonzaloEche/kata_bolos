import unittest;

from serv2 import Servidor

class TestServidor(unittest.TestCase):

    def test_contador1(self):
        servidor = Servidor()
        frase = ("a")
        frase_count = servidor.contador(frase)
        self.assertEqual(frase_count, "a    1")

    def test_contador_mayuscula(self):
        servidor = Servidor()
        frase = ("A")
        frase_count = servidor.contador(frase)
        self.assertEqual(frase_count, "a    1")
    
    def test_contador_tilde(self):
        servidor = Servidor()
        frase = ("á")
        frase_count = servidor.contador(frase)
        self.assertEqual(frase_count, "a    1")
    

