from random import randrange
from domain import Rejilla, Constantes, Jugador


class Juego:
    def __init__(self):
        self.rejilla = Rejilla()

    def __check_cell__(self, columna: int, fila: int) -> bool:
        obj = next(filter(lambda item: item.columna == columna and item.fila == fila and not item.activada, self.rejilla.celdas))
        return obj is not None

    def __activate_cell__(self, columna: int, fila: int, jugador: Jugador) -> None:
        idx = map(lambda item: item.columna == columna and item.fila == fila and (not item.activada), self.rejilla.celdas).index(True)

        self.rejilla.celdas[idx].jugador = jugador
        self.rejilla.celdas[idx].activada = True

    def __check_filled__(self) -> bool:
        return len(filter(lambda item: item.activada, self.rejilla.celdas)) == (Constantes.TAMAÑO ** Constantes.TAMAÑO)

    def __check_win__(self, jugador: Jugador) -> bool:
        vertical: bool = self.__vertical__(jugador)
        horizontal: bool = self.__horizontal__(jugador)
        izq_diagonal: bool = self.__left_diagonal__(jugador)

        return vertical | horizontal | izq_diagonal

    def __vertical__(self, jugador: Jugador) -> bool:
        bandera: bool = False

        itera: int = 0

        while itera <= Constantes.TAMAÑO | (not bandera):
            bandera = len(filter(lambda item: item.activada and item.Jugador == jugador and item.columna == itera, self.rejilla.celdas)) == Constantes.TAMAÑO

            itera = itera + 1

        return bandera

    def __horizontal__(self, jugador: Jugador) -> bool:
        bandera: bool = False

        itera: int = 0

        while itera <= Constantes.TAMAÑO | (not bandera):
            bandera = len(filter(lambda item: item.activada and item.Jugador == jugador and item.fila == itera, self.rejilla.celdas)) == Constantes.TAMAÑO

            itera = itera + 1

        return bandera

    def __left_diagonal__(self, jugador: Jugador) -> bool:
        bandera: bool = len(filter(lambda item: item.activada and item.Jugador == jugador and item.fila == item.columna, self.rejilla.celdas)) == Constantes.TAMAÑO

        return bandera

    def __intro_human__(self) -> tuple[int, int]:
        columna: str = ""

        fila: str = ""

        while not columna.isnumeric() and columna not in  range(Constantes.TAMAÑO):
            columna = (input("******* Introduce tu columna **********  \n"))

        while not fila.isnumeric() and fila not in  range(Constantes.TAMAÑO):
            fila = (input("******* Introduce tu fila **********  \n"))

        return int(columna), int(fila)

    def __intro_computer__(self) -> tuple[int, int]:
        return randrange(Constantes.TAMAÑO), randrange(Constantes.TAMAÑO)

    def __activate_human__(self) -> None:
        columna,fila = self.__intro_human__()

        while not self.__check_cell__(columna, fila):
            columna, fila = self.__intro_human__()

        self.__activate_cell__(columna, fila, Jugador.HUMANO)

    def __activate_computer__(self) -> None:

        columna, fila = self.__intro_computer__()

        while not self.__check_cell__(columna, fila):
            columna, fila = self.__intro_computer__()

        self.__activate_cell__(columna, fila, Jugador.COMPUTADORA)

    def __play__(self) -> None:
        print(self.rejilla.__str__())

        while not self.__check_win__(Jugador.HUMANO) or self.__check_win__(Jugador.COMPUTADORA) or not self.__check_filled__():
            self.__activate_human__()
            self.__activate_computer__()
            self.__check_status__()


        print(self.rejilla.__str__())

    def __check_status__(self) -> None:
        if self.__check_win__() or self.__check_filled__():
            movimiento: str = ""

            while movimiento not in ["Y", "S", "N", "Q"]:
                movimiento = (input("\n" +
                                    "******* ¿Comenzar de nuevo? **********  \n" +
                                    "1. Y \n" +
                                    "2. S \n" +
                                    "3. N \n" +
                                    "4. Q \n")).upper()

                match movimiento:
                    case "Y":
                        self.__init__()
                        self.__play__()
                    case "S":
                        self.__init__()
                        self.__play__()
                    case "N":
                        self.stop()
                    case "Q":
                        self.stop()

    def stop(self) -> None:
        quit()
