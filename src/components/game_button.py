from typing import Callable
from components.button import Button, Coordinates
from utils.board import Plays
from utils import Board


class GameButton(Button):
    __x: int
    __y: int

    def __init__(self, topleft: Coordinates, x: int, y: int) -> None:
        super().__init__(topleft)
        self.__x = x
        self.__y = y

    def insert_play(self, board: Board):
        play = board.get_play(self.__x, self.__y)

        if play == Plays.EMPTY:
            self.insert_text("", 16, "yellow")
        else:
            if play == Plays.X:
                self.insert_text("X", 25, "yellow")
            else:
                self.insert_text("O", 25, "yellow")

    def get_on_click(self, board: Board) -> Callable:
        x = self.__x
        y = self.__y

        def on_click():
            nonlocal board
            nonlocal y
            nonlocal x

            board.play(x, y)

        return on_click
