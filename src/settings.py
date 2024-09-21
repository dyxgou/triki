import pygame
from pathlib import Path

assets = Path("..") / "assets"

HEIGHT = 700
WIDTH = 1100

BACKGROUND_PATH = assets / "Background.png"
TRICKYBUTTONSTART_PATH = "assets/StartButton.png"
TRICKYBUTTONEXIT_PATH = "assets/ExitButton.png"
TRICKYGRID_PATH = "assets/TrickyGrid.png"
TRICKYPLAYBUTTON_PATH = "assets/PlayButton.png"
TRICKYX_PATH = "assets/TrickyX.png"
TRICKYO_PATH = "assets/TrickyO.png"


def get_font(size: int):
    pygame.font.init()
    font_path = assets / "font.ttf"
    return pygame.font.Font(font_path, size)


def get_image(image_name: str):
    """
    image_name : str -> El nombre de la imagen (Ejemplo : Background.png)
    Ésta function retorna la imagen cargada en pygame.
    """
    image_path = assets / image_name
    return pygame.image.load(image_path)
