import pygame
from sys import exit

from pygame.event import Event
from game import Game
from components.button import Button


def main():
    pygame.init()

    game = Game("Triki!")
    surface_center, center_cors = game.create_center_surface(x=900, y=900)

    start = Button(center_cors.topleft)
    start.insert_text("Iniciar Juego!", 16, "yellow")

    def on_start():
        print("Start Game!")

    start.on_click = on_start

    game.blit_button(
        surface_center,
        start,
        x=surface_center.get_width() // 2 - start.surface.get_width() // 2,
        y=surface_center.get_height() // 2 - start.surface.get_height() // 2,
    )

    quit = Button(center_cors.topleft)
    quit.insert_text("Quit!", 16, "yellow")

    def on_quit():
        pygame.quit()
        exit()

    quit.on_click = on_quit
    game.blit_button(
        surface_center,
        quit,
        x=surface_center.get_width() // 2 - quit.surface.get_width() // 2,
        y=((surface_center.get_height() // 2) + start.surface.get_height() + 20)
        - quit.surface.get_height() // 2,
    )

    def on_click(event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for button in game.buttons:
                if button.is_clicked(mouse_pos):
                    button.click()

    game.blit_surface(surface_center, center_cors)
    game.on_click = on_click
    game.init()


if __name__ == "__main__":
    main()
