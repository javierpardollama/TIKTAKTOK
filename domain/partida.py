from domain import Casilla
from domain.jugador import Jugador


class Partida:

    rejilla: int = 3

    def __init__(self) -> None:
        self.tablero: list[Casilla] = []

        for i in range(self.rejilla):
            for j in range(self.rejilla):
                self.tablero.append(Casilla(i, j, Jugador.N, False))

    def __str__(self) -> None:
        for i in self.tablero:
            print(i.__str__())

    def __buscar__(self, columna: int, fila: int) -> bool:
        obj = next(filter(lambda item: item.columna == columna & item.fila == fila & (not item.activada), self.tablero))
        return obj is not None

    def __activar__(self, columna: int, fila: int, jugador: Jugador) -> None:
        idx = map(lambda item: item.columna == columna & item.fila == fila & (not item.activada), self.tablero).index(
            True)

        self.tablero[idx].jugador = jugador
        self.tablero[idx].activada = True

    def __completo__(self) -> bool:
        return len(filter(lambda item: item.activada, self.tablero)) == (self.rejilla ** self.rejilla)

    def __ganar__(self,jugador:Jugador) -> bool:
        vertical:bool = self.__vertical__(jugador)
        horizontal:bool = self.__horizontal__(jugador)
        izq_diagonal:bool = self.__izq_diagonal__(jugador)
        dere_diagonal:bool = self.__dere_diagonal__(jugador)

        return vertical | horizontal | izq_diagonal | dere_diagonal

    def __vertical__(self, jugador: Jugador) -> bool:
        bandera: bool = False

        itera: int = 0

        while itera <= self.rejilla | (not bandera):
            bandera = len(filter(lambda item: item.activada & item.Jugador == jugador & item.columna == itera, self.tablero)) == self.rejilla

            itera+=itera

        return bandera

    def __horizontal__(self, jugador: Jugador) -> bool:
        bandera: bool = False

        itera: int = 0

        while itera <= self.rejilla | (not bandera):
            bandera = len(filter(lambda item: item.activada & item.Jugador == jugador & item.fila == itera, self.tablero)) == self.rejilla

            itera += itera

        return bandera

    def __izq_diagonal__(self, jugador: Jugador)-> bool:
        bandera:bool = len(filter(lambda item: item.activada & item.Jugador == jugador & item.fila == item.columna, self.tablero)) == self.rejilla

        return bandera

    def __dere_diagonal__(self, jugador: Jugador)-> bool:
        bandera: bool = False

        for i in range(self.rejilla):
            for j in range(self.rejilla):
                diagonal: list[Casilla] = []

        return bandera