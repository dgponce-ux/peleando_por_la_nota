
from src.Personaje import Personaje


class Jugador(Personaje):
    "Clase que representa al jugador, hereda de personaje"
    def __init__(self, nombre, fuerza, ataque):
        "constructor de la clase jugador, recibe un parametro de nombre, fuerza, ataque"
        super().__init__(nombre, 100)
        self.posicion_x = 0
        self.fuerza = fuerza
        self.ataque = ataque

    def calcularDanio(self):
        danio = self.fuerza + self.ataque
        return danio

    def actualizar(self):
        if self.vida < 0:
            self.morir()
        self.resetearEstado()

    def resetearEstado(self):
        self.esta_atacando = False
        self.esta_bloqueando = False

    def mostrar_estado(self):
        super().mostrar_estado()
        print(f"{self.nombre}: Vida = {self.vida}/{self.vida_maxima}, Fuerza={self.fuerza}, Ataque={self.ataque}")

