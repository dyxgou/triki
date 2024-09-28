from enum import Enum
from typing import List

from errors.button_errors import EmptyPlayException


class Plays(Enum):
    """
    Enumeración para representar el estado de una posición en el tablero.
    Puede ser vacío (EMPTY), jugada de X o jugada de O.
    """
    EMPTY = 0
    X = 1
    O = 2


ROWS = 3


class Board:
    """
    Clase que representa el tablero del juego.
    
    Atributos:
        __board (List[Plays]): Lista que almacena el estado de cada posición del tablero.
        __turn (int): Turno actual del juego (1 para X, 2 para O).
    
    Métodos:
        turn(): Propiedad que retorna el turno actual.
        __get_index(x: int, y: int): Convierte coordenadas en el índice correspondiente del tablero.
        __set_play(x: int, y: int, value: Plays): Asigna una jugada en la posición especificada.
        play(x: int, y: int): Realiza una jugada en una posición dada y cambia el turno.
        get_play(x: int, y: int): Devuelve la jugada en una posición específica.
    """

    __board: List[Plays]
    __turn: int = 1  # El turno de las X siempre será impar y el de las O será par

    @property
    def turn(self):
        """
        Propiedad que retorna el turno actual del juego.
        """
        return self.__turn

    def __init__(self) -> None:
        """
        Inicializa el tablero con todas las posiciones vacías (EMPTY).
        """
        self.__board = [Plays.EMPTY] * (ROWS * ROWS)

    @staticmethod
    def __get_index(x: int, y: int) -> int:
        """
        Convierte las coordenadas (x, y) en un índice para la lista del tablero.
        
        Parámetros:
            x (int): Fila del tablero.
            y (int): Columna del tablero.
        
        Retorno:
            int: El índice correspondiente en la lista del tablero.
        """
        return (ROWS * x) + y

    def __set_play(self, x: int, y: int, value: Plays):
        """
        Asigna una jugada (X o O) en la posición (x, y) del tablero.
        
        Parámetros:
            x (int): Fila del tablero.
            y (int): Columna del tablero.
            value (Plays): Jugada a asignar (X o O).
        
        Excepciones:
            EmptyPlayException: Si se intenta asignar una jugada vacía.
        """
        index = self.__get_index(x, y)

        if value == Plays.EMPTY:
            raise EmptyPlayException(
                "No se puede asignar una jugada vacía otra vez al tablero"
            )

        self.__board[index] = value

    def play(self, x: int, y: int):
        """
        Realiza una jugada en la posición (x, y) del tablero.
        Alterna entre jugada de X y jugada de O, dependiendo del turno actual.
        
        Parámetros:
            x (int): Fila del tablero.
            y (int): Columna del tablero.
        """
        index = self.__get_index(x, y)

        if self.__board[index] != Plays.EMPTY:
            return

        is_o_turn = self.__turn % 2 == 0
        self.__turn = self.__turn + 1
        self.__turn += 1

        if is_o_turn:
            self.__set_play(x, y, Plays.O)
        else:
            self.__set_play(x, y, Plays.X)

    def get_play(self, x: int, y: int) -> Plays:
        """
        Devuelve la jugada realizada en la posición (x, y) del tablero.
        
        Parámetros:
            x (int): Fila del tablero.
            y (int): Columna del tablero.
        
        Retorno:
            Plays: Estado de la posición (X, O o vacío).
        """
        shifted_index = self.__get_index(x, y)

        return self.__board[shifted_index]


if __name__ == "__main__":
    board = Board()

    board.play(2, 2)
    board.play(0, 2)

    for i in range(3):
        for j in range(3):
            print(board.get_play(i, j))
