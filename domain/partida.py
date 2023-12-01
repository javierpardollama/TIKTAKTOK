from domain import Casilla
from domain.jugador import Jugador

class Partida:

    rejilla:int = 3

    def __init__(self):
        self.tablero:list[Casilla] = []
        for i in range(self.rejilla):
            for j in range(self.rejilla):
                self.tablero.append(Casilla(i, j, Jugador.N, False))

    def __str__(self):
        for i in self.tablero:
            print(i.__str__())

    def __buscar__(self, columna:int, fila:int) -> bool:
        obj = next(filter(lambda item: item.columna == columna & item.fila == fila & item.activada, self.tablero))
        return obj is not None

    def __activar__(self, columna: int, fila: int, jugador: Jugador) -> None:
        self.tablero[columna][fila].jugador = jugador
        self.tablero[columna][fila].activada = True


    def __vertical__(self) -> bool:
        bandera:bool = False



        return bandera

    def __horizontal(self) -> bool:
        bandera: bool = False

        return bandera
