from pygame import SurfaceType
from pygame.rect import RectType
from components.game_button import GameButton
from game import Game
from settings import PADDING
from utils.board import Board


def render_board(surface: SurfaceType, cors: RectType, board: Board, game: Game):
    for i in range(3):
        for j in range(3):
            button = GameButton(cors.topleft, i, j)
            button.on_click = button.get_on_click(board)
            print(board.get_play(i, j))
            button.insert_play(board)
            game.blit_button(
                surface,
                button,
                x=i * (button.surface.get_width() + PADDING),
                y=j * (button.surface.get_height() + PADDING),
            )
    else:
        game.blit_surface(surface, cors)
