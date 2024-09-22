from pygame import SurfaceType, transform as image_transform


from screen import Screen
from settings import get_font, get_image
from color import ColorValue


class Button:
    __surface: SurfaceType

    def __init__(self, background_name: str) -> None:
        self.__surface = get_image(background_name)

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
        surface.blit(self.__surface, (x, y))

    def on_click(self):
        pass


if __name__ == "__main__":
    screen = Screen("test button!")
    button = Button("PlayButton.png")
    button.insert_text("O", 30, "yellow")
    button.blit(screen.screen)

    button2 = Button("PlayButton.png")
    button2.insert_text("X", 30, "yellow")
    button2.blit(screen.screen, y=150)

    button3 = Button("PlayButton.png")
    button3.insert_text("", 30, "yellow")
    button3.blit(screen.screen, y=300)
    screen.init()
