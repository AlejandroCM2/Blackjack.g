import random

class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta = pinta
        self.valor = valor
        self.tapada = False

class Baraja:
    def __init__(self):
        self.cartas = []

    def revolver(self):

        pass

    def repartir_carta(self, tapada: bool) -> Carta:

        pass

class Mano:
    def __init__(self):
        self.cartas = []

    def es_blackjack(self):
        pass

    def valor_mano(self):
        pass

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()
        self.fichas = 1000

    def apostar(self, apuesta):
        pass

class Casa:
    def __init__(self):
        self.mano = Mano()

    def inicializar_mano(self, cartas):
        pass

    def hacer_jugada_casa(self):
        pass

class Blackjack:
    def __init__(self):
        self.jugadores = []
        self.baraja = Baraja()
        self.jugador_actual = None
        self.apuesta_actual = 0
        self.juego_terminado = False

    def registrar_jugador(self, nombre):
        pass

    def iniciar_juego(self, apuesta):
        pass

    def hacer_jugada_jugador(self, tipo_jugada):
        pass

    def hacer_jugada_casa(self):
        pass

    def finalizar_juego(self):
        pass

    def mostrar_jugador(self):
        pass
