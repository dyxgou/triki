from typing import Callable, Optional
from pygame.event import Event
from pygame import MOUSEBUTTONDOWN, SurfaceType
import pygame
from sys import exit


from settings import HEIGHT, WIDTH, get_font, get_image
from errors import screen_errors
from clock import Clock

EventHandler = Callable[[Event], None]


class Screen(Clock):
    __screen: SurfaceType
    __title: str
    __background: SurfaceType
    __running: bool = True
    __on_click: Optional[EventHandler] = None

    @property
    def on_click(self):
        return self.__on_click

    @on_click.setter
    def on_click(self, new_on_click: EventHandler):
        self.__on_click = new_on_click

    def __init__(self, title: str) -> None:
        Clock.__init__(self)
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background = get_image("Background.png")
        self.__screen.blit(self.__background, (0, 0))
        self.__title = title

    @property
    def screen(self):
        return self.__screen

    def init(self):
        if self.__on_click is None:
            raise screen_errors.UndefinedClickException(
                "El click handler no ha sido definido."
            )

        pygame.display.set_caption(self.__title)

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    pygame.quit()
                    exit()

                self.__on_click(event)

            pygame.display.update()
            self.tick(30)


if __name__ == "__main__":
    menu = Screen("Triki!")

    def on_click(event: Event):
        if event.type == MOUSEBUTTONDOWN:
            print("click!")

    menu.on_click = on_click
    surface = pygame.Surface((500, 500))
    surface.fill((0, 0, 200))

    font = get_font(18)
    button_img = get_image("TextButton.png")
    text = font.render("start", True, "yellow")
    text_center_cors = text.get_rect(
        center=(
            button_img.get_width() // 2,
            button_img.get_height() // 2 - 10,
        )
    )

    button_img.blit(text, text_center_cors)
    center_cors = surface.get_rect(
        center=(
            menu.screen.get_width() // 2,
            menu.screen.get_height() // 2,
        )
    )

    surface.blit(
        button_img,
        (
            0,
            0,
        ),
    )

    menu.screen.blit(surface, center_cors)
    menu.init()
