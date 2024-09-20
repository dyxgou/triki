from pygame import SurfaceType
import pygame
from sys import exit

from settings import BACKGROUND_PATH, HEIGHT, WIDTH
from clock import Clock


class Screen(Clock):
    __screen: SurfaceType
    __title: str
    __background: SurfaceType
    __running: bool = True

    def __init__(self, title: str) -> None:
        Clock.__init__(self)
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background = pygame.image.load(BACKGROUND_PATH)
        self.__screen.blit(self.__background, (0, 0))
        self.__title = title

    def init(self):
        pygame.display.set_caption(self.__title)
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.tick(60)


if __name__ == "__main__":
    menu = Screen("triki!")
    menu.init()
