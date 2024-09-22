from typing import Callable, Optional, Tuple
from pygame import SurfaceType, transform as image_transform


from screen import Screen
from settings import get_font, get_image
from color import ColorValue
from errors.button_errors import ButtonNotRedered

Coordinates = Tuple[int, int]


class Button:
    __surface: SurfaceType
    __on_click: Optional[Callable]
    __topleft: Coordinates
    __coordinates: Optional[Coordinates] = None

    def __init__(self, background_name: str, topleft: Coordinates) -> None:
        self.__surface = get_image(background_name)
        self.__topleft = topleft

    def is_clicked(self, mouse_pos: Coordinates):
        if self.__coordinates is None:
            raise ButtonNotRedered("El botón no ha sido renderizado.")

        mouse_x, mouse_y = mouse_pos
        cor_x, cor_y = self.__topleft

        button_x, button_y = self.__coordinates
        cor_x = cor_x + button_x
        cor_y = cor_y + button_y

        relative_pos = (mouse_x - cor_x, mouse_y - cor_y)

        return self.surface.get_rect().collidepoint(relative_pos)

    @property
    def on_click(self):
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

    def insert_text(self, text_content: str, size: int, color: ColorValue):
        font = get_font(size)
        text = font.render(text_content, True, color)
        text_width, text_height = text.get_size()

        ACCEPTABLE_TEXT_PADDING = 20

        if text_width + ACCEPTABLE_TEXT_PADDING > self.__surface.get_width():
            self.__surface = image_transform.smoothscale(
                self.__surface,
                (self.__surface.get_width() + text_width, text_height * 5),
            )

        text_center_cors = text.get_rect(
            center=(
                self.__surface.get_width() // 2,
                self.__surface.get_height() // 2 - 5,
            )
        )

        self.__surface.blit(text, text_center_cors)

    def blit(self, surface: SurfaceType, x: int = 0, y: int = 0):
        self.__coordinates = (x, y)
        surface.blit(self.__surface, (x, y))


if __name__ == "__main__":
    screen = Screen("test button!")
    topleft = screen.screen.get_rect().topleft
    button = Button("PlayButton.png", topleft)
    button.insert_text("O", 30, "yellow")
    button.blit(screen.screen)

    button2 = Button("PlayButton.png", topleft)
    button2.insert_text("X", 30, "yellow")
    button2.blit(screen.screen, y=150)

    button3 = Button("PlayButton.png", topleft)
    button3.insert_text("", 30, "yellow")
    button3.blit(screen.screen, y=300)
    screen.init()
