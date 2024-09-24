import pygame
from pygame.event import Event
from game import Game
from components.button import Button

BUTTON_WIDTH = 130
BUTTON_HEIGHT = 105
PADDING = 20


def start_game():
    game = Game("Triki!")
    surface_center, center_cors = game.create_center_surface(
        x=(BUTTON_WIDTH * 3) + PADDING * 2,
        y=(BUTTON_HEIGHT * 3) + PADDING * 2,
    )

    for i in range(3):
        for j in range(3):
            button = Button(center_cors.topleft)
            print(button.surface.get_size())
            button.insert_text("")
            game.blit_button(
                surface_center,
                button,
                x=i * (button.surface.get_width() + PADDING),
                y=j * (button.surface.get_height() + PADDING),
            )

    game.blit_surface(surface_center, center_cors)

    def on_click(event: Event):
        mouse_pos = pygame.mouse.get_pos()

        for button in game.buttons:
            if button.is_hover(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    game.on_click = on_click

    game.init()


if __name__ == "__main__":
    start_game()
