from pygame.rect import RectType
from game import Game
from components.button import Button


def get_turn_surface(game: Game, cors: RectType):
    """
    Crea una superficie para mostrar el turno actual en el juego.

    Este método genera una superficie de juego donde se mostrará el texto 
    que indica el turno actual (ya sea el turno de 'X' o de 'O'). 
    El turno se alterna dependiendo del valor entero que representa el turno actual.

    Argumentos:
    - game (Game): Instancia del juego en curso que se encargará de gestionar la superficie.
    - cors (RectType): Coordenadas y dimensiones (rectángulo) donde se colocará la superficie del turno.
    Retorno:
    - Tuple[Surface, Rect, function]: Retorna la superficie creada, el rectángulo asociado a la superficie y una función `render_turn`.
    """


    turn_surface = game.create_surface()
    turn_cors = turn_surface.get_rect(topleft=cors.topleft)

    turn_text = Button(turn_cors.topleft)

    def render_turn(turn: int):
        """
        Función interna que actualiza el texto del turno en función del número de turno.

        Argumentos:
        - turn (int): Número entero que representa el turno actual.
        """
        nonlocal turn_text

        is_x_turn = turn % 2 == 0

        if is_x_turn:
            turn_text.insert_text("Es el turno de O", 17, "yellow")
        else:
            turn_text.insert_text("Es el turno de X", 17, "yellow")

        game.blit_surface(turn_surface, turn_cors)

    turn_surface.blit(
        turn_text.surface,
        (turn_surface.get_width() // 2, turn_surface.get_height() // 2),
    )

    return (turn_surface, turn_cors, render_turn)
