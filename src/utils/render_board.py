from pygame import SurfaceType
from pygame.rect import RectType
from components.game_button import GameButton
from game import Game
from settings import PADDING
from utils.board import Board


def render_board(surface: SurfaceType, cors: RectType, board: Board, game: Game):
    """
    Renderiza el tablero de juego de 3x3 en la superficie proporcionada.
    Cada posición del tablero está representada por un botón, al cual se le asigna
    una función al hacer clic y se posiciona en la cuadrícula del juego.

    Parámetros:
        surface (SurfaceType): Superficie de Pygame donde se dibujará el tablero.
        cors (RectType): Rectángulo con las coordenadas para el tablero.
        board (Board): Instancia del tablero con la lógica de juego.
        game (Game): Instancia del juego que maneja la ventana y los elementos.

    Retorno:
        Ninguno
    """
    for i in range(3):
        for j in range(3):
            button = GameButton(cors.topleft, i, j)
            button.on_click = button.get_on_click(board)
            button.insert_play(board)
            game.blit_button(
                surface,
                button,
                x=i * (button.surface.get_width() + PADDING),
                y=j * (button.surface.get_height() + PADDING),
            )
    else:
        game.blit_surface(surface, cors)
