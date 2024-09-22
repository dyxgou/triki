import pygame
from pygame.event import Event
from game import Game
from components.button import Button


def main():
    pygame.init()

    game = Game("Triki!")
    surface_center, center_cors = game.create_center_surface()

    start = Button("PlayButton.png", center_cors.topleft)
    start.insert_text("Iniciar!", 16, "yellow")
    game.blit_button(
        surface_center,
        start,
        x=surface_center.get_width() // 2 - start.surface.get_width() // 2,
        y=surface_center.get_height() // 2 - start.surface.get_height() // 2,
    )

    quit = Button("PlayButton.png", center_cors.topleft)
    quit.insert_text("Quit!", 16, "yellow")
    game.blit_button(
        surface_center,
        quit,
        x=surface_center.get_width() // 2 - quit.surface.get_width() // 2,
        y=((surface_center.get_height() // 2) + start.surface.get_height() + 20)
        - quit.surface.get_height() // 2,
    )

    def on_click(event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")

    game.blit_surface(surface_center, center_cors)
    game.on_click = on_click
    game.init()


if __name__ == "__main__":
    main()
