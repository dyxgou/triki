from typing import Callable, Optional, Tuple
from pygame import SurfaceType, transform as image_transform
import pygame
from pygame.event import Event
from pygame.surface import Surface


from screen import Screen
from settings import get_font, get_image
from color import ColorValue
from errors.button_errors import ButtonNotRederedException

Coordinates = Tuple[int, int]


class Button:
    __surface: SurfaceType
    __text_surface: SurfaceType
    __right_corner: SurfaceType
    __left_corner: SurfaceType
    __on_click: Optional[Callable]
    __topleft: Coordinates
    __coordinates: Optional[Coordinates] = None

    def __init__(self, topleft: Coordinates) -> None:
        self.__text_surface = get_image("TextButton.png")
        self.__right_corner = get_image("RightCorner.png")
        self.__left_corner = get_image("LeftCorner.png")
        self.__surface = Surface(
            (
                self.__left_corner.get_width()
                + self.__text_surface.get_width()
                + self.__right_corner.get_width(),
                self.__text_surface.get_height(),  # height
            ),
            pygame.SRCALPHA,
        )

        self.__topleft = topleft

    def _blit_text(self):
        self.__surface = Surface(
            (
                self.__left_corner.get_width()
                + self.__text_surface.get_width()
                + self.__right_corner.get_width(),
                self.__text_surface.get_height(),  # height
            ),
            pygame.SRCALPHA,
        )

        self.__surface.blits(
            (
                (self.__left_corner, (0, 0)),
                (self.__text_surface, (self.__left_corner.get_width(), 0)),
                (
                    self.__right_corner,
                    (
                        self.__text_surface.get_width()
                        + self.__left_corner.get_width(),
                        0,
                    ),
                ),
            )
        )

    def is_hover(self, mouse_pos: Coordinates):
        if self.__coordinates is None:
            raise ButtonNotRederedException("El botón no ha sido renderizado.")

        mouse_x, mouse_y = mouse_pos
        cor_x, cor_y = self.__topleft

        button_x, button_y = self.__coordinates
        cor_x = cor_x + button_x
        cor_y = cor_y + button_y

        relative_pos = (mouse_x - cor_x, mouse_y - cor_y)

        return self.surface.get_rect().collidepoint(relative_pos)

    @property
    def on_click(self):
        self.__on_click = None
        return self.__on_click

    @on_click.setter
    def on_click(self, on_click: Callable):
        self.__on_click = on_click

    def click(self):
        if self.__on_click is None:
            return

        self.__on_click()

    @property
    def surface(self):
        return self.__surface

    def insert_text(
        self, text_content: str, size: int = 16, color: ColorValue = "white"
    ):
        font = get_font(size)
        text = font.render(text_content, True, color)
        text_width, text_height = text.get_size()

        ACCEPTABLE_TEXT_PADDING = 15

        text_surface_width = self.__text_surface.get_width()

        if text_width + ACCEPTABLE_TEXT_PADDING > text_surface_width:
            self.__text_surface = image_transform.smoothscale(
                self.__text_surface,
                (
                    (text_surface_width // 2) + text_width,
                    self.__text_surface.get_height(),
                ),
            )

        text_center_cors = text.get_rect(
            center=(
                (self.__text_surface.get_width() // 2),
                (self.__text_surface.get_height() // 2) - (text_height // 3),
            )
        )

        self.__text_surface.blit(text, text_center_cors)
        self._blit_text()

    def blit(self, surface: SurfaceType, x: int = 0, y: int = 0):
        self.__coordinates = (x, y)
        surface.blit(self.__surface, (x, y))


if __name__ == "__main__":
    screen = Screen("test button!")

    topleft = screen.screen.get_rect().topleft
    button = Button(topleft)
    button.insert_text("O", 30, "yellow")
    button.blit(screen.screen)

    button2 = Button(topleft)
    button2.insert_text("X", 30, "yellow")
    button2.blit(screen.screen, y=150)

    button3 = Button(topleft)
    button3.insert_text("", 30, "yellow")
    button3.blit(screen.screen, y=300)

    def on_click(event: Event):
        pass

    screen.on_click = on_click
    screen.init()
