from domain.jugador import Jugador


class Casilla:
    def __init__(self, columna: int = 0,
                 fila: int = 0,
                 jugador: Jugador = Jugador.N,
                 activada: bool = False) -> None:
        self.columna = columna
        self.fila = fila
        self.jugador = jugador
        self.activada = activada

    def __str__(self) -> str:
        return f"{self.columna}\n{self.fila}\n{self.jugador}\n{self.activada}\n"
