import pygame
from sys import exit

from pygame.event import Event
from game import Game
from components.button import Button
from start_game import start_game


def main():
    pygame.init()

    game = Game("Triki!")
    surface_center, center_cors = game.create_center_surface(x=900, y=900)

    start_button = Button(center_cors.topleft)
    start_button.insert_text("¡Jugar contra la Maquina!", 16, "yellow")

    start_button.on_click = start_game

    game.blit_button(
        surface_center,
        start_button,
        x=surface_center.get_width() // 2 - start_button.surface.get_width() // 2,
        y=surface_center.get_height() // 2 - start_button.surface.get_height() // 2,
    )

    versus_button = Button(center_cors.topleft)
    versus_button.insert_text("¡Versus!", 16, "yellow")

    def on_versus():
        print("Versus")

    versus_button.on_click = on_versus

    game.blit_button(
        surface_center,
        versus_button,
        x=surface_center.get_width() // 2 - versus_button.surface.get_width() // 2,
        y=((surface_center.get_height() // 2) + start_button.surface.get_height() + 20)
        - versus_button.surface.get_height() // 2,
    )

    quit_button = Button(center_cors.topleft)
    quit_button.insert_text("¡Salir!", 16, "yellow")

    def on_quit():
        pygame.quit()
        exit()

    quit_button.on_click = on_quit
    game.blit_button(
        surface_center,
        quit_button,
        x=surface_center.get_width() // 2 - quit_button.surface.get_width() // 2,
        y=(
            (surface_center.get_height() // 2)
            + start_button.surface.get_height()
            + versus_button.surface.get_height()
            + 30
        )
        - quit_button.surface.get_height() // 2,
    )

    def on_click(event: Event):
        mouse_pos = pygame.mouse.get_pos()
        for button in game.buttons:
            if button.is_hover(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.click()

                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    game.blit_surface(surface_center, center_cors)
    game.on_click = on_click
    game.init()


if __name__ == "__main__":
    main()
