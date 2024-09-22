from typing import List, Optional, Tuple
import pygame
from pygame.rect import RectType
from screen import Screen
from color import ColorValue
from components.button import Button


class Game(Screen):
    __surfaces: List[Tuple[pygame.SurfaceType, RectType]] = []

    def __init__(self, title: str) -> None:
        super().__init__(title)

    def create_center_surface(
        self,
        x: int = 500,
        y: int = 500,
        alpha: bool = False,
        color: Optional[ColorValue] = None,
    ):
        new_surface = pygame.Surface((x, y), pygame.SRCALPHA, 32)

        if alpha:
            new_surface = pygame.Surface.convert_alpha(new_surface)
        elif color is not None:
            new_surface.fill(color)

        center_cors = new_surface.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )

        return (new_surface, center_cors)

    def blit_button(
        self, surface: pygame.SurfaceType, button: Button, x: int = 0, y: int = 0
    ):
        self.__surfaces.append((button.surface, button.surface.get_rect()))
        button.blit(surface, x, y)


if __name__ == "__main__":
    pygame.init()
    game = Game("Triki!")
    buttons_surface, center_cors = game.create_center_surface()

    screen_height = buttons_surface.get_height()

    start = Button("PlayButton.png")
    start.insert_text("Iniciar!", 16, "yellow")
    game.blit_button(
        buttons_surface,
        start,
        x=buttons_surface.get_width() // 2 - start.surface.get_width() // 2,
        y=screen_height // 2 - start.surface.get_height(),
    )

    quit = Button("PlayButton.png")
    quit.insert_text("Salir!", 17, "yellow")
    game.blit_button(
        buttons_surface,
        quit,
        x=buttons_surface.get_width() // 2 - quit.surface.get_width() // 2,
        y=screen_height // 2 + 20,
    )

    game.screen.blit(buttons_surface, center_cors)

    game.init()
