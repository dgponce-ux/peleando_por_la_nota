#comando para probar el test

#python -m unittest discover -s test

#python -m unittest discover -s test -v miro todos los test

import unittest
from src.Personaje import Personaje

class TestPersonaje(unittest.TestCase):

    #personaje = Personaje(10) -- no se usa asi, acordarse de los hambitos

    def setUp(self):
        #prepara el set de datos, con el que heremos las pruebas
        self.personaje = Personaje("Alan", 100)
        self.personaje2 = Personaje("Eli", 100)
    
    def test_recibir_danio(self):
        self.personaje.recibir_Danio(10)
        self.assertEqual(self.personaje.vida,90)

    # def test_recibir_danio_mayor_vida(self):
    #     self.personaje.recibir_danio(15)
    #     self.assertEqual(self.personaje.vida, 0)

    def test_estoy_vivo(self):
        self.assertTrue(self.personaje.estoy_Vivo())

    def test_mostrar_estado(self):
        estado = self.personaje.mostrar_estado()
        self.assertEqual(100,estado)

    def test_atacar(self):
        self.personaje.atacar(self.personaje2)
        self.assertEqual(self.personaje2.vida,99)

    def test_morir(self):
        self.assertEqual(self.personaje.morir(), True)