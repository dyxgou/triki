from pygame.rect import RectType
from game import Game
from components.button import Button


def get_turn_surface(game: Game, cors: RectType):
    turn_surface = game.create_surface()
    turn_cors = turn_surface.get_rect(topleft=cors.topleft)

    turn_text = Button(turn_cors.topleft)

    def render_turn(turn: int):
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
