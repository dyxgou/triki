import pygame
from screen import Screen
from color import ColorValue


class Game(Screen):
    def __init__(self, title: str) -> None:
        super().__init__(title)

    def create_center_surface(
        self, x: int = 500, y: int = 500, bg_color: ColorValue = (0, 0, 0)
    ):
        new_surface = pygame.Surface((x, y))
        center_cors = new_surface.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        new_surface.fill(bg_color)

        return (new_surface, center_cors)
