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
    """
    Clase que representa un botón interactivo en Pygame con imágenes y texto.

    Atributos:
        __surface (SurfaceType): Superficie completa del botón compuesta por la esquina izquierda, texto e imagen de esquina derecha.
        __text_surface (SurfaceType): Superficie que contiene el texto dentro del botón.
        __right_corner (SurfaceType): Imagen que representa la esquina derecha del botón.
        __left_corner (SurfaceType): Imagen que representa la esquina izquierda del botón.
        __on_click (Optional[Callable]): Función que se ejecuta cuando el botón es clicado.
        __topleft (Coordinates): Coordenadas de la esquina superior izquierda donde se dibuja el botón.
        __coordinates (Optional[Coordinates]): Coordenadas actuales del botón en la superficie donde fue renderizado.
    """

    def __init__(self, topleft: Coordinates) -> None:
        """
        Inicializa un nuevo botón con imágenes predefinidas.

        Argumentos:
            topleft (Coordinates): Coordenadas de la esquina superior izquierda donde se posicionará el botón.
        """
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
        """
        Dibuja el texto junto con las esquinas izquierda y derecha del botón sobre la superficie del botón.
        """
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
        """
        Verifica si el cursor del mouse está sobre el botón.

        Args:
            mouse_pos (Coordinates): Posición actual del mouse.

        Raises:
            ButtonNotRederedException: Si el botón aún no ha sido renderizado en la pantalla.

        Returns:
            bool: Verdadero si el mouse está sobre el botón, Falso en caso contrario.
        """
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
        """
        Propiedad getter para obtener la función asociada a la acción de clic del botón.

        Returns:
            Optional[Callable]: Función a ejecutar cuando el botón es clicado.
        """
        self.__on_click = None
        return self.__on_click

    @on_click.setter
    def on_click(self, on_click: Callable):
        """
        Propiedad setter para asignar una función que se ejecutará cuando el botón sea clicado.

        Args:
            on_click (Callable): Función a ejecutar al hacer clic en el botón.
        """
        self.__on_click = on_click

    def click(self):
        """
        Ejecuta la función `on_click` si existe cuando se hace clic en el botón.
        """
        if self.__on_click is None:
            return

        self.__on_click()

    @property
    def surface(self):
        """
        Propiedad getter que devuelve la superficie del botón.

        Returns:
            SurfaceType: Superficie que contiene el botón.
        """
        return self.__surface

    def insert_text(
        self, text_content: str, size: int = 16, color: ColorValue = "white"
    ):
        """
        Inserta el texto dentro del área de texto del botón.

        Args:
            text_content (str): Texto que se mostrará en el botón.
            size (int): Tamaño de la fuente del texto.
            color (ColorValue): Color del texto.
        """
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
        """
        Dibuja el botón en una superficie de Pygame.

        Args:
            surface (SurfaceType): Superficie donde se renderizará el botón.
            x (int): Posición X en la superficie.
            y (int): Posición Y en la superficie.
        """
        self.__coordinates = (x, y)
        surface.blit(self.__surface, (x, y))


if __name__ == "__main__":
    """
    Bloque principal que ejecuta una pantalla de prueba para ver el comportamiento de los botones.
    """
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
