from domain import Partida
from domain.jugador import Jugador

class Teclado:
    salir: bool = False

    def __init__(self):
        self.partida = Partida()

    def __jugar__(self):


        return None

    def __intro_casilla__(self, jugador: Jugador) -> None:
        disponible: bool = False

        fila: int | None = None
        columna: int | None = None

        print(f'Tu turno jugador {jugador}\n')

        while (not disponible) | (fila is None) | (columna is None):

            columna = int(input('Elige tu Columna'))

            fila = int(input('Elige tu fila'))

            disponible = self.partida.__buscar__(columna, fila)

            if not disponible:
                print('Casilla no disponible. Ya está seleccionada. Vuelve a intertarlo')

        if disponible:
            self.partida.__activar__(columna, fila, jugador)
