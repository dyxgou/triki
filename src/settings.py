import pygame
from pathlib import Path

# Definimos la ruta de los activos (assets) dentro del directorio principal
assets = Path("..") / "assets"

# Dimensiones de la ventana del juego
WIDTH = 1280
HEIGHT = 853

# Dimensiones y espaciado de los botones
BUTTON_WIDTH = 130
BUTTON_HEIGHT = 105
PADDING = 20

def get_font(size: int):
    """
    Carga una fuente personalizada desde el archivo "font.ttf" ubicado en la carpeta de assets.

    Args:
        size (int): Tamaño de la fuente en puntos.

    Returns:
        pygame.font.Font: Objeto de fuente cargado.
    """

    pygame.font.init()
    font_path = assets / "font.ttf"
    return pygame.font.Font(font_path, size)

def get_image(image_name: str):
    """
    Carga una imagen desde el directorio de assets y la convierte a un formato compatible con Pygame.

    Args:
        image_name (str): Nombre del archivo de la imagen (sin extensión).

    Returns:
        pygame.Surface: Superficie de Pygame que representa la imagen cargada.
    """

    image_path = assets / image_name
    return pygame.image.load(image_path).convert_alpha()
