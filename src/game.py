from typing import List, Optional
import pygame
from sys import exit

from pygame.event import Event
from pygame.rect import RectType
from pygame.surface import SurfaceType

from screen import Screen
from color import ColorValue
from components.button import Button


class Game(Screen):
    __buttons: List[Button] = []

    def __init__(self, title: str) -> None:
        super().__init__(title)

    @property
    def buttons(self):
        return self.__buttons

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

    def blit_surface(self, surface: SurfaceType, cors: RectType):
        game.screen.blit(surface, cors)

    def blit_button(self, surface: SurfaceType, button: Button, x: int = 0, y: int = 0):
        self.__buttons.append(button)
        button.blit(surface, x, y)


if __name__ == "__main__":
    pygame.init()

    game = Game("Triki!")
    surface_center, center_cors = game.create_center_surface()

    button = Button("PlayButton.png", center_cors.topleft)
    button.insert_text("quit!", 16, "yellow")

    def on_quit():
        pygame.quit()
        exit()

    button.on_click = on_quit

    surface_width, surface_height = surface_center.get_size()

    game.blit_button(
        surface_center,
        button,
        x=surface_width // 2 - button.surface.get_width() // 2,
        y=surface_height // 2 - button.surface.get_height() // 2,
    )
    game.blit_surface(surface_center, center_cors)

    def on_click(event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for button in game.buttons:
                if button.is_clicked(mouse_pos):
                    button.click()

    game.on_click = on_click

    game.init()
