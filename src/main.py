import pygame
from game import Game
from components.button import Button


def main():
    pygame.init()
    game = Game("Triki!")
    buttons_surface, center_cors = game.create_center_surface()
    buttons_surface.fill((1, 1, 1))

    screen_height = buttons_surface.get_height()

    start = Button("PlayButton.png")
    start.insert_text("Iniciar!", 17, "yellow")
    start.blit(
        buttons_surface,
        x=buttons_surface.get_width() // 2 - start.surface.get_width() // 2,
        y=screen_height // 2 - start.surface.get_height(),
    )

    quit = Button("PlayButton.png")
    quit.insert_text("Salir!", 17, "yellow")
    quit.blit(
        buttons_surface,
        x=buttons_surface.get_width() // 2 - start.surface.get_width() // 2,
        y=screen_height // 2 + 20,
    )

    game.screen.blit(buttons_surface, center_cors)

    game.init()


if __name__ == "__main__":
    main()
