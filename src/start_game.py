import pygame
from sys import exit
from pygame.event import Event
from game import Game
from components.button import Button
from settings import BUTTON_HEIGHT, BUTTON_WIDTH, PADDING
from utils.render_board import render_board
from utils.get_turn_surface import get_turn_surface
from utils import Board


def start_game():
    game = Game("Triki!")
    surface_center, center_cors = game.create_center_surface(
        x=(BUTTON_WIDTH * 3) + PADDING * 2,
        y=(BUTTON_HEIGHT * 3) + PADDING * 2,
    )

    buttons_surface = game.create_surface(surface_center.get_width(), y=200)
    button_cors = buttons_surface.get_rect(bottomleft=center_cors.topleft)

    quit_button = Button(button_cors.topleft)

    quit_button.insert_text("¡Salir!", 16, "yellow")

    def on_quit():
        pygame.quit()
        exit()

    quit_button.on_click = on_quit

    game.blit_button(
        buttons_surface,
        quit_button,
        x=(buttons_surface.get_width() // 2) - quit_button.surface.get_width() // 2,
        y=(buttons_surface.get_height() // 2) - quit_button.surface.get_height() // 2,
    )

    board = Board()

    # render_turn = get_turn_surface(game, center_cors)

    render_board(surface_center, center_cors, board, game)

    game.blit_surface(surface_center, center_cors)
    game.blit_surface(buttons_surface, button_cors)
    # render_turn(board.turn)

    def on_click(event: Event):
        mouse_pos = pygame.mouse.get_pos()

        for button in game.buttons:
            if button.is_hover(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.click()
                    render_board(surface_center, center_cors, board, game)
                    # render_turn(board.turn)

                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    game.on_click = on_click

    game.init()


if __name__ == "__main__":
    start_game()
