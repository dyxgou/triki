import pygame
from pathlib import Path

assets = Path("..") / "assets"

WIDTH = 1280
HEIGHT = 853


BUTTON_WIDTH = 130
BUTTON_HEIGHT = 105
PADDING = 20


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
    return pygame.image.load(image_path).convert_alpha()
