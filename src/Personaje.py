class Personaje:
    def __init__(self, nombre, vida_maxima):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida = vida_maxima
        self.esta_atacando = False
        self.esta_bloqueando = False

    def recibir_Danio(self, danio):
        if (danio < 0 ): 
            print("El daño no puede ser negativo")
    
        if self.esta_bloqueando:
            print(f"{self.nombre} bloqueó el daño!")
        else:
            self.vida = self.vida - danio
            if self.vida < 0:
                self.vida = 0
            print(f"{self.nombre} recibió {danio} de daño")

        if self.vida == 0:
            self.morir()

    def estoy_Vivo(self):
        # return self.vida > 0
        return True
    
    def mostrar_estado(self):
        return self.vida

    def atacar(self, enemigo):
        self.esta_atacando = True
        danio = 1
        enemigo.recibir_Danio(danio)

    def morir(self):
        # self.vida = 0
        print(f"{self.nombre} ha muerto!")
        return True
        
