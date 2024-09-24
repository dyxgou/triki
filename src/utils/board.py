from enum import Enum
from typing import List

from errors.button_errors import EmptyPlayException


class Plays(Enum):
    EMPTY = 0
    X = 1
    O = 2


ROWS = 3


class Board:
    __board: List[Plays]
    __turn: int = 1  # El turno de las X siempre será impar y el de las O será par

    def __init__(self) -> None:
        self.__board = [Plays.EMPTY] * (ROWS * ROWS)

    @staticmethod
    def __get_index(x: int, y: int) -> int:
        return (ROWS * x) + y

    def __set_play(self, x: int, y: int, value: Plays):
        index = self.__get_index(x, y)

        if value == Plays.EMPTY:
            raise EmptyPlayException(
                "No se puede asignar una jugada vacia otra vez al tablero"
            )

        self.__board[index] = value

    def play(self, x: int, y: int):
        index = self.__get_index(x, y)

        if self.__board[index] != Plays.EMPTY:
            return

        is_o_turn = self.__turn % 2 == 0
        self.__turn = self.__turn + 1

        if is_o_turn:
            self.__set_play(x, y, Plays.O)
        else:
            self.__set_play(x, y, Plays.X)

    def get_play(self, x: int, y: int) -> Plays:
        shifted_index = self.__get_index(x, y)

        return self.__board[shifted_index]


if __name__ == "__main__":
    board = Board()

    board.play(2, 2)
    board.play(0, 2)

    for i in range(3):
        for j in range(3):
            print(board.get_play(i, j))
