from typing import Callable
from components.button import Button, Coordinates
from utils.board import Board


class GameButton(Button):
    __x: int
    __y: int

    def __init__(self, topleft: Coordinates, x: int, y: int) -> None:
        super().__init__(topleft)
        self.__x = x
        self.__y = y

    def get_on_click(self, board: Board) -> Callable:
        x = self.__x
        y = self.__y

        def on_click():
            nonlocal board
            nonlocal x
            nonlocal y

            board.play(x, y)

        return on_click
