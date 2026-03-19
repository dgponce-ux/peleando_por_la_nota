#comando para probar el test

#python -m unittest discover -s test

#python -m unittest discover -s test -v miro todos los test

import unittest
from src.Jugador import Jugador

class TestJugador(unittest.TestCase):

    #personaje = Personaje(10) -- no se usa asi, acordarse de los hambitos

    def setUp(self):
        #prepara el set de datos, con el que heremos las pruebas
        self.jugador = Jugador("Alan", 100)

        